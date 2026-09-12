# Intuitive Surgical — evidence packet

**Identity/boundary.** Intuitive Surgical, Inc., Nasdaq:ISRG common stock, USD quote/reporting. Cutoff/retrieval 12 September 2026. Latest period H1/Q2 2026, released 16 July 2026. Unreviewed; G3/G4 deferred. Intuitive owns a deeply embedded robotic-surgery ecosystem and growing procedure data, but its current value engine is instruments, systems and service. Public AI evidence is chiefly analytics capability and retrospective correlations, with no disclosed autonomous surgery or causal cash attribution.

## Business and financial resilience

Intuitive sells da Vinci robotic systems and Ion endoluminal systems, recurring instruments/accessories used per procedure, and service. Leasing lowers hospital adoption barriers and expands recurring economics. Surgeon training, procedure-specific instruments, regulatory clearances, uptime service and a large installed base produce switching costs. Competition includes Medtronic Hugo, J&J Ottava and regional systems; hospital capital budgets, reimbursement, procedure availability and tariffs can constrain demand.

FY2025 revenue was **$10.065bn**, GAAP operating income **$2.946bn**, net income attributable to Intuitive **$2.856bn**, operating cash flow **$3.031bn**, and capex **$540m**, implying simple OCF less capex of **$2.491bn**. Cash and investments were $9.034bn and the balance sheet reported only $2.517bn total liabilities, with no conventional funded-debt burden disclosed in the balance-sheet summary. [2025 10-K](https://www.sec.gov/Archives/edgar/data/1035267/000103526726000010/isrg-20251231.htm), filed 3 February 2026.

H1 2026 revenue was **$5.663bn** and GAAP operating income **$1.827bn**. Q2 revenue rose 19% to $2.89bn; combined da Vinci/Ion procedures grew about 16%; the da Vinci base reached 11,710 and Ion 1,096. Cash/investments ended Q2 at $8.626bn. [Q2 release](https://www.sec.gov/Archives/edgar/data/1035267/000103526726000047/q226ex-991earningsrelease.htm), 16 July 2026. Inventory and leased-system investment make OCF/capex volatile. Tariff refunds benefited Q2; procedure growth guidance of 13.5–15.5% indicated moderation. The conventional installed-base flywheel is viable without incremental AI.

## Data and rights

| Input | Owner/exclusivity | Customer inference | Training/reuse | Labels/replication |
|---|---|---|---|---|
| Robot telemetry and system events | Intuitive generates device data; hospital/patient interests remain | Service and case analytics under agreements | Pooled use/retention terms not publicly established | Dense signals, weak direct outcome labels; rival robots generate analogous data |
| Surgical video | Patient/provider-controlled with contractual platform rights | My Intuitive/Case Insights use depends on consent/configuration | Cross-hospital model training unknown | Phase/technique labels require expert effort; video export can aid substitutes |
| Procedure/outcome data | Providers/payers/patients; Intuitive may receive linked subsets | Customer-specific dashboards plausible | HIPAA/consent and data-use agreement bounded | Clinically valuable but selection/case mix confounds causal inference |
| Surgeon training/simulation records | Mixed Intuitive and user data | Personalized feedback plausible | Pooled learning undisclosed | Repeated performance labels; competitors can build curricula |

The installed workflow and regulatory distribution are scarce. Data exclusivity is not established. The company’s safety notice says da Vinci is a surgeon-controlled tool and serious complications can occur, underlining human responsibility.

## Mechanisms and challengers

1. **Case Insights and performance analytics (classical/deep ML).** Robot/video data can identify surgical phases and correlations between technique and outcomes, then deliver dashboards/coaching. The economic path is greater utilization, improved training and customer retention → more procedures/instrument revenue. Intuitive describes a secure My Intuitive platform with data and performance dashboards. Reported correlations are E1/E2 capability, not E3 causal outcome.
2. **Service prediction and uptime (classical ML).** High-frequency system telemetry can forecast component issues and guide 24/7 service, potentially lowering downtime and field cost. Installed base and proprietary engineering help. Public sources describe service but do not disclose matched downtime or cash savings.
3. **Future intraoperative assistance (vision/agentic).** Surgical video and robot kinematics might support anatomy recognition, guardrails or automation. Intuitive emphasizes surgeon autonomy; no broad autonomous clinical deployment was identified. Independent VLM evaluation found spatial/temporal reasoning difficult, making this E0/E1.

Medtronic is the incumbent challenger with Hugo and Touch Surgery analytics. J&J and open/academic surgical vision models are entrants/substitutes. Hospitals could demand data portability, build vendor-neutral analytics, or capture efficiency through lower prices. Instrument revenue may benefit from more procedures, but analytics could also reduce training/system differentiation if generic tools work across platforms.

## Evidence ledger

| Claim | Type/source/date | Scope | Stage | Confounder |
|---|---|---|---|---|
| FY25 revenue $10.065bn, OP $2.946bn, OCF $3.031bn | Fact, 10-K, 3 Feb 2026, statements/MD&A | Group | financial | Lease/inventory investment; SBC |
| Q2 revenue $2.89bn; installed bases 11,710/1,096 | Fact, SEC Q2 release, 16 Jul 2026 | Group/platforms | financial/E2 installed base | Procedure mix and placements |
| My Intuitive combines surgical data, learning and dashboards | Company claim, [platform page](https://www.intuitive.com/en-us/products-and-services/my-intuitive), opened 12 Sep | Digital platform | E1/E2 | No adoption denominator/outcome |
| Case Insights correlates technique and outcomes | Company/executive claim reported by [MedTech Dive](https://www.medtechdive.com/news/intuitive-surgical-ai-robotic-surgery-tony-jarc/692977/), 8 Sep 2023 | Analytics | E1/E2 | Retrospective correlation, selection bias |
| 2026 procedure outlook 13.5–15.5% | Fact, Q2 release | Worldwide da Vinci | financial | Insurance access, bariatric mix |
| VLM spatial/temporal tasks remain difficult | Independent research, [Rau et al.](https://arxiv.org/abs/2504.02799), 3 Apr 2025 | 13 datasets, 11 models | E3 for external benchmark | Not an Intuitive product test |
| Serious complications remain possible and system does not treat cancer | Company safety disclosure, [Intuitive](https://www.intuitive.com/en-us/patients/important-safety-information), opened 12 Sep | da Vinci | adverse fact | General surgical risk |

## Measurement contract and materiality

| KPI | Comparator | Eligible workload | Quality | Known | Review event |
|---|---|---|---|---|---|
| Minutes and errors per trained case | Matched surgeons/sites before rollout | Cases with Case Insights | Complications/conversion/readmission no worse by risk-adjusted cohort | Unknown | Stepped-wedge deployment study |
| Unplanned downtime hours/system/year | Same model/age without predictive workflow | Connected systems with service consent | False-alert and cancellation rates | Unknown | Service KPI/renewal disclosure |
| Incremental instrument contribution from analytics | Similar sites without module | Paid module sites | Case mix and procedure trend controlled | Unknown | Cohort utilization and paid attach |

Five percent of FY2025 GAAP operating income is **$147m/year**. Illustrative recurring revenue path: 11,710 da Vinci systems × $30,000 annual analytics price × 40% paid attach × 75% contribution margin × 80% retained after hospital sharing = **$84m/year**. Service-cost path: assume $1.5bn eligible global service/field cost × 8% efficiency × 50% realization × 70% retention = **$42m/year**. Less assumed $30m recurring model/privacy/support cost gives **$96m/year**, below hurdle. Required analytics attach holding other assumptions: `(147+30-42)/(11710×30000×.75×.8)=64.1%`. All nonfinancial inputs are assumptions; procedure growth already in reported baseline and is not attributed to AI.

## Hypotheses, falsifiers and gates

Positive: Intuitive’s installed systems, high-frequency procedure data, training network and consumable model let analytics improve utilization and lock in recurring instrument economics. Negative: data rights are fragmented, outcomes confounded, and hospitals or generic analytics capture value; safety constraints keep agentic execution remote.

Falsifiers: no paid analytics attach/renewal disclosure by three cycles; matched studies show no quality-adjusted utilization or training benefit; hospitals secure broad export/interoperability that supports vendor-neutral analytics at lower cost. Questions: pooled training rights, labeled outcome coverage, module pricing, connected-system penetration, and whether analytics changes procedure volume rather than just dashboards.

Confidence: mechanism medium; deployment low-medium; capture low-medium. G0 pass; G1 provisional pass; G2 insufficient/provisional because E2 platform evidence lacks controlled quality-adjusted results or retained cash. G3/G4 deferred.

## Sources

1. Intuitive, 2025 10-K, filed 3 Feb 2026, pp. 61–93/MD&A, opened 12 Sep: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000010/isrg-20251231.htm
2. Intuitive, Q2 2026 release, 16 Jul 2026, opened 12 Sep: https://www.sec.gov/Archives/edgar/data/1035267/000103526726000047/q226ex-991earningsrelease.htm
3. Intuitive, My Intuitive platform, undated, opened 12 Sep; marketing scope: https://www.intuitive.com/en-us/products-and-services/my-intuitive
4. MedTech Dive, AI/Case Insights interview, 8 Sep 2023, opened 12 Sep; management claims: https://www.medtechdive.com/news/intuitive-surgical-ai-robotic-surgery-tony-jarc/692977/
5. Intuitive, safety information, undated, opened 12 Sep: https://www.intuitive.com/en-us/patients/important-safety-information
6. Rau et al., surgical VLM evaluation, 3 Apr 2025, opened 12 Sep; preprint/external: https://arxiv.org/abs/2504.02799
7. Medtronic, Touch Surgery product, undated, opened 12 Sep; competitor source: https://www.medtronic.com/en-us/healthcare-professionals/products/digital-surgery/touch-surgery-performance-insights.html

Capsule: [c009.json](../capsules/c009.json). Verify financial statements, Case Insights scope and assumed attach arithmetic. Unreviewed.
