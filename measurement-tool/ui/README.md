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

## Kimlik

- Yerelde `LECTA_USER`.
- Sunucuda Apache'nin doğruladığı kullanıcı `X-Remote-User` başlığıyla gelir; başlığa yalnız `LECTA_TRUSTED_PROXIES` adreslerinden (varsayılan `127.0.0.1`) gelen istekte güvenilir. `LECTA_USER` sunucuda **tanımlanmaz**.
- Not (adım 2): container köprü ağında çalışırsa istek kaynağı Docker ağ geçidi adresi olur. Kurulumda ya `network_mode: host` + `127.0.0.1` dinleme ya da ağ geçidi adresinin `LECTA_TRUSTED_PROXIES`'e yazılması seçilir.

## Testler

```
pip install -r requirements-dev.txt
pytest
```

- `test_qs_regresyon.py`: `qs.py rehber`, `puanlama` ve `seviye` çıktıları `tests/golden/` ile bayt bayt aynı olmalı. `qs.py`'de her değişiklikten sonra çalıştırılır.
- `test_depo.py`: atomik yazma, dosya kilidi, sürüm çakışması.
- `test_uygulama.py`: kimlik, boş liste sayfası, `org_fields.yaml`.

## Dosyalar

```
app/__init__.py     Flask uygulaması, kimlik
app/depo.py         YAML dosya katmanı: atomik yazma, kilit, sürüm kontrolü
app/framework.py    source/ ve tools/ için tek giriş
app/static/         htmx 2.0.4 (repoda; CDN yok), stil
fixtures/qs/        sentetik puanlama CSV'leri (Örnek Kurum, CE + SOV)
tests/golden/       regresyon testinin beklenen çıktıları
```
