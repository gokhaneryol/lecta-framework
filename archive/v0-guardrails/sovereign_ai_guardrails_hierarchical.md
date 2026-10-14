# Sovereign AI Guardrails — Hiyerarşik Okunabilir İçerik

Bu Markdown dosyası, üç interaktif HTML belgesindeki gömülü içeriklerin hiyerarşik ve okunabilir biçimde derlenmiş halidir.

Kaynak HTML belgeleri: `Sovereign-AI-Guardrails_Overview`, `Sovereign-AI-Guardrails-Maturity_Matrix`, `Sovereign-AI-Regulatory_Convergence_Map`.


## 1. Sovereign AI Guardrails Overview

### 1.1. Çerçeve özeti

- Kapsam: Privacy-preserving framework · Turkey / EU / UK / US regulatory horizon
- Kontrol sayısı: 36
- Olgunluk aralığı: L0 → L6
- Regülasyon / framework kapsamı: 24 framework

### 1.2. Pipeline aşamaları

Ingestion, Storage, Prompt, Inference, Response, Downstream

### 1.3. Concern katmanları

Containment, Hygiene, Identity, Behaviour, Traceability, Attestation

### 1.4. Concern × Stage aktivasyon seviyeleri

| Concern | Ingestion | Storage | Prompt | Inference | Response | Downstream |
|---|---|---|---|---|---|---|
| Containment | L0 | L0 | L1 | L1 | L2 | L3 |
| Hygiene | L1 | L1 | L2 | L3 | L2 | L4 |
| Identity | L0 | L1 | L2 | L2 | L3 | L4 |
| Behaviour | L2 | L2 | L3 | L3 | L3 | L5 |
| Traceability | L1 | L1 | L2 | L2 | L3 | L4 |
| Attestation | L4 | L4 | L5 | L5 | L5 | L6 |

### 1.5. Olgunluk seviyeleri — genel görünüm

#### L0 — Infrastructure baseline
- Aktif kontrol: 4/36
- Yeni kontrol: 4
- Açıklama: Container perimeter defined and enforced. TLS throughout. Source authentication at all entry points. Network segmentation active. Nothing communicates outside the boundary by default.
- Gate: Container perimeter, TLS, and source authentication active. No data processing begins before this level.
- Regülasyonlar: ISO 27001 A.8, HIPAA §164.312 baseline, SOC 2 CC6.6, GDPR Art.32, NIS2 Art.21

#### L1 — Privacy foundation
- Aktif kontrol: 16/36
- Yeni kontrol: 12
- Açıklama: All model inference runs locally — no external API calls. Encryption at rest enforced on all storage. PII detected and redacted at ingestion. Immutable audit log and dataset versioning initialised.
- Gate: Sovereign data boundary active. Raw personal data does not persist beyond the ingestion stage.
- Regülasyonlar: GDPR Art.32, UK GDPR Art.32, KVKK Art.12, HIPAA encryption, CCPA/CPRA baseline, PIPL Art.51, DPDP Act 2023 Art.8

#### L2 — Access & audit
- Aktif kontrol: 27/36
- Yeni kontrol: 11
- Açıklama: RBAC enforced at every pipeline stage via OPA and Keycloak. Immutable prompt and response logging via Langfuse, bound to session identity. Schema validation gates ingestion. Model lineage fully tracked via MLflow and DVC.
- Gate: No pipeline stage accessible without a validated identity token. Audit trail active and searchable.
- Regülasyonlar: GDPR Art.30, SOC 2 CC6–CC7, HIPAA access ctrl, ISO 27001 A.9, NIS2 Art.21, DORA Art.9, PCI DSS Req.7/8/10, KVKK Art.12

#### L3 — Behavioural controls
- Aktif kontrol: 33/36
- Yeni kontrol: 6
- Açıklama: Input guardrails active — NeMo Guardrails and LLM Guard scan every prompt before inference. Output classification via Detoxify and LLM Guard filters responses before delivery. Evidently AI monitors drift. Human escalation path must be defined architecturally at this level.
- Gate: Behavioural policy enforced at both pipeline boundaries. Drift monitoring active.
- Regülasyonlar: EU AI Act Art.52, HIPAA admin safeguards, SOC 2 CC8, NIST AI RMF, ISO/IEC 42001 baseline, FFIEC guidance

#### L4 — Compliance operationalisation
- Aktif kontrol: 36/36
- Yeni kontrol: 3
- Açıklama: All 36 controls active. CVE scanning gates every container deployment via Trivy. Infrastructure compliance benchmarked via OpenSCAP. Clean handoff enforced on all downstream data. Identity context propagated via Istio. Attestation evidence collection begins.
- Gate: All technical controls active. Earliest point at which a SOC 2 Type II evidence period can meaningfully begin.
- Regülasyonlar: GDPR DSAR technical foundation, SOC 2 Type II evidence period begins, EU AI Act limited risk — full, KVKK Art.11, CCPA/CPRA consumer rights, ISO 27001 operational controls, PDPA Singapore, APPI Japan

#### L5 — Sector & geo compliance
- Aktif kontrol: 36/36
- Yeni teknik kontrol: yok; evidence artefacts seviyesi
- Koşul: sector-conditional
- Açıklama: No new tools deployed. Satisfied by evidence artefacts: AI risk classification, model cards, human oversight procedure, sector agreements (BAAs / DORA register entries), cross-border transfer mechanisms documented, bias assessment conducted, data residency verified by egress audit.
- Gate: Required for healthcare, financial services, and public-sector deployments. Evidence artefacts, not additional controls.
- Regülasyonlar: EU AI Act Art.9–15 high-risk, HIPAA full + BAAs, DORA Art.30, NIS2 essential entity, APRA CPS 234, PIPL full + cross-border, DPDP Act 2023 full, FedRAMP Moderate

#### L6 — Certification & attestation
- Aktif kontrol: 36/36
- Yeni teknik kontrol: yok; evidence artefacts seviyesi
- Açıklama: No new tools deployed. Requires building an evidence aggregation pipeline across Langfuse, MLflow, Trivy, and OpenSCAP. Produces documentation sufficient for third-party audit: SOC 2 Type II scope, ISO 27001 ISMS package, ISO 42001 AI management docs, EU AI Act Art.43 technical file, independent penetration test report.
- Gate: Third-party verifiable evidence package covering the full pipeline. Maintenance: annual re-assessment required.
- Regülasyonlar: SOC 2 Type II audit report, ISO/IEC 27001 certification, ISO/IEC 42001 certification, EU AI Act Art.43 conformity, FedRAMP High, HITRUST r2, PCI DSS QSA


## 2. Sovereign AI Guardrails — Maturity Matrix

### 2.1. Matrix mantığı

Axis A yatayda veri akış aşamalarını, Axis B dikeyde concern derinliğini gösterir. Her hücre, ilgili fonksiyonun hangi olgunluk seviyesinde aktifleştiğini, açıklamasını, araçlarını ve regülasyon sürücülerini içerir.

### 2.2. Seviyeler

