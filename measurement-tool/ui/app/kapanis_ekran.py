"""Kapanış, inceleme ve sonuç ekranları (TASARIM.md §5.2/4–6, K6).

Akış sıralıdır: değerlendirici kapanışta eksikleri görüp incelemeye gönderir; gözden geçiren her maddeye
"katılıyorum / katılmıyorum + yorum" verir, sonra kapatır ya da geri gönderir. Her geçişte cikti/ yeniden
üretilir ve değerlendirme deposuna yerel commit atılır.
"""
import os

from flask import Blueprint, abort, current_app, g, redirect, render_template, request, send_file, url_for

from . import cikti, gorusme, kayit
from .framework import qs

bp = Blueprint('kapanis', __name__)
CIKTILAR = {'qs.csv': 'text/csv', 'seviye.md': 'text/markdown', 'kaynak.yaml': 'text/yaml'}


def depo():
    return current_app.extensions['depo']


def yukle(did):
    if not kayit.KIMLIK.match(did):
        abort(404)
    dg, _ = depo().oku(did, 'degerlendirme.yaml')
    if dg is None:
        abort(404)
    kurum, _ = depo().oku(did, 'kurum.yaml')
    return dg, kurum


def commit_at(did, mesaj):
    """Değişiklik varsa değerlendirme deposuna yerel commit (§5.4). Dönüş: commit atıldı mı."""
    yol = depo().yol(did)
    if not kayit.git(yol, 'status', '--porcelain').strip():
        return False
    kayit.git_commit(yol, mesaj, g.kullanici)
    return True


def _gecis(did, ne):
    """degerlendirme.yaml'da kilit altında durum geçişi; sonra çıktılar ve commit."""
    dg = depo().degistir(lambda dg: cikti.gecis(dg, ne, g.kullanici), did, 'degerlendirme.yaml')
    _, kurum = yukle(did)
    cikti.ciktilari_yaz(depo(), did, dg, kurum, g.kullanici)
    commit_at(did, {'incelemeye-gonderildi': 'Kapanış: incelemeye gönderildi',
                    'kapandi': 'İnceleme bitti: değerlendirme kapandı',
                    'geri-gonderildi': 'İnceleme: değerlendiriciye geri gönderildi'}[ne] + f' ({g.kullanici})')
    return dg


# ------------------------------------------------------------------ kapanış
@bp.route('/d/<did>/kapanis', methods=['GET', 'POST'])
def kapanis(did):
    dg, kurum = yukle(did)
    hata = None
    if request.method == 'POST':
        try:
            _gecis(did, 'incelemeye-gonderildi')
            return redirect(url_for('kapanis.inceleme', did=did), code=303)
        except cikti.Gecis as e:
            hata = str(e)
            dg, kurum = yukle(did)
    return render_template('kapanis.html', dg=dg, kurum=kurum, sekme='kapanis', hata=hata,
                           eksikler=cikti.eksikler(depo(), did, dg), durum_etiket=gorusme.DURUM_ETIKET,
                           yetkili=(dg['durum'] == 'taslak' and g.kullanici == dg['degerlendirici']))


# ------------------------------------------------------------------ inceleme
def _inceleme_baglam(did, dg, kurum, hata=None):
    satirlar = cikti.incelemeler(depo(), did, dg)
    return dict(dg=dg, kurum=kurum, sekme='inceleme', hata=hata, satirlar=satirlar,
                uyusmazlik=[s for s in satirlar if s['inceleme'].get('karar') == 'katilmiyor'],
                kararsiz=sum(1 for s in satirlar if not s['inceleme'].get('karar')),
                yetkili=(dg['durum'] == 'incelemede' and g.kullanici == dg.get('gozden_geciren')),
                durum_etiket=gorusme.DURUM_ETIKET)


@bp.get('/d/<did>/inceleme')
def inceleme(did):
    dg, kurum = yukle(did)
    return render_template('inceleme.html', **_inceleme_baglam(did, dg, kurum))


