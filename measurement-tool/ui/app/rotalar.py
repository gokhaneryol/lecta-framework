"""Ekranlar: değerlendirme listesi, yeni değerlendirme, kurum ve kapsam (TASARIM.md §5.2/1–2).

Alan değişikliği htmx ile anında kaydedilir (K9). Yanıt ana içeriği değiştirmez (hx-swap="none");
yalnız sürüm alanını ve durum satırını out-of-band günceller, böylece odak kaybolmaz.
Sürüm uyuşmazsa (başkası değiştirdi) kayıt reddedilir ve "yenile" mesajı gösterilir (§5.3).
"""
import datetime as dt
import os

from flask import (Blueprint, abort, current_app, g, redirect, render_template, request, send_file,
                   url_for)

from . import framework, kayit
from .depo import Cakisma

bp = Blueprint('ekran', __name__)


def depo():
    return current_app.extensions['depo']


def commit():
    return current_app.config['LECTA_FRAMEWORK_COMMIT']


def yukle(did):
    if not kayit.KIMLIK.match(did):
        abort(404)
    dg, dg_s = depo().oku(did, 'degerlendirme.yaml')
    if dg is None:
        abort(404)
    kurum, kurum_s = depo().oku(did, 'kurum.yaml')
    return dg, dg_s, kurum, kurum_s


def cevap_var(did, sid):
    return os.path.exists(depo().yol(did, 'cevaplar', f'{sid}.yaml'))


def durum(hedef, mesaj, hata=False):
    return render_template('_durum.html', hedef=hedef, mesaj=mesaj, hata=hata)


def cakisma(hedef):
    return durum(hedef, 'Bu kayıt o arada başka biri tarafından değiştirildi. Sayfayı yenileyin; '
                        'girdiğiniz değer kaydedilmedi.', hata=True)


def kaydedildi(hedef):
    return durum(hedef, 'Kaydedildi ' + dt.datetime.now(kayit.TZ).strftime('%H:%M:%S'))


# ------------------------------------------------------------------ liste ve açma
@bp.get('/')
def degerlendirmeler():
    return render_template('degerlendirmeler.html', liste=kayit.liste(depo()))


@bp.route('/yeni', methods=['GET', 'POST'])
def yeni():
    form = request.form if request.method == 'POST' else dict(ref_date=dt.date.today().isoformat(), servis='AS-01')
    hatalar = []
    if request.method == 'POST':
        try:
            did = kayit.ac(depo(), request.form, g.kullanici, commit())
            return redirect(url_for('ekran.kapsam', did=did), code=303)
        except kayit.Hata as e:
            hatalar = e.mesajlar
    return render_template('yeni.html', form=form, hatalar=hatalar, servisler=list(kayit.SERVIS))


# ------------------------------------------------------------------ kurum ve kapsam
@bp.get('/d/<did>/')
def kapsam(did):
    dg, dg_s, kurum, kurum_s = yukle(did)
    uyari = (dg['framework'].get('commit') not in (commit(), 'dev') and commit() != 'dev')
    return render_template('kapsam.html', dg=dg, dg_s=dg_s, kurum=kurum, kurum_s=kurum_s,
                           alanlar=framework.org_fields(), duzenlenebilir=kayit.duzenlenebilir(dg),
                           commit_uyari=uyari, en_cok=kayit.QS_EN_COK_SISTEM,
                           cevapli={s['id'] for s in dg['sistemler'] if cevap_var(did, s['id'])})


@bp.post('/d/<did>/kurum')
def kurum_kaydet(did):
    dg, _, kurum, _ = yukle(did)
    if not kayit.duzenlenebilir(dg):
        return durum('kurum-durum', 'Değerlendirme taslak değil; değiştirilemez.', hata=True)
    try:
        yeni = kayit.kurum_guncelle(kurum, request.form)
        s = depo().yaz(yeni, did, 'kurum.yaml', beklenen=request.form.get('surum', ''))
    except kayit.Hata as e:
        return durum('kurum-durum', ' · '.join(e.mesajlar), hata=True)
    except Cakisma:
        return cakisma('kurum-durum')
    return render_template('_surum.html', id='kurum-surum', surum=s) + kaydedildi('kurum-durum')


