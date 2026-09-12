# SAP (C041) — initial dossier

**Status:** unreviewed research-agent work; lead judgment required.  
**Security:** SAP SE ordinary bearer share, Xetra: SAP, ISIN DE0007164600, EUR; reporting currency EUR. NYSE: SAP is a sponsored ADR and one ADR corresponds to one ordinary share. The valuation uses the Xetra ordinary to avoid FX mixing.  
**Cutoff / retrieval date:** 12 September 2026. Q2/H1 ended 30 June 2026, published 23 July; FY2025 ended 31 December 2025. Price is the 11 September Xetra close.  
**Industry:** enterprise systems and workflow orchestration (I03).  
**Provisional conclusion:** SAP’s system-of-record position, permissions and process schemas make the agent mechanism plausible. Yet deployment evidence is much weaker than order-entry language: a 2026 user-group survey found 3% of implementing respondents used SAP AI in production, versus 77% using non-SAP solutions. No AI-specific recurring revenue, net contract value, inference cost or renewal cohort supports E4. At €177.26, reverse valuation requires about 12% annual 2026–30 EPS growth at a 23× terminal multiple. Provisional disposition: **watch / operating-thesis candidate; G3 blocked pending normalized EPS and point share reconciliation**.

## Conventional business and dated economics

SAP sells applications spanning finance, procurement, HR, supply chain and customer experience. Applications, Technology & Support includes cloud subscriptions, support and products; Core Services is mainly consulting. Costly implementations create switching costs, while ECC-to-S/4HANA conversion supports bookings.

