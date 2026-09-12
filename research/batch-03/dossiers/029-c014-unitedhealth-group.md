# C014 — UnitedHealth Group evidence dossier

**Unreviewed agent work.** UnitedHealth Group Incorporated; NYSE common stock UNH, USD quote/reporting currency. Cutoff/retrieval 12 September 2026. Latest period Q2/H1 ended 30 June 2026, published 16 July 2026; FY2025 latest audited year.

## Business and financial anchor

UnitedHealth combines UnitedHealthcare insurance benefits with Optum Health care delivery, Optum Rx pharmacy services and Optum Insight technology/services. Its potential scarce asset is the integrated stream of eligibility, claims, pharmacy, provider and care-delivery context, plus the contractual ability to act inside workflows. The integration can improve marginal decisions, but it also creates conflicts: a cost avoided by the payer can be revenue lost by an owned provider, and automated denial creates regulatory, legal and patient harm risk.

FY2025 revenue was about **$447.6bn** and operating earnings **$19.0bn**, down from $32.3bn, with medical costs, restructuring and other items overwhelming scale growth; the medical-care ratio was 88.9% versus 85.5% in 2024. Those figures are in the [2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000012/unh-20251231.htm) and related annual results. Revenue is not a useful profit proxy because most premiums pass through as medical expense. The [Q2 2026 release](https://www.unitedhealthgroup.com/newsroom/2026/2026-07-16-uhg-reports-second-quarter-results.html) reports quarterly revenue **$112.0bn**, earnings from operations **$8.0bn**, and net margin 4.9%; quarterly operating cash flow was about $11.1bn. Full-year guidance was raised, but timing of government receipts makes one quarter's cash a weak normalized anchor. Debt-to-capital was 42.9% at 31 March 2026. Goodwill and acquired intangibles are substantial; Change Healthcare cyber remediation, care utilization, Medicare funding and regulation complicate comparisons.

The zero-additional-AI business retains scale, provider/network access, PBM purchasing and claims administration. Yet 2025 showed forecasting and underwriting can fail even with extensive data. Capital must support regulated insurance subsidiaries; ordinary industrial FCF arithmetic is inappropriate. Regulatory capital, medical-cost trend and risk adjustment matter more.

## Rights audit

| Input | Owner/exclusivity | Permitted use | Label quality | Replication threat |
|---|---|---|---|---|
| Eligibility and claims | Plan/customer/member context; UHG holds regulated copies | Treatment/payment/operations under HIPAA and contracts; cross-customer training scope undisclosed | Paid/denied outcomes frequent, but payment is not clinical appropriateness | CVS/Aetna, Elevance and government datasets have similar fields |
| Optum provider records | Patients/providers with Optum as covered entity/business associate | Purpose-, consent- and contract-bound; minimum-necessary rules apply | Clinical outcomes richer but fragmented | Health systems and EHR vendors control source workflow |
| Pharmacy transactions | Members, plans, pharmacies and Optum Rx contracts | Adjudication and operations; rebate and pooling rights not public | Fast approval/fill labels; adherence/outcome incomplete | CVS Caremark and Cigna/Evernorth comparable |
| naviHealth prediction/output | UHG software and licensed clinical inputs | Exact model-training and adverse-decision rights disputed in litigation | Length-of-stay prediction is not individual necessity | Human review, competitor tools and provider appeals |

The [UHG privacy policy](https://www.unitedhealthgroup.com/privacy-policy.html) describes broad regulated processing but does not establish economic exclusivity or universal model-training permission. Customer-specific inference may be lawful where contracted; cross-employer reuse remains unknown.

## Mechanisms, challengers and evidence

1. **Prior-authorization workflow (ML/agentic execution).** Eligibility, formulary and clinical criteria → route/approve requests → shorter clean approvals and less manual rework → lower administrative cost and faster care. UHG says Optum Rx eliminated more than 25% of drug reauthorizations since early 2025 and a named tool achieved 96% first-pass approval. These are management claims and E2 production use; they do not show equal clinical quality, member outcomes or retained cash.
2. **Care management (classical ML).** Claims and clinical history → identify interventions/sites of care → reduced avoidable utilization at equal outcomes → lower medical cost. This is economically central but public controlled evidence linking a named current model to risk-adjusted loss improvement is absent. 2025's medical-cost miss is adverse aggregate evidence, though not a clean AI test.
3. **Documentation/coding (generative assistance).** Optum provider context → draft notes/codes and claims → clinician-approved throughput → service margin or capacity. Material workload and error/audit rates are not disclosed; coding intensity may attract regulator scrutiny.

Incumbent challenger **CVS Health/Aetna** has insurance, PBM and care assets; substitute/entrant **Oscar** or an independent utilization-management vendor can use interoperable records and generic models. Providers and patient-side appeal agents can counter automated decisions. Regulation may force human review and transparency, transferring savings to patients/providers.

| Claim | Type/source/date | Stage | Confounder |
|---|---|---|---|
| Q2 revenue $112bn and OP $8bn | Fact; UHG Q2 release, 16 Jul 2026 | Financial | mix and restructuring |
| >25% of drug reauthorizations eliminated | Management; [business-change page](https://www.unitedhealthgroup.com/), accessed 12 Sep 2026 | E2 | eligible denominator and outcomes unclear |
| 96% first-pass approval reported | Management interview; [STAT](https://www.statnews.com/2026/04/06/unitedhealth-group-ai-prior-authorization/), 6 Apr 2026 | E2 | no independent quality comparator |
| Court ordered production in naviHealth case | Fact; [Becker's](https://www.beckerspayer.com/legal/judge-orders-unitedhealth-to-hand-over-documents-in-ai-denials-lawsuit/), 11 Mar 2026 | adverse | allegations unresolved |
| UHG disputes tool made adverse benefit decisions | Company position; litigation reporting, 2026 | E0 counterclaim | disputed facts |
| FY2025 MCR rose to 88.9% | Filing fact | Financial/adverse | utilization and rates dominate |
| >100m people served | Company fact; corporate site | Scale | people across services not unique members |

## KPI and materiality contract

| KPI | Baseline/comparator | Eligible workload/quality | Known result | Closing evidence |
|---|---|---|---|---|
| End-to-end authorization minutes | Same request class before tool or randomized rollout | Complete requests; appeal, reversal and adverse-event rates non-inferior | first-pass claim only | audited cohort by request class |
| Risk-adjusted medical cost PMPM | matched members/regions | tool-exposed population; access and severity controlled | unknown; 2025 aggregate worsened | prospective matched disclosure |
| Clinician minutes per closed encounter | pre-rollout teams | adopted workflows; coding accuracy and outcomes maintained | unknown | Optum segment cohort and cash reconciliation |

The 5% scale proxy is **$950m** annual pre-tax using FY2025 reported operating earnings (`0.05 × $19.0bn`). Illustration: an eligible $8bn administrative cost pool × 15% task efficiency × 50% realization × 50% retained share − $250m recurring cost = **$50m**, far below hurdle. Inputs are assumptions, exposing how large deployment/capture must be. Decision-quality economics require risk-adjusted medical cost, not gross denied claims. No member saving is counted as company cost removal.

Positive hypothesis: integrated claims/pharmacy/provider context enables faster, better interventions and UHG retains part through premiums and service fees. Negative: regulation, appeals, customer bargaining and internal conflicts absorb gains, while misuse creates legal/reputational cost; extensive data did not prevent 2025 underwriting miss.

Falsifiers: authorization automation raises appeal/reversal or access harm; matched PMPM does not improve; AI expense/coding scrutiny exceeds realized savings. Confidence mechanism **medium**, deployment **medium**, capture **low**. G0 passes; G1 incomplete due 2025 deterioration, litigation and governance; G2 insufficient because E2 workflow evidence lacks controlled quality/cash. G3/G4 deferred. Original prior 73 preserved; no new score.

## Sources and handoff

Opened 12 Sep 2026: [2025 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000012/unh-20251231.htm) (2 Mar 2026, financial statements/risk); [Q2 release](https://www.unitedhealthgroup.com/newsroom/2026/2026-07-16-uhg-reports-second-quarter-results.html) (16 Jul 2026); [business changes](https://www.unitedhealthgroup.com/) (2025–26 operational claims); [privacy](https://www.unitedhealthgroup.com/privacy-policy.html) (undated); [STAT](https://www.statnews.com/2026/04/06/unitedhealth-group-ai-prior-authorization/) (6 Apr 2026, paywalled portions); [Becker's litigation report](https://www.beckerspayer.com/legal/judge-orders-unitedhealth-to-hand-over-documents-in-ai-denials-lawsuit/) (11 Mar 2026); [Georgetown litigation tracker](https://litigationtracker.law.georgetown.edu/litigation/estate-of-gene-b-lokken-et-al-v-unitedhealth-group-inc-et-al/) (case docket context); [UHG independent review page](https://www.unitedhealthgroup.com/newsroom/2026/2026-07-10-independent-review-findings-next-steps.html) (10 Jul 2026).

Handoff: [c014.json](../capsules/c014.json). Verify Q2/FY financial definitions, exact eligible denominator behind reauthorization/96% claims, and procedural status of denial litigation. Strongest counterevidence is 2025 medical-cost and governance deterioration. Research-only; G2 incomplete. The next review should prioritize quality-adjusted member outcomes over throughput counts.
