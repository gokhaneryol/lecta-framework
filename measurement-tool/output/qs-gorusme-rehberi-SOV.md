# Quick Scan Görüşme Rehberi — Sovereign profili

*Lecta Sovereign AI Control Framework · v1.0-draft · kaynaktan üretildi (`tools/qs.py`) — elle düzenlemeyin*

## Görüşmeye başlarken (okunacak metin)

> Bu görüşme bir **Hızlı Tarama**dır: sorularımız beyanınıza dayanır, kanıt incelemesi yapılmaz. Sonuç bir **gösterge hazırlık seviyesidir**; denetim görüşü ya da belge değildir. Bilmediğiniz soruya "bilmiyorum" demeniz en doğru cevaptır ve öyle kaydedilir.

**Puanlama notu:** Kontrol listeli maddelerde her kontrole beyana göre E / H / B yazılır, puan betikle hesaplanır (`basis: declared`). Kontrol listesi olmayan maddede 0–3 verilir. Katılımcı cevabı bilmiyorsa **NE**; madde kurumda yoksa ve uygulanabilirlik ölçütü karşılanmıyorsa **NA** (gerekçe yazılır). Kanıt istenmez; katılımcı kendiliğinden gösterirse `evidence_ref` alanına not edilir.

**Süre:** 9 kurum + 8 sistem maddesi (sistem başına) · ~4 dk/madde · 1 sistemle ~83 dk.

## Bölüm A — Kurum (G bloğu, kurum başına bir kez)

### G-POL-02 · Yapay zekâ araçlarının kabul edilebilir kullanımı  `L0`

**Soru:** Çalışanların hangi AI araçlarını kullanabileceği ve hangi verileri girebileceğine dair yazılı kural var mı?

**Derinleştirme:** Çalışanlar hangi yapay zekâ araçlarını kullanabileceklerini ve bunlara hangi verileri girebileceklerini biliyor mu?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Çalışanların yapay zekâ araçlarını kullanımına dair yazılı kural var (ayrı belge ya da bir politikanın içinde). | E / H / B |
| c2 | temel | Kurallar kurumun veri sınıflarına atıf yapıyor. | E / H / B |
| c3 | temel | Onaylı araç listesi var ve listedeki her araç için izin verilen veri sınıfları yazılı. | E / H / B |
| c4 | temel | Onaylı araç listesinin son güncelleme tarihi son 12 ay içinde. **[≤ 12 ay]** | E / H / B |
| s1 | sürdürme | Kurallara uyum G-INV-02 kullanım verisiyle karşılaştırılmış ve bu karşılaştırmanın tarihli kaydı 6 ay içinde. **[≤ 6 ay]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **veri sınıfı**: Kurumun yazılı veri sınıflandırmasındaki bir kategori (ör. açık, iç, gizli, kişisel, özel nitelikli kişisel). Sınıflandırma tarihli bir belge olmalıdır; yazılı olmayan ya da sözlü bir ayrım sayılmaz. · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **onaylı araç listesi**: Çalışanların kullanabileceği her yapay zekâ aracını adıyla (ürün ve gerekiyorsa hesap türü, ör. kurumsal/bireysel) sayan, sahibi ve son güncelleme tarihi olan yazılı liste. Yalnız kategori sayan liste ("onaylı sohbet botları") sayılmaz.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c5) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c5) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Kabul edilebilir kullanım kuralları (ayrı belge ya da AI/kabul edilebilir kullanım politikası içinde); `DOC` Araç başına izin verilen veri sınıflarını ve son güncelleme tarihini gösteren onaylı AI araç listesi; `INT` Farklı birimlerden iki çalışanın hangi aracı kullanabileceği ve hangi veri sınıfını girebileceğine dair cevapları (kontrol c5)

### G-INV-01 · Yapay zekâ sistem envanteri  `L1`

**Soru:** Kullanılan AI sistemlerinin ve kullanım senaryolarının, her birinin sahibiyle birlikte bir listesi var mı?

**Derinleştirme:** Hangi yapay zekâ sistemleri ve kullanım senaryoları canlıda ya da pilotta, nerede kayıtlı?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | AI sistemleri ve kullanım senaryoları envanteri var. | E / H / B |
| c2 | temel | Envanter kayıtlarından tüm zorunlu alanları dolu olanların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Satın alma kayıtlarında, onaylı araç listesinde (G-POL-02) ya da görüşmelerde görülen sistemlerden envanterde bulunanların oranı. **[%100 (hepsi)]** | E / H / B |
| c4 | temel | Envanterin son güncelleme tarihi son 6 ay içinde. **[≤ 6 ay]** | E / H / B |
| s1 | sürdürme | Envanter G-INV-02 trafik verisiyle karşılaştırılmış, eklenen ve çıkarılan kayıtlar yazılmış; tarihli kaydı 6 ay içinde. **[≤ 6 ay]** | E / H / B |

