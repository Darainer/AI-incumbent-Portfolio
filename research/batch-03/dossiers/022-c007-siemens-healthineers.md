# C007 Siemens Healthineers — evidence dossier

**Unreviewed agent packet. Cutoff:** 12 September 2026. **Security:** Siemens Healthineers AG registered shares, Frankfurt/Xetra: SHL; quote/reporting currency EUR. Siemens AG remains a controlling shareholder. **Latest period:** fiscal Q3 ended 30 June 2026, published 31 July 2026. No valuation or ranking.

## Existing business and financial resilience

Siemens Healthineers sells imaging systems and service, diagnostics, precision therapy (including Varian cancer care) and digital workflow. Its installed instruments, clinical integration, service footprint and regulatory approvals create recurring service/software opportunities. Hospitals nevertheless own much patient data, procurement is competitive and reimbursement can pass productivity to customers.

FY2025 [annual report](https://corporate.webassets.siemens-healthineers.com/a364b935102e7df5/d7fdacda458e/siemens-healthineers-ir-annual-report-2025.pdf) reports €23.375bn revenue, €3.154bn IFRS EBIT, €2.167bn net income, €3.532bn operating cash flow and €2.714bn company-defined free cash flow after €818m additions to intangibles/PPE. Net debt including pensions was €12.472bn (2.8× EBITDA), much of it financing liabilities to Siemens Group. Imaging revenue was €13.182bn, Diagnostics €4.347bn, Varian €4.081bn and Advanced Therapies €2.128bn under the then segment structure. R&D expense was €1.958bn.

The [Q3 FY2026 statement](https://corporate.webassets.siemens-healthineers.com/2637d4a46dbcd161/a3335cc16ed1/siemens-healthineers-Q3_FY2026_Earnings-Release-and-Financial-Results.pdf) reports €5.764bn revenue, €1.101bn adjusted EBIT, €946m IFRS EBIT, €676m net income and €1.023bn free cash flow. Tariff refunds lifted every segment and about €0.2bn of quarterly FCF, so margins are not a clean AI baseline. Diagnostics revenue fell 5.5% comparably and margin dropped to 4.1%; management cut FY2026 comparable growth guidance to 3.5–4.0%. China procurement/market change, currency, inflation, mix and the diagnostics platform transition are larger current drivers than disclosed AI.

## Data rights

| Input | Owner/exclusivity | Use rights | Labels/quality | Replication |
|---|---|---|---|---|
| Scanner raw/reconstructed images | hospital/patient context; Healthineers owns device methods | local inference/product licence evidenced; training/reuse depends on site consent and agreements | images are rich; diagnosis/outcome labels may be incomplete | GE HealthCare, Philips and hospital archives |
| Device telemetry/service logs | mixed device-maker/customer | remote service and optimization plausible; cross-site learning terms not public | failure/maintenance labels observable | rival installed bases and third-party monitoring |
| Clinical workflow and reports | providers/clinicians | AI-Rad Companion assists under regulated intended use; broad pooled training unknown | reports provide labels but contain practice bias | PACS vendors and foundation models |
| Varian treatment/planning data | clinics/patients plus Varian software | customer workflow use; cross-customer training undisclosed | dose, plan and outcomes differ in latency/quality | Elekta and oncology platforms |

Possession through an installed base is not ownership. The EU GDPR, medical-device rules and hospital contracts narrow patient-level reuse. Regulatory clearance validates an intended use and risk process, not economic exclusivity.

## Mechanisms, challengers and evidence

**AI-assisted imaging reconstruction/acquisition (classical ML).** Scanner data → reconstruction/positioning → diagnostic-quality image with shorter scan/repeat burden → throughput or premium system/service revenue. Healthineers' annual report says AI is deployed for analysis, decision support, robot control and automation. Product families such as Deep Resolve and myExam Companion are commercially integrated, reaching E2 at product level. Yet disclosed materials do not provide a matched installed-base throughput/revenue bridge.

**AI-Rad Companion interpretation (ML assistance).** Images → automated measurements/flagging → radiologist review → potentially shorter reading time and consistent detection → software attach/renewal. Product pages establish commercial availability and specific intended uses (E1/E2), while equal-quality end-to-end performance across real hospitals is not reported. A cleared algorithm can add review burden or fail under case-mix shift.

**Digital/agentic workflow and service.** Device/worklist context → scheduling, protocoling or remote service recommendation/action → less downtime and staff effort → service margin/renewal. Annual-report deployment language is broad; no eligible-workload denominator, autonomous-action rate or recurring savings is disclosed, so this remains E1/company-reported E2.

GE HealthCare is the principal incumbent challenger, with a similarly large installed imaging base and Edison/AI applications; Philips is another. Hospital PACS/cloud vendors and radiology foundation-model entrants can sit above equipment and weaken attach. Interoperability standards and customer-owned data reduce exclusivity. Negative evidence is visible in Diagnostics: transition and China procurement produced declining revenue despite company-wide digital/AI claims. Q3 tariff refunds, not AI, lifted margin. FDA guidance requires transparency, bias control, robustness and lifecycle monitoring; subgroup deterioration or extra review can erase throughput.

## Evidence ledger

| Claim | Type | Source/date/section | Scope | Stage | Confounder |
|---|---|---|---|---|---|
| AI used in data interpretation, decisions, robot control and automation | company fact/claim | [FY2025 report](https://corporate.webassets.siemens-healthineers.com/a364b935102e7df5/d7fdacda458e/siemens-healthineers-ir-annual-report-2025.pdf), 26 Nov 2025, p.7 | portfolio | E2 | no adoption denominator |
| AI-Rad Companion products are commercially offered | fact | [AI-Rad Companion](https://www.siemens-healthineers.com/digital-health-solutions/digital-solutions-overview/clinical-decision-support/ai-rad-companion), accessed cutoff | named applications | E1/E2 | availability ≠ measured outcome |
| AI can ease routine workflow | company/customer narrative | [Shape spotlight](https://events.siemens-healthineers.com/sessions/spotlight/ai-elevates-patient-care), 2025 | selected stories | E2 | anecdotes, no controls |
| Installed product workflow could retain software/service revenue | inference | annual report, business/segments | imaging/service | E1 | hospital captures throughput |
| Q3 margin rose partly from tariff refunds | financial fact | [Q3 statement](https://corporate.webassets.siemens-healthineers.com/2637d4a46dbcd161/a3335cc16ed1/siemens-healthineers-Q3_FY2026_Earnings-Release-and-Financial-Results.pdf), 31 Jul 2026, pp.1–5 | company | financial | nonrecurring refund |
| Diagnostics decline challenges broad productivity attribution | inference | same, p.4 | Diagnostics | E0 | China/platform transition |
| Controlled installed-base AI economics are absent | negative finding | searched sources through cutoff | company | E0 | nondisclosure not failure |

## KPI and materiality contract

| KPI | Baseline/comparator | Eligible work | Quality condition | Known | Next proof |
|---|---|---|---|---|---|
| diagnostic-quality scans per installed unit-hour | same system/site before vs randomized rollout | AI-enabled examinations | sensitivity/specificity and dose fixed | unknown | multi-site paired rollout |
| repeat scan rate | matched protocols/case mix | supported anatomies | no subgroup deterioration | unknown | post-market cohort |
| reading minutes per finalized report | radiologist/site matched control | AI-Rad-supported cases | errors, follow-ups, review time | not disclosed | controlled study |
| paid software attach/renewal | prior product generation | eligible installed base | net of inference/support cost | unknown | segment attach disclosure |

Five percent of FY2025 IFRS EBIT is **€157.7m**. Illustrative cost bridge: assume €1.5bn annual eligible service/workflow cost, 15% efficiency, 60% realization, 50% retained and €50m recurring AI cost. €1.5bn × 15% × 60% × 50% − €50m = **€17.5m**, below the hurdle. A revenue mechanism needs premium attach or throughput-linked contribution: at an assumed 70% incremental margin, €157.7m requires €225.3m incremental annual revenue before tax. Neither input is disclosed; these are break-even illustrations, not forecasts.

## Hypotheses, falsifiers and gates

Positive: regulated AI integrated with scarce equipment improves quality-adjusted throughput and sells through service/software. Negative: customers own the data and capture throughput, rivals match features, and validation/review plus procurement pressure eliminate pricing.

Falsifiers: (1) multi-site deployments show no throughput at equal diagnostic quality; (2) software attach/renewal fails to rise or is bundled free; (3) repeat scans, adverse events or review time offset automation. Unresolved: active installed base, rights, paid attach, model cost, subgroup performance and service-margin contribution.

Confidence: mechanism **medium-high**, deployment **medium**, capture **low**. G0 met; G1 provisionally met but leverage/Diagnostics transition matter; G2 **provisional limited** because product deployment reaches E2 while controlled quality-adjusted and cash evidence do not. G3/G4 deferred.

## Source register

Opened/accessed 12 Sep 2026: [FY2025 annual report](https://corporate.webassets.siemens-healthineers.com/a364b935102e7df5/d7fdacda458e/siemens-healthineers-ir-annual-report-2025.pdf) (26 Nov 2025, pp.7,15–23,138–43,161); [Q3 FY2026 statement](https://corporate.webassets.siemens-healthineers.com/2637d4a46dbcd161/a3335cc16ed1/siemens-healthineers-Q3_FY2026_Earnings-Release-and-Financial-Results.pdf) (31 Jul 2026, pp.1–6); [Q3 release](https://www.siemens-healthineers.com/press/releases/2026q3) (31 Jul 2026); [AI-Rad Companion](https://www.siemens-healthineers.com/digital-health-solutions/digital-solutions-overview/clinical-decision-support/ai-rad-companion) (undated product scope); [Shape AI spotlight](https://events.siemens-healthineers.com/sessions/spotlight/ai-elevates-patient-care) (2025); [FDA AI medical-products paper](https://www.fda.gov/media/177030/download) (Mar 2024); [FDA AI device list](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices) (updated periodically; regulatory/challenger context); [GE HealthCare AI](https://www.gehealthcare.com/insights/artificial-intelligence) (undated; challenger capability); [Philips AI](https://www.philips.com/a-w/about/artificial-intelligence.html) (undated; challenger). Product sources do not independently prove efficacy or capture.

**Handoff:** verify FY2025 EBIT/FCF/net debt; Q3 tariff-refund/Diagnostics confounders; portfolio-level AI deployment without attach economics. Files: this dossier and [capsule](../capsules/c007.json).
