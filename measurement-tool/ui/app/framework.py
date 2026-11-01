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


# Kaynak imajla birlikte sabittir; her istekte YAML'ı yeniden okumamak için önbellek.
# Dönen nesneler paylaşılır: çağıran değiştirmez.
@functools.lru_cache(maxsize=4)
def qs_maddeleri(profil):
    """qs.qs_items(profil) → (G maddeleri, matris maddeleri), aynı sırayla."""
    return qs.qs_items(profil)


@functools.lru_cache(maxsize=1)
def terimler():
    return kontrol.terms()


@functools.lru_cache(maxsize=1)
def maddeler():
    """{madde_id: madde} — bütün maddeler (qs.load_items)."""
    return {m['id']: m for m in qs.load_items()}


def commit():
    """Arayüzün çalıştığı imajın framework commit'i."""
    from flask import current_app
    return current_app.config['LECTA_FRAMEWORK_COMMIT']
