# Quick Scan — Gösterge Seviye Hesabı

*Kaynak: `karisik-2.csv` · `tools/qs.py seviye` ile üretildi*

| Birim | Profil | Matris (gösterge) | G bloğu (gösterge) | **Raporlanan** |
|---|---|---|---|---|
| Kurumsal Asistan | CE | L0 | L0 altı | **L0 altı** |
| Belge Arama | SOV | L0 altı | L0 altı | **L0 altı** |

*Gösterge seviye beyana dayalıdır ve 9 kurum + sistem başına 8 maddelik alt kümeyle hesaplanmıştır; L1'in üstünde seviye üretmez. Doğrulanmış seviye için Detailed Scan (AS-02) gerekir.*

## En kritik 5 risk (sıralama kuralı: puan ↑ · seviye ↑ · CE zinciri önce · kurum önce · ID)

| # | Madde | Birim | Seviye | Puan | Not |
|---|---|---|---|---|---|
| 1 | G-POL-02 · Yapay zekâ araçlarının kabul edilebilir kullanımı | Örnek Kurum | CE:L0/SOV:L0 | 0 | c2: Sentetik not 58 · karşılanmayan: c1, c4, s1 |
| 2 | HYG-PRM-01 · Prompt'taki kişisel verinin modele ulaşmadan işlenmesi | Kurumsal Asistan | L1 | 0 | karşılanmayan: c1 |
| 3 | CON-INF-01 · Çıkarımın yönetilen sınır içinde kalması | Belge Arama | L1 | 0 | c4: Sentetik not 24 s1: Sentetik not 22 · karşılanmayan: c1, c2, s1, s2 |
| 4 | CON-STO-02 · Kontrollü anahtarlarla depolamada şifreleme | Kurumsal Asistan | L1 | 0 | karşılanmayan: c1, s1 |
| 5 | HYG-ING-02 · Saklamadan önce otomatik tespit ve muamele | Kurumsal Asistan | L1 | 0 | karşılanmayan: c1, c3 |

*Geçmeyen madde sayısı: 16. Tamamı memo ekindeki tabloda.*

