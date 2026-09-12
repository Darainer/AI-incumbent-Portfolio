# Munich Re — initial evidence dossier

> Lead review complete. The [lead judgment](../lead-review.md) governs dispositions, scores and gates; provisional agent views below are retained for traceability.

**ID:** C015 · **Status:** research-agent packet; lead reviewed 12 September 2026. · **Research cutoff:** 12 September 2026 · **Access date for all web sources:** 12 September 2026

**Security:** Münchener Rückversicherungs-Gesellschaft Aktiengesellschaft in München ordinary registered shares, Xetra **MUV2**, euro quote and euro reporting currency. No ADR is used here. The 11 September 2026 close was **€503.40** according to Trading Economics; the source is a market-data vendor rather than the exchange, so timestamp quality is adequate for an initial G3 test but should be independently checked by the reviewer. The 2025 annual report gives 2025 EPS of **€47.15**, year-end book value per share of **€259.76**, and a 31 December 2025 share price of €562.20 ([annual report, pp. 1–2](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf); [11 September quote](https://tradingeconomics.com/germany/stock-market)).

## Provisional conclusion

Munich Re is a financially strong, diversified reinsurer with a plausible scarce asset in risk histories, catastrophe expertise, underwriting workflows and client relationships. It has production-oriented classical analytics and automated underwriting tools, and management now describes generative AI use in pricing, portfolio management, claims-trend monitoring and data entry. The evidence is strongest for technical plausibility and a selected predictive-model proof of concept, but weak for scaled deployment denominators and absent for incremental cash economics. The exceptionally low 2025 and first-half 2026 major-loss burden, rising investment income and the hard-market legacy explain current earnings far more directly than AI.

At €503.40, the shares are about **10.7× 2025 EPS** and **1.94× 2025 book value**. A residual-income reverse calculation implies roughly a 13.7% sustainable ROE if the cost of equity is 9% and long-run book growth is 4%, below management's >18% 2030 ambition but not obviously conservative after catastrophe normalization. Provisional disposition: **qualified business; watch for evidence and price, not yet an AI-qualified opportunity**. G2 fails because no measured, material, net AI benefit is disclosed.

## Conventional business and dated financial record

Munich Re combines reinsurance (property-casualty, life/health and Global Specialty Insurance), ERGO primary insurance and MEAG asset management. Diversification, capital strength and the ability to withdraw capacity when prices are inadequate support the zero-additional-AI case. Reinsurance client relationships and global capacity are difficult to replicate, but underwriting is cyclical and tail outcomes are sparse.

| €m unless stated | FY2024 | FY2025 | H1 2026 / latest | Interpretation |
|---|---:|---:|---:|---|
| Insurance revenue | 60,830 | 60,412 | 29,957 | 2025 decline and 2026 currency pressure show growth is not the current earnings driver. |
| Operating result | 7,998 | 8,876 | Q2 2,795 | Reported, not AI-attributed. |
| Net result | 5,690 | 6,121 | 3,925 | H1 benefited from low major losses and strong investments. |
| EPS | €42.93 | €47.15 | Not disclosed in release | 2025 denominator verified. |
| Group ROE | 18.2% | 18.3% | 23.0% annualised | H1 is above a normalized assumption. |
| P&C reinsurance combined ratio | 77.3% | 73.5% | Q2 68.9% | 2025 included 5.0 points of prior-year reserve releases; Q2 major-loss load was 4.9% versus an 18% expectation. |
| GSI combined ratio | 93.6% | 85.9% | Q2 88.9% | Mix and catastrophe burden matter. |
| ERGO P&C Germany / International | 88.6% / 91.9% | 88.9% / 90.0% | H1 88.4% / 89.7% | Stable primary underwriting, not identified as AI-caused. |
| Investment result / ROI | €7,191 / 3.1% | €7,514 / 3.2% | Q2 €3,159 / 5.5% | Q2 fair-value gains and equity markets were material. |
| Equity / investments | 32,901 / 230,716 | 33,421 / 222,747 | 33,727 / 225,228 | Large investment float; industrial FCF is inappropriate. |
| Solvency II ratio | — | 298% | 304% | Well above management's >200% floor. |

Sources: [2025 annual report, pp. 1, 5–8, 32–34](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf), published 26 February 2026; [H1 2026 release](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/half-year-financial-report.html), 7 August 2026.

The cleanest normalization warning is explicit: 2025 P&C reinsurance benefited from €864m of prior-year reserve releases (5.0 combined-ratio points) and low major losses; Q2 2026 major-loss expenditure was only 4.9% of net insurance revenue versus an expected 18%. July 2026 renewal volume fell 9.1% and risk-adjusted prices fell 5.5%. Management held 2026 net-profit guidance at €6.3bn but cut expected group insurance revenue to €62bn from €64bn. Thus neither a 68.9% quarterly combined ratio nor 23% annualized ROE is an appropriate through-cycle AI baseline.

Capital allocation is shareholder-friendly but already embedded in reported returns: 2025 dividend €24 per share, a €2.25bn buyback, and an Ambition 2030 target for >80% total payout, >18% ROE and >8% annual EPS growth ([annual report, pp. 5–8](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf)).

## Scarce asset and data-rights audit

| Input | Origin / owner | Exclusivity | Retrieval / inference | Training / cross-customer improvement | Labels / quality | Replication threat |
|---|---|---|---|---|---|---|
| Munich Re policy, exposure and claims history | Munich Re and cedants/policyholders under contract | Historical collection is proprietary; underlying facts may not be | Internal use likely; exact client-contract scope unknown | **Unknown**; no disclosed pooled-training terms | Paid/rejected claims and development triangles offer labels; tail losses are sparse and drifting | Swiss Re, Hannover Re and brokers have substantial parallel histories |
| NatCatSERVICE | Public agencies, scientific institutes, industry, media plus Munich Re curation | Curation/expertise proprietary; many raw inputs public | Munich Re analyzes them | Training rights not stated | Long series but reporting revisions and climate/nonstationarity matter | Vendor catastrophe models and Swiss Re sigma datasets |
| Life/health applications and medical claims | Applicants, cedants and third-party data suppliers | Customer-specific and licensed, not automatically owned | Tokenized joins and risk scoring demonstrated | Cross-client reuse/retention unknown; health-data restrictions material | Mortality/claims labels are useful but delayed | LexisNexis, reinsurer and carrier models; data vendors can sell broadly |
| Underwriter/claims-handler workflow context | Munich Re employees and systems; some cedant submissions | Customer-specific | Annual report says AI/language models are used in relevant workflows | Pooled learning and model-provider retention unknown | Human decisions and subsequent losses provide imperfect labels | Generic LLMs plus broker/carrier workflow software |

Munich Re’s 2025 report describes group privacy governance, risk review for IT-supported personal-data processing, portability rights and supplier clauses, but does **not** establish permission to train models across customers ([annual report, pp. 154–156](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf)). Therefore the investable moat is expertise plus workflow access and capital, with pooled-data rights unresolved.

## Mechanisms, deployment and challengers

1. **Underwriting/risk selection (classical ML plus generative assistance).** Asset → historical exposure/claim and medical data → risk score/submission interpretation → more selective pricing at equal risk → lower loss ratio or profitable new business. Munich Re Life US published a proof of concept using tokenized employer census data joined to third-party medical claims; thousands of employers per decile showed increasing paid/expected claims across risk bands, and management says it has integrated third-party predictions into carrier workbenches ([case study](https://www.munichre.com/us-life/en/insights/future-of-risk/mortality-risk-segmentation-in-the-group-benefits-market.html), 3 July 2024). This is E1 for proof-of-concept validity and E2 for management-reported carrier integration. Ranking deciles without a disclosed holdout test or current-best comparator does not meet E3 and does not establish group-wide retained earnings.

2. **Claims and portfolio monitoring (rules, ML and generative assistance).** MIRA/CLARA structure cases and log paid and rejected claims; the annual report says AI and language models are used in pricing, portfolio management and claims-trend monitoring ([underwriting and claims product page](https://www.munichre.com/en/solutions/reinsurance-life-health/underwriting-and-claims-handling.html), undated; [annual report, p. 58](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf)). These sources establish E1 and management-reported use, but disclose no eligible case count, completion rate, error rate or causal expense benefit.

3. **Agentic workflow and administrative efficiency.** The July 2026 company white-paper page describes a transition from assistants to agents and cites claims, underwriting, customer service and knowledge work. It also says legacy systems, governance, operating models and integration determine scalability ([Munich Re AI investment article](https://www.munichre.com/en/insights/digitalisation/sweet-spot-of-ai.html), 23 July 2026). This is E1, not E2: no named production system or denominator is given. Management separately targeted €200m group cost savings in 2026, but did not attribute that target to AI ([annual report, p. 9](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf)).

**Competitive comparison.** Swiss Re already offers client tools and reports a P&C Re combined ratio of 86.1% for H1 2026, demonstrating that advanced analytics and strong underwriting are not Munich Re-exclusive ([Swiss Re H1 2026 report](https://www.swissre.com/investors/financial-information/financial-results/hy-2026.html), 6 August 2026). Munich Re itself says digital MGAs have less legacy friction, that useful new variables often do not exist in incumbents’ historical data, and that packaged external datasets are becoming easier for both incumbents and entrants to obtain ([MGA interview](https://www.munichre.com/specialty/en/insights/artificial-intelligence/na/partnering-with-tech-savvy-mgas-to-unlock-the-full-potential-of-.item-b0c1d605d391668847f6c5de6853b1ff.html), 25 July 2025). This is strong negative evidence against equating data age with an unassailable moat. EIOPA’s governance opinion further requires proportionate data governance, record-keeping, fairness, cybersecurity and human oversight, increasing verification cost ([EIOPA opinion](https://www.eiopa.europa.eu/publications/opinion-artificial-intelligence-governance-and-risk-management_en), 6 August 2025).

## Evidence ledger

| Claim | Type | Source / section | Scope | Stage | Confounder |
|---|---|---|---|---|---|
| AI/language models are used in pricing, portfolio management and claims monitoring | Management fact | 2025 annual report p.58, 26 Feb 2026 | Group opportunity disclosure | E2, management-reported | No workload denominator or result |
| Mortality model separates risk bands | Company study fact | Life US case study, 3 Jul 2024 | Group-life proof of concept | E1 | No holdout/current-best comparator, economics or independent replication |
| Carrier integrations exist | Management claim | Same case study, workflow section | Unnamed carriers | E2 | Scale and renewal unknown |
| Agentic AI can address underwriting/claims | Management claim | AI article, 23 Jul 2026 | Industry/own journey | E1 | No named production deployment |
| 2025 P&C ratio included 5.0 points reserve benefit | Filed fact | Annual report p.32 | P&C reinsurance | Conventional | Reserve assumptions and mix |
| Q2 2026 major-loss load 4.9% vs 18% expected | Reported fact | H1 release, 7 Aug 2026 | One quarter | Conventional | Catastrophe luck dominates |
| July renewal risk-adjusted price fell 5.5% | Reported fact | H1 release | July renewal book | Adverse | Portfolio exits/mix |
| Historical incumbent data may omit new parameters | Management counterevidence | MGA interview, 25 Jul 2025 | Industry | E1 | Qualitative |

## KPI contract and retained-economics bridge

Minimum materiality uses **5% of FY2025 net result as a scale proxy**, about **€306m after tax** or roughly €390m pretax at a 22% tax rate. FY2025 is not normalized because its catastrophe and reserve experience was favorable; this is a screening hurdle, not company guidance or a normalized forecast.

| KPI | Baseline / comparator | Eligible workload | Quality constraint | Known result | Next proof event |
|---|---|---|---|---|---|
| Accident-year loss ratio, price/mix/cat normalized | Pre-AI matched underwriting cohort | Policies actually scored | Same risk appetite, reserve adequacy and tail limits | Unknown | 2026 annual report / cohort disclosure |
| Expense per completed case | Existing production system | Submissions/claims end-to-end, not drafts | Leakage, complaints and human referral no worse | Unknown | Ambition 2030 cost bridge |
| New-business risk-adjusted return | Similar unscored cohort | Business accepted due to model | Equal capital and loss emergence | POC ranks mortality risk; return unknown | 3–5 year emergence |

For a cost route, `benefit = A × e × r × c − K`. To reach about €390m pretax with 20% task efficiency, 60% realization, 60% shareholder retention and €75m recurring AI cost requires **A ≈ (€390m+€75m)/(0.20×0.60×0.60) = €6.46bn** of eligible annual cost. Total 2025 administration and acquisition costs were €9.33bn, so the hurdle requires about 69% of that entire pool—implausibly broad without revenue or loss-ratio gains. A 10-basis-point improvement on €60.4bn insurance revenue is only €60m pretax. The 5% hurdle likely requires several mechanisms and controlled evidence; none is currently disclosed.

## Valuation and reverse valuation

Residual-income shorthand uses `justified P/B = (ROE − g)/(cost of equity − g)` and 2025 book value of €259.76 per share. It is sensitive to catastrophe normalization, book accounting and the chosen return hurdle. The formula also requires internally consistent retention: `g = ROE × retention`. For example, 15% ROE and 4% growth imply 26.7% retention and a 73.3% payout, below management's >80% payout aspiration. Treat the cases as steady-state valuation sensitivities rather than simultaneous adoption of every Ambition 2030 target.

| Case | Conventional ROE / g / cost of equity | Incremental AI | Indicated value | What must happen |
|---|---|---|---:|---|
| Bear | 12% / 3% / 10% | Zero; €0.2bn implementation drag absorbed in ROE | **€334** | Softer pricing, normal catastrophes and reserve strain normalize earnings. |
| Base | 15% / 4% / 9% | +0.3ppt ROE after cost; conventional value €571, with AI **€587** | **€587** | Underwriting discipline and investment income sustain mid-teens ROE. AI contribution remains below 5% hurdle. |
| Bull | 16% / 4.5% / 8.5% | +0.8ppt ROE; conventional value €747, with AI **€799** | **€799** | High ROE persists through cycle and scaled AI improves selection/expense. |

At €503.40 / €259.76 = 1.938× book, the price implies `ROE = P/B × (r−g)+g`: **13.7%** at 9%/4%, **15.6%** at 10%/4%, or **12.7%** at 8.5%/4%. The market therefore requires a sustained low-to-mid-teens ROE, not the current 23% H1 run rate. A one-point change in sustainable ROE changes value by roughly €52 per share at a 5-point `(r−g)` spread. Dilution is limited by buybacks, but book value and EPS should be refreshed after the €2.25bn program. These are scenarios, not targets.

## Risks, falsifiers and alternative

- **Core-business failure:** several normalized accident years produce sub-cost-of-capital ROE after softer pricing; adverse reserve development or hidden casualty/social-inflation exposure appears.
- **AI/capture failure:** by FY2028 Munich Re still cannot disclose eligible workload, matched quality and a bridge from AI to at least €300m after-tax benefit; generic vendors and MGAs match performance using shared data.
- **Price failure:** the share price implies >16% sustainable ROE under a 10% cost of equity while renewal pricing and normalized underwriting deteriorate.

The strongest positive hypothesis is that proprietary risk curation, capital and distribution let Munich Re apply common models more effectively than entrants and retain gains in risk selection. The strongest negative hypothesis is that reported gains are catastrophe luck, reserves and investment markets, while AI tools are common and their surplus is competed into price. Swiss Re is the direct peer; inaction until a normalized cohort and data-rights disclosure is preferable to treating the AI option as proven.

## Priors, proposed revisions and gates

| Dimension | Original | Proposed | Reason |
|---|---:|---:|---|
| Scarce asset | 5 | 4 | Expertise/history are real; raw data and third-party variables are replicable and rights unclear. |
| AI leverage | 4 | 4 | Underwriting, claims and administration are material. |
| Feedback | 4 | 3 | Frequent claims help, but reinsurance tails are sparse and cross-client reuse unknown. |
| Testability | 2 | 3 | Life model validation exists; tail underwriting remains slow. |
| Distribution | 5 | 5 | Global cedant and primary-insurance access is strong. |
| Capture | 5 | 3 | Pricing cycles, cedant bargaining and vendor costs can pass benefits through. |

**G0 pass. G1 provisional pass** on business/capital, with pooled data rights unresolved. **G2 fail:** selected E2 evidence exists, but no company-specific measurable route to a controlled comparison over a material workload is disclosed; net economics are also absent. **G3 provisional/limited:** price and annual denominators are verified sufficiently for scenarios, but current Xetra quote should be independently confirmed and reserve/cycle normalization remains incomplete. **G4 not assessed.** Confidence: mechanism **moderate**; deployment **low–moderate**; capture **low**; valuation **moderate-low**.

## Source register

1. Munich Re, *Group Annual Report 2025*, published 26 Feb 2026, pp.1, 5–9, 13, 32–34, 58, 154–156. Direct PDF above. Limitation: management reporting; AI outcomes not quantified.
2. Munich Re, *Record half-year profit of almost €4bn*, 7 Aug 2026. Direct release above. Latest financial update; unusually benign losses.
3. Munich Re Life US, *Mortality risk segmentation in the Group Benefits market*, 3 Jul 2024. Company POC; no independent control or cash bridge.
4. Munich Re, *Underwriting & claims*, undated. Product description; not proof of scale or causality.
5. Munich Re, *How to find the sweet spot of AI investments*, 23 Jul 2026. Strategy/white-paper landing page; E1 only.
6. Munich Re Specialty, *Partnering with tech-savvy MGAs*, 25 Jul 2025. Useful company-authored challenger evidence.
7. Munich Re, *First-half 2026 natural-disaster review*, 30 Jul 2026, [direct page](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/natural-disaster-figures-first-half-2026.html). Industry data; not company claims.
8. Swiss Re, *Half-Year Report 2026*, 6 Aug 2026. Peer benchmark; accounting/mix differ.
9. EIOPA, *Opinion on AI governance and risk management*, 6 Aug 2025. Regulatory standard; no company economics.
10. Trading Economics, Munich Re quote, 11 Sep 2026. Vendor price, not primary exchange.

## Handoff to lead reviewer

**Verify decisively:** (1) whether annual-report wording supports E2 rather than only intended use; (2) the POC's thousands-per-decile validation and unnamed production integrations; (3) €503.40 Xetra price and the 1.94× book reverse valuation. **Strongest counterargument:** benign catastrophe/reserve and investment effects explain earnings, while data rights and AI cash attribution remain absent. **Blocking questions:** production workload denominator; pooled-learning rights; matched accident-year outcomes; full AI cost and retained economics. **Provisional disposition:** qualified conventional insurer, evidence watch; do not promote as a proven AI beneficiary. **File written:** `research/batch-01/dossiers/09-munich-re.md`.
