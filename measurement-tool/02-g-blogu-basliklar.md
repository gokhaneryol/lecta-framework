# G Bloğu — Madde Başlıkları (öneri)

*Ölçüm aracı · Oturum 1–2 · 14 Ekim 2026 · durum: tam maddeler `source/G.yaml`'da (draft)*

G bloğu **kurum başına bir kez** ölçülür. Seviyeler öneridir; CE/SOV farkı olan yerde ikisi ayrı yazıldı. **QS** = Quick Scan adayı.

| ID | Başlık | Neyi ölçer | Sv. (CE / SOV) | QS | Eşleme adayları | Kaynağı |
|---|---|---|---|---|---|---|
| G-POL-01 | AI policy | Onaylı, yayımlanmış AI politikası; sahibi ve gözden geçirme tarihi | L1 / L1 | ✓ | ISO 42001 A.2.2 · cl. 5.2 | v0'da yok |
| G-POL-02 | Acceptable use of AI tools | Çalışanlar için: hangi araç, hangi veri sınıfı girilebilir; kurala bağlı onaylı araç listesi | L0 / L0 | ✓ | KVKK md.12 · ISO 27001 A.5.10 · ISO 42001 A.9 | Shadow AI |
| G-INV-01 | AI system inventory | Her sistem: amaç, sahip, veri kategorileri, sağlayıcı, profil, kullanıcılar | L1 / L1 | ✓ | ISO 42001 A.4.2 · KVKK VERBİS envanteri · EU AI Act Art.49 (yüksek risk) | v0'da yok |
| G-INV-02 | Visibility of AI service use | AI servislerine giden trafik görünür ve kayıtlı mı (DNS/proxy/firewall) | L1 / L2 | ✓ | KVKK md.12 · ISO 27001 A.8.15–8.16 | AS-04 (Y-10 notu) |
| G-ROL-01 | Roles and accountability | Sistem başına adlandırılmış AI sahibi; yönetişim sorumlusu; DPO/CISO'nun karar noktaları | L1 / L1 | ✓ | ISO 42001 A.3.2 · cl. 5.3 | v0'da yok |
| G-RSK-01 | AI risk assessment | Sistem başına yazılı risk değerlendirmesi; tetikleyiciler (yeni sistem, model değişikliği) | L2 / L2 | ✓ | ISO 42001 cl. 6.1.2 · NIST AI RMF MAP · ISO 27001 cl. 6.1 | L5 artefaktı |
| G-RSK-02 | Risk classification | EU AI Act kategorisine ve sektör kurallarına göre sınıflandırma, gerekçe ve imza | L3 / L3 → L5'te zorunlu | — | EU AI Act Art.6 + Annex III | L5 artefaktı |
| G-RSK-03 | Impact assessment | Kişisel veri işleyen sistemlerde DPIA tarzı etki analizi (AS-07 çıktısı) | L2 / L2 | — | GDPR Art.35 · ISO 42001 A.5 · KVKK md.12(1) | AS-07 |
| G-SUP-01 | Supplier assessment before onboarding | Veri yeri, saklama, eğitimde kullanım, alt işleyenler, aktarım mekanizması — kullanımdan önce | **L1** / L2 | ✓ | KVKK md.9 (Kanun 7499) · ISO 27001 A.5.19–5.22 · ISO 42001 A.10 · DORA Art.28 | ATT-ING'den ayrıldı |
| G-SUP-02 | Sovereignty test | Üç soru: nihai şirketin hukuki yetki alanı · mimari sınır kanıtı · bağımsız işletebilme/çıkış | L2 / L1 | — | KVKK md.9 · BDDK Bilgi Sistemleri Yön. md. 25 · DORA Art.28(8) çıkış | AS-05 → DS-04 |
| G-SUP-03 | Contractual safeguards | DPA, eğitimde kullanmama, silme, ihlal bildirimi, denetim hakkı maddeleri | L2 / L2 | — | KVKK md.9 · GDPR Art.28 · ISO 27001 A.5.20 | v0'da yok |
| G-LIT-01 | AI literacy | Tüm kullanıcılar için asgari okuryazarlık eğitimi, katılım kaydı | L1 / L1 | ✓ | EU AI Act Art.4 · ISO 42001 cl. 7.3 | EN-02 |
| G-LIT-02 | Role-based training | Geliştirici, operatör, gözden geçirici için rol eğitimi | L3 / L3 | — | ISO 42001 cl. 7.2 · ISO 27001 A.6.3 | EN-03 |
| G-INC-01 | AI incident procedure | AI olay tanımı (prompt ile veri sızıntısı, zararlı çıktı, model hatası), bildirim zinciri ve süreleri | L2 / L2 | ✓ | KVKK md.12(5) (72 saat) · Kanun 7545 md. 7(1)(b) · NIS2 Art.23 · ISO 42001 A.8.4 | SU-05 |
| G-OVS-01 | Human oversight | Hangi çıktı sınıfı insana gider, kim, SLA, beklerken ne olur; **en az bir kez uçtan uca işletilmiş** | L3 / L3 → L5'te tam | — | EU AI Act Art.14 · GDPR Art.22 · ISO 42001 A.9 | v0 L3 "process gap" + L5 artefaktı |

**15 madde · 9'u QS adayı** (oturum 1'de "7" yazılmıştı, tabloda 9 işaret var — düzeltildi). Quick Scan kesiti için matristen 8–10 L0–L1 anahtar madde eklenince toplam ~17–19'a oturur (Aşama 2).

> **Oturum 2 (14 Ekim):** 15 maddenin tamamı rubric'leriyle `source/G.yaml`'a yazıldı. Bu tablo artık özet; kaynak `G.yaml`.

## Bilinçli olarak dışarıda bırakılanlar

- **DSAR / ilgili kişi hakları:** v0'da L4 seviye metninde var, hücresi yok. Öneri: teknik kısmı (AI pipeline'da silme/erişim) HYG-STO'ya madde; süreç kısmı kurumun genel KVKK süreci, G bloğuna girmez — IM-06 hizmetiyle ilişkilendirilir. `[KARAR]`
- **Kullanıcıya AI ile etkileşim bildirimi (EU AI Act Art.50):** sistem özelliği → matriste BEH-RES ya da yeni bir RES maddesi.
- **Model card:** sistem belgesi → ATT-INF'te kalır.