@bp.post('/d/<did>/inceleme/<birim>/<madde_id>')
def inceleme_kaydet(did, birim, madde_id):
    dg, kurum = yukle(did)
    if dg['durum'] != 'incelemede' or g.kullanici != dg.get('gozden_geciren'):
        return render_template('_durum.html', hedef='inceleme-durum', mesaj='Bu maddeye yalnız gözden geçiren, inceleme sırasında karar verir.', hata=True)
    bulunan = gorusme.bul(gorusme.birimler(dg), birim, madde_id)
    if bulunan is None:
        abort(404)
    madde = bulunan[1]
    karar = request.form.get('karar', '')
    if karar not in ('katiliyor', 'katilmiyor', ''):
        abort(400)

    def fn(veri):
        veri = dict(veri or {})
        veri[madde_id] = cikti.inceleme_karari(madde, veri.get(madde_id), karar, request.form.get('yorum', ''), g.kullanici)
        return veri

    depo().degistir(fn, did, 'cevaplar', f'{birim}.yaml')
    b = _inceleme_baglam(did, dg, kurum)
    return (render_template('_inceleme_ozet.html', **b, oob=True)
            + render_template('_durum.html', hedef='inceleme-durum', mesaj='Kaydedildi ' + kayit.simdi()[11:19]))


@bp.post('/d/<did>/inceleme/bitir')
def inceleme_bitir(did):
    dg, kurum = yukle(did)
    b = _inceleme_baglam(did, dg, kurum)
    if b['kararsiz']:
        return render_template('inceleme.html', **dict(b, hata=f"{b['kararsiz']} maddede karar yok; kapatmadan önce hepsine karar verin."))
    try:
        _gecis(did, 'kapandi')
    except cikti.Gecis as e:
        return render_template('inceleme.html', **dict(b, hata=str(e)))
    return redirect(url_for('kapanis.sonuc', did=did), code=303)


@bp.post('/d/<did>/inceleme/geri')
def inceleme_geri(did):
    dg, kurum = yukle(did)
    try:
        _gecis(did, 'geri-gonderildi')
    except cikti.Gecis as e:
        return render_template('inceleme.html', **_inceleme_baglam(did, dg, kurum, hata=str(e)))
    return redirect(url_for('ekran.kapsam', did=did), code=303)


# ------------------------------------------------------------------ sonuç
@bp.get('/d/<did>/sonuc')
def sonuc(did):
    dg, kurum = yukle(did)
    rows, h = cikti.sonuc(depo(), did, dg, kurum)
    birim_id = {s['ad']: s['id'] for s in dg['sistemler']}
    bid = lambda r: gorusme.KURUM if r['unit_type'] == 'KURUM' else birim_id.get(r['unit'])
    dosyalar = [ad for ad in CIKTILAR if os.path.exists(depo().yol(did, 'cikti', ad))]
    return render_template('sonuc.html', dg=dg, kurum=kurum, sekme='sonuc', h=h, lvname=qs.lvname, bid=bid,
                           dosyalar=dosyalar, mesaj=request.args.get('mesaj'))


@bp.get('/d/<did>/cikti/<ad>')
def cikti_dosyasi(did, ad):
    yukle(did)
    if ad not in CIKTILAR or not os.path.exists(depo().yol(did, 'cikti', ad)):
        abort(404)
    return send_file(depo().yol(did, 'cikti', ad), mimetype=CIKTILAR[ad], as_attachment=True,
                     download_name=f'{did}-{ad}', max_age=0)


@bp.post('/d/<did>/goruntu')
def goruntu(did):
    """Anlık görüntü: o anki durumu değerlendirme deposuna commit eder (§5.4)."""
    yukle(did)
    atildi = commit_at(did, f'Anlık görüntü ({g.kullanici})')
    return redirect(url_for('kapanis.sonuc', did=did, mesaj='Anlık görüntü alındı.' if atildi else 'Son görüntüden beri değişiklik yok.'), code=303)
