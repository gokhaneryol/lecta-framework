---
title: "{{Kurum}} — Yapay Zekâ Araçları Kabul Edilebilir Kullanım Kuralları"
id: TPL-02
g_items: [G-POL-02, G-LIT-01]
version: 1.0-draft
framework: Lecta Sovereign AI Control Framework v1.0-draft
date: 2026-10-14
---

> **Lecta şablon notu — müşteriye vermeden önce bu kutuyu silin.**
> **Karşıladığı madde:** G-POL-02, rubric 2 — veri sınıflandırmasına atıf (Bölüm 3), araç başına izinli veri sınıfı ve güncelleme tarihi (Ek A). "İki çalışanın kuralları tutarlı anlatması" ölçütü belgeyle değil eğitimle sağlanır (G-LIT-01; Bölüm 7).
> **Ön koşul:** Kurumun bir veri sınıflandırması olmalı. Yoksa Bölüm 3'teki dört sınıf önerisi geçici olarak kullanılır ve bu bir bulgu olarak kaydedilir.
> **Uyarlama:** Ek A'daki araçlar örnektir; kurumun gerçek lisans ve sözleşmelerine göre doldurulur.

# 1. Amaç ve kapsam

Bu kurallar, {{Kurum}} çalışanlarının iş amacıyla AI araçlarını nasıl kullanacağını belirler ve **Yapay Zekâ Politikası**'nın ({{TPL-01 no}}) parçasıdır. Kurallar, kurum cihazlarında ve kişisel cihazlarda yapılan tüm iş amaçlı kullanımı kapsar.

# 2. Temel kural

**Bir AI aracını iş için yalnız Ek A'daki onaylı araç listesinde varsa ve yalnız o araç için izin verilen veri sınıflarıyla kullanabilirsiniz.** Listede olmayan bir aracı kullanmak isterseniz Bölüm 6'daki talep yolunu izleyin.

# 3. Veri sınıfları

{{Kurumun veri sınıflandırması varsa ona atıf yapın ve bu tabloyu kurumun sınıflarıyla değiştirin.}}

| Sınıf | Örnekler | Genel kural |
|---|---|---|
| **Genel** | Yayımlanmış bilgiler, genel bilgi soruları, kamuya açık metinler | Onaylı tüm araçlarda kullanılabilir |
| **Kurum içi** | İç yazışmalar, kişisel veri içermeyen süreç belgeleri, taslaklar | Yalnız kurum hesabıyla kullanılan ve sözleşmeli araçlarda |
| **Gizli** | Sözleşmeler, finansal veriler, kaynak kod, teklif ve ihale belgeleri, ticari sırlar | Yalnız Ek A'da açıkça izin verilen araçlarda |
| **Kişisel / özel nitelikli kişisel veri** | Ad-soyad ile birlikte TCKN, IBAN, telefon, adres; sağlık, biyometrik, ceza mahkûmiyeti verileri | Yalnız Ek A'da açıkça izin verilen ve verinin kurum sınırında maskelendiği araçlarda; **özel nitelikli veri dış AI servislerine girilmez** {{kurum kararı}} |

# 4. Yapın

- Kurum hesabınızla (kurumsal e-posta / tek oturum açma) giriş yapın.
- Prompt'a veri girmeden önce sınıfını düşünün; emin değilseniz bir üst sınıf varsayın.
- AI çıktısını kullanmadan önce doğruluğunu kontrol edin; çıktının sorumluluğu sizdedir.
- Dışarıya giden belgelerde AI'nin kullanıldığını, {{kurum kuralına göre}} belirtin.
- Yanlışlıkla izin verilmeyen bir veri girdiyseniz hemen bildirin (Bölüm 8). Bildirim cezalandırılmaz; geç kalınması zararı büyütür.

# 5. Yapmayın

- Kişisel hesabınızla ya da ücretsiz sürümlerle iş verisi işlemeyin.
- Müşteri, hasta, vatandaş ya da çalışan verisini izin verilmeyen araca kopyalamayın.
- AI'ye parola, erişim anahtarı ya da kimlik bilgisi vermeyin.
- Bir kişi hakkında karar (işe alım, kredi, performans, hizmet erişimi) yalnız AI çıktısına dayanarak vermeyin; İnsan Gözetimi Prosedürü'ne ({{TPL-13 no}}) uyun.
- Onaysız tarayıcı eklentisi, masaüstü uygulaması ya da toplantı kayıt/özet botu kurmayın.

# 6. Yeni araç talebi

Listede olmayan bir araç için {{talep kanalı / form}} üzerinden talep açın. Talep; amaç, kullanılacak veri sınıfları ve kullanıcı sayısını içerir. Değerlendirme, Yapay Zekâ Politikası Bölüm 6'daki onay yoluyla yapılır. Hedef cevap süresi: {{10 iş günü}}.

# 7. Eğitim

AI araçlarına erişim verilen her çalışan, erişimden sonraki **60 gün** içinde {{AI okuryazarlık eğitimi adı}}'ni tamamlar. Tamamlama {{eğitim sistemi}}'nde kaydedilir.

# 8. Bildirim

Şüpheli bir durum, yanlışlıkla veri girişi ya da zararlı bir çıktı: {{bildirim kanalı — e-posta / form / telefon}} — AI Olay Bildirim Formu ({{TPL-04 no}}).

# 9. İzleme

{{Kurum}}, AI servislerine giden ağ trafiğini içerik düzeyinde değil, **üst veri düzeyinde** (servis adı, birim, hacim) izler. İzleme, kişisel verilerin korunması mevzuatına ve kurumun çalışan aydınlatma metnine uygun olarak yapılır. {{Hukuk danışmanının onayladığı aydınlatma metnine atıf}}

# Ek A — Onaylı AI araç listesi

Son güncelleme: **{{gg.aa.yyyy}}** · Sahibi: {{AI yönetişim sorumlusu}} · Gözden geçirme: en geç 12 ayda bir

| Araç | Kullanım amacı | Hesap türü | Genel | Kurum içi | Gizli | Kişisel | Not |
|---|---|---|---|---|---|---|---|
| {{Örn. kurum içi doküman asistanı}} | Belge arama, özet | Kurum SSO | ✓ | ✓ | ✓ | ✓ (maskeli) | Kurum sınırında çalışır |
| {{Örn. kurumsal sözleşmeli üretken AI servisi}} | Metin taslağı, çeviri | Kurumsal lisans | ✓ | ✓ | ✗ | ✗ | Eğitimde kullanmama taahhüdü var (TPL-08) |
| {{Örn. kod asistanı}} | Kod önerisi | Kurumsal lisans | ✓ | ✓ | {{✓/✗}} | ✗ | {{…}} |
| Ücretsiz/kişisel hesaplı servisler | — | — | ✗ | ✗ | ✗ | ✗ | Kullanılmaz |
