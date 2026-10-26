import pytest

from app import create_app, framework


def uygulama(tmp_path, **ayar):
    return create_app(dict(LECTA_DATA=str(tmp_path), LECTA_FRAMEWORK_COMMIT='abc1234', TESTING=True, **ayar))


def test_bos_liste_sayfasi(tmp_path):
    r = uygulama(tmp_path, LECTA_USER='gokhan').test_client().get('/')
    html = r.get_data(as_text=True)
    assert r.status_code == 200
    assert 'Henüz değerlendirme yok' in html and 'gokhan' in html and 'abc1234' in html
    assert framework.surum() in html


def test_degerlendirme_dizini_listelenir(tmp_path):
    (tmp_path / 'ornek-2026-as01').mkdir()
    (tmp_path / 'ornek-2026-as01' / 'degerlendirme.yaml').write_text('id: ornek-2026-as01\n')
    (tmp_path / 'baska-dizin').mkdir()
    html = uygulama(tmp_path, LECTA_USER='gokhan').test_client().get('/').get_data(as_text=True)
    assert 'ornek-2026-as01' in html and 'baska-dizin' not in html


def test_kimliksiz_istek_reddedilir(tmp_path):
    assert uygulama(tmp_path, LECTA_USER='').test_client().get('/').status_code == 401


def test_guvenilen_vekilden_baslik_kabul(tmp_path):
    c = uygulama(tmp_path, LECTA_USER='').test_client()
    r = c.get('/', headers={'X-Remote-User': 'ayhan'}, environ_base={'REMOTE_ADDR': '127.0.0.1'})
    assert r.status_code == 200 and 'ayhan' in r.get_data(as_text=True)


def test_baska_adresten_baslik_yok_sayilir(tmp_path):
    c = uygulama(tmp_path, LECTA_USER='').test_client()
    r = c.get('/', headers={'X-Remote-User': 'ayhan'}, environ_base={'REMOTE_ADDR': '10.8.0.5'})
    assert r.status_code == 401


def test_saglik_ve_htmx_kimliksiz(tmp_path):
    c = uygulama(tmp_path, LECTA_USER='').test_client()
    assert c.get('/saglik').status_code == 200
    r = c.get('/static/htmx.min.js')
    assert r.status_code == 200 and b'htmx' in r.data[:200]


def test_lecta_data_zorunlu(monkeypatch):
    monkeypatch.delenv('LECTA_DATA', raising=False)
    with pytest.raises(RuntimeError):
        create_app()


def test_org_fields_kodlari():
    alanlar = framework.org_fields()
    assert set(alanlar) == {'sector', 'employee_band', 'ai_use'}
    assert alanlar['ai_use']['multi'] is True
    for ad, a in alanlar.items():
        kodlar = [o['code'] for o in a['options']]
        assert len(kodlar) == len(set(kodlar)), ad
        for o in a['options']:
            assert isinstance(o['code'], str) and o['label']['tr'] and o['label']['en']
