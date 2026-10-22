# Ölçüm Aracı — Şema (Aşama 0)

*Lecta Sovereign AI Control Framework · `framework v1.0-draft` · durum: **ONAYLANDI (ana kararlar, Gökhan 14 Ekim)** · 14 Ekim 2026*

`[KARAR]` işaretli satırlar hâlâ açık olan küçük kararlardır. Onaylananlar `✅` ile işaretli.

---

## 1. İki ayrı veri: madde kataloğu ve değerlendirme kaydı

| | Madde kataloğu (kaynak) | Değerlendirme kaydı |
|---|---|---|
| Ne | Framework'ün kendisi: maddeler, rubric, eşleme | Bir müşteride yapılan ölçüm: puan, kanıt, değerlendirici |
| Kim yazar | Gökhan (yöntem sahibi) | Değerlendirici + ikinci değerlendirici |
| Sürüm | `framework v1.x` | Değerlendirme ID'si + hangi framework sürümüyle yapıldığı |
| Yer | `measurement-tool/source/` | Müşteri klasörü (bu repoda değil) |

Bu ayrım sayesinde Quick Scan → Detailed Scan → SU-01 tekrarları aynı madde ID'leri üzerinden karşılaştırılır.

## 2. Dosya formatı ✅

**YAML master, CSV/XLSX üretilen çıktı** (Gökhan, 14 Ekim). Gerekçe: rubric dört çok satırlı metin, eşlemeler ve kanıtlar liste; CSV'de bunlar kaçış karakterleri ve hücre içi satır sonlarıyla okunmaz hâle gelir. YAML git diff'te satır satır okunur, yorum alır, ileride JSON Schema ile doğrulanır.

```
measurement-tool/
  schema.md              ← bu belge
  source/
    meta.yaml            ← sürüm, değişiklik kaydı, seviye ve profil tanımları, kod tabloları
    G.yaml               ← G bloğu
    CON.yaml HYG.yaml IDE.yaml BEH.yaml TRA.yaml ATT.yaml   ← katman başına bir dosya
  output/                 ← üretilen tablo, kanıt talep listesi (Aşama 5)
```

## 3. ID kuralı

- **Matris:** `{KATMAN}-{AŞAMA}-{NN}` → `HYG-ING-02`
  - Katman: `CON` containment · `HYG` hygiene · `IDE` identity · `BEH` behaviour · `TRA` traceability · `ATT` attestation
  - Aşama: `ING` ingestion · `STO` storage · `PRM` prompt · `INF` inference · `RES` response · `DWN` downstream
- **G bloğu:** `G-{ALAN}-{NN}` → `G-SUP-02` ✅ (alan kodu, araya madde eklendiğinde numaraların kaymasını önler)
  - Alan: `POL` politika · `INV` envanter · `ROL` roller · `RSK` risk ve etki · `SUP` tedarikçi · `LIT` eğitim/okuryazarlık · `INC` olay · `OVS` insan gözetimi
- **Doğrulama testi:** `VT-{madde ID}-{harf}` → `VT-HYG-ING-03-a`
- **Kurallar:** ID bir kez verilir, **asla yeniden kullanılmaz ve yeniden numaralanmaz.** Kaldırılan madde `status: deprecated` + `replaced_by` ile kalır. Birleşen maddeler yeni ID alır, eskiler `replaced_by` gösterir.

## 4. Madde alanları

| Alan | Zorunlu | Açıklama |
|---|---|---|
| `id` | ✓ | Bölüm 3 |
| `block` | ✓ | `matrix` / `governance` |
| `layer`, `stage` | matris | Kod tablosundan |
| `domain` | G | Kod tablosundan |
| `title` | ✓ | Kısa ad `{en, tr}` |
| `objective` | ✓ | Kontrol hedefi, teknolojiden bağımsız, tek gereksinim `{en, tr}` |
| `question` | ✓ | Değerlendirme sorusu `{en, tr}` |
| `level` | ✓ | Profil başına: `{CE: L1, SOV: L1}`; `null` = o profilde uygulanmaz |
| `applicability` | ✓ | Maddenin hangi durumda N/A olduğu, ölçütüyle `{en, tr}` |
| `evidence` | ✓ | Beklenen kanıtlar; her biri bir tür kodu (aşağıda) + `{en, tr}` açıklama |
| `checks` | ✓ | Kontrol listesi; puan kuralla hesaplanır, rubric metni bundan üretilir (Bölüm 5.5) |
| `review_interval` | 3 puanı için | Ay cinsinden; rubric 3'teki "düzenli" kelimesinin sayısal karşılığı |
| `quick_scan` | ✓ | `true/false` + varsa beyana dayalı kısa soru `qs_question {en, tr}` |
| `validation_tests` | — | AS-03 senaryoları: ön koşul · adımlar · beklenen sonuç `{en, tr}` · ilgili rubric puanı |
| `mappings` | ✓ | Madde/fıkra düzeyinde: `{framework, ref}` listesi; emin olunmayan `[CHECK]` |
| `services` | ✓ | Maddeyi kullanan servisler: `AS-01`, `AS-02`, `AS-03`, … |
| `legacy` | matris | v0 hücre fonksiyon adı (izlenebilirlik) |
| `status`, `since` | ✓ | `draft` / `approved` / `deprecated` · ilk girdiği framework sürümü |
| `notes` | — | İç not: gerekçe, sınır durumlar, tool reference'a işaret (araç adı yalnız burada). Tek dil yeterli |

