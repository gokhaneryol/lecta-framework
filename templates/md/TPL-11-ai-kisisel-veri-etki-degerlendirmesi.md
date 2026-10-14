---
title: "{{Kurum}} — AI Kişisel Veri Etki Değerlendirmesi"
id: TPL-11
g_items: [G-RSK-03]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-RSK-03, rubric 2 — tüm pipeline aşamalarında veri haritası (Bölüm 2), yurt dışı aktarım noktaları (Bölüm 3), sahipli önlemler (Bölüm 5), kayıtlı DPO görüşü (Bölüm 6). AS-07 çekirdek çıktısının biçimi budur.
> **Sınır:** Bölüm 4'teki hukuka uygunluk sebebi ve aktarım mekanizması alanları **hukuk danışmanı/ortağı tarafından** doldurulur; Lecta teknik analiz yapar, hukuki sonuç vermez. GDPR kapsamındaysa Art. 35(7)'deki asgari içerik ayrıca karşılanır: işlemenin sistematik tanımı, gereklilik ve orantılılık değerlendirmesi, kişilerin hak ve özgürlüklerine yönelik riskler, önlemler.

# 1. Sistem ve işleme

| | |
|---|---|
| Sistem / envanter no / sahip | |
| İşleme amacı | |
| İlgili kişi grupları ve yaklaşık sayı | |
| Kişisel veri kategorileri | |
| Özel nitelikli veri | ☐ Yok ☐ Var: ___ |
| Profil | ☐ Dış servis ☐ Kurum içi ☐ Hibrit |

# 2. Veri haritası — pipeline aşamaları

| Aşama | Hangi kişisel veri | Nerede / hangi bileşen | Ne kadar saklanıyor | Kim erişiyor | Uygulanan teknik önlem |
|---|---|---|---|---|---|
| **Giriş** (belge yükleme, bağlayıcı, veri aktarımı) | | | | | {{ör. otomatik maskeleme — HYG-ING-02}} |
| **Depolama** (korpus, vektör indeksi, yedek) | | | | | |
| **Prompt** (kullanıcı girdisi, ekler) | | | | | {{HYG-PRM-01}} |
| **Çıkarım** (model; dış sağlayıcı / kurum içi) | | | | | |
| **Yanıt** (çıktı, çıktıdaki kişisel veri) | | | | | |
| **Sonraki kullanım** (çıktının aktarıldığı sistemler, kayıtlar) | | | | | |
| **Kayıtlar** (prompt/yanıt kayıtları, denetim izi) | | | | | |

# 3. Yurt dışı aktarım noktaları

| Aşama | Alıcı (sağlayıcı / alt işleyen) | Ülke | Aktarılan veri | TPL-06 no |
|---|---|---|---|---|
| | | | | |

# 4. Hukuki değerlendirme (hukuk danışmanı doldurur)

| | |
|---|---|
| Hukuka uygunluk sebebi (KVKK md. 5/6) | |
| Aydınlatma yükümlülüğü karşılandı mı (KVKK md. 10)? | |
| Aktarım mekanizması (KVKK md. 9) | |
| Otomatik işleme ile aleyhe sonuç riski (KVKK md. 11(1)(g)) | |

# 5. Riskler ve önlemler

| # | Kişiler için risk | Olasılık / etki | Önlem | Sorumlu | Tarih | Durum |
|---|---|---|---|---|---|---|
| 1 | {{ör. kişisel verinin dış sağlayıcıda kalması}} | | | | | |
| 2 | {{ör. yetkisiz çalışanın model üzerinden müşteri verisine erişmesi}} | | | | | |
| 3 | {{ör. çıktıda yanlış kişiye ait veri}} | | | | | |
| 4 | {{ör. kayıtların gereğinden uzun saklanması}} | | | | | |

# 6. DPO görüşü ve karar

| | |
|---|---|
| KVKK irtibat kişisi / DPO görüşü | |
| Görüş tarihi / ad | |
| Sistem sahibi kararı | ☐ Devam ☐ Önlemlerle devam ☐ Durdur |
| Güncelleme | En geç 12 ayda bir; veri kategorisi ya da sağlayıcı değişikliğinde |
