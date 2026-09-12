# C014 — UnitedHealth Group evidence dossier

**Unreviewed agent work.** UnitedHealth Group Incorporated; NYSE common stock UNH, USD quote/reporting currency. Cutoff/retrieval 12 September 2026. Latest period Q2/H1 ended 30 June 2026, published 16 July 2026; FY2025 latest audited year.

## Business and financial anchor

UnitedHealth combines UnitedHealthcare insurance benefits with Optum Health care delivery, Optum Rx pharmacy services and Optum Insight technology/services. Its potential scarce asset is the integrated stream of eligibility, claims, pharmacy, provider and care-delivery context, plus the contractual ability to act inside workflows. The integration can improve marginal decisions, but it also creates conflicts: a cost avoided by the payer can be revenue lost by an owned provider, and automated denial creates regulatory, legal and patient harm risk.

FY2025 revenue was about **$447.6bn** and operating earnings **$19.0bn**, down from $32.3bn, with medical costs, restructuring and other items overwhelming scale growth; the medical-care ratio was 88.9% versus 85.5% in 2024. Those figures are in the [2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm) and related annual results. Revenue is not a useful profit proxy because most premiums pass through as medical expense. The [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/731766/000073176626000191/earningsrelease2q26_7152.htm) reports quarterly revenue **$112.0bn**, earnings from operations **$8.0bn**, and net margin 4.9%; quarterly operating cash flow was about $11.1bn. Full-year guidance was raised, but timing of government receipts makes one quarter's cash a weak normalized anchor. Debt-to-capital was 42.9% at 31 March 2026. Goodwill and acquired intangibles are substantial; Change Healthcare cyber remediation, care utilization, Medicare funding and regulation complicate comparisons.

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

1. **Prior-authorization workflow (ML/agentic execution).** Eligibility, formulary and clinical criteria → route/approve requests → shorter clean approvals and less manual rework → lower administrative cost and faster care. UHG says Optum Rx eliminated more than 25% of drug reauthorizations since early 2025, but this was removal of policy requirements rather than an AI outcome. An Optum product release says Humata deployments—not a demonstrated UHG cohort—achieved 96% first-pass approval. These support policy change and product capability (E1; at most limited E2 for third-party deployments), not a company-specific AI production result, equal clinical quality or retained cash.
2. **Care management (classical ML).** Claims and clinical history → identify interventions/sites of care → reduced avoidable utilization at equal outcomes → lower medical cost. This is economically central but public controlled evidence linking a named current model to risk-adjusted loss improvement is absent. 2025's medical-cost miss is adverse aggregate evidence, though not a clean AI test.
3. **Documentation/coding (generative assistance).** Optum provider context → draft notes/codes and claims → clinician-approved throughput → service margin or capacity. Material workload and error/audit rates are not disclosed; coding intensity may attract regulator scrutiny.

Incumbent challenger **CVS Health/Aetna** has insurance, PBM and care assets; substitute/entrant **Oscar** or an independent utilization-management vendor can use interoperable records and generic models. Providers and patient-side appeal agents can counter automated decisions. Regulation may force human review and transparency, transferring savings to patients/providers.