@bp.post('/d/<did>/logo')
def logo_yukle(did):
    dg, _, kurum, kurum_s = yukle(did)
    if not kayit.duzenlenebilir(dg):
        return durum('kurum-durum', 'Değerlendirme taslak değil; değiştirilemez.', hata=True)
    f = request.files.get('logo')
    b = f.read() if f else b''
    try:
        kayit.logo_dogrula(b)
    except kayit.Hata as e:
        return durum('kurum-durum', ' · '.join(e.mesajlar), hata=True)
    depo().yaz_ham(b, did, 'logo.png')
    s = kurum_s
    if kurum.get('logo') != 'logo.png':
        try:
            s = depo().yaz(dict(kurum, logo='logo.png'), did, 'kurum.yaml', beklenen=kurum_s)
        except Cakisma:
            return cakisma('kurum-durum')
    return (render_template('_logo.html', did=did, kurum=dict(kurum, logo='logo.png'), oob=True)
            + render_template('_surum.html', id='kurum-surum', surum=s) + kaydedildi('kurum-durum'))


@bp.get('/d/<did>/logo.png')
def logo(did):
    _, _, kurum, _ = yukle(did)
    if not kurum.get('logo'):
        abort(404)
    r = send_file(depo().yol(did, 'logo.png'), mimetype='image/png')
    r.headers['Cache-Control'] = 'no-store'
    return r


def _dg_yaz(did, fn):
    """degerlendirme.yaml üzerinde bir değişiklik: (yanıt, yeni sürüm | None)."""
    dg, _, _, _ = yukle(did)
    try:
        yeni = fn(dg)
        return None, depo().yaz(yeni, did, 'degerlendirme.yaml', beklenen=request.form.get('surum', ''))
    except kayit.Hata as e:
        return durum('kapsam-durum', ' · '.join(e.mesajlar), hata=True), None
    except Cakisma:
        return cakisma('kapsam-durum'), None


@bp.post('/d/<did>/ayar')
def ayar_kaydet(did):
    hata, s = _dg_yaz(did, lambda dg: kayit.ayar_guncelle(dg, request.form, g.kullanici))
    return hata or render_template('_surum.html', id='dg-surum', surum=s) + kaydedildi('kapsam-durum')


@bp.post('/d/<did>/sistem/<sid>')
def sistem_kaydet(did, sid):
    hata, s = _dg_yaz(did, lambda dg: kayit.sistem_guncelle(dg, sid, request.form, cevap_var(did, sid)))
    return hata or render_template('_surum.html', id='dg-surum', surum=s) + kaydedildi('kapsam-durum')


@bp.post('/d/<did>/sistem')
def sistem_ekle(did):
    hata, _ = _dg_yaz(did, lambda dg: kayit.sistem_ekle(dg, request.form))
    return hata or _sistemler(did, 'Sistem eklendi')


@bp.post('/d/<did>/sistem/<sid>/sil')
def sistem_sil(did, sid):
    hata, _ = _dg_yaz(did, lambda dg: kayit.sistem_sil(dg, sid, cevap_var(did, sid)))
    return hata or _sistemler(did, 'Sistem silindi')


def _sistemler(did, mesaj):
    """Yapı değiştiğinde sistem bölümü baştan çizilir (hx-swap-oob), sürüm alanıyla birlikte."""
    dg, dg_s, _, _ = yukle(did)
    return (render_template('_sistemler.html', dg=dg, duzenlenebilir=kayit.duzenlenebilir(dg),
                            en_cok=kayit.QS_EN_COK_SISTEM, oob=True,
                            cevapli={s['id'] for s in dg['sistemler'] if cevap_var(did, s['id'])})
            + render_template('_surum.html', id='dg-surum', surum=dg_s) + durum('kapsam-durum', mesaj))
