"""Lecta ölçüm aracı — kontrol listesi ve sabit puanlama kuralı (schema.md 5.5).

Ortak kütüphane: qs.py ve inceleme.py buradan kullanır. Komut satırı aracı değildir.

Bir maddenin `checks` alanı varsa puan elle verilmez, kontrol cevaplarından hesaplanır:
  0  varlık kontrolü (c1) karşılanmıyor
  1  c1 karşılanıyor, temel kontrollerden en az biri karşılanmıyor
  2  tüm temel kontroller karşılanıyor
  3  2 + tüm sürdürme kontrolleri karşılanıyor (madde sürdürme kontrolü taşımıyorsa 3 verilmez)

Cevaplar:
  binary  E (evet) | H (hayır) | B (bilmiyor)
  ratio   "a/b" (ör. 7/7) ya da QS'de E/H/B         eşik: min (0–1)
  date    YYYY-MM-DD ya da QS'de E/H/B              eşik: max_months | max_days
  count   tam sayı ya da QS'de E/H/B                 eşik: min
  Her türde: B = bilmiyor, karşılanmıyor sayılır. c1 = B ise madde NE olur.
  c1 = NA ise madde NA olur (gerekçe na_reason alanına).
"""
import datetime as dt
import os

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'source')

KIND = {'exist': {'tr': 'varlık', 'en': 'existence'},
        'core': {'tr': 'temel', 'en': 'core'},
        'sustain': {'tr': 'sürdürme', 'en': 'sustain'}}
YES, NO, DK = 'E', 'H', 'B'


def terms():
    with open(os.path.join(SRC, 'terms.yaml'), encoding='utf-8') as fh:
        return {t['id']: t for t in yaml.safe_load(fh)['terms']}


def _months_between(d, ref):
    return (ref.year - d.year) * 12 + (ref.month - d.month) - (1 if ref.day < d.day else 0)


def threshold_text(c, item, lang='tr'):
    th = c.get('threshold') or {}
    ri = item.get('review_interval')
    if c['type'] == 'binary':
        return ''
    if c['type'] == 'ratio':
        pct = int(round(th.get('min', 1.0) * 100))
        s = th.get('sample')
        if lang == 'tr':
            return f'{s}/{s}' if s and pct == 100 else '%100 (hepsi)' if pct == 100 else f'en az %{pct}'
        return f'{s}/{s}' if s and pct == 100 else '100% (all)' if pct == 100 else f'at least {pct}%'
    if c['type'] == 'date':
        m = th.get('max_months')
        if m == 'review_interval':
            m = ri
        if m:
            return f'≤ {m} ay' if lang == 'tr' else f'≤ {m} months'
        return f"≤ {th['max_days']} gün" if lang == 'tr' else f"≤ {th['max_days']} days"
    if c['type'] == 'count':
        return f"≥ {th['min']}"
    raise ValueError(c['type'])


def check_met(c, answer, item, ref_date=None):
    """True/False; B ve boş = False. Sayısal cevap eşikle karşılaştırılır."""
    a = str(answer or '').strip().upper()
    if a in ('', DK, NO):
        return False
    if a == YES:
        return True
    th = c.get('threshold') or {}
    if c['type'] == 'ratio' and '/' in a:
        x, y = (int(v) for v in a.split('/'))
        return y > 0 and x / y >= th.get('min', 1.0) and (not th.get('sample') or y >= th['sample'])
    if c['type'] == 'date':
        d = dt.date.fromisoformat(a)
        ref = ref_date or dt.date.today()
        m = th.get('max_months')
        if m == 'review_interval':
            m = item.get('review_interval')
        return _months_between(d, ref) < m if m else (ref - d).days <= th['max_days']
    if c['type'] == 'count':
        return int(a) >= th['min']
    raise ValueError(f"{item['id']} {c['id']}: anlaşılmayan cevap {answer!r}")


def score(item, answers, qs=False, ref_date=None):
    """answers: {check_id: cevap}. qs=True ise yalnız `qs: true` kontroller hesaba girer.
    Dönüş: '0'..'3' | 'NA' | 'NE'."""
    cs = [c for c in item['checks'] if c.get('qs', True) or not qs]
    ex = [c for c in cs if c['kind'] == 'exist']
    a1 = str(answers.get(ex[0]['id'], '')).strip().upper()
    if a1 == 'NA':
        return 'NA'
    if a1 in ('', DK):
        return 'NE'
    met = {c['id']: check_met(c, answers.get(c['id']), item, ref_date) for c in cs}
    if not met[ex[0]['id']]:
        return '0'
    if not all(met[c['id']] for c in cs if c['kind'] == 'core'):
        return '1'
    sus = [c for c in cs if c['kind'] == 'sustain']
    return '3' if sus and all(met[c['id']] for c in sus) else '2'


def ids(cs, kind):
    x = [c['id'] for c in cs if c['kind'] == kind]
    return x[0] if len(x) == 1 else f'{x[0]}–{x[-1]}' if x else ''


def rubric(item, lang='tr'):
    """Elle yazılmış rubric varsa onu, `checks` varsa kurala göre üretilmiş metni döndürür. {0..3: str}"""
    ri = item.get('review_interval')
    if 'checks' not in item:
        return {k: ' '.join(str(item['rubric'][k][lang]).split())
                .replace('review_interval', (f'{ri} ay' if lang == 'tr' else f'{ri} months') if ri else 'review_interval')
                for k in (0, 1, 2, 3)}
    cs = item['checks']
    e, c, s = ids(cs, 'exist'), ids(cs, 'core'), ids(cs, 'sustain')
    if lang == 'tr':
        out = {0: f'Varlık kontrolü ({e}) karşılanmıyor.',
               1: f'{e} karşılanıyor; temel kontrollerden ({c}) en az biri karşılanmıyor.',
               2: f'{e} ve tüm temel kontroller ({c}) karşılanıyor.',
               3: f'2 ve tüm sürdürme kontrolleri ({s}) karşılanıyor.' if s else '— (bu maddede 3 tanımlı değil)'}
    else:
        out = {0: f'Existence check ({e}) not met.',
               1: f'{e} met; at least one core check ({c}) not met.',
               2: f'{e} and all core checks ({c}) met.',
               3: f'2 and all sustain checks ({s}) met.' if s else '— (3 not defined for this item)'}
    return out


def check_line(c, item, lang='tr'):
    th = threshold_text(c, item, lang)
    ri = item.get('review_interval')
    txt = ' '.join(str(c['text'][lang]).split())
    if ri:
        txt = txt.replace('review_interval', f'{ri} ay' if lang == 'tr' else f'{ri} months')
    return txt + (f' **[{th}]**' if th else '')