| Claim | Type/source/date | Stage | Confounder |
|---|---|---|---|
| Q2 revenue $112bn and OP $8bn | Fact; UHG Q2 release, 16 Jul 2026 | Financial | mix and restructuring |
| >25% of drug reauthorizations eliminated | Management; [business-change page](https://www.unitedhealthgroup.com/uhg/business-initiatives.html), accessed 12 Sep 2026 | Policy fact, not AI evidence | requirements removed for 270 drugs; causality must not be assigned |
| 96% first-pass approval refers to Humata deployments | Optum product/STAT reporting, 6 Apr 2026 | E1 product; limited third-party E2, not UHG cohort | no independent quality comparator |
| Court ordered production in naviHealth case | Fact; [Becker's](https://law.justia.com/cases/federal/district-courts/minnesota/mndce/0%3A2023cv03514/211721/162/), 11 Mar 2026 | adverse | allegations unresolved |
| UHG disputes tool made adverse benefit decisions | Company position; litigation reporting, 2026 | E0 counterclaim | disputed facts |
| FY2025 MCR rose to 88.9% | Filing fact | Financial/adverse | utilization and rates dominate |
| >100m people served | Company fact; corporate site | Scale | people across services not unique members |

## KPI and materiality contract

| KPI | Baseline/comparator | Eligible workload/quality | Known result | Closing evidence |
|---|---|---|---|---|
| End-to-end authorization minutes | Same request class before tool or randomized rollout | Complete requests; appeal, reversal and adverse-event rates non-inferior | first-pass claim only | audited cohort by request class |
| Risk-adjusted medical cost PMPM | matched members/regions | tool-exposed population; access and severity controlled | unknown; 2025 aggregate worsened | prospective matched disclosure |
| Clinician minutes per closed encounter | pre-rollout teams | adopted workflows; coding accuracy and outcomes maintained | unknown | Optum segment cohort and cash reconciliation |

The exact 5% scale proxy is **$948.2m** annual pre-tax using FY2025 reported operating earnings (`0.05 × $18.964bn`). Illustration: an eligible $8bn administrative cost pool × 15% task efficiency × 50% realization × 50% retained share − $250m recurring cost = **$50m**, far below hurdle. Inputs are assumptions, exposing how large deployment/capture must be. Decision-quality economics require risk-adjusted medical cost, not gross denied claims. No member saving is counted as company cost removal.

Positive hypothesis: integrated claims/pharmacy/provider context enables faster, better interventions and UHG retains part through premiums and service fees. Negative: regulation, appeals, customer bargaining and internal conflicts absorb gains, while misuse creates legal/reputational cost; extensive data did not prevent 2025 underwriting miss.

Falsifiers: authorization automation raises appeal/reversal or access harm; matched PMPM does not improve; AI expense/coding scrutiny exceeds realized savings. Confidence mechanism **medium**, deployment **medium**, capture **low**. G0 passes; G1 incomplete due 2025 deterioration, litigation and governance; G2 insufficient because E1 product and limited third-party deployment evidence lacks a company-specific controlled quality/cash cohort. G3/G4 deferred. Original prior 73 preserved; no new score.

## Sources and handoff

Opened 12 Sep 2026: [2025 10-K](https://www.sec.gov/Archives/edgar/data/731766/000073176626000062/unh-20251231.htm) (2 Mar 2026, financial statements/risk); [Q2 release](https://www.sec.gov/Archives/edgar/data/731766/000073176626000191/earningsrelease2q26_7152.htm) (16 Jul 2026); [business changes](https://www.unitedhealthgroup.com/uhg/business-initiatives.html) (2025–26 operational claims); [privacy](https://www.unitedhealthgroup.com/privacy-policy.html) (undated); [Optum primary product release](https://www.optum.com/en/newsroom/health-tech/optum-is-advancing-ai-powered-digital-prior-authorization.html) (6 Apr 2026, opened directly); [federal court order](https://law.justia.com/cases/federal/district-courts/minnesota/mndce/0%3A2023cv03514/211721/162/) (9 Mar 2026; motion to compel granted in part/denied in part, no merits finding); [Georgetown litigation tracker](https://litigationtracker.law.georgetown.edu/litigation/estate-of-gene-b-lokken-et-al-v-unitedhealth-group-inc-et-al/) (case docket context).

Handoff: [c014.json](../capsules/c014.json). Verify Q2/FY financial definitions, policy nature of reauthorization removal and Humata—not UHG—scope of the 96% claim, and procedural status of denial litigation. Strongest counterevidence is 2025 medical-cost and governance deterioration. Research-only; G2 incomplete. The next review should prioritize quality-adjusted member outcomes over throughput counts.
