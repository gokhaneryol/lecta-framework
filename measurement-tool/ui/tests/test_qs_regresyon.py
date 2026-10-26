"""qs.py çıktıları, hesapla() ayrıştırmasından önceki sürümle bayt bayt aynı kalmalı (TASARIM.md §5.1).

golden/ dosyaları ayrıştırmadan önceki qs.py ile üretildi. İstisna: seviye-karisik-1/-2 c1 = NA satırı
içerir; eski sürüm bu girdide çöküyordu (check_met('NA')), bu yüzden düzeltmeden sonra üretildi.
"""
import csv
import datetime as dt
import os
import subprocess
import sys

import pytest

import kontrol
import qs

UI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(UI, '..', 'tools')
GOLDEN = os.path.join(UI, 'tests', 'golden')
FIX = os.path.join(UI, 'fixtures', 'qs')
SEVIYE = ['bos', 'hepsi-e', 'karisik-1', 'karisik-2', 'karisik-3', 'seyrek']


def calistir(*args):
    return subprocess.run([sys.executable, os.path.join(TOOLS, 'qs.py'), *args],
                          check=True, capture_output=True).stdout


def golden(ad):
    with open(os.path.join(GOLDEN, ad), 'rb') as fh:
        return fh.read()


@pytest.mark.parametrize('profil', ['CE', 'SOV'])
def test_rehber(profil):
    assert calistir('rehber', '--profil', profil) == golden(f'rehber-{profil}.md')


def test_puanlama(tmp_path):
    out = tmp_path / 'p.csv'
    calistir('puanlama', '--kurum', 'Örnek Kurum', '--sistem', 'Kurumsal Asistan:CE',
             '--sistem', 'Belge Arama:SOV', '--out', str(out))
    assert out.read_bytes() == golden('puanlama.csv')


@pytest.mark.parametrize('ad', SEVIYE)
def test_seviye(ad):
    assert calistir('seviye', os.path.join(FIX, f'{ad}.csv')) == golden(f'seviye-{ad}.md')


def satirlar(ad):
    with open(os.path.join(FIX, f'{ad}.csv'), encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


@pytest.mark.parametrize('ad', SEVIYE)
def test_seviye_md_hesapla_sonucundan(ad):
    md = qs.seviye_md(qs.hesapla(satirlar(ad)), f'{ad}.csv') + '\n'
    assert md.encode('utf-8') == golden(f'seviye-{ad}.md')


def test_hesapla_girdiyi_degistirmez():
    rows = satirlar('karisik-1')
    once = [dict(r) for r in rows]
    qs.hesapla(rows)
    assert rows == once


def test_c1_na_maddesi_na_olur():
    h = qs.hesapla(satirlar('karisik-1'))
    na = [r for r in h['maddeler'] if r['score'] == 'NA']
    assert na and all(r['na_reason'] for r in na)
    assert not any(r['score'] == 'NA' for r in h['riskler'])


def test_bloklayanlar_raporlanan_seviyenin_ustunu_engeller():
    h = qs.hesapla(satirlar('karisik-1'))
    for s in h['seviyeler']:
        bl = h['bloklayanlar'][s['birim']]
        if s['raporlanan'] >= qs.QS_CAP:
            assert bl == []
        else:
            assert bl and all(qs.passed(r) is False for r in bl)
    tam = qs.hesapla(satirlar('hepsi-e'))
    assert all(s['raporlanan'] == qs.QS_CAP for s in tam['seviyeler'])
    assert all(v == [] for v in tam['bloklayanlar'].values())


def test_ref_date_tarih_kontrollerine_gecer():
    """Tarih cevabı ref_date'e göre değerlendirilir; collapse() ref_date'i kontrol.score'a iletir."""
    i, c = next((i, c) for i in qs.load_items() if 'checks' in i
                for c in i['checks'] if c['type'] == 'date' and (c.get('threshold') or {}).get('max_months'))
    m = c['threshold']['max_months']
    m = i['review_interval'] if m == 'review_interval' else m
    d = dt.date(2026, 1, 15)
    yakin, uzak = dt.date(2026, 2, 1), dt.date(2026 + m // 12 + 1, 1, 15)
    assert kontrol.check_met(c, d.isoformat(), i, yakin) is True
    assert kontrol.check_met(c, d.isoformat(), i, uzak) is False
    cevap = {x['id']: 'E' for x in i['checks']}
    cevap[c['id']] = d.isoformat()
    rows = [dict(unit='U', unit_type='SISTEM', profile='CE', item_id=i['id'], check_id=k,
                 answer=v, note='', na_reason='') for k, v in cevap.items()]
    puan = lambda ref: qs.collapse([dict(r) for r in rows], ref)[0]['score']
    assert puan(yakin) != puan(uzak)


def test_org_fields_madde_sanilmaz():
    import inceleme
    ids = [i['id'] for i in qs.load_items()]
    assert len(ids) == 29 and len(set(ids)) == 29
    assert len(inceleme.items()) == 29
