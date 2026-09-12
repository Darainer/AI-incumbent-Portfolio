# Thomson Reuters (C036) — initial evidence dossier

> Lead review complete. The [lead judgment](../lead-review.md) governs dispositions, scores and gates; provisional agent views below are retained for traceability.

**Research-agent evidence packet; lead reviewed 12 September 2026.**  
**Cutoff/access date:** 12 September 2026. **Issuer/security:** Thomson Reuters Corporation common shares, Nasdaq **TRI**, USD quote and USD reporting currency (the same common shares also trade on TSX in CAD). **Price:** US$97.35, latest vendor trade timestamp 12 September 2026 00:15 UTC; the overnight timestamp and quote should be independently checked before an investment decision. **Industry:** I01 legal, tax and professional information.

## Provisional conclusion

Thomson Reuters has the clearest asset-to-workflow mechanism in this pair: owned/licensed editorial content, citations and professional tax/legal workflows are embedded in CoCounsel and Westlaw. Production deployment is credible—management identifies CoCounsel as a driver of recurring organic growth and the current product page reports 2,700 corporate customers—but measured, net AI economics remain undisclosed. Customer anecdotes show large task-time savings, while a controlled academic test of earlier incumbent legal-research products found meaningful hallucination rates. At US$97.35 the shares are about 20.4 times management's 2026 free-cash-flow guidance; the DCF base case is below price and reverse valuation requires about 8.5% five-year FCF/share growth at a 9% return hurdle and 2.5% terminal growth. **Provisional disposition: watch / G2 pass, G3 conditional; no purchase recommendation.** Mechanism confidence moderate-high, deployment moderate, capture low-moderate, valuation low-moderate.

## Conventional business and financial resilience

TR sells subscription-heavy information and workflow products to legal professionals, corporations, and tax/audit/accounting professionals, plus Reuters News and declining Global Print. The “Big 3” represented 84% of first-half 2026 revenue and grew 9% organically. Legal Professionals generated US$1.528bn, Corporates US$1.145bn and Tax/Audit/Accounting US$721m in the half. Recurring revenue was 97% of Legal's second-quarter total and 86% of Corporates', supporting resilience without any *additional* AI uplift. Reuters and print diversify but have weaker growth; the July 2026 agreement to place Global Print in a KKR joint venture is a material perimeter change that the valuation below does not separately model.

| Metric | Period / publication | Result | Comment |
|---|---|---:|---|
| Revenue | H1 ended 30 Jun 2026; 5 Aug 2026 | US$4.041bn, +10% reported / +8% organic | Latest verified update |
| IFRS operating profit | H1 2026 | US$1.197bn, +20% | Includes operating gains and acquisition/intangible effects |
| Adjusted EBITDA | H1 2026 | US$1.626bn, 40.2% margin | Non-IFRS; Q2 margin 38.1% |
| Operating cash flow | H1 2026 | US$1.425bn | Working-capital timing helped |
| Free cash flow | H1 2026 | US$1.059bn | OCF less US$333m capex, US$31m lease principal, US$2m preference dividends |
| Diluted EPS / adjusted EPS | H1 2026 | US$2.05 / US$2.22 | Do not mix the adjusted measure with IFRS silently |
| Diluted weighted shares | H1 2026 | 441.7m | Q2 was 438.6m; repurchases reduce denominator |
| Net debt | 30 Jun 2026 | US$2.628bn incl. leases; 0.9x adjusted EBITDA | Cash US$577m; balance sheet is resilient |
| FY2026 guidance | 5 Aug 2026 | revenue and organic growth ~8%; adjusted EBITDA margin +100bp vs 39.2% in 2025; FCF ~US$2.1bn | Acquisitions and AI are already embedded in guidance |

