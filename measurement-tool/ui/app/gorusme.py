"""Görüşme: birimler, madde cevapları, skip kuralları, durum ve tespit (TASARIM.md §4.4, §5.2/3, K4, K7).

Madde ve kontrol metni yalnız source/*.yaml'dan (qs.qs_items); puan yalnız kontrol.score / check_met ile.
Cevap dosyası: cevaplar/<birim>.yaml — birim KURUM (G bloğu) ya da sistem kimliği.

Kontrol durumu (saklanan): bos · cevaplandi · atlandi ("sonra döneceğim").
Otomatik durumlar saklanmaz, her seferinde hesaplanır:
  c1 = H  → cevaplanmamış diğer kontroller "atlandı (c1=H)"; düzenlenebilir kalır.
  c1 = NA → diğer kontroller kapanır, na_reason zorunlu.
"""
from . import framework
from .framework import kontrol, qs

KURUM = 'KURUM'
CEVAPLAR = ('E', 'H', 'B')
NA = 'NA'
DURUM_ETIKET = {'bos': 'boş', 'not-alindi': 'eksik', 'atlandi': 'atlandı', 'tamam': 'tamam'}


def qs_kontrolleri(madde):
    return [c for c in madde['checks'] if c.get('qs', True)]


# ------------------------------------------------------------------ birimler
def birimler(dg):
    """[{id, ad, profiller, maddeler: [(madde, seviye_metni)]}] — KURUM önce, sonra sistemler.

    G maddeleri kullanılan profillerin birleşimidir (qs.py puanlama ile aynı küme); sıra
    en düşük seviye, sonra ID. Sistem maddeleri qs_items() sırasındadır (seviye, ID).
    """
    sistemler = dg.get('sistemler') or []
    if not sistemler:
        return []
    profiller = list(dict.fromkeys(s['profil'] for s in sistemler))
    g = {}
    for p in profiller:
        for m in framework.qs_maddeleri(p)[0]:
            g.setdefault(m['id'], (m, {}))[1][p] = m['level'][p]
    g_sirali = sorted(g.values(), key=lambda x: (min(qs.LV[v] for v in x[1].values()), x[0]['id']))
    out = [dict(id=KURUM, ad='Kurum (G bloğu)', profiller=profiller,
                maddeler=[(m, '/'.join(f'{p}:{v}' for p, v in lv.items())) for m, lv in g_sirali])]
    for s in sistemler:
        out.append(dict(id=s['id'], ad=s['ad'], profiller=[s['profil']],
                        maddeler=[(m, m['level'][s['profil']]) for m in framework.qs_maddeleri(s['profil'])[1]]))
    return out


def bul(birim_listesi, birim_id, madde_id):
    """(birim, madde, seviye, önceki (birim, madde_id), sonraki (birim, madde_id)) ya da None."""
    sira = [(b, m, lv) for b in birim_listesi for m, lv in b['maddeler']]
    for n, (b, m, lv) in enumerate(sira):
        if b['id'] == birim_id and m['id'] == madde_id:
            onceki = (sira[n - 1][0]['id'], sira[n - 1][1]['id']) if n > 0 else None
            sonraki = (sira[n + 1][0]['id'], sira[n + 1][1]['id']) if n + 1 < len(sira) else None
            return b, m, lv, onceki, sonraki
    return None


# ------------------------------------------------------------------ madde bloğu
def bos_blok(madde):
    return dict(gorusme_notu='', na_reason=None,
                kontroller={c['id']: dict(cevap=None, durum='bos', **{'not': ''}, kanit=[]) for c in qs_kontrolleri(madde)})


def tamamla(madde, blok):
    """Eksik alanları doldurulmuş kopya (eski dosyalar ve yeni kontroller için)."""
    b = bos_blok(madde)
    if blok:
        b.update({k: v for k, v in blok.items() if k != 'kontroller'})
        for cid, k in (blok.get('kontroller') or {}).items():
            b['kontroller'][cid] = dict(b['kontroller'].get(cid, {}), **k)
    return b


def c1_cevabi(blok):
    return (blok['kontroller'].get('c1') or {}).get('cevap')


def etkin_durumlar(madde, blok):
    """{kontrol: bos | cevaplandi | atlandi | otomatik-atlandi | kapali} — ekranda görünen durum."""
    c1 = c1_cevabi(blok)
    out = {}
    for c in qs_kontrolleri(madde):
        k = blok['kontroller'][c['id']]
        if c['kind'] == 'exist':
            out[c['id']] = k['durum']
        elif c1 == NA:
            out[c['id']] = 'kapali'
        elif k['durum'] in ('bos', 'atlandi') and c1 == 'H':
            out[c['id']] = 'otomatik-atlandi'
        else:
            out[c['id']] = k['durum']
    return out


