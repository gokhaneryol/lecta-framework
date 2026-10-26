# Quick Scan — Gösterge Seviye Hesabı

*Kaynak: `karisik-1.csv` · `tools/qs.py seviye` ile üretildi*

| Birim | Profil | Matris (gösterge) | G bloğu (gösterge) | **Raporlanan** |
|---|---|---|---|---|
| Kurumsal Asistan | CE | L0 altı | L0 altı | **L0 altı** |
| Belge Arama | SOV | L0 altı | L0 altı | **L0 altı** |

*Gösterge seviye beyana dayalıdır ve 9 kurum + sistem başına 8 maddelik alt kümeyle hesaplanmıştır; L1'in üstünde seviye üretmez. Doğrulanmış seviye için Detailed Scan (AS-02) gerekir.*

## En kritik 5 risk (sıralama kuralı: puan ↑ · seviye ↑ · CE zinciri önce · kurum önce · ID)

| # | Madde | Birim | Seviye | Puan | Not |
|---|---|---|---|---|---|
| 1 | G-POL-02 · Yapay zekâ araçlarının kabul edilebilir kullanımı | Örnek Kurum | CE:L0/SOV:L0 | 0 | karşılanmayan: c1 |
| 2 | CON-INF-01 · Çıkarımın yönetilen sınır içinde kalması | Belge Arama | L1 | 0 | s1: Sentetik not 38 · karşılanmayan: c1, c2, c4 |
| 3 | CON-STO-02 · Kontrollü anahtarlarla depolamada şifreleme | Kurumsal Asistan | L1 | 0 | karşılanmayan: c1, c4 |
| 4 | HYG-ING-01 · Kişisel veri kapsamı ve muamelesi tanımlı | Kurumsal Asistan | L1 | NE | c1: Sentetik not 28 c4: Sentetik not 97 |
| 5 | HYG-ING-02 · Saklamadan önce otomatik tespit ve muamele | Belge Arama | L1 | 0 | karşılanmayan: c1, c2, c3, c4, s1, s2 |

*Geçmeyen madde sayısı: 21. Tamamı memo ekindeki tabloda.*

