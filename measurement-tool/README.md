# Ölçüm Aracı — Durum ve Kullanım Rehberi

*Lecta Sovereign AI Control Framework · `framework v1.0-draft` · 14 Ekim 2026*

AI Quick Scan (AS-01) bugün yürütülebilir durumda. Ölçüm aracının şeması, 29 onaylı madde, Quick Scan kesiti, memo şablonu ve 13 belgelik şablon kütüphanesi hazır. Wave A'yı açmak için yalnız yasal atıfların son doğrulaması kaldı.

## Durum

| Aşama | İçerik | Durum |
| --- | --- | --- |
| 0 · Şema | Madde alanları, ID kuralı, puanlama ve geçiş kapısı, YAML kaynak | Tamam |
| 1 · G bloğu | 15 yönetişim maddesi, tam rubric'le | Tamam |
| 2 · Quick Scan kesiti | 17 madde/profil, görüşme rehberi, puanlama tablosu, seviye hesabı, memo şablonu | Tamam |
| Şablon kütüphanesi | 13 belge şablonu (md + Word) — [`templates/`](../templates/README.md) | Tamam, ilk sürüm |
| 3 · Matris maddeleri | 36 hücrenin kalanı | Sırada |
| 4 · Profil kapıları | Controlled External / Sovereign kapı tablosu | Sırada |
| 5 · Çıktı üretimi | AS-02 puanlama tablosu ve kanıt talep listesi | Sırada |
| 6 · Pilot | Dost bir kurumda ya da Lecta'da deneme, rubric kalibrasyonu | Sırada |

**Temel tasarım:**

- **Tek kaynak:** Maddeler YAML'da; tablo, rehber ve Word çıktıları ondan üretilir.
- **Dil:** Her metin alanı iki dilli (EN/TR).
- **ID'ler:** Matris `KATMAN-AŞAMA-NN` (ör. `HYG-ING-02`), yönetişim `G-ALAN-NN` (ör. `G-SUP-01`). Bir ID asla yeniden kullanılmaz.
- **Puan ve seviye:** Puan 0–3. Ağırlık ve ortalama yok; seviye geçiş kapısıyla belirlenir.
- **G bloğu sistem seviyesini sınırlar:** Kurumda yönetişim eksikse sistem daha yüksek seviye raporlayamaz.
- **Quick Scan:** Gösterge seviye yalnız kesitle hesaplanır ve L1'in üstüne çıkmaz. Bir taramada en çok 2 sistem.

## Ölçüm kapsamı: bugün ve hedef

Bugünkü 29 madde, Quick Scan'de L1'e kadar gösterge seviye verir. Kanıta dayalı değerlendirmede (AS-02) durum şöyle:

- **Matris:** L0 eksiksiz ölçülür. L1 için dört madde grubu eksik.
- **G bloğu:** L3'e kadar hazır.
- **Tam araç:** Yaklaşık 120 madde olacak ve L0–L6'nın tamamını ölçecek.

| Seviye | G (bugün) | Matris (bugün) | Matris (hedef, tahmini) | Bugün ölçülebilir mi |
| --- | --- | --- | --- | --- |
| L0 Altyapı temeli | 1 | 4 | ~5 | Evet |
| L1 Gizlilik temeli | 7 | 9 | ~18 | Quick Scan'de evet (gösterge). AS-02 için CON-PRM, HYG-STO, TRA-STO ve secret yönetimi maddeleri gerekli |
| L2 Erişim ve denetim izi | 4 | 0 | ~25 | Hayır; matris maddeleri Aşama 3'te |
| L3 Davranış kontrolleri | 3 | 1 | ~22 | Hayır |
| L4 Uyum operasyonu | 0 | 0 | ~15 | Hayır |
| L5 Sektör ve coğrafya uyumu | 0 | 0 | ~12 | Hayır (kanıt artefaktları) |
| L6 Belgelendirmeye hazırlık | 0 | 0 | ~5 | Hayır (kanıt paketi) |
| **Toplam** | **15** | **14** | **~100–105** | |

