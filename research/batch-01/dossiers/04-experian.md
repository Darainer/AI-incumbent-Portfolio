# Experian (C031) — initial evidence dossier

**Unreviewed research-agent output; lead reviewer owns the final judgment.**  
**Cutoff/access date:** 12 September 2026. **Issuer/security:** Experian plc ordinary US$0.10 shares, London Stock Exchange **EXPN**, quoted in GBX (pence sterling); reporting currency USD. No ADR is used. **Price:** 2,782 GBX (£27.82) on 11 September 2026, LSE delayed quote. At £1=US$1.3501 on that date, price is about US$37.56. **Industry:** F05 credit data, exchanges and financial intelligence.

## Provisional conclusion

Experian owns a scaled, frequently refreshed decision asset, but much of the value is classical credit analytics already in earnings. FY2026 disclosures establish production use of Ascend, 3.5m engagements with consumer assistant EVA, and commercially growing AI-enabled health/credit workflows. They do not isolate incremental generative/agentic revenue, controlled risk lift, or net cash economics. Rights are narrower than “data ownership”: lenders furnish many records, customers own their own context, consumers permission bank data, and cross-customer model-training rights are not disclosed. At 2,782p the stock is about 20.9x FY2026 benchmark EPS and 21.8x benchmark FCF; a simple cash-flow model requires roughly 10% five-year FCF/share growth at a 9% hurdle. **Provisional disposition: watch / G2 pass, G3 pass with low confidence; no purchase recommendation.** Mechanism confidence high for established analytics but moderate for incremental GenAI; deployment moderate; capture low-moderate; valuation moderate-low.

## Conventional business and dated financial record

Experian sells credit data, scores, decision analytics, fraud/identity tools and software to financial institutions and vertical customers; Consumer Services sells subscriptions and monetizes marketplaces. Financial Services is 53% of FY2026 revenue, Verticals 20% and Consumer Services 27%. North America supplies 67% of revenue, Latin America 15%, UK/Ireland 11%, and EMEA/APAC 7%. This mix creates recurring data/workflow economics but exposes results to lending volumes, regulation, data accuracy, breach-response contract run-off and FX.

| Metric | Period / publication | Result | Comment |
|---|---|---:|---|
| Total / ongoing revenue | FY ended 31 Mar 2026; annual report 17 Jun 2026 | US$8.445bn / US$8.425bn | Ongoing organic growth 8%; acquisitions contributed |
| Statutory operating profit / margin | FY2026 | US$2.045bn / 24.2% | After US$348m exceptional/benchmark adjustments |
| Benchmark EBIT / margin | FY2026 | US$2.397bn / 28.6% | Non-GAAP; ongoing EBIT US$2.407bn |
| Operating cash inflow | FY2026 | US$2.239bn | Statutory cash flow |
| Benchmark operating / free cash flow | FY2026 | US$2.221bn / US$1.583bn | FCF after US$198m interest, US$438m tax and US$2m NCI dividends |
| Intangible / PP&E purchases | FY2026 | US$677m / US$49m | Capitalized development is economically important |
| Diluted statutory / benchmark EPS | FY2026 | 163.4c / 178.7c | Basic benchmark EPS 179.8c; valuation uses diluted where appropriate |
| Diluted weighted shares | FY2026 | 919m | FY2027 guidance indicated 880–885m, reflecting buybacks |
| Net debt | 31 Mar 2026 | US$5.179bn; 1.7x benchmark EBITDA | US$2.510bn undrawn committed facilities |
| FY2027 guidance | May 2026; reaffirmed 16 Jul 2026 | 6–8% organic revenue, 8–11% total revenue, +50bp benchmark EBIT margin, capex ~8% revenue | Q1 organic growth 7% |

Sources: [FY2026 annual report](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/reports/2026/experian-annual-report-2026.pdf), pp. 61–68, 183, 191–92, 210–11; [Q1 FY2027 update](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/experian-fy27-q1-trading-update-announcement.pdf), 16 July 2026.

