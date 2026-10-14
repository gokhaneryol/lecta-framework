---
title: "{{Kurum}} — Yapay Zekâ Rolleri ve Sorumluluklar Matrisi"
id: TPL-12
g_items: [G-ROL-01, G-LIT-02]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-ROL-01, rubric 2 — resmî atanmış yönetişim rolü (Bölüm 1), danışma noktaları (Bölüm 3), danışma kaydı (Bölüm 4); sistem sahipleri envanterde (TPL-05). G-LIT-02 için rol–eğitim eşlemesi Bölüm 5'te.
> **Uyarlama:** Küçük kurumlarda roller birleşebilir (ör. AI yönetişim sorumlusu = bilgi güvenliği sorumlusu); birleşme açıkça yazılır.

# 1. Roller ve atamalar

| Rol | Görev özeti | Atanan | Atama belgesi / tarih |
|---|---|---|---|
| AI yönetişim sorumlusu | Politika, envanter, onay süreci, gözden geçirme | | |
| AI sistem sahibi | Sistem başına risk, sınıflandırma, kullanım, olay — envanterde | TPL-05 | |
| KVKK irtibat kişisi / DPO | Kişisel veri etki değerlendirmesi görüşü, ihlal bildirimi | | |
| Bilgi güvenliği sorumlusu | Teknik kontroller, sağlayıcı güvenliği, olay koordinasyonu | | |
| Hukuk | Sınıflandırma, aktarım, sözleşme görüşleri | | |
| İnsan gözetimi inceleyicileri | Sistem başına, TPL-13'e göre | TPL-13 | |
| Satın alma | AI içeren ürün/servis alımlarını onay yoluna yönlendirmek | | |

# 2. RACI

S = Sorumlu (yapar) · H = Hesap veren (onaylar) · D = Danışılan · B = Bilgilendirilen

| Faaliyet | Üst yön. | AI yönetişim | Sistem sahibi | DPO | Bilgi güv. | Hukuk |
|---|---|---|---|---|---|---|
| AI politikasının onayı | H | S | B | D | D | D |
| Envanter bakımı | B | H/S | S | B | D | — |
| Yeni sistem onayı | (Yüksek risk: H) | H | S | D | D | D |
| Sağlayıcı değerlendirmesi | — | B | D | D | H/S | D |
| Risk değerlendirmesi ve sınıflandırma | B | D | H/S | D | D | D |
| Kişisel veri etki değerlendirmesi | — | B | H/S | D | D | D |
| AI olayına müdahale | B | B | D | D (AI-1: H) | H/S | D |
| Yasal bildirim kararı | B | B | B | H | D | S |
| Eğitim programı | B | H | B | D | S | — |

# 3. Danışma noktaları (zorunlu)

| Tetikleyici | Danışılacak | Kayıt |
|---|---|---|
| Yeni AI sistemi ya da yeni dış AI servisi | DPO + Bilgi güvenliği | Onay kaydı |
| Sisteme yeni kişisel veri kategorisi eklenmesi | DPO | TPL-11 güncellemesi |
| Yeni sağlayıcı ya da sağlayıcı değişikliği | Bilgi güvenliği (+ hukuk) | TPL-06 |
| Kişiler hakkında karar destekleyen kullanım | DPO + hukuk | TPL-10, TPL-13 |
| AI-1 olayı (veri sızıntısı) | DPO | TPL-04 |

# 4. Danışma kaydı

| Tarih | Tetikleyici | Danışılan | Görüş özeti | Belge no |
|---|---|---|---|---|
| | | | | |

Son 12 ayda tetikleyici olmadıysa: "{{tarih}} itibarıyla tetikleyici olay yok" kaydı düşülür.

# 5. Role özgü eğitim

| Rol | Eğitim modülü | Süre | Tazeleme |
|---|---|---|---|
| Tüm kullanıcılar | AI okuryazarlığı (kabul edilebilir kullanım, veri riski, çıktının sınırları) | {{1 saat}} | 12 ay |
| AI sistem sahipleri | Risk değerlendirme, sınıflandırma, envanter | | 12 ay |
| Geliştirici / işletmeci | Güvenli AI geliştirme: prompt injection, veri maskeleme, kayıt, fail-closed | | 12 ay |
| İnsan gözetimi inceleyicileri | Sistem çıktı sınıfları, karar kriterleri, SLA | | 12 ay |
| DPO / hukuk | AI'ye özgü veri koruma ve aktarım | | 12 ay |

# 6. Onay ve gözden geçirme

Onaylayan: {{Ad, unvan, tarih}} · Gözden geçirme: en geç 12 ayda bir ve her rol sahibinin değişiminde.