Tahmin, 36 hücre × ortalama 2–3 madde ile seviye metinlerinde olup hücresi olmayan kontrollerden (şifreleme, zafiyet yönetimi, veri yerleşimi vb.) hesaplandı. G bloğuna 3–5 madde eklenmesi bekleniyor (değişiklik yönetimi, kullanıcı bilgilendirme gibi). Böylece tam araç **yaklaşık 120 madde** olur. Bazı maddeler yalnız bir profile uygulandığı için bir değerlendirmede uygulanabilir madde sayısı bundan biraz azdır.

Araç hangi seviyede olursa olsun **hazırlığı** ölçer, denetim yapmaz. L6, belgelendirmeye hazır kanıt paketinin varlığını ölçer; belgelendirmeyi akredite bağımsız kuruluş yapar.

## Ölçüm aracı nasıl çalışır

Ölçüm aracı kendi kendine çalışan bir yazılım değil. Değerlendiricinin uyguladığı bir yöntem ve bu yöntemi taşıyan dosyalardan oluşur.

- **Puanı her zaman insan verir.** Değerlendirici bir Lecta danışmanıdır; denetçi değildir.
- **Betikler hesap yapar, karar vermez.** Soruları ve tabloları üretir, girilen puanlardan seviyeyi hesaplar ve riskleri sıralar.
- **Müşteri sistemlerine bağlanmaz.** Kendiliğinden veri toplamaz.

### Süreç: kim, hangi dosyayı doldurur

