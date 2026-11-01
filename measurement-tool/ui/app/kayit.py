"""Değerlendirme dizini: açma, kurum ve kapsam kayıtları (TASARIM.md §4).

Ekrandan bağımsızdır; form sözlüğü alır, hata listesi ya da yazılacak veriyi döndürür.
Dosyaya yazma Depo üzerinden, sürüm kontrolüyle yapılır.
"""
import datetime as dt
import os
import re
import shutil
import subprocess
from zoneinfo import ZoneInfo

from . import framework

KIMLIK = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
SERVIS = {'AS-01': 'as01'}          # akış yalnız QS (K3)
PROFILLER = ('CE', 'SOV')
QS_EN_COK_SISTEM = 2
AYRILMIS = {'kurum'}                # cevaplar/KURUM.yaml ile çakışmasın (büyük/küçük harf duyarsız dosya sistemleri)
LOGO_EN_BUYUK = 512 * 1024
PNG = b'\x89PNG\r\n\x1a\n'
TZ = ZoneInfo('Europe/Istanbul')
SABLON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sablon')
_TR = str.maketrans('çğıöşüâîûÇĞİÖŞÜÂÎÛ', 'cgiosuaiuCGIOSUAIU')


class Hata(Exception):
    """Kullanıcıya gösterilecek doğrulama hataları."""

    def __init__(self, *mesajlar):
        super().__init__('; '.join(mesajlar))
        self.mesajlar = list(mesajlar)


def simdi():
    return dt.datetime.now(TZ).isoformat(timespec='seconds')


def kimlik_uret(metin):
    s = re.sub(r'[^a-z0-9]+', '-', metin.translate(_TR).lower()).strip('-')
    return s[:30].strip('-')


ETIKET = dict(ad_tam='Tam ad', ad_kisa='Kısa ad', ad='Ad', aciklama='Açıklama',
              saglayici='Sağlayıcı', gozden_geciren='Gözden geçiren', sector='Sektör',
              employee_band='Çalışan sayısı', ai_use='AI kullanım alanları', iletisim='Görüşme katılımcıları')


def _metin(form, ad, zorunlu=False, en_cok=200):
    v = ' '.join(str(form.get(ad, '')).split())
    if zorunlu and not v:
        raise Hata(f'{ETIKET.get(ad, ad)} boş olamaz')
    if len(v) > en_cok:
        raise Hata(f'{ETIKET.get(ad, ad)} en çok {en_cok} karakter')
    return v


# ------------------------------------------------------------------ liste
def liste(depo):
    out = []
    for d in sorted(os.listdir(depo.kok)):
        dg, _ = depo.oku(d, 'degerlendirme.yaml') if os.path.isdir(depo.yol(d)) else (None, None)
        if not dg:
            continue
        kurum, _ = depo.oku(d, 'kurum.yaml')
        out.append(dict(id=d, kurum=(kurum or {}).get('ad', {}).get('tam', ''), servis=dg.get('servis'),
                        durum=dg.get('durum'), degerlendirici=dg.get('degerlendirici'),
                        sistem=len(dg.get('sistemler') or []), ref_date=dg.get('ref_date')))
    return out