#### L0 — Infrastructure baseline
Container perimeter defined and enforced. TLS throughout. Source authentication at all entry points. Network segmentation in place. Nothing runs or communicates outside the container boundary.

Regulatory frameworks addressed:
- ISO 27001 A.8 (network controls)
- HIPAA §164.312 (technical safeguards baseline)
- NIS2 Art.21 (security baseline)
- SOC 2 CC6.6 (logical access)
- GDPR Art.32 (appropriate measures)

#### L1 — Privacy foundation
All model serving is local — no data sent to external APIs. Encryption at rest and in transit. PII detected and redacted at ingestion. Basic immutable audit log active. Sovereign data boundary enforced.

Regulatory frameworks addressed:
- GDPR Art.32 (encryption, pseudonymisation)
- UK GDPR Art.32
- KVKK Art.12 (technical measures)
- HIPAA §164.312(a)(2)(iv) (encryption)
- CCPA/CPRA (data security, minimisation)
- LGPD Art.46 (security measures)
- PIPL Art.51 (personal data security)
- DPDP Act 2023 Art.8 (data fiduciary obligations)
- Privacy Act APP 11 (Australia)

#### L2 — Access & audit
RBAC enforced at every pipeline stage. Immutable, searchable audit trail active. Model and dataset versioning enforced. Data lineage tracked. Session attribution for all prompts. Schema validation at ingestion.

Regulatory frameworks addressed:
- GDPR Art.30 (records of processing)
- SOC 2 CC6–CC7 (access & change management)
- HIPAA §164.312 (access control, audit controls)
- ISO 27001 A.9 (access control)
- NIS2 Art.21 (access management)
- DORA Art.9 (ICT security)
- PCI DSS Req.7/8/10 (access & logging)
- PIPEDA Principle 7 (safeguards)
- KVKK Art.12 (access controls)

#### L3 — Behavioural controls
Input and output guardrails active — policy violation detection, output classification and filtering. Model drift and quality monitoring running. Human-review escalation paths defined and tested.

Regulatory frameworks addressed:
- EU AI Act Art.52 (limited risk transparency)
- HIPAA §164.308 (administrative safeguards)
- SOC 2 CC8 (change management)
- NIST AI RMF (GOVERN, MAP functions)
- ISO/IEC 42001 (AI management baseline)
- FDA 21 CFR Part 11 (audit trails, where applicable)
- FFIEC IT examination guidance
- HITRUST CSF (partial coverage)

#### L4 — Compliance operationalisation
Consent management and DSAR workflows operational. Model cards and FactSheets in place. Bias and fairness audits conducted. CVE scanning on containers. Data residency enforced. Attestation evidence collection begins.

Regulatory frameworks addressed:
- GDPR Art.15–22 (data subject rights + DSAR)
- GDPR Art.22 (automated decision-making)
- SOC 2 Type II (evidence collection)
- EU AI Act limited risk (full)
- KVKK Art.11 (data subject rights)
- CCPA/CPRA (consumer rights)
- LGPD Art.18 (data subject rights)
- PDPA Singapore
- APPI Japan
- ISO 27001 (operational controls complete)

#### L5 — Sector & geo compliance
Formal AI risk classification assigned. Sector-specific controls activated (healthcare, finance, public sector). Cross-border transfer safeguards in place. Human oversight mechanisms documented and tested.

Regulatory frameworks addressed:
- EU AI Act Art.9–15 (high-risk requirements)
- HIPAA full safeguards + BAAs
- DORA Art.30 (third-party ICT risk)
- NIS2 (essential entity full compliance)
- APRA CPS 234 (Australia financial)
- PIPL full + cross-border controls (China)
- DPDP Act 2023 full (India)
- FedRAMP Moderate
- ISO 27001 certification track
- HITRUST r2 (partial assessment)

#### L6 — Certification & attestation
Complete third-party audit evidence across all pipeline stages. Conformity assessment documentation produced. Continuous compliance posture with automated evidence collection. Ready for formal certification.

Regulatory frameworks addressed:
- SOC 2 Type II audit report
- ISO/IEC 27001 certification
- ISO/IEC 42001 (AI Management) certification
- EU AI Act Art.43 (conformity assessment)
- FedRAMP High authorization
- HITRUST r2 certification
- PCI DSS QSA assessment

### 2.3. 36 kontrol hücresi

#### Containment
| Stage | Function | Level | Description | Primary tools | Alternative tools | Notes |
|---|---|---:|---|---|---|---|
| Ingestion | Source boundary | L0 | Enforce strict perimeter at data entry. Only approved sources, formats, and protocols may supply data. Unapproved inputs are rejected before any processing occurs. | envoy, cilium | traefik | composed |
| Storage | Store isolation | L0 | Prevent cross-tenant and cross-context access in storage. Network segmentation between data stores ensures no component can reach beyond its authorised scope. | cilium, opa | — | composed |
| Prompt | Input surface restrict. | L1 | Constrain the prompt interface to validated templates only. No arbitrary code execution paths. Injection surface is minimised by design — not configuration. | envoy, pydantic | kong | composed |
| Inference | Execution air-gap | L1 | Model execution environment is isolated from external networks. Model weights, intermediate activations, and outputs cannot be exfiltrated during inference. | istio, cilium | — | composed |
| Response | Output channel control | L2 | Only sanctioned output channels are available. No unsolicited writes to external APIs, file systems, or communication channels are physically possible. | envoy, opa | — | composed |
| Downstream | Egress governance | L3 | All data leaving the system post-response is logged, classified, and controlled. Downstream re-transmission to any external party requires explicit authorisation. | opa, falco | — | composed |

#### Hygiene
| Stage | Function | Level | Description | Primary tools | Alternative tools | Notes |
|---|---|---:|---|---|---|---|
| Ingestion | PII detect & redact | L1 | Scan every ingested data item for personal identifiers and sensitive categories. Redact, mask, or synthesise before data enters the pipeline. No raw PII proceeds further. | presidio | spacy | — |
| Storage | Data minimisation | L1 | Retain only what is necessary and proportionate for the stated task. Enforce automated purge schedules. Restrict storage of raw personal data beyond immediate need. | — | atlas | tooling emerging; No dedicated OSS tool covers automated data minimisation end-to-end. Implement via K8s CronJob retention policies and storage-level TTL rules. Apache Atlas provides data lifecycle governance at significant operational cost. |
| Prompt | Prompt sanitisation | L2 | Strip injected instructions, sensitive content patterns, and disallowed constructs from user-supplied prompt text before it reaches the model context window. | llmguard | presidio, rebuff | composed |
| Inference | Input integrity check | L3 | Validate that model inputs conform to expected shape, type, and value ranges. Detect adversarial perturbations or malformed inputs that could compromise inference integrity. | pydantic, llmguard | rebuff | composed |
| Response | Output PII scrubbing | L2 | Detect and remove personal data the model may have reproduced or hallucinated in its response. Applied as a post-generation filter before delivery to the user. | presidio, llmguard | — | composed |
| Downstream | Clean handoff | L4 | Verify that data passed to downstream consumers contains no residual sensitive content beyond what is explicitly authorised for that consumer and context. | presidio, opa | — | composed |