*Terimler:* **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **envanter zorunlu alanları**: Amaç, sahip, kullanıcı grupları, veri kategorileri, sağlayıcı, profil (CE/SOV) ve durum.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c4) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c4) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Amaç, sahip, kullanıcılar, veri kategorileri, sağlayıcı, profil ve durum alanlarını içeren envanter; `DOC` Karşılaştırma için onaylı araç listesi (G-POL-02) ve satın alma ya da proje kayıtları

### G-LIT-01 · Tüm kullanıcılar için yapay zekâ okuryazarlığı  `L1`

**Soru:** AI araçlarını kullanan çalışanlar güvenli kullanım eğitimi aldı mı?

**Derinleştirme:** AI kullanıcıları hangi eğitimi alıyor ve ne kadarı tamamladı?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Yapay zekâ okuryazarlık programı var. | E / H / B |
| c2 | temel | Program içeriği üç konuyu kapsıyor. | E / H / B |
| c3 | temel | Tamamlama kişi başına tarihli kayıt altında. | E / H / B |
| c4 | temel | AI kullanıcılarından kayıtlı tamamlaması olanların oranı. **[en az %80]** | E / H / B |
| s1 | sürdürme | İçeriğin son güncelleme tarihi 12 ay içinde. **[≤ 12 ay]** | E / H / B |
| s2 | sürdürme | Anlama ölçülüyor (sınav ya da uygulama) ve sonuçlar kayıtlı. | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **AI kullanıcısı**: AI envanterindeki (G-INV-01) en az bir sisteme erişimi olan kişi. Eğitim oranlarının paydası AI kullanıcısı sayısıdır. · **üç okuryazarlık konusu**: Kabul edilebilir kullanım (G-POL-02); veri riskleri (neyin girilemeyeceği ve nedeni); AI çıktısının sınırları (hatalar, doğrulama yükümlülüğü).

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c5) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c5) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Üç konuyu kapsayan program içeriği; `LOG` Kişi başına tarihli tamamlama kayıtları; payda için G-INV-01'den AI kullanıcı sayısı

### G-POL-01 · Yapay zekâ politikası  `L1`

**Soru:** Onaylanmış bir yapay zekâ politikanız var mı, çalışanlara duyuruldu mu?

**Derinleştirme:** Kurumun onaylanmış bir yapay zekâ politikası var mı ve çalışanlara nasıl duyuruldu?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Yazılı bir yapay zekâ politikası var ya da AI onaylı başka bir politikada ele alınıyor. | E / H / B |
| c2 | temel | Politika üst yönetim ya da yetkilendirdiği bir kurul tarafından onaylanmış, onay kaydı var. | E / H / B |
| c3 | temel | Politika hesap verecek rolü adlandırıyor. | E / H / B |
| c4 | temel | Politika yeni bir AI sisteminin onay yolunu tanımlıyor. | E / H / B |
| c6 | temel | Kapsamdaki tüm çalışanlara duyuru kaydı var. | E / H / B |
| s1 | sürdürme | Politika gözden geçirilmiş; tarihli kaydı (değişiklikler ya da "değişiklik yok") 12 ay içinde. **[≤ 12 ay]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **duyuru kaydı**: Belgenin kapsamdaki çalışanlara ulaştığını gösteren tarihli kayıt: intranet yayını, onları kapsayan dağıtım listesine e-posta ya da okundu listesi. · **onay kaydı**: Onaylayanı, tarihi ve onaylanan sürümü gösteren kayıt (kurul kararı, imzalı kapak sayfası ya da belge yönetim sistemi iş akışı girdisi). · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c6) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c6) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Onay kaydıyla (onaylayan, tarih, sürüm) yapay zekâ politikası; `DOC` Duyuru kaydı (intranet yayını, e-posta, okundu listesi)

### G-ROL-01 · Roller ve hesap verebilirlik  `L1`

**Soru:** Her AI sisteminin adı belli bir sahibi ve genel olarak AI yönetişiminden sorumlu biri var mı?

