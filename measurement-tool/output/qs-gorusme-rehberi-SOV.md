# Quick Scan Görüşme Rehberi — Sovereign profili

*Lecta Sovereign AI Control Framework · v1.0-draft · kaynaktan üretildi (`tools/qs.py`) — elle düzenlemeyin*

## Görüşmeye başlarken (okunacak metin)

> Bu görüşme bir **Hızlı Tarama**dır: sorularımız beyanınıza dayanır, kanıt incelemesi yapılmaz. Sonuç bir **gösterge hazırlık seviyesidir**; denetim görüşü ya da belge değildir. Bilmediğiniz soruya "bilmiyorum" demeniz en doğru cevaptır ve öyle kaydedilir.

**Puanlama notu:** Her maddede beyana göre 0–3 verilir (`basis: declared`). Katılımcı cevabı bilmiyorsa **NE**; madde kurumda yoksa ve uygulanabilirlik ölçütü karşılanmıyorsa **NA** (gerekçe yazılır). Kanıt istenmez; katılımcı kendiliğinden gösterirse `evidence_ref` alanına not edilir.

**Süre:** 9 kurum + 8 sistem maddesi (sistem başına) · ~4 dk/madde · 1 sistemle ~83 dk.

## Bölüm A — Kurum (G bloğu, kurum başına bir kez)

### G-POL-02 · Yapay zekâ araçlarının kabul edilebilir kullanımı  `L0`

**Soru:** Çalışanların hangi AI araçlarını kullanabileceği ve hangi verileri girebileceğine dair yazılı kural var mı?

**Derinleştirme:** Çalışanlar hangi yapay zekâ araçlarını kullanabileceklerini ve bunlara hangi verileri girebileceklerini biliyor mu?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | Çalışanların AI araçlarını kullanımına dair yazılı kural yok. |
| 1 | Kurallar var ama şunlardan en az biri geçerli: kurumun veri sınıflandırmasına atıf yapmıyor; onaylı araç listesi yok; liste son 12 ayda güncellenmemiş; görüşülen çalışanlar kuralları bilmiyor. |
| 2 | Kurallar veri sınıflandırmasına atıf yapıyor; onaylı araç listesi araç başına izin verilen veri sınıflarını belirtiyor ve son 12 ayda güncellenmiş; farklı birimlerden görüşülen en az iki çalışan kuralları tutarlı anlatıyor. |
| 3 | 2'yi karşılıyor ve kurallara uyum 6 ay içinde G-INV-02 verileriyle karşılaştırılarak kontrol edilmiş; bulgu ve aksiyonların tarihli kaydı var. |

*AS-02'de istenecek kanıt:* `DOC` Kabul edilebilir kullanım kuralları (ayrı belge ya da AI/kabul edilebilir kullanım politikası içinde); `DOC` Araç başına izin verilen veri sınıflarını ve son güncelleme tarihini gösteren onaylı AI araç listesi; `INT` Farklı birimlerden en az iki çalışan kuralları tutarlı biçimde anlatıyor

### G-INV-01 · Yapay zekâ sistem envanteri  `L1`

**Soru:** Kullanılan AI sistemlerinin ve kullanım senaryolarının, her birinin sahibiyle birlikte bir listesi var mı?

**Derinleştirme:** Hangi yapay zekâ sistemleri ve kullanım senaryoları canlıda ya da pilotta, nerede kayıtlı?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | AI sistemleri ya da kullanım senaryoları için envanter yok. |
| 1 | Envanter var ama şunlardan en az biri geçerli: bir ya da daha fazla kayıtta zorunlu bir alan boş; satın alma kayıtlarında, onaylı araç listesinde ya da görüşmelerde görülen bir sistem envanterde yok; son 6 ayda güncellenmemiş. |
| 2 | Her kayıtta tüm zorunlu alanlar dolu; satın alma kayıtlarında, onaylı araç listesinde ya da görüşmelerde görülen hiçbir sistem eksik değil; envanter son 6 ayda güncellenmiş. |
| 3 | 2'yi karşılıyor ve envanter 6 ay içinde G-INV-02 trafik verileriyle karşılaştırılmış; eklenen ve çıkarılan kayıtların tarihli kaydı var. |

