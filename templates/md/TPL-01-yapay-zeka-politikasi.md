---
title: "{{Kurum}} — Yapay Zekâ Politikası"
id: TPL-01
g_items: [G-POL-01]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-POL-01, rubric 2 — üst yönetim onayı (Bölüm 10), hesap verecek rol (Bölüm 5), yeni AI sistemi onay yolu (Bölüm 6), G-POL-02'ye atıf (Bölüm 7), duyuru kaydı (Bölüm 10). Rubric 3 için Bölüm 9'daki gözden geçirme kaydı tutulmalı.
> **Doldurma:** `{{…}}` alanları kuruma göre doldurulur. Kurum ISO 27001 politika setine sahipse bu metin ayrı politika ya da bilgi güvenliği politikasının bir bölümü olarak kullanılabilir.
> **Sınır:** Bu şablon hukuki görüş değildir; sektör ve hukuk değerlendirmesi kurumun hukuk danışmanına aittir.

# 1. Amaç

Bu politika, {{Kurum}}'un yapay zekâ (AI) sistemlerini ve AI servislerini hangi amaçlarla, hangi sınırlar içinde ve kimin sorumluluğunda kullandığını belirler. Amaç, AI'nin sağladığı faydayı kişisel verilerin, gizli bilginin ve kurumun itibarının korunmasıyla birlikte elde etmektir.

# 2. Kapsam

- **Kişiler:** Tüm çalışanlar, stajyerler, danışmanlar ve kurum adına çalışan yükleniciler.
- **Sistemler:** Kurumun geliştirdiği, satın aldığı, abone olduğu ya da çalışanların iş amacıyla kullandığı tüm AI sistemleri ve servisleri. Buna dış sağlayıcıların üretken AI servisleri, kurum içinde çalışan modeller ve başka yazılımların içine gömülü AI özellikleri dahildir.
- **Veri:** AI sistemlerine girilen, onlar tarafından işlenen ya da üretilen her türlü kurum verisi.

# 3. Tanımlar

| Terim | Anlamı |
|---|---|
| AI sistemi | Girdiden tahmin, içerik, öneri ya da karar üreten makine tabanlı sistem |
| AI sistem sahibi | Bir AI sisteminin amacından, riskinden ve kurallara uygun kullanımından hesap veren, adı belli yönetici |
| Onaylı araç | Kabul edilebilir kullanım kurallarındaki (TPL-02) onaylı araç listesinde bulunan AI aracı |
| Dış AI servisi | Verinin kurumun yönettiği sınırların dışında işlendiği AI servisi |

# 4. İlkeler

1. **Amaçla sınırlılık:** AI yalnız envanterde (TPL-05) kayıtlı amaçlar için kullanılır.
2. **Veri koruma önce gelir:** Kişisel veri ve gizli bilgi, yalnız izin verilen araçlara ve izin verilen sınıflarda girilir (TPL-02).
3. **İnsan sorumluluğu:** AI çıktısı, sorumluluğu bir insandan almaz. İnsan gözetimi gereken çıktılar TPL-13'e göre incelenir.
4. **Şeffaflık:** Kişiler, bir AI sistemiyle etkileşimde olduklarında ya da hakkındaki bir kararda AI kullanıldığında, ilgili mevzuatın gerektirdiği ölçüde bilgilendirilir.
5. **Risk temelli yaklaşım:** Her AI sistemi canlıya alınmadan önce risk açısından değerlendirilir (TPL-09) ve sınıflandırılır (TPL-10).
6. **Sağlayıcı güvencesi:** Dış AI servisleri, kullanımdan önce değerlendirilir (TPL-06) ve sözleşmesel güvencelere bağlanır (TPL-08).

# 5. Roller ve sorumluluklar