With zero additional AI improvement, Experian remains a growing oligopoly-scale bureau and analytics platform. FY2020–26 revenue and benchmark EBIT CAGRs were about 8% and 10%, respectively; however, acquisitions, credit cycles, new datasets and pre-existing ML are all in that baseline. FY2026 included US$792m across four acquisitions; two US$1bn buyback programs were announced in January and May 2026. Buybacks can raise per-share growth while increasing the importance of price discipline. Q1 Consumer Services organic revenue fell 2% due to two mass-data-breach contracts winding down, and EMEA/APAC grew only 1%; those are useful conventional-business negatives.

## Asset and data-rights audit

| Input | Origin / owner | Exclusive? | Retrieval / inference | Training / pooled learning | Quality / labels | Replication threat |
|---|---|---|---|---|---|---|
| US credit files: 250m+ records, ~12,000 furnishers, 1.3bn monthly updates | Banks, lenders, collectors and public sources; Experian curates | Experian compilation proprietary; underlying tradelines often sent to rival bureaus | FCRA-defined permissible-purpose products; exact client contracts vary | Undisclosed; possession does not prove unrestricted training | Defaults/payments are frequent outcomes, but reporting errors and drift matter | Equifax/TransUnion have parallel files; lenders have own performance data |
| Expanded FCRA / Clarity alternative-credit data | Acquired/specialty furnishers; 68m+ consumers | More differentiated, not necessarily exclusive | Regulated use | Unknown | Thin-file and alternative-finance labels may add lift | TransUnion/Equifax and open-banking vendors |
| Consumer-permissioned bank/rent/utility data | Consumer and account providers | Relationship-specific | Explicit consumer connection supports the current decision | Consent duration, retention, model-training and cross-customer use unknown | Cash-flow and payment recency can be predictive | Plaid/open banking, rival bureaus, lender direct access |
| Lender customer portfolios, criteria and decisions | Customer | Customer-specific | Ascend can combine these with Experian data | Cross-customer reuse rights unknown | Approval, repayment and fraud outcomes valuable if observable | Lenders can build models internally or use FICO/cloud tools |
| Consumer membership/marketplace behavior | Consumer/Experian interaction | First-party access, subject to law/choice | Personalization and offer matching disclosed | Training scope unknown | Click, approval and conversion are rapid labels but may optimize commission rather than borrower welfare | Credit Karma/Intuit, bank marketplaces, ChatGPT distribution |

