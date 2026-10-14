# Quick Scan Kesiti (AS-01)

*Ölçüm aracı · Oturum 3 · 14 Ekim 2026 · durum: kesit tanımlı (draft); memo şablonu oturum 4*

Kaynak: `source/*.yaml` içinde `quick_scan: true` olan maddeler. Bu liste kaynaktan türetilir; çelişki olursa YAML esastır.

## Kesit — profil başına 17 madde

| # | ID | Başlık | CE | SOV | Birim |
|---|---|---|---|---|---|
| 1 | G-POL-01 | AI policy | L1 | L1 | Kurum |
| 2 | G-POL-02 | Acceptable use of AI tools | L0 | L0 | Kurum |
| 3 | G-INV-01 | AI system inventory | L1 | L1 | Kurum |
| 4 | G-INV-02 | Visibility of AI service use | L1 | L2 | Kurum |
| 5 | G-ROL-01 | Roles and accountability | L1 | L1 | Kurum |
| 6 | G-RSK-01 | AI risk assessment | L2 | L2 | Kurum |
| 7 | G-SUP-01 | AI provider assessment before use | L1 | L2 | Kurum |
| 8 | G-LIT-01 | AI literacy | L1 | L1 | Kurum |
| 9 | G-INC-01 | AI incident procedure | L2 | L2 | Kurum |
| 10 | CON-ING-01 | Approved data sources only | L0 | L0 | Sistem |
| 11 | CON-STO-02 | Encryption at rest with controlled keys | L1 | L1 | Sistem |
| 12 | CON-INF-01 / -02 | Inference inside boundary (SOV) / via sanctioned endpoints (CE) | L1 | L1 | Sistem |
| 13 | IDE-STO-01 | Role-based access to AI data and artefacts | L1 | L1 | Sistem |
| 14 | HYG-ING-01 | Personal data scope and treatment defined | L1 | L1 | Sistem |
| 15 | HYG-ING-02 | Automated detection and treatment before persistence | L1 | L1 | Sistem |
| 16 | HYG-PRM-01 | Personal data in prompts treated before the model | L1 | L2 | Sistem |
| 17 | TRA-ING-01 | Tamper-evident provenance log | L1 | L1 | Sistem |

**Dağılım:** 9 kurum (G) + 8 sistem (matris). Katmanlar: CON 3, HYG 3, IDE 1, TRA 1 — BEH ve ATT bilerek yok (L2+ ve L4+ katmanları). Quick Scan'de sistem maddeleri **en çok 2 sistem** için sorulur (ana kullanım + varsa bir CE kullanımı) ✅; daha fazlası AS-02'nin işi.

## Neden bunlar
- **CE profilinin kritik zinciri** eksiksiz: kural (G-POL-02) → görünürlük (G-INV-02) → sağlayıcı (G-SUP-01) → kontrollü çıkış (CON-INF-02) → prompt'ta PII (HYG-PRM-01).
- **G-RSK-01 ve G-INC-01 L2** ama kesitte: Quick Scan memo'sunun "en kritik 5 risk" bölümü için yüksek bilgi değeri. Seviye hesabına L0–L1 sınırında girmezler, bulgu olarak raporlanırlar.
- **Kesitte olmayan L0–L1 maddeler:** CON-ING-02 (TLS — beyanla hep "evet"), CON-STO-01 (ağ ayrıştırma), IDE-ING-01 (kaynak kimliği — CON-ING-01 yakalıyor), HYG-ING-03 (fail-closed — test gerektiriyor). Bunlar AS-02'de ölçülür.

## Quick Scan seviye kuralı ✅ (Gökhan, 14 Ekim)
Geçiş kapısı tüm uygulanabilir maddeleri ister; Quick Scan ise alt küme ve `declared`. Öneri:
- Quick Scan sonucu **"gösterge seviye"** olarak verilir ve kapı **yalnız kesitteki maddelere** uygulanır: kesitteki L0 maddeleri ≥2 → gösterge L0; L0+L1 maddeleri ≥2 → gösterge L1. Kesit L1'in üstünde seviye üretmez (katalog önerisi K-1 ile tutarlı).
- Memo'da sabit cümle: *"Gösterge seviye, beyana dayalı ve [n] maddelik alt kümeyle hesaplanmıştır; doğrulanmış seviye için Detailed Scan gerekir."*
- G bloğu sınırı Quick Scan'de de uygulanır (kesitteki G maddeleriyle).

## Tahmini görüşme süresi
17 madde × ~4 dk + açılış/kapanış ≈ 90 dakikalık tek görüşme (BT/güvenlik + bir iş birimi sahibi). 2–3 adam-günlük efor bandıyla tutarlı (hazırlık + görüşme + memo).
