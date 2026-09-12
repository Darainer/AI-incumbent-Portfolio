# C016 — Swiss Re evidence dossier

**Unreviewed agent work.** Swiss Re Ltd; registered shares SREN on SIX Swiss Exchange, CHF quote; group reporting USD. Cutoff/retrieval 12 September 2026. Latest period H1 ended 30 June 2026, published 6 August 2026. FY2025 annual report is the latest audited report, but H1 2026 provides the freshest extracted baseline.

## Ordinary business and resilience

Swiss Re writes P&C and life/health reinsurance and commercial primary insurance, and supplies risk data/analytics. Its economic assets are global underwriting relationships, long-tail claims histories, catastrophe and mortality expertise, and capital able to absorb volatile risks. Premium and investment income compensate for claims, expenses and cost of capital. AI can sharpen selection, pricing and claims triage, but a low observed loss ratio may instead reflect price cycle, mix, reserve release or benign catastrophes.

The [H1 2026 report](https://www.swissre.com/investors/half-year-report-2026-online.html) reported group net income **$2.8bn**, up 9%, ROE **22.7%**, investment result $2.3bn and ROI 4.0%. P&C Re net income was $1.4bn and combined ratio **76.7%**; Corporate Solutions net income $490m and combined ratio **86.1%**; L&H Re net income $1.0bn. Estimated Swiss Solvency Test ratio was **264%** at 1 July, above the 200–250% target range. Shareholders' equity fell after a $2.4bn ordinary dividend and $0.7bn treasury purchases. Favorable prior-year claims development and lower-than-expected natural catastrophes helped Corporate Solutions; low large-cat experience helped P&C. Those are explicit confounders, not evidence of algorithmic lift.

Management targets $4.5bn net income for 2026, a multi-year ROE above 14%, and began a $500m annual buyback program, conditional on performance; these are targets, not facts. Reinsurance renewals face price pressure, while climate, casualty inflation and model error can create tail losses. L&H assumption reviews show historical data does not remove reserve uncertainty.

## Data rights and replication

| Input | Origin/owner | Permitted inference/training | Quality/labels | Threat |
|---|---|---|---|---|
| Treaty submissions and cedent portfolios | Cedents; Swiss Re receives under contract | Underwriting/servicing use; pooled model learning depends on treaty and privacy terms, undisclosed | Broad exposure, inconsistent schemas and reporting lag | Munich Re/Hannover Re receive similar submissions |
| Claims and reserve histories | Insurer/claimants/Swiss Re contractual records | Claim administration and actuarial use; personal/sensitive fields regulated | Ultimate-loss labels can take years and are revised | Industry catastrophe vendors and brokers aggregate data |
| Proprietary hazard/risk models | Swiss Re plus licensed geospatial/climate inputs | Internal and client-tool use; third-party license restrictions apply | Physically informed but non-stationary climate/cyber risk | Moody's RMS, Verisk and open models |
| Client-uploaded Impact+ data | Client-specific | Tool page says clients can upload portfolio data; reuse/training permission unknown | Useful for portfolio decisions, client-dependent | Brokers and analytics platforms can offer multi-carrier view |

The [Impact+ product page](https://analytics.swissre.com/details/coin) says applications combine Swiss Re risk data/models with external data and can accept uploaded client portfolios. It does not say Swiss Re may train across clients. Contract wording, retention and output ownership remain unknown. Reinsurance data breadth is valuable but cedents and brokers can multi-home.

## Mechanisms and competitive challenge

1. **Underwriting/portfolio optimization (classical ML).** Exposure, claims and hazard models → select, price and aggregate risks → lower risk-adjusted loss at equal volume/capital → underwriting income. Impact+ documents portfolio analytics and pricing-model support. This is E1/E2 product use where clients deploy it, but no controlled loss result or retained pricing gain is disclosed.
2. **Claims triage (classical ML).** Claim features and past outcomes → prioritize cases for assessment → faster closure/fraud detection at equal leakage/customer outcome → lower expense/loss. Impact+ explicitly mentions ML claims triage, establishing capability E1. Eligible claim count, precision/recall and cash savings are absent.
3. **Generative employee assistance.** Contract, submission and claims documents → summarize/draft and retrieve → more underwriter decisions per employee → expense benefit. Strategy commentary says AI is being integrated, but production penetration and error rates are undisclosed. Treat as E1, not company-wide productivity proof.

**Munich Re** is the incumbent challenger, with comparable global loss data, risk capital and analytics. **Moody's RMS/Verisk** are substitutes that sell catastrophe models across carriers; brokers can capture cross-market data and steer risks. Cedents can retain better risks or demand lower price, and model/cloud suppliers can capture economics. Greater decision speed can amplify correlated model error.

| Claim | Type/source | Stage | Confounder |
|---|---|---|---|
| H1 net income $2.8bn, ROE 22.7% | Fact; Swiss Re H1 report, 6 Aug 2026 | Financial | half-year seasonality |
| P&C combined ratio 76.7% | Fact; H1 report | Financial | benign large losses, reserving, price/mix |
| SST 264% | Management estimate; H1 report | Capital fact | model and market sensitivity |
| Impact+ supports portfolio optimization and ML claims triage | Product fact; Impact+, accessed 12 Sep | E1 | no outcome disclosed |
| Client data can be uploaded | Product fact; Impact+ FAQ | E1/right boundary | reuse terms unknown |
| AI integrated to improve productivity/decisions | Management target; [2026 targets](https://www.swissre.com/media/press-release/pr-20251205-swiss-re-targets-2026.html), 5 Dec 2025 | E1 | cost program and cycle overlap |
| H1 global insured catastrophe losses $42bn, below trend | Swiss Re Institute estimate, 11 Aug 2026 | Adverse/confounder | market-wide estimate |
| Corporate Solutions faced price pressure | H1 report fact | Economic adverse | line/mix variation |

## KPI and materiality contract

| KPI | Baseline/comparator | Eligible population/quality | Known result | Proof event |
|---|---|---|---|---|
| Accident-year loss ratio at equal modeled risk | matched treaties/renewals without tool | AI-scored risks; exposure, terms and catastrophe load held constant | unknown | multi-year cohort through claims maturity |
| Claim triage precision/recall and leakage | current rules/manual triage | eligible claims; fairness, reopen and customer-outcome guardrails | capability only | randomized rollout and cash reconciliation |
| Underwriter submissions bound per hour | matched teams/lines | adopted workflow; expected margin and audit errors constant | unknown | operating KPI with expense bridge |

Using reported **H1 2026 net income of $2.8bn** as a half-year, after-tax scale gives a same-period 5% hurdle of **$140m after tax**; it is not annualized. Management's $4.5bn 2026 net-income target is kept separate as a target rather than mixed with the reported-period denominator. Illustration: $2.0bn eligible expense × 15% efficiency × 60% realization × 50% retention − $80m recurring cost = **$10m pre-tax** and, assuming a 20% tax rate solely for sensitivity, **$8m after tax**, well below the after-tax hurdle and not a forecast. For underwriting, the valid test is incremental loss improvement after price, mix, reserves and catastrophes, plus capital effects. A 0.5-point apparent ratio change on an assumed $30bn eligible premium is $150m before attribution, tax and capital; the premium is an assumption, illustrating the needed magnitude rather than claiming benefit.

Positive hypothesis: rare global loss history plus capital and distribution create better marginal selection and a lawful feedback loop. Negative: losses are slow/non-stationary; cedents and vendors share the data, cycle effects swamp signal, and competition passes gains through price.

Falsifiers: tool-scored cohorts do not outperform after risk/mix control; claim triage worsens leakage/fairness; AI expense grows without ratio/expense reconciliation. Confidence mechanism **medium**, deployment **low-medium**, capture **low**. G0 passes, G1 provisional on strong capital, G2 insufficient without E2 outcome or controlled evidence; G3/G4 deferred. Original prior 83 preserved.

## Sources and handoff

Opened 12 Sep 2026: [H1 2026 online report](https://www.swissre.com/investors/half-year-report-2026-online.html) and [PDF](https://www.swissre.com/dam/jcr%3A0f74b8a4-7528-4654-80f5-d119ec47c37d/2026-half-year-report.pdf) (6 Aug 2026, financials/notes); [2026 targets](https://www.swissre.com/media/press-release/pr-20251205-swiss-re-targets-2026.html) (5 Dec 2025); [Impact+ Commercial Insurance Insights](https://analytics.swissre.com/details/coin) (undated product/FAQ); [Swiss Re Institute H1 catastrophe estimate](https://sigma.swissre.com/) (11 Aug 2026); [Swiss Re privacy](https://www.swissre.com/terms-of-use/privacy-policy.html) (undated); [Munich Re AI risk perspective](https://www.munichre.com/topics-online/en/digitalisation/artificial-intelligence.html) (competitor, accessed 12 Sep); [Moody's RMS platform](https://www.rms.com/risk-intelligence-platform) (substitute, accessed 12 Sep).

Handoff: [c016.json](../capsules/c016.json). Verify H1 ratio/capital confounders, Impact+ claims-triage scope, and whether any later source supplies controlled cohort economics. Strongest counterargument is cycle/catastrophe/reserve attribution. Research-only; G2 incomplete.