*AS-02'de istenecek kanıt:* `DOC` Amaç, sahip, kullanıcılar, veri kategorileri, sağlayıcı, profil ve durum alanlarını içeren envanter; `DOC` Karşılaştırma için onaylı araç listesi (G-POL-02) ve satın alma ya da proje kayıtları

### G-LIT-01 · Tüm kullanıcılar için yapay zekâ okuryazarlığı  `L1`

**Soru:** AI araçlarını kullanan çalışanlar güvenli kullanım eğitimi aldı mı?

**Derinleştirme:** AI kullanıcıları hangi eğitimi alıyor ve ne kadarı tamamladı?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | Yapay zekâ okuryazarlık programı yok. |
| 1 | Program var ama şunlardan en az biri geçerli: üç konudan birini atlıyor; tamamlama kaydedilmiyor; kayıtlı tamamlama AI kullanıcılarının %80'inin altında. |
| 2 | Program üç konuyu kapsıyor ve AI kullanıcılarının en az %80'inin kayıtlı tamamlaması var; yeni kullanıcılar erişimden sonraki 60 gün içinde tamamlıyor. |
| 3 | 2'yi karşılıyor; içerik 12 ay içinde güncellenmiş ve anlama ölçülüyor (sınav ya da uygulama), sonuçlar kayıtlı. |

*AS-02'de istenecek kanıt:* `DOC` Üç konuyu kapsayan program içeriği; `LOG` Kişi başına tarihli tamamlama kayıtları; payda için G-INV-01'den AI kullanıcı sayısı

### G-POL-01 · Yapay zekâ politikası  `L1`

**Soru:** Onaylanmış bir yapay zekâ politikanız var mı, çalışanlara duyuruldu mu?

**Derinleştirme:** Kurumun onaylanmış bir yapay zekâ politikası var mı ve çalışanlara nasıl duyuruldu?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | Yapay zekâ politikası yok ve AI başka hiçbir onaylı politikada ele alınmıyor. |
| 1 | Politika ya da taslak var ama şunlardan en az biri geçerli: üst yönetim ya da yetkilendirdiği bir kurul tarafından onaylanmamış; hesap verecek rolü belirtmiyor; yeni bir AI sisteminin nasıl onaylanacağını tanımlamıyor; çalışanlara duyurulduğuna dair kayıt yok. |
| 2 | Politika üst yönetim ya da yetkilendirilmiş kurul tarafından onaylanmış, hesap verecek rolü belirtiyor, yeni AI sistemleri için onay yolunu tanımlıyor, G-POL-02'ye atıf yapıyor ve kapsamdaki tüm çalışanlara duyurulduğuna dair kayıt var. |
| 3 | 2'yi karşılıyor ve politika 12 ay içinde gözden geçirilmiş; değişiklikleri ya da değişiklik olmadığını belirten tarihli kayıt var. |

*AS-02'de istenecek kanıt:* `DOC` Onay kaydıyla (onaylayan, tarih, sürüm) yapay zekâ politikası; `DOC` Duyuru kaydı (intranet yayını, e-posta, okundu listesi)

### G-ROL-01 · Roller ve hesap verebilirlik  `L1`

**Soru:** Her AI sisteminin adı belli bir sahibi ve genel olarak AI yönetişiminden sorumlu biri var mı?

