"""Adım 3 kabulü: fixture kurum arayüzden oluşturulabiliyor; dosyalar TASARIM.md §4 biçiminde."""
import io
import os
import re
import struct
import subprocess
import zlib

import pytest
import yaml

from app import create_app
from app.depo import Depo

FIX = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fixtures', 'ornek-2026-as01')
DID = 'ornek-2026-as01'


def png(w=4, h=2):
    raw = b''.join(b'\x00' + b'\x1f\x4e\x79' * w for _ in range(h))
    ch = lambda t, d: struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d))
    return (b'\x89PNG\r\n\x1a\n' + ch(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
            + ch(b'IDAT', zlib.compress(raw)) + ch(b'IEND', b''))


@pytest.fixture
def ortam(tmp_path):
    app = create_app(dict(LECTA_DATA=str(tmp_path), LECTA_USER='gokhan', LECTA_FRAMEWORK_COMMIT='abc1234', TESTING=True))
    return app.test_client(), Depo(tmp_path)


def ac(c, **ek):
    veri = dict(kurum_id='ornek', ad_tam='Örnek Kurum A.Ş.', ad_kisa='Örnek', servis='AS-01',
                ref_date='2026-11-05', gozden_geciren='ayhan')
    veri.update(ek)
    return c.post('/yeni', data=veri)


def sistem_ekle(c, d, ad, profil='CE'):
    return c.post(f'/d/{DID}/sistem', data=dict(surum=d.surum(DID, 'degerlendirme.yaml'), ad=ad, profil=profil,
                                                aciklama='', saglayici=''))


def fixture_olustur(c, d):
    assert ac(c).status_code == 303
    r = c.post(f'/d/{DID}/kurum', data=dict(surum=d.surum(DID, 'kurum.yaml'), ad_tam='Örnek Kurum A.Ş.', ad_kisa='Örnek',
                                            sector='banking', employee_band='1000-4999',
                                            ai_use=['rag', 'ext-assistant'], iletisim='CISO'))
    assert 'Kaydedildi' in r.get_data(as_text=True)
    with open(os.path.join(FIX, 'logo.png'), 'rb') as fh:
        r = c.post(f'/d/{DID}/logo', data=dict(logo=(io.BytesIO(fh.read()), 'logo.png')), content_type='multipart/form-data')
    assert 'Kaydedildi' in r.get_data(as_text=True)
    assert 'Sistem eklendi' in sistem_ekle(c, d, 'Kurumsal Asistan', 'CE').get_data(as_text=True)
    assert 'Sistem eklendi' in sistem_ekle(c, d, 'Belge Arama', 'SOV').get_data(as_text=True)


def zamansiz(metin):
    return re.sub(r"zaman: '[^']*'", "zaman: '-'", metin)


def test_fixture_kurum_arayuzden_olusturulur(ortam, tmp_path):
    c, d = ortam
    fixture_olustur(c, d)
    for ad in ('kurum.yaml', 'degerlendirme.yaml'):
        with open(os.path.join(FIX, ad), encoding='utf-8') as fh:
            beklenen = fh.read()
        olan = (tmp_path / DID / ad).read_text(encoding='utf-8')
        assert zamansiz(olan) == zamansiz(beklenen), ad
    assert (tmp_path / DID / 'logo.png').read_bytes() == open(os.path.join(FIX, 'logo.png'), 'rb').read()
    dg = yaml.safe_load((tmp_path / DID / 'degerlendirme.yaml').read_text(encoding='utf-8'))
    assert re.match(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\+03:00$', dg['olaylar'][0]['zaman'])


def test_git_deposu_acilir_ve_kilitler_girmez(ortam, tmp_path):
    c, d = ortam
    fixture_olustur(c, d)
    git = lambda *a: subprocess.run(['git', '-C', str(tmp_path / DID), *a], capture_output=True, text=True, check=True).stdout
    assert git('log', '--format=%an %s').strip() == f'gokhan Değerlendirme açıldı: {DID}'
    durum = git('status', '--porcelain')
    assert '.lock' not in durum and '.tmp' not in durum
    assert 'README.md' in git('ls-files')


def test_listede_gorunur(ortam):
    c, d = ortam
    fixture_olustur(c, d)
    html = c.get('/').get_data(as_text=True)
    assert DID in html and 'Örnek Kurum A.Ş.' in html and 'taslak' in html


@pytest.mark.parametrize('ek, mesaj', [
    (dict(kurum_id='Örnek Kurum'), 'Kurum kimliği'),
    (dict(ad_tam=''), 'Tam ad boş olamaz'),
    (dict(ref_date='05.11.2026'), 'YYYY-AA-GG'),
    (dict(gozden_geciren='gokhan'), 'farklı biri'),
    (dict(servis='AS-02'), 'desteklenmiyor'),
])
def test_yeni_dogrulama(ortam, tmp_path, ek, mesaj):
    c, _ = ortam
    r = ac(c, **ek)
    assert r.status_code == 200 and mesaj in r.get_data(as_text=True)
    assert os.listdir(tmp_path) == []


def test_ayni_degerlendirme_iki_kez_acilmaz(ortam):
    c, _ = ortam
    ac(c)
    assert 'zaten var' in ac(c).get_data(as_text=True)


def test_gecersiz_kod_kaydedilmez(ortam):
    c, d = ortam
    ac(c)
    once = d.oku(DID, 'kurum.yaml')
    r = c.post(f'/d/{DID}/kurum', data=dict(surum=once[1], ad_tam='X', ad_kisa='X', sector='uydurma'))
    assert 'Sektör: geçersiz seçim' in r.get_data(as_text=True)
    assert d.oku(DID, 'kurum.yaml') == once


def test_eski_surumle_kayit_reddedilir(ortam):
    c, d = ortam
    ac(c)
    eski = d.surum(DID, 'kurum.yaml')
    c.post(f'/d/{DID}/kurum', data=dict(surum=eski, ad_tam='Bir', ad_kisa='Bir'))
    r = c.post(f'/d/{DID}/kurum', data=dict(surum=eski, ad_tam='İki', ad_kisa='İki'))
    assert 'başka biri tarafından değiştirildi' in r.get_data(as_text=True)
    assert d.oku(DID, 'kurum.yaml')[0]['ad']['tam'] == 'Bir'


def test_qsde_en_cok_iki_sistem_ve_kimlik_cakismasi(ortam):
    c, d = ortam
    ac(c)
    sistem_ekle(c, d, 'Asistan')
    sistem_ekle(c, d, 'Asistan', 'SOV')
    assert [s['id'] for s in d.oku(DID, 'degerlendirme.yaml')[0]['sistemler']] == ['asistan', 'asistan-2']
    assert "en çok 2 sistem" in sistem_ekle(c, d, 'Üçüncü').get_data(as_text=True)


def test_ayrilmis_kimlik_ve_gecersiz_profil(ortam):
    c, d = ortam
    ac(c)
    sistem_ekle(c, d, 'Kurum')
    assert d.oku(DID, 'degerlendirme.yaml')[0]['sistemler'][0]['id'] == 'kurum-sistem'
    assert 'CE ya da SOV' in sistem_ekle(c, d, 'X', 'GEN').get_data(as_text=True)


def test_cevabi_olan_sistem_silinemez_profili_degismez(ortam, tmp_path):
    c, d = ortam
    ac(c)
    sistem_ekle(c, d, 'Asistan')
    (tmp_path / DID / 'cevaplar').mkdir()
    (tmp_path / DID / 'cevaplar' / 'asistan.yaml').write_text('{}\n')
    s = lambda: d.surum(DID, 'degerlendirme.yaml')
    r = c.post(f'/d/{DID}/sistem/asistan', data=dict(surum=s(), ad='Asistan', profil='SOV'))
    assert 'profil değiştirilemez' in r.get_data(as_text=True)
    r = c.post(f'/d/{DID}/sistem/asistan/sil', data=dict(surum=s()))
    assert 'silinemez' in r.get_data(as_text=True)
    (tmp_path / DID / 'cevaplar' / 'asistan.yaml').unlink()
    r = c.post(f'/d/{DID}/sistem/asistan/sil', data=dict(surum=s()))
    assert 'Sistem silindi' in r.get_data(as_text=True)
    assert d.oku(DID, 'degerlendirme.yaml')[0]['sistemler'] == []


def test_ayar_kaydi(ortam):
    c, d = ortam
    ac(c)
    r = c.post(f'/d/{DID}/ayar', data=dict(surum=d.surum(DID, 'degerlendirme.yaml'), ref_date='2026-11-12', gozden_geciren=''))
    assert 'Kaydedildi' in r.get_data(as_text=True)
    dg = d.oku(DID, 'degerlendirme.yaml')[0]
    assert str(dg['ref_date']) == '2026-11-12' and dg['gozden_geciren'] == ''
    assert dg['id'] == DID       # kimlik referans tarihten türetilir ama sonradan değişmez


@pytest.mark.parametrize('icerik, mesaj', [(b'GIF89a....', 'PNG olmalı'), (b'\x89PNG\r\n\x1a\n' + b'0' * 600_000, 'en çok 512 KB')])
def test_logo_dogrulama(ortam, icerik, mesaj):
    c, d = ortam
    ac(c)
    r = c.post(f'/d/{DID}/logo', data=dict(logo=(io.BytesIO(icerik), 'x.png')), content_type='multipart/form-data')
    assert mesaj in r.get_data(as_text=True)
    assert d.oku(DID, 'kurum.yaml')[0]['logo'] is None


def test_taslak_olmayan_degisemez(ortam, tmp_path):
    c, d = ortam
    ac(c)
    dg, s = d.oku(DID, 'degerlendirme.yaml')
    d.yaz(dict(dg, durum='incelemede'), DID, 'degerlendirme.yaml', beklenen=s)
    assert 'taslak değil' in sistem_ekle(c, d, 'X').get_data(as_text=True)
    r = c.post(f'/d/{DID}/kurum', data=dict(surum=d.surum(DID, 'kurum.yaml'), ad_tam='Y', ad_kisa='Y'))
    assert 'taslak değil' in r.get_data(as_text=True)
    assert 'salt okunur' in c.get(f'/d/{DID}/').get_data(as_text=True)


def test_baska_siteden_post_reddedilir(ortam, tmp_path):
    c, _ = ortam
    assert ac(c).status_code == 303
    r = c.post(f'/d/{DID}/sistem', data=dict(ad='X', profil='CE'), headers={'Sec-Fetch-Site': 'cross-site'})
    assert r.status_code == 403


@pytest.mark.parametrize('yol', ['/d/yok-2026-as01/', '/d/..%2F..%2Fetc/', '/d/Buyuk/'])
def test_olmayan_ya_da_gecersiz_kimlik_404(ortam, yol):
    c, _ = ortam
    assert c.get(yol).status_code == 404


def test_framework_commit_farki_uyarisi(tmp_path):
    a = create_app(dict(LECTA_DATA=str(tmp_path), LECTA_USER='gokhan', LECTA_FRAMEWORK_COMMIT='abc1234', TESTING=True))
    ac(a.test_client())
    b = create_app(dict(LECTA_DATA=str(tmp_path), LECTA_USER='gokhan', LECTA_FRAMEWORK_COMMIT='def5678', TESTING=True))
    html = b.test_client().get(f'/d/{DID}/').get_data(as_text=True)
    assert 'abc1234' in html and 'def5678' in html and 'Madde ve kontrol metinleri farklı olabilir' in html
