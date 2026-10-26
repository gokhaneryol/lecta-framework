import os
import threading

import pytest

from app.depo import YOK, Cakisma, Depo


@pytest.fixture
def depo(tmp_path):
    return Depo(tmp_path)


def test_yeni_dosya_okuma_yazma(depo):
    assert depo.oku('d', 'kurum.yaml') == (None, YOK)
    veri = {'ad': {'tam': 'Örnek Kurum A.Ş.'}, 'ai_use': ['rag']}
    v = depo.yaz(veri, 'd', 'kurum.yaml', beklenen=YOK)
    assert depo.oku('d', 'kurum.yaml') == (veri, v)
    assert 'Örnek' in open(depo.yol('d', 'kurum.yaml'), encoding='utf-8').read()   # \u kaçışı yok


def test_eski_surumle_yazma_reddedilir(depo):
    v1 = depo.yaz({'a': 1}, 'x.yaml', beklenen=YOK)
    v2 = depo.yaz({'a': 2}, 'x.yaml', beklenen=v1)
    with pytest.raises(Cakisma):
        depo.yaz({'a': 3}, 'x.yaml', beklenen=v1)
    with pytest.raises(Cakisma):
        depo.yaz({'a': 3}, 'x.yaml', beklenen=YOK)      # "yeni" sanılan dosya zaten var
    assert depo.oku('x.yaml') == ({'a': 2}, v2)


def test_ayni_icerik_ayni_surum(depo):
    v1 = depo.yaz({'a': 1}, 'x.yaml', beklenen=YOK)
    assert depo.yaz({'a': 1}, 'x.yaml', beklenen=v1) == v1 == depo.surum('x.yaml')


def test_gecici_dosya_kalmaz(depo):
    depo.yaz({'a': 1}, 'd', 'x.yaml', beklenen=YOK)
    kalan = [f for f in os.listdir(depo.yol('d')) if f.endswith('.tmp')]
    assert kalan == []


def test_yazma_hatasinda_eski_dosya_saglam(depo, monkeypatch):
    v = depo.yaz({'a': 1}, 'x.yaml', beklenen=YOK)
    def bozuk(*a):
        raise OSError('disk dolu')
    monkeypatch.setattr(os, 'replace', bozuk)
    with pytest.raises(OSError):
        depo.yaz({'a': 2}, 'x.yaml', beklenen=v)
    monkeypatch.undo()
    assert depo.oku('x.yaml') == ({'a': 1}, v)
    assert not [f for f in os.listdir(depo.kok) if f.endswith('.tmp')]


@pytest.mark.parametrize('yol', [('..', 'x.yaml'), ('/etc', 'passwd'), ('d', '..', '..', 'x')])
def test_kok_disina_cikilamaz(depo, yol):
    with pytest.raises(ValueError):
        depo.yol(*yol)


def test_es_zamanli_yazmada_tek_kazanan(depo):
    v = depo.yaz({'n': 0}, 'x.yaml', beklenen=YOK)
    sonuc, engel = [], threading.Barrier(8)
    def yazar(n):
        engel.wait()
        try:
            depo.yaz({'n': n}, 'x.yaml', beklenen=v)
            sonuc.append(n)
        except Cakisma:
            pass
    ts = [threading.Thread(target=yazar, args=(n,)) for n in range(1, 9)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    assert len(sonuc) == 1
    assert depo.oku('x.yaml')[0] == {'n': sonuc[0]}
