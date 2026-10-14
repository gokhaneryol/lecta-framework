---
title: "{{Kurum}} — Yapay Zekâ İnsan Gözetimi Prosedürü"
id: TPL-13
g_items: [G-OVS-01]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-OVS-01, rubric 2 — sistem başına dört unsur (çıktı sınıfları, inceleyen rol, süre sınırı, bekleme durumu — Bölüm 3) ya da imzalı "inceleme gerekmez" kararı (Bölüm 4), ve **en az bir uçtan uca işletim kaydı** (Bölüm 5). Kâğıt üzerindeki prosedür 2 puan almaz. Rubric 3: süre içinde tamamlanma oranı (Bölüm 6).
> **Bağlantı:** EU AI Act Art. 14 (yüksek risk) ve Art. 26(2); GDPR Art. 22 / KVKK md. 11(1)(g) `[CHECK]`.

# 1. Amaç

AI çıktısının kişiler, müşteriler ya da kurum için önemli sonuç doğurmadan önce, gerektiği durumlarda yetkin bir insan tarafından incelenmesini sağlamak.

# 2. Genel kural

Aşağıdaki çıktılar **her sistemde** insan incelemesi olmadan etkili olmaz:
- bir kişi hakkında hak, hizmet, istihdam ya da finansal sonuç doğuran karar ya da öneri;
- kurum adına dışarıya gönderilen ve hukuki/sözleşmesel bağlayıcılığı olan metin;
- davranış kontrollerinin (çıktı filtresi) "şüpheli" olarak işaretlediği çıktılar.

# 3. Sistem başına gözetim tanımı

Her AI sistemi için bir tablo doldurulur.

**Sistem:** {{AI-SYS-nnn — ad}} · **Sahip:** {{…}}

| Unsur | Tanım |
|---|---|
| **1. İncelenecek çıktı sınıfları** | {{ör. kredi ön değerlendirme notu "ret" önerisi; müşteriye gidecek tazminat cevabı; filtre tarafından işaretlenen her çıktı}} |
| **2. İnceleyen rol** | {{rol}} — yetkinlik: TPL-12 Bölüm 5 eğitimi; inceleyenin çıktıyı reddetme/değiştirme yetkisi var |
| **3. Süre sınırı (SLA)** | {{ör. 1 iş günü}}; aşılırsa {{üst rol}}'e yükseltilir |
| **4. İnceleme beklerken çıktıya ne olur** | {{ör. müşteriye gönderilmez; işlem askıda kalır; kullanıcıya "incelemede" bilgisi verilir}} |
| İnceleme kaydı nerede tutulur | {{sistem / kuyruk / tablo}} — alanlar: çıktı no, inceleyen, karar (onay/değişiklik/ret), gerekçe, tarih-saat |
| İnceleyenin göreceği bilgi | AI çıktısı + dayandığı kaynaklar + sistemin bilinen sınırları |

# 4. "İnceleme gerekmez" kararı

Bir sistemin çıktıları Bölüm 2'deki türlerin hiçbirine girmiyorsa (ör. çalışanın kendi kullanımı için özet), sistem sahibi gerekçeli olarak bunu kaydeder.

| Sistem | Gerekçe | Sahip imza / tarih |
|---|---|---|
| | | |

# 5. Uçtan uca işletim kaydı (zorunlu)

Prosedür canlıya almadan önce **gerçek vaka ya da test** ile en az bir kez baştan sona işletilir: çıktı sınıflandırılır → kuyruğa düşer → inceleyen karar verir → çıktı bekleme durumundan çıkar → kayıt oluşur.

| Tarih | Sistem | Vaka/test açıklaması | Süre | Sonuç | Bulunan aksaklık |
|---|---|---|---|---|---|
| | | | | | |

# 6. Ölçüm

Her {{6}} ayda bir, sistem başına: incelenen çıktı sayısı · süre sınırı içinde tamamlanma oranı · ret/değişiklik oranı. Sonuçlar AI yönetişim sorumlusuna raporlanır.

# 7. Onay

Belge no / sürüm: {{…}} · Onaylayan: {{Ad, unvan, tarih}} · Gözden geçirme: en geç 12 ayda bir
