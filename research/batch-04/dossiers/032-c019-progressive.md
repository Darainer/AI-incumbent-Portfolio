# C019 Progressive — evidence dossier

**Unreviewed agent packet. Cutoff:** 12 September 2026. **Security:** The Progressive Corporation common stock, NYSE: PGR; USD. **Latest period:** July 2026 monthly results, filed/released 19 August 2026. Valuation/ranking deferred.

## Business and financial base

Progressive underwrites personal auto, property, special lines and commercial auto through agency and direct channels. Its scarce asset is long-cycle underwriting discipline plus high-frequency driving, quote, policy and claim outcomes. The reported baseline already includes decades of statistical pricing and telematics; only incremental model improvement belongs in the AI thesis.

The [July 2026 SEC-filed release](https://www.sec.gov/Archives/edgar/data/80661/000008066126000315/pgr202607ex99earningsrelea.htm) reports $7.441bn net premiums written, $7.355bn earned, $961m net income and an 86.8 combined ratio. Policies in force were 40.304m, up 7%, including 28.082m agency/direct auto. Monthly results are volatile and realized investment losses affected income.

The [2025 10-K](https://www.sec.gov/Archives/edgar/data/80661/000008066126000086/pgr-20251231.htm) reports $83.2bn net premiums written, $81.661bn earned, 87.1 statutory combined ratio, diluted EPS $19.23 and statutory surplus $28.4bn, a 2.9× premiums-to-surplus ratio. The company declared $13.90 per share dividends for 2025 and maintained $5.5bn securities in a non-insurance subsidiary at January 2026. These indicate substantial excess capital/cash generation, but favorable pricing, frequency/severity and reserve development dominate one-year comparisons.

## Data rights

| Input | Owner/exclusivity | Use/training | Labels | Replication |
|---|---|---|---|---|
| Quote/policy/claims records | insured and Progressive; regulated | underwriting/claims inference established; pooled-model rights subject to privacy/law | frequent auto outcomes, but ultimate severity develops | GEICO, State Farm and carriers have large books |
| Snapshot mobile/device driving data | driver-generated under programme consent | Progressive terms permit programme scoring; reuse beyond disclosed purposes is not established | mileage, braking and driving behavior with later claims | OEM/phone telematics and rival programmes |
| Vehicle/repair images and estimates | customer, repairer, vendors | claim-specific inference; vendor and cross-customer rights unknown | repair cost and supplements are observable | CCC/Mitchell ecosystems and CV vendors |
| Agent/customer interactions | mixed customer/company | service assistance plausible; generative training terms unknown | conversion, completion, complaint labels | generic CRM/copilots |

Telematics consent can support pricing but is not universal training permission. State insurance regulators review rating variables, unfair discrimination and claim practices.

## Mechanisms and challengers

**Risk selection/pricing (classical ML).** Quote, policy and telematics context → risk estimate/price → lower loss ratio at constant rate and mix → underwriting profit/capital growth. Snapshot is deployed at scale as an insurance programme, but public sources do not isolate the latest algorithm against the incumbent production score. This is E2 deployment, not E3 incremental lift.

**Claims triage/estimate (computer vision/ML).** Claim images/history → routing/estimate/fraud signal → faster accurate close → lower adjustment expense/leakage. Progressive describes digital photo/claims workflows, while sample, matched leakage, supplements and human-review cost are not disclosed. Stage is E1/E2.

**Customer/agent assistance (generative/automation).** Policy context → quote/service answer/action → lower expense and higher conversion. No decisive public source by cutoff reconciles generative AI to expense ratio or retention; E0/E1.

GEICO is a direct challenger with large direct distribution and telematics; State Farm has broader agent/claim data. OEM embedded insurance and comparison platforms are substitutes that may own driving/interface data. Vendor claim-estimation systems reduce exclusivity. Negative evidence: June/July combined ratios rose year over year even while remaining excellent, showing weather, loss severity and pricing can overwhelm small model effects. Progressive's current underwriting success may reflect rate adequacy and disciplined growth rather than incremental AI. Regulators or customers can capture improved risk differentiation through required filings or discounts.

## Evidence ledger

| Claim | Type | Source/date | Scope | Stage | Confounder |
|---|---|---|---|---|---|
| Snapshot telematics is a production programme | fact | [Snapshot](https://www.progressive.com/auto/discounts/snapshot/), accessed cutoff | participating auto policies | E2 | selection and pricing changes |
| July combined ratio 86.8 | fact | [July filing](https://www.sec.gov/Archives/edgar/data/80661/000008066126000315/pgr202607ex99earningsrelea.htm), 19 Aug 2026 | one month | financial | catastrophe/reserve/season |
| 2025 statutory combined ratio 87.1 | fact | [2025 10-K](https://www.sec.gov/Archives/edgar/data/80661/000008066126000086/pgr-20251231.htm), 2 Mar 2026 | full year | financial | pricing/cycle |
| Driving data can improve segmentation | inference | Snapshot/privacy and 10-K | opted-in policies | E1 | behavior/selection bias |
| New-model incremental lift is undisclosed | negative finding | searched company filings/product material | pricing | E0 | nondisclosure |
| Claim automation can reduce handling work | management capability | [claims](https://www.progressive.com/claims/), accessed cutoff | claims channel | E1/E2 | customer self-service, no causal result |

## KPI and materiality

| KPI | Baseline/comparator | Eligible | Quality control | Known | Proof event |
|---|---|---|---|---|---|
| accident-year loss ratio at fixed rate | matched states/products/vintages or randomized model | newly scored policies | exposure/fairness/cat normalized | unknown | 24–36 month filing cohort |
| claims expense per closed claim | randomized adjuster rollout | eligible claims | leakage, supplement, appeal, satisfaction | unknown | controlled claims study |
| quote conversion at risk-adjusted margin | old production score | model-treated quotes | same expected loss/capital | unknown | filed cohort renewal |

Use underwriting profit/capital. FY2025 underwriting margin from 87.1 ratio is 12.9%; applied to $81.661bn earned premium gives a rough **$10.535bn pretax underwriting profit** before investment income and reconciliation. The 5% convention is $526.8m. That equals about **64.5 bps of earned premium** ($526.8m/$81.661bn). A 20bp sustainable AI improvement is $163.3m before model/implementation cost, below the hurdle. These are scale calculations, not attributed forecasts.


## Measurement design and decision use

A useful next disclosure would separate technical performance from economic realization. The technical layer should report the frozen model version, evaluation set, error taxonomy and drift; the operating layer should report eligible cases, attempted cases, accepted recommendations, overrides and downstream quality; the finance layer should show gross benefit, implementation expense, recurring inference/vendor cost, displaced spend and timing. All three layers need the same cohort and period. Otherwise a high acceptance rate can coexist with no cash benefit, and a favorable cost trend can be driven by unrelated restructuring.

Selection is another risk. Early adopters, easier cases and high-performing sites often enter first. A credible design would randomize where feasible or use matched sites/workflows with pre-period trends, fixed inclusion rules and confidence intervals. It would retain failed runs and human corrections rather than measure only completed outputs. Quality guardrails should include customer harm, regulatory exceptions, rework and tail latency. The company should disclose whether automation removes a step, shifts it to another team, or merely increases capacity.

The committee can use a staged evidence rule. Product availability supports E1. Authenticated production use with an eligible-workload denominator supports E2. A persistent matched operational lift supports E3. A finance reconciliation net of all costs is needed for E4. Until those steps are met, the arithmetic above defines what evidence must explain; it does not convert management claims into an earnings contribution. This design also makes the thesis falsifiable within a defined reporting cycle rather than waiting for broad margin movement that has many causes.

## Falsifiers and gates

Positive: frequent proprietary telematics and claim outcomes reinforce pricing/claims at scale. Negative: regulated variables and comparable carrier/OEM data eliminate advantage; cycle explains superior results. Falsifiers: matched vintages fail to improve risk-adjusted loss; claim automation raises leakage/complaints; Snapshot selection weakens or regulators restrict variables. Unknown: current algorithm deployment share, consent/reuse, controlled lift, AI cost and retained renewal pricing.

Confidence: mechanism **medium-high**, deployment **medium**, capture **low-medium**. G0 met; G1 provisionally met with strong surplus; G2 **provisional limited** because telematics deployment is E2 but incremental AI lift/cash attribution is absent. G3/G4 deferred.

## Source register

Opened 12 Sep 2026: [July 2026 filing](https://www.sec.gov/Archives/edgar/data/80661/000008066126000315/pgr202607ex99earningsrelea.htm) (19 Aug 2026); [2025 10-K](https://www.sec.gov/Archives/edgar/data/80661/000008066126000086/pgr-20251231.htm) (2 Mar 2026); [2025 financial review](https://s202.q4cdn.com/605347829/files/doc_financials/2025/q4/interactive/progressive-ir-25/pdfs/Progressive-2025-Financial-Review.pdf) (2 Mar 2026); [Snapshot](https://www.progressive.com/auto/discounts/snapshot/) (undated); [Progressive privacy](https://www.progressive.com/privacy/) (undated); [claims service](https://www.progressive.com/claims/) (undated); [NAIC AI principles](https://content.naic.org/insurance-topics/artificial-intelligence) (regulatory); [GEICO DriveEasy](https://www.geico.com/driveeasy/) (challenger); [State Farm Drive Safe & Save](https://www.statefarm.com/insurance/auto/discounts/drive-safe-save) (challenger). No controlled Progressive incremental-AI study was found.

**Handoff:** verify July 86.8 ratio/40.3m policies; FY2025 $81.661bn earned/87.1 ratio/$28.4bn surplus; no disclosed latest-model lift. Files: this dossier and [capsule](../capsules/c019.json).
