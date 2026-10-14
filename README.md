# Lecta Sovereign AI Control Framework

Lecta Intelligence Lab'in yapay zekâ yönetişimi ve egemenlik kontrol çerçevesi: ölçüm aracı, şablon kütüphanesi ve ilk sürümün arşivi.

**Güncel sürüm:** `v1.0-draft` (Ekim 2026) — 29 onaylı madde, Quick Scan (AS-01) kiti, 13 şablon.

> Lecta denetlemez, denetime hazırlar. Bu repodaki araçlar hazırlık ölçer; denetim görüşü ya da sertifika üretmez.

## İçerik

| Dizin | Ne var |
|---|---|
| [`measurement-tool/`](measurement-tool/README.md) | Ölçüm aracı: YAML madde kaynağı, şema, betikler, Quick Scan kiti, üretilmiş rehber ve tablolar. **Başlangıç noktası** |
| [`templates/`](templates/README.md) | Şablon kütüphanesi: 13 yönetişim belgesi (md master + Word) |
| [`archive/v0-guardrails/`](archive/v0-guardrails/README.md) | Çerçevenin ilk sürümü (Sovereign AI Guardrails, Nisan–Mayıs 2026), salt okunur |
| [`ILK-ADIMLAR.md`](ILK-ADIMLAR.md) | Yeni katılan için başlangıç |
| [`CHANGELOG.md`](CHANGELOG.md) | Sürüm notları |

## Çalışma kuralları

- **Kaynak YAML'dır.** Maddeler `measurement-tool/source/*.yaml`, şablonlar `templates/md/` altında. `output/` ve `templates/docx/` betikle üretilir; elle düzenlenmez.
- **Her değişiklik bir dal ve Pull Request ile girer.** `main` dalına doğrudan yazılmaz.
- **Sürüm.** Her değişiklik `measurement-tool/source/meta.yaml` değişiklik kaydına bir satır ekler. Yayımlanan sürümler `vX.Y` etiketiyle işaretlenir ve `CHANGELOG.md` dosyasına yazılır. Değerlendirme kayıtları hangi sürümle yapıldığını bu etiketle belirtir.
- **Müşteri verisi bu repoya girmez.** Değerlendirme kayıtları müşteri klasöründe tutulur.
- **Açıklık.** İçerik Lecta know-how'ıdır; varsayılan olarak paylaşılmaz.

## Gereken araçlar

Python 3 (`pyyaml`, `openpyxl`, `python-docx`) ve `pandoc`:

```
pip install pyyaml openpyxl python-docx
brew install pandoc
```

Komutlar: [`measurement-tool/README.md`](measurement-tool/README.md) → "Dosyalar ve komutlar".

## İlgili repo

Kurumsal belgeler, marka ve Lab çalışmaları: `gokhaneryol/lecta-corp`.
