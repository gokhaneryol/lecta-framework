# Quick Scan Memo Şablonu (AS-01)

*Ölçüm aracı · Oturum 4 · 14 Ekim 2026 · hedef uzunluk 4–6 sayfa · `{{…}}` alanları doldurulur, *italik yönergeler* silinir*

**Üretim akışı:** `tools/qs.py puanlama` → görüşme (`output/qs-gorusme-rehberi-{CE|SOV}.md`) → CSV doldurulur → ikinci değerlendirici CSV'yi kontrol eder → `qs.py seviye` → çıktı Bölüm 2–3'e yapıştırılır → Bölüm 4–5 aşağıdaki kurallarla yazılır.

---

# {{Kurum adı}} — Yapay Zekâ Hızlı Tarama (AI Quick Scan)

| | |
|---|---|
| Tarih | {{gg.aa.yyyy}} |
| Kapsam | Kurum (yönetişim) + {{1–2}} AI sistemi: {{Sistem adları ve profilleri}} |
| Yöntem | Lecta Sovereign AI Control Framework {{sürüm}} — Quick Scan kesiti ({{n}} madde), beyana dayalı |
| Görüşülenler | {{Ad, unvan}} · {{Ad, unvan}} |
| Değerlendirici / İkinci değerlendirici | {{Ad}} / {{Ad}} |

> **Bu belge bir hazırlık okumasıdır.** Bulgular görüşmede verilen beyanlara dayanır; kanıt incelemesi yapılmamıştır. Gösterge seviye bir denetim görüşü, uygunluk beyanı ya da sertifika değildir. Lecta denetim yapmaz; kurumları bağımsız denetime hazırlar.

## 1. Yönetici özeti

*En fazla yarım sayfa. Üç paragraf: (1) gösterge seviye tek cümle, (2) en önemli iki bulgu, (3) önerilen sonraki adım. Teknik terim yok.*

{{Kurum}}'un yapay zekâ kullanımı, beyanlara göre **gösterge {{Lx}}** seviyesindedir. {{…}}

## 2. Gösterge seviye

*`qs.py seviye` çıktısındaki tablo ve sabit cümle buraya, değiştirilmeden.*

{{seviye tablosu}}

**Seviyeler:** L0 Altyapı temeli · L1 Gizlilik temeli · L2 Erişim ve denetim izi · L3 Davranış kontrolleri · L4 Uyum operasyonu · L5 Sektör ve coğrafya uyumu · L6 Belgelendirmeye hazırlık. Hızlı Tarama L1'in üstünde seviye üretmez.

*Raporlanan seviye matris seviyesinden düşükse bir cümle ekle: "Sistem teknik olarak {{Lx}} göstergesi verse de kurum düzeyindeki {{G maddeleri}} eksikliği nedeniyle {{Ly}} olarak raporlanmıştır."*

## 3. En kritik 5 risk

*`qs.py seviye` sıralaması **değiştirilmeden** kullanılır (puan ↑ · seviye ↑ · CE zinciri önce · kurum önce · ID); değerlendirici sırayı kendi yargısıyla değiştirmez. Her risk için aşağıdaki kalıp, en fazla 5 satır.*

### 3.{{n}} {{Madde başlığı}} (`{{ID}}`)
- **Beyan:** {{görüşmede ne söylendi — bir cümle}}
- **Neden önemli:** {{risk — verinin nereye gidebileceği / ne olabileceği, bir–iki cümle}}
- **Dayanak:** {{maddenin eşlemesinden 1–2 referans, ör. KVKK md. 12(1)}}
- **Kapanış ölçütü:** {{maddenin rubric 2 ölçütü, sadeleştirilmiş}}

*NE (bilinmiyor) olan madde: "Kurum bu konuda bilgi veremedi; bilinmemesi başlı başına bir bulgudur." kalıbı kullanılır.*

## 4. Önerilen sonraki adım

