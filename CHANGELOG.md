# Sürüm notları

## v1.0-draft — Ekim 2026

**Ölçüm aracı**

- Şema: madde alanları, ID kuralı (`KATMAN-AŞAMA-NN`, `G-ALAN-NN`), iki dilli metin alanları, 0–3 rubric, NA/NE, kümülatif geçiş kapısı, G bloğunun sistem seviyesini sınırlaması, `declared`/`verified` dayanağı.
- 29 onaylı madde:
  - G bloğu: 15 madde.
  - Matris: CON 6, HYG 5, IDE 2, TRA 1.
- Quick Scan (AS-01) kiti:
  - kesit: 17 madde/profil;
  - gösterge seviye kuralı (L1 tavanı);
  - görüşme rehberleri;
  - puanlama tablosu;
  - seviye ve risk hesabı (`qs.py`);
  - memo şablonu.
- İnceleme ve tablo üretimi (`inceleme.py`).

**Şablon kütüphanesi**

- 13 şablon (TPL-01…13), G bloğu rubric 2 ölçütlerine göre; md master + Word, `docx_uret.py`.

## v0 — Nisan–Mayıs 2026

- Sovereign AI Guardrails: 36 kontrol hücresi (6 katman × 6 pipeline aşaması), L0–L6, 24 regülasyon eşlemesi, araç kaydı, kurulum rehberi. Arşiv: `archive/v0-guardrails/`.
