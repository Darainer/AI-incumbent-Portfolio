# C023 JPMorgan Chase — evidence dossier

**Unreviewed agent packet. Research cutoff:** 12 September 2026. **Security:** JPMorgan Chase & Co. common stock, NYSE: JPM; quote/reporting currency USD. **Latest period:** Q2 ended 30 June 2026, released 14 July 2026. No valuation, ranking or recommendation.

## Ordinary business and resilience

JPMorganChase combines Consumer & Community Banking (CCB), Commercial & Investment Bank (CIB), Asset & Wealth Management (AWM) and Corporate. Its scarce assets are a low-cost deposit and payment franchise, regulated client access, transaction/credit outcomes, and workflow distribution across 320,000-plus employees. Those advantages coexist with interest-rate, market, credit and regulation exposures that can overwhelm task-level AI effects.

The opened [Q2 2026 earnings release](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/2nd-quarter/6cded9fd-a164-4e6c-8cff-377357cf105c.pdf) reports $57.347bn GAAP revenue, $21.155bn net income, $27.316bn noninterest expense and $2.515bn credit provision. A $4.6bn after-tax Visa-related gain and other equity gains inflate reported income; excluding significant items, net income was $16.9bn. Average loans were $1.5tn, deposits grew 7%, assets were $5.0tn and stockholders' equity $375bn. Standardized CET1 was 14.1%, total loss-absorbing capacity $590bn and cash/marketable securities $1.5tn. Capital returns were $4.0bn common dividends plus $6.2bn net buybacks. These sector-appropriate anchors show resilience, but market activity was unusually favorable and expenses rose 15%, including compensation and technology.

CCB produced $20.272bn revenue and $5.311bn net income; card net charge-offs were 3.34%. CIB produced $24.853bn revenue and $9.678bn net income; AWM $6.851bn revenue and $1.957bn net income. The ordinary business earns through spread, fees and risk taking, so neither revenue nor an overhead-ratio move identifies AI. Capital allocation must preserve regulatory capital through stressed losses.

## Data and rights

| Input | Owner/exclusivity | Inference/training permission | Labels | Replication |
|---|---|---|---|---|
| Deposit, card and payment histories | Customer-originated; JPMorgan holds regulated records; not universally exclusive | In-account fraud/personalization use is asserted; public terms do not establish unrestricted cross-customer generative training | frequent transactions, fraud disputes and servicing outcomes; fraud labels drift | Bank of America, Capital One and payment networks have comparable data |
| Credit applications and repayment vintages | Applicant/borrower plus bank underwriting record | Decisions subject to fair-lending, privacy and adverse-action controls; exact pooled-learning terms unknown | eventual defaults are useful but delayed and policy-dependent | bureaus and fintechs license external data |
| CIB/AWM research, risk and trading records | mixed bank proprietary, licensed market data and client confidential material | SpectrumIQ use is evidenced; underlying vendor licences and client-data reuse are undisclosed | orders, execution cost and risk outcomes are observable, investment alpha is noisy | Bloomberg, LSEG, other banks and buy-side systems |
| Employee documents and workflow | firm and employees; confidentiality varies | LLM Suite/Employee Assistant run in governed firm environment; model-vendor retention terms not public | acceptance, completion and errors can be logged | Microsoft and enterprise copilots reduce uniqueness |