#### Identity
| Stage | Function | Level | Description | Primary tools | Alternative tools | Notes |
|---|---|---:|---|---|---|---|
| Ingestion | Source authentication | L0 | Every data source must present verifiable credentials at ingestion. Unauthenticated or unrecognised sources are rejected without processing. Provenance is logged. | keycloak | authelia | — |
| Storage | Artefact access ctrl | L1 | Datasets, model weights, checkpoints, and pipeline artefacts are access-controlled by role. No unauthenticated reads, writes, or copies are permitted. | keycloak, infisical | vault | composed |
| Prompt | Session attribution | L2 | Every prompt is bound to an authenticated user or service identity with a verifiable session token. Anonymous prompts are not permitted in regulated contexts. | keycloak | authelia | composed |
| Inference | Role-based model access | L2 | Model capabilities and data scope are constrained to what the requesting identity's role authorises during inference. No capability escalation is possible at runtime. | opa, keycloak | — | composed |
| Response | Response binding | L3 | Each generated response is logically or cryptographically bound to the requesting identity, enabling non-repudiation and accountability in case of dispute. | keycloak | — | composed; tooling emerging; Cryptographic response binding — no standard OSS solution exists. Requires a custom signing service that anchors each response to Keycloak-issued identity tokens. Tooling in this space is emerging. |
| Downstream | Identity propagation | L4 | Downstream consuming systems receive the identity context of the originating request, preserving accountability across integration boundaries and third-party handoffs. | keycloak, istio | — | composed |

#### Behaviour
| Stage | Function | Level | Description | Primary tools | Alternative tools | Notes |
|---|---|---:|---|---|---|---|
| Ingestion | Schema & policy valid. | L2 | Ingested data must conform to defined schemas and pass content policy checks at the gate. Violations are rejected before entering the pipeline and logged for review. | greatexp | pydantic | — |
| Storage | Integrity enforcement | L2 | Data quality rules are enforced in storage: corrupt, inconsistent, or policy-violating records trigger alerts and quarantine. No bad data silently persists. | greatexp | deequ | composed |
| Prompt | Violation detection | L3 | Prompts are evaluated against a rule set covering disallowed topics, harmful instructions, and policy-violating patterns. Violations are blocked and flagged before inference. | nemo, llmguard | rebuff | composed |
| Inference | Output scope constraint | L3 | Model inference is constrained to the permitted topic, content, and format scope defined for this deployment. Out-of-scope generation is intercepted before completion. | nemo | llmguard | — |
| Response | Output classification | L3 | Generated responses are classified against the behavioural policy. Outputs that fail — toxic, disallowed, or out-of-scope — are filtered or escalated before delivery. | llmguard | detoxify | composed |
| Downstream | Post-response monitoring | L5 | Downstream use of model outputs is monitored for policy compliance. Anomalous patterns, abuse signals, or unexpected downstream effects trigger automated review. | evidently, prometheus | — | composed |

#### Traceability
| Stage | Function | Level | Description | Primary tools | Alternative tools | Notes |
|---|---|---:|---|---|---|---|
| Ingestion | Provenance logging | L1 | Every data item entering the pipeline is logged with source, timestamp, format, classification, and transformations applied. The log is immutable and tamper-evident. | otel, opensearch | loki | composed; Grafana Loki is AGPL 3.0. It is listed as an alternative but its licence must be reviewed before use. OpenSearch (Apache 2.0) is the recommended primary log sink. |
| Storage | Versioned lineage | L1 | Datasets and model artefacts are version-controlled with full lineage. The complete chain from raw data source to trained model checkpoint is reconstructible at any point. | dvc, mlflow | — | composed |
| Prompt | Prompt audit record | L2 | All prompts are stored with user identity, session ID, timestamp, system prompt version, and provided context. Records are immutable and retained per data policy. | langfuse | — | composed |
| Inference | Decision parameter log | L2 | Model version, inference config, sampling parameters, and retrieval context are logged for every call — sufficient to reproduce the exact conditions of any decision. | mlflow, otel | — | composed |
| Response | Response context link | L3 | Each stored response is linked to its prompt, model version, user identity, and inference parameters, enabling full reconstruction of any individual decision post-hoc. | langfuse, mlflow | — | composed |
| Downstream | Output usage tracking | L4 | How, when, and by whom model outputs are accessed, forwarded, or acted upon downstream is recorded, extending accountability beyond the system boundary. | otel | — | composed; tooling emerging; Tracking downstream consumption beyond the system boundary is architecturally complex. OpenTelemetry instruments events within the boundary; external tracking requires custom capture at each consumer integration point. No dedicated OSS solution covers this fully. |

#### Attestation
| Stage | Function | Level | Description | Primary tools | Alternative tools | Notes |
|---|---|---:|---|---|---|---|
| Ingestion | Source compliance | L4 | Data sources are assessed for compliance before onboarding. Supplier compliance status, DPAs, and transfer legitimacy are verified and re-assessed periodically. | trivy | openscap | composed; tooling emerging; Container and infrastructure compliance is covered by Trivy and OpenSCAP. Supplier DPA verification and transfer legitimacy assessment remain largely manual — no OSS tool automates this reliably yet. |
| Storage | Storage ctrl evidence | L4 | Auditable, documented evidence that all storage security controls are implemented, tested, and operating as specified — suitable for presentation to external auditors. | trivy, openscap | — | composed |
| Prompt | Prompt gov. evidence | L5 | Auditable records demonstrating that prompt governance controls exist, are actively tested, exceptions are investigated, and remediation is tracked to closure. | langfuse | — | composed; tooling emerging; Langfuse provides the audit export foundation. Auditor-ready evidence packaging and exception tracking require a custom collection pipeline — no OSS standard for this evidence format exists yet. |
| Inference | Model documentation | L5 | Model cards, system cards, risk classification assessments, and intended use documentation are produced, maintained, and accessible to regulators and auditors. | mlflow | — | composed; tooling emerging; MLflow Model Registry provides versioned metadata. Model cards, risk classification, and ISO/IEC 42001-compliant FactSheet documentation require custom templates — tooling in this area is still emerging. |
| Response | Output audit reconstruct | L5 | Any past model output can be fully reconstructed from stored records — with full context, identity, model state, and parameters — enabling post-hoc audit of decisions. | langfuse, mlflow | — | composed; tooling emerging |
| Downstream | E2E compliance proof | L6 | Third-party verifiable evidence covering the full pipeline from ingestion to downstream — sufficient for formal certification, regulatory inspection, and conformity assessment. | — | — | composed; tooling emerging; Function defined, tooling emerging. No single OSS solution covers full pipeline attestation. Requires a custom evidence aggregator across Langfuse, MLflow, Trivy and OpenSCAP outputs, formatted for third-party audit consumption. |

### 2.4. Tool registry