**Kanıt türleri:** `DOC` belge/politika/kayıt · `CFG` yapılandırma · `LOG` kayıt örneği · `TST` test sonucu · `INT` görüşme beyanı · `OBS` canlı gözlem/ekran paylaşımı. `INT` tek başına 2 puan için yeterli değildir.

## 5. Puanlama

### 5.1 Rubric iskeleti ✅

| Puan | Genel ölçüt | Örnek kanıt eşiği |
|---|---|---|
| **0** | Yok, ya da varlığına dair kanıt yok | — |
| **1** | Tanımlı ama kapsamın tamamında uygulanmıyor; **ya da** uygulanıyor ama kanıtlanamıyor | DOC var, CFG/LOG yok; ya da kapsamın bir kısmı |
| **2** | Kapsamın tamamında uygulanıyor **ve** kanıtlı | CFG + LOG/TST, kapsamdaki tüm yollar |
| **3** | 2 + `review_interval` içinde gözden geçirilmiş/ölçülmüş ve kaydı var | 2 + tarihli gözden geçirme ya da ölçüm kaydı |

Her maddenin rubric'i bu iskeleti **maddeye özgü, sayılabilir ölçütlerle** doldurur. Yasak kelimeler: *yeterli, uygun, makul, etkin, gerektiği gibi, düzenli* (sayısı verilmeden).

**Ek işaretler (puan değil):** `NA` uygulanmaz (`applicability` ölçütüne dayanarak, gerekçesi yazılır) · `NE` değerlendirilemedi (erişim/kanıt verilmedi). **NE geçiş kapısını kapatır**, NA kapatmaz.

### 5.2 Kanıt durumu

Her puanın yanında `basis: declared | verified`. AS-01'de tüm puanlar `declared` (gösterge seviye); AS-02'de `verified` zorunlu. Quick Scan puanı Detailed Scan'e taşınır ama `verified` olana kadar seviye hesabına girmez. Quick Scan'in kendi **gösterge seviyesi** yalnız kesitteki maddelerle, aynı kapı kuralıyla hesaplanır ve L1'in üstüne çıkmaz (`03-quick-scan-kesiti.md`) ✅ (Gökhan, 14 Ekim).

### 5.3 Geçiş kapısı

Bir sistem, bir profil için **Lk** seviyesindedir ⇔ `level ≤ Lk` olan **tüm uygulanabilir** maddeler ≥ 2 ve hiçbiri `NE` değil. Kümülatiftir: L3 için L0–L3 maddelerinin hepsi geçmeli.

- Ağırlıklandırma yok. Ortalama hesaplanmaz.
- Raporda ayrıca katman × aşama ısı haritası ve **"seviyeyi bloklayan maddeler"** listesi verilir — yol haritası buradan çıkar.
- **G bloğu ile ilişki** ✅: G bloğu kurum için ayrı bir seviye üretir ve **sistem seviyesini sınırlar**: sistem Lk'yı ancak G bloğunda da Lk'ya kadarki maddeler geçmişse raporlar (ör. insan gözetimi prosedürü olmayan kurumda sistem L3 olamaz). Raporda sistemin "matris seviyesi" ve "raporlanan seviye" (G ile sınırlanmış) ayrı gösterilir; fark yol haritasında G eksikleri olarak listelenir.

### 5.5 Kontrol listesi ve sabit puanlama kuralı (A2, pilot)

Amaç: iki değerlendirici aynı maddeye aynı puanı versin. Rubric metni elle yazılmaz; madde `checks` alanında **atomik kontroller** taşır, puan bu kontrollerin cevabından kuralla hesaplanır. Pilot G-POL-02 ve HYG-ING-02 ile onaylandı ✅ (Gökhan, 22 Ekim). 29 maddenin hepsi bu biçimde (182 kontrol, 48 terim). Yeni madde de `checks` ile yazılır; elle yazılmış `rubric` alanı yalnız geriye dönük uyumluluk için araçlarda okunur.