**Derinleştirme:** Her AI sisteminden kim sorumlu? KVKK irtibat kişisi/DPO ve güvenlik birimi hangi noktalarda devreye girmek zorunda?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | En az bir AI sisteminin adı belli sahibi var ya da bir AI yönetişim rolü atanmış. | E / H / B |
| c2 | temel | Envanterdeki (G-INV-01) sistemlerden adı belli sahibi olanların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | AI yönetişim rolü resmî olarak atanmış (atama yazısı ya da görev tanımı). | E / H / B |
| c4 | temel | DPO ve güvenlik için danışma noktaları tanımlı. | E / H / B |
| s1 | sürdürme | Sahipler ve rol atamaları, personel değişikliği sonrası güncellemeler dahil teyit edilmiş; tarihli kaydı 12 ay içinde. **[≤ 12 ay]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **danışma noktaları**: DPO ve güvenliğe danışılması gereken, yazılı olaylar; en az: yeni AI sistemi, yeni kişisel veri kategorisi, yeni sağlayıcı. · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **adı belli sahip**: Belirli bir kişi ya da aynı anda tek kişinin tuttuğu bir rol; adıyla ya da rol unvanıyla kayıtlı. Birim adı ya da "BT" sayılmaz.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c5) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c5) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` G-INV-01'de kişi ya da rol adıyla doldurulmuş sahip alanı; `DOC` AI yönetişim rolü için atama yazısı ya da görev tanımı; `DOC` DPO ve güvenlik için tanımlı danışma noktaları (ör. yeni sistem, yeni veri kategorisi, yeni sağlayıcı)

### G-INC-01 · Yapay zekâ olay prosedürü  `L2`

**Soru:** Olay prosedürünüz prompt üzerinden veri sızıntısı gibi AI'ye özgü olayları kapsıyor mu?

**Derinleştirme:** Bir prompt üzerinden kişisel veri sızsa ya da bir AI sistemi zararlı bir çıktı üretse kime, kim tarafından, ne kadar sürede bildirilir?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | AI olayları bir olay prosedüründe ele alınıyor (ayrı ya da genel prosedürün içinde). | E / H / B |
| c2 | temel | Prosedür dört AI olay türünün hepsini adlandırıyor. | E / H / B |
| c3 | temel | Raporlama zinciri adı belli rollerle tanımlı. | E / H / B |
| c4 | temel | Uygulanan bildirim sürelerinin tablosu var. | E / H / B |
| c6 | temel | Son tatbikatın ya da ele alınmış AI olayı kaydının tarihi son 12 ay içinde. **[≤ 12 ay]** | E / H / B |
| s1 | sürdürme | Her tatbikat ya da olaydan çıkan dersler kayıtlı ve aksiyonlar kapanışa kadar izleniyor. | E / H / B |
| s2 | sürdürme | Prosedür gözden geçirilmiş; tarihli kaydı 12 ay içinde. **[≤ 12 ay]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **dört AI olay türü**: Prompt ya da çıktı yoluyla veri sızıntısı; etkisi olan zararlı ya da yanlış çıktı; model üzerinden yetkisiz erişim; sağlayıcı tarafı olay. · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **uygulanan bildirim süreleri**: Kuruma uygulanan süreler, her biri hukuki dayanağı ve muhatabıyla; en az KVKK ihlal bildirimi (72 saat) ve uygulanıyorsa 7545 sayılı Kanun ve sektör kuralları.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c6) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c6) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` En az şu AI olay türlerini adlandıran prosedür — prompt ya da çıktı yoluyla veri sızıntısı, etkisi olan zararlı ya da yanlış çıktı, model üzerinden yetkisiz erişim, sağlayıcı tarafı olay; `DOC` Bildirim süreleri tablosu (ör. KVKK ihlal bildirimi, sektör ve siber güvenlik yükümlülükleri); `TST` Bir tatbikatın ya da ele alınmış bir AI olayının kaydı

### G-INV-02 · AI servis kullanımının görünürlüğü  `L2`

**Soru:** Çalışanların hangi dış AI servislerini kullandığını ağ kayıtlarından görebiliyor musunuz?

**Derinleştirme:** Geçen ay ağınızdan hangi dış AI servislerine, hangi birimlerden erişildiğini gösterebilir misiniz?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Dış AI servislerine giden trafik DNS, proxy ya da firewall kayıtlarında tanımlanabiliyor. | E / H / B |
| c2 | temel | Bu kayıtların saklama süresi (gün). **[≥ 90]** | E / H / B |
| c3 | temel | Trafik bir birime ya da kullanıcı grubuna atfedilebiliyor. | E / H / B |
| c4 | temel | AI servis alan adı listesinin son güncelleme tarihi son 6 ay içinde. **[≤ 6 ay]** | E / H / B |
| c5 | temel | Talep edildiğinde birim bazında, en az 30 günü kapsayan rapor üretilebiliyor. | E / H / B |
| s1 | sürdürme | Raporlar gözden geçirilmiş; tarihli kaydı 3 ay içinde. **[≤ 3 ay]** | E / H / B |
| s2 | sürdürme | Onaylı listede (G-POL-02) olmayan bir servise giden trafik kayıtlı bir takip başlatıyor. | E / H / B |

*Terimler:* **AI servis alan adı listesi**: Kayıtlarda AI servis trafiğini tanımak için kullanılan alan adı ve uç nokta listesi, tarihli. Üretici kategori beslemesi, güncelleme tarihi gösterilebiliyorsa sayılır. · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c5) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c5) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `CFG` DNS, proxy ya da firewall kayıt yapılandırması ve saklama süresi; `DOC` Tanımlama için kullanılan, güncelleme tarihli AI servis alan adı/uç nokta listesi; `LOG` En az 30 günlük dönem için birim bazında AI servis trafiği raporu ya da sorgu sonucu

### G-RSK-01 · Yapay zekâ risk değerlendirmesi  `L2`

**Soru:** Bir AI sistemi canlıya alınmadan önce yazılı risk değerlendirmesi yapılıyor mu?

**Derinleştirme:** Bir AI sisteminin riskleri canlıya alınmadan önce nasıl değerlendiriliyor ve bu değerlendirme ne zaman tekrarlanıyor?