| Tool | Licence | Status | Weight | Description | Licence warning |
|---|---|---|---|---|---|
| Apache Atlas | Apache 2.0 | Approved | H | Data governance platform — lineage tracking, classification and data lifecycle management | — |
| Apache Deequ | Apache 2.0 | Approved | M | Spark-based data quality constraints — integrity checking for large-scale datasets | — |
| Authelia | Apache 2.0 | Approved | L | Lightweight SSO and MFA — simpler self-hosted alternative to Keycloak | — |
| Cilium | Apache 2.0 | Approved | M | eBPF-based network security — L3/L4/L7 policy enforcement between containers | — |
| Detoxify | MIT | Approved | L | ML-based toxicity classifier for output screening and content policy enforcement | — |
| DVC | Apache 2.0 | Approved | L | Data version control — dataset and ML pipeline versioning with pluggable storage backends | — |
| Envoy Proxy | Apache 2.0 | Approved | L | L7 proxy and API gateway — traffic control, rate limiting, mTLS, egress enforcement | — |
| Evidently AI | Apache 2.0 | Approved | M | ML monitoring — data drift detection, model quality tracking, output distribution analysis | — |
| Falco | Apache 2.0 | Approved | L | Runtime security — detects unexpected container behaviour, file access, network egress | — |
| Grafana Loki | AGPL 3.0 | Flagged | M | Log aggregation and query engine — structured log storage with LogQL query language | AGPL 3.0 — requires source disclosure for all networked service deployments. Use OpenSearch as the primary log sink to avoid this obligation. |
| Great Expectations | Apache 2.0 | Approved | M | Data quality validation — schema, type, value range and statistical expectation testing | — |
| HashiCorp Vault | BSL 1.1 | Flagged | M | Secrets management — dynamic credentials, encryption-as-a-service, PKI | BSL 1.1 — commercial production deployment requires a HashiCorp licence. Evaluate Infisical (MIT) as an open alternative. |
| Infisical | MIT | Approved | M | Open-source secrets management — self-hostable, MIT-licensed alternative to Vault | — |
| Istio | Apache 2.0 | Approved | H | Service mesh — mutual TLS between all services, traffic policy, full observability | — |
| Keycloak | Apache 2.0 | Approved | M | Identity and access management — OIDC, SAML, RBAC, session tokens, MFA | — |
| Kong OSS | Apache 2.0 | Approved | M | API gateway with plugin ecosystem — request validation, rate limiting, authentication | — |
| Langfuse | MIT | Approved | M | LLM observability — prompt and response logging, session tracing, evaluation and cost tracking | — |
| LLM Guard | MIT | Approved | L | Input and output scanning — PII, toxicity, prompt injection and data leakage detection | — |
| MLflow | Apache 2.0 | Approved | M | ML lifecycle management — experiment tracking, model registry, lineage, parameter logging | — |
| MS Presidio | MIT | Approved | L | PII detection and anonymisation — identifies and redacts personal identifiers in text | — |
| NeMo Guardrails | Apache 2.0 | Approved | M | Programmable LLM guardrails — topic restrictions, safety rails, dialogue flow control | — |
| Open Policy Agent | Apache 2.0 | Approved | L | Policy-as-code engine — authorisation and policy enforcement at any pipeline layer | — |
| OpenSCAP | LGPL 2.1 | Flagged | L | Infrastructure compliance scanning against CIS benchmarks, NIST and STIG profiles | LGPL 2.1 — dynamic linking restrictions apply; review terms carefully before packaging in a commercial product. |
| OpenSearch | Apache 2.0 | Approved | H | Apache 2.0 log and search store — community fork of Elasticsearch; full API compatibility retained | — |
| OpenTelemetry | Apache 2.0 | Approved | L | Vendor-neutral observability SDK — distributed traces, metrics and structured logs across the stack | — |
| Prometheus | Apache 2.0 | Approved | L | Metrics collection and alerting — standard observability backend for infrastructure and apps | — |
| Pydantic | MIT | Approved | L | Python data validation — schema and type enforcement at API and pipeline boundaries | — |
| Rebuff | MIT | Approved | L | Prompt injection detection via heuristics, vector similarity and canary token signals | — |
| spaCy | MIT | Approved | L | NLP library — custom NER pipelines for domain-specific PII detection and classification | — |
| Traefik | MIT | Approved | L | Edge router and reverse proxy — simpler ingress control alternative to Envoy | — |
| Trivy | Apache 2.0 | Approved | L | Container and filesystem scanner — CVEs, misconfigurations, licence compliance across images | — |

### 2.5. Regulatory frameworks reference — 24 framework

#### European
| Framework | Full name | Geography / sector | Minimum level | Full level | Note |
|---|---|---|---:|---:|---|
| GDPR | General Data Protection Regulation | EU / EEA | L1 | L4 | Data subject rights, security measures Art.32, automated decisions Art.22 |
| UK GDPR / DPA 2018 | UK General Data Protection Regulation | United Kingdom | L1 | L4 | Post-Brexit equivalent; same technical safeguard requirements |
| EU AI Act | EU Artificial Intelligence Act | EU | L3 | L6 | Risk-tiered: limited risk L3–4, high risk L5–6, GPAI additional obligations |
| NIS2 | Network & Information Security Directive 2 | EU | L2 | L5 | Cybersecurity for essential/important entities; incident reporting, supply chain |
| DORA | Digital Operational Resilience Act | EU — Financial | L2 | L5 | ICT risk management, resilience testing, third-party provider oversight |
| KVKK | Kişisel Verileri Koruma Kanunu | Turkey | L1 | L4 | Turkish personal data law; mirrors GDPR structure with local obligations |

#### North American
| Framework | Full name | Geography / sector | Minimum level | Full level | Note |
|---|---|---|---:|---:|---|
| HIPAA | Health Insurance Portability and Accountability Act | USA — Healthcare | L1 | L5 | PHI protection; technical, physical and admin safeguards; BAAs required |
| CCPA / CPRA | California Consumer Privacy Act / Privacy Rights Act | USA — California | L1 | L4 | Consumer data rights; opt-out of sale; sensitive data category restrictions |
| PIPEDA / Law 25 | Personal Information Protection and Electronic Documents Act | Canada | L1 | L4 | Federal privacy law; Québec Law 25 significantly strengthens requirements |
| FedRAMP | Federal Risk and Authorization Management Program | USA — Federal | L2 | L6 | Cloud services for US federal agencies; Moderate and High authorization tiers |
| FFIEC | Federal Financial Institutions Examination Council | USA — Banking | L2 | L5 | IT examination guidelines for financial institutions; AI/ML guidance emerging |
| PCI DSS | Payment Card Industry Data Security Standard | Global — Payments | L2 | L5 | Cardholder data protection; access ctrl, audit logging, encryption, vuln. mgmt |

