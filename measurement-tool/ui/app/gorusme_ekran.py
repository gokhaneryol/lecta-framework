"""Madde ekranları (TASARIM.md §5.2/3): madde başına bir ekran, otomatik kayıt, skip, tespit satırı.

Kayıt madde düzeyinde sürüm kontrolüyle yapılır: aynı birim dosyasında başka bir maddeyi
düzenleyen kişi çakışma yaratmaz; aynı madde o arada değiştiyse kayıt reddedilir (§5.3).
"""
import re
import threading
import time

from markupsafe import Markup, escape
from flask import Blueprint, abort, current_app, g, make_response, redirect, render_template, request, url_for

from . import gorusme, kayit
from .depo import Cakisma, parca_surumu

bp = Blueprint('gorusme', __name__)
VARLIK_SURE = 120          # sn: aynı birimde başka kullanıcı "şu an burada" sayılır
_varlik, _varlik_kilit = {}, threading.Lock()


@bp.app_template_filter('kalin')
def kalin(s):
    """kontrol.check_line'ın **[eşik]** işaretini <strong>'a çevirir; geri kalanı kaçışlanır."""
    return Markup(re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', str(escape(s))))


def depo():
    return current_app.extensions['depo']


def varlik(did, birim):
    """Bu birimde son VARLIK_SURE saniyede görülen diğer kullanıcılar; çağıranı da kaydeder."""
    simdi = time.time()
    with _varlik_kilit:
        d = _varlik.setdefault((did, birim), {})
        d[g.kullanici] = simdi
        return sorted(k for k, t in d.items() if k != g.kullanici and simdi - t < VARLIK_SURE)


def baglam(did, birim_id, madde_id):
    if not kayit.KIMLIK.match(did):
        abort(404)
    dg, _ = depo().oku(did, 'degerlendirme.yaml')
    if dg is None:
        abort(404)
    birimler = gorusme.birimler(dg)
    bulunan = gorusme.bul(birimler, birim_id, madde_id)
    if bulunan is None:
        abort(404)
    birim, madde, seviye, onceki, sonraki = bulunan
    veri, _ = depo().oku(did, 'cevaplar', f'{birim_id}.yaml')
    return dict(dg=dg, birimler=birimler, birim=birim, madde=madde, seviye=seviye, onceki=onceki,
                sonraki=sonraki, veri=veri or {})


def durumlar(did, birimler, haric=None):
    """{(birim, madde): durum} — sol menü için. haric: (birim, veri) zaten okunmuşsa."""
    out = {}
    for b in birimler:
        veri = haric[1] if haric and haric[0] == b['id'] else (depo().oku(did, 'cevaplar', f"{b['id']}.yaml")[0] or {})
        for m, _ in b['maddeler']:
            blok = veri.get(m['id'])
            out[(b['id'], m['id'])] = gorusme.madde_durumu(m, gorusme.tamamla(m, blok) if blok else None)
    return out


def madde_url(hedef, did):
    return url_for('gorusme.madde', did=did, birim=hedef[0], madde_id=hedef[1]) if hedef else url_for('ekran.kapsam', did=did)


# ------------------------------------------------------------------ ekranlar
@bp.get('/d/<did>/gorusme')
def baslat(did):
    """İlk tamamlanmamış maddeye; hepsi tamamsa ilk maddeye."""
    if not kayit.KIMLIK.match(did):
        abort(404)
    dg, _ = depo().oku(did, 'degerlendirme.yaml')
    if dg is None:
        abort(404)
    birimler = gorusme.birimler(dg)
    if not birimler:
        return redirect(url_for('ekran.kapsam', did=did))
    d = durumlar(did, birimler)
    hedef = next((k for k, v in d.items() if v != 'tamam'), next(iter(d)))
    return redirect(madde_url(hedef, did))


@bp.get('/d/<did>/m/<birim>/<madde_id>')
def madde(did, birim, madde_id):
    b = baglam(did, birim, madde_id)
    blok_ham = b['veri'].get(madde_id)
    blok = gorusme.tamamla(b['madde'], blok_ham)
    return render_template('madde.html', **b, did=did, blok=blok, surum=parca_surumu(blok_ham),
                           satirlar=gorusme.kontrol_satirlari(b['madde'], blok),
                           tespit=gorusme.tespit(b['madde'], blok, b['dg']['ref_date']),
                           terimler=gorusme.terimler(b['madde']), metin=gorusme.metin,
                           durumlar=durumlar(did, b['birimler'], (birim, b['veri'])),
                           durum_etiket=gorusme.DURUM_ETIKET, digerleri=varlik(did, birim),
                           duzenlenebilir=kayit.duzenlenebilir(b['dg']),
                           onceki_url=madde_url(b['onceki'], did), sonraki_url=madde_url(b['sonraki'], did))


def _yaz(did, b, degisiklik):
    """Madde bloğunu kilit altında, madde sürümünü denetleyerek yazar. Dönüş: (eski, yeni).

    kapanis=1: sayfa kapanırken gönderilen son kayıt. O sırada yolda olan bir otomatik kayıtla aynı
    sürüme dayanabilir; madde en son aynı kullanıcı tarafından değiştirildiyse çakışma sayılmaz.
    """
    madde_id, beklenen, sonuc = b['madde']['id'], request.form.get('surum', ''), {}
    kapanis = request.form.get('kapanis') == '1'
    sira = [m['id'] for m, _ in b['birim']['maddeler']]

    def fn(veri):
        veri = dict(veri or {})
        eski = veri.get(madde_id)
        kendi = kapanis and eski and (eski.get('guncelleme') or {}).get('kim') == g.kullanici
        if parca_surumu(eski) != beklenen and not kendi:
            raise Cakisma(madde_id, beklenen, parca_surumu(eski))
        yeni = degisiklik(eski)
        if eski and {k: v for k, v in eski.items() if k != 'guncelleme'} == yeni:
            yeni = eski                                      # içerik aynı: sürüm değişmesin
        else:
            yeni['guncelleme'] = dict(kim=g.kullanici, zaman=kayit.simdi())
        veri[madde_id] = yeni
        sonuc.update(eski=eski, yeni=yeni)
        return {k: veri[k] for k in sorted(veri, key=lambda k: (sira.index(k) if k in sira else len(sira), k))}

    veri = depo().degistir(fn, did, 'cevaplar', f"{b['birim']['id']}.yaml")
    return sonuc['eski'], sonuc['yeni'], veri


def _yanit(did, b, eski, yeni, veri, mesaj, satirlar_yenile):
    madde = b['madde']
    blok = gorusme.tamamla(madde, yeni)
    satirlar = gorusme.kontrol_satirlari(madde, blok)
    parcalar = [
        render_template('_surum.html', id='m-surum', surum=parca_surumu(yeni)),
        render_template('_durum.html', hedef='m-durum', mesaj=mesaj),
        render_template('_tespit.html', tespit=gorusme.tespit(madde, blok, b['dg']['ref_date']), oob=True),
        render_template('_nav_madde.html', did=did, birim=b['birim'], m=madde, oob=True,
                        durum=gorusme.madde_durumu(madde, blok), durum_etiket=gorusme.DURUM_ETIKET,
                        aktif=True),
        render_template('_varlik.html', digerleri=varlik(did, b['birim']['id']), oob=True),
        render_template('_madde_durum.html', durum=gorusme.madde_durumu(madde, blok),
                        durum_etiket=gorusme.DURUM_ETIKET, oob=True),
    ]
    for s in satirlar:
        if s['id'] in satirlar_yenile:
            parcalar.append(render_template('_kontrol.html', s=s, blok=blok, oob=True, duzenlenebilir=True))
        else:
            parcalar.append(render_template('_rozet.html', s=s, oob=True))
    if satirlar_yenile:            # c1 değişti: gerekçe alanı açılır/kapanır
        parcalar.append(render_template('_na.html', blok=blok, oob=True))
    elif gorusme.c1_kapatir(blok) == gorusme.NA:     # yazarken alan yeniden çizilmez, yalnız uyarı
        parcalar.append(render_template('_na_uyari.html', blok=blok, oob=True))
    return ''.join(parcalar)


def _hata(mesaj):
    return render_template('_durum.html', hedef='m-durum', mesaj=mesaj, hata=True)


@bp.post('/d/<did>/m/<birim>/<madde_id>')
def kaydet(did, birim, madde_id):
    b = baglam(did, birim, madde_id)
    if not kayit.duzenlenebilir(b['dg']):
        return _hata('Değerlendirme taslak değil; değiştirilemez.')
    try:
        eski, yeni, veri = _yaz(did, b, lambda e: gorusme.formdan(b['madde'], e, request.form))
    except gorusme.Gecersiz as e:
        return _hata(str(e))
    except Cakisma:
        return _hata('Bu madde o arada başka biri tarafından değiştirildi. Sayfayı yenileyin; son değişikliğiniz kaydedilmedi.')
    c1_degisti = gorusme.c1_durumu(gorusme.tamamla(b['madde'], eski)) != gorusme.c1_durumu(gorusme.tamamla(b['madde'], yeni))
    yenile = _bagimlilar(b['madde']) if c1_degisti else []
    return _yanit(did, b, eski, yeni, veri, 'Kaydedildi ' + kayit.simdi()[11:19], yenile)


@bp.post('/d/<did>/m/<birim>/<madde_id>/atla')
def atla(did, birim, madde_id):
    """kontrol verilirse o kontrol, verilmezse maddenin cevaplanmamış kontrolleri "sonra döneceğim"."""
    b = baglam(did, birim, madde_id)
    if not kayit.duzenlenebilir(b['dg']):
        return _hata('Değerlendirme taslak değil; değiştirilemez.')
    kid = request.form.get('kontrol') or None
    if kid and kid not in {c['id'] for c in gorusme.qs_kontrolleri(b['madde'])}:
        abort(400)
    try:
        eski, yeni, veri = _yaz(did, b, lambda e: gorusme.atla(b['madde'], e, kid))
    except Cakisma:
        return _hata('Bu madde o arada başka biri tarafından değiştirildi. Sayfayı yenileyin.')
    if kid is None:
        r = make_response('')
        r.headers['HX-Redirect'] = madde_url(b['sonraki'], did)
        return r
    # c1 atlanınca diğerleri de kapanır (K4): hepsi yeniden çizilir
    yenile = [kid] + (_bagimlilar(b['madde']) if kid == 'c1' else [])
    return _yanit(did, b, eski, yeni, veri, f'{kid} atlandı; kapanışta eksikler listesinde görünecek', yenile)


def _bagimlilar(madde):
    """c1'e bağlı (varlık dışı) kontroller."""
    return [c['id'] for c in gorusme.qs_kontrolleri(madde) if c['kind'] != 'exist']
