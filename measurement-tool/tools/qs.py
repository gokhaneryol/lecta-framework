#!/usr/bin/env python3
"""Lecta ölçüm aracı — Quick Scan (AS-01) yardımcı betiği.

Tek kaynak: ../source/*.yaml (quick_scan: true maddeler). Hiçbir madde metni burada yazılmaz.

Komutlar:
  rehber   --profil CE|SOV [--out DOSYA]          Türkçe görüşme rehberi (md)
  puanlama --kurum AD --sistem "Ad:CE" [--sistem "Ad2:SOV"] [--out DOSYA]
                                                  Boş puanlama tablosu (csv)
  seviye   PUAN.csv [--out DOSYA]                 Gösterge seviye + en kritik 5 risk (md)

Kurallar (schema.md 5.2–5.3, 03-quick-scan-kesiti.md):
  - Gösterge seviye yalnız kesitteki maddelerle, kapı kuralıyla hesaplanır; L1'in üstüne çıkmaz.
  - Kapı: level <= Lk olan tüm uygulanabilir maddeler >= 2. NA hariç; NE ya da boş = geçmez.
  - G bloğu sistem seviyesini sınırlar: raporlanan = min(sistem, G[profil]).
  - Quick Scan'de en çok 2 sistem.
"""
import argparse, csv, glob, os, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'source')
LV = {f'L{i}': i for i in range(7)}
QS_CAP = 1  # gösterge seviye L1'i aşmaz
CE_CHAIN = ['G-POL-02', 'G-INV-02', 'G-SUP-01', 'CON-INF-02', 'HYG-PRM-01']
FIELDS = ['unit', 'unit_type', 'profile', 'item_id', 'title_tr', 'level', 'score',
          'basis', 'na_reason', 'note', 'evidence_ref', 'assessor', 'reviewer']


def load_items():
    items = []
    for f in sorted(glob.glob(os.path.join(SRC, '*.yaml'))):
        if os.path.basename(f) in ('meta.yaml', '_template.yaml'):
            continue
        with open(f, encoding='utf-8') as fh:
            items += yaml.safe_load(fh)['items']
    return items


def meta():
    with open(os.path.join(SRC, 'meta.yaml'), encoding='utf-8') as fh:
        return yaml.safe_load(fh)


def qs_items(profile):
    out = [i for i in load_items()
           if i.get('quick_scan') and i['level'].get(profile) is not None
           and i.get('status') != 'deprecated']
    gov = [i for i in out if i['block'] == 'governance']
    mat = [i for i in out if i['block'] == 'matrix']
    key = lambda i: (LV[i['level'][profile]], i['id'])
    return sorted(gov, key=key), sorted(mat, key=key)


def t(x):
    return ' '.join(str(x['tr']).split())


