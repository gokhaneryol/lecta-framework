"""Kapanış, inceleme ve sonuç: CSV'ye dönüşüm, eksikler, seviye, durum geçişleri (TASARIM.md §4.5, §5.2/4–6, K6).

CSV satırları qs.puanlama_satirlari ile üretilir (elle doldurulan tabloyla aynı satırlar, aynı sıra);
seviye qs.hesapla + qs.seviye_md ile. Burada yalnız cevapların satırlara yazılması var.
"""
import io

from . import framework, gorusme, kayit
from .depo import parca_surumu
from .framework import qs

KAPALI_CEVAP = {'H': 'H', 'NA': 'NA', 'atlandi': 'B'}    # c1 diğerlerini kapattıysa (K4, §4.5)
ATLANDI = 'atlandı'


class Gecis(Exception):
    """İzin verilmeyen durum geçişi; mesaj kullanıcıya gösterilir."""


def _birim_verisi(depo, did, dg):
    """{birim_id: {madde_id: blok}}"""
    ids = [gorusme.KURUM] + [s['id'] for s in dg['sistemler']]
    return {b: (depo.oku(did, 'cevaplar', f'{b}.yaml')[0] or {}) for b in ids}


def _not_ekle(notu, ek):
    return f'{notu} · {ek}' if notu else ek


def csv_satirlari(depo, did, dg, kurum):
    """Değerlendirmenin puanlama CSV satırları (score boş; betik hesaplar)."""
    sistemler = dg['sistemler']
    rows = qs.puanlama_satirlari(kurum['ad']['kisa'], [(s['ad'], s['profil']) for s in sistemler])
    birim_id = {s['ad']: s['id'] for s in sistemler}
    veri = _birim_verisi(depo, did, dg)
    maddeler = framework.maddeler()
    for r in rows:
        bid = gorusme.KURUM if r['unit_type'] == 'KURUM' else birim_id[r['unit']]
        madde = maddeler[r['item_id']]
        blok = gorusme.tamamla(madde, veri[bid].get(r['item_id']))
        kontrol = next(c for c in madde['checks'] if c['id'] == r['check_id'])
        k = blok['kontroller'][r['check_id']]
        neden = gorusme.c1_kapatir(blok)
        if neden and kontrol['kind'] != 'exist':
            cevap, notu, kanit = KAPALI_CEVAP[neden], (ATLANDI if neden == 'atlandi' else ''), ''
        else:
            cevap, notu = k.get('cevap'), (k.get('not') or '')
            if not cevap:                                # boş ya da "sonra döneceğim": kapanışta B
                cevap, notu = 'B', _not_ekle(notu, ATLANDI)
            kanit = ';'.join(x['ref'] for x in k.get('kanit') or [])
        r.update(answer=cevap, note=notu, evidence_ref=kanit,
                 na_reason=(blok.get('na_reason') or '') if kontrol['kind'] == 'exist' and cevap == 'NA' else '',
                 assessor=dg.get('degerlendirici') or '', reviewer=dg.get('gozden_geciren') or '')
    return rows


def csv_metni(rows):
    fh = io.StringIO(newline='')
    qs.csv_yaz(rows, fh)
    return fh.getvalue()


def sonuc(depo, did, dg, kurum):
    """qs.hesapla sonucu + CSV satırları."""
    rows = csv_satirlari(depo, did, dg, kurum)
    return rows, qs.hesapla(rows, dg['ref_date'])


def eksikler(depo, did, dg):
    """Tamamlanmamış maddeler: [{birim, madde, durum, ayrinti}] (K4: kapanışta B olarak çıkar)."""
    veri = _birim_verisi(depo, did, dg)
    out = []
    for b in gorusme.birimler(dg):
        for m, _ in b['maddeler']:
            ham = veri[b['id']].get(m['id'])
            blok = gorusme.tamamla(m, ham)
            durum = gorusme.madde_durumu(m, blok if ham else None)
            if durum == 'tamam':
                continue
            etkin = gorusme.etkin_durumlar(m, blok)
            if gorusme.c1_kapatir(blok) == gorusme.NA:
                ayrinti = 'NA gerekçesi yok'
            else:
                bos = [c for c, d in etkin.items() if d == 'bos']
                atl = [c for c, d in etkin.items() if d in ('atlandi', 'kapali-atlandi')]
                ayrinti = ' · '.join(x for x in (f"boş: {', '.join(bos)}" if bos else '',
                                                f"atlandı: {', '.join(atl)}" if atl else '') if x)
            out.append(dict(birim=b, madde=m, durum=durum, ayrinti=ayrinti))
    return out