# ------------------------------------------------------------------ açma
def ac(depo, form, kullanici, commit, kullanicilar=()):
    """Yeni değerlendirme dizini: şablon + kurum.yaml + degerlendirme.yaml + git init. Dönüş: id.

    Kurum kimliği kısa addan üretilir (Örnek Banka → ornek-banka); değerlendirme kimliği
    <kurum>-<yıl>-<servis>. Aynı kimlik varsa kuruma -2, -3 … eklenir.
    """
    tam = _metin(form, 'ad_tam', True)
    kisa = _metin(form, 'ad_kisa', True, 60)
    temel = re.sub(r'-(as\d\d|(19|20)\d\d)$', '', re.sub(r'-(as\d\d|(19|20)\d\d)$', '', kimlik_uret(kisa)))
    if not temel:
        raise Hata('Kısa addan kimlik üretilemedi; en az bir harf ya da rakam içermeli')
    servis = form.get('servis', 'AS-01')
    if servis not in SERVIS:
        raise Hata(f'Servis desteklenmiyor: {servis}')
    ref = _tarih(form.get('ref_date', ''))
    gozden = _gozden_geciren(form, kullanici, kullanicilar)
    kisa_id, n = temel, 2
    while os.path.exists(depo.yol(f'{kisa_id}-{ref.year}-{SERVIS[servis]}')):
        kisa_id, n = f'{temel}-{n}', n + 1
    did = f'{kisa_id}-{ref.year}-{SERVIS[servis]}'
    hedef = depo.yol(did)
    try:
        shutil.copytree(SABLON, hedef)
    except FileExistsError:
        raise Hata(f'{did} aynı anda başka biri tarafından açıldı; tekrar deneyin')
    try:
        depo.yaz(dict(id=kisa_id, ad=dict(tam=tam, kisa=kisa), logo=None, sector=None, employee_band=None,
                      ai_use=[], olgular={}, iletisim=[]),
                 did, 'kurum.yaml', beklenen='')
        depo.yaz(dict(id=did, servis=servis, framework=dict(surum=framework.surum(), commit=commit),
                      ref_date=ref, durum='taslak', degerlendirici=kullanici, gozden_geciren=gozden,
                      sistemler=[], oturum_notu='',
                      olaylar=[dict(ne='acildi', kim=kullanici, zaman=simdi())]),
                 did, 'degerlendirme.yaml', beklenen='')
        git(hedef, 'init', '-q', '-b', 'main')
        git_commit(hedef, f'Değerlendirme açıldı: {did}', kullanici)
    except BaseException:
        shutil.rmtree(hedef, ignore_errors=True)
        raise
    return did


def git(dizin, *args):
    return subprocess.run(['git', '-C', dizin, *args], check=True, capture_output=True, text=True).stdout


def git_commit(dizin, mesaj, kullanici):
    git(dizin, 'add', '-A')
    git(dizin, '-c', f'user.name={kullanici}', '-c', f'user.email={kullanici}@lecta.local',
        'commit', '-q', '-m', mesaj)


def _tarih(v):
    try:
        return dt.date.fromisoformat(str(v).strip())
    except ValueError:
        raise Hata('Referans tarih YYYY-AA-GG biçiminde olmalı')


def gozden_gecirenler(kullanicilar, degerlendirici):
    """Gözden geçiren olarak seçilebilecek kullanıcılar: değerlendirici dışındakiler (K6)."""
    return [k for k in kullanicilar if k != degerlendirici]


def _gozden_geciren(form, degerlendirici, kullanicilar):
    g = _metin(form, 'gozden_geciren', en_cok=40)
    if not g:
        return ''
    if g == degerlendirici:
        raise Hata('Gözden geçiren, değerlendiriciden farklı biri olmalı')
    if kullanicilar and g not in kullanicilar:
        raise Hata(f"Gözden geçiren listeden seçilmeli ({', '.join(gozden_gecirenler(kullanicilar, degerlendirici))})")
    if not KIMLIK.match(g):
        raise Hata(f'Gözden geçiren bir kullanıcı kimliği olmalı (küçük harf, Türkçe karakter yok; ör. ayhan): {g}')
    return g


def duzenlenebilir(dg):
    return dg.get('durum') == 'taslak'


def _taslak(dg):
    if not duzenlenebilir(dg):
        raise Hata('Değerlendirme taslak değil; kurum ve kapsam değiştirilemez')


