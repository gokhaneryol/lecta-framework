# Lecta Şablon Kütüphanesi

*Lecta know-how'ı — varsayılan olarak paylaşılmaz; iş kapsamında müşteriyle ya da anlaşmalı kanalla vaka bazında paylaşılır (katalog 0.2.2 açıklık ilkesi).*
*Sürüm 1.0-draft · 14 Ekim 2026 · framework: Lecta Sovereign AI Control Framework v1.0-draft*

## Ne için

Ölçüm aracının G bloğu maddeleri bir belgenin varlığını ve içeriğini ölçer. Bu şablonlar, her G maddesinin **rubric 2** ölçütünü karşılayacak biçimde yazıldı. Kullanım yerleri:
- **DS-03 AI Governance Policy Set:** kurumun G bloğu eksiklerini kapatmak (ana kullanım).
- **AS-01 / AS-02:** "iyi bir belge neye benzer" sorusuna örnek; memo'daki kapanış ölçütüne referans.
- **EN-02:** eğitimde kabul edilebilir kullanım ve olay bildirimi örnekleri.

**Güven zinciri:** Şablon bir başlangıç noktasıdır; doldurulmuş belge kurumun kendi belgesidir. Lecta kendi hazırladığı belgeye bağımsız değerlendirme notu vermez. Şablonlar hukuki görüş değildir. Yasal süre ve atıflar 14.10.2026'da doğrulandı; mevzuat değiştikçe güncellenir.

## Dizin

| ID | Şablon | G maddesi | Tür |
|---|---|---|---|
| TPL-01 | Yapay Zekâ Politikası | G-POL-01 | Politika |
| TPL-02 | AI Araçları Kabul Edilebilir Kullanım Kuralları (+ onaylı araç listesi) | G-POL-02 · G-LIT-01 | Kural seti |
| TPL-03 | AI Olay Prosedürü | G-INC-01 | Prosedür |
| TPL-04 | AI Olay Bildirim Formu | G-INC-01 | Form |
| TPL-05 | AI Sistem Envanteri | G-INV-01 · G-ROL-01 | Kayıt |
| TPL-06 | AI Sağlayıcı Değerlendirme Formu | G-SUP-01 | Form |
| TPL-07 | Egemenlik Testi Kaydı | G-SUP-02 | Form |
| TPL-08 | AI Sağlayıcı Sözleşme Maddeleri Kontrol Listesi | G-SUP-03 | Kontrol listesi |
| TPL-09 | AI Risk Değerlendirmesi | G-RSK-01 | Form |
| TPL-10 | AI Risk Sınıflandırma Kaydı | G-RSK-02 | Form |
| TPL-11 | AI Kişisel Veri Etki Değerlendirmesi | G-RSK-03 | Form |
| TPL-12 | Roller ve Sorumluluklar Matrisi (+ rol eğitimi) | G-ROL-01 · G-LIT-02 | Matris |
| TPL-13 | İnsan Gözetimi Prosedürü | G-OVS-01 | Prosedür |

**Şablonu olmayan G maddeleri:** G-INV-02 (AI trafiği görünürlüğü — teknik; AS-04 kitinde log gereksinim şablonu olarak gelecek) · G-LIT-01 eğitim içeriğinin kendisi (EN-02 materyali).

## Yapı ve kurallar

```
templates/
  README.md
  md/     ← MASTER. Düzenleme yalnız burada.
  docx/   ← Üretilen müşteri sürümü. Elle düzenlenmez.
  tools/docx_uret.py, reference.docx
```

- Her md'nin başında **"Lecta şablon notu"** kutusu var: hangi madde, hangi rubric ölçütü, yasal dayanaklar. Bu kutu **DOCX'e girmez**.
- `{{…}}` alanları müşteriye göre doldurulur.
- Şablonlar arası atıflar TPL ID'leriyle; müşteride kurumun belge numaralarıyla değiştirilir.
- Çapraz tutarlılık: dört AI olay türü (TPL-03/04/09), beş sağlayıcı konusu (TPL-06 ↔ G-SUP-01), beş sözleşme maddesi (TPL-08 ↔ G-SUP-03) framework maddeleriyle birebir aynıdır. Framework maddesi değişirse şablon da aynı oturumda güncellenir.
- DOCX üretimi: `cd templates/tools && python3 docx_uret.py` (tek şablon: `python3 docx_uret.py TPL-04`). Gerekli: pandoc, python-docx.

## Değişiklik kaydı

| Tarih | Değişiklik |
|---|---|
| 14 Ekim 2026 | İlk sürüm: 13 şablon (md + docx), G bloğu rubric 2 ölçütlerine göre |