**Derinleştirme:** Her AI sisteminden kim sorumlu? KVKK irtibat kişisi/DPO ve güvenlik birimi hangi noktalarda devreye girmek zorunda?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | Adı belli sahip yok, yönetişim rolü yok. |
| 1 | Şunlardan en az biri geçerli: envanterdeki bir ya da daha fazla sistemin adı belli sahibi yok; yönetişim rolü resmî olarak atanmamış; DPO ve güvenlik için danışma noktaları tanımlı değil. |
| 2 | Envanterdeki her sistemin adı belli sahibi var, yönetişim rolü resmî olarak atanmış, danışma noktaları tanımlı ve en az bir danışmanın yapıldığına dair kayıt var (ya da son 12 ayda tetiklenmediği belirtilmiş). |
| 3 | 2'yi karşılıyor ve sahipler ile rol atamaları 12 ay içinde teyit edilmiş; personel değişikliği sonrası güncellemeleri de içeren tarihli kayıt var. |

*AS-02'de istenecek kanıt:* `DOC` G-INV-01'de kişi ya da rol adıyla doldurulmuş sahip alanı; `DOC` AI yönetişim rolü için atama yazısı ya da görev tanımı; `DOC` DPO ve güvenlik için tanımlı danışma noktaları (ör. yeni sistem, yeni veri kategorisi, yeni sağlayıcı)

### G-INC-01 · Yapay zekâ olay prosedürü  `L2`

**Soru:** Olay prosedürünüz prompt üzerinden veri sızıntısı gibi AI'ye özgü olayları kapsıyor mu?

**Derinleştirme:** Bir prompt üzerinden kişisel veri sızsa ya da bir AI sistemi zararlı bir çıktı üretse kime, kim tarafından, ne kadar sürede bildirilir?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | AI olayları hiçbir prosedürde ele alınmıyor. |
| 1 | Şunlardan en az biri geçerli: prosedür dört AI olay türünü adlandırmıyor; raporlama zincirinde adı belli roller yok; uygulanan bildirim süreleri eksik; genel olay süreciyle bağlantılı değil. |
| 2 | Prosedür dört olay türünü, adı belli rollerle raporlama zincirini ve uygulanan süreleri tanımlıyor, genel süreçle bağlantılı ve son 12 ayda bir tatbikat ya da ele alınmış bir AI olayı kayıtlı. |
| 3 | 2'yi karşılıyor; her tatbikat ya da olaydan çıkan dersler kayıtlı, aksiyonlar kapanışa kadar izleniyor ve prosedür 12 ay içinde gözden geçirilmiş. |

*AS-02'de istenecek kanıt:* `DOC` En az şu AI olay türlerini adlandıran prosedür — prompt ya da çıktı yoluyla veri sızıntısı, etkisi olan zararlı ya da yanlış çıktı, model üzerinden yetkisiz erişim, sağlayıcı tarafı olay; `DOC` Bildirim süreleri tablosu (ör. KVKK ihlal bildirimi, sektör ve siber güvenlik yükümlülükleri); `TST` Bir tatbikatın ya da ele alınmış bir AI olayının kaydı

### G-INV-02 · AI servis kullanımının görünürlüğü  `L2`

**Soru:** Çalışanların hangi dış AI servislerini kullandığını ağ kayıtlarından görebiliyor musunuz?

**Derinleştirme:** Geçen ay ağınızdan hangi dış AI servislerine, hangi birimlerden erişildiğini gösterebilir misiniz?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | AI servislerine giden trafik tanımlanamıyor ya da ilgili kayıtlar tutulmuyor. |
| 1 | Kayıtlar var ama şunlardan en az biri geçerli: saklama 90 günden kısa; trafik bir birime ya da kullanıcı grubuna atfedilemiyor; AI servis alan adı listesi tutulmuyor; hiç rapor üretilmemiş. |
| 2 | Kayıtlar en az 90 gün saklanıyor, trafik bir birime ya da kullanıcı grubuna atfedilebiliyor, AI servis alan adı listesi son 6 ayda güncellenmiş ve talep edildiğinde en az 30 günlük rapor üretilebiliyor. |
| 3 | 2'yi karşılıyor; raporlar 3 ay içinde gözden geçiriliyor ve onaylı listede (G-POL-02) olmayan servislere giden trafik kayıtlı bir takip başlatıyor. |