**Uygulanabilirlik:** Her zaman uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | En az bir AI sistemi için yazılı risk değerlendirmesi var. | E / H / B |
| c2 | temel | Kriterleri, ölçekleri ve kabul kuralını içeren yazılı bir risk değerlendirme yöntemi var. | E / H / B |
| c3 | temel | Canlıdaki AI sistemlerinden bu yöntemle yapılmış tarihli yazılı risk değerlendirmesi olanların oranı. **[%100 (hepsi)]** | E / H / B |
| c4 | temel | Değerlendirmelerden dört AI'ye özgü risk grubunun hepsini ele alanların oranı. **[%100 (hepsi)]** | E / H / B |
| c6 | temel | Yeniden değerlendirme tetikleyicileri tanımlı. | E / H / B |
| s1 | sürdürme | Değerlendirmelerden 12 ay içinde ve her tetikleyici olaydan sonra (hangisi önce gelirse) tekrarlanmış olanların oranı. **[%100 (hepsi)]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **AI'ye özgü risk grupları**: Dört grup: prompt ya da çıktı yoluyla veri sızıntısı; yanlış ya da zararlı çıktı; model üzerinden yetkisiz erişim; sağlayıcı bağımlılığı. · **yeniden değerlendirme tetikleyicileri**: Yeni değerlendirme gerektiren yazılı olaylar; en az: yeni model ya da sağlayıcı, yeni veri kategorisi, yeni kullanıcı grubu, olay.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c6) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c6) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` AI'ye özgü riskleri kapsayan risk değerlendirme yöntemi (kriterler, ölçekler, kabul); `DOC` Envanterdeki her sistem için tarihli, muamele kararlarını ve sahip onayını içeren risk değerlendirmesi; `DOC` Tanımlı yeniden değerlendirme tetikleyicileri (yeni model ya da sağlayıcı, yeni veri kategorisi, yeni kullanıcı grubu, olay)

### G-SUP-01 · Kullanım öncesi AI sağlayıcı değerlendirmesi  `L2`

**Soru:** Dış bir AI servisini kullanmadan önce verinin nerede tutulduğunu ve sağlayıcının onu eğitimde kullanıp kullanmadığını kontrol ediyor musunuz?

**Derinleştirme:** Dış bir AI servisini kullanmadan önce verinin nereye gittiği ve sağlayıcının onu nasıl kullandığı konusunda neyi kontrol ediyorsunuz?

**Uygulanabilirlik:** Kurum verisiyle hiçbir dış AI modeli ya da servisi kullanılmıyorsa uygulanmaz (G-INV-01 ve G-INV-02'ye göre).

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Kurum verisiyle kullanılan en az bir dış AI sağlayıcısı için yazılı değerlendirme var. | E / H / B |
| c2 | temel | Kurum verisiyle kullanılan dış AI sağlayıcılarından yazılı değerlendirmesi olanların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Değerlendirmelerden beş konunun hepsini kapsayanların oranı. **[%100 (hepsi)]** | E / H / B |
| c4 | temel | Değerlendirmelerden kurum verisiyle ilk kullanımdan önce tarihli olanların oranı. **[%100 (hepsi)]** | E / H / B |
| s1 | sürdürme | Değerlendirmelerden 12 ay içinde ve sağlayıcı koşullarında ya da alt işleyenlerde bildirilen her değişiklikten sonra tekrarlanmış olanların oranı. **[%100 (hepsi)]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **beş sağlayıcı konusu**: Verinin tutulduğu yer; saklama süresi; müşteri verisinin eğitimde kullanımı; alt işleyenler; yurt dışı aktarım mekanizması.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c5) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c5) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Sağlayıcı başına beş konuyu kapsayan, ilk kullanımdan önce tarihli değerlendirme kaydı; `DOC` Dayanılan sağlayıcı belgeleri (koşullar, veri işleme eki, alt işleyen listesi, veri yerleşimi beyanı)

## Bölüm B — Sistem (her sistem için ayrı; en çok 2 sistem)

### CON-ING-01 · Yalnız onaylı veri kaynakları  `L0`

**Soru:** AI sistemlerinize hangi sistem ya da kaynakların veri besleyebileceği tanımlı mı, diğerleri engelleniyor mu?

**Derinleştirme:** Bu AI sistemine hangi kaynaklar veri besleyebilir ve başka bir kaynaktan gelen veriye ne oluyor?

**Uygulanabilirlik:** HYG-ING-01 ile aynı (kurumun işlettiği en az bir veri giriş yolu).

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Sistem için onaylı veri kaynakları kaydı var. | E / H / B |
| c2 | temel | Sistemi fiilen besleyen kaynaklardan kayıtta bulunanların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Yalnız kayıtlı kaynaklardan veri kabul edecek biçimde yapılandırılmış giriş yollarının oranı. **[%100 (hepsi)]** | E / H / B |
| s1 | sürdürme | Kayıt çalışan yapılandırmayla karşılaştırılmış; tarihli kaydı 6 ay içinde. **[≤ 6 ay]** | E / H / B |
| s2 | sürdürme | Kayda kaynak eklemek kayıtlı bir onay gerektiriyor. | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c4

