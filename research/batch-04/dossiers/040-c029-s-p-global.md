# C029 — S&P Global evidence dossier

**Unreviewed agent work.** S&P Global Inc.; NYSE common stock SPGI, USD quote/reporting. Cutoff/retrieval 12 September 2026. Latest period Q2/H1 ended 30 June 2026, published 28 July 2026; FY2025 latest audited.

## Business and financial anchor

S&P Global sells credit ratings, benchmarks/indices, commodity price assessments, market and private-market data, workflow software and (through the divestiture period) mobility data. Its scarce assets include regulated ratings franchises, long time series, benchmark licenses, Platts price-discovery processes, Capital IQ distribution and embedded customer workflows. AI can improve research/retrieval and data operations, but it also lowers barriers to summarizing public information and may shift interface control to model/platform vendors.

The [Q2 2026 SEC-filed release](https://www.sec.gov/Archives/edgar/data/64040/000006404026000040/spgi2q2026-earningsrelease.htm) reported quarterly GAAP revenue **$4.146bn**, up 10%, operating profit **$1.812bn**, up 17%, net income $1.217bn and diluted EPS $4.12. Excluding Mobility on a pro-forma basis, revenue was $3.678bn and operating profit $1.757bn. H1 operating cash flow was $2.476bn; company-defined FCF was **$2.249bn** after $65m capex and $162m distributions to noncontrolling holders. Mobility disposition and gain, severance and transition items confound year-over-year comparisons.

The [2025 10-K](https://www.sec.gov/Archives/edgar/data/64040/000006404026000013/spgi-20251231.htm) reported revenue **$15.336bn**, operating profit **$6.478bn** (including disposition effects), attributable net income $4.471bn, cash $1.745bn, short-term debt $718m and long-term debt $12.370bn. Subscription, ratings issuance, asset-linked index and usage-based revenue have different cyclicality. Debt issuance can fall abruptly; index fees depend on market levels/flows; commodity activity cycles. Core durability comes from regulatory acceptance, benchmark network effects, proprietary collection and workflow integration.

## Rights audit

| Input | Owner/exclusivity | Inference/training rights | Labels/quality | Replication threat |
|---|---|---|---|---|
| Ratings files/default histories | Issuer submissions plus S&P opinions | Confidential data contract-bound; published ratings usable; pooled training terms undisclosed | Long default history, sparse tail events and rating-policy changes | Moody's/Fitch have comparable histories |
| Capital IQ datasets | Exchanges, filings, vendors and S&P transformations | Each license controls redistribution/training; customer entitlements apply | Normalized/linkable but vendor corrections and survivorship matter | LSEG, Bloomberg, FactSet |
| Platts assessments | Market participants and editorial process | Source confidentiality and methodology govern use | Expert-reviewed price labels; illiquid markets subjective | Argus/ICE and exchange prices |
| Customer prompts/documents | Customer-specific | S&P AI terms/privacy determine retention; no blanket cross-client permission established | High workflow relevance; inconsistent labels | Generic RAG on customer-licensed content |
| Kensho models/code | S&P-owned technology plus third-party models | Internal/commercial use; foundation-model provider terms vary | Strong data-engineering capability, effectiveness task-specific | Open models and hyperscalers commoditize tooling |

Licenses are both moat and constraint. Owning a compiled database does not imply rights to train on every upstream field or redistribute model outputs. Ratings analytical independence also limits automated decision delegation.

## Mechanisms and challengers

1. **Search and research assistance (generative/RAG).** Entitled Capital IQ content plus customer query → sourced answer/draft → analyst-approved research faster → retention, premium pricing or capacity. S&P has introduced generative search/capabilities and uses Kensho; public sources establish availability, not end-to-end controlled productivity or incremental renewal cash.
2. **Data extraction/normalization (ML/generative assistance).** Filings/documents → structured entities and estimates → faster, broader dataset updates at maintained accuracy → lower content cost and faster products. Kensho Scribe/NLP capabilities establish E1/E2 internal/product use; error and cost cohorts are undisclosed.
3. **Ratings surveillance/risk signals (classical ML).** Issuer/market/default history → flag analysts' review → faster detection at unchanged rating quality → lower labor or better product. Human committees and regulation remain essential; no evidence supports autonomous ratings or improved default discrimination attributable to current AI.

**Moody's** is the closest incumbent challenger, with ratings, Orbis/data and GenAI products. **Bloomberg/LSEG plus generic model/RAG stacks** are substitutes that can answer across licensed corpora and own the terminal interface. Customers can build on SEC/public data. Model vendors can capture serving economics; AI summaries can cannibalize seats or research views. Credit-rating regulation and data licenses limit scaling.

| Claim | Type/source/date | Stage | Confounder |
|---|---|---|---|
| Q2 revenue $4.146bn, OP $1.812bn | Fact; SEC release, 28 Jul 2026 | Financial | Mobility disposition |
| H1 FCF $2.249bn | Non-GAAP fact; SEC release | Financial | distributions and adjustment choices |
| FY2025 revenue $15.336bn, OP $6.478bn | Filing fact; 10-K, Feb 2026 | Financial | disposition gains/restructuring |
| Enterprise strategy explicitly scales AI/data | Filing fact/management aim; 10-K pp.38 | E1 | no causal outcome |
| Kensho supplies AI/ML capabilities | Product fact; [Kensho](https://www.kensho.com/) | E1/E2 | marketing scope |
| GenAI product answers use licensed content | Product claim; [S&P Global AI](https://www.spglobal.com/en/research-insights/ai) | E1 | adoption/accuracy unknown |
| Moody's offers Research Assistant | Competitor product; [Moody's](https://www.moodys.com/web/en/us/capabilities/genai.html) | Challenger E1 | vendor claim |
| Debt and rating-issuance revenue are cyclical | 10-K risk fact | Core adverse | rate/issuance cycle |

## KPI and materiality

| KPI | Baseline/comparator | Eligible workload/quality | Known result | Closing event |
|---|---|---|---|---|
| Analyst minutes per accepted research task | current search/manual extraction | entitled users/tasks; citation accuracy and corrections capped | unknown | randomized usage cohort |
| Fields published per content FTE | pre-AI pipeline | eligible filings; audited field accuracy/freshness | unknown | segment cost/KPI disclosure |
| AI product ARR/renewal/seat effect | same customer cohort without product | AI-entitled accounts; cannibalized seats and model cost included | unknown | renewal cohort disclosure |

Five percent of FY2025 GAAP operating profit is **$323.9m annual pre-tax** (`0.05 × $6.478bn`), but disposition effects make it an imperfect scale proxy. Illustration: assumed $2.5bn eligible content/technology labor cost × 20% task improvement × 60% realization × 50% retention − $100m recurring model cost = **$50m**, below hurdle. Alternatively, $500m AI revenue at 60% contribution less $100m model/cannibalization cost yields $200m. Inputs are assumptions; consolidated margin expansion cannot prove either path.

Positive: proprietary, permissioned content and entrenched workflows allow S&P to distribute sourced AI and retain subscription/usage economics. Negative: third-party licenses restrict reuse, customers prefer cross-publisher interfaces, seat compression and model costs transfer value away.

Falsifiers: factual/citation error prevents material workflow adoption; AI cohorts show no net renewal/ARR after seat cannibalization; content cost per accepted field does not decline. Confidence mechanism **high**, deployment **medium**, capture **low-medium**. G0/G1 pass provisionally; G2 incomplete because E2-scale use and controlled economics are not disclosed. G3/G4 deferred. Original prior 89 preserved.

## Sources and handoff

Opened 12 Sep 2026: [Q2 2026 filed release](https://www.sec.gov/Archives/edgar/data/64040/000006404026000040/spgi2q2026-earningsrelease.htm) (28 Jul, financial/FCF); [2025 10-K](https://www.sec.gov/Archives/edgar/data/64040/000006404026000013/spgi-20251231.htm) (Feb 2026, business/financial/risk); [Kensho](https://www.kensho.com/) (product); [S&P AI research hub](https://www.spglobal.com/en/research-insights/ai) (product/research); [S&P privacy](https://www.spglobal.com/en/privacy/privacy-policy-english) (rights); [ratings definitions/methodology](https://www.spglobal.com/ratings/en/about/understanding-credit-ratings) (quality/governance); [Moody's GenAI](https://www.moodys.com/web/en/us/capabilities/genai.html) (challenger); [SEC EDGAR](https://www.sec.gov/edgar/search/) (public-data substitute).

Handoff [c029.json](../capsules/c029.json). Verify Mobility pro-forma treatment, current product production scope, and license/training boundaries. Research-only; G2 incomplete.

A valid causal design would separate discovery time from final accepted output. For research assistance, measure completion against the existing terminal/search workflow and require identical citations, factual accuracy and compliance review. For extraction, sample fields after downstream corrections mature and include rework. Revenue evidence needs customer cohorts with the same product bundle, contract term and market conditions. Ratings surveillance must compare discrimination and timeliness without automating committee judgment. These tests also need full model inference, data-licensing, security and human-review expense. Mobility disposal changes the company perimeter, while issuance and market levels change variable revenue, so neither consolidated organic growth nor margin can substitute for these mechanism-level controls.