*AS-02'de istenecek kanıt:* `CFG` DNS, proxy ya da firewall kayıt yapılandırması ve saklama süresi; `DOC` Tanımlama için kullanılan, güncelleme tarihli AI servis alan adı/uç nokta listesi; `LOG` En az 30 günlük dönem için birim bazında AI servis trafiği raporu ya da sorgu sonucu

### G-RSK-01 · Yapay zekâ risk değerlendirmesi  `L2`

**Soru:** Bir AI sistemi canlıya alınmadan önce yazılı risk değerlendirmesi yapılıyor mu?

**Derinleştirme:** Bir AI sisteminin riskleri canlıya alınmadan önce nasıl değerlendiriliyor ve bu değerlendirme ne zaman tekrarlanıyor?

**Uygulanabilirlik:** Her zaman uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | Hiçbir AI sistemi için risk değerlendirmesi yok. |
| 1 | Şunlardan en az biri geçerli: yalnız bazı sistemler için değerlendirme var; yazılı yöntem yok; değerlendirmeler AI'ye özgü riskleri (prompt ile veri çıkışı, yanlış ya da zararlı çıktı, model üzerinden yetkisiz erişim, sağlayıcı bağımlılığı) ele almıyor; yeniden değerlendirme tetikleyicileri tanımlı değil. |
| 2 | Canlıdaki her sistem için, yazılı yöntemle yapılmış, dört AI'ye özgü risk grubunu ele alan, muamele kararları sahip tarafından onaylanmış tarihli bir değerlendirme var ve yeniden değerlendirme tetikleyicileri tanımlı. |
| 3 | 2'yi karşılıyor ve her değerlendirme 12 ay içinde ya da her tetikleyici olaydan sonra (hangisi önce gelirse) tekrarlanmış, kayıtları var. |

*AS-02'de istenecek kanıt:* `DOC` AI'ye özgü riskleri kapsayan risk değerlendirme yöntemi (kriterler, ölçekler, kabul); `DOC` Envanterdeki her sistem için tarihli, muamele kararlarını ve sahip onayını içeren risk değerlendirmesi; `DOC` Tanımlı yeniden değerlendirme tetikleyicileri (yeni model ya da sağlayıcı, yeni veri kategorisi, yeni kullanıcı grubu, olay)

### G-SUP-01 · Kullanım öncesi AI sağlayıcı değerlendirmesi  `L2`

**Soru:** Dış bir AI servisini kullanmadan önce verinin nerede tutulduğunu ve sağlayıcının onu eğitimde kullanıp kullanmadığını kontrol ediyor musunuz?

**Derinleştirme:** Dış bir AI servisini kullanmadan önce verinin nereye gittiği ve sağlayıcının onu nasıl kullandığı konusunda neyi kontrol ediyorsunuz?

