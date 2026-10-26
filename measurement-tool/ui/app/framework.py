"""Framework kaynağına (source/*.yaml) ve hesap koduna (tools/qs.py, tools/kontrol.py) tek giriş.

Arayüz madde metni yazmaz, puan hesaplamaz: hepsi buradan, mevcut fonksiyonlarla gelir (TASARIM.md K7, §5.1).
"""
import functools
import os
import sys

TOOLS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools')
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

import kontrol  # noqa: E402
import qs  # noqa: E402
import yaml  # noqa: E402


@functools.lru_cache(maxsize=1)
def surum():
    return qs.meta()['version']


@functools.lru_cache(maxsize=1)
def org_fields():
    with open(os.path.join(kontrol.SRC, 'org_fields.yaml'), encoding='utf-8') as fh:
        return yaml.safe_load(fh)['fields']
