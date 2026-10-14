---
title: "{{Kurum}} — Yapay Zekâ Sistem Envanteri"
id: TPL-05
g_items: [G-INV-01, G-ROL-01]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-INV-01, rubric 2 — zorunlu alanlar (amaç, sahip, kullanıcılar, veri kategorileri, sağlayıcı, profil, durum) her kayıtta dolu; son 6 ayda güncel. Rubric 2'nin "satın alma kayıtlarında, onaylı araç listesinde ya da görüşmelerde görülen hiçbir sistem eksik değil" şartı için Bölüm 3'teki mutabakat yapılır. G-ROL-01'in "her sistemin sahibi" kanıtı da bu tablodur.
> **Uyarlama:** Pratikte bir tablo dosyası (xlsx) ya da kurumun varlık envanteri aracında tutulur; bu belge alan tanımlarını ve kuralları verir. Profil alanı Lecta framework'ündeki CE/SOV ayrımıdır; müşteriye "Dış servis / Kurum içi / Hibrit" olarak gösterilir.

# 1. Amaç ve kural

{{Kurum}}'da canlıda ya da pilotta olan her AI sistemi ve kullanım senaryosu bu envanterde kayıtlıdır. **Envanterde olmayan bir AI sistemi kullanılamaz** (Yapay Zekâ Politikası, Bölüm 6). Envanterin sahibi AI yönetişim sorumlusudur; en geç **6 ayda bir** güncellenir.

# 2. Alanlar

| # | Alan | Açıklama | Zorunlu |
|---|---|---|---|
| 1 | Envanter no | AI-SYS-nnn | ✓ |
| 2 | Sistem / kullanım senaryosu adı | | ✓ |
| 3 | Amaç | Hangi iş için, bir cümle | ✓ |
| 4 | AI sistem sahibi | Ad soyad, unvan | ✓ |
| 5 | Kullanıcı grupları ve yaklaşık sayı | Birimler | ✓ |
| 6 | Veri kategorileri | Genel / kurum içi / gizli / kişisel / özel nitelikli | ✓ |
| 7 | Kişisel veri işleniyor mu? | Evet ise etki değerlendirmesi no (TPL-11) | ✓ |
| 8 | Sağlayıcı ve ürün | Model ve servis sağlayıcısı; kurum içi ise "kurum içi" | ✓ |
| 9 | İşleme yeri / profil | Dış servis (CE) · Kurum içi (SOV) · Hibrit | ✓ |
| 10 | Verinin yurt dışına çıkıp çıkmadığı | Evet / Hayır / Bilinmiyor | ✓ |
| 11 | Durum | Pilot / Canlı / Askıda / Kapatıldı | ✓ |
| 12 | Risk sınıfı ve değerlendirme tarihi | TPL-09 / TPL-10 no | Canlı için ✓ |
| 13 | İnsan gözetimi gereken çıktılar | Var / Yok (TPL-13 no) | Canlı için ✓ |
| 14 | Canlıya alma onayı | Onaylayan, tarih | Canlı için ✓ |
| 15 | Son güncelleme tarihi | | ✓ |

# 3. Mutabakat (her güncellemede)

Envanter aşağıdaki kaynaklarla karşılaştırılır; bulunan her eksik sistem eklenir ya da kullanımı durdurulur:

| Kaynak | Kontrol edildi | Eklenen / çıkarılan |
|---|---|---|
| Onaylı AI araç listesi (TPL-02 Ek A) | ☐ {{tarih}} | |
| Satın alma ve lisans kayıtları (AI içeren ürün/abonelikler) | ☐ {{tarih}} | |
| AI servis trafiği raporu (ağ kayıtları) | ☐ {{tarih}} | |
| Proje portföyü / BT değişiklik kayıtları | ☐ {{tarih}} | |

# 4. Envanter tablosu

| No | Ad | Amaç | Sahip | Kullanıcılar | Veri | Kişisel? | Sağlayıcı | Profil | Yurt dışı? | Durum | Risk | Gözetim | Onay | Güncelleme |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI-SYS-001 | {{…}} | | | | | | | | | | | | | |