The [COO's 2025 shareholder letter](https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-jennifer-piepszak) says customer controls and governed data safeguards apply. That supports operational governance, not blanket ownership or training rights. Regulated decisioning creates both defensibility and liability.

## Mechanisms and competition

**1. Credit/fraud/personalization (classical ML).** Transaction and outcome data feed decision models; outputs are better risk controls or relevant offers; value appears as lower fraud/credit loss or higher risk-adjusted revenue. Management says a decade of advanced ML is producing measurable value across these domains, but supplies no vintage-matched loss or incremental earnings bridge. This is management-reported production E2; much is already in reported baseline.

**2. Employee workflow (generative/agentic assistance).** The homegrown LLM Suite and newly rolled out Employee Assistant summarize, retrieve and take actions. The task output should be completed work at equal error/compliance rates, not prompts or time saved. Management explicitly expects freed capacity to be reinvested in growth rather than primarily removed headcount. This weakens a direct cost-capture model even if productivity is real.

**3. AWM research and adviser capacity.** The [AWM shareholder letter](https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-mary-callahan-erdoes) reports SpectrumIQ automates nearly 75% of equity trading and 85% of FX trading, covers 90,000 securities/22m documents, and its Smart Monitor compresses time-to-insight by 80%. Connect Coach served 12,000 users with 25 specialized agents and pushed 1m insights. These are meaningful E2 deployment facts. The same letter reports 2025 AWM revenue $24bn, pre-tax income $9bn, client assets $7tn and $553bn flows, but market appreciation, distribution and adviser growth confound attribution.

Bank of America is an incumbent challenger with Erica/employee AI and similar customer distribution. Capital One is a focused data/credit competitor. Generic enterprise copilots and model vendors can commoditize document tasks. The strongest negative evidence is economic: Q2 noninterest expense rose 15% and management plans approximately $19.8bn of 2026 technology spending while saying capacity is reinvested. This is consistent with growth investment and favorable revenues, but it does not prove net cost extraction. Fair-lending errors, hallucinations, data leakage and credit-cycle selection are material downside paths.

## Evidence ledger

| Claim | Type | Source/date/section | Scope | Stage | Confounder |
|---|---|---|---|---|---|
| ML is deployed across credit, fraud and personalization | management claim | [COO letter](https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-jennifer-piepszak), 6 Apr 2026, technology/data/AI | unspecified workflows | E2 | no denominators/control |
| Generative AI is deployed at enterprise scale | management claim | same, technology/data/AI | employees | E2 | adoption and exception rate absent |
| Employee Assistant can provide help and take action | fact/capability | same, workforce | recently rolled out | E2 | completion quality absent |
| Smart Monitor reduces time-to-insight 80% | management claim | [AWM letter](https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-mary-callahan-erdoes), 6 Apr 2026, SpectrumIQ | investment users | E2 | baseline and quality unknown |
| Connect Coach serves 12,000 users | management claim | same, Connect Coach | PB/USWM | E2 | usage not incremental flows |
| Capacity will be reinvested in growth | management intent | COO letter, productivity paragraph | company | E1 | capture may arrive as revenue |
| Q2 earnings do not prove AI value | inference | [Q2 release](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/2nd-quarter/6cded9fd-a164-4e6c-8cff-377357cf105c.pdf), pp.1–4 | company | E0 | Visa gain, markets, rates, mix |

## KPI contract and materiality

| KPI | Baseline/comparator | Eligible population | Quality condition | Known | Closing event |
|---|---|---|---|---|---|
| fraud loss per 10,000 transactions | matched prior model/holdout | decisions scored by new model | fixed approval, disputes and latency | undisclosed | cohort disclosure with loss and approvals |
| vintage net charge-off / risk-adjusted return | matched product, FICO, policy and macro vintage | AI-influenced originations | fairness and capital held constant | Q2 card NCO 3.34%, no AI attribution | 24–36 month vintages |
| completed employee cases per paid hour | pre-rollout or randomized teams | actual LLM Suite users | same errors, escalation and compliance | deployment only | audited task study and expense bridge |
| adviser households per adviser / organic flows | matched adviser books | Connect Coach users | suitability/complaints controlled | users disclosed, causal result absent | matched renewal/flow cohort |

For a bank, use normalized risk-adjusted earnings rather than industrial operating profit. A transparent scale proxy is Q2 net income excluding significant items annualized: $16.9bn × 4 = $67.6bn; this is **not a forecast or normalized cycle estimate**. The 5% convention is $3.38bn annual after-tax benefit. Illustrative expense bridge: assume 25% of quarterly $27.316bn expense is eligible ($27.316bn quarterly expense × 4 × 25% = $27.316bn annual pool), 15% efficiency, 50% realization, 50% retention and $0.5bn recurring AI expense. Benefit = $27.316bn × 15% × 50% × 50% − $0.5bn = **$0.524bn annual pre-tax**. This is **NOT_COMPARABLE** with the $3.38bn after-tax earnings hurdle until a tax conversion is specified; the earlier below-hurdle conclusion is withdrawn. Credit/fraud or growth benefits might be larger, but public evidence cannot distinguish model effect from policy and cycle.

## Falsifiers and gates

Positive hypothesis: regulated distribution and integrated outcomes let JPMorgan deploy models faster across many valuable decisions, with reinvested capacity compounding growth. Negative: common models plus regulatory constraints commoditize workflows; costs remain high; favorable markets and credit obscure weak incremental economics.

Falsifiers: (1) matched credit/fraud vintages fail at fixed risk appetite; (2) LLM cohorts show no end-to-end output gain after review and model costs; (3) technology expense and staffing rise without better mix-adjusted overhead or growth. Unresolved: vendor/data rights, eligible workload, error rates, model cost and how benefits enter business-line earnings.

Confidence: mechanism **high**, deployment **medium-high**, capture **low-medium**. G0 met; G1 provisionally met given capital and diversification; G2 **provisional limited pass** because enterprise and AWM deployments reach E2 with credible tests, while controlled causality/materiality are absent. G3/G4 deferred by user.

## Source register

Opened/accessed 12 Sep 2026: [Q2 2026 release](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/2nd-quarter/6cded9fd-a164-4e6c-8cff-377357cf105c.pdf) (14 Jul 2026, pp.1–8); [Q2 2026 10-Q](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/2nd-quarter/corp-q2-2026.pdf) (30 Jun 2026; financial/risk detail); [2025 annual report hub](https://www.jpmorganchase.com/ir) (published 6 Apr 2026); [COO letter](https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-jennifer-piepszak) (6 Apr 2026); [AWM letter](https://www.jpmorganchase.com/ir/annual-report/2025/ar-ceo-letter-mary-callahan-erdoes) (6 Apr 2026); [JPMorganChase privacy](https://www.jpmorganchase.com/privacy) (undated; rights boundary); [Federal Reserve SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) (4 Apr 2011; model-risk requirements); [CFPB adverse-action AI guidance](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/) (19 Sep 2023; regulated limitation); [Bank of America Erica](https://newsroom.bankofamerica.com/content/newsroom/press-releases/2024/04/erica-surpasses-2-billion-interactions--helping-42-million-clients.html) (15 Apr 2024; challenger). Company letters supply management claims, not independent efficacy.

**Handoff:** verify (i) Q2 $16.9bn net income excluding significant items and 14.1% CET1, (ii) $19.8bn technology budget/enterprise GenAI deployment, (iii) SpectrumIQ and Connect Coach scope. Counterargument: management reinvests capacity and expense rose. Files: this dossier and [capsule](../capsules/c023.json).