def madde_durumu(madde, blok):
    """bos → not-alindi (bir şey girilmiş, cevap eksik) → tamam; kullanıcı atladıysa atlandi."""
    if blok is None:
        return 'bos'
    c1 = c1_cevabi(blok)
    etkin = etkin_durumlar(madde, blok)
    if c1 == NA:
        return 'tamam' if (blok.get('na_reason') or '').strip() else 'not-alindi'
    if all(d in ('cevaplandi', 'otomatik-atlandi') for d in etkin.values()):
        return 'tamam'
    if 'atlandi' in etkin.values():
        return 'atlandi'
    dolu = (blok.get('gorusme_notu') or '').strip() or any(
        k.get('cevap') or (k.get('not') or '').strip() or k.get('kanit') for k in blok['kontroller'].values())
    return 'not-alindi' if dolu else 'bos'


def tespit(madde, blok, ref_date):
    """Durum tespiti (K7): kontrol.score ve check_met ile. {puan, karsilanmayan}."""
    cevap = {cid: (k.get('cevap') or '') for cid, k in blok['kontroller'].items()}
    puan = kontrol.score(madde, cevap, qs=True, ref_date=ref_date)
    eksik = [] if puan in ('NA', 'NE') else [
        c['id'] for c in qs_kontrolleri(madde) if not kontrol.check_met(c, cevap.get(c['id']), madde, ref_date)]
    return dict(puan=puan, karsilanmayan=eksik)


# ------------------------------------------------------------------ değişiklikler
class Gecersiz(ValueError):
    pass


def formdan(madde, eski, form):
    """Formdaki madde alanlarından yeni blok. c1 = NA iken diğer kontroller formda kapalıdır
    (gönderilmez); saklı değerleri korunur."""
    blok = tamamla(madde, eski)
    blok['gorusme_notu'] = str(form.get('gorusme_notu', '')).strip('\n')[:20000]
    c1_yeni = form.get('cevap_c1') or None
    for c in qs_kontrolleri(madde):
        cid, k = c['id'], blok['kontroller'][c['id']]
        if c1_yeni == NA and c['kind'] != 'exist':
            continue
        cevap = form.get(f'cevap_{cid}') or None
        if cevap is not None and cevap not in CEVAPLAR and not (cevap == NA and c['kind'] == 'exist'):
            raise Gecersiz(f'{cid}: geçersiz cevap {cevap!r}')
        k['cevap'] = cevap
        k['durum'] = 'cevaplandi' if cevap else ('atlandi' if k['durum'] == 'atlandi' else 'bos')
        k['not'] = str(form.get(f'not_{cid}', '')).strip()[:2000]
        k['kanit'] = [dict(ref=r.strip()) for r in str(form.get(f'kanit_{cid}', '')).split(';') if r.strip()][:20]
    blok['na_reason'] = (str(form.get('na_reason', '')).strip()[:500] or None) if c1_yeni == NA else None
    return blok


def atla(madde, eski, kontrol_id=None):
    """Bir kontrolü ya da maddenin cevaplanmamış bütün kontrollerini "sonra döneceğim" yapar (K4)."""
    blok = tamamla(madde, eski)
    for cid, k in blok['kontroller'].items():
        if (kontrol_id is None and k['durum'] == 'bos') or cid == kontrol_id:
            k.update(cevap=None, durum='atlandi')
    return blok


def kontrol_satirlari(madde, blok):
    """Ekran için kontrol satırları: metin kontrol.py'den, durum hesaplanmış."""
    etkin = etkin_durumlar(madde, blok)
    out = []
    for c in qs_kontrolleri(madde):
        k = blok['kontroller'][c['id']]
        out.append(dict(id=c['id'], tur=kontrol.KIND[c['kind']]['tr'], metin=kontrol.check_line(c, madde),
                        varlik=c['kind'] == 'exist', cevap=k.get('cevap'), durum=etkin[c['id']],
                        **{'not': k.get('not') or ''}, kanit='; '.join(x['ref'] for x in k.get('kanit') or [])))
    return out


def terimler(madde):
    tm = framework.terimler()
    ids = sorted({x for c in qs_kontrolleri(madde) for x in c.get('terms', [])})
    return [dict(id=x, ad=tm[x]['term']['tr'], tanim=' '.join(tm[x]['definition']['tr'].split())) for x in ids]


def metin(x):
    return ' '.join(str(x['tr']).split()) if x else ''

