# Ölçüm Aracı — İlk Adımlar

*Ayhan için · 14 Ekim 2026*

Lecta Sovereign AI Control Framework'ün ölçüm aracı ve şablon kütüphanesi bu repoda: `measurement-tool/` ve `templates/`. Quick Scan (AS-01) için gereken her şey hazır. Bu belge, nereden başlayacağını ve hangi konularda senin gözüne ihtiyaç olduğunu özetliyor.

## 1. Erişim

- GitHub'dan gelen `gokhaneryol/lecta-framework` davetini kabul et.
- Dosyaları tarayıcıdan okuyabilirsin; ayrıca bir şey kurman gerekmez.
- Claude ile çalışmak istersen claude.ai'da GitHub'ı bağlayıp bu repoyu bir projeye ekleyebilirsin. Claude dosyaları doğrudan okur.
- Betikleri kendin çalıştırmak istersen gereken araçlar `measurement-tool/README.md` dosyasının "Dosyalar ve komutlar" bölümünde.

## 2. Önce okunacaklar (~45 dk)

1. [`measurement-tool/README.md`](measurement-tool/README.md): durum, ölçüm aracının nasıl çalıştığı, Quick Scan akışı, sıradaki işler.
2. [`measurement-tool/output/madde-rubric-tablosu.md`](measurement-tool/output/madde-rubric-tablosu.md): 29 maddenin tamamı ve 0–3 rubric'leri.
3. [`templates/README.md`](templates/README.md): 13 şablonun dizini.

## 3. Senden beklenen geri bildirim

| # | Konu | Nerede | Nasıl |
| --- | --- | --- | --- |
| 1 | **Rubric'lerin netliği.** İkinci değerlendirici gözüyle: aynı kanıta bakan iki kişi aynı puanı verir mi? Özellikle 1 ile 2 arasındaki çizgi. Kanıt beklentisi gerçekçi mi? | `measurement-tool/output/inceleme-paketi.xlsx` | Sarı "Karar" (Onay / Düzelt / Sil / Tartışalım) ve "Yorum" sütunları |
| 2 | **Kanıt ve kayıt tarafı.** Kayıt bütünlüğü (TRA-ING-01), sağlayıcı ve sözleşme maddeleri (G-SUP-01…03), olay prosedürü (G-INC-01). Forensics ve güven hizmetleri deneyimiyle en çok değer katacağın yerler | aynı tablo | aynı |
| 3 | **Şablonlar.** Bir kurumun bunları doldururken nerede takılacağı; eksik ya da fazla alanlar | `templates/docx/` | Word'de yorum ya da kısa bir not |
| 4 | **Katalog önerileri K-1…K-4.** Kataloğa işlenmesi | `measurement-tool/katalog-onerileri.md` | Katalog master'ında |
| 5 | **Ortak işler.** README'deki "Sırada ne var" tablosunda 3, 5, 6, 7, 8 ve 12 numaralı satırlar | `measurement-tool/README.md` | Birlikte konuşalım |

İnceleme tablosunu doldurduktan sonra bana gönder ya da repoya PR olarak ekle. Kararlar kaynak dosyalara işlenir ve tablolar yeniden üretilir.

## 4. Çalışma kuralları

- **Kaynak YAML'dır.** Maddeler `measurement-tool/source/*.yaml` dosyalarında. `output/` ve `docx/` altındaki dosyalar oradan üretilir; elle düzenlenmez.
- **Değişiklikler PR ile girer.** `main` dalına doğrudan yazılmaz. Teknik bir değişiklik değilse yorum ya da inceleme tablosu yeterli.
- **Müşteri verisi bu repoya girmez.** Değerlendirme kayıtları müşteri klasöründe tutulur.
- **Dil.** Ölçüm aracı ve şablonlar denetim dili kullanmaz: "hazırlık", "gösterge", "kapanış ölçütü". Lecta denetlemez, denetime hazırlar.
