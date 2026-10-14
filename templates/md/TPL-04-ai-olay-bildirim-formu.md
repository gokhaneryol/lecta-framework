---
title: "{{Kurum}} — Yapay Zekâ Olay Bildirim Formu"
id: TPL-04
g_items: [G-INC-01]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-INC-01 (TPL-03'ün eki). Bölüm A çalışan tarafından 5 dakikada doldurulabilecek kadar kısa tutuldu; teknik alanlar Bölüm B'de koordinatöre bırakıldı.
> **Uyarlama:** Kurumun olay yönetim aracı varsa form alanları oraya taşınır; alan adları korunursa kayıtlar karşılaştırılabilir kalır.

# Bölüm A — Bildiren (çalışan) doldurur

**Önemli:** Bu forma kişisel veri ya da gizli bilginin kendisini **yazmayın**; yalnız türünü belirtin (ör. "müşteri TCKN'leri", "teklif dosyası").

| Alan | Cevap |
|---|---|
| Ad soyad / birim / telefon | |
| Fark edilme tarihi ve saati | |
| Olayın yaşandığı tarih ve saat (biliniyorsa) | |
| Hangi AI aracı / sistemi? | |
| Kurum hesabı mı, kişisel hesap mı? | ☐ Kurum ☐ Kişisel ☐ Bilmiyorum |

**Ne oldu?** (uygun olanları işaretleyin)

☐ AI aracına izin verilmeyen veri girildi / yüklendi\
☐ AI başka bir kişinin verisini ya da görmemem gereken bir bilgiyi gösterdi\
☐ AI yanlış, zararlı ya da uygunsuz bir çıktı üretti ve bu çıktı kullanıldı / dışarıya gitti\
☐ AI'nin olağandışı davrandığını ya da kurallarını aştığını düşünüyorum\
☐ AI sağlayıcısından bir uyarı / bildirim geldi\
☐ Diğer:

**Kısa açıklama** (en fazla birkaç cümle):

&nbsp;

**İlgili veri türü:** ☐ Kişisel veri ☐ Özel nitelikli kişisel veri (sağlık, biyometrik vb.) ☐ Gizli kurum bilgisi ☐ Müşteri bilgisi ☐ Bilmiyorum

**Yaklaşık kaç kişi / kayıt etkilenmiş olabilir?** ☐ 1–10 ☐ 11–100 ☐ 100+ ☐ Bilmiyorum

**Şu ana kadar ne yaptınız?** (ör. sohbeti sildim, çıktıyı geri çektim, hiçbir şey)

&nbsp;

# Bölüm B — Olay koordinatörü doldurur

| Alan | Kayıt |
|---|---|
| Olay no | {{AI-yyyy-nnn}} |
| Alınış tarihi / saati | |
| Olay türü (TPL-03 Bölüm 3) | ☐ AI-1 ☐ AI-2 ☐ AI-3 ☐ AI-4 |
| Önem derecesi | ☐ Düşük ☐ Orta ☐ Yüksek ☐ Kritik |
| İlgili AI sistemi (envanter no) ve sahibi | |
| Kişisel veri ihlali şüphesi? | ☐ Evet → DPO'ya iletildi: {{tarih/saat}} ☐ Hayır |
| **Yasal bildirim süresi başlangıcı** (öğrenme anı) | {{tarih/saat}} |
| Bildirim kararı ve gerekçesi | ☐ KVKK ☐ GDPR ☐ 7545 ☐ Sektör ☐ Müşteri ☐ Sağlayıcı ☐ Gerekmiyor — gerekçe: |
| Korunan kanıtlar (prompt/yanıt kaydı, erişim kaydı, ekran görüntüsü) | |
| İlk müdahale adımları | |
| Kök neden | |
| Aksiyonlar — sorumlu — hedef tarih | |
| Kapanış tarihi / kapatan | |