| # | Kim | Ne yapar | Dosya |
| --- | --- | --- | --- |
| 1 | Lecta yöntem ekibi | Maddeleri ve rubric'leri yazar, onaylar, sürüm verir. Bu, her müşteride değil, framework güncellendiğinde yapılır | `source/*.yaml` |
| 2 | Betik | Kapsama göre görüşme rehberini, boş puanlama tablosunu ve (AS-02'de) kanıt talep listesini üretir | `output/` |
| 3 | Değerlendirici | Görüşmeyi yapar. AS-02'de belgeleri, yapılandırma ve kayıt örneklerini inceler | görüşme rehberi |
| 4 | Değerlendirici | Her maddeye puan (0–3) ya da NA/NE girer; gerekçe, not ve kanıt referansı yazar | **puanlama tablosu** |
| 5 | İkinci değerlendirici | Puanların gerekçesini okur, kanıtların bir örneklemini yeniden açar, uyuşmazlıkları kaydeder | aynı tablo, `reviewer` sütunu |
| 6 | Betik | Geçiş kapısı ve G sınırıyla seviyeleri hesaplar, riskleri sabit kurala göre sıralar | seviye çıktısı |
| 7 | Değerlendirici | Memo ya da raporu ve yol haritasını yazar | memo / rapor şablonu |
| 8 | Müşteri | AS-02'de istenen kanıtları sağlar. Eksikleri kapatırken şablon kütüphanesini kullanır | şablonlar |

**Elle doldurulan dosyalar:**

- **Yöntem olarak:** YAML maddeleri ve şablonlar, framework güncellendikçe.
- **Her müşteri işinde:** Puanlama tablosu ile memo ya da rapor.

Bunların dışındaki her şey betikle üretilir. Değerlendirme kayıtları müşteri klasöründe tutulur, bu repoya girmez.

**Bugün çalışan:**

- **Quick Scan (AS-01):** Adımların hepsi hazır; puanlama tablosu CSV.
- **Detailed Scan (AS-02):** Aynı akışı izler. Excel puanlama tablosu, kanıt talep listesi ve rapor şablonu Aşama 5'te üretilecek.

### Yapı

**İki blok:**

- **G bloğu (yönetişim):** Kurum başına bir kez ölçülür: politika, envanter, roller, risk, tedarikçi, eğitim, olay, insan gözetimi.
- **Sistem matrisi:** Her AI sistemi için ayrı ölçülür. 6 pipeline aşaması × 6 kontrol katmanı = 36 hücre; her hücre 2–4 maddeye bölünür.

**İki profil:** Her madde iki profil için ayrı seviye taşır. Bir profile uymayan madde o profilde uygulanmaz.

- **CE — Controlled External:** Dış model ve servislerin yönetilen kullanımı.
- **SOV — Sovereign:** İşleme kurumun yönettiği sınırlar içinde.

**Puan:**

| Puan | Genel ölçüt |
| --- | --- |
| 0 | Yok ya da varlığına dair kanıt yok |
| 1 | Tanımlı ama kapsamın tamamında uygulanmıyor ya da kanıtlanamıyor |
| 2 | Kapsamın tamamında uygulanıyor ve kanıtlı |
| 3 | 2 + madde başına tanımlı aralıkla (ay) gözden geçiriliyor ya da ölçülüyor |

Her maddenin rubric'i bu iskeleti sayılabilir ölçütlerle doldurur. "Yeterli", "uygun", "düzenli" gibi ölçütsüz kelimeler kullanılmaz. Puan dışı iki işaret var:

- **NA:** Madde uygulanmaz; hesaba girmez.
- **NE:** Değerlendirilemedi; kapıyı kapatır.

**Seviye:** Bir sistem Lk seviyesindedir ⇔ seviyesi Lk ve altı olan tüm uygulanabilir maddeler en az 2 puan almıştır. Raporlanan seviye, sistemin matris seviyesi ile G bloğu seviyesinin düşük olanıdır. Örnek: teknik olarak L1 olan bir RAG sistemi, kurumun AI envanteri eksikse L0 olarak raporlanır.

**Kanıt dayanağı:**

- **Quick Scan:** Puanlar beyana dayanır (`declared`); sonuç gösterge seviyedir.
- **Detailed Scan:** Puanlar kanıtla doğrulanır (`verified`).

İki tarama aynı ID'leri kullandığı için Quick Scan sonucu Detailed Scan'e kayıpsız taşınır.

Tüm maddeler ve rubric'ler: [`output/madde-rubric-tablosu.md`](output/madde-rubric-tablosu.md) · kanıt, eşleme ve doğrulama senaryolarıyla: [`output/inceleme-paketi.xlsx`](output/inceleme-paketi.xlsx).

## Quick Scan nasıl yürütülür

Bir Quick Scan yaklaşık 2–3 adam-gün sürer. İçinde tek bir görüşme var: 1 sistemle ~85 dakika, 2 sistemle ~120 dakika. Çıktısı 4–6 sayfalık bir memo ve 30 dakikalık bir sunum.

1. **Kapsam:** Kurum adı ve en çok 2 sistem belirlenir. Her sistemin profili (CE/SOV) bu aşamada seçilir.
2. **Puanlama tablosu üretilir:** `python3 qs.py puanlama --kurum "Kurum" --sistem "Asistan:CE" --out kurum-qs.csv`
3. **Görüşme:** Profile göre `output/qs-gorusme-rehberi-CE.md` ya da `-SOV.md` rehberi kullanılır. Açılış metni okunur: "beyana dayalı, denetim değil". Katılımcılar BT/güvenlik sorumlusu ve bir iş birimi sahibidir.
4. **Puanlar CSV'ye girilir:** Her maddeye 0–3, NA ya da NE yazılır. Kanıt istenmez; katılımcı kendiliğinden gösterirse `evidence_ref` alanına not edilir.
5. **İkinci değerlendirici** CSV'yi kontrol eder ve `reviewer` sütununu doldurur.
6. **Seviye hesaplanır:** `python3 qs.py seviye kurum-qs.csv --out kurum-seviye.md`. Çıktıda sistem başına gösterge seviye ve en kritik 5 risk yer alır.
7. **Memo yazılır:** [`04-quick-scan-memo-sablonu.md`](04-quick-scan-memo-sablonu.md) kullanılır. Seviye tablosu ve risk sırası betikten gelir; değerlendirici bunları değiştirmez. Önerilen sonraki adım karar tablosundan seçilir.

**Kesit — 17 madde/profil:**

- **9 kurum maddesi:** G-POL-01, G-POL-02, G-INV-01, G-INV-02, G-ROL-01, G-RSK-01, G-SUP-01, G-LIT-01, G-INC-01.
- **8 sistem maddesi:** CON-ING-01, CON-STO-02, CON-INF-01 (SOV) ya da CON-INF-02 (CE), IDE-STO-01, HYG-ING-01, HYG-ING-02, HYG-PRM-01, TRA-ING-01.

**Risk sıralaması sabit kurala bağlı:**

1. Düşük puan önce gelir; NE, 0 sayılır.
2. Düşük seviye önce gelir.
3. CE sistemlerde dış veri çıkış zinciri önce gelir: G-POL-02, G-INV-02, G-SUP-01, CON-INF-02, HYG-PRM-01.
4. Kurum maddesi sistem maddesinden önce gelir.
5. Eşitlikte ID sırası geçerlidir.

Böylece iki değerlendirici aynı CSV'den aynı memo'yu çıkarır.

**Sonraki adım karar tablosu** (ilk eşleşen satır seçilir):

| Koşul | Öneri |
| --- | --- |
| G bloğu L0 ya da altı | DS-03 Governance Policy Set (+ EN-02) |
| CE zincirinde 0 ya da NE | AS-04 Shadow AI Discovery → DS-01 |
| Sistem matrisi L0 ya da altı | AS-02 Detailed Scan |
| Gösterge L1 | AS-02 Detailed Scan (doğrulama ve L2+ yolu) |
| Kişisel veri + G-RSK-01 < 2 | AS-07 (ek öneri) |
| Yönetim farkındalığı talebi | EN-01 (ek öneri) |

## Neden YAML ve kaynaktan üretim

Maddeler tek bir YAML kaynağında tutuluyor. Değerlendiriciye ve müşteriye giden her şey bu kaynaktan betikle üretiliyor: görüşme rehberi, puanlama tablosu, inceleme tablosu, rubric tablosu, Word şablonları. Amaç, aynı maddenin farklı belgelerde farklı sürümlerinin oluşmasını engellemek.

| Avantaj | Ne sağlar |
| --- | --- |
| **Tek doğru kaynak** | Bir rubric değişince rehber, tablo ve rapor aynı anda güncellenir. Kopyalar arasında fark oluşmaz |
| **Karşılaştırılabilir sonuçlar** | Sabit ID'ler ve her değerlendirmeye yazılan framework sürümü sayesinde Quick Scan, Detailed Scan ve SU-01 tekrarları aynı maddeler üzerinden kıyaslanır |
| **İzlenebilir değişiklik** | YAML düz metindir. Git ile her değişiklik satır satır görülür: kim, ne zaman, neyi değiştirdi. Yöntemin kendisi denetime hazır tutulur |
| **Yapıyı taşır** | Bir maddede dört çok satırlı rubric metni, kanıt ve eşleme listeleri, iki dil var. Bunlar Excel ya da CSV hücrelerinde bozulur; YAML'da okunur kalır ve yorum alır |
| **Otomatik kontrol** | Betik ölçütsüz kelimeleri, eksik dil alanını, kesit sayısını ve seviye tutarlılığını tarar |
| **Araçtan bağımsız** | Aynı kaynaktan ileride öz değerlendirme formu, web arayüzü ya da veritabanı üretilebilir. Tek bir yazılıma ya da kapalı bir platforma bağımlı kalınmaz |
| **Herkes kendi biçimini görür** | Müşteri Word ve Excel görür, değerlendirici rehber ve tablo görür. YAML yalnız yöntem ekibinin çalıştığı katmandır |

**Bedeli:** YAML'ı elle düzenlemek teknik bir iştir. Bu yüzden okuma ve yorum için bir Excel inceleme tablosu üretiliyor. Düzenlemeler Claude ile de yapılabilir.

## Dosyalar ve komutlar

```
ILK-ADIMLAR.md                  yeni katılan için başlangıç (repo kökü)
measurement-tool/
  README.md                     bu belge
  schema.md                     şema ve kurallar
  source/                       KAYNAK — maddeler burada
    meta.yaml                   sürüm, değişiklik kaydı, seviye/profil tanımları
    G.yaml                      G bloğu (15 madde)
    CON.yaml HYG.yaml IDE.yaml TRA.yaml   matris maddeleri (14)
    _template.yaml              yeni madde için boş şablon
  tools/
    qs.py                       Quick Scan: rehber, puanlama CSV, seviye hesabı
    inceleme.py                 inceleme tablosu (xlsx), kararları okuma, rubric tablosu (md)
  output/                       üretilen dosyalar (elle düzenlenmez)
  01-hucre-analizi.md           v0 çerçevenin 36 hücresinin ölçülebilirlik analizi
  02-g-blogu-basliklar.md       G bloğu özeti
  03-quick-scan-kesiti.md       Quick Scan kesiti ve seviye kuralı
  04-quick-scan-memo-sablonu.md memo şablonu
  katalog-onerileri.md          katalog önerileri (K-1…K-4)
templates/
  README.md                     şablon dizini ve kurallar
  md/                           KAYNAK — 13 şablon
  docx/                         üretilen Word sürümleri
  tools/docx_uret.py          md → docx
archive/
  v0-guardrails/                framework'ün ilk sürümü (HTML + hiyerarşik md), salt okunur
```

**Gereken araçlar:** Python 3 (`pyyaml`, `openpyxl`, `python-docx`) ve `pandoc`. Kurulum: `pip install pyyaml openpyxl python-docx`, `brew install pandoc`.

**Komutlar** (`measurement-tool/tools/` içinden):

| Ne için | Komut |
| --- | --- |
| Görüşme rehberi | `python3 qs.py rehber --profil CE --out ../output/qs-gorusme-rehberi-CE.md` |
| Boş puanlama tablosu | `python3 qs.py puanlama --kurum "Kurum" --sistem "Asistan:CE" --sistem "RAG:SOV" --out kurum-qs.csv` |
| Gösterge seviye + 5 risk | `python3 qs.py seviye kurum-qs.csv --out kurum-seviye.md` |
| Madde inceleme tablosu | `python3 inceleme.py uret --out ../output/inceleme-paketi.xlsx` |
| İncelemedeki kararları okumak | `python3 inceleme.py oku ../output/inceleme-paketi.xlsx` |
| Rubric tablosu (md) | `python3 inceleme.py tablo` |
| Şablonların Word sürümü (`templates/tools/` içinden) | `python3 docx_uret.py` ya da tek şablon: `python3 docx_uret.py TPL-04` |

**Framework nasıl işlenir:**

1. **Yeni madde:** `_template.yaml` kopyalanır ve ilgili katman dosyasına eklenir. Durumu `draft` olur.
2. **Değişiklik:** Bir alanın EN ve TR metni aynı anda güncellenir. Madde metni değişirse ID değişmez. Madde kaldırılırsa `deprecated` + `replaced_by` ile dosyada kalır.
3. **İnceleme:** `inceleme.py uret` ile xlsx üretilir. Okuyan, "Karar" (Onay / Düzelt / Sil / Tartışalım) ve "Yorum" sütunlarını doldurur. Kararlar YAML'a işlenir; onaylananlar `approved` olur.
4. **Kayıt:** Her değişiklikte `meta.yaml` değişiklik kaydına bir satır eklenir. Repoya her değişiklik ayrı bir dal ve Pull Request ile girer.
5. **Bağlantılı dosyalar:** Bir G maddesi değişirse ona bağlı şablon aynı PR'da güncellenir; rehberler, tablolar ve Word dosyaları yeniden üretilir.
6. **Katalog:** Katalog master'ı ayrı yürütülür; bu çalışmada düzenlenmez. Katalogda değişmesi gerekenler `katalog-onerileri.md` dosyasında toplanır.

## Şablon kütüphanesi

13 şablon, G bloğunun 15 maddesinden 13'ünü karşılıyor. Her şablon, bağlı olduğu maddenin 2 puan ölçütünü karşılayacak biçimde yazıldı. Ayrıntı: [`templates/README.md`](../templates/README.md).

| ID | Şablon | G maddesi |
| --- | --- | --- |
| TPL-01 | Yapay Zekâ Politikası | G-POL-01 |
| TPL-02 | AI Araçları Kabul Edilebilir Kullanım Kuralları | G-POL-02 · G-LIT-01 |
| TPL-03 | AI Olay Prosedürü | G-INC-01 |
| TPL-04 | AI Olay Bildirim Formu | G-INC-01 |
| TPL-05 | AI Sistem Envanteri | G-INV-01 · G-ROL-01 |
| TPL-06 | AI Sağlayıcı Değerlendirme Formu | G-SUP-01 |
| TPL-07 | Egemenlik Testi Kaydı | G-SUP-02 |
| TPL-08 | Sağlayıcı Sözleşme Maddeleri Kontrol Listesi | G-SUP-03 |
| TPL-09 | AI Risk Değerlendirmesi | G-RSK-01 |
| TPL-10 | AI Risk Sınıflandırma Kaydı | G-RSK-02 |
| TPL-11 | AI Kişisel Veri Etki Değerlendirmesi | G-RSK-03 |
| TPL-12 | Roller ve Sorumluluklar Matrisi | G-ROL-01 · G-LIT-02 |
| TPL-13 | İnsan Gözetimi Prosedürü | G-OVS-01 |

**Yasal süreler (doğrulandı 14.10.2026):** KVKK ihlal bildirimi 72 saat (Kurul kararı 2019/10) · 7545 md. 7(1)(b): zafiyet ve siber olaylar Siber Güvenlik Başkanlığı'na gecikmeksizin, usul ikincil düzenlemeye bağlı · KVKK md. 9: standart sözleşme 5 iş günü içinde Kurula · EU AI Act: Ek III yüksek risk 2 Aralık 2027, Ek I 2 Ağustos 2028 (Tüzük (AB) 2026/1744). Takip edilecek: 7545 ikincil düzenlemeleri.

## Sırada ne var

Ekim sonuna kadar üç iş var: yasal atıfların doğrulanması, örnek bir Quick Scan memo'su ve Wave A'nın dışarıya anlatımı. Ardından matrisin geri kalanı yazılır ve bir dost kurumda pilot yapılır. Tarihler öneridir; program yoğunluğuna göre daraltılabilir ya da kaydırılabilir.

| # | İş | Kimde | Hedef |
| --- | --- | --- | --- |
| 1 | `[CHECK]` eşlemelerini ve şablonlardaki yasal süreleri doğrulamak | Gökhan + Claude | 23 Ekim |
| 2 | EN-01'de gösterilecek sentetik bir örnek Quick Scan memo'su | Gökhan + Claude | 31 Ekim |
| 3 | Wave A'nın dışarıya anlatımı: "Quick Scan ile başlar, Detailed Scan kapsamı matrisle genişler" | Ayhan + Gökhan | 23 Ekim |
| 4 | Katalog önerilerinin (K-1…K-4) kataloğa işlenmesi | Ayhan | 23 Ekim |
| 5 | Quick Scan fiyatlaması ve Detailed Scan'e mahsup (katalog açık karar 1) | Ayhan + Gökhan | 31 Ekim |
| 6 | Hukuk ortağı: şablonlardaki yasal süreler ve AS-07 tam paketi | Ayhan + Gökhan | 15 Kasım |
| 7 | İkinci değerlendirici düzeni: ilk taramalarda Ayhan ve Gökhan karşılıklı ikinci değerlendirici (öneri); kanıt örneklem oranı (öneri %20) | Ayhan + Gökhan | 15 Kasım |
| 8 | Referans tarama için dost kurum (indirimli Quick Scan → Detailed Scan) | Ayhan + Gökhan | 30 Kasım |
| 9 | Aşama 3a: AS-03 için gereken matris hücreleri ve L1'in eksik maddeleri | Gökhan + Ayhan + Claude | 15 Aralık |
| 10 | Aşama 4: profil geçiş kapıları tablosu | Gökhan + Ayhan + Claude | 15 Aralık |
| 11 | Aşama 3b + 5: kalan matris maddeleri, AS-02 puanlama tablosu, kanıt talep listesi ve rapor şablonu | Gökhan + Ayhan + Claude | 31 Aralık |
| 12 | Aşama 6: pilot ve rubric kalibrasyonu | Ayhan + Gökhan | Şubat 2027 |
