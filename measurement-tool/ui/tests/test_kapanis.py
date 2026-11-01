"""Adım 5 kabulü: aynı cevaplarla elle doldurulmuş CSV ile arayüzün CSV'si, qs.py seviye'den bayt bayt aynı
çıktıyı verir. Ayrıca kapanış → inceleme → kapanma akışı, çıktı dosyaları ve yerel git commit'leri.

"Elle doldurulmuş" tablo, kuralları bilen bir değerlendiricinin dolduracağı tablodur (TASARIM §4.5, K4):
boş kontrol B + "atlandı"; c1 = H/NA ise diğer kontroller c1'in değerini alır, notları ve kanıtları yazılmaz.
"""
import csv
import os
import subprocess
import sys
from collections import defaultdict

import pytest

import qs
from app import cikti, create_app, gorusme
from app.depo import Depo
from test_gorusme import BIRIM, csv_satirlari as fixture_csv, gonder
from test_kapsam import DID, fixture_olustur

UI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(UI, '..', 'tools')
KURUM_AD = 'Örnek'           # fixture kurumun kısa adı: KURUM satırlarının birim adı


def elle_doldur(rows):
    """Ham fixture CSV'sinden, kuralları uygulayan değerlendiricinin elle dolduracağı tablo."""
    rows = [dict(r, unit=KURUM_AD if r['unit_type'] == 'KURUM' else r['unit']) for r in rows]
    c1 = {(r['unit'], r['item_id']): r['answer'] for r in rows if r['check_id'] == 'c1'}
    for r in rows:
        kapatan = c1[(r['unit'], r['item_id'])]
        if r['check_id'] != 'c1' and kapatan in ('H', 'NA'):
            r.update(answer=kapatan, note='', evidence_ref='', na_reason='')
        elif not r['answer']:
            r.update(answer='B', note=f"{r['note']} · atlandı" if r['note'] else 'atlandı')
        if not (r['check_id'] == 'c1' and r['answer'] == 'NA'):
            r['na_reason'] = ''
    return rows


class Istemci:
    """Kimliği X-Remote-User ile değiştirilebilen test istemcisi (sunucudaki gibi)."""

    def __init__(self, tmp_path):
        app = create_app(dict(LECTA_DATA=str(tmp_path), LECTA_USER='', LECTA_FRAMEWORK_COMMIT='abc1234',
                              LECTA_KULLANICILAR='gokhan,ayhan', TESTING=True))
        self.c = app.test_client()
        self.app = app
        self.kim('gokhan')

    def kim(self, k):
        self.c.environ_base.update(REMOTE_ADDR='127.0.0.1', HTTP_X_REMOTE_USER=k)
        return self.c


@pytest.fixture
def ortam(tmp_path):
    i = Istemci(tmp_path)
    d = Depo(tmp_path)
    fixture_olustur(i.c, d)
    return i, d, tmp_path


def doldur(c, d, ad):
    gruplar = defaultdict(dict)
    for r in fixture_csv(ad):
        alan = gruplar[(BIRIM[r['unit']], r['item_id'])]
        if r['answer']:
            alan[f"cevap_{r['check_id']}"] = r['answer']
        alan[f"not_{r['check_id']}"] = r['note']
        alan[f"kanit_{r['check_id']}"] = r['evidence_ref']
        if r['na_reason']:
            alan['na_reason'] = r['na_reason']
    for (birim, mid), alan in gruplar.items():
        assert 'Kaydedildi' in gonder(c, d, birim, mid, **alan).get_data(as_text=True)


def seviye(csv_yolu):
    return subprocess.run([sys.executable, os.path.join(TOOLS, 'qs.py'), 'seviye', str(csv_yolu)],
                          check=True, capture_output=True).stdout


@pytest.mark.parametrize('ad', ['karisik-1', 'karisik-2', 'karisik-3', 'seyrek', 'hepsi-e'])
def test_kabul_elle_ve_arayuz_csv_bayt_bayt_ayni(ortam, ad):
    i, d, tmp = ortam
    doldur(i.c, d, ad)
    elle_dir, ui_dir = tmp / 'elle', tmp / 'arayuz'
    elle_dir.mkdir(), ui_dir.mkdir()
    with open(elle_dir / 'qs.csv', 'w', newline='', encoding='utf-8') as fh:
        qs.csv_yaz(elle_doldur(fixture_csv(ad)), fh)
    with i.app.app_context():
        dg, kurum = d.oku(DID, 'degerlendirme.yaml')[0], d.oku(DID, 'kurum.yaml')[0]
        (ui_dir / 'qs.csv').write_bytes(cikti.csv_metni(cikti.csv_satirlari(d, DID, dg, kurum)).encode('utf-8'))
    assert (ui_dir / 'qs.csv').read_bytes() == (elle_dir / 'qs.csv').read_bytes()
    assert seviye(ui_dir / 'qs.csv') == seviye(elle_dir / 'qs.csv')


