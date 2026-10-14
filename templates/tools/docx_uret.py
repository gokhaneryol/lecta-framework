#!/usr/bin/env python3
"""Şablon kütüphanesi: md master -> docx (müşteriye verilecek sürüm).

  python3 docx_uret.py            # tüm şablonlar
  python3 docx_uret.py TPL-04     # tek şablon

- "Lecta şablon notu" blockquote'u DOCX'e girmez (iç not; md master'da kalır).
- Biçim: reference.docx (Calibri, lacivert başlıklar). Tablo kenarlıkları eklenir.
"""
import glob, os, re, subprocess, sys, tempfile
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, '..', 'md')
OUT = os.path.join(HERE, '..', 'docx')
REF = os.path.join(HERE, 'reference.docx')


def strip_note(text):
    lines, out, skip = text.split('\n'), [], False
    lines = [ln for ln in lines if not ln.startswith('date: ')]  # şablon tarihi müşteri belgesine basılmaz
    for ln in lines:
        if ln.startswith('> **Lecta şablon notu'):
            skip = True; continue
        if skip:
            if ln.startswith('>'):
                continue
            skip = False
        out.append(ln)
    return '\n'.join(out)


TOTAL = 9600  # twips, A4 kenar boşluklarıyla kullanılabilir genişlik


def widths(t):
    """Sütun genişliği içerik uzunluğuna göre; boş sütunlar da yazılabilir genişlik alır."""
    ncol = len(t.columns)
    w = []
    for c in range(ncol):
        lens = [len(r.cells[c].text) for r in t.rows]
        hdr = lens[0] if lens else 0
        body = max(lens[1:], default=0)
        w.append(min(60, max(14, hdr, body if body else 30)))
    tot = sum(w)
    tw = [int(TOTAL * x / tot) for x in w]
    grid = t._tbl.tblGrid
    for gc, val in zip(grid.findall(qn('w:gridCol')), tw):
        gc.set(qn('w:w'), str(val))
    for r in t.rows:
        for c, val in zip(r.cells, tw):
            c.width = val * 635  # twip -> EMU


def borders(path):
    d = Document(path)
    for t in d.tables:
        widths(t)
        tblPr = t._tbl.tblPr
        for old in tblPr.findall(qn('w:tblW')):
            tblPr.remove(old)
        tw = OxmlElement('w:tblW'); tw.set(qn('w:w'), str(TOTAL)); tw.set(qn('w:type'), 'dxa'); tblPr.append(tw)
        lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
        b = OxmlElement('w:tblBorders')
        for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            el = OxmlElement(f'w:{e}')
            el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), '4'); el.set(qn('w:color'), '8A9BB0')
            b.append(el)
        tblPr.append(b)
    d.save(path)


def build(src):
    name = os.path.splitext(os.path.basename(src))[0]
    dst = os.path.join(OUT, name + '.docx')
    with open(src, encoding='utf-8') as fh:
        text = strip_note(fh.read())
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as tmp:
        tmp.write(text); tp = tmp.name
    subprocess.run(['pandoc', tp, '-f', 'markdown', '-o', dst, f'--reference-doc={REF}'], check=True)
    os.unlink(tp)
    borders(dst)
    print('yazıldı:', os.path.relpath(dst, os.path.join(HERE, '..')))


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pat = sys.argv[1] + '*' if len(sys.argv) > 1 else 'TPL-*'
    for f in sorted(glob.glob(os.path.join(MD, pat + '.md'))):
        build(f)