*Aşağıdaki karar tablosundan **ilk** eşleşen satır seçilir. Ek öneri en fazla bir tane.*

| Koşul (Quick Scan sonucu) | Önerilen adım | Servis |
|---|---|---|
| G bloğu L0 altı ya da L0 (politika/kural/envanter yok) | Yönetişim temelini kurmak: AI politikası, kabul edilebilir kullanım, envanter | DS-03 (+ EN-02) |
| CE zincirinde (G-POL-02, G-INV-02, G-SUP-01, CON-INF-02, HYG-PRM-01) 0 ya da NE var | Dış AI kullanımının görünür kılınması ve veri çıkışının kontrolü | AS-04 → DS-01 |
| Sistem matrisi L0 altı ya da L0 | Kanıta dayalı tam ölçüm ve yol haritası | AS-02 |
| Gösterge L1 (her iki blok) | Gösterge seviyeyi doğrulamak ve L2+ yolunu çizmek | AS-02 |
| Kişisel veri işleyen sistem + G-RSK-01 < 2 | Kullanım senaryosu bazında veri akışı ve etki analizi | AS-07 (ek öneri olarak) |
| Yönetim kurulu / üst yönetim farkındalığı talebi görüşmede dile getirildi | Yönetici bilgilendirmesi | EN-01 (ek öneri olarak) |

*Quick Scan bedelinin Detailed Scan'e mahsubu ticari karardır (katalog açık karar); memo'da fiyat yazılmaz.*

## 5. Kapsam, yöntem ve sınırlamalar

- Kesit: {{n}} madde ({{9}} kurum + sistem başına {{8}}); maddeler, rubric ve kimlikler Detailed Scan ile aynıdır, sonuçlar kayıpsız taşınır.
- Puanlar beyana dayanır (`declared`); hiçbir puan kanıtla doğrulanmamıştır.
- Kesit dışında kalan alanlar (davranış kontrolleri, kanıt/attestation, L2 ve üstü teknik kontroller) değerlendirilmemiştir; bulgu olmaması bu alanlarda risk olmadığı anlamına gelmez.
- Hukuki değerlendirme içermez. Hukuki sonuç gerektiren konular kurumun hukuk danışmanına ya da Lecta'nın hukuk ortağına yönlendirilir.

## Ek A — Madde tablosu

*Doldurulmuş CSV'den: ID · başlık · birim · seviye · puan · not. Puanı 2 ve üstü olanlar dahil tümü.*

| ID | Madde | Birim | Seviye | Puan | Not |
|---|---|---|---|---|---|
| {{…}} | | | | | |

## Ek B — Seviye ve puan tanımları

| Puan | Anlam |
|---|---|
| 0 | Yok ya da var olduğuna dair bilgi yok |
| 1 | Tanımlı ama kapsamın tamamında uygulanmıyor ya da kanıtlanamıyor |
| 2 | Kapsamın tamamında uygulanıyor ve kanıtlanabilir (beyana göre) |
| 3 | 2 + belirli aralıklarla gözden geçiriliyor ya da ölçülüyor |
| NA / NE | Uygulanmaz / bilgi verilemedi (NE seviye hesabında geçmez sayılır) |

---

## Yazım kuralları (memo'ya girmez)

1. **Dil:** "denetim", "uygun/uygunsuz", "sertifika", "compliant" kelimeleri kullanılmaz; "hazırlık", "gösterge", "eksik", "kapanış ölçütü" kullanılır.
2. **Vaat yok:** Önerilen adım yalnız katalogdaki Faz 1 servislerinden seçilir.
3. **Kişi yok:** Bulgular kişiye değil maddeye bağlanır; görüşülen kişilerin beyanları alıntılanmaz.
4. **Sıra sabit:** Risk sırası ve sonraki adım tablodan gelir; değerlendirici değiştirirse gerekçeyi ikinci değerlendirici kaydına yazar.
5. **Uzunluk:** Gövde (Bölüm 1–5) 4 sayfayı geçmez; ekler hariç.
