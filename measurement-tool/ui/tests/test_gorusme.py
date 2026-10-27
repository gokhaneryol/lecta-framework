"""Adım 4 kabulü: QS akışı fixture'la uçtan uca doldurulabiliyor; sayfa yeniden açıldığında veri kaybı yok.

Cevaplar fixtures/qs/*.csv'den (elle doldurulmuş tabloyla aynı veri) arayüze girilir; her maddenin
ekrandaki tespiti qs.hesapla()'nın aynı CSV'den bulduğu puanla karşılaştırılır.
"""
import csv
import os
import re
from collections import defaultdict

import pytest

import qs
from app import create_app, gorusme
from app.depo import Depo, parca_surumu
from test_kapsam import DID, fixture_olustur

UI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIRIM = {'Örnek Kurum': 'KURUM', 'Kurumsal Asistan': 'kurumsal-asistan', 'Belge Arama': 'belge-arama'}


def uygulama(tmp_path, kullanici='gokhan'):
    return create_app(dict(LECTA_DATA=str(tmp_path), LECTA_USER=kullanici, LECTA_FRAMEWORK_COMMIT='abc1234',
                           LECTA_KULLANICILAR='gokhan,ayhan', TESTING=True))


@pytest.fixture
def ortam(tmp_path):
    c = uygulama(tmp_path).test_client()
    d = Depo(tmp_path)
    fixture_olustur(c, d)
    return c, d


def surum(d, birim, mid):
    veri, _ = d.oku(DID, 'cevaplar', f'{birim}.yaml')
    return parca_surumu((veri or {}).get(mid))


def gonder(c, d, birim, mid, kapali=(), **alan):
    """Tarayıcı gibi gönderir: açık her kontrol satırının not/kanıt alanı formda bulunur (boş da olsa);
    kapali verilen kontroller (devre dışı satırlar) hiç gönderilmez."""
    dg = d.oku(DID, 'degerlendirme.yaml')[0]
    m = next(m for b in gorusme.birimler(dg) if b['id'] == birim for m, _ in b['maddeler'] if m['id'] == mid)
    veri = dict(surum=surum(d, birim, mid), gorusme_notu='')
    for k in gorusme.qs_kontrolleri(m):
        if k['id'] not in kapali:
            veri.setdefault(f"not_{k['id']}", '')
            veri.setdefault(f"kanit_{k['id']}", '')
    veri.update(alan)
    return c.post(f'/d/{DID}/m/{birim}/{mid}', data=veri)


def blok(d, birim, mid):
    return ((d.oku(DID, 'cevaplar', f'{birim}.yaml')[0]) or {}).get(mid)