# ------------------------------------------------------------------ rehber
def cmd_rehber(a):
    gov, mat = qs_items(a.profil)
    m = meta()
    pname = m['profiles'][a.profil]['name']
    L = []
    L.append(f'# Quick Scan Görüşme Rehberi — {pname} profili\n')
    L.append(f"*{m['framework']} · {m['version']} · kaynaktan üretildi (`tools/qs.py`) — elle düzenlemeyin*\n")
    L.append('## Görüşmeye başlarken (okunacak metin)\n')
    L.append('> Bu görüşme bir **Hızlı Tarama**dır: sorularımız beyanınıza dayanır, kanıt incelemesi yapılmaz. '
             'Sonuç bir **gösterge hazırlık seviyesidir**; denetim görüşü ya da belge değildir. '
             'Bilmediğiniz soruya "bilmiyorum" demeniz en doğru cevaptır ve öyle kaydedilir.\n')
    L.append('**Puanlama notu:** Her maddede beyana göre 0–3 verilir (`basis: declared`). '
             'Katılımcı cevabı bilmiyorsa **NE**; madde kurumda yoksa ve uygulanabilirlik ölçütü karşılanmıyorsa **NA** (gerekçe yazılır). '
             'Kanıt istenmez; katılımcı kendiliğinden gösterirse `evidence_ref` alanına not edilir.\n')
    L.append(f'**Süre:** {len(gov)} kurum + {len(mat)} sistem maddesi (sistem başına) · ~4 dk/madde · 1 sistemle ~{4*(len(gov)+len(mat))+15} dk.\n')

    def block(title, items):
        L.append(f'## {title}\n')
        for n, i in enumerate(items, 1):
            L.append(f"### {i['id']} · {t(i['title'])}  `{i['level'][a.profil]}`\n")
            L.append(f"**Soru:** {t(i['qs_question'])}\n")
            L.append(f"**Derinleştirme:** {t(i['question'])}\n")
            L.append(f"**Uygulanabilirlik:** {t(i['applicability'])}\n")
            L.append('| Puan | Ölçüt |\n|---|---|')
            ri = i.get('review_interval')
            for k in (0, 1, 2, 3):
                txt = t(i['rubric'][k])
                if ri:
                    txt = txt.replace('review_interval', f'{ri} ay')
                L.append(f"| {k} | {txt} |")
            L.append('')
            ev = '; '.join(f"`{e['type']}` {' '.join(e['tr'].split())}" for e in i['evidence'])
            L.append(f'*AS-02\'de istenecek kanıt:* {ev}\n')
    block('Bölüm A — Kurum (G bloğu, kurum başına bir kez)', gov)
    block('Bölüm B — Sistem (her sistem için ayrı; en çok 2 sistem)', mat)
    write(a.out, '\n'.join(L))


# ------------------------------------------------------------------ puanlama
def cmd_puanlama(a):
    systems = []
    for s in a.sistem:
        name, _, prof = s.rpartition(':')
        if prof not in ('CE', 'SOV') or not name:
            sys.exit(f'--sistem "Ad:CE|SOV" biçiminde olmalı: {s}')
        systems.append((name, prof))
    if len(systems) > 2:
        sys.exit("Quick Scan'de en çok 2 sistem (03-quick-scan-kesiti.md).")
    rows = []
    # G maddeleri: kurum başına bir kez; kullanılan profillerin hepsi için seviye yazılır
    profs = sorted({p for _, p in systems})
    gov_ids = {}
    for p in profs:
        for i in qs_items(p)[0]:
            gov_ids.setdefault(i['id'], (i, {}))[1][p] = i['level'][p]
    for iid, (i, lv) in sorted(gov_ids.items(), key=lambda kv: kv[0]):
        rows.append(dict(unit=a.kurum, unit_type='KURUM', profile='/'.join(lv),
                         item_id=iid, title_tr=t(i['title']),
                         level='/'.join(f'{p}:{v}' for p, v in lv.items()), basis='declared'))
    for name, p in systems:
        for i in qs_items(p)[1]:
            rows.append(dict(unit=name, unit_type='SISTEM', profile=p, item_id=i['id'],
                             title_tr=t(i['title']), level=i['level'][p], basis='declared'))
    out = open(a.out, 'w', newline='', encoding='utf-8') if a.out else sys.stdout
    w = csv.DictWriter(out, fieldnames=FIELDS)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, '') for k in FIELDS})
    if a.out:
        out.close(); print(f'yazıldı: {a.out} ({len(rows)} satır)')


# ------------------------------------------------------------------ seviye
def passed(r):
    s = r['score'].strip().upper()
    if s == 'NA':
        return None          # hesap dışı
    return s in ('2', '3')


def gate(rows, levelof):
    """En yüksek k (0..QS_CAP) için level<=k maddelerin hepsi geçiyorsa k; L0 bile geçmezse -1."""
    best = -1
    for k in range(QS_CAP + 1):
        rel = [r for r in rows if levelof(r) <= k and passed(r) is not None]
        if all(passed(r) for r in rel):
            best = k
        else:
            break
    return best


def lvname(k):
    return 'L0 altı' if k < 0 else f'L{k}'