def git_log(tmp):
    return subprocess.run(['git', '-C', str(tmp / DID), 'log', '--format=%an|%s'], capture_output=True, text=True,
                          check=True).stdout.strip().splitlines()


def test_kapanis_eksikleri_listeler_ve_incelemeye_gonderir(ortam):
    i, d, tmp = ortam
    birim, m = 'KURUM', 'G-POL-02'
    gonder(i.c, d, birim, m, cevap_c1='E')
    html = i.c.get(f'/d/{DID}/kapanis').get_data(as_text=True)
    assert 'maddede' not in html or 'tamamlanmadı' in html
    assert 'G-POL-02' in html and 'boş: c2' in html
    r = i.c.post(f'/d/{DID}/kapanis')
    assert r.status_code == 303 and r.headers['Location'].endswith(f'/d/{DID}/inceleme')
    dg = d.oku(DID, 'degerlendirme.yaml')[0]
    assert dg['durum'] == 'incelemede' and dg['olaylar'][-1]['ne'] == 'incelemeye-gonderildi'
    # çıktılar: seviye.md, aynı CSV'den qs.py seviye ile bayt bayt aynı
    assert (tmp / DID / 'cikti' / 'seviye.md').read_bytes() == seviye(tmp / DID / 'cikti' / 'qs.csv')
    kaynak = d.oku(DID, 'cikti', 'kaynak.yaml')[0]
    assert kaynak['framework']['acilis']['commit'] == 'abc1234' and kaynak['framework']['cikti']['commit'] == 'abc1234'
    assert git_log(tmp)[0] == 'gokhan|Kapanış: incelemeye gönderildi (gokhan)'
    # incelemede madde değiştirilemez
    assert 'taslak değil' in gonder(i.c, d, birim, m, cevap_c1='H').get_data(as_text=True)


def test_kapanisi_yalniz_degerlendirici_ve_gozden_geciren_secilmisse(ortam):
    i, d, tmp = ortam
    i.kim('ayhan')
    assert 'yalnız değerlendirici' in i.c.post(f'/d/{DID}/kapanis').get_data(as_text=True)
    i.kim('gokhan')
    dg, s = d.oku(DID, 'degerlendirme.yaml')
    d.yaz(dict(dg, gozden_geciren=''), DID, 'degerlendirme.yaml', beklenen=s)
    assert 'gözden geçireni seçin' in i.c.post(f'/d/{DID}/kapanis').get_data(as_text=True)
    assert d.oku(DID, 'degerlendirme.yaml')[0]['durum'] == 'taslak'


def karar(i, birim, mid, k, yorum=''):
    return i.c.post(f'/d/{DID}/inceleme/{birim}/{mid}', data=dict(karar=k, yorum=yorum))


def tum_maddeler(d):
    dg = d.oku(DID, 'degerlendirme.yaml')[0]
    return [(b['id'], m['id']) for b in gorusme.birimler(dg) for m, _ in b['maddeler']]


def test_inceleme_akisi_kapanir(ortam):
    i, d, tmp = ortam
    i.c.post(f'/d/{DID}/kapanis')
    assert 'yalnız gözden geçiren' in karar(i, 'KURUM', 'G-POL-02', 'katiliyor').get_data(as_text=True)   # gokhan
    i.kim('ayhan')
    maddeler = tum_maddeler(d)
    for n, (b, m) in enumerate(maddeler):
        if n == len(maddeler) - 1:
            break
        karar(i, b, m, 'katilmiyor' if n == 0 else 'katiliyor', 'c2 bence H' if n == 0 else '')
    html = i.c.post(f'/d/{DID}/inceleme/bitir').get_data(as_text=True)
    assert '1 maddede karar yok' in html
    html = karar(i, *maddeler[-1], 'katiliyor').get_data(as_text=True)
    assert f'<strong>{len(maddeler)}</strong> / {len(maddeler)}' in html and 'Uyuşmazlık: <strong>1</strong>' in html
    inc = d.oku(DID, 'cevaplar', f'{maddeler[0][0]}.yaml')[0][maddeler[0][1]]['inceleme']
    assert inc['karar'] == 'katilmiyor' and inc['yorum'] == 'c2 bence H' and inc['kim'] == 'ayhan'
    r = i.c.post(f'/d/{DID}/inceleme/bitir')
    assert r.status_code == 303 and r.headers['Location'].endswith('/sonuc')
    assert d.oku(DID, 'degerlendirme.yaml')[0]['durum'] == 'kapali'
    assert git_log(tmp)[0] == 'ayhan|İnceleme bitti: değerlendirme kapandı (ayhan)'