def incelemeler(depo, did, dg):
    """İnceleme ekranı için madde satırları: tespit, inceleme kararı, inceleme sonrası değişti mi."""
    veri = _birim_verisi(depo, did, dg)
    out = []
    for b in gorusme.birimler(dg):
        for m, lv in b['maddeler']:
            ham = veri[b['id']].get(m['id']) or {}
            blok = gorusme.tamamla(m, ham or None)
            inc = ham.get('inceleme') or {}
            degisti = bool(inc) and inc.get('madde_surumu') != icerik_surumu(ham)
            out.append(dict(birim=b, madde=m, seviye=lv, tespit=gorusme.tespit(m, blok, dg['ref_date']),
                            durum=gorusme.madde_durumu(m, blok if ham else None), inceleme=inc, degisti=degisti))
    return out


# ------------------------------------------------------------------ durum geçişleri
def _olay(dg, ne, kim):
    dg['olaylar'] = list(dg.get('olaylar') or []) + [dict(ne=ne, kim=kim, zaman=kayit.simdi())]


def gecis(dg, ne, kim):
    """Durum makinesi (K6): taslak → incelemede → kapali; incelemede → taslak (geri gönder)."""
    d, yeni = dg.get('durum'), dict(dg)
    if ne == 'incelemeye-gonderildi':
        if d != 'taslak':
            raise Gecis('Yalnız taslak değerlendirme incelemeye gönderilir.')
        if kim != dg['degerlendirici']:
            raise Gecis('İncelemeye yalnız değerlendirici gönderir.')
        if not dg.get('gozden_geciren'):
            raise Gecis('Önce kapsam ekranında gözden geçireni seçin.')
        if not dg.get('sistemler'):
            raise Gecis('En az bir sistem gerekli.')
        yeni['durum'] = 'incelemede'
    elif ne in ('kapandi', 'geri-gonderildi'):
        if d != 'incelemede':
            raise Gecis('Değerlendirme incelemede değil.')
        if kim != dg.get('gozden_geciren'):
            raise Gecis('Bu adımı yalnız gözden geçiren yapar.')
        yeni['durum'] = 'kapali' if ne == 'kapandi' else 'taslak'
    else:
        raise ValueError(ne)
    _olay(yeni, ne, kim)
    return yeni


def icerik_surumu(blok):
    """Maddenin cevap içeriğinin özeti (inceleme ve güncelleme bilgisi hariç): karar sonrası değişti mi?"""
    return parca_surumu({k: v for k, v in (blok or {}).items() if k not in ('inceleme', 'guncelleme')})


def inceleme_karari(madde, eski, karar, yorum, kim):
    if karar not in ('katiliyor', 'katilmiyor', ''):
        raise ValueError(karar)
    blok = gorusme.tamamla(madde, eski)
    if eski and 'guncelleme' in eski:
        blok['guncelleme'] = eski['guncelleme']           # inceleme, maddenin güncellemesi sayılmaz
    blok['inceleme'] = dict(karar=karar or None, yorum=yorum.strip()[:2000], kim=kim, zaman=kayit.simdi(),
                            madde_surumu=icerik_surumu(eski))
    return blok


def ciktilari_yaz(depo, did, dg, kurum, kim):
    """cikti/qs.csv, cikti/seviye.md (qs.py seviye ile aynı bayt), cikti/kaynak.yaml."""
    rows, h = sonuc(depo, did, dg, kurum)
    depo.yaz_ham(csv_metni(rows).encode('utf-8'), did, 'cikti', 'qs.csv')
    depo.yaz_ham((qs.seviye_md(h, 'qs.csv') + '\n').encode('utf-8'), did, 'cikti', 'seviye.md')
    depo.yaz(dict(degerlendirme=did, uretim=dict(kim=kim, zaman=kayit.simdi()),
                  framework=dict(acilis=dg['framework'], cikti=dict(surum=framework.surum(),
                                                                   commit=framework.commit()))),
             did, 'cikti', 'kaynak.yaml', beklenen=None)
