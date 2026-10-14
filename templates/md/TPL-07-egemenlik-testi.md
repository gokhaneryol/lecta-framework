---
title: "{{Kurum}} — Egemenlik Testi Kaydı"
id: TPL-07
g_items: [G-SUP-02]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-SUP-02, rubric 2 — üç soru kaynaklarıyla (Bölüm 2–4), sınır cevabı çıkış trafiği ya da yerleşim kanıtıyla (Bölüm 3, yalnız beyan yetmez), kritik sağlayıcı için çıkış planı (Bölüm 4). Rubric 3: çıkış planının tatbiki (Bölüm 5).
> **Kökeni:** AS-05'ten DS-04 modülüne taşınan egemenlik testi. "Kritik sağlayıcı" tanımı kurum tarafından Bölüm 1'de yapılmalı; tanım yoksa rubric 2 verilmez.

# 1. Kapsam

| | |
|---|---|
| Sağlayıcı / barındırma düzeni | |
| İlgili AI sistemleri (envanter no) | |
| Kritik sağlayıcı mı? | ☐ Evet ☐ Hayır — kurum tanımı: {{ör. kesintisi bir iş sürecini 1 iş gününden fazla durdurur ya da kişisel/gizli veri işler}} |
| Değerlendiren / tarih | |

# 2. Soru 1 — Hukuki yetki alanı

**Verinize hangi ülkenin hukuku, sağlayıcıyı erişim vermeye zorlayabilir?**

| | Cevap | Kaynak |
|---|---|---|
| Sözleşme tarafı şirket ve ülkesi | | Sözleşme |
| Nihai ana şirket ve ülkesi | | Ticaret sicili / yıllık rapor |
| Ana şirketin tabi olduğu, yabancı veri erişimine imkân veren düzenlemeler | | {{hukuk görüşü}} |
| Sağlayıcının kamu erişim talebi politikası ve şeffaflık raporu | | |

# 3. Soru 2 — Mimari sınır

**Veri, iddia edilen sınırın içinde mi işleniyor? Bunu yalnız beyanla değil gözlemle gösterin.**

| | Cevap | Kanıt |
|---|---|---|
| İddia edilen işleme sınırı (ülke / bölge / kurum veri merkezi) | | Sağlayıcı beyanı |
| Gözlem: AI çağrılarının gittiği uç noktaların konumu | | Ağ çıkış kayıtları, {{tarih aralığı}} |
| Destek, telemetri ve yedekleme akışları sınır dışına çıkıyor mu? | | Mimari belge / sağlayıcı yazılı cevabı |
| Şifreleme anahtarları kimde? | | |

# 4. Soru 3 — Bağımsız işletebilme / çıkış

**Sağlayıcı yarın hizmeti kesse ya da koşulları değiştirse devam edebilir misiniz?**

| | Cevap |
|---|---|
| Verinin (belgeler, indeksler, kayıtlar, ince ayar ağırlıkları) dışa aktarımı mümkün mü, hangi formatta? | |
| Alternatif sağlayıcı ya da kurum içi model seçeneği ve geçiş süresi tahmini | |
| Sözleşmede fesih sonrası veri iadesi/silme süresi | |
| **Çıkış planı** (kritik sağlayıcı için zorunlu): tetikleyici, adımlar, sorumlu, hedef süre | |

# 5. Sonuç ve tatbikat

| | |
|---|---|
| Egemenlik değerlendirmesi | ☐ Kabul ☐ Koşullu ☐ Kabul edilemez — gerekçe: |
| Çıkış planı tatbiki (masa başı / teknik) | Tarih: ___ · Sonuç: ___ |
| Sonraki gözden geçirme | En geç 12 ay: {{tarih}} |