The [2025 Integrated Report](https://www.sap.com/docs/download/investors/2025/sap-2025-integrated-report.pdf) records revenue of €36.800bn, up 8% reported. Subscription revenue rose 22% to €21.328bn; cloud revenue was €21.023bn, while support fell 7% and licenses 29%. IFRS operating profit was €9.617bn (26.1% margin), but the doubling from 2024 largely reflects restructuring expense falling from €3.144bn to €3m. Non-IFRS operating profit was €10.419bn. Profit after tax was €7.326bn and EPS €6.14.

| EUR millions except EPS | FY2024 | FY2025 | Q2 2026 | H1 2026 |
|---|---:|---:|---:|---:|
| Revenue | 34,176 | 36,800 | 9,878 | 19,432 |
| Cloud revenue | 17,141 | 21,023 | 6,281 | 12,244 |
| IFRS operating profit / margin | 4,665 / 13.6% | 9,617 / 26.1% | 2,643 / 26.8% | 5,383 / 27.7% |
| Profit after tax / basic EPS | 3,150 / €2.68 | 7,326 / €6.14 | 2,209 / €1.89 | 4,155 / €3.55 |
| Operating cash flow / FCF | 5,207 / 4,222 | 9,156 / 8,239 | 3,153 / 3,002 | 6,666 / 6,250 |

SAP’s 2025 FCF definition is OCF less intangible/PP&E purchases, plus sale proceeds, less lease payments; interest is excluded from OCF. It is not a clean levered owner-earnings proxy. FY2025 share compensation was €1.695bn; IFRS earnings retain it.

The [Q2 statement](https://www.sap.com/docs/download/investors/2026/sap-2026-q2-statement.pdf) shows cloud growth with pressure underneath. Cloud revenue rose 22%, backlog 27%, total revenue 9% and IFRS operating profit 8%; cloud gross margin fell 0.5 point to 74.3%. H1 FCF rose 5%. Licenses fell 32% and support 8% as migration cannibalized legacy revenue; Reltio added less than one point to backlog growth.

FY2026 guidance is €25.8–26.2bn cloud revenue, €11.8–12.2bn non-IFRS operating profit and about €10bn FCF. Dremio/Prior Labs cut the profit range by €0.1bn. SAP expects backlog growth to decelerate. At FY2025 SAP had €3.381bn net liquidity before leases. By June it had repurchased 16.28m shares for €2.6bn under a €10bn program.

## Scarce asset and data-rights audit

| Input | Origin / owner | Exclusive? | Retrieval / inference rights | Training / cross-customer rights | Labels / quality | Replication threat |
|---|---|---|---|---|---|---|
| ERP transactions, master data and documents | Customer; SAP processes/hosts in cloud or software runs on-premises | Tenant context unique; SAP does not own customer facts | Contract permits processing for subscribed service | [SAP AI FAQ](https://www.sap.com/documents/2024/10/447a6b1f-dd7e-0010-bca6-c68f7e60039b.html): data may improve existing subscribed features; new-feature use is subject to a product-development schedule and opt-out | Approvals, postings, fulfillment and exceptions are frequent labels; customization and dirty master data impair them | Oracle, Microsoft, Workday and customer data platforms have overlapping context |
| Process schemas, authorization roles, workflow/application code | SAP and customer customization | SAP standard schemas/code proprietary; custom configurations customer-specific | SAP can execute within configured roles | SAP internal product telemetry rights vary by cloud agreement; on-prem data access is narrower | Strong audit and completion states; local custom code introduces drift | Migration is costly, but open standards and integrators can map processes |
| Cross-customer benchmarks and de-identified patterns | Derived from customers subject to contracts | Potentially differentiated, scope unknown | Product-specific | FAQ establishes a conditional legal route, not universal permission; customers can opt out | Scale could improve anomaly/benchmark models; representativeness unknown | Cloud hyperscalers and sector platforms have alternative pools |
| Third-party foundation models through AI Core | Model vendors | Non-exclusive | SAP selects embedded models; customers can choose models for custom extensions | SAP says customer data is not shared to train third-party models and is processed without provider retention | Model quality vendor-dependent | Providers and rivals can offer the same base models; bargaining/inference cost risk |
| Business network/supplier and HR context | Customers, employees, suppliers and SAP network contracts | Network graph partly differentiated | Permission depends on module, role and purpose | Sensitive personal/procurement data adds GDPR and purpose-limitation constraints | Decisions and exceptions observable; bias and consent matter | Coupa, Oracle, Workday and cross-vendor agents compete |

The moat is execution rights and semantic integration, with conditional pooled learning in opted-in cloud services. Customers may opt out of new-feature data use; SAP says third-party models do not train on or retain customer prompts. Trust protections limit universal feedback claims.

## Mechanisms, deployment and challengers

**1. Joule agents execute finance, procurement, HR and service workflows (agentic execution).** [SAP’s Joule page](https://www.sap.com/products/artificial-intelligence/ai-agents.html) describes assistants coordinating agents across processes. The scarce asset is the configured process graph, roles, transaction state and audit trail. Quality-adjusted output is an authorized, auditable transaction. SAP can capture value through premium packages, cloud migration and higher renewal or suite scope.

SAP’s [FY2025 results](https://news.sap.com/2026/01/sap-announces-q4-and-fy-2025-results/) say Business AI appeared in two-thirds of Q4 cloud order entry. This is E2 bundling, not active use or incremental price; cloud conversion confounds it. SAP discloses no AI ARR, active users, completed workflows, exception rates or model cost.

The strongest named customer is [Bosch Digital](https://news.sap.com/2026/07/sap-business-ai-release-highlights-q2-2026/): SAP reports 20% developer productivity improvement and 15–20% faster unit testing. This is E2. No baseline definition, sample, control, quality, cost or cash conversion supports E3; it also tests assistance, not autonomous transactions.

**2. Internal productivity (generative and agentic assistance).** Management attributes efficiency partly to AI; FY2025 non-IFRS profit outgrew revenue. Restructuring, lower cash payments/share awards, currency, pricing and cloud mix dominate the observed bridge. No controlled output-per-employee or AI-cost reconciliation exists: E1–E2, not cash-causal evidence.

**3. Cloud-suite demand catalyst (revenue).** Agents may accelerate S/4HANA and Data Cloud adoption. Backlog growth and AI order inclusion make this plausible, but support decline, maintenance deadlines and migration policy are independent drivers. Dremio/Prior Labs add capability while diluting 2026 profit by more than €100m: the option is not free.

The decisive challenge is the [DSAG Investment Report 2026](https://impulsant.dsag.de/formate/pressemeldung/dsag-investment-report-2026-companies-are-investing-more-selectively-ai-is-becoming-established-cloud-computing-is-being-put-to-the-test/). Among 198 German-speaking user firms, 43% had implemented AI; among implementers, 77% reported production/use with non-SAP solutions and 3% with SAP. Also, 79% cited SAP investment cost-effectiveness and 70% license design as challenges. Sample and denominator limit generalization, but broad SAP AI production is not established.

Oracle Fusion, Microsoft Copilot and independent agents compete. SAP’s advantage is governed execution inside the record system; its threat is a cross-vendor agent that owns intent and calls SAP only to commit transactions.

## Evidence ledger

| Claim | Type | Source/date; section | Scope / stage | Confounder |
|---|---|---|---|---|
| FY2025 revenue €36.8bn, IFRS operating profit €9.617bn | Fact | Integrated Report, 26 Feb 2026; pp. 52–64 | Company baseline, E2 | 2024 restructuring comparison |
| Q2 cloud revenue +22%, backlog +27%, cloud gross margin −0.5pp | Fact | Q2 statement, 23 Jul 2026; pp. 1–3 | Company baseline, E2 | FX, acquisitions, migration |
| Business AI included in two-thirds of Q4 cloud order entry | Management claim | FY2025 results, 29 Jan 2026 | Contract inclusion, E2 | Bundling; price and usage unknown |
| Bosch developer productivity +20%; testing +15–20% | Customer result reported by SAP | Release highlights, Jul 2026 | One customer/task, E2 | No comparator design, quality or cost |
| Only 3% of AI implementers use SAP AI in production vs 77% non-SAP | Independent user survey | DSAG, 26 Feb 2026 | 198 DACH firms, E2 | Ambiguous multiple-response denominator, regional mix |
| Conditional rights permit improvement/new features with schedule and opt-out | Fact | SAP AI FAQ, 2025; customer data section | Contract framework, E1 | Individual agreements/modules differ |
| Third-party models do not train/retain customer prompts under SAP arrangement | SAP policy claim | SAP AI FAQ, 2025 | Embedded SAP AI | Customer direct model use outside agreement differs |
| Dremio/Prior Labs dilute 2026 profit >€100m | Management forecast | Q2 statement, 23 Jul 2026; outlook | AI investment economics | Integration upside not yet visible |
| H1 FCF +5% despite revenue +8% | Fact | Q2 statement, 23 Jul 2026; p. 3 | Cash baseline | Seasonality and working capital |
| Support/license revenue fell 8%/32% in Q2 | Fact | Q2 statement, 23 Jul 2026; p. 2 | Conventional transition risk | Intended cloud cannibalization |

## KPI contract and retained economics

| KPI | Baseline / comparator | Eligible workload | Quality control | Known result / next event |
|---|---|---|---|---|
| Authorized end-to-end workflows completed per labor hour | Same SAP process without Joule; randomized or phased rollout | AI-enabled transactions by process and tenant | Unauthorized action, rollback, exception and audit failure | Unknown; seek tenant cohort in Q3/FY2026 |
| AI net new contract value / renewal | Contract without AI or pre-AI cohort | Cloud contracts with paid AI entitlement | Include suite migration, discount, seats and model cost | Two-thirds inclusion only; price unknown |
| Total customer spend after seat/interface change | Matched non-AI renewals | AI-active accounts | Include third-party agent use, consulting and support | Unknown; observe two renewal cycles |
| Developer output at equal quality | Bosch pre-Joule/matched developers | Joule-enabled engineering tasks | Defects, security, rework, cycle time | 20% claim lacks protocol; require logs and cash realization |

The research materiality convention is 5% of normalized FY2025 non-IFRS operating profit: **€521m annual net benefit within five years**. Illustrative internal-cost bridge on €17.1bn combined FY2025 R&D, sales/marketing and G&A: 10% eligible task efficiency × 50% realization × 50% retained share − €300m recurring AI/implementation expense = **€128m**, only 1.2% of normalized profit. A strong 15% × 60% × 60% − €300m = **€624m**, above the hurdle. This shows why task productivity must convert into broad capacity or valuable output.

Illustrative revenue route: 4% incremental uplift on €21.023bn FY2025 cloud revenue × 75% contribution margin − €100m incremental model/support cost = **€531m**. This clears the hurdle, but two-thirds order inclusion does not establish 4% incremental pricing, retention or volume. Cost and revenue bridges must not count the same released labor twice.

## Valuation and reverse valuation

Xetra SAP closed at **€177.26 on 11 September 2026** ([Investing.com dated quote](https://www.investing.com/equities/sap-ag)); Deutsche Börse confirms the ordinary security and ISIN on its [SAP listing page](https://live.deutsche-boerse.com/equity/sap-se). FY2025 issued shares were 1.229bn less 60.9m treasury; another 16.28m were repurchased by 30 June 2026. Ignoring intervening reissuance gives approximately 1.152bn economic shares and €204bn equity value. This share bridge must be reconciled before G3 passes.

SAP does not guide IFRS EPS, so the model assumes **€7.00 normalized 2026 EPS**, near twice H1 EPS of €3.55. FY2025 EPS is distorted by lapping €3.1bn restructuring expense and equity gains. The model treats 2026 as year 1, compounds through 2030, discounts at 9%, includes a €2.50 growing dividend and retains stock compensation.

| Case | Conventional business / AI change | 2026–30 EPS CAGR; terminal P/E | Approx. PV/share | Key sensitivity |
|---|---|---:|---:|---|
| Bear | Slow conversion, zero AI uplift, margin/model pressure | 4%; 18× | **€106** | Cloud growth and multiple |
| Base | Cloud transition supports conventional growth; no separate AI credit | 8%; 23× | **€154** | Normalized starting EPS |
| Bull | 9% conventional plus 5pp conditional AI/capture contribution | 14%; 28× | **€228** | Paid attach, renewal and margin evidence |

Formula: PV = discounted annual dividends + [€7.00 × (1+g)^4 × terminal P/E] / 1.09^5. At €177.26, the reverse requirement is **12.1% 2026–30 EPS CAGR** at 23×, **15.9%** at 20×, or **8.8%** at 26×. Thus the price requires durable double-digit earnings growth unless a premium multiple persists. AI may help deliver it, but current evidence does not prove incremental cash capture.

## Risks, falsifiers and alternative

Positive hypothesis: SAP’s process graph and execution rights let Joule complete high-value transactions, raising suite scope and retention while internal agents expand margins. Configured process logic is costly to reproduce.

Negative hypothesis: customers prefer non-SAP agents, resist license economics and expose SAP through open interfaces. SAP becomes a costly record layer while model vendors control interaction. DSAG is early supporting evidence.

Falsifiers:

1. SAP AI production use remains below 10% in credible user surveys through 2027 while non-SAP agents keep widening their lead.
2. AI-included renewal cohorts show no incremental net contract value, or cloud gross margin falls below 72% because inference/support and acquisition costs absorb price.
3. Core failure: cloud backlog growth falls to low teens while support/license decline accelerates, leaving total revenue below mid-single-digit growth.

Oracle is the integrated-suite peer; Microsoft plus independent agents is the substitute. Waiting for AI ARR, workflow and renewal evidence is reasonable.

## Priors, revisions, gates and confidence

| Dimension | Original prior | Proposed revision | Reason |
|---|---:|---:|---|
| Scarce asset | 5 | 5 | Deep process schemas, permissions and installed systems remain costly to replace |
| AI leverage | 4 | 4 | Core workflows are addressable, but autonomous scope is constrained by controls |
| Feedback | 4 | 3 | Frequent outcomes; opt-outs, tenant isolation and on-prem deployments limit pooling |
| Testability | 4 | 4 | Fast workflow KPIs are measurable; current evidence lacks controls |
| Distribution | 5 | 5 | Large installed base and cloud migration channel |
| Capture | 5 | 3 | Suite pricing and execution control help; DSAG shows non-SAP adoption and license friction |

Revised structural score: **80/100** versus 91 prior. With capture weighted 30% and feedback 5%, score is also 80.

| Gate | Status | Reason |
|---|---|---|
| G0 candidate | Pass | Explicit asset, mechanisms, capture route and falsifiers |
| G1 qualified business | Pass, moderate/high | Recurring cloud/support franchise, net liquidity and strong cash generation; litigation/governance need lead audit |
| G2 operating thesis | Pass, low/moderate | E2 order/deployment evidence and clear route to controlled workflow tests; material production breadth weak |
| G3 valued opportunity | Blocked | Dated price and scenarios exist, but normalized EPS and point share count are assumptions, and AI cash contribution is absent |
| G4 portfolio eligible | Blocked | No sizing/correlation review; G3 and E4 absent |

Confidence: **mechanism high; deployment low/moderate; capture low; valuation low/moderate**.

## Source register

1. SAP, [2025 Integrated Report](https://www.sap.com/docs/download/investors/2025/sap-2025-integrated-report.pdf), 26 Feb 2026, pp. 38, 50–68, 74, 213–14, 267–70; audited, restructuring-distorted.
2. SAP, [Q2 2026 statement](https://www.sap.com/docs/download/investors/2026/sap-2026-q2-statement.pdf), 23 Jul 2026, pp. 1–5, 22; outlook is management forecast.
3. SAP, [FY2025 results](https://news.sap.com/2026/01/sap-announces-q4-and-fy-2025-results/), 29 Jan 2026; AI price/use denominator absent.
4. SAP, [Business AI FAQ](https://www.sap.com/documents/2024/10/447a6b1f-dd7e-0010-bca6-c68f7e60039b.html), ©2025; individual agreements control.
5. SAP, [Joule agents](https://www.sap.com/products/artificial-intelligence/ai-agents.html), retrieved 12 Sep 2026; product scope.
6. SAP, [Q2 AI highlights](https://news.sap.com/2026/07/sap-business-ai-release-highlights-q2-2026/), Jul 2026; Bosch claim lacks protocol.
7. DSAG, [Investment Report 2026](https://impulsant.dsag.de/formate/pressemeldung/dsag-investment-report-2026-companies-are-investing-more-selectively-ai-is-becoming-established-cloud-computing-is-being-put-to-the-test/), 26 Feb 2026; independent n=198 DACH survey.
8. SAP, [Generative AI Hub](https://www.sap.com/products/artificial-intelligence/generative-ai-hub.html), retrieved 12 Sep 2026; capability, no economics.
9. Deutsche Börse, [SAP security](https://live.deutsche-boerse.com/equity/sap-se), retrieved 12 Sep 2026; primary identity, dynamic quote absent.
10. Investing.com, [SAP Xetra quote](https://www.investing.com/equities/sap-ag), 11 Sep 2026; secondary dated price.

## Handoff for lead review

- **Three decisive claims to verify:** (1) DSAG’s 3% SAP versus 77% non-SAP production-use comparison and denominator; (2) two-thirds Q4 cloud-order inclusion is E2 commercial bundling, not paid active deployment; (3) €177.26 implies 12.1% EPS CAGR at 23× using the stated €7 normalized starting EPS.
- **Strongest counterargument:** DSAG is a 198-company DACH sample skewed toward complex/on-prem estates; global cloud customers may be adopting SAP AI far faster, and order-entry/backlog may precede usage evidence.
- **Blocking questions:** AI ARR and paid attach; active users/completed workflows; exception and rollback rates; full model cost; customer-specific opt-in rates; point share count after repurchase/reissuance; sustainable IFRS EPS; acquisition funding/net debt.
- **Provisional disposition:** Watch / operating-thesis candidate. G3 and G4 blocked; E3/E4 absent.
- **File written:** `research/batch-01/dossiers/06-sap.md`.
