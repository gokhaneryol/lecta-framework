---
title: "{{Kurum}} — Yapay Zekâ Olay Prosedürü"
id: TPL-03
g_items: [G-INC-01]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-INC-01, rubric 2 — dört AI olay türü (Bölüm 3), adı belli rollerle raporlama zinciri (Bölüm 4–5), uygulanan bildirim süreleri (Bölüm 6), genel olay süreciyle bağlantı (Bölüm 2), son 12 ayda tatbikat ya da olay kaydı (Bölüm 8). Rubric 3: Bölüm 8'deki ders/aksiyon takibi.
> **Yasal dayanaklar (doğrulandı 14.10.2026):** KVKK md. 12(5) + Kurul kararı 24.01.2019/2019-10 → Kurula 72 saat; gecikmede gerekçe; veri işleyen veri sorumlusuna gecikmeksizin. 7545 sayılı Kanun md. 7(1)(b) → zafiyet ve siber olaylar Siber Güvenlik Başkanlığı'na **gecikmeksizin**; saatle tanımlı süre yok, usul ikincil düzenlemeye bırakılmış; aykırılık md. 16(10) → 1–10 milyon TL. Kanunun kapsamı geniş (bilişim sistemiyle hizmet sunan, veri toplayan veya işleyen herkes); kritik altyapı sektörlerinde ek yükümlülükler var.
> **Kullanmadan önce:** 7545 ikincil düzenlemelerinin yayımlanıp yayımlanmadığı ve kurumun sektör kuralları kontrol edilir. Bu şablon hukuki görüş değildir.
> **Sınır:** Prosedür kurumun mevcut bilgi güvenliği olay sürecine **ek**tir, onun yerine geçmez.

# 1. Amaç

AI sistemlerine ve servislerine özgü olayların hızlı tanınmasını, doğru kişilere ulaşmasını ve yasal bildirim sürelerinin kaçırılmamasını sağlamak.

# 2. Genel olay süreciyle ilişki

Bu prosedür {{Kurum}}'un **{{Bilgi Güvenliği Olay Yönetimi Prosedürü, belge no}}**'nun AI'ye özgü ekidir. Sınıflandırma, müdahale, kanıt saklama ve kapanış adımları o prosedüre göre yürür; bu belge AI'ye özgü olay türlerini, ek rolleri ve bildirim noktalarını tanımlar.

# 3. AI olay türleri

| Kod | Olay türü | Örnekler |
|---|---|---|
| **AI-1** | Prompt ya da çıktı yoluyla veri sızıntısı | Çalışanın müşteri verisini onaysız bir AI servisine yapıştırması; modelin yanıtında başka bir kişinin verisini göstermesi |
| **AI-2** | Etkisi olan zararlı ya da yanlış çıktı | Müşteriye yanlış bilgi verilmesi; ayrımcı ya da hakaret içeren çıktı; hatalı çıktıya dayanılarak işlem yapılması |
| **AI-3** | Model üzerinden yetkisiz erişim | Kullanıcının yetkisi olmayan belgeye AI asistanı üzerinden ulaşması; prompt injection ile kural dışı davranış |
| **AI-4** | Sağlayıcı tarafı olay | Dış AI sağlayıcısının ihlal bildirimi; sağlayıcının koşul değişikliği ile verinin eğitimde kullanılmaya başlanması; servis kesintisi |

Şüphe durumunda olay **bildirilir**; türü değerlendirme sırasında belirlenir.

# 4. Kim, kime bildirir

1. **Fark eden kişi** → {{bildirim kanalı}} üzerinden **AI Olay Bildirim Formu** ({{TPL-04 no}}) ile, fark ettikten sonra **en geç {{2}} saat** içinde.
2. **Olay koordinatörü** ({{Bilgi güvenliği sorumlusu}}) → ilk değerlendirme ve önem derecesi: **{{4}} saat** içinde.
3. Önem derecesi Yüksek/Kritik ya da AI-1 ise → **AI sistem sahibi**, **KVKK irtibat kişisi/DPO**, **AI yönetişim sorumlusu** aynı gün bilgilendirilir.
4. Kritik olaylarda → **{{Genel Müdür}}** bilgilendirilir.