def test_geri_gonderilince_duzenlenir_ve_sonra_degisti_isaretlenir(ortam):
    i, d, tmp = ortam
    gonder(i.c, d, 'KURUM', 'G-POL-02', cevap_c1='E')
    i.c.post(f'/d/{DID}/kapanis')
    i.kim('ayhan')
    karar(i, 'KURUM', 'G-POL-02', 'katilmiyor', 'c1 kanıtsız')
    assert i.c.post(f'/d/{DID}/inceleme/geri').status_code == 303
    assert d.oku(DID, 'degerlendirme.yaml')[0]['durum'] == 'taslak'
    i.kim('gokhan')
    assert 'Kaydedildi' in gonder(i.c, d, 'KURUM', 'G-POL-02', cevap_c1='H').get_data(as_text=True)
    assert 'sonra değişti' in i.c.get(f'/d/{DID}/inceleme').get_data(as_text=True)
    assert [x.split('|')[1] for x in git_log(tmp)[:2]] == ['İnceleme: değerlendiriciye geri gönderildi (ayhan)',
                                                            'Kapanış: incelemeye gönderildi (gokhan)']


def test_sonuc_ekrani_ve_cikti_indirme(ortam):
    i, d, tmp = ortam
    doldur(i.c, d, 'hepsi-e')
    html = i.c.get(f'/d/{DID}/sonuc').get_data(as_text=True)
    assert 'Önizleme' in html and '<strong>L1</strong>' in html and 'Çıktılar kapanışta üretilir' in html
    assert i.c.get(f'/d/{DID}/cikti/qs.csv').status_code == 404
    i.c.post(f'/d/{DID}/kapanis')
    r = i.c.get(f'/d/{DID}/cikti/seviye.md')
    assert r.status_code == 200 and r.data == (tmp / DID / 'cikti' / 'seviye.md').read_bytes()
    assert i.c.get(f'/d/{DID}/cikti/../kurum.yaml').status_code == 404


def test_anlik_goruntu(ortam):
    i, d, tmp = ortam
    gonder(i.c, d, 'KURUM', 'G-POL-02', cevap_c1='E')
    r = i.c.post(f'/d/{DID}/goruntu')
    assert 'Anl%C4%B1k+g%C3%B6r%C3%BCnt%C3%BC+al%C4%B1nd%C4%B1' in r.headers['Location'] or 'mesaj=' in r.headers['Location']
    assert git_log(tmp)[0] == 'gokhan|Anlık görüntü (gokhan)'
    r = i.c.post(f'/d/{DID}/goruntu')
    assert len([x for x in git_log(tmp) if 'Anlık' in x]) == 1          # değişiklik yoksa commit yok


def test_csv_kapali_kontroller_c1_degeriyle(ortam):
    i, d, tmp = ortam
    gonder(i.c, d, 'KURUM', 'G-POL-02', cevap_c1='E', cevap_c2='E', not_c2='var', kanit_c2='EK-1')
    gonder(i.c, d, 'KURUM', 'G-POL-02', cevap_c1='H')
    gonder(i.c, d, 'KURUM', 'G-INV-01', cevap_c1='NA', na_reason='Envanter yok')
    i.c.post(f'/d/{DID}/m/KURUM/G-INV-02/atla', data=dict(surum='', kontrol='c1'))
    with i.app.app_context():
        dg, kurum = d.oku(DID, 'degerlendirme.yaml')[0], d.oku(DID, 'kurum.yaml')[0]
        rows = {(r['unit'], r['item_id'], r['check_id']): r for r in cikti.csv_satirlari(d, DID, dg, kurum)}
    c2 = rows[(KURUM_AD, 'G-POL-02', 'c2')]
    assert (c2['answer'], c2['note'], c2['evidence_ref']) == ('H', '', '')        # kayıtlı E yazılmaz
    assert rows[(KURUM_AD, 'G-INV-01', 'c1')]['na_reason'] == 'Envanter yok'
    assert rows[(KURUM_AD, 'G-INV-01', 'c2')]['answer'] == 'NA'
    assert (rows[(KURUM_AD, 'G-INV-02', 'c1')]['answer'], rows[(KURUM_AD, 'G-INV-02', 'c1')]['note']) == ('B', 'atlandı')
    assert (rows[(KURUM_AD, 'G-INV-02', 'c2')]['answer'], rows[(KURUM_AD, 'G-INV-02', 'c2')]['note']) == ('B', 'atlandı')