def csv_satirlari(ad):
    with open(os.path.join(UI, 'fixtures', 'qs', f'{ad}.csv'), encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


@pytest.mark.parametrize('ad', ['karisik-1', 'karisik-2', 'karisik-3', 'seyrek', 'hepsi-e'])
def test_uctan_uca_qs_akisi_ve_puan_esitligi(ortam, ad):
    c, d = ortam
    rows = csv_satirlari(ad)
    gruplar = defaultdict(dict)
    for r in rows:
        alan = gruplar[(BIRIM[r['unit']], r['item_id'])]
        if r['answer']:
            alan[f"cevap_{r['check_id']}"] = r['answer']
        alan[f"not_{r['check_id']}"] = r['note']
        alan[f"kanit_{r['check_id']}"] = r['evidence_ref']
        if r['na_reason']:
            alan['na_reason'] = r['na_reason']
    # arayüzün birim/madde kümesi puanlama CSV'siyle aynı
    dg = d.oku(DID, 'degerlendirme.yaml')[0]
    ekran = {(b['id'], m['id']) for b in gorusme.birimler(dg) for m, _ in b['maddeler']}
    assert ekran == set(gruplar)
    for (birim, mid), alan in gruplar.items():
        r = gonder(c, d, birim, mid, **alan)
        assert 'Kaydedildi' in r.get_data(as_text=True), (birim, mid, r.get_data(as_text=True)[:300])
    beklenen = {(BIRIM[r['unit']], r['item_id']): r['score'] for r in qs.hesapla(rows)['maddeler']}
    for b in gorusme.birimler(dg):
        for m, _ in b['maddeler']:
            bl = gorusme.tamamla(m, blok(d, b['id'], m['id']))
            assert gorusme.tespit(m, bl, dg['ref_date'])['puan'] == beklenen[(b['id'], m['id'])], (b['id'], m['id'])
    # sayfa yeniden açıldığında girilenler yerinde (tarayıcı kapatılıp açılınca veri kaybı yok)
    (birim, mid), alan = next((k, v) for k, v in gruplar.items() if any(x.startswith('cevap_') for x in v))
    html = c.get(f'/d/{DID}/m/{birim}/{mid}').get_data(as_text=True)
    kapali = alan.get('cevap_c1') in ('H', 'NA')         # K4: c1 = H/NA diğerlerini kapatır
    for k, v in alan.items():
        if k.startswith('cevap_') and (k == 'cevap_c1' or not kapali):
            assert re.search(rf'name="{k}" value="{v}" checked', html), k


def ilk(d):
    dg = d.oku(DID, 'degerlendirme.yaml')[0]
    b = gorusme.birimler(dg)[0]
    return b['id'], b['maddeler'][0][0], b['maddeler'][1][0]


def test_madde_ekrani_metni_yamldan_gosterir(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    html = c.get(f'/d/{DID}/m/{birim}/{m["id"]}').get_data(as_text=True)
    assert gorusme.metin(m['qs_question'])[:40] in html
    assert 'Bu cevaplarla madde puanı: <strong>NE</strong>' in html
    for s in gorusme.kontrol_satirlari(m, gorusme.tamamla(m, None)):
        assert f'id="k-{s["id"]}"' in html
    for t in gorusme.terimler(m):
        assert t['ad'] in html


def test_c1_hayir_cevapli_olanlar_dahil_hepsini_kapatir(ortam):
    """Saha bulgusu (27 Ekim): c1 E iken cevaplanan c2/c3, c1 H olunca da kapanmalı."""
    c, d = ortam
    birim, m, _ = ilk(d)
    gonder(c, d, birim, m['id'], cevap_c1='E', cevap_c2='E', cevap_c3='H')
    html = gonder(c, d, birim, m['id'], cevap_c1='H').get_data(as_text=True)
    assert html.count('atlandı (c1=H)') == len(gorusme.qs_kontrolleri(m)) - 1
    assert 'kayıtlı cevap: E' in html and 'madde puanı: <strong>0</strong>' in html
    assert 'id="madde-durum" class="rozet madde-durum durum-tamam"' in html
    assert re.search(r'id="k-c2"[^>]*hx-swap-oob="true">\s*<fieldset disabled', html)
    # kayıtlı cevaplar silinmez; c1 E'ye dönünce geri gelir
    k = blok(d, birim, m['id'])['kontroller']
    assert (k['c2']['cevap'], k['c3']['cevap']) == ('E', 'H')
    # tarayıcıdaki gibi: c1'i E yapan istekte diğer satırlar hâlâ kapalı, gönderilmez
    digerleri = [x['id'] for x in gorusme.qs_kontrolleri(m) if x['id'] != 'c1']
    html = gonder(c, d, birim, m['id'], kapali=digerleri, cevap_c1='E').get_data(as_text=True)
    assert 'atlandı (c1=H)' not in html and 'name="cevap_c2" value="E" checked' in html
    assert 'name="cevap_c3" value="H" checked' in html


def test_c1_atlaninca_digerleri_de_atlandi(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    gonder(c, d, birim, m['id'], cevap_c2='H')
    html = c.post(f'/d/{DID}/m/{birim}/{m["id"]}/atla', data=dict(surum=surum(d, birim, m['id']), kontrol='c1')).get_data(as_text=True)
    assert html.count('atlandı (c1 atlandı)') == len(gorusme.qs_kontrolleri(m)) - 1
    assert 'durum-atlandi' in html
    html = gonder(c, d, birim, m['id'], cevap_c1='E', cevap_c2='H').get_data(as_text=True)
    assert 'c1 atlandı' not in html


def test_c1_na_digerlerini_kapatir_gerekce_zorunlu(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    gonder(c, d, birim, m['id'], cevap_c1='E', cevap_c2='H', not_c2='saklanmalı')
    html = gonder(c, d, birim, m['id'], cevap_c1='NA').get_data(as_text=True)
    assert 'kapalı (c1=NA)' in html and 'name="na_reason"' in html and 'durum-not-alindi' in html
    k = blok(d, birim, m['id'])['kontroller']
    assert k['c2']['cevap'] == 'H' and k['c2']['not'] == 'saklanmalı'      # kapalı kontrolün değeri korunur
    html = gonder(c, d, birim, m['id'], cevap_c1='NA', na_reason='Kurumda bu süreç yok').get_data(as_text=True)
    assert 'durum-tamam' in html and '<strong>NA</strong>' in html
    assert blok(d, birim, m['id'])['na_reason'] == 'Kurumda bu süreç yok'


def test_na_yalniz_c1de(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    r = gonder(c, d, birim, m['id'], cevap_c1='E', cevap_c2='NA')
    assert 'geçersiz cevap' in r.get_data(as_text=True)
    assert blok(d, birim, m['id']) is None


def test_kontrol_atla_ve_sonra_cevapla(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    r = c.post(f'/d/{DID}/m/{birim}/{m["id"]}/atla', data=dict(surum=surum(d, birim, m['id']), kontrol='c2'))
    assert 'atlandı — sonra dönülecek' in r.get_data(as_text=True) and 'durum-atlandi' in r.get_data(as_text=True)
    assert blok(d, birim, m['id'])['kontroller']['c2']['durum'] == 'atlandi'
    gonder(c, d, birim, m['id'], cevap_c1='E', cevap_c3='E')
    assert blok(d, birim, m['id'])['kontroller']['c2']['durum'] == 'atlandi'   # cevapsız kaldıkça atlandı
    gonder(c, d, birim, m['id'], cevap_c1='E', cevap_c2='E')
    assert blok(d, birim, m['id'])['kontroller']['c2']['durum'] == 'cevaplandi'


def test_madde_atla_sonrakine_gider(ortam):
    c, d = ortam
    birim, m, m2 = ilk(d)
    gonder(c, d, birim, m['id'], cevap_c1='E')
    r = c.post(f'/d/{DID}/m/{birim}/{m["id"]}/atla', data=dict(surum=surum(d, birim, m['id'])))
    assert r.headers['HX-Redirect'] == f'/d/{DID}/m/{birim}/{m2["id"]}'
    k = blok(d, birim, m['id'])['kontroller']
    assert k['c1']['durum'] == 'cevaplandi' and all(v['durum'] == 'atlandi' for x, v in k.items() if x != 'c1')


def test_madde_duzeyinde_cakisma(ortam):
    c, d = ortam
    birim, m, m2 = ilk(d)
    eski = surum(d, birim, m['id'])
    gonder(c, d, birim, m['id'], cevap_c1='E')
    r = c.post(f'/d/{DID}/m/{birim}/{m["id"]}', data=dict(surum=eski, cevap_c1='H', not_c1=''))
    assert 'başka biri tarafından değiştirildi' in r.get_data(as_text=True)
    assert blok(d, birim, m['id'])['kontroller']['c1']['cevap'] == 'E'
    # aynı dosyadaki başka madde etkilenmez
    assert 'Kaydedildi' in gonder(c, d, birim, m2['id'], cevap_c1='B').get_data(as_text=True)


def test_ayni_icerik_surumu_degistirmez(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    gonder(c, d, birim, m['id'], cevap_c1='E', gorusme_notu='x')
    once = surum(d, birim, m['id'])
    gonder(c, d, birim, m['id'], cevap_c1='E', gorusme_notu='x')
    assert surum(d, birim, m['id']) == once


def test_guncelleme_ve_dosya_bicimi(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    gonder(c, d, birim, m['id'], cevap_c1='E', not_c1='politika var', kanit_c1='EK-01; EK-02')
    b = blok(d, birim, m['id'])
    assert list(b) == ['gorusme_notu', 'na_reason', 'kontroller', 'guncelleme']
    assert b['kontroller']['c1'] == {'cevap': 'E', 'durum': 'cevaplandi', 'not': 'politika var',
                                     'kanit': [{'ref': 'EK-01'}, {'ref': 'EK-02'}]}
    assert b['guncelleme']['kim'] == 'gokhan'


def test_baslat_ilk_tamamlanmamis_maddeye(ortam):
    c, d = ortam
    birim, m, m2 = ilk(d)
    assert c.get(f'/d/{DID}/gorusme').headers['Location'].endswith(f'/m/{birim}/{m["id"]}')
    gonder(c, d, birim, m['id'], cevap_c1='H')
    assert c.get(f'/d/{DID}/gorusme').headers['Location'].endswith(f'/m/{birim}/{m2["id"]}')


def test_ayni_birimde_baska_kullanici_uyarisi(tmp_path):
    a = uygulama(tmp_path, '')
    c = a.test_client()
    ac = lambda k: dict(headers={'X-Remote-User': k}, environ_base={'REMOTE_ADDR': '127.0.0.1'})
    c.post('/yeni', data=dict(ad_tam='Örnek Kurum A.Ş.', ad_kisa='Örnek', servis='AS-01', ref_date='2026-11-05'), **ac('gokhan'))
    d = Depo(tmp_path)
    c.post(f'/d/{DID}/sistem', data=dict(surum=d.surum(DID, 'degerlendirme.yaml'), ad='Asistan', profil='CE'), **ac('gokhan'))
    birim, m, _ = ilk(d)
    c.get(f'/d/{DID}/m/{birim}/{m["id"]}', **ac('ayhan'))
    html = c.get(f'/d/{DID}/m/{birim}/{m["id"]}', **ac('gokhan')).get_data(as_text=True)
    assert 'şu an ayhan de çalışıyor' in html


def test_taslak_olmayan_degismez_ve_404(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    assert c.get(f'/d/{DID}/m/{birim}/YOK-01').status_code == 404
    assert c.get(f'/d/{DID}/m/yok/{m["id"]}').status_code == 404
    dg, s = d.oku(DID, 'degerlendirme.yaml')
    d.yaz(dict(dg, durum='incelemede'), DID, 'degerlendirme.yaml', beklenen=s)
    assert 'taslak değil' in gonder(c, d, birim, m['id'], cevap_c1='E').get_data(as_text=True)


def test_kalin_suzgeci_kacislar():
    from app.gorusme_ekran import kalin
    assert str(kalin('a <b> **[≤ 12 ay]**')) == 'a &lt;b&gt; <strong>[≤ 12 ay]</strong>'


def test_kapanis_kaydi_kendi_kaydiyla_cakismaz(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    eski = surum(d, birim, m['id'])
    gonder(c, d, birim, m['id'], cevap_c1='E')                          # yoldaki otomatik kayıt
    r = c.post(f'/d/{DID}/m/{birim}/{m["id"]}', data=dict(surum=eski, kapanis='1', cevap_c1='E', not_c1='', gorusme_notu='son not'))
    assert 'Kaydedildi' in r.get_data(as_text=True)
    assert blok(d, birim, m['id'])['gorusme_notu'] == 'son not'


def test_kapanis_kaydi_baskasinin_degisikligini_ezmez(tmp_path):
    a = uygulama(tmp_path, '')
    c = a.test_client()
    ac = lambda k: dict(headers={'X-Remote-User': k}, environ_base={'REMOTE_ADDR': '127.0.0.1'})
    c.post('/yeni', data=dict(ad_tam='Örnek Kurum A.Ş.', ad_kisa='Örnek', servis='AS-01', ref_date='2026-11-05'), **ac('gokhan'))
    d = Depo(tmp_path)
    c.post(f'/d/{DID}/sistem', data=dict(surum=d.surum(DID, 'degerlendirme.yaml'), ad='Asistan', profil='CE'), **ac('gokhan'))
    birim, m, _ = ilk(d)
    eski = surum(d, birim, m['id'])
    c.post(f'/d/{DID}/m/{birim}/{m["id"]}', data=dict(surum=eski, cevap_c1='H', not_c1=''), **ac('ayhan'))
    r = c.post(f'/d/{DID}/m/{birim}/{m["id"]}', data=dict(surum=eski, kapanis='1', cevap_c1='E', not_c1=''), **ac('gokhan'))
    assert 'başka biri tarafından değiştirildi' in r.get_data(as_text=True)
    assert blok(d, birim, m['id'])['kontroller']['c1']['cevap'] == 'H'


def test_madde_formunda_tarayici_dogrulamasi_yok(ortam):
    """htmx, form geçersizse isteği hiç göndermez: c1=NA iken boş zorunlu alan, sonraki tüm
    kayıtları sessizce engelliyordu (saha denemesi, 27 Ekim). Formda required/pattern olmamalı."""
    c, d = ortam
    birim, m, _ = ilk(d)
    gonder(c, d, birim, m['id'], cevap_c1='NA')
    html = c.get(f'/d/{DID}/m/{birim}/{m["id"]}').get_data(as_text=True)
    form = html[html.index('<form id="madde-form"'):html.index('</form>', html.index('<form id="madde-form"'))]
    assert 'name="na_reason"' in form
    assert ' required' not in form and 'pattern=' not in form
    # NA'dan başka cevaba dönünce kapalı kontroller yeniden açılır
    r = gonder(c, d, birim, m['id'], cevap_c1='B').get_data(as_text=True)
    assert 'durum-kapali' not in r and 'id="na" hx-swap-oob="true"' in r


def test_otomatik_kayit_formlarinda_required_yok(ortam):
    c, d = ortam
    html = c.get(f'/d/{DID}/').get_data(as_text=True)
    assert ' required' not in html


def test_na_gerekcesi_c1_altinda_ve_silinince_eksik(ortam):
    c, d = ortam
    birim, m, _ = ilk(d)
    html = gonder(c, d, birim, m['id'], cevap_c1='NA').get_data(as_text=True)
    sayfa = c.get(f'/d/{DID}/m/{birim}/{m["id"]}').get_data(as_text=True)
    assert sayfa.index('id="na"') < sayfa.index('id="k-c2"')            # c1 satırının içinde, c2'den önce
    gonder(c, d, birim, m['id'], cevap_c1='NA', na_reason='Süreç yok')
    assert gorusme.madde_durumu(m, gorusme.tamamla(m, blok(d, birim, m['id']))) == 'tamam'
    html = gonder(c, d, birim, m['id'], cevap_c1='NA', na_reason='').get_data(as_text=True)
    assert 'durum-not-alindi' in html and 'id="na-uyari"' in html and 'tamamlanmış sayılmaz' in html
    assert 'id="na" hx-swap-oob' not in html            # yazarken gerekçe alanı yeniden çizilmez
    # c1 NA'dan çıkınca gerekçe silinmez, geri dönünce yerinde
    gonder(c, d, birim, m['id'], cevap_c1='NA', na_reason='Süreç yok')
    gonder(c, d, birim, m['id'], cevap_c1='E')
    assert blok(d, birim, m['id'])['na_reason'] == 'Süreç yok'
