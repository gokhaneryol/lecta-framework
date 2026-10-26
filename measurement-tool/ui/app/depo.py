"""Değerlendirme verisinin dosya katmanı (TASARIM.md K10, §5.3).

Veritabanı yok; her birim bir YAML dosyasıdır.
  - Atomik yazma: aynı dizinde geçici dosya + fsync + os.replace. Yarım yazılmış dosya oluşmaz.
  - Dosya başına kilit: `.<ad>.lock` üzerinde fcntl.flock (süreçler ve thread'ler arası).
  - İyimser sürüm kontrolü: sürüm = dosya içeriğinin sha256'sı. Form okuduğu sürümü taşır;
    dosya o arada değiştiyse yazma reddedilir (Cakisma) ve kullanıcıya "yenile" denir.
"""
import contextlib
import fcntl
import hashlib
import os
import tempfile

import yaml

YOK = ''   # var olmayan dosyanın sürümü


class Cakisma(Exception):
    """Dosya, okunduğu sürümden bu yana başkası tarafından değiştirildi."""

    def __init__(self, yol, beklenen, mevcut):
        super().__init__(f'{yol}: sürüm değişmiş (beklenen {beklenen[:8] or "yok"}, mevcut {mevcut[:8] or "yok"})')
        self.yol, self.beklenen, self.mevcut = yol, beklenen, mevcut


def _ozet(b):
    return hashlib.sha256(b).hexdigest()


def _ham(yol):
    try:
        with open(yol, 'rb') as fh:
            return fh.read()
    except FileNotFoundError:
        return None


class Depo:
    """Kök dizin (LECTA_DATA) altındaki dosyalar. Yollar köke göre görelidir; kök dışına çıkılamaz."""

    def __init__(self, kok):
        self.kok = os.path.realpath(kok)

    def yol(self, *parcalar):
        p = os.path.realpath(os.path.join(self.kok, *parcalar))
        if p != self.kok and not p.startswith(self.kok + os.sep):
            raise ValueError(f'kök dizin dışında yol: {os.path.join(*parcalar)}')
        return p

    @contextlib.contextmanager
    def kilit(self, *parcalar):
        p = self.yol(*parcalar)
        d, ad = os.path.split(p)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, f'.{ad}.lock'), 'a') as fh:
            fcntl.flock(fh, fcntl.LOCK_EX)
            try:
                yield p
            finally:
                fcntl.flock(fh, fcntl.LOCK_UN)

    def surum(self, *parcalar):
        b = _ham(self.yol(*parcalar))
        return YOK if b is None else _ozet(b)

    def oku(self, *parcalar):
        """(veri, sürüm). Dosya yoksa (None, YOK)."""
        b = _ham(self.yol(*parcalar))
        if b is None:
            return None, YOK
        return yaml.safe_load(b.decode('utf-8')), _ozet(b)

    def yaz(self, veri, *parcalar, beklenen):
        """Veriyi atomik yazar, yeni sürümü döndürür.

        beklenen: okunan sürüm (yeni dosya için YOK). Dosya o arada değiştiyse Cakisma.
                  None verilirse kontrol yapılmaz (yalnız sistemin kendi yazdığı dosyalar için).
        """
        b = yaml.safe_dump(veri, allow_unicode=True, sort_keys=False, default_flow_style=False).encode('utf-8')
        with self.kilit(*parcalar) as p:
            mevcut = _ham(p)
            mevcut = YOK if mevcut is None else _ozet(mevcut)
            if beklenen is not None and beklenen != mevcut:
                raise Cakisma(p, beklenen, mevcut)
            d, ad = os.path.split(p)
            fd, gecici = tempfile.mkstemp(dir=d, prefix=f'.{ad}.', suffix='.tmp')
            try:
                with os.fdopen(fd, 'wb') as fh:
                    fh.write(b)
                    fh.flush()
                    os.fsync(fh.fileno())
                os.replace(gecici, p)
            except BaseException:
                with contextlib.suppress(FileNotFoundError):
                    os.unlink(gecici)
                raise
            dfd = os.open(d, os.O_RDONLY)
            try:
                os.fsync(dfd)
            finally:
                os.close(dfd)
        return _ozet(b)