*Terimler:* **onaylı kaynak kaydı**: AI sistemini beslemesine izin verilen her kaynak için kaynağı, sahibini, veri kategorilerini, kullandığı giriş yolunu ve onay tarihini sayan yazılı kayıt. · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **veri giriş yolu**: İçeriğin bir yapay zekâ sistemine saklanmak, indekslenmek, bağlam olarak ya da eğitimde kullanılmak üzere girdiği her yol: dosya yükleme, başka sisteme bağlayıcı, API, zamanlanmış aktarım, e-posta ya da sohbet kanalı. Her bağlayıcı ve her API ayrı yol sayılır. · **giriş yolu envanteri**: Sistemin her veri giriş yolunu adıyla gösteren, tarihli yazılı liste (ya da mimari/veri akış şeması). Yollarla ilgili oran kontrollerinin paydasıdır.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c4) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c4) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Onaylı kaynak kaydı (kaynak, sahip, veri kategorileri, giriş yolu, onay tarihi); `CFG` Her giriş yolunda kabul edilen kaynakları sınırlayan yapılandırma (izin listesi, bağlayıcı kapsamı, yükleme yetkileri); `LOG` Onaysız kaynak ret kayıtları; son 90 günde olmadıysa test kaydı

### CON-INF-01 · Çıkarımın yönetilen sınır içinde kalması  `L1`

**Soru:** AI modelleriniz kendi altyapınızda, dışarıya internet erişimi olmadan mı çalışıyor?

**Derinleştirme:** Modeller nerede çalışıyor ve çıkarım ortamı sınırın dışındaki bir yere erişebiliyor mu?

**Uygulanabilirlik:** Yalnız Sovereign profil. Controlled External sistemlerde CON-INF-02 değerlendirilir.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Sistemin en az bir modeli yönetilen sınır içinde çalışıyor (dış bir servis üzerinden değil). | E / H / B |
| c2 | temel | Sistemin modellerinden yönetilen sınır içinde çalışanların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Çıkarım ortamından çıkış varsayılan red; yalnız listelenmiş iç hedeflere izin var. | E / H / B |
| c4 | temel | İzin listesinde hiçbir dış hedef yok (telemetri, çalışma anında model ya da paket indirme dahil). | E / H / B |
| s1 | sürdürme | Çıkarım ortamından dışarıya bağlantı denemesi alarm üretiyor ve her alarmın ele alınma kaydı var. | E / H / B |
| s2 | sürdürme | Son çıkış testinin tarihi 6 ay içinde. **[≤ 6 ay]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c5

*Terimler:* **varsayılan red çıkış**: Hedef açık bir izin listesinde değilse dışarıya giden trafik engellenir; kural uygulamada değil ağ yapılandırmasında uygulanır. · **yönetilen sınır**: Kurumun işlettiği ya da sözleşmeyle kontrol ettiği, ağ politikasını kendisinin belirlediği altyapı (kendi veri merkezi, ayrılmış ya da özel bulut kiracılığı). Paylaşımlı genel API sınırın dışındadır.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c5) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c5) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Her modelin nerede çalıştığını ve sınırı gösteren mimari; `CFG` Çıkarım ortamı için çıkış politikası (varsayılan red, listelenmiş iç hedefler); `LOG` Çıkarım ortamından en az 7 günlük çalışmaya ait çıkış/düşürme kayıtları ya da tarihli çıkış testi

### CON-STO-02 · Kontrollü anahtarlarla depolamada şifreleme  `L1`

**Soru:** AI sistemlerinizin kullandığı belgeler, indeksler ve kayıtlar saklandıkları yerde şifreli mi?

**Derinleştirme:** Kayıtlar ve yedekler dahil AI verisi tutan her depo depolamada şifreli mi, anahtarlar kimde?

**Uygulanabilirlik:** Her zaman uygulanır. Sağlayıcının işlettiği depolarda kanıt, sağlayıcının belgelenmiş şifreleme ve anahtar düzenidir.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Sistemin kaynak belgelerini ya da korpusunu tutan depolar depolamada şifreli. | E / H / B |
| c2 | temel | Depo envanteri indeksler, prompt ve yanıt kayıtları, yedekler ve sağlayıcı depoları dahil her AI veri deposunu sayıyor. | E / H / B |
| c3 | temel | Envanterdeki depolardan depolamada şifreli olduğu yapılandırma ya da sağlayıcı belgesiyle gösterilenlerin oranı. **[%100 (hepsi)]** | E / H / B |
| c4 | temel | Envanterdeki depolardan anahtar sahibi kayıtlı olanların oranı. **[%100 (hepsi)]** | E / H / B |
| s1 | sürdürme | Anahtar rotasyonu ya da anahtarlara erişim gözden geçirilmiş; tarihli kaydı 12 ay içinde. **[≤ 12 ay]** | E / H / B |