Source: [Q2 2026 results](https://ir.thomsonreuters.com/news-releases/news-release-details/thomson-reuters-reports-second-quarter-2026-results), published 5 August 2026, tables “Consolidated Financial Highlights,” “2026 Outlook” and FCF/net-debt reconciliations.

The zero-additional-AI case is therefore a durable, cash-generative subscription business, but it is not an AI-free historical baseline: Westlaw has used machine learning for years and current reported growth already includes CoCounsel. Conventional risks are legal-information competition, print decline, acquisition execution, rising software amortization, and controlling-shareholder governance. The 10 September financing announcement (US$1.3bn notes plus C$1bn private placement) occurred after Q2 and means the Q2 debt bridge is stale; use-of-proceeds and final pro-forma leverage require review.

## Asset and data-rights audit

| Input | Origin / owner | Exclusive? | Retrieval / inference rights | Training / cross-customer rights | Labels / quality | Replication threat |
|---|---|---|---|---|---|---|
| Westlaw cases, statutes, KeyCite and editorial enhancements | Public law plus TR-owned/licensed taxonomy, citator and editorial work | Public raw law no; enrichment partly proprietary/licensed | Product use is explicit | TR does not disclose corpus/model training terms in enough detail | Citations, treatment history and 4,500+ experts provide useful verification labels | RELX/LexisNexis has a comparable corpus and citator |
| Practical Law / Checkpoint guidance | TR authors and licensed contributors | Partly proprietary | Used to ground answers in a defined verified set | Unknown whether all licensed items permit model training versus retrieval | Human-authored, jurisdiction-specific | Wolters Kluwer and specialist publishers; customers can use generic RAG over owned materials |
| Customer documents, prompts and firm context | Customer | Customer-specific | CoCounsel processes it for that customer's workflow | TR says neither it nor third parties use it to train/improve CoCounsel or underlying LLMs; no pooled flywheel | Rich matter context but outcomes and reuse rights unknown | Harvey, Microsoft and in-house agents can access the same customer-authorized documents |
| Usage telemetry / accepted outputs | Likely split by contract | Unknown | Operational telemetry likely, but scope undisclosed | Cross-customer learning permission unknown | Acceptance is a noisy label; ultimate legal correctness requires review | Common vendors can learn product UX even without content |
| Reuters news / CLEAR public records | TR-owned reporting plus licensed/public records | Mixed | Embedded search/entity-resolution uses are offered | Training and onward-use rights not established | Timeliness and entity linkage useful | LSEG, Bloomberg, LexisNexis and specialist data vendors |

The [TR AI FAQ](https://www.thomsonreuters.com/en/artificial-intelligence) (undated live page, accessed 12 September 2026, FAQ) expressly rules out training on customer content and prompts and says OpenAI/Google are contractually barred from doing so. This supports privacy and customer trust but weakens the original feedback-loop prior. It does not establish rights to train on every item in TR's editorial corpus.

## Mechanisms and competitive challenge

**1. Grounded legal research and drafting (generative assistance becoming agentic execution).** Westlaw/Practical Law content → retrieve and cite relevant authority → draft/review/analyze in CoCounsel → more completed matters or lower verified completion cost → subscription uplift and retention. Management reports Legal recurring revenue +9% organically in Q2, driven primarily by Westlaw and CoCounsel, which is E2 deployment and revenue association—not causal AI capture. The product page reports 2,700 corporate CoCounsel customers and a 61% reduction in correspondence-drafting time, but gives no design, sample or quality-adjusted comparator; grade that result E1/E2, not E3.

**2. Tax/audit workflow automation (generative assistance plus bounded execution).** Checkpoint/ONESOURCE content and customer workpapers → research, return review and audit preparation → more files completed at fixed error rate → paid modules, retention or customer labor capacity. Tax/Audit/Accounting organic revenue grew 8% in Q2 and management named CoCounsel and GoSystem among drivers. No eligible-workload denominator, exception rate or net revenue per customer was disclosed.

**3. Internal/product development productivity.** TR says it invests more than US$200m annually in AI and has over 1,000 AI/ML specialists. A proprietary “Thomson” model launched 24 August 2026 may reduce third-party bargaining or improve domain performance, but launch status is E1. Serving cost, benchmark quality, capex and customer adoption are unknown.

RELX's LexisNexis (Lexis+ AI/Protégé) is the closest incumbent rival: it has comparable authoritative content, citations and distribution, so TR's moat is relative rather than unique. Harvey is a credible entrant/substitute because it integrates into major firms and can work on customer documents; generic Gemini/OpenAI/Anthropic agents plus firm RAG pressure standalone seat pricing. Anthropic's legal solution lists a CoCounsel Legal connector alongside NetDocuments: this supports alternative-interface risk, but also shows that a general agent may preserve TR's backend/content relevance rather than eliminate it. The strongest negative evidence is Magesh et al., “Hallucination-Free?”: an academic evaluation of earlier Lexis+ AI, Ask Practical Law AI and Westlaw AI-Assisted Research found hallucinations remained above zero and product behavior varied. It does not test today's CoCounsel and therefore cannot establish current failure, but it proves human verification remains an economic cost. A May 2026 court-sanctions report also recorded a disputed Westlaw-AI attribution; Reuters could not determine the source of the false citation, so it is an adverse operational warning rather than product-causation evidence.

## Evidence ledger

| Claim | Type | Source/date; section | Scope / stage | Confounder |
|---|---|---|---|---|
| H1 revenue +10%, organic +8% | Fact | Q2 results, 5 Aug 2026, highlights | Group, E2 | FX, acquisitions, price/mix |
| CoCounsel helped drive recurring growth in all Big 3 | Management claim | Q2 results, segment commentary | Production association, E2 | No contribution split or counterfactual |
| 2,700 corporate customers; 61% drafting-time reduction | Management claim | AI product page, accessed 12 Sep 2026 | Adoption/result, E2 at most | Definition, sample, quality and publication date absent |
| Customer prompts are excluded from training | Fact about policy | AI FAQ, undated | Rights boundary, E1 | Contract exceptions and telemetry detail unknown |
| Verified TR content grounds answers | Management claim | AI FAQ, guardrails | Capability, E1 | Grounding does not ensure correctness |
| Annual AI investment exceeds US$200m | Management claim | AI page | Cost scale, E1 | Accounting split and ROI unknown |
| Earlier incumbent legal-AI tools hallucinated | Fact from study | Magesh et al., 2024 working paper / 2025 publication | Controlled task test, E3 for older tools | Not current CoCounsel; benchmark scope |
| Legal-AI error led to sanctions, product causation disputed | Fact | Reuters, 1 May 2026 | Adverse case, E2 | Copy/paste and supervision; no causal attribution |
| Global Print JV changes perimeter | Fact | TR release, 14 Jul 2026 | Corporate transaction | Closing/pro-forma terms need audit |

## KPI contract and retained economics

| KPI | Baseline/comparator | Eligible workload | Quality constraint | Known result | Next proof event |
|---|---|---|---|---|---|
| Net revenue/customer after seat changes | Pre-CoCounsel cohort vs matched non-adopter | Customers offered paid AI | renewal, churn and seat count | Unknown | FY2026 results / renewal cohorts |
| Verified completion cost per matter | Existing Westlaw/manual workflow | Research, drafting, review tasks | citation accuracy and senior-review minutes | 61% drafting-time claim lacks method | Controlled customer study |
| Paid AI ARR and gross margin | 2025 product baseline | Big 3 customers | inference, content and support cost included | Undisclosed | 2026 investor reporting |

**Pre-registered materiality hurdle:** 5% of normalized operating profit. Annualized H1 IFRS operating profit of about US$2.394bn is only a scale proxy, not a normalized estimate; it puts the screening hurdle near US$120m pretax. Illustrative cost bridge before incremental AI expense: US$1.0bn eligible labor/content-production cost × 20% task efficiency × 60% realization × 50% retained share = US$60m. Let incremental recurring AI expense be **K**; net benefit is US$60m − K, so this cost route cannot reach US$120m even at K=0. The disclosed US$200m+ annual AI investment is already included in reported earnings/FCF and must not be subtracted again; the incremental portion K is unknown. A revenue route clears the hurdle where paid AI revenue × contribution margin after cannibalization/model/support costs − K ≥ US$120m (for example, at 40% contribution and K=US$80m, required revenue is US$500m). These are break-even requirements, not forecasts. Avoid counting customer time saved as TR cost savings.

## Valuation and reverse valuation

At US$97.35 and 438.6m Q2 diluted shares, illustrative equity value is US$42.70bn; adding Q2 net debt gives EV US$45.33bn. FY2026 guided FCF of US$2.1bn equals US$4.79/share and a **20.4x price/FCF**. The post-quarter financing makes EV provisional.

Five-year DCF formula: value = sum of FCF/share grown at *g* and discounted at 9%, plus year-5 FCF × (1+terminal growth)/(9%−terminal growth), discounted five years. Bear/base/bull use starting FCF/share US$4.79 and 438.6m shares, with no extra dilution.

| Case | Conventional / AI assumption | 5y growth; terminal growth | Value/share | Reading |
|---|---|---:|---:|---|
| Bear | print/competition pressure; AI net zero/adverse | 2%; 2% | ~US$69.77 | Material downside |
| Base | core subscription compounding; reported AI already in base | 6%; 2.5% | ~US$87.70 | Below observed price |
| Bull | paid workflow expansion with durable capture | 9%; 3% | ~US$106.13 | Requires evidence beyond E2 |

Reverse valuation at US$97.35, 9% discount and 2.5% terminal growth implies approximately **8.5% annual FCF/share growth for five years** (interpolated; 8.5% produces about US$97.40). At a 10% hurdle the requirement rises materially. Sensitivity is dominated by discount/terminal rates and whether buybacks offset acquisition funding. The conventional business is not obviously cheap; AI is not a free option.

## Risks, falsifiers, priors and gates

Strongest positive hypothesis: trusted content and citations let TR charge for higher-value completed workflows, with 500,000+ existing customers lowering distribution cost. Strongest negative: RELX and entrants match quality, customers retain productivity through lower fees/fewer seats, verification costs persist, and model/content investment absorbs the surplus.

Three falsifiers: (1) CoCounsel adopter net revenue/retention underperforms matched non-adopters after two renewal cycles; (2) blinded tests show generic/entrant agents achieve equivalent citation accuracy and completion time at materially lower total cost; (3) paid AI contribution cannot exceed model/support/cannibalization cost and approach US$120m pretax by 2031. Waiting for cohort economics is a valid alternative; RELX is the direct peer.

| Dimension | Original prior | Proposed revision | Reason |
|---|---:|---:|---|
| Scarce asset | 5 | 5 | Proprietary enrichment and workflow verified, though rival assets exist |
| AI leverage | 4 | 4 | Core professional tasks, but verification remains |
| Feedback | 4 | 2 | customer content/prompts excluded from training; pooled rights unknown |
| Testability | 4 | 4 | rapid task tests feasible; economics cohorts still absent |
| Distribution | 5 | 5 | broad installed customer base and cross-workflow products |
| Capture | 5 | 3 | revenue association exists; net AI contribution and cannibalization unknown |

Weighted posterior is 77/100 versus prior 91; this remains structural judgment, not a probability. **G0 pass:** explicit asset/mechanism/falsifiers. **G1 pass with governance/rights caveat:** durable cash generation, moderate leverage; corpus training rights incomplete. **G2 pass:** management-reported production deployment and credible materiality test, strongest stage E2. **G3 conditional/provisional:** price, shares and scenarios supplied, but quote timestamp and post-Q2 financing/print JV need reconciliation. **G4 fail/not assessed.** Confidence: mechanism 4/5, deployment 3/5, capture 2/5, valuation 2/5.

## Source register

1. [Thomson Reuters Q2 2026 results](https://ir.thomsonreuters.com/news-releases/news-release-details/thomson-reuters-reports-second-quarter-2026-results), 5 Aug 2026; accessed 12 Sep 2026. Primary financials, outlook and segment commentary; non-IFRS measures included.
2. [TR AI for professionals / FAQ](https://www.thomsonreuters.com/en/artificial-intelligence), undated live page; accessed 12 Sep 2026. Primary products, customer count, policy and selected outcomes; promotional and methods absent.
3. [TR investor relations](https://ir.thomsonreuters.com/), accessed 12 Sep 2026. Security/filing index and latest-event check.
4. [TR launches Thomson model](https://www.thomsonreuters.com/en/press-releases/2026/august/thomson-reuters-leverages-its-world-class-data-assets-to-launch-its-own-frontier-model), 24 Aug 2026; accessed 12 Sep 2026. Primary launch claim; no economics.
5. [TR–KKR Global Print joint venture](https://www.thomsonreuters.com/en/press-releases/2026/july/thomson-reuters-and-kkr-announce-joint-venture-for-thomson-reuters-global-print-business), 14 Jul 2026; accessed 12 Sep 2026. Primary transaction announcement; closing effects not modeled.
6. [Stanford/RegLab, “Hallucination-Free?” paper](https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf), working paper 2024 / published 2025; accessed 12 Sep 2026. Controlled older-product evaluation; not current CoCounsel.
7. [Reuters, senior-lawyer sanctions report](https://www.reuters.com/legal/litigation/us-judge-says-senior-lawyers-must-pay-mistakes-by-subordinates-using-ai-tools-2026-05-01/), 1 May 2026; accessed 12 Sep 2026. Adverse case; explicitly unresolved product causation.
8. [RELX 2025 annual report—market segments](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/2025-ar-sections/relx-2025-market-segments.pdf), published Feb 2026; accessed 12 Sep 2026. Primary incumbent comparison; competitor-selected metrics.
9. [Harvey product/customer site](https://www.harvey.ai/), undated live site; accessed 12 Sep 2026. Entrant capability/deployment claims; promotional, no matched economics.
10. Nasdaq TRI quote supplied by live finance vendor, latest trade 12 Sep 2026 00:15 UTC; accessed 12 Sep 2026. Recheck anomalous overnight timestamp before reliance.
11. [Anthropic legal solution](https://claude.com/solutions/legal), undated live page; accessed 12 Sep 2026. Lists a CoCounsel Legal connector, supporting both interface risk and possible backend persistence; no commercial economics.

## Handoff

**Reviewer should verify:** (1) whether CoCounsel truly drives recurring growth versus bundling/price and acquisitions; (2) the 2,700-corporate-customer and 61%-time claims' definitions and dates; (3) quote timestamp and pro-forma debt/FCF after the September notes and print JV. **Strongest counterargument:** rival/generic agents may match grounded quality while clients capture time savings and TR bears US$200m+ annual cost. **Blocking questions:** paid AI ARR/gross margin, adopter renewal/seat cohorts, eligible workload, corpus training rights, inference cost, print-JV and financing bridge. **Provisional disposition:** watch; operating thesis qualified, valuation only conditional. **File written:** `research/batch-01/dossiers/03-thomson-reuters.md`.
