---
title: "{{Kurum}} — AI Risk Değerlendirmesi"
id: TPL-09
g_items: [G-RSK-01]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-RSK-01, rubric 2 — yazılı yöntem (Bölüm 1), dört AI'ye özgü risk grubu (Bölüm 3, ilk dört grup zorunlu), sahip onaylı muamele kararları (Bölüm 4–5), tanımlı yeniden değerlendirme tetikleyicileri (Bölüm 6).
> **Uyarlama:** Kurum ISO 27001 risk yöntemini kullanıyorsa Bölüm 1'deki ölçekler kurumunkilerle değiştirilir; dört risk grubu korunur.

# 1. Yöntem

**Olasılık (O)** 1 Çok düşük · 2 Düşük · 3 Orta · 4 Yüksek · 5 Çok yüksek
**Etki (E)** 1 Önemsiz · 2 Sınırlı · 3 Orta (tek müşteri/kişi, düzeltilebilir) · 4 Ciddi (çok kişi, yasal bildirim, itibar) · 5 Kritik (yaygın ihlal, faaliyet kesintisi, ağır yaptırım)
**Risk = O × E** · 1–6 Düşük · 8–12 Orta · 15–25 Yüksek
**Kabul kriteri:** Yüksek risk muamelesiz kabul edilemez; Orta risk sistem sahibinin, Yüksek riskin kalıntısı {{üst yönetimin}} onayıyla kabul edilir.

# 2. Sistem bilgisi

| | |
|---|---|
| Sistem / envanter no | AI-SYS-{{nnn}} |
| Sistem sahibi | |
| Amaç ve kullanıcılar | |
| Veri kategorileri / profil (dış servis, kurum içi, hibrit) | |
| Değerlendirme türü | ☐ İlk (canlıdan önce) ☐ Periyodik ☐ Tetikleyici: ___ |
| Değerlendirenler / tarih | |

# 3. Risk tablosu

| # | Risk grubu | Senaryo (bu sistemde) | Mevcut kontrol | O | E | Risk | Muamele |
|---|---|---|---|---|---|---|---|
| R1 | **Prompt ile veri çıkışı** — kişisel/gizli verinin modele ya da sağlayıcıya gitmesi | | | | | | |
| R2 | **Yanlış ya da zararlı çıktı** — hatalı bilgi, ayrımcı/uygunsuz içerik, hatalı çıktıya dayanılan işlem | | | | | | |
| R3 | **Model üzerinden yetkisiz erişim** — yetkisiz belgeye erişim, prompt injection, yetki aşımı | | | | | | |
| R4 | **Sağlayıcı bağımlılığı** — kesinti, koşul değişikliği, eğitimde kullanım, yetki alanı | | | | | | |
| R5 | {{Ek: model performansında zamanla bozulma}} | | | | | | |
| R6 | {{Ek: kişiler hakkında otomatik karar / şeffaflık}} | | | | | | |
| R7 | {{Ek: fikri mülkiyet / telif}} | | | | | | |

Muamele: **Azalt** (kontrol ekle) · **Kaçın** (kullanımı değiştir/durdur) · **Aktar** (sözleşme/sigorta) · **Kabul et** (gerekçeli).

# 4. Muamele planı

| Risk # | Aksiyon | Lecta framework maddesi (varsa) | Sorumlu | Hedef tarih | Kalıntı risk |
|---|---|---|---|---|---|
| | | {{ör. HYG-PRM-01}} | | | |

# 5. Onay

| | |
|---|---|
| Sistem sahibi kararı | ☐ Canlıya alınabilir ☐ Koşullu (aksiyonlar tamamlanınca) ☐ Alınamaz |
| Kalıntı risk kabulü (Orta/Yüksek) | {{Ad, unvan, tarih}} |
| AI yönetişim sorumlusu | {{Ad, tarih}} |

# 6. Yeniden değerlendirme tetikleyicileri

En geç **12 ayda bir** ve şu durumlarda: yeni model ya da sağlayıcı · yeni veri kategorisi (özellikle kişisel/özel nitelikli) · yeni kullanıcı grubu ya da dış kullanıcılar · amaç değişikliği · bu sistemle ilgili AI olayı (TPL-03).

| Tarih | Tetikleyici | Değişen riskler | Onay |
|---|---|---|---|
| | | | |