# 5. Roller

| Rol | Kişi | Yedek |
|---|---|---|
| Olay koordinatörü | {{Ad Soyad}} | {{Ad Soyad}} |
| AI yönetişim sorumlusu | {{Ad Soyad}} | {{Ad Soyad}} |
| KVKK irtibat kişisi / DPO | {{Ad Soyad}} | {{Ad Soyad}} |
| Hukuk | {{Ad Soyad / dış danışman}} | — |
| İletişim | {{Ad Soyad}} | — |

# 6. Yasal ve sözleşmesel bildirimler

| Yükümlülük | Ne zaman | Muhatap | Karar veren |
|---|---|---|---|
| KVKK md. 12(5) ve Kurul kararı 2019/10 — kişisel veri ihlali | Öğrenildikten sonra **72 saat** içinde Kurula (gecikirse gerekçesiyle); ilgili kişilere makul en kısa sürede, ulaşılamıyorsa web sitesinden duyuru | KVKK Kurumu (ihlal bildirim formu) | DPO + hukuk |
| GDPR Art. 33 — AB'deki kişilerin verisi varsa | 72 saat | Yetkili denetim makamı | DPO + hukuk |
| 7545 sayılı Siber Güvenlik Kanunu md. 7(1)(b) — zafiyet ve siber olaylar | **Gecikmeksizin** (usul ve ayrıntılar ikincil düzenlemeye göre: {{yayımlandıysa atıf}}) | Siber Güvenlik Başkanlığı {{ve varsa sektör SOME'si}} | Bilgi güvenliği + hukuk |
| Sektör düzenlemesi | {{BDDK / EPDK / kamu}} | {{…}} | {{…}} |
| Müşteri / sözleşme gereği | {{Sözleşmedeki süre}} | {{Müşteri}} | Sözleşme sahibi birim |
| AI sağlayıcısına bildirim (AI-3, AI-4) | Değerlendirme sonrası | Sağlayıcı destek / güvenlik kanalı | Bilgi güvenliği |

Sürenin başlangıcı ve bildirim kararı olay kaydına yazılır. "Bildirim gerekmiyor" kararı da gerekçesiyle kaydedilir.

# 7. İlk müdahale — AI'ye özgü adımlar

- **AI-1:** Girilen verinin ne olduğu ve hangi servise gittiği tespit edilir; sağlayıcıdan silme talep edilir (sözleşme varsa); ilgili hesap/erişim gözden geçirilir.
- **AI-2:** Çıktının kime ulaştığı tespit edilir; düzeltme yapılır; benzer çıktıları önlemek için sistem kapatılır ya da insan gözetimine alınır.
- **AI-3:** Erişim yolu kapatılır; ilgili kayıtlar (prompt/yanıt kayıtları) korunur; yetki yapılandırması incelenir.
- **AI-4:** Sağlayıcıdan yazılı bilgi istenir; servis kullanımı askıya alınabilir; G-SUP değerlendirmesi yenilenir.

Tüm türlerde prompt, yanıt ve erişim kayıtları **silinmez**; kanıt olarak saklanır.

# 8. Kapanış, dersler ve tatbikat

- Her olay için kök neden, alınan aksiyonlar, sorumlusu ve tarihi olay kaydına yazılır; aksiyonlar kapanana kadar izlenir.
- Son 12 ayda AI olayı yaşanmadıysa en az **bir masa başı tatbikat** yapılır (örnek senaryo: çalışanın müşteri listesini ücretsiz bir AI servisine yüklemesi).
- Prosedür en geç 12 ayda bir gözden geçirilir.

| Tarih | Olay / tatbikat | Ders | Aksiyon — sorumlu — tarih | Durum |
|---|---|---|---|---|
| {{…}} | | | | |

# 9. Onay

Belge no / sürüm: {{…}} · Onaylayan: {{Ad Soyad, unvan}} — {{tarih}}