*Terimler:* **AI veri deposu**: AI sisteminin verisini tutan her depo: belge korpusu, vektör indeksi, veritabanı, model dosyaları, prompt ve yanıt kayıtları, yedekler. Sağlayıcının işlettiği depolar dahildir. · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **anahtar sahibi**: Bir deponun şifreleme anahtarını kontrol eden taraf; şunlardan biri olarak kaydedilir: kurum (kendi KMS/HSM), sağlayıcı KMS'i üzerinden kurum ya da sağlayıcı.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c4) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c4) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Depo başına şifreleme durumu ve anahtar sahibini gösteren depo envanteri (CON-STO-01 + sağlayıcı depoları ve yedekler); `CFG` Kurumun işlettiği depolar için şifreleme yapılandırması; `DOC` Sağlayıcının işlettiği depolar için sağlayıcı belgeleri

### HYG-ING-01 · Kişisel veri kapsamı ve muamelesi tanımlı  `L1`

**Soru:** Yapay zekâ sistemlerine giren belgelerde hangi kişisel verilerin aranacağı ve bunlara ne yapılacağı yazılı olarak belirlenmiş mi?

**Derinleştirme:** Bu yapay zekâ sistemine giren verilerde hangi kişisel veri türleri tespit edilmeli ve her biri için ne yapılıyor (engelleme, maskeleme, takma adlandırma, izinli)?

**Uygulanabilirlik:** Kurumun sisteme en az bir veri giriş yolu işlettiği durumda uygulanır (belge yükleme, RAG indeksleme, veri seti aktarımı, bağlayıcı senkronizasyonu). Tek veri girişi kullanıcının yazdığı prompt ise NA işaretlenir, HYG-PRM değerlendirilir.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Sistem için tespit edilecek kişisel veri kategorilerinin yazılı listesi var. | E / H / B |
| c2 | temel | Kapsamdaki veri kaynaklarından listede karşılığı olanların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Liste özel nitelikli kişisel verileri içeriyor. | E / H / B |
| c4 | temel | Liste ilgili yerel tanımlayıcıları (ör. TCKN, IBAN) içeriyor. | E / H / B |
| c5 | temel | Her kategori için muamele tanımlı; her "izin ver" için yazılı dayanak var. | E / H / B |
| c6 | temel | Liste adı belli bir sahip tarafından onaylanmış. | E / H / B |
| s1 | sürdürme | Son tarihli gözden geçirme 12 ay içinde ve son veri kaynağı eklenmesinden önce değil. | E / H / B |

*Terimler:* **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **veri giriş yolu**: İçeriğin bir yapay zekâ sistemine saklanmak, indekslenmek, bağlam olarak ya da eğitimde kullanılmak üzere girdiği her yol: dosya yükleme, başka sisteme bağlayıcı, API, zamanlanmış aktarım, e-posta ya da sohbet kanalı. Her bağlayıcı ve her API ayrı yol sayılır. · **özel nitelikli kişisel veri**: KVKK md. 6'daki (ve uygulanıyorsa GDPR md. 9'daki) kategoriler: ırk, etnik köken, siyasi düşünce, inanç, kılık kıyafet, dernek/sendika üyeliği, sağlık, cinsel hayat, ceza mahkûmiyeti, biyometrik ve genetik veri. · **muamele**: HYG-ING-01'de her kişisel veri kategorisi için tanımlanan işlem: maskeleme, tokenizasyon, takma adlandırma, çıkarma ya da engelleme. Yalnız tespit edip kaydetmek muamele değildir.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c6) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c6) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Veri kaynağı başına kategori listesi (ör. TCKN, IBAN, kart numarası, telefon, adres, sağlık verisi); `DOC` Muamele tablosu: kategori -> engelle / maskele / takma adlandır / izin ver; 'izin ver' için dayanak; `DOC` Sahibini adıyla gösteren onay kaydı

### HYG-ING-02 · Saklamadan önce otomatik tespit ve muamele  `L1`

**Soru:** Yapay zekâ sistemlerine yüklenen veya bağlanan verilerdeki kişisel veriler (TCKN, IBAN, sağlık verisi vb.) otomatik olarak maskeleniyor mu?

**Derinleştirme:** Kişisel veriler hangi giriş noktalarında otomatik olarak tespit edilip maskeleniyor? Bu işlem veri saklanmadan ya da indekslenmeden önce mi yapılıyor?

**Uygulanabilirlik:** HYG-ING-01 ile aynı.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | En az bir veri giriş yolunda kişisel veriyi otomatik tespit eden bir kontrol var. | E / H / B |
| c2 | temel | Giriş yolu envanteri var. | E / H / B |
| c3 | temel | Envanterdeki yollardan tespit kontrolü bulunanların oranı. **[%100 (hepsi)]** | E / H / B |
| c4 | temel | Kontrol bulunan yollardan kontrolün saklamadan önce çalıştığı yolların oranı. **[%100 (hepsi)]** | E / H / B |
| c5 | temel | Kontrol HYG-ING-01'deki muameleyi otomatik uyguluyor (yalnız kaydetmiyor, elle adım gerekmiyor). | E / H / B |
| s1 | sürdürme | Değişiklik sürecinde, yeni bir giriş yolunun kontrol olmadan canlıya alınmasını engelleyen bir adım var. | E / H / B |
| s2 | sürdürme | Yol envanteri çalışan sistemle karşılaştırılmış; tarihli kaydı 6 ay içinde. **[≤ 6 ay]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c6