**Kontrol türü (`kind`):**

| Tür | Kod | Anlamı |
|---|---|---|
| varlık | `exist` | Maddenin konusu var mı? Her maddede tek, `c1` |
| temel | `core` | 2 puan için hepsi gerekli. `c2`, `c3`, … |
| sürdürme | `sustain` | 3 puan için 2'ye ek olarak hepsi gerekli. `s1`, `s2`, … |

**Ölçüm tipi (`type`) ve eşik (`threshold`):**

| Tip | AS-02 cevabı | Eşik | Örnek |
|---|---|---|---|
| `binary` | E / H | — | Kurallar veri sınıflarına atıf yapıyor |
| `ratio` | a/b | `min` (0–1), isteğe bağlı `sample` | Envanterdeki yolların %100'ünde kontrol var |
| `date` | YYYY-MM-DD | `max_months` (sayı ya da `review_interval`) / `max_days` | Liste son 12 ay içinde güncellenmiş |
| `count` | tam sayı | `min` | — |

Quick Scan'de her kontrol E / H / B (bilmiyor) ile cevaplanır; eşik sağlanıyorsa E. **B ve boş cevap karşılanmıyor sayılır.**

**Puanlama kuralı (sabit, maddeye göre değişmez):**

| Puan | Kural |
|---|---|
| 0 | `c1` karşılanmıyor |
| 1 | `c1` karşılanıyor, temel kontrollerden en az biri karşılanmıyor |
| 2 | `c1` ve tüm temel kontroller karşılanıyor |
| 3 | 2 + tüm sürdürme kontrolleri karşılanıyor (sürdürme kontrolü yoksa 3 verilmez) |

`c1` = B ise madde **NE**, `c1` = NA ise madde **NA** (gerekçe `na_reason`). Kural `tools/kontrol.py` içinde tek yerde yazılıdır; rehber, tablo ve rubric metni oradan üretilir.

**Kontrol alanları:** `id` · `kind` · `type` · `threshold` · `text {en, tr}` (doğru/yanlış denebilecek tek ifade) · `evidence` (kanıt türü kodu) · `qs` (Quick Scan'de sorulur mu; `false` olanlar QS puanında hesap dışı, AS-02'de bakılır) · `terms` (sözlük atfı) · `sampling` (örneklem kuralı uygulanır mı).

**Terimler:** Kontrol metninde geçen ve yoruma açık her terim `source/terms.yaml` içinde tanımlanır. Tanım, bir şeyin terime girip girmediğine evet/hayır ile karar verdirmelidir.

**Örneklem (AS-02, `sampling: true` kontroller):** Paydada 10 ya da daha az öğe varsa hepsine bakılır. 10'dan fazlaysa en az 5 öğe seçilir; seçim gerekçesi ve seçilen öğeler değerlendirme kaydına yazılır. Örneklemdeki tek bir başarısızlık oranı %100'ün altına düşürür. `[KALİBRASYON: pilot]`

**Eşikler:** Mevcut eşikler (%100, 12 ay, 30 gün, `review_interval`) korunur, pilotta kalibre edilir ✅ (Gökhan, 22 Ekim).

### 5.4 İkinci değerlendirici

Değerlendirme kaydında her madde için `assessor`, `reviewer`, `evidence_refs`. Reviewer ≥ 2 verilen her puanın gerekçesini okur ve bunların rastgele seçilmiş %20'sinin kanıtını yeniden açar `[KARAR: oran]`; uyuşmazlık kaydı tutulur (Aşama 6 kalibrasyonunun girdisi).

## 6. Dil ✅

**Her metin alanı çift dilli `{en, tr}`** (Gökhan, 14 Ekim): `title`, `objective`, `question`, `qs_question`, `applicability`, `evidence`, `rubric`, `validation_tests`. Kod ve ID'ler İngilizce; `notes` iç not, tek dil yeterli. İki dil eşdeğerdir; anlam farkı çıkarsa İngilizce metin esas alınır ve TR düzeltilir `[KARAR]`. Bakım kuralı: bir alanın bir dili değişirse diğeri aynı commit'te güncellenir.

## 7. Henüz kapsam dışı

Profil geçiş kapılarının nihai tablosu (Aşama 4) · üretim betiği (Aşama 5) · JSON Schema doğrulaması (Aşama 5).