#### Asia-Pacific
| Framework | Full name | Geography / sector | Minimum level | Full level | Note |
|---|---|---|---:|---:|---|
| PIPL | Personal Information Protection Law | China | L1 | L5 | Strict cross-border transfer restrictions; consent and purpose limitation |
| DPDP Act 2023 | Digital Personal Data Protection Act | India | L1 | L5 | India's first comprehensive data protection law; significant fiduciary obligations |
| PDPA | Personal Data Protection Act | Singapore / Thailand | L1 | L4 | Both countries have PDPAs with overlapping but distinct requirements |
| APPI | Act on the Protection of Personal Information | Japan | L1 | L4 | Third-party transfer restrictions; anonymisation and pseudonymisation provisions |
| Privacy Act / APPs | Privacy Act 1988 + Australian Privacy Principles | Australia | L1 | L4 | Federal privacy law; review underway to strengthen AI-related provisions |
| APRA CPS 234 | Prudential Standard CPS 234 | Australia — Financial | L2 | L5 | Information security requirements for APRA-regulated financial entities |

#### Global Standards & Sector
| Framework | Full name | Geography / sector | Minimum level | Full level | Note |
|---|---|---|---:|---:|---|
| ISO/IEC 27001 | Information Security Management System | Global standard | L2 | L6 | Risk-based ISMS; certification via accredited third-party auditor |
| ISO/IEC 42001 | AI Management System Standard | Global standard | L3 | L6 | 2023 standard for responsible AI governance; designed to complement ISO 27001 |
| SOC 2 Type II | System and Organisation Controls 2 | Global (US origin) | L2 | L6 | Trust services criteria: security, availability, confidentiality; annual audit |
| NIST AI RMF | AI Risk Management Framework | USA (voluntary / reference) | L3 | L5 | Govern/Map/Measure/Manage structure; reference for US sector regulation |
| HITRUST CSF | Health Information Trust Alliance CSF | Healthcare — global | L3 | L6 | Harmonises HIPAA, ISO 27001, NIST; widely adopted in US and global healthcare |
| FDA 21 CFR Part 11 | Electronic Records and Electronic Signatures | USA — Pharma / Medical | L3 | L5 | Required for AI/ML in FDA-regulated clinical or manufacturing contexts |

### 2.6. Stack guide — sıralı deployment referansı

Ordered deployment reference per maturity level · architectural and development register · open↑ marks controls that fail open by default and require explicit override

#### L0 — Infrastructure baseline 3 tools · 4 controls activated
Establishes the container perimeter: network segmentation between all pods, TLS at every ingress and service boundary, and source authentication at all entry points. Nothing communicates outside the boundary by default. No data processing begins before this level is complete.

| # | Tool | Role at this level | Validation / failure note |
|---:|---|---|---|
| 1 | Cilium | eBPF network policy — default-deny between all namespaces. Covers L3/L4/L7 enforcement between pods. | open↑ Without an explicit NetworkPolicy, Cilium defaults to allow-all. A cluster-wide default-deny policy must be deployed before any workload starts. |
| 2 | Envoy alt: Traefik | L7 ingress perimeter — mTLS termination, rate limiting, protocol enforcement at the cluster boundary. | open↑ Envoy's default behavior on upstream failure is to return a 503 and pass the connection through. Configure x-envoy-upstream-rq-timeout-ms with an explicit deny action on timeout to fail closed. |
| 3 | Keycloak alt: Authelia | Source authentication — every data source must present a verifiable credential at ingestion. Unauthenticated requests are rejected at the gateway layer. | Fails closed by default when the Keycloak backend is unavailable. Confirm the Envoy ext_authz filter is configured to deny on unreachable auth service. |
| 4 | cert-manager | Automated TLS certificate provisioning and rotation for all internal and external service endpoints. | Verify certificate rotation does not cause downtime — configure a renewal buffer of at least 30% of certificate lifetime. |

Composition / implementation notes:
- ⟳ Source boundary (Containment × Ingestion) is a composed function: Cilium enforces pod-level network policy; Envoy enforces L7 protocol and authentication at the perimeter. A correctly configured Envoy with a misconfigured Cilium policy still permits lateral movement between internal services.

Compliance gate:
- ✓ Now claimable: ISO 27001 A.8 network controls · HIPAA §164.312 technical safeguards baseline · SOC 2 CC6.6 logical access · GDPR Art.32 appropriate technical measures (encryption in transit) · NIS2 Art.21 security baseline
- → Still open: PII protection, encryption at rest, audit logging, RBAC — addressed at L1 and L2

#### L1 — Privacy foundation 7 tools · 16 controls activated
Activates the sovereign data boundary: all model inference runs locally with no external API calls. Encryption at rest is enforced on all storage. PII is detected and redacted at ingestion before any data enters the pipeline. An immutable audit log and dataset versioning are initialised. Raw personal data does not persist beyond the ingestion stage.

| # | Tool | Role at this level | Validation / failure note |
|---:|---|---|---|
| 1 | Ollama / vLLM | Local model serving — all inference stays within the container boundary. No data leaves the cluster for model calls. | Verify no outbound connections from the serving pod: cilium monitor --type drop should show no egress to external CIDRs during inference. |
| 2 | MinIO | Encrypted object storage for model weights, datasets, and pipeline artefacts. Encryption at rest enforced via server-side encryption with locally managed keys. | Enable SSE-S3 or SSE-KMS at bucket creation — it cannot be applied retroactively to existing objects. |
| 3 | Infisical alt: Vault (BSL ⚠) | Secrets management — all credentials, API keys, and encryption keys are stored and injected via Infisical. No secrets in environment variables or config maps. | — |
| 4 | MS Presidio alt: spaCy NER | PII detection and redaction at ingestion — scans every data item for personal identifiers before it enters the pipeline. Raw PII is blocked from proceeding. | open↑ Presidio returns the original text unchanged for entity types not covered by the configured recogniser set. Explicitly enumerate supported languages and entity categories; anything outside that set must be blocked, not passed through. |
| 5 | OpenTelemetry | Structured log and trace collection — instruments every pipeline stage with source, timestamp, classification, and transformation events. | Deploy the OTel Collector as a DaemonSet, not a sidecar, to ensure no gaps during pod restart. |
| 6 | OpenSearch | Immutable log sink — append-only index configuration. Provides tamper-evident provenance logging satisfying the audit baseline. | Configure index lifecycle policy with a read-only phase and disable the delete action on audit indices. |
| 7 | DVC | Dataset version control — all datasets entering the pipeline are versioned with content hashes. Full lineage from raw source begins here. | — |

Composition / implementation notes:
- ⟳ Provenance logging (Traceability × Ingestion) requires OTel + OpenSearch together — OTel captures and structures the events; OpenSearch provides the immutable, queryable store. Either alone does not satisfy the tamper-evident requirement. ⟳ PII detect & redact (Hygiene × Ingestion): single primary tool, but coverage is only as wide as the configured recogniser set. spaCy is recommended as a complementary deployment for domain-specific entity types not covered by Presidio's default models.

Compliance gate:
- ✓ Now claimable: GDPR Art.32 (encryption, pseudonymisation) · UK GDPR Art.32 · KVKK Art.12 technical measures · HIPAA §164.312(a)(2)(iv) encryption · CCPA/CPRA data security baseline · PIPL Art.51 · DPDP Act 2023 Art.8 · Privacy Act APP 11
- → Still open: RBAC, session attribution, schema validation, model versioning — addressed at L2

