# Değerlendirme arayüzü — tasarım notu (ADR-001)

*Durum: **KABUL** (Gökhan, 26 Ekim 2026) · ❓ işaretli satırlar teyit bekliyor*
*Bu not ilk PR'da `lecta-framework/measurement-tool/ui/TASARIM.md` olarak repoya girer. Müşteri verisi içermez.*

## 1. Bağlam

Quick Scan bugün CSV doldurularak yürütülüyor (`qs.py puanlama` → elle E/H/B → `qs.py seviye`). Arayüz bu akışın **giriş katmanı**: değerlendirici görüşmede laptopunu açar, notlarını ve kontrol cevaplarını doğrudan buraya girer; ayrı kâğıt, Excel ya da docx kullanmaz. Sonradan geri dönüp tamamlar. Çıktı, bugünkü `qs.py seviye` ve memo akışının değişmeden çalıştığı CSV'dir.

## 2. Kararlar

| # | Konu | Karar |
|---|---|---|
| K1 | Barındırma | **donut üzerinde ayrı bir Docker container.** Uygulama `127.0.0.1`'e bağlanır, önünde Apache reverse proxy ve erişim katmanı. Geliştirme yerelde aynı compose dosyasıyla. Veri diskte şimdilik şifrelenmez (bilinçli kabul, §7) |
| K2 | Kurum verisi | **Her değerlendirme ayrı bir private GitHub reposu** (şablon repodan). Saklama süresi dolunca repo silinir. `lecta-framework` müşteri verisi içermez. Notlara kişi adı değil rol yazılır |
| K3 | Kapsam | Akış **yalnız QS**. Veri modeli AS-02 alanlarını (oran/tarih/sayı cevabı, örneklem, kanıt listesi, `verified`) baştan taşır; ekranları sonra gelir |
| K4 | Skip | "Sonra döneceğim" demek. Kapanışta eksikler listesi gösterilir; onaylanınca dışa aktarmada **B** ve notunda "atlandı" olarak çıkar. QS'de c1 = H olursa kalan kontroller otomatik "atlandı (c1=H)" durumuna geçer ama düzenlenebilir kalır. c1 = NA olursa kalanlar kapanır ve `na_reason` zorunlu olur |
| K5 | Meta veri | İki katman. **Tanımlayıcı alanlar** (ad, logo, sektör, çalışan bandı, AI kullanım alanları) yalnız başlık ve memo içindir; listeler sabittir ve kodlarıyla `source/org_fields.yaml`'da tutulur. **Ön koşul olguları** (27001 vb.) framework'te tanımlanır (`source/facts.yaml`, K7) ve maddeler bunlara atıf yapar. İkinci katman K7 YAML'a girmeden arayüze eklenmez |
| K6 | İkinci değerlendirici | Madde düzeyinde "katılıyorum / katılmıyorum + yorum". Akış sıralı: değerlendirici kaydı incelemeye gönderir, gözden geçiren açar. Uyuşmazlıklar listelenir (Aşama 6 kalibrasyonunun girdisi) |
| K7 | Puan | **A2 olduğu gibi kalır.** Yargıyı değerlendirici verir: her kontrole E/H/B (c1'e NA). Madde puanı, seviye ve risk sırası bir karar değil, **durum tespitidir**; `kontrol.py` ve `qs.py`'nin kodu çağrılarak gösterilir. Puan alanı elle düzenlenmez; port yapılmaz |
| K8 | Ekran birimi | **Madde başına bir ekran.** Kontroller alt alta, terimler yan panelde |
| K9 | Kullanım | Hem canlı (görüşme sırasında) hem sonradan. Her alan değiştiğinde otomatik kaydedilir. Klavye ile hızlı kullanılır |
| K10 | Teknoloji | Python 3.12 · Flask · Jinja · htmx (dosyası repoda, CDN yok) · PyYAML · gunicorn · Docker Compose. Veritabanı yok; YAML dosyaları atomik yazılır (geçici dosya + rename) |
| K11 | Kodun yeri | `lecta-framework/measurement-tool/ui/`. YAML kaynağı ve `kontrol.py` ile aynı commit'te sürümlenir; değişiklikler dal + PR ile yapılır |

## 3. Sabit listeler (`source/org_fields.yaml`) ❓ taslak, onay bekliyor

- **sector:** `gov-central` Kamu (merkezi) · `gov-local` Kamu (yerel) · `banking` Bankacılık · `insurance` Sigorta · `fin-other` Diğer finans (SPK) · `energy` Enerji (EPDK) · `telecom` Telekom (BTK) · `health` Sağlık · `edu-research` Eğitim ve araştırma · `defence` Savunma · `manufacturing` Üretim · `retail` Perakende ve e-ticaret · `transport` Ulaşım ve lojistik · `legal-consulting` Hukuk ve danışmanlık · `it` Bilişim ve yazılım · `other` Diğer
- **employee_band:** `1-49` · `50-249` · `250-999` · `1000-4999` · `5000+`
- **ai_use (çoklu seçim):** `ext-assistant` Harici genel asistan · `int-assistant` Kurumsal asistan · `rag` RAG / belge arama · `code` Kod asistanı · `cs-bot` Müşteri hizmetleri chatbot'u · `doc-processing` Belge işleme ve çıkarım · `decision` Karar destek ve skorlama · `agents` Ajan ve otomasyon · `other` Diğer

Her kod iki dilli etiket taşır (`{en, tr}`). Kod bir kez verilir, yeniden kullanılmaz.

## 4. Veri modeli

### 4.1 Değerlendirme reposu

Kurum kimliği (`kurum-kisa`) elle yazılmaz, kısa addan üretilir: `Örnek Banka` → `ornek-banka`; Türkçe harfler sadeleşir. Aynı kimlik o yıl varsa `-2`, `-3` eklenir (Gökhan, 27 Ekim).

```
<kurum-kisa>-<yyyy>-<servis>/        # ör. ornek-2026-as01 — private GitHub repo
  kurum.yaml
  degerlendirme.yaml
  cevaplar/
    KURUM.yaml                       # G bloğu, kurum başına bir kez
    <sistem-id>.yaml                 # sistem başına bir dosya
  cikti/                             # üretilen, elle düzenlenmez
    qs.csv  seviye.md
  logo.png
```

### 4.2 `kurum.yaml`

```yaml
id: ornek
ad: {tam: "Örnek Kurum A.Ş.", kisa: "Örnek"}
logo: logo.png
sector: banking                 # org_fields.yaml kodu
employee_band: 1000-4999
ai_use: [ext-assistant, rag]
olgular: {}                     # K7 sonrası: {iso27001: yes}
iletisim: [{rol: CISO}]         # kişi adı yok
```

### 4.3 `degerlendirme.yaml`

```yaml
id: ornek-2026-as01
servis: AS-01
framework: {surum: v1.0-draft, commit: 4440cdc}  # açılışta yazılır, değişmez
ref_date: 2026-11-05            # tarih kontrolleri bu tarihe göre değerlendirilir
durum: taslak                   # taslak → incelemede → kapali
degerlendirici: gokhan          # kullanıcı kimliği (§5.3)
gozden_geciren: ayhan
sistemler:                      # QS'de en çok 2
  - {id: asistan, ad: "Kurumsal Asistan", profil: CE, aciklama: "", saglayici: ""}
oturum_notu: ""                 # görüşmenin başı ve sonu, katılımcı rolleri
olaylar:                        # durum geçişleri: kim, ne zaman
  - {ne: acildi, kim: gokhan, zaman: 2026-11-05T10:02:00+03:00}
```

### 4.4 `cevaplar/<birim>.yaml`

```yaml
HYG-ING-02:
  gorusme_notu: "Ham not: müşteri X dedi…"   # kontrol notlarından ayrı
  na_reason: null
  kontroller:
    c1: {cevap: E, durum: cevaplandi, not: "", kanit: []}
    c2: {cevap: null, durum: atlandi, not: ""}
    c3: {cevap: "7/7", durum: cevaplandi, basis: verified,           # AS-02
         kanit: [{tur: CFG, ref: "EK-04"}],
         orneklem: {secilen: ["..."], gerekce: "..."}}
  inceleme: {karar: katiliyor, yorum: "", kim: ayhan, zaman: ...}
  guncelleme: {kim: gokhan, zaman: ...}
```

- **Kontrol durumu:** `bos` · `cevaplandi` · `atlandi`. Madde durumu kontrollerden ve nottan türetilir: `bos` → `not-alindi` (notu var, cevabı eksik) → `tamam`.
- **Saklanmaz, her seferinde hesaplanır:** madde puanı, seviye, risk sırası.

### 4.5 CSV'ye dönüşüm

`qs.py` `FIELDS` sırası birebir korunur. G satırlarında `profile=CE/SOV` ve `level=CE:L2/SOV:L1` biçimi aynen üretilir.

| CSV alanı | Kaynak |
|---|---|
| `answer` | `cevap`; `atlandi` ya da `bos` ise kapanışta `B` |
| `note` | kontrol notu; atlandıysa "atlandı" eklenir. Görüşme notu CSV'ye girmez, memo girdisine girer |
| `na_reason` | maddenin `na_reason`'ı, c1 satırına |
| `evidence_ref` | `kanit` listesi, `;` ile birleştirilmiş |
| `assessor` / `reviewer` | `degerlendirme.yaml`'dan; maddenin bütün satırlarına aynı değer |
| `score` | boş (betik hesaplar) |

**Kabul testi:** Aynı cevaplarla elle doldurulmuş CSV ve arayüzün ürettiği CSV, `qs.py seviye`'den **bayt bayt aynı** çıktıyı vermeli.

## 5. Uygulama

### 5.1 `qs.py` ve `kontrol.py`'de küçük değişiklikler

- `cmd_seviye` içindeki hesap saf bir fonksiyona ayrılır (`hesapla(rows, ref_date) -> {seviyeler, riskler, bloklayanlar, bosluklar}`). Markdown çıktısı bu fonksiyonun sonucundan üretilir. **Mevcut çıktı değişmez**; regresyon testiyle güvence altına alınır.
- `ref_date`, `collapse()` üzerinden `kontrol.score()` ve `check_met()`'e geçirilir. Verilmezse bugünkü davranış (bugünün tarihi) korunur.
- Arayüz yalnız bu fonksiyonları çağırır. Madde ve kontrol metni yazmaz, YAML'dan okur.

### 5.2 Ekranlar

1. **Değerlendirmeler:** liste, yeni değerlendirme açma.
2. **Kurum ve kapsam:** tanımlayıcı alanlar, logo, sistemler ve profilleri.
3. **Madde ekranı:** başta `qs_question`; açılır alanlarda derinleştirme sorusu ve uygulanabilirlik. Ardından görüşme notu, kontroller (E/H/B, c1'de NA), kontrol notu, kanıt referansı; yan panelde terimler. Altta tespit satırı: "Bu cevaplarla madde puanı: 1 — karşılanmayan: c3" (düzenlenemez). Atla / önceki / sonraki düğmeleri; solda durum işaretli madde listesi.
4. **Kapanış:** eksikler listesi (atlanan, boş, notu olup cevabı eksik) → onay → `incelemede`.
5. **İnceleme:** madde başına katılıyorum / katılmıyorum + yorum; uyuşmazlık listesi → `kapali`.
6. **Sonuç:** sistem başına matris / G / raporlanan seviye, seviyeyi bloklayan maddeler, en kritik 5 risk; `cikti/qs.csv` ve `cikti/seviye.md` üretimi.

Madde sırası `qs_items()` sırasıdır (seviye, sonra ID; 16 Ekim K8 açık). Arayüz dili TR.

### 5.3 Kimlik ve eşzamanlılık

- **Kimlik:** Apache'nin doğruladığı kullanıcı `X-Remote-User` başlığıyla gelir. Bu başlığa yalnız `127.0.0.1`'den gelen istekte güvenilir. Yerelde kimlik `LECTA_USER` ortam değişkeninden okunur.
- **Yazma:** dosya başına kilit (`fcntl`) + iyimser sürüm kontrolü. Form dosyanın hash'ini taşır; dosya o arada değiştiyse kayıt reddedilir ve "başkası değiştirdi, yenile" mesajı gösterilir. Aynı birimde başka kullanıcı varsa ekranda uyarı çıkar.
- gunicorn tek worker + thread'lerle çalışır.

### 5.4 Donut kurulumu

- Container 127.0.0.1:`<port>`'u dinler; Apache vhost reverse proxy yapar, TLS certbot ile.
- **Erişim:** ✅ VPN kısıtı (`Require ip 10.11.12.0/24`) **ve** Apache kimlik doğrulaması (htpasswd, bcrypt). Ad VPN adresine çözüldüğü için TLS Let's Encrypt DNS-01 ile (yalnız `_acme-challenge.lecta-frui` dinamik alt bölge). Ayhan'a bir VPN profili verilir (Gökhan, 27 Ekim). Ayrıntı: `ui/deploy/KURULUM.md`
- **Volume:** `/srv/lecta-ui/data` → container'da `/data`; değerlendirme repoları burada.
- **Framework sürümü:** imaj belirli bir commit'ten build edilir. Açık bir değerlendirmenin `framework.commit`'i imajınkinden farklıysa ekranda uyarı çıkar ve CSV başlığına iki commit de yazılır.
- **Git:** v1'de uygulama değerlendirme reposuna yerel commit atar (kapanışta ve "anlık görüntü" düğmesiyle). GitHub'a push elle yapılır; repo başına deploy key ile otomatik push sonraki adım ❓.
- Alan adı ✅ `lecta-frui.deepwake.tech` (Gökhan, 27 Ekim).

## 6. Test verisi

`ui/fixtures/` altında sentetik "Örnek Kurum" (1 CE + 1 SOV sistem). A1 POC kurgusu hazır olunca (hedef 29 Ekim) o kurgu eklenir. **Gerçek müşteri verisi, arayüz kabul edilene kadar girilmez.**

## 7. Kabul edilen riskler

- Veri donut diskinde şifresiz duruyor (Gökhan, 26 Ekim). Bu durum ilk gerçek müşteriden önce yeniden değerlendirilecek.
- donut çok amaçlı bir VPS. Bu risk ayrı container, ayrı volume ve erişim katmanıyla sınırlanıyor.
- Notlarda kişi adı yazılmaması bir kuraldır, arayüz bunu denetlemez.
