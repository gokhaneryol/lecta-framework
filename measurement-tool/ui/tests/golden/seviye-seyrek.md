# Quick Scan — Gösterge Seviye Hesabı

*Kaynak: `seyrek.csv` · `tools/qs.py seviye` ile üretildi*

> ⚠️ Boş puan (42): G-INC-01/c2@Örnek Kurum, G-INC-01/c3@Örnek Kurum, G-INC-01/s2@Örnek Kurum, G-INV-01/c2@Örnek Kurum, G-INV-01/s1@Örnek Kurum, G-INV-02/c4@Örnek Kurum, G-LIT-01/c3@Örnek Kurum, G-LIT-01/s1@Örnek Kurum, G-LIT-01/s2@Örnek Kurum, G-POL-01/c2@Örnek Kurum, G-POL-01/c3@Örnek Kurum, G-POL-02/c2@Örnek Kurum, G-POL-02/c3@Örnek Kurum, G-POL-02/s1@Örnek Kurum, G-ROL-01/c2@Örnek Kurum, G-SUP-01/c3@Örnek Kurum, CON-ING-01/s1@Kurumsal Asistan, CON-INF-02/c2@Kurumsal Asistan, CON-INF-02/c3@Kurumsal Asistan, CON-STO-02/c1@Kurumsal Asistan, CON-STO-02/c2@Kurumsal Asistan, HYG-ING-01/c6@Kurumsal Asistan, HYG-ING-02/c1@Kurumsal Asistan, HYG-PRM-01/c1@Kurumsal Asistan, HYG-PRM-01/c3@Kurumsal Asistan, IDE-STO-01/c5@Kurumsal Asistan, IDE-STO-01/s1@Kurumsal Asistan, TRA-ING-01/c3@Kurumsal Asistan, TRA-ING-01/s1@Kurumsal Asistan, CON-ING-01/c3@Belge Arama, CON-INF-01/c3@Belge Arama, CON-STO-02/c2@Belge Arama, HYG-ING-01/s1@Belge Arama, HYG-ING-02/c1@Belge Arama, HYG-ING-02/c2@Belge Arama, HYG-ING-02/s1@Belge Arama, IDE-STO-01/s1@Belge Arama, TRA-ING-01/s1@Belge Arama, HYG-PRM-01/c1@Belge Arama, HYG-PRM-01/c2@Belge Arama, HYG-PRM-01/c3@Belge Arama, HYG-PRM-01/s1@Belge Arama — boş puan NE, boş kontrol cevabı B (bilmiyor) gibi işlem görür.

| Birim | Profil | Matris (gösterge) | G bloğu (gösterge) | **Raporlanan** |
|---|---|---|---|---|
| Kurumsal Asistan | CE | L0 altı | L0 altı | **L0 altı** |
| Belge Arama | SOV | L0 altı | L0 altı | **L0 altı** |

*Gösterge seviye beyana dayalıdır ve 9 kurum + sistem başına 8 maddelik alt kümeyle hesaplanmıştır; L1'in üstünde seviye üretmez. Doğrulanmış seviye için Detailed Scan (AS-02) gerekir.*

## En kritik 5 risk (sıralama kuralı: puan ↑ · seviye ↑ · CE zinciri önce · kurum önce · ID)

| # | Madde | Birim | Seviye | Puan | Not |
|---|---|---|---|---|---|
| 1 | CON-ING-01 · Yalnız onaylı veri kaynakları | Kurumsal Asistan | L0 | 0 | s1: Sentetik not 20 · karşılanmayan: c1, s1, s2 |
| 2 | CON-ING-01 · Yalnız onaylı veri kaynakları | Belge Arama | L0 | NE | c3: Sentetik not 10 s1: Sentetik not 86 |
| 3 | CON-INF-02 · Dış çıkarımın yalnız onaylı uç noktalardan yapılması | Kurumsal Asistan | L1 | NE |  |
| 4 | HYG-PRM-01 · Prompt'taki kişisel verinin modele ulaşmadan işlenmesi | Kurumsal Asistan | L1 | NE |  |
| 5 | G-LIT-01 · Tüm kullanıcılar için yapay zekâ okuryazarlığı | Örnek Kurum | CE:L1/SOV:L1 | 0 | c3: Sentetik not 99 · karşılanmayan: c1, c3, s1, s2 |

*Geçmeyen madde sayısı: 23. Tamamı memo ekindeki tabloda.*