#### L2 — Access & audit 5 tools · 27 controls activated
Extends Keycloak to enforce RBAC at every pipeline stage and activates policy-as-code enforcement via OPA. Immutable prompt and response logging begins via Langfuse, bound to authenticated session identity. Schema validation gates ingestion. Model and dataset lineage is fully tracked. No pipeline stage is accessible without a validated identity token.

| # | Tool | Role at this level | Validation / failure note |
|---:|---|---|---|
| 1 | Keycloak | Extend existing deployment: configure realm-per-pipeline-stage, define roles for each service identity, enforce RBAC on all internal service endpoints. Session tokens issued per prompt. | Fails closed when Keycloak is unavailable — confirm all downstream services return 401 (not 500) during a Keycloak restart. |
| 2 | Open Policy Agent | Policy-as-code enforcement — evaluates authorisation decisions at every pipeline boundary. Decouples policy from application code. | open↑ OPA's default decision when no policy matches is undefined (not deny). All policies must include an explicit default deny: default allow = false . Verify with a request that matches no rule — it must be rejected. |
| 3 | MLflow | Model registry and experiment tracking — all model versions are registered with provenance, training parameters, and lineage. Completes the chain from DVC-versioned data to deployed checkpoint. | — |
| 4 | Langfuse | Prompt and response logging — every prompt is stored with session ID, user identity (from Keycloak token), timestamp, and system prompt version. Records are append-only. | Bind Keycloak-issued JWT to each Langfuse trace at capture time — do not rely on post-hoc correlation. Without this binding, traceability requirements at L3+ cannot be satisfied. |
| 5 | Great Expectations alt: Apache Deequ | Schema and data quality validation at ingestion — type, range, and constraint checks gate data entry. Violations are logged and rejected. | open↑ Great Expectations logs validation failures but does not block pipeline execution by default. Configure action_list with a StoreValidationResultAction and an explicit pipeline halt on critical expectation failure. |

Composition / implementation notes:
- ⟳ Role-based model access (Identity × Inference) requires OPA + Keycloak — Keycloak issues the identity token encoding the user's roles; OPA evaluates the policy against that token to determine permitted model capabilities and data scope. OPA alone has no identity; Keycloak alone has no policy engine. ⟳ Session attribution (Identity × Prompt) requires Keycloak + Langfuse — the session token from Keycloak must be injected into every Langfuse trace at capture time. These are two separate services with no native integration; the binding must be implemented in the prompt handling layer.

Compliance gate:
- ✓ Now claimable: GDPR Art.30 records of processing · SOC 2 CC6–CC7 access & change management · HIPAA §164.312 access control and audit controls · ISO 27001 A.9 access control · NIS2 Art.21 access management · DORA Art.9 ICT security · PCI DSS Req.7/8/10 · PIPEDA Principle 7 · KVKK Art.12 access controls
- → Still open: behavioural guardrails, output filtering, drift monitoring — addressed at L3

#### L3 — Behavioural controls 5 tools · 33 controls activated
Activates the guardrail layer on both sides of the model. Input scanning detects prompt injection, policy violations, and disallowed content before inference. Output scanning classifies responses against the behavioural policy before delivery. Model drift and output distribution monitoring begins. Human-escalation paths must be defined and tested at this level — this is an architectural decision, not a tooling one.

| # | Tool | Role at this level | Validation / failure note |
|---:|---|---|---|
| 1 | NeMo Guardrails | Programmable topic and dialogue guardrails — enforces allowed topic scope, safety rails, and dialogue flow restrictions at the prompt layer before inference. | open↑ NeMo Guardrails fails open if the rail configuration file is malformed or missing — the model call proceeds without guardrails. Validate rail activation explicitly with a known-violation prompt in each deployment environment; do not infer from absence of errors. |
| 2 | LLM Guard | Input and output content scanning — PII detection, toxicity classification, prompt injection detection, and data leakage scanning applied at both pipeline boundaries. | open↑ LLM Guard's default behavior on scanner timeout is to return the original input/output unchanged. Set raise_error_on_scanner_exception=True and configure the serving layer to treat scanner exceptions as blocks, not warnings. |
| 3 | Rebuff | Prompt injection detection — heuristic, vector similarity, and canary token signals complement LLM Guard's injection scanner with a different detection surface. | Deploy as a secondary scanner, not a replacement for LLM Guard's injection module. Overlap is intentional — the two tools have different false-negative profiles. |
| 4 | Detoxify | Output toxicity classification — ML-based classifier applied as a post-generation filter before response delivery. Catches content that passes LLM Guard's rule-based output scanner. | — |
| 5 | Evidently AI | Model drift and output distribution monitoring — tracks output quality metrics and data drift over time. Feeds alerts into Prometheus. | — |

Composition / implementation notes:
- ⟳ Violation detection (Behaviour × Prompt) requires NeMo + LLM Guard — NeMo enforces topic and dialogue policy at the semantic level; LLM Guard scans content at the token and pattern level. They detect different violation classes; neither alone covers the full behavioural policy surface. ⟳ Output classification (Behaviour × Response) requires LLM Guard + Detoxify — LLM Guard applies rule-based and heuristic filters; Detoxify provides a model-based toxicity score. A response can pass LLM Guard's filters while still scoring above the toxicity threshold. ⟳ Egress governance (Containment × Downstream) requires OPA + Falco — OPA enforces the downstream transmission policy; Falco provides runtime detection of policy violations at the system call level. OPA prevents; Falco detects what prevention missed. ⚠ Human escalation path — no OSS tool covers this. The escalation trigger (which output classes require human review), the review queue, the reviewer role, the SLA, and the disposition action must be defined as an architectural decision before L3 is considered complete. This is a process gap, not a tooling gap.

Compliance gate:
- ✓ Now claimable: EU AI Act Art.52 limited risk transparency · HIPAA §164.308 administrative safeguards baseline · SOC 2 CC8 change management · NIST AI RMF GOVERN and MAP functions · ISO/IEC 42001 AI management baseline · FFIEC IT examination guidance
- → Still open: CVE scanning, model documentation, DSAR workflows, attestation evidence collection — addressed at L4

#### L4 — Compliance operationalisation 4 tools · 36 controls activated
All 36 matrix controls are active at L4. This level adds the compliance operations layer: CVE scanning gates every container deployment, infrastructure compliance is benchmarked, clean data handoff to downstream consumers is enforced, and identity context propagates across integration boundaries. Attestation evidence collection begins — this is the earliest level at which a SOC 2 Type II evidence period can meaningfully start.