def cmd_seviye(a):
    with open(a.csv, encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    blank = [r['item_id'] + '@' + r['unit'] for r in rows if not r['score'].strip()]
    gov = [r for r in rows if r['unit_type'] == 'KURUM']
    sysunits = []
    for r in rows:
        if r['unit_type'] == 'SISTEM' and (r['unit'], r['profile']) not in sysunits:
            sysunits.append((r['unit'], r['profile']))

    def g_level(p):
        def lv(r):
            d = dict(x.split(':') for x in r['level'].split('/'))
            return LV[d[p]] if p in d else 99
        return gate([r for r in gov if r['level'] and p in r['level']], lv)

    L = ['# Quick Scan — Gösterge Seviye Hesabı\n',
         f"*Kaynak: `{os.path.basename(a.csv)}` · `tools/qs.py seviye` ile üretildi*\n"]
    if blank:
        L.append(f'> ⚠️ Boş puan ({len(blank)}): ' + ', '.join(blank) + ' — boş, NE gibi işlem görür.\n')
    L.append('| Birim | Profil | Matris (gösterge) | G bloğu (gösterge) | **Raporlanan** |')
    L.append('|---|---|---|---|---|')
    for name, p in sysunits:
        sr = [r for r in rows if r['unit'] == name and r['unit_type'] == 'SISTEM']
        ms = gate(sr, lambda r: LV[r['level']])
        gs = g_level(p)
        L.append(f'| {name} | {p} | {lvname(ms)} | {lvname(gs)} | **{lvname(min(ms, gs))}** |')
    L.append('')
    L.append(f"*Gösterge seviye beyana dayalıdır ve {len(gov)} kurum + sistem başına "
             f"{len(rows)-len(gov) if not sysunits else len([r for r in rows if r['unit']==sysunits[0][0] and r['unit_type']=='SISTEM'])} "
             "maddelik alt kümeyle hesaplanmıştır; L1'in üstünde seviye üretmez. "
             "Doğrulanmış seviye için Detailed Scan (AS-02) gerekir.*\n")

    # En kritik 5 risk — deterministik sıralama
    def sc(r):
        s = r['score'].strip().upper()
        return 0 if s in ('', 'NE', '0') else int(s) if s.isdigit() else 9
    def lvnum(r):
        if r['unit_type'] == 'SISTEM':
            return LV[r['level']]
        return min(LV[x.split(':')[1]] for x in r['level'].split('/'))
    def chain(r):
        ce = 'CE' in r['profile'].split('/')
        return 0 if (ce and r['item_id'] in CE_CHAIN) else 1
    cand = [r for r in rows if passed(r) is False]
    cand.sort(key=lambda r: (sc(r), lvnum(r), chain(r), r['unit_type'] != 'KURUM', r['item_id']))
    L.append('## En kritik 5 risk (sıralama kuralı: puan ↑ · seviye ↑ · CE zinciri önce · kurum önce · ID)\n')
    L.append('| # | Madde | Birim | Seviye | Puan | Not |\n|---|---|---|---|---|---|')
    for n, r in enumerate(cand[:5], 1):
        L.append(f"| {n} | {r['item_id']} · {r['title_tr']} | {r['unit']} | {r['level']} | "
                 f"{r['score'] or 'boş'} | {r['note']} |")
    L.append(f'\n*Geçmeyen madde sayısı: {len(cand)}. Tamamı memo ekindeki tabloda.*\n')
    write(a.out, '\n'.join(L))


def write(path, text):
    if path:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text + '\n')
        print(f'yazıldı: {path}')
    else:
        print(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    r = sp.add_parser('rehber'); r.add_argument('--profil', choices=['CE', 'SOV'], required=True); r.add_argument('--out')
    p = sp.add_parser('puanlama'); p.add_argument('--kurum', required=True)
    p.add_argument('--sistem', action='append', required=True); p.add_argument('--out')
    s = sp.add_parser('seviye'); s.add_argument('csv'); s.add_argument('--out')
    a = ap.parse_args()
    {'rehber': cmd_rehber, 'puanlama': cmd_puanlama, 'seviye': cmd_seviye}[a.cmd](a)


if __name__ == '__main__':
    main()