# ------------------------------------------------------------------ kurum
def kurum_guncelle(kurum, form):
    """Formdaki tanımlayıcı alanları org_fields.yaml kodlarına göre doğrular (K5). Yeni kurum sözlüğü döndürür."""
    alanlar = framework.org_fields()
    yeni = dict(kurum)
    yeni['ad'] = dict(tam=_metin(form, 'ad_tam', True), kisa=_metin(form, 'ad_kisa', True, 60))
    hatalar = []
    for ad, a in alanlar.items():
        gecerli = {o['code'] for o in a['options'] if not o.get('deprecated')}
        if a['multi']:
            secilen = [v for v in form.getlist(ad)] if hasattr(form, 'getlist') else list(form.get(ad) or [])
            if set(secilen) - gecerli:
                hatalar.append(f'{ETIKET.get(ad, ad)}: geçersiz seçim')
            # sıra org_fields sırasıdır; formdaki sıra değil
            yeni[ad] = [o['code'] for o in a['options'] if o['code'] in secilen]
        else:
            v = form.get(ad) or None
            if v is not None and v not in gecerli:
                hatalar.append(f'{ETIKET.get(ad, ad)}: geçersiz seçim')
            yeni[ad] = v
    roller = [r.strip() for r in str(form.get('iletisim', '')).split(',') if r.strip()]
    if any(len(r) > 60 for r in roller):
        hatalar.append('Görüşme katılımcıları: rol en çok 60 karakter')
    yeni['iletisim'] = [dict(rol=r) for r in roller]
    if hatalar:
        raise Hata(*hatalar)
    return yeni


def logo_dogrula(b):
    if not b.startswith(PNG):
        raise Hata('Logo PNG olmalı')
    if len(b) > LOGO_EN_BUYUK:
        raise Hata(f'Logo en çok {LOGO_EN_BUYUK // 1024} KB olmalı')


# ------------------------------------------------------------------ kapsam
def ayar_guncelle(dg, form, kullanicilar=()):
    _taslak(dg)
    yeni = dict(dg)
    yeni['ref_date'] = _tarih(form.get('ref_date', ''))
    yeni['gozden_geciren'] = _gozden_geciren(form, dg['degerlendirici'], kullanicilar)
    return yeni


def sistem_ekle(dg, form):
    _taslak(dg)
    sistemler = list(dg.get('sistemler') or [])
    if len(sistemler) >= QS_EN_COK_SISTEM:
        raise Hata(f"Quick Scan'de en çok {QS_EN_COK_SISTEM} sistem")
    s = _sistem_alanlari(form)
    _ad_benzersiz(sistemler, s['ad'])
    temel = kimlik_uret(s['ad']) or 'sistem'
    if temel in AYRILMIS:
        temel += '-sistem'
    mevcut = {x['id'] for x in sistemler}
    sid, n = temel, 2
    while sid in mevcut:
        sid, n = f'{temel}-{n}', n + 1
    sistemler.append(dict(id=sid, **s))
    return dict(dg, sistemler=sistemler)


def sistem_guncelle(dg, sid, form, cevap_var):
    _taslak(dg)
    sistemler = [dict(x) for x in dg.get('sistemler') or []]
    s = next((x for x in sistemler if x['id'] == sid), None)
    if s is None:
        raise Hata(f'Sistem yok: {sid}')
    yeni = _sistem_alanlari(form)
    _ad_benzersiz([x for x in sistemler if x['id'] != sid], yeni['ad'])
    if yeni['profil'] != s['profil'] and cevap_var:
        raise Hata('Bu sistemde cevap var; profil değiştirilemez')
    s.update(yeni)
    return dict(dg, sistemler=sistemler)


def sistem_sil(dg, sid, cevap_var):
    _taslak(dg)
    if cevap_var:
        raise Hata('Bu sistemde cevap var; silinemez')
    sistemler = [x for x in dg.get('sistemler') or [] if x['id'] != sid]
    return dict(dg, sistemler=sistemler)


def _ad_benzersiz(sistemler, ad):
    # Sistem adı puanlama CSV'sinde birim anahtarıdır (qs.py seviye adla gruplar)
    if ad.casefold() in {x['ad'].casefold() for x in sistemler}:
        raise Hata(f'Bu adla bir sistem zaten var: {ad}')


def _sistem_alanlari(form):
    profil = form.get('profil', '')
    if profil not in PROFILLER:
        raise Hata('Profil CE ya da SOV olmalı')
    return dict(ad=_metin(form, 'ad', True, 80), profil=profil,
                aciklama=_metin(form, 'aciklama', en_cok=500), saglayici=_metin(form, 'saglayici', en_cok=120))