| # | Tool | Role at this level | Validation / failure note |
|---:|---|---|---|
| 1 | Trivy | Container and filesystem CVE scanning — integrated as a pre-deploy gate in the CI/CD pipeline. No image with critical or high CVEs is deployed without explicit sign-off. | Configure as a pipeline blocking step, not a reporting step. A scan that produces output but does not block deployment provides no security guarantee. |
| 2 | OpenSCAP LGPL ⚠ | Infrastructure compliance scanning — benchmarks host and node configuration against CIS profiles. Produces auditable evidence of control implementation. | LGPL 2.1 — review dynamic linking terms before packaging in a commercial product. Run as an out-of-band scheduled job, not an inline request-path component, to avoid any linking ambiguity. |
| 3 | Presidio + OPA | Clean handoff enforcement — Presidio scans outbound data for residual PII; OPA enforces the policy gate, blocking transmission if the scan fails or returns findings above threshold. | open↑ This is a composed function: if OPA policy is not explicitly configured to deny on Presidio scan failure (not just on findings), a Presidio service outage silently bypasses the clean handoff check. The OPA policy must treat an unreachable Presidio scanner as a denial condition. |
| 4 | Keycloak + Istio | Identity propagation — Istio carries the Keycloak-issued identity context in service-to-service headers across all downstream integrations, preserving accountability at every boundary. | Verify that downstream consumer services receive and log the propagated identity header — propagation without consumption provides no accountability. |

Composition / implementation notes:
- ⟳ Source compliance (Attestation × Ingestion) requires Trivy + OpenSCAP — Trivy covers the container image layer; OpenSCAP covers the host and node configuration layer. Supplier DPA verification and transfer legitimacy assessment have no OSS tool equivalent and remain manual processes at this level. ⟳ Clean handoff (Hygiene × Downstream) requires Presidio + OPA — see failure posture note above. The composition failure mode here is particularly consequential as it operates at the system boundary.

Compliance gate:
- ✓ Now claimable: GDPR Art.15–22 technical foundation for DSAR (process layer still required) · GDPR Art.22 automated decision-making controls · SOC 2 Type II evidence collection period can begin · EU AI Act limited risk full · KVKK Art.11 data subject rights technical controls · CCPA/CPRA consumer rights infrastructure · ISO 27001 operational controls complete · PDPA Singapore · APPI Japan
- → Still open: formal AI risk classification, sector-specific controls, cross-border transfer mechanisms, human oversight documentation — addressed at L5

#### L5 — Sector & geo compliance evidence artefacts · no new tool deployments
No new tools are deployed at L5. The full 36-control technical stack is already active. This level is satisfied by producing, testing, and maintaining a specific set of organisational and technical evidence artefacts. Sector-specific obligations (healthcare, finance, public sector) and cross-border transfer safeguards are formalised here. The items below are the L5 completion criteria.

Evidence artefacts:
- AI risk classification document — system formally classified against EU AI Act Annex III criteria. Classification rationale documented and signed off by a named responsible person.
- Model card per deployed model — covers intended use, known limitations, training data provenance, performance characteristics, and out-of-scope use cases. Stored in MLflow Model Registry and accessible to reviewers.
- Human oversight procedure — documents which output classes trigger human review, the review queue mechanism, the responsible role, the SLA for disposition, and what happens to the output while pending. Must have been exercised end-to-end at least once.
- Sector-specific agreement in place — healthcare: BAA signed with all relevant parties; financial: DORA third-party ICT risk register entry; public sector: applicable national procurement/security classification applied.
- Cross-border transfer mechanism documented — for each jurisdiction where data originates or is processed: adequacy decision, SCCs, BCRs, or equivalent mechanism is identified, documented, and current.
- Post-response monitoring active and tested — Evidently AI drift alerts configured with defined thresholds, Prometheus alert rules firing correctly, and at least one test alert handled end-to-end through the escalation path.
- Bias and fairness assessment conducted — outputs evaluated for systematic bias across protected characteristic proxies relevant to the deployment context. Findings documented; any remediation tracked to closure.
- Data residency enforcement verified — all personal data confirmed to remain within the designated jurisdiction boundary. Verified by network egress audit (Cilium/Falco logs), not self-declaration.

Compliance gate:
- ✓ Now claimable: EU AI Act Art.9–15 high-risk system requirements · HIPAA full safeguards + BAAs · DORA Art.30 third-party ICT risk · NIS2 essential entity full compliance · APRA CPS 234 · PIPL full + cross-border controls · DPDP Act 2023 full · FedRAMP Moderate (with additional controls)
- → Still open: third-party audit evidence package, conformity assessment documentation, continuous evidence collection pipeline — addressed at L6

#### L6 — Certification & attestation evidence artefacts · audit readiness
No new tools are deployed at L6. This level requires building an evidence aggregation pipeline across the existing tools — Langfuse, MLflow, Trivy, and OpenSCAP — and producing the documentation package sufficient for third-party audit and formal certification. The items below are the L6 completion criteria. Some require external parties; they cannot be self-certified.

Evidence artefacts:
- Continuous evidence collection pipeline — automated aggregation of audit-relevant outputs from Langfuse (prompt/response records), MLflow (model lineage), Trivy (CVE scan results), and OpenSCAP (compliance scan results) into a single queryable evidence store. Pipeline must run on a defined schedule and alert on gaps.
- Audit trail completeness test — sampled reconstruction of at least 10 past decisions from stored records, verifying that each can be fully reconstructed from Langfuse trace + MLflow model version + Keycloak identity + inference parameters alone. Reconstruction log retained as evidence.
- SOC 2 Type II scope document — trust services criteria mapped to specific technical controls in the stack. Evidence collection period of at least 6 months completed. Prepared for presentation to an accredited auditor.
- ISO/IEC 27001 ISMS documentation package — risk register, statement of applicability, risk treatment plan, and internal audit results. Covers the full system boundary including the AI pipeline.
- ISO/IEC 42001 AI management documentation — AI policy, AI risk assessment, AI impact assessment, and intended use documentation. Aligned with the model cards produced at L5.
- EU AI Act technical documentation file — Art.43 conformity assessment documentation: system description, risk classification justification, training data governance evidence, accuracy and robustness testing results, human oversight procedure, and post-market monitoring plan.
- Independent penetration test report — conducted by a party independent of the development team, covering the full system boundary. All critical and high findings remediated and re-tested. Report retained as audit evidence.
- Evidence retention policy active — retention periods defined per regulation (GDPR: duration of processing + 3 years; HIPAA: 6 years; SOC 2: audit period + 1 year). Automated enforcement verified — evidence is not manually deleted.

Compliance gate:
- ✓ Now claimable: SOC 2 Type II audit report · ISO/IEC 27001 certification · ISO/IEC 42001 certification · EU AI Act Art.43 conformity assessment · FedRAMP High authorization (with additional controls) · HITRUST r2 certification · PCI DSS QSA assessment
- → Maintenance: annual re-assessment required for SOC 2, ISO 27001, and HITRUST. EU AI Act post-market monitoring is continuous. Evidence collection pipeline must remain active.


## 3. Sovereign AI — Regulatory Convergence Map

### 3.1. Convergence argument

Across all 17 frameworks, the same ten technical requirement families recur with near-identical definitions. The left columns are claimed by almost every regulation simultaneously; the right columns by progressively fewer. The maturity levels reflect the natural clustering order in which regulations demand these controls, from universal to sector-specific to certification-grade.

### 3.2. Requirement families

