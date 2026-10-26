# Quick Scan — Gösterge Seviye Hesabı

*Kaynak: `karisik-3.csv` · `tools/qs.py seviye` ile üretildi*

| Birim | Profil | Matris (gösterge) | G bloğu (gösterge) | **Raporlanan** |
|---|---|---|---|---|
| Kurumsal Asistan | CE | L0 | L0 altı | **L0 altı** |
| Belge Arama | SOV | L0 | L0 altı | **L0 altı** |

*Gösterge seviye beyana dayalıdır ve 9 kurum + sistem başına 8 maddelik alt kümeyle hesaplanmıştır; L1'in üstünde seviye üretmez. Doğrulanmış seviye için Detailed Scan (AS-02) gerekir.*

## En kritik 5 risk (sıralama kuralı: puan ↑ · seviye ↑ · CE zinciri önce · kurum önce · ID)

| # | Madde | Birim | Seviye | Puan | Not |
|---|---|---|---|---|---|
| 1 | G-POL-02 · Yapay zekâ araçlarının kabul edilebilir kullanımı | Örnek Kurum | CE:L0/SOV:L0 | NE | c1: Sentetik not 48 c4: Sentetik not 73 |
| 2 | G-INV-02 · AI servis kullanımının görünürlüğü | Örnek Kurum | CE:L1/SOV:L2 | 0 | s2: Sentetik not 79 · karşılanmayan: c1, c2, c3, c4, c5, s2 |
| 3 | G-SUP-01 · Kullanım öncesi AI sağlayıcı değerlendirmesi | Örnek Kurum | CE:L1/SOV:L2 | 0 | c2: Sentetik not 76 c3: Sentetik not 89 · karşılanmayan: c1, c4 |
| 4 | CON-INF-02 · Dış çıkarımın yalnız onaylı uç noktalardan yapılması | Kurumsal Asistan | L1 | 0 | c3: Sentetik not 7 · karşılanmayan: c1, c3, s1 |
| 5 | G-INV-01 · Yapay zekâ sistem envanteri | Örnek Kurum | CE:L1/SOV:L1 | 0 | karşılanmayan: c1 |

*Geçmeyen madde sayısı: 19. Tamamı memo ekindeki tabloda.*

