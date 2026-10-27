# Değerlendirme arayüzü (`ui/`)

Quick Scan'in giriş katmanı: değerlendirici görüşmede notlarını ve kontrol cevaplarını buraya girer, çıktı bugünkü `qs.py seviye` akışının değişmeden okuduğu CSV'dir. Kararlar ve veri modeli: [`TASARIM.md`](TASARIM.md) (ADR-001).

**Kurallar:** madde, kontrol ve terim metni yalnız `source/*.yaml`'dan okunur; puan, seviye ve risk sırası yalnız `tools/kontrol.py` ve `tools/qs.py` ile hesaplanır (`app/framework.py` tek giriş). Müşteri verisi bu repoya girmez: veri dizini (`LECTA_DATA`) repo dışındadır; `fixtures/` yalnız sentetik veri içerir.

## Çalıştırma

```
LECTA_USER=gokhan LECTA_DATA=~/Claude/Projects/Lecta/engagements-dev docker compose up --build
```

Arayüz `http://127.0.0.1:8080` adresinde açılır (`LECTA_PORT` ile değişir). İmajın framework commit'ini etiketlemek için `FRAMEWORK_COMMIT=$(git rev-parse --short HEAD)` ekleyin; commit ekranın altında görünür.

Docker'sız geliştirme:

```
pip install -r requirements-dev.txt
LECTA_USER=gokhan LECTA_DATA=/tmp/lecta-dev flask --app app:create_app run
```

## Kayıt

Her alan değiştiğinde htmx ile kaydedilir; yanıt yalnız sürüm alanını ve "Kaydedildi" satırını günceller (odak kaybolmaz). Aynı dosyayı yazan istekler sıraya girer (`hx-sync`); dosya başka bir oturumda değiştiyse kayıt reddedilir ve sayfayı yenileme mesajı çıkar.

## Kimlik

- Yerelde `LECTA_USER`.
- Sunucuda Apache'nin doğruladığı kullanıcı `X-Remote-User` başlığıyla gelir; başlığa yalnız `LECTA_TRUSTED_PROXIES` adreslerinden (varsayılan `127.0.0.1`) gelen istekte güvenilir. `LECTA_USER` sunucuda **tanımlanmaz**.
- Sunucuda container köprü ağında çalışır; istek kaynağı Docker ağ geçidi olduğu için `LECTA_TRUSTED_PROXIES=172.30.0.1` (`deploy/compose.donut.yaml`).

## Sunucu (donut)

Kurulum, güncelleme ve geri alma: [`deploy/KURULUM.md`](deploy/KURULUM.md).

## Testler

```
pip install -r requirements-dev.txt
pytest
```

- `test_qs_regresyon.py`: `qs.py rehber`, `puanlama` ve `seviye` çıktıları `tests/golden/` ile bayt bayt aynı olmalı. `qs.py`'de her değişiklikten sonra çalıştırılır.
- `test_depo.py`: atomik yazma, dosya kilidi, sürüm çakışması.
- `test_uygulama.py`: kimlik, boş liste sayfası, `org_fields.yaml`.
- `test_kapsam.py`: değerlendirme açma, kurum ve kapsam ekranları; fixture kurumun arayüzle oluşturulması (adım 3 kabulü).
- `test_kapanis.py`: **kabul testi** — aynı cevaplarla elle doldurulmuş CSV ile arayüz CSV'si bayt bayt aynı, `qs.py seviye` çıktıları aynı (5 sentetik CSV); kapanış → inceleme → kapanma akışı, git commit'leri (adım 5).
- `test_gorusme.py`: `fixtures/qs/*.csv` cevapları arayüzden girilir, her maddenin tespiti `qs.hesapla()` puanıyla aynı olmalı; skip ve NA kuralları, madde düzeyinde çakışma (adım 4 kabulü).

## Dosyalar

```
app/__init__.py     Flask uygulaması, kimlik, başka siteden POST engeli
app/rotalar.py      ekranlar: değerlendirme listesi, yeni değerlendirme, kurum ve kapsam
app/kayit.py        değerlendirme dizini: açma (şablon + git init), kurum/sistem doğrulama
app/gorusme.py      görüşme: birimler, madde cevapları, skip kuralları (K4), madde durumu, tespit (kontrol.py ile)
app/gorusme_ekran.py madde ekranları, madde düzeyinde sürüm kontrolü, aynı birimde başka kullanıcı uyarısı
app/static/klavye.js klavye kısayolları; sayfa kapanırken kaydedilmemiş değişikliği gönderir
app/cikti.py        CSV'ye dönüşüm (qs.puanlama_satirlari üstüne), eksikler, inceleme, durum geçişleri, cikti/ dosyaları
app/kapanis_ekran.py kapanış, inceleme, sonuç ekranları; durum geçişlerinde yerel git commit
app/sablon/         yeni değerlendirme dizininin şablonu (.gitignore, README)
app/depo.py         YAML dosya katmanı: atomik yazma, kilit, sürüm kontrolü
app/framework.py    source/ ve tools/ için tek giriş
app/static/         htmx 2.0.4 (repoda; CDN yok), stil
fixtures/qs/        sentetik puanlama CSV'leri (Örnek Kurum, CE + SOV)
fixtures/ornek-2026-as01/  arayüzle oluşturulan sentetik değerlendirme (kabul testi beklentisi)
tests/golden/       regresyon testinin beklenen çıktıları
```