*Terimler:* **saklamadan önce**: Kontrol, içerik yapay zekâ sisteminin okuduğu herhangi bir depoya (vektör indeksi, veritabanı, dosya deposu, eğitim kümesi) yazılmadan önce çalışır. Geçici işlem belleği depo sayılmaz. · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **veri giriş yolu**: İçeriğin bir yapay zekâ sistemine saklanmak, indekslenmek, bağlam olarak ya da eğitimde kullanılmak üzere girdiği her yol: dosya yükleme, başka sisteme bağlayıcı, API, zamanlanmış aktarım, e-posta ya da sohbet kanalı. Her bağlayıcı ve her API ayrı yol sayılır. · **giriş yolu envanteri**: Sistemin her veri giriş yolunu adıyla gösteren, tarihli yazılı liste (ya da mimari/veri akış şeması). Yollarla ilgili oran kontrollerinin paydasıdır. · **muamele**: HYG-ING-01'de her kişisel veri kategorisi için tanımlanan işlem: maskeleme, tokenizasyon, takma adlandırma, çıkarma ya da engelleme. Yalnız tespit edip kaydetmek muamele değildir.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c6) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c6) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Veri giriş yolları envanteri (mimari ya da veri akış şeması); `CFG` Kontrolün her yoldaki varlığını ve saklama/indeksleme öncesindeki yerini gösteren yapılandırma; `LOG` Son 30 güne ait, her yoldan tespit/muamele kayıtları

### IDE-STO-01 · AI verisine ve artefaktlarına rol bazlı erişim  `L1`

**Soru:** AI sistemlerinizin belgelerine ve kayıtlarına erişim, rol bazında ve adı belli kişilerle sınırlı mı?

**Derinleştirme:** Bu AI sisteminin belgelerini, indekslerini, model dosyalarını ve kayıtlarını kim okuyabilir ya da değiştirebilir, buna nasıl karar veriliyor?

**Uygulanabilirlik:** Her zaman uygulanır. Sağlayıcının işlettiği depolarda kurum tarafındaki erişim (yönetim konsolları, çalışma alanı rolleri) değerlendirilir.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | Her AI veri deposu kimlik doğrulama istiyor ve hiçbiri varsayılan olarak tüm çalışanlara açık değil. | E / H / B |
| c2 | temel | Prompt ve yanıt kayıtları dahil depolardan rolleri tanımlı olanların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Hiçbir depoya paylaşımlı ya da genel hesabın erişimi yok. | E / H / B |
| c5 | temel | Son erişim gözden geçirmesinin (gözden geçiren ve kaldırılan erişimlerle) tarihi son 12 ay içinde. **[≤ 12 ay]** | E / H / B |
| s1 | sürdürme | Son erişim gözden geçirmesinin tarihi 6 ay içinde. **[≤ 6 ay]** | E / H / B |
| s2 | sürdürme | Ayrılan çalışanlardan erişimi 2 iş günü içinde kaldırılanların oranı. **[%100 (hepsi)]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c4

*Terimler:* **AI veri deposu**: AI sisteminin verisini tutan her depo: belge korpusu, vektör indeksi, veritabanı, model dosyaları, prompt ve yanıt kayıtları, yedekler. Sağlayıcının işlettiği depolar dahildir. · **paylaşımlı ya da genel hesap**: Birden fazla kişinin kullandığı ya da adı belli bir kişiye bağlı olmayan hesap (ör. "admin", "ai-ekip"). Yalnız bir sistemin kullandığı ve adı belli sahibi olan servis hesapları sayılmaz.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c5) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c5) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Her depo için rol tanımları ve rol başına kimlik listesi; `CFG` Her depo için erişim kontrol yapılandırması (ya da yetki dökümü); `DOC` Tarih, gözden geçiren ve kaldırılan erişimleri içeren erişim gözden geçirme kaydı

### TRA-ING-01 · Kurcalamaya dayanıklı kaynak kaydı  `L1`

**Soru:** AI sistemlerinizdeki her belgenin nereden ve ne zaman geldiğini, değiştirilemeyen bir kayıttan gösterebilir misiniz?

**Derinleştirme:** AI sistemindeki herhangi bir belge için nereden, ne zaman geldiğini ve ona ne yapıldığını gösterebilir misiniz; bu kaydı kim değiştirebilir?

**Uygulanabilirlik:** HYG-ING-01 ile aynı.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | En az bir giriş yolunda veri girişi kaydediliyor. | E / H / B |
| c2 | temel | Giriş yollarından dört kaynak alanının hepsini kaydedenlerin oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Kayıt deposu korumalı. | E / H / B |
| s1 | sürdürme | Kayıt bütünlüğü doğrulanmış (ör. özet kontrolü ya da boşluk tespiti); tarihli kaydı 3 ay içinde. **[≤ 3 ay]** | E / H / B |
| s2 | sürdürme | Kayıt saklama süresi tanımlı saklama süresiyle örtüşüyor. | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c4