| Rol | Sorumluluk | Atanan |
|---|---|---|
| Üst yönetim | Politikayı onaylar, kaynak sağlar, kabul edilemez riskleri reddeder | {{Genel Müdür / Yönetim Kurulu}} |
| AI yönetişim sorumlusu | Politikanın sahibi; envanteri, onay sürecini ve gözden geçirmeyi yürütür | {{Ad Soyad, unvan}} |
| AI sistem sahibi | Kendi sisteminin risk değerlendirmesi, sınıflandırması, kullanıcıları ve olayları | Envanterde sistem başına |
| KVKK irtibat kişisi / DPO | Kişisel veri işleyen sistemlerde etki değerlendirmesine görüş verir | {{Ad Soyad}} |
| Bilgi güvenliği sorumlusu | Teknik kontrolleri, sağlayıcı güvenliğini ve olay müdahalesini yönetir | {{Ad Soyad}} |
| Tüm çalışanlar | Kabul edilebilir kullanım kurallarına uyar, olayları bildirir, eğitimi tamamlar | — |

Ayrıntılı RACI: TPL-12.

# 6. Yeni AI sistemi ya da kullanım senaryosu için onay yolu

Yeni bir AI sistemi, yeni bir dış AI servisi ya da mevcut sistemin yeni bir amaçla kullanımı aşağıdaki adımlar tamamlanmadan canlıya alınamaz:

| # | Adım | Sorumlu | Kayıt |
|---|---|---|---|
| 1 | Talep ve envanter kaydı | Talep eden birim | TPL-05 |
| 2 | Sağlayıcı değerlendirmesi (dış servis ise) | Bilgi güvenliği | TPL-06, TPL-07, TPL-08 |
| 3 | Risk değerlendirmesi ve sınıflandırma | AI sistem sahibi | TPL-09, TPL-10 |
| 4 | Kişisel veri işleniyorsa etki değerlendirmesi ve DPO görüşü | AI sistem sahibi + DPO | TPL-11 |
| 5 | İnsan gözetimi tanımı | AI sistem sahibi | TPL-13 |
| 6 | Onay | AI yönetişim sorumlusu ({{ve risk sınıfı yüksekse üst yönetim}}) | Onay kaydı |

# 7. Kullanım kuralları

Çalışanların AI araçlarını kullanımına ilişkin kurallar ve onaylı araç listesi **{{TPL-02 belge numarası}} Yapay Zekâ Araçları Kabul Edilebilir Kullanım Kuralları**'nda yer alır ve bu politikanın parçasıdır.

# 8. Olaylar ve ihlaller

AI ile ilgili olaylar (prompt ya da çıktı yoluyla veri sızıntısı, zararlı veya yanlış çıktı, model üzerinden yetkisiz erişim, sağlayıcı tarafı olay) **{{TPL-03 belge numarası}} AI Olay Prosedürü**'ne göre bildirilir. Politikaya aykırılık, {{kurumun disiplin yönetmeliği}} kapsamında değerlendirilir.

# 9. Gözden geçirme

Bu politika en geç **12 ayda bir** ve aşağıdaki durumlarda gözden geçirilir: yürürlüğe giren yeni mevzuat, önemli bir AI olayı, kurumun AI kullanımında önemli değişiklik. Her gözden geçirme, değişiklik olmasa da tarihli olarak kaydedilir.

| Tarih | Gözden geçiren | Sonuç (değişiklik / değişiklik yok) |
|---|---|---|
| {{gg.aa.yyyy}} | {{Ad}} | {{…}} |

# 10. Onay ve duyuru

| | |
|---|---|
| Belge no / sürüm | {{…}} / {{1.0}} |
| Onaylayan | {{Ad Soyad, unvan}} — {{gg.aa.yyyy}} |
| Yürürlük | {{gg.aa.yyyy}} |
| Duyuru | {{intranet / e-posta}} — {{gg.aa.yyyy}}; okundu kaydı: {{sistem / liste}} |

# İlgili belgeler

TPL-02 Kabul edilebilir kullanım · TPL-03 Olay prosedürü · TPL-05 Envanter · TPL-06/07/08 Sağlayıcı · TPL-09/10/11 Risk · TPL-12 Roller · TPL-13 İnsan gözetimi