**Uygulanabilirlik:** Kurum verisiyle hiçbir dış AI modeli ya da servisi kullanılmıyorsa uygulanmaz (G-INV-01 ve G-INV-02'ye göre).

| Puan | Ölçüt |
|---|---|
| 0 | Dış AI servisleri hiçbir sağlayıcı değerlendirmesi olmadan kullanılıyor. |
| 1 | Şunlardan en az biri geçerli: yalnız bazı sağlayıcılar değerlendirilmiş; bir değerlendirme beş konudan birini atlıyor; değerlendirme ilk kullanımdan sonra tarihli; dayanılan sağlayıcı belgeleri saklanmamış. |
| 2 | Kurum verisiyle kullanılan her sağlayıcının, beş konunun hepsini kapsayan, ilk kullanımdan önce tarihli değerlendirmesi var ve dayanılan sağlayıcı belgeleri saklanıyor. |
| 3 | 2'yi karşılıyor ve her değerlendirme 12 ay içinde ve sağlayıcı koşullarında ya da alt işleyenlerde bildirilen her değişiklikten sonra tekrarlanmış, kayıtları var. |

*AS-02'de istenecek kanıt:* `DOC` Sağlayıcı başına beş konuyu kapsayan, ilk kullanımdan önce tarihli değerlendirme kaydı; `DOC` Dayanılan sağlayıcı belgeleri (koşullar, veri işleme eki, alt işleyen listesi, veri yerleşimi beyanı)

## Bölüm B — Sistem (her sistem için ayrı; en çok 2 sistem)

### CON-ING-01 · Yalnız onaylı veri kaynakları  `L0`

**Soru:** AI sistemlerinize hangi sistem ya da kaynakların veri besleyebileceği tanımlı mı, diğerleri engelleniyor mu?

**Derinleştirme:** Bu AI sistemine hangi kaynaklar veri besleyebilir ve başka bir kaynaktan gelen veriye ne oluyor?

**Uygulanabilirlik:** HYG-ING-01 ile aynı (kurumun işlettiği en az bir veri giriş yolu).

| Puan | Ölçüt |
|---|---|
| 0 | Kaynak kaydı yok ve giriş yollarında kısıt yok. |
| 1 | Şunlardan en az biri geçerli: kayıt var ama bir ya da daha fazla yol kayıt dışı kaynaklardan veri kabul ediyor; kısıt yapılandırılmış ama kayıt yok; ne ret kaydı ne test kaydı sunulabiliyor. |
| 2 | Kullanılan her kaynak kayıtta, her yol yalnız kayıtlı kaynakları kabul ediyor ve ret kayıtları ya da tarihli bir test kaydı onaysız bir kaynağın reddedildiğini gösteriyor. |
| 3 | 2'yi karşılıyor; kayıt 6 ay içinde çalışan yapılandırmayla karşılaştırılmış ve kaynak eklemek kayıtlı bir onay gerektiriyor. |

*AS-02'de istenecek kanıt:* `DOC` Onaylı kaynak kaydı (kaynak, sahip, veri kategorileri, giriş yolu, onay tarihi); `CFG` Her giriş yolunda kabul edilen kaynakları sınırlayan yapılandırma (izin listesi, bağlayıcı kapsamı, yükleme yetkileri); `LOG` Onaysız kaynak ret kayıtları; son 90 günde olmadıysa test kaydı

### CON-INF-01 · Çıkarımın yönetilen sınır içinde kalması  `L1`

**Soru:** AI modelleriniz kendi altyapınızda, dışarıya internet erişimi olmadan mı çalışıyor?

**Derinleştirme:** Modeller nerede çalışıyor ve çıkarım ortamı sınırın dışındaki bir yere erişebiliyor mu?

**Uygulanabilirlik:** Yalnız Sovereign profil. Controlled External sistemlerde CON-INF-02 değerlendirilir.

| Puan | Ölçüt |
|---|---|
| 0 | Çıkarım ortamının dışarıya kısıtsız erişimi var ya da modeller dış bir servis üzerinden çağrılıyor. |
| 1 | Modeller sınır içinde çalışıyor ama şunlardan en az biri geçerli: çıkış varsayılan red değil; listelenenler dışında dış hedefler var (ör. telemetri, çalışma anında model ya da paket indirme); kayıt ya da test kanıtı yok. |
| 2 | Tüm modeller sınır içinde çalışıyor, çıkış yalnız listelenmiş iç hedeflerle varsayılan red ve kayıtlar ya da tarihli bir test başka bir dış bağlantı olmadığını gösteriyor. |
| 3 | 2'yi karşılıyor; çıkarım ortamından dışarıya bağlantı denemeleri alarm üretiyor ve ele alınıyor; çıkış testi 6 ay içinde tekrarlanıyor. |

*AS-02'de istenecek kanıt:* `DOC` Her modelin nerede çalıştığını ve sınırı gösteren mimari; `CFG` Çıkarım ortamı için çıkış politikası (varsayılan red, listelenmiş iç hedefler); `LOG` Çıkarım ortamından en az 7 günlük çalışmaya ait çıkış/düşürme kayıtları ya da tarihli çıkış testi

### CON-STO-02 · Kontrollü anahtarlarla depolamada şifreleme  `L1`

**Soru:** AI sistemlerinizin kullandığı belgeler, indeksler ve kayıtlar saklandıkları yerde şifreli mi?

**Derinleştirme:** Kayıtlar ve yedekler dahil AI verisi tutan her depo depolamada şifreli mi, anahtarlar kimde?

**Uygulanabilirlik:** Her zaman uygulanır. Sağlayıcının işlettiği depolarda kanıt, sağlayıcının belgelenmiş şifreleme ve anahtar düzenidir.

| Puan | Ölçüt |
|---|---|
| 0 | Kişisel ya da gizli veri tutan bir ya da daha fazla depo şifresiz ya da durum bilinmiyor. |
| 1 | Ana depolar şifreli ama şunlardan en az biri geçerli: kayıtlar, indeksler ya da yedekler şifresiz; her depo için anahtar sahibi belirlenmemiş; yapılandırma ya da sağlayıcı kanıtı sunulamıyor. |
| 2 | Kayıtlar, indeksler ve yedekler dahil envanterdeki her depo depolamada şifreli, yapılandırma ya da sağlayıcı kanıtı var ve her biri için anahtar sahibi kayıtlı. |
| 3 | 2'yi karşılıyor ve anahtar rotasyonu ya da anahtarlara erişim 12 ay içinde gözden geçirilmiş, kaydı var. |

*AS-02'de istenecek kanıt:* `DOC` Depo başına şifreleme durumu ve anahtar sahibini gösteren depo envanteri (CON-STO-01 + sağlayıcı depoları ve yedekler); `CFG` Kurumun işlettiği depolar için şifreleme yapılandırması; `DOC` Sağlayıcının işlettiği depolar için sağlayıcı belgeleri

### HYG-ING-01 · Kişisel veri kapsamı ve muamelesi tanımlı  `L1`

**Soru:** Yapay zekâ sistemlerine giren belgelerde hangi kişisel verilerin aranacağı ve bunlara ne yapılacağı yazılı olarak belirlenmiş mi?

**Derinleştirme:** Bu yapay zekâ sistemine giren verilerde hangi kişisel veri türleri tespit edilmeli ve her biri için ne yapılıyor (engelleme, maskeleme, takma adlandırma, izinli)?

**Uygulanabilirlik:** Kurumun sisteme en az bir veri giriş yolu işlettiği durumda uygulanır (belge yükleme, RAG indeksleme, veri seti aktarımı, bağlayıcı senkronizasyonu). Tek veri girişi kullanıcının yazdığı prompt ise NA işaretlenir, HYG-PRM değerlendirilir.

| Puan | Ölçüt |
|---|---|
| 0 | Sistem için yazılı bir kişisel veri kategori listesi yok. |
| 1 | Liste var ama şunlardan en az biri geçerli: kapsamdaki her veri kaynağını kapsamıyor; özel nitelikli verileri içermiyor; veriyle ilgili yerel tanımlayıcıları (ör. TCKN, IBAN) içermiyor; kategori başına muamele tanımlı değil; adı belli bir sahip tarafından onaylanmamış. |
| 2 | Liste kapsamdaki her veri kaynağını kapsıyor, özel nitelikli verileri ve ilgili yerel tanımlayıcıları içeriyor, kategori başına muamele tanımlıyor ve adı belli bir sahip tarafından onaylanmış. |
| 3 | 2'yi karşılıyor ve liste 12 ay içinde ya da son veri kaynağı eklendikten sonra (hangisi önce gelirse) gözden geçirilmiş; tarihli gözden geçirme kaydı var. |

*AS-02'de istenecek kanıt:* `DOC` Veri kaynağı başına kategori listesi (ör. TCKN, IBAN, kart numarası, telefon, adres, sağlık verisi); `DOC` Muamele tablosu: kategori -> engelle / maskele / takma adlandır / izin ver; 'izin ver' için dayanak; `DOC` Sahibini adıyla gösteren onay kaydı

### HYG-ING-02 · Saklamadan önce otomatik tespit ve muamele  `L1`

**Soru:** Yapay zekâ sistemlerine yüklenen veya bağlanan verilerdeki kişisel veriler (TCKN, IBAN, sağlık verisi vb.) otomatik olarak maskeleniyor mu?

**Derinleştirme:** Kişisel veriler hangi giriş noktalarında otomatik olarak tespit edilip maskeleniyor? Bu işlem veri saklanmadan ya da indekslenmeden önce mi yapılıyor?

**Uygulanabilirlik:** HYG-ING-01 ile aynı.

| Puan | Ölçüt |
|---|---|
| 0 | Hiçbir giriş yolunda otomatik tespit yok. |
| 1 | Şunlardan en az biri geçerli: kontrol yolların yalnız bir kısmında; tespit edip kaydediyor ama muameleyi uygulamıyor; veri saklandıktan ya da indekslendikten sonra çalışıyor; muamele elle yapılıyor; kayıt kanıtı sunulamıyor. |
| 2 | Envanterdeki her yolda kontrol saklama/indeksleme öncesinde var, HYG-ING-01'deki muamele uygulanıyor ve son 30 günde veri alan her yol için o döneme ait kayıt var. |
| 3 | 2'yi karşılıyor; değişiklik yönetiminde hiçbir yeni giriş yolunun kontrol olmadan canlıya alınmadığını güvenceye alan bir kontrol adımı var; yol envanteri 6 ay içinde çalışan sistemle karşılaştırılmış, tarihli kaydı var. |

*AS-02'de istenecek kanıt:* `DOC` Veri giriş yolları envanteri (mimari ya da veri akış şeması); `CFG` Kontrolün her yoldaki varlığını ve saklama/indeksleme öncesindeki yerini gösteren yapılandırma; `LOG` Son 30 güne ait, her yoldan tespit/muamele kayıtları

### IDE-STO-01 · AI verisine ve artefaktlarına rol bazlı erişim  `L1`

**Soru:** AI sistemlerinizin belgelerine ve kayıtlarına erişim, rol bazında ve adı belli kişilerle sınırlı mı?

**Derinleştirme:** Bu AI sisteminin belgelerini, indekslerini, model dosyalarını ve kayıtlarını kim okuyabilir ya da değiştirebilir, buna nasıl karar veriliyor?

**Uygulanabilirlik:** Her zaman uygulanır. Sağlayıcının işlettiği depolarda kurum tarafındaki erişim (yönetim konsolları, çalışma alanı rolleri) değerlendirilir.

| Puan | Ölçüt |
|---|---|
| 0 | Bir ya da daha fazla AI deposu anonim erişime izin veriyor ya da varsayılan olarak tüm çalışanlara açık. |
| 1 | Şunlardan en az biri geçerli: paylaşımlı ya da genel hesapların erişimi var; yetkiler rol tanımlarıyla örtüşmüyor; prompt ve yanıt kayıtları için rol tanımlı değil; hiç erişim gözden geçirmesi yapılmamış. |
| 2 | Prompt ve yanıt kayıtları dahil her depo için roller tanımlı, erişim yalnız adı belli kimliklerde, yetkiler rol tanımlarıyla örtüşüyor ve son 12 ayda erişim gözden geçirmesi yapılmış. |
| 3 | 2'yi karşılıyor; erişim gözden geçirmeleri 6 ay içinde yapılıyor ve ayrılan çalışanların erişiminin 2 iş günü içinde kaldırıldığı kayıtlarla gösteriliyor. |

*AS-02'de istenecek kanıt:* `DOC` Her depo için rol tanımları ve rol başına kimlik listesi; `CFG` Her depo için erişim kontrol yapılandırması (ya da yetki dökümü); `DOC` Tarih, gözden geçiren ve kaldırılan erişimleri içeren erişim gözden geçirme kaydı

### TRA-ING-01 · Kurcalamaya dayanıklı kaynak kaydı  `L1`

**Soru:** AI sistemlerinizdeki her belgenin nereden ve ne zaman geldiğini, değiştirilemeyen bir kayıttan gösterebilir misiniz?

**Derinleştirme:** AI sistemindeki herhangi bir belge için nereden, ne zaman geldiğini ve ona ne yapıldığını gösterebilir misiniz; bu kaydı kim değiştirebilir?

**Uygulanabilirlik:** HYG-ING-01 ile aynı.

| Puan | Ölçüt |
|---|---|
| 0 | Veri girişi kaydedilmiyor. |
| 1 | Veri girişi kaydediliyor ama şunlardan en az biri geçerli: dört alandan biri eksik; bazı yollar kaydedilmiyor; sistem yöneticileri girdileri fark edilmeden değiştirip silebiliyor; örnek bir öğe izlenemiyor. |
| 2 | Her yol dört alanı kaydediyor, kayıt deposu listelenen mekanizmalardan en az biriyle korunuyor ve üç örnek öğenin üçü de girdilerine kadar izleniyor. |
| 3 | 2'yi karşılıyor; kayıt bütünlüğü 3 ay içinde doğrulanıyor (ör. özet kontrolü ya da boşluk tespiti) ve kaydı var; kayıt saklama süresi tanımlı süreyle örtüşüyor. |

*AS-02'de istenecek kanıt:* `CFG` Her giriş yolunda dört alanı (kaynak, zaman, kategoriler, muamele) içeren kayıt yapılandırması; `CFG` Kayıt deposu koruması (yalnız ekleme ya da tek yazım ayarı, sistem yöneticilerinden ayrı yetki ya da bütünlük doğrulaması); `TST` Saklanan üç örnek öğenin kayıt girdilerine kadar izlenmesi

### HYG-PRM-01 · Prompt'taki kişisel verinin modele ulaşmadan işlenmesi  `L2`

**Soru:** AI araçlarına yazılan ya da yapıştırılan kişisel veriler modele ulaşmadan otomatik olarak maskeleniyor mu?

**Derinleştirme:** Bir kullanıcı prompt'a müşterinin TCKN'sini ya da sağlık verisini yapıştırırsa, bu veri modele ulaşmadan ne oluyor?

**Uygulanabilirlik:** Prompt arayüzü olan her sisteme uygulanır.

| Puan | Ölçüt |
|---|---|
| 0 | Prompt içeriği kişisel veri için otomatik kontrol olmadan modele ulaşıyor. |
| 1 | Şunlardan en az biri geçerli: kanalların yalnız bir kısmı kapsanıyor; ekler kontrol edilmiyor; kontrol tespit edip uyarıyor ama muameleyi uygulamıyor; kullanıcı kayıtlı gerekçe olmadan atlatabiliyor; kayıt kanıtı yok. |
| 2 | Ekler dahil her prompt kanalı model çağrısından önce tanımlı muameleyi uyguluyor; kullanıcının her atlatması kayıtlı gerekçe gerektiriyor; o dönemde kullanılan her kanal için son 30 güne ait kayıt var. |
| 3 | 2'yi karşılıyor; atlatmalar ve tespitler 3 ay içinde gözden geçiriliyor, aksiyonlar kayıtlı. |

*AS-02'de istenecek kanıt:* `DOC` Prompt'lar için kategori ve muamele listesi (HYG-ING-01 kullanılabilir; serbest metin ve ekleri kapsamalı); `CFG` Kontrolün her prompt kanalında (arayüz, API, eklentiler) model çağrısından önce bulunduğunu gösteren yapılandırma; `LOG` Kanal başına son 30 güne ait tespit/muamele kayıtları