*Terimler:* **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **giriş yolu envanteri**: Sistemin her veri giriş yolunu adıyla gösteren, tarihli yazılı liste (ya da mimari/veri akış şeması). Yollarla ilgili oran kontrollerinin paydasıdır. · **korumalı kayıt deposu**: Şunlardan en az birinin geçerli olduğu kayıt deposu: yalnız ekleme ya da tek yazım (WORM) ayarı; sistem yöneticilerinden ayrı yazma/silme yetkisi; bütünlük doğrulaması (özet zinciri ya da imza). · **dört kaynak alanı**: Kaynak, zaman, tespit edilen veri kategorileri, uygulanan muamele.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c4) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c4) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1–s2) karşılanıyor. |

*AS-02'de istenecek kanıt:* `CFG` Her giriş yolunda dört alanı (kaynak, zaman, kategoriler, muamele) içeren kayıt yapılandırması; `CFG` Kayıt deposu koruması (yalnız ekleme ya da tek yazım ayarı, sistem yöneticilerinden ayrı yetki ya da bütünlük doğrulaması); `TST` Saklanan üç örnek öğenin kayıt girdilerine kadar izlenmesi

### HYG-PRM-01 · Prompt'taki kişisel verinin modele ulaşmadan işlenmesi  `L2`

**Soru:** AI araçlarına yazılan ya da yapıştırılan kişisel veriler modele ulaşmadan otomatik olarak maskeleniyor mu?

**Derinleştirme:** Bir kullanıcı prompt'a müşterinin TCKN'sini ya da sağlık verisini yapıştırırsa, bu veri modele ulaşmadan ne oluyor?

**Uygulanabilirlik:** Prompt arayüzü olan her sisteme uygulanır.

Her kontrol için **E** (evet) / **H** (hayır) / **B** (bilmiyor). Sayı ya da tarih isteyen kontrolde eşik sağlanıyorsa E. Puan cevaplardan hesaplanır, elle verilmez.

| Kontrol | Tür | İfade (doğru mu?) | Cevap |
|---|---|---|---|
| c1 | varlık | En az bir prompt kanalında model çağrısından önce otomatik kişisel veri kontrolü var. | E / H / B |
| c2 | temel | Prompt kanallarından kontrolün model çağrısından önce çalıştığı kanalların oranı. **[%100 (hepsi)]** | E / H / B |
| c3 | temel | Serbest metnin yanında ekler de kontrol ediliyor. | E / H / B |
| c4 | temel | Kontrol tanımlı muameleyi uyguluyor (yalnız tespit edip uyarmıyor). | E / H / B |
| c5 | temel | Kullanıcının her atlatması kayıtlı gerekçe gerektiriyor. | E / H / B |
| s1 | sürdürme | Atlatmalar ve tespitler gözden geçirilmiş, aksiyonlar yazılmış; tarihli kaydı 3 ay içinde. **[≤ 3 ay]** | E / H / B |

*QS'de sorulmaz, AS-02'de bakılır:* c6

*Terimler:* **atlatma**: İçeriği tanımlı muamele olmadan modele gönderen kullanıcı eylemi (ör. "yine de gönder", kontrolü bir oturum için kapatma). · **tarihli kayıt**: Tarihi, işi kimin yaptığını, ne bulunduğunu ve sonuçtaki aksiyonu (ya da "bulgu yok") gösteren belge, kayıt talebi ya da log girdisi. Takvim daveti ya da sözlü beyan sayılmaz. · **prompt kanalı**: Metnin ya da dosyanın modele prompt olarak ulaştığı her yol: sohbet arayüzü, API, eklenti ya da entegrasyon, e-posta ya da sohbet botu. Her biri ayrı sayılır. · **muamele**: HYG-ING-01'de her kişisel veri kategorisi için tanımlanan işlem: maskeleme, tokenizasyon, takma adlandırma, çıkarma ya da engelleme. Yalnız tespit edip kaydetmek muamele değildir.

| Puan | Ölçüt |
|---|---|
| 0 | Varlık kontrolü (c1) karşılanmıyor. |
| 1 | c1 karşılanıyor; temel kontrollerden (c2–c6) en az biri karşılanmıyor. |
| 2 | c1 ve tüm temel kontroller (c2–c6) karşılanıyor. |
| 3 | 2 ve tüm sürdürme kontrolleri (s1) karşılanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Prompt'lar için kategori ve muamele listesi (HYG-ING-01 kullanılabilir; serbest metin ve ekleri kapsamalı); `CFG` Kontrolün her prompt kanalında (arayüz, API, eklentiler) model çağrısından önce bulunduğunu gösteren yapılandırma; `LOG` Kanal başına son 30 güne ait tespit/muamele kayıtları

