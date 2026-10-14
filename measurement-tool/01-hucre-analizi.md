# 36 Hücre — Ölçülebilirlik Analizi

*Ölçüm aracı · Oturum 1 · 14 Ekim 2026 · kaynak: `regulatives/sovereign_ai_guardrails_hierarchical.md` (Mayıs 2026)*

Amaç: bugünkü hücre ifadelerinin neden doğrudan puanlanamadığını görmek ve v1.0'da her hücrenin nasıl bölüneceğine yön vermek. Kodlar v1.0 ID kuralına göredir (`schema.md`).

**Sorun kodları:** **ABS** mutlak/test edilemez ifade ("every", "no … possible") · **CMP** tek cümlede birden çok gereksinim · **TOOL** araç/mimari bağımlı · **SOV** yalnız kendi işletilen pipeline'ı varsayıyor, Controlled External'a uymuyor · **OVL** başka hücreyle çakışma · **UND** tanımsız kavram ("approved", "necessary", "regulated contexts") · **META** kontrol değil, başka kontrollerin kanıtı · **LVL** seviye tutarsızlığı

## 1. Hücre tablosu

| Kod | Fonksiyon | Sv. | Bugünkü ifade (özet) | Sorun | v1.0 yönü |
|---|---|---|---|---|---|
| CON-ING | Source boundary | L0 | Yalnız onaylı kaynak/format/protokol; diğerleri işlenmeden reddedilir | CMP, UND | Onaylı kaynak kaydı + giriş noktalarının tamamının kayda bağlı olması + ret testi |
| CON-STO | Store isolation | L0 | Depolar arası/tenant'lar arası erişim yok, segmentasyon | SOV, OVL (IDE-STO) | Segmentasyon + **şifreleme (at rest)** buraya; CE'de sağlayıcı tarafı taahhüt |
| CON-PRM | Input surface restrict. | L1 | Yalnız doğrulanmış şablonlar; "by design, not configuration" | ABS, UND, OVL (HYG-PRM, BEH-PRM) | Sohbet asistanında şablon şartı gerçekçi değil → "modele açılan araç/fonksiyon yüzeyi tanımlı ve sınırlı" |
| CON-INF | Execution air-gap | L1 | Inference dış ağdan izole; aktivasyonlar sızdırılamaz | **SOV**, ABS | Profil ayrımı: SOV = egress-deny kanıtı; CE = yalnız sanctioned endpoint'lere allow-list + sağlayıcı taahhüdü |
| CON-RES | Output channel control | L2 | İzinsiz dış yazım "fiziksel olarak mümkün değil" | ABS, eksik: **agent/tool-use** | Model adına aksiyon (tool call, yazma, e-posta) izin listesine bağlı; agentic boşluk burada kapanır |
| CON-DWN | Egress governance | L3 | Çıkan veri loglanır, sınıflanır, kontrol edilir, yetki ister | CMP, OVL (TRA-DWN, HYG-DWN) | Bölünür: dış aktarım yetki kaydı · veri yerleşimi doğrulaması (L5 artefaktı buraya) |
| HYG-ING | PII detect & redact | L1 | Her öğe taranır; ham PII ilerlemez | ABS, UND (PII kapsamı), TOOL | **Örnek hücre** — `kaynak/HYG.yaml` |
| HYG-STO | Data minimisation | L1 | "Necessary and proportionate"; otomatik silme | UND | Saklama çizelgesi + otomatik silme kanıtı; politika kısmı G bloğuna |
| HYG-PRM | Prompt sanitisation | L2 | Enjekte talimat + hassas içerik prompt'tan ayıklanır | CMP, OVL (BEH-PRM), **LVL** | Bölünür: (a) prompt'taki PII → hygiene, (b) injection → behaviour. CE profilinde (a) **L1** olmalı: veri sağlayıcıya burada çıkıyor |
| HYG-INF | Input integrity check | L3 | Şekil/tip/aralık doğrulama, adversarial perturbation tespiti | ABS, OVL (BEH-PRM) | Adversarial tespit güvenilir ölçülemez → yapısal girdi doğrulamasına daralt; GenAI'de çoğu zaman N/A |
| HYG-RES | Output PII scrubbing | L2 | Yanıttaki üretilmiş/halüsine PII çıkarılır | UND (kapsam), ABS | HYG-ING kalıbıyla: kapsam + otomatik filtre + fail-closed + bilinen-cevaplı test |
| HYG-DWN | Clean handoff | L4 | Tüketiciye izinli olandan fazlası gitmez | UND ("explicitly authorised") | Tüketici başına veri sözleşmesi (izinli alanlar) + çıkış kontrolü |
| IDE-ING | Source authentication | L0 | Her kaynak doğrulanabilir kimlik sunar; provenance loglanır | OVL (TRA-ING) | Provenance TRA-ING'e; kullanıcı yüklemelerinde kaynak = kullanıcı kimliği |
| IDE-STO | Artefact access ctrl | L1 | Veri seti, ağırlık, artefakt rol bazlı erişim | — (iyi) | + periyodik erişim gözden geçirme; **secret yönetimi** buraya |
| IDE-PRM | Session attribution | L2 | Her prompt kimliğe bağlı; "regulated contexts"te anonim yok | UND | CE'deki tipik açık: tek paylaşımlı API anahtarı → kullanıcı atfı yok |
| IDE-INF | Role-based model access | L2 | Yetki rolün izin verdiğiyle sınırlı; escalation imkânsız | ABS | **RAG'de belge yetkisinin retrieval'da korunması** açıkça madde olmalı (A kullanıcısı B'nin belgesi — AS-03 senaryosu) |
| IDE-RES | Response binding | L3 | Yanıt kimliğe mantıksal/kriptografik bağlı | OVL (TRA-RES, ATT-RES), UND | Mantıksal bağ TRA-RES'e; kriptografik imza ayrı, isteğe bağlı L5+ madde |
| IDE-DWN | Identity propagation | L4 | Downstream kimlik bağlamını alır | — | Entegrasyon başına ölçülebilir; "alınır **ve loglanır**" |
| BEH-ING | Schema & policy valid. | L2 | Şema ve içerik politikasına uymayan reddedilir | UND ("content policy") | Şema doğrulama + ret kaydı |
| BEH-STO | Integrity enforcement | L2 | Bozuk/tutarsız kayıt alarm + karantina | — | RAG korpusu bütünlüğü (beklenmeyen değişiklik) olarak yorumla |
| BEH-PRM | Violation detection | L3 | Prompt kural setine göre değerlendirilir, bloklanır | UND (kural seti) | Yazılı davranış politikası + otomatik kontrol + bilinen-ihlal testi; injection buraya |
| BEH-INF | Output scope constraint | L3 | Kapsam dışı üretim tamamlanmadan kesilir | TOOL (streaming), OVL (BEH-RES) | BEH-RES ile birleştirme adayı |
| BEH-RES | Output classification | L3 | Yanıt politikaya göre sınıflanır, filtrelenir/escalate | eksik: escalation | Eşikler tanımlı + escalation G-OVS'ye bağlı |
| BEH-DWN | Post-response monitoring | L5 | Downstream kullanım izlenir, anomali incelemesi | **LVL** | Seviye metinleri drift izlemeyi L3'te istiyor, hücre L5 |
| TRA-ING | Provenance logging | L1 | Her öğe kaynak/zaman/sınıf ile immutable loglanır | UND ("tamper-evident") | Kurcalamaya dayanıklılık için ölçüt: append-only + ayrı yetki + bütünlük doğrulaması |
| TRA-STO | Versioned lineage | L1 | Ham veriden checkpoint'e lineage | **SOV** | CE'de: model sürüm kimliği + RAG korpus sürümü |
| TRA-PRM | Prompt audit record | L2 | Prompt kimlik, oturum, sistem prompt sürümüyle saklanır | çatışma (HYG-STO) | Log saklama süresi ve log içindeki PII muamelesi maddenin parçası |
| TRA-INF | Decision parameter log | L2 | "Aynı koşulları üretmeye yeterli" | ABS | LLM'de birebir yeniden üretim yok → "koşulların yeniden kurulabilmesi" |
| TRA-RES | Response context link | L3 | Yanıt prompt, model, kimlik, parametreye bağlı | OVL (IDE-RES, ATT-RES) | Üçlü çakışmanın merkezi; IDE-RES'in mantıksal bağı buraya |
| TRA-DWN | Output usage tracking | L4 | Sınır ötesi kullanım da kayıtlı | ABS | Sınırı geçiş anı ile sınırla |
| ATT-ING | Source compliance | L4 | Tedarikçi DPA + container CVE taraması | CMP | Tedarikçi kısmı **G-SUP**'a; zafiyet yönetimi ayrı madde (bugün hiçbir hücrede yok) |
| ATT-STO | Storage ctrl evidence | L4 | Depolama kontrollerinin denetçiye sunulabilir kanıtı | META | Kanıt paketi maddesi: CON/IDE-STO kanıtları güncel ve tek yerde |
| ATT-PRM | Prompt gov. evidence | L5 | Prompt kontrolleri test ediliyor, istisnalar kapatılıyor | META | İstisna kaydı + kapanış takibi |
| ATT-INF | Model documentation | L5 | Model/system card, risk sınıfı, intended use | **LVL**, OVL (G) | Model card burada; risk sınıflandırması G-RSK'ye |
| ATT-RES | Output audit reconstruct | L5 | Geçmiş her çıktı yeniden kurulabilir | OVL (TRA-RES) | Örneklem testi (L6 artefaktındaki "10 karar") → iyi ölçülebilir madde |
| ATT-DWN | E2E compliance proof | L6 | "Formal sertifikasyona yeterli" kanıt | META, dil | Yeterliliğe denetçi karar verir → "kanıt paketi kontrol listesine göre eksiksiz" |

## 2. Çapraz bulgular

1. **Seviye sayıları tutarsız.** Aktivasyon tablosundan sayınca kümülatif aktif hücre: L0 **3** · L1 **10** · L2 **19** · L3 **26** · L4 **31** · L5 **35** · L6 **36**. Genel bakış metni ise 4 · 16 · 27 · 33 · 36 · 36 · 36 diyor ve "L4'te 36 kontrolün hepsi aktif" iddia ediyor; tabloda 5 hücre L5–L6'da. v1.0'da seviye madde düzeyinde tanımlanacağı için bu sayılar kaynaktan üretilmeli, elle yazılmamalı.
2. **Seviye metinleri hiçbir hücrede olmayan kontroller istiyor:** TLS/in-transit şifreleme, **encryption at rest**, secret yönetimi, ağ segmentasyonu (kısmen CON-STO), **zafiyet/CVE yönetimi**, DSAR/rıza akışları, insan escalation yolu, bias değerlendirmesi, veri yerleşimi doğrulaması, yurt dışı aktarım mekanizması. → Teknik olanlar ilgili hücrelere madde olarak, organizasyonel olanlar G bloğuna.
3. **İki seviye tanımı birbirini tutmuyor.** Bölüm 1.5 (Overview) ile 2.2 (Matrix) aynı seviyeleri farklı anlatıyor: model card, bias denetimi ve veri yerleşimi 2.2'de L4, 1.5'te L5; drift izleme seviye metninde L3, hücrede (BEH-DWN) L5.
4. **Profil sorunu (Y-6) tek hücrede değil, dağınık.** CON-INF, TRA-STO, CON-STO doğrudan SOV varsayıyor; HYG-PRM ise CE için seviye olarak geç kalıyor (L2) — CE profilinde verinin kurumdan çıktığı nokta prompt'tur.
5. **Agentic kullanım kapsanmıyor.** Model adına aksiyon alan sistemler (tool call, e-posta, kayıt yazma) yalnız CON-RES'te dolaylı. Ayrı madde gerekir.
6. **Yanıt tarafında üçlü çakışma:** IDE-RES · TRA-RES · ATT-RES aynı şeyi (yanıtın bağlamıyla yeniden kurulması) üç açıdan söylüyor. Öneri: bağ TRA-RES'te, yeniden kurma testi ATT-RES'te, kriptografik imza isteğe bağlı ayrı madde.
7. **Attestation satırı kontrol değil kanıt.** ATT maddeleri "diğer satırların kanıtı güncel, test edilmiş, tek yerde" diye yazılmalı; aksi hâlde aynı eksik iki kez puan kaybettirir.
8. **Denetim dili.** Stack guide'daki "✓ Now claimable: …" ifadeleri güven zinciriyle çelişiyor → "supports readiness for …".
9. **Regülasyon eşlemesi seviye düzeyinde, madde düzeyinde değil.** v1.0'da eşleme madde başına ve madde/fıkra düzeyinde yapılır; seviye eşlemesi kaynaktan türetilir.