| Family | Short | Level | Description |
|---|---|---:|---|
| Encryption | Enc | L1 | At-rest and in-transit encryption, key management. Addressed at L1 — sovereign storage and local model serving. |
| Access control | RBAC | L2 | RBAC, authentication, session management, principle of least privilege. Addressed at L2 via Keycloak + OPA. |
| Audit & records | Audit | L2 | Immutable logging, records of processing, tamper-evident audit trail. Addressed at L2 via OTel + OpenSearch + Langfuse. |
| PII handling | PII | L1 | Detection, redaction, minimisation, data subject rights infrastructure. Addressed at L1 via Presidio; rights workflows at L4. |
| Data integrity | Integ | L2 | Schema validation, data quality enforcement, corruption detection. Addressed at L2 via Great Expectations + Pydantic. |
| Behavioural controls | Behav | L3 | Input/output guardrails, policy enforcement, toxicity filtering, drift monitoring. Addressed at L3 via NeMo + LLM Guard + Evidently. |
| Identity & provenance | Prov | L2 | Source authentication, data lineage, model versioning, session attribution. Addressed at L2 via Keycloak + DVC + MLflow. |
| Model governance | MdlGv | L5 | Model cards, risk classification, intended use documentation, AI system transparency. Addressed at L5 as evidence artefacts. |
| Transfer & residency | Xfer | L5 | Cross-border transfer mechanisms, data localisation, adequacy decisions. Addressed at L5 via topology and documented SCCs/BCRs. |
| Attestation | Attest | L6 | Third-party audit evidence, conformity assessment, continuous compliance posture. Addressed at L6 as evidence package. |

### 3.3. Framework × requirement family coverage

| Group | Framework | Geography / sector | Coverage | Requirement families present | Caveat / note |
|---|---|---|---:|---|---|
| Privacy laws — Turkey · EU · UK · US | GDPR | EU / EEA | 7/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Identity & provenance, Transfer & residency | — |
| Privacy laws — Turkey · EU · UK · US | UK GDPR | United Kingdom | 7/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Identity & provenance, Transfer & residency | — |
| Privacy laws — Turkey · EU · UK · US | KVKK | Turkey | 7/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Identity & provenance, Transfer & residency | — |
| Privacy laws — Turkey · EU · UK · US | CCPA / CPRA | USA — California | 5/10 | Encryption, Access control, PII handling, Identity & provenance, Transfer & residency | — |
| EU sector & cyber frameworks | EU AI Act | EU | 7/10 | Access control, Audit & records, Data integrity, Behavioural controls, Identity & provenance, Model governance, Attestation | — |
| EU sector & cyber frameworks | NIS2 | EU | 7/10 | Encryption, Access control, Audit & records, Data integrity, Behavioural controls, Identity & provenance, Attestation | — |
| EU sector & cyber frameworks | DORA | EU — Financial | 7/10 | Encryption, Access control, Audit & records, Data integrity, Behavioural controls, Identity & provenance, Attestation | — |
| US sector frameworks | HIPAA | USA — Healthcare | 9/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Behavioural controls, Identity & provenance, Transfer & residency, Attestation | — |
| US sector frameworks | PCI DSS | Global — Payments | 7/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Identity & provenance, Attestation | — |
| US sector frameworks | FedRAMP | USA — Federal | 9/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Behavioural controls, Identity & provenance, Transfer & residency, Attestation | — |
| Global standards | ISO 27001 | Global standard | 8/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Identity & provenance, Transfer & residency, Attestation | — |
| Global standards | ISO 42001 | Global standard | 7/10 | Access control, Audit & records, Data integrity, Behavioural controls, Identity & provenance, Model governance, Attestation | — |
| Global standards | SOC 2 | Global (US origin) | 8/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Behavioural controls, Identity & provenance, Attestation | — |
| Global standards | NIST AI RMF | USA (voluntary) | 7/10 | Access control, Audit & records, Data integrity, Behavioural controls, Identity & provenance, Model governance, Attestation | — |
| Turkey — Sector frameworks | DDO BIG Rehberi | Turkey — Banking (BDDK) | 8/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Identity & provenance, Transfer & residency, Attestation | AI-specific behavioural controls and model governance provisions are emerging in current revision cycles but not yet formally codified as technical requirements. |
| Turkey — Sector frameworks | BDDK Circulars | Turkey — Banking (BDDK) | 8/10 | Encryption, Access control, Audit & records, PII handling, Data integrity, Identity & provenance, Transfer & residency, Attestation | Cloud and outsourcing circulars impose explicit data localisation and third-party audit obligations beyond the BIG Rehberi scope. Treated as a distinct row for that reason. |
| Turkey — Sector frameworks | EPDK Guide | Turkey — Energy (EPDK) | 7/10 | Encryption, Access control, Audit & records, Data integrity, Identity & provenance, Transfer & residency, Attestation | PII handling is lighter than BDDK — energy operational data focus rather than financial customer data. AI-specific guidance is thin and evolving; this mapping reflects the current framework, not anticipated revisions. |

### 3.4. Framework grupları

#### Privacy laws — Turkey · EU · UK · US
- **GDPR** — General Data Protection Regulation (EU / EEA)
- **UK GDPR** — UK General Data Protection Regulation (United Kingdom)
- **KVKK** — Kişisel Verileri Koruma Kanunu (Turkey)
- **CCPA / CPRA** — California Consumer Privacy Act (USA — California)

#### EU sector & cyber frameworks
- **EU AI Act** — EU Artificial Intelligence Act (EU)
- **NIS2** — Network & Information Security Dir. 2 (EU)
- **DORA** — Digital Operational Resilience Act (EU — Financial)

#### US sector frameworks
- **HIPAA** — Health Insurance Portability Act (USA — Healthcare)
- **PCI DSS** — Payment Card Industry Data Security (Global — Payments)
- **FedRAMP** — Federal Risk & Authorization Program (USA — Federal)

#### Global standards
- **ISO 27001** — Information Security Management System (Global standard)
- **ISO 42001** — AI Management System Standard (Global standard)
- **SOC 2** — System & Organisation Controls 2 (Global (US origin))
- **NIST AI RMF** — AI Risk Management Framework (USA (voluntary))

#### Turkey — Sector frameworks
- **DDO BIG Rehberi** — BDDK Bilgi İşlem ve Bilgi Güvenliği Rehberi (Turkey — Banking (BDDK))
  - Not: AI-specific behavioural controls and model governance provisions are emerging in current revision cycles but not yet formally codified as technical requirements.
- **BDDK Circulars** — Cloud computing, outsourcing & fintech technology circulars (Turkey — Banking (BDDK))
  - Not: Cloud and outsourcing circulars impose explicit data localisation and third-party audit obligations beyond the BIG Rehberi scope. Treated as a distinct row for that reason.
- **EPDK Guide** — Enerji Piyasası Siber Güvenlik Rehberi (Turkey — Energy (EPDK))
  - Not: PII handling is lighter than BDDK — energy operational data focus rather than financial customer data. AI-specific guidance is thin and evolving; this mapping reflects the current framework, not anticipated revisions.