The annual report says Experian sources from reputable companies with appropriate permissions, audits provenance, and stops sourcing providers that will not improve quality. Its [Global Data Principles](https://www.experianplc.com/responsibility/treating-data-with-respect) emphasize minimum necessary data, legitimate purposes, correction/deletion and lifecycle controls. These are governance claims, not evidence of exclusivity or pooled-learning permission. The unresolved rights question warrants lowering the feedback prior.

## Mechanisms, deployment and challengers

**1. Credit/fraud model development and decisioning (classical ML plus generative assistance).** Curated bureau/alternative data → build, validate, explain and deploy lender models in Ascend → faster model cycles and potentially better approvals/losses → platform/data fees and retention. Ascend's sandbox offers 20+ years of data on 245m consumers. The FY2026 report says its Model Risk Management assistant uses an LLM grounded in cross-jurisdiction regulation; documentation that took weeks can be completed in days, with humans retaining final oversight. This is a management result without sample, error rate or matched design, so E2 deployment, not E3. Q1 says North American Financial Services growth was driven partly by Ascend analytics and UK Ascend revenue continued to increase, but no product revenue is given.

**2. Consumer financial co-pilot and offer matching (generative assistance / emerging agentic execution).** Permissioned consumer credit/cash-flow context → explain position and match lender-defined offers → higher qualified applications and marketplace commission, potentially better inclusion. EVA recorded nearly 3.5m engagements by FY2026. Experian Activate launched 10 September 2026 for 90m+ marketplace members and uses real-time, permissioned bank data and lender rules. “Engagements” and launch establish E1/E2, not quality-adjusted approvals, loan performance or incremental contribution.

**3. Health registration automation (agentic workflow).** Patient/coverage data → identify missing registration/insurance fields → reduce manual work and claim denials → software/data revenue. Q1 management reported ongoing adoption of AI-powered Patient Access Curator and called it a growth driver. Eligible encounters, autonomous completion, denial rate and economics are absent.

Equifax and TransUnion are direct incumbent rivals with equivalent access to broad bureau records, decisioning and explainable ML. TransUnion's TruIQ explicitly supports credit strategies, alternative data and automated approvals; lenders can also use FICO and their own repayment records. Open-banking providers weaken exclusivity by letting consumers send fresh account data directly. ChatGPT distribution can expand Experian's marketplace, but it also risks making the agent the customer interface and capturing bargaining power. Experian's September app/Activate releases demonstrate this two-sided risk.

The most decision-relevant adverse evidence is the CFPB case. The Bureau's updated enforcement page says its second amended complaint alleges inadequate reinvestigations, failure to remove unverifiable data and improper reinsertion; discovery was ongoing as of March 2026. These are allegations, not adjudicated facts, but directly challenge the quality of the scarce asset and could add remediation/regulatory cost. The annual report itself identifies data loss/misuse, data quality, competition and regulation as principal risks.

## Evidence ledger

| Claim | Type | Source/date; section | Scope / stage | Confounder |
|---|---|---|---|---|
| FY2026 ongoing revenue +8% organic; EBIT margin +50bp | Fact | Annual report, 17 Jun 2026, pp. 43, 63 | Group economics | acquisitions, mix, credit cycle, prior ML |
| Q1 FY2027 organic growth 7%; Ascend and health AI named drivers | Management claim | Q1 update, 16 Jul 2026, pp. 1–2 | Production association, E2 | no contribution split; stable client activity |
| Model-risk documentation fell from weeks to days | Management claim | Annual report p.16 | Customer workflow, E2 | sample/error/comparator absent; human review |
| EVA produced ~3.5m engagements | Management claim | Annual report p.31 | Usage, E2 | engagements are not actions, retention or profit |
| Activate uses real-time permissioned cash-flow data for offer matching | Fact about launch/capability | Experian release, 10 Sep 2026 | E1/early E2 | no observed approvals, losses or revenue |
| 250m+ files, ~12,000 furnishers, 1.3bn monthly updates | Management fact | Annual report p.21 | Asset scale, E1 | not exclusive; accuracy varies |
| CFPB alleges defective dispute/reinsertion practices | Regulatory allegation | CFPB case page, updated 13 Mar 2026 | Adverse quality evidence | unresolved litigation; not adjudicated |
| TransUnion offers comparable decision management | Competitor fact | TruIQ page, accessed 12 Sep 2026 | Challenger E1/E2 claims | promotional, no head-to-head test |

## KPI contract and retained-economics bridge

| KPI | Baseline / comparator | Eligible population | Quality constraint | Known result | Review event |
|---|---|---|---|---|---|
| Incremental approval at fixed expected loss/fairness | Existing lender model; same lawful dataset, then add Experian-only attributes | Applicants scored through Ascend/Activate | realized 12–24m losses, adverse impact and calibration | Unknown | lender cohort maturity / FY2027 results |
| Model deployment time and cost | existing production stack, including classical ML | all models entering governance | documentation error, exceptions, regulator acceptance | weeks-to-days claim; uncertainty unknown | controlled client study |
| Paid AI attach/net retention | pre-launch customer cohort vs matched customers | Ascend and health platform clients | full model/cloud/support cost | Unknown | FY2027 renewals |
| Marketplace contribution per active member | pre-EVA/Activate matched cohort | eligible members and offers | approval quality, complaints and lender economics | 3.5m engagements only | 2027 cohort disclosure |

**Materiality convention:** 5% of FY2026 ongoing benchmark EBIT is about US$120m. Cost illustration: US$1.0bn eligible client/model-operations pool × 20% efficiency × 50% realization × 50% retained share − incremental recurring AI cost **K** = US$50m − K, insufficient alone. A non-overlapping revenue/decision path must produce contribution ≥US$120m + K; at 50% net contribution and K=0, that requires US$240m incremental revenue after cannibalization. Alternatively, improved marketplace matching needs the same contribution through qualified volume/commission net of credit-cycle and serving costs. All pool, efficiency, capture and K inputs are unknown; these are break-even requirements, not forecasts. Existing technology cost is already in FY2026 profit and should not be subtracted twice.

## Valuation and reverse valuation

At 2,782p and 919m FY2026 diluted shares, equity value is about £25.57bn / US$34.52bn using US$1.3501/£. Adding US$5.179bn net debt gives provisional EV US$39.70bn. The observed Google/LSE market-cap fields differ because buybacks lowered current shares; the bridge deliberately uses the filed diluted denominator and should be refreshed with issued shares after buybacks. Price/benchmark diluted EPS is 21.0x; price/benchmark FCF is 21.8x (US$1.583bn / 919m = US$1.723/share).

Five-year DCF: value = annual FCF/share grown at *g*, discounted at 9%, plus year-5 FCF × (1+terminal growth)/(9%−terminal growth), discounted five years. Starting FCF/share US$1.723; USD values converted at constant US$1.3501/£ solely for comparability.

| Case | Conventional / AI change | 5y growth; terminal | Value/share | Interpretation |
|---|---|---:|---:|---|
| Bear | weaker lending/mix; AI net zero/adverse | 2%; 2% | US$25.10 / £18.59 | meaningful downside |
| Base | durable conventional growth; current AI already embedded | 7%; 2.5% | US$32.91 / £24.38 | below price |
| Bull | Ascend/marketplace capture and buyback accretion | 10%; 3% | US$39.80 / £29.48 | modest upside, evidence-dependent |

At US$37.56, a 9% discount rate and 2.5% terminal growth imply about **10.2% annual FCF/share growth for five years** (interpolation; 10% gives US$37.28). A 10% return hurdle raises the required growth. Key business sensitivity is lending/marketplace volume and realized credit outcomes; valuation sensitivity is discount/terminal rate. This is a demanding price for an E2 incremental-AI thesis even after the 2026 share decline.

## Risks, falsifiers, priors and gates

Strongest positive hypothesis: Experian combines legally usable bureau and permissioned data with real-time workflows, allowing it to sell more decisions and improve models faster across an installed base. Strongest negative: bureau inputs are nonexclusive, lenders/competitors own comparable data and outcomes, regulation restricts reuse, and customer/platform suppliers capture the gain while data-quality liabilities grow.

Three falsifiers: (1) proprietary attributes show no material incremental approval/loss lift over rival bureau plus open-banking data in matched tests; (2) Ascend AI attach and adopter retention fail to improve after two renewals net of pricing/acquisition mix; (3) incremental AI contribution cannot credibly approach US$120m by FY2031 after cloud/model/support costs. TransUnion, Equifax and FICO are peers; waiting for loss-seasoned cohorts and AI revenue disclosure is a valid alternative.

| Dimension | Original prior | Proposed revision | Reason |
|---|---:|---:|---|
| Scarce asset | 5 | 4 | scale/refresh verified; much underlying data nonexclusive |
| AI leverage | 5 | 4 | core decisions affected, but established ML already baseline |
| Feedback | 5 | 3 | frequent outcomes plausible; access and pooled rights unknown |
| Testability | 4 | 4 | rapid model/time tests feasible; credit losses need seasoning |
| Distribution | 5 | 5 | broad lender and 215m+ free-member channels |
| Capture | 4 | 3 | platform growth association; net incremental economics absent |

Weighted posterior is **76/100** versus prior 94; judgment, not probability. **G0 pass. G1 pass with rights/litigation caveats:** financially resilient but leveraged and dependent on regulated data accuracy. **G2 pass:** several management-reported production deployments and a credible test route; strongest stage E2. **G3 pass with low confidence:** dated quote, FX, denominator, downside and reverse valuation supplied, though current post-buyback shares need refresh. **G4 fail/not assessed.** Confidence: mechanism 4/5 for analytics, 3/5 for incremental GenAI; deployment 3/5; capture 2/5; valuation 3/5.

## Source register

1. [Experian FY2026 annual report](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/reports/2026/experian-annual-report-2026.pdf), published 17 Jun 2026; accessed 12 Sep 2026. Primary audited financials, strategy, asset and management-use-case claims.
2. [Experian Q1 FY2027 trading update](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/experian-fy27-q1-trading-update-announcement.pdf), 16 Jul 2026; accessed 12 Sep 2026. Latest trading/deployment update; unaudited and no product economics.
3. [Experian Ascend Platform](https://www.experian.com/business/products/ascend), undated live page; accessed 12 Sep 2026. Capability and commissioned ROI claims; promotional, composite design.
4. [Ascend Analytical Sandbox](https://www.experian.com/business/products/ascend-analytical-sandbox), undated live page; accessed 12 Sep 2026. Dataset/product scope; no independent lift.
5. [Experian Activate launch](https://www.experianplc.com/newsroom/press-releases/2026/experian-launches-ai-enabled-decisioning-platform-bringing-real-), 10 Sep 2026; accessed 12 Sep 2026. Primary launch and permissioned-data mechanism; no outcomes.
6. [Experian Global Data Principles](https://www.experianplc.com/responsibility/treating-data-with-respect), undated live page; accessed 12 Sep 2026. Governance policy; does not specify training rights.
7. [CFPB Experian enforcement action](https://www.consumerfinance.gov/enforcement/actions/experian-information-solutions-inc/), filed 7 Jan 2025, page updated 13 Mar 2026; accessed 12 Sep 2026. Primary allegations and procedural status; unresolved.
8. [TransUnion TruIQ Decision Management](https://www.transunion.com/solution/truiq/enabling-technology/decision-management), undated live page; accessed 12 Sep 2026. Primary rival capability/customer claim; no controlled comparison.
9. [LSE EXPN quote](https://www.londonstockexchange.com/stock/EXPN/experian-plc/company-page), 2,782 GBX on 11 Sep 2026; accessed 12 Sep 2026. Delayed ordinary-share quote.
10. [GBP/USD historical data](https://www.investing.com/currencies/gbp-usd-historical-data), 1.3501 on 11 Sep 2026; accessed 12 Sep 2026. Secondary FX input; replace with official fix if required.

## Handoff

**Reviewer should verify:** (1) current issued shares after the two buybacks and resulting EV/per-share denominator; (2) whether Ascend/Patient Access growth is incremental AI rather than platform migration, pricing or classical analytics; (3) the exact rights to train/improve models across furnished, customer and permissioned data. **Strongest counterargument:** parallel bureau datasets and lender-owned outcomes prevent unique lift while regulation, accuracy remediation and hyperscaler/interface bargaining absorb the surplus. **Blocking questions:** AI revenue/attach/gross margin, controlled marginal lift at fixed loss/fairness, consent/retention/cross-customer rights, cohort renewals, inference/cloud cost and CFPB-case exposure. **Provisional disposition:** watch; operating thesis qualifies, price requires strong per-share compounding. **File written:** `research/batch-01/dossiers/04-experian.md`.
