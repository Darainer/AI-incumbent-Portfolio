# Intuit (C037) — initial dossier

> Lead review complete. The [lead judgment](../lead-review.md) governs dispositions, scores and gates; provisional agent views below are retained for traceability.

**Status:** research-agent packet; lead reviewed 12 September 2026.  
**Security:** Intuit Inc. common stock, Nasdaq: INTU; quote/reporting currency USD.  
**Cutoff / retrieval date:** 12 September 2026. FY2026 ended 31 July 2026; 10-K filed 9 September. Price is the 11 September close.  
**Industry:** vertical software and financial administration (I02).  
**Provisional conclusion:** The ordinary business is profitable, cash-generative and still growing without assuming any *additional* AI uplift. Intuit has E2 production deployment and one useful payment-reminder association, but no disclosed cohort bridge from AI use to retention, net revenue, or cash contribution. At $321.57, the shares imply roughly 7% FY2027–31 EPS growth under a 10% return hurdle and 18× terminal P/E, with exposure to Mailchimp stagnation, tax-unit contraction, model cost, and interface competition. Provisional disposition: **watch; G3 remains blocked pending valuation-input audit**.

## Conventional business and financial resilience

Intuit sells tax preparation, accounting, payroll, payments, marketing and consumer-finance matching products. FY2026 segments are Global Business Solutions (GBS: QuickBooks and Mailchimp) and Consumer (TurboTax, Credit Karma and ProTax); Mailchimp separates in FY2027. The system-of-record role, accountant channel and payment/payroll rails create recurring engagement. Only 8% of revenue was international, leaving U.S. tax-policy concentration.

The [FY2026 10-K](https://investors.intuit.com/sec-filings/all-sec-filings/content/0000896878-26-000037/intu-20260731.htm) shows a strong baseline: revenue grew 14%, GAAP operating profit 20%, and diluted EPS 20%. GBS revenue was $12.864bn and Consumer $8.584bn. QuickBooks Online Accounting grew 23% to $5.051bn, while the more mature desktop ecosystem still produced $2.946bn. Consumer quality is mixed: TurboTax revenue rose 7% despite total U.S. units falling 2%, Credit Karma rose 20%, and TurboTax Live rose 37% to 53% of TurboTax revenue. These results already include deployed AI and pricing; they are the zero-*additional*-AI baseline. FY2027 guidance signals deceleration: total revenue growth falls to 9–10%, TurboTax to 2–3%, and Mailchimp to −1% to flat.

| USD millions except EPS | FY2024 | FY2025 | FY2026 | Comment |
|---|---:|---:|---:|---|
| Revenue | 16,285 | 18,831 | 21,448 | 14% FY2026 growth |
| GAAP operating income | 3,630 | 4,923 | 5,884 | 27.4% margin in FY2026 |
| Net income / diluted EPS | 2,963 / $10.43 | 3,869 / $13.67 | 4,566 / $16.46 | FY2026 diluted shares 277m |
| Operating cash flow | 4,884 | 6,207 | 8,838 | FY2026 boosted by working-capital/funds movements; not equal to recurring owner earnings |
| Property/equipment purchases | 191 | 84 | 175 | Simple FCF = OCF − PP&E purchases = $8.663bn; interpretation constrained by customer-funds flows |

At 31 July 2026, cash plus investments were $7.2bn and debt $7.7bn; customer funds are segregated. FY2026 repurchases of $5.5bn reduced weighted diluted shares 2% despite stock compensation. GAAP stock compensation was $2.056bn, 35% of operating income. FY2027 non-GAAP reporting now includes stock compensation, so FY2026 non-GAAP EPS of $24.27 is **not comparable** with FY2027 non-GAAP guidance.

The [25 August 2026 results](https://investors.intuit.com/news-events/press-releases/detail/1320/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance) guide FY2027 revenue to $23.279–23.512bn, GAAP operating income to $7.408–7.490bn and GAAP EPS to $20.12–20.36. The profit step includes restructuring effects: the 10-K records a $293m FY2026 charge and estimates $315m total plan cost. Mailchimp guidance is −1% to flat. Other risks include tax competition, AI accuracy, privacy, cyber exposure and model reliance.

## Scarce asset and data-rights audit

| Input | Origin / owner | Exclusive? | Retrieval / inference rights | Training / cross-customer rights | Labels / quality | Replication threat |
|---|---|---|---|---|---|---|
| QuickBooks ledger, invoices, bank feeds, payroll | Customer and connected institutions; Intuit is processor/steward | Customer context is unique, not Intuit-owned | Product use appears permitted to provide requested service | **Unknown.** [Stewardship principles](https://www.intuit.com/privacy/data-stewardship-principles/) allow use to operate the business and improve customer experience, and publication of combined de-identified data; they do not establish unrestricted model training | Reconciliations, payment outcomes and filings offer labels, but corrections and exceptions matter | Xero, banks and accountants possess overlapping records; portability/APIs lower exclusivity |
| TurboTax returns and expert interactions | Taxpayer; Intuit holds sensitive records and generated workflow context | Customer-specific history is difficult to recreate but legally constrained | Usable for preparation/support subject to consent and law | Pooled learning permission not verified; privacy safeguards are not ownership | Accepted/rejected filings and expert corrections are useful; delayed audits weaken labels | IRS/free-file alternatives and rival tax software can reproduce much of the rules engine |
| Credit Karma member and marketplace response data | Member, bureaus and financial partners | Licensed and relationship-specific, partly non-exclusive | Used for recommendations and matching | Contractual pooled-training scope unknown | Click, approval and repayment outcomes; selection bias and partner underwriting confound | Lenders, bureaus, aggregators and generic agents have substitutes |
| Mailchimp campaign/content/engagement data | Customer and recipients | Tenant-specific | Service delivery and analytics | Cross-customer training/benchmark rights unknown | Opens/clicks/conversions are frequent but privacy changes impair observation | HubSpot, Salesforce and independent agents connect to the same channels |
| Intuit tax code, workflow software and expert playbooks | Intuit/licensed public law; experts contribute | Software/integration proprietary; statutes public | Full product use | Internal code and operational learnings likely usable; exact rights to expert/customer content unknown | High-quality workflow constraints; tax changes cause drift | Rivals can encode public rules; trust/distribution and integrations take longer to replicate |

The asset is workflow context and execution permission, not a proven proprietary training corpus. Intuit serves about 93m customers, uses third parties that may receive customer data, and warns that processing errors can harm results. Distribution comes with liability and supplier risk.

## Mechanisms, deployment and competition

**1. QuickBooks accounting and payments agents (generative assistance plus agentic execution).** Intuit’s [1 July 2025 launch](https://investors.intuit.com/news-events/press-releases/detail/1258/intuit-introduces-ground-breaking-virtual-team-of-ai-agents-to-fuel-growth-for-businesses) says agents categorize transactions, reconcile books, draft/send invoices and reminders, and manage leads. Rollout began that day across a range of U.S. QuickBooks Online plans. The strongest disclosed outcome is an association framed as a comparison: U.S. beta customers using outstanding-invoice notifications and AI-drafted reminders were paid an average five days faster than customers sending standard reminders to the same customers during January–August 2024. Without sample size, assignment method, invoice mix, quality controls, cash collected or cost, this remains **E2**, not the repository's carefully matched E3 standard. A survey says 45% of users of the new bank feed saved 12 hours monthly, which is E2/self-reported rather than controlled efficacy.

The scarce asset is live ledger/invoice/customer history plus permission to send inside QuickBooks. The output is faster collection or cleaner books; value can reach Intuit through higher price, retention, payment volume, or expert-service attach. Human approval and accountants remain quality controls. No disclosed net contribution margin establishes shareholder capture.

**2. TurboTax AI plus human expert service (assistance with limited execution).** Tax rules, prior returns and expert review can reduce interview friction, route complex cases and raise TurboTax Live attachment. Live’s 37% FY2026 growth and 53% revenue share show commercial migration, but do not isolate AI from marketing, price/mix or human service. Total TurboTax units fell 2%, so higher revenue may coexist with weaker volume and rising labor/service cost. Evidence is E2 for platform availability and aggregate adoption, E0–E1 for incremental AI economics.

**3. Internal productivity (agentic workflow).** [Intuit’s technology page](https://www.intuit.com/technology/) describes GenOS across coding, testing and operations. Restructuring, mix, pricing and lapping charges confound FY2027 margin expansion. No controlled output, quality result or recurring AI cost is disclosed: E1.

[Xero’s 20 August 2026 release](https://www.xero.com/us/media-releases/new-ai-innovations-xerocon-denver/) reports more than 100m transactions auto-reconciled, roughly 50% reconciliation time saved, early-access month-end agents and integrations with Claude, Microsoft 365 and ChatGPT. This company-reported E2 disproves uniqueness. Generic agents can query ledgers through APIs. Intuit’s defense is its U.S. base, execution rails and experts; its vulnerability is an external agent that owns interaction and treats QuickBooks as a replaceable ledger.

## Evidence ledger

| Claim | Type | Source/date; section | Scope / stage | Main confounder |
|---|---|---|---|---|
| FY2026 revenue $21.448bn; GAAP operating income $5.884bn | Fact | 10-K, 9 Sep 2026; MD&A | Company, E2 financial baseline | Price, mix and acquisitions |
| FY2027 GAAP EPS guidance $20.12–20.36 | Management claim | Results, 25 Aug 2026; guidance | Company forecast, E1 | Restructuring benefits, tax, macro |
| Payment-agent beta invoices paid five days faster | Management-reported association | Agent release, 1 Jul 2025; footnote 3 | Narrow QBO feature, E2 | Undisclosed sample, assignment, selection, amount/cost |
| 45% of bank-feed users report saving 12 hours/month | Management survey claim | Agent release, 1 Jul 2025; footnote 1 | Feature users, E2 | Self-report, no quality/cost control |
| Agents rolled out in U.S. QBO plans | Fact/company report | Agent release, 1 Jul 2025; availability | Production availability, E2 | Eligible denominator and active use undisclosed |
| TurboTax Live revenue +37% | Fact | Results, 25 Aug 2026; segment results | Commercial outcome, E2 | Price, marketing and human expert service |
| Customer data may be used to operate/improve experience; pooled training rights unproved | Fact + inference | Data principles, undated; retrieved 12 Sep 2026 | Rights, E1 | Product-specific contracts may differ |
| Xero auto-reconciled >100m transactions and claims ~50% time saved | Rival claim | Xero, 20 Aug 2026; reconciliation | Challenger deployment, E2 | No independent quality-adjusted comparison |
| Mailchimp FY2027 revenue guide −1% to flat | Management claim | Results, 25 Aug 2026; guidance | Core adverse evidence | Portfolio resegmentation |
| May 2026 plan cuts workforce; $315m expected cost | Fact | 10-K, 9 Sep 2026; Note 15 | Core/cost action | AI attribution absent |

## KPI contract and retained-economics bridge

| KPI | Baseline / comparator | Eligible population | Quality constraint | Known result / next proof |
|---|---|---|---|---|
| Days-to-payment and net payment gross profit | Standard reminders to same customer | QBO invoices with overdue risk | Bad reminders, disputes, opt-outs, cash actually collected | Five days faster reported; require sample, dollars, fees and renewal at next FY/Q result |
| Verified reconciliations per accountant hour | Existing QBO bank feed | Active bank-feed users and transactions | Error/correction rate and close accuracy | 12 hours is survey-only; require logs, matched cohort and six-month persistence |
| Total spend and retention after agents | Pre-agent cohort / randomized holdout | Customers offered agents | Include downgrades, seat/expert cannibalization, inference and support | Unknown; FY2027 GBS growth and cohort disclosure are next events |
| AI contribution margin | No-agent product economics | AI-active accounts | Fully loaded model, human review, implementation and liability cost | Unknown |

The research hurdle is an assumed 5% of normalized operating profit. FY2026 reported GAAP operating profit provides a scale proxy of **$294m annual net operating benefit** within five years, pending normalization. Illustrative cost bridge: if $3.0bn of service, support and product-development cost is eligible, 15% task efficiency × 60% realization × 50% retained share − $100m recurring AI cost = **$35m**, only 0.6% of operating profit. A stronger 25% × 75% × 70% − $100m = **$294m**, exactly the hurdle. Thus modest time savings are insufficient; Intuit needs broad workload eligibility, real capacity conversion and/or revenue capture.

A revenue route may be more plausible: on $12.864bn GBS revenue, a 3% incremental revenue lift at a 75% contribution margin, less $100m serving/cannibalization cost, yields **$189m**. Reaching $294m needs about 4.1% incremental GBS revenue at those economics. Neither requirement is established by current disclosures.

## Valuation and reverse valuation

The closing price was **$321.57 on 11 September 2026** ([MarketWatch dated report](https://www.marketwatch.com/data-news/intuit-inc-stock-outperforms-competitors-on-strong-trading-day-a32c9d2e-89642996b522)); FY2026 diluted shares were 277m, implying about $89.1bn equity value on that period-average denominator. FY2026 cash/investments of $7.2bn less $7.7bn debt gives an approximate $89.6bn enterprise value. The share count is not a point-in-time basic count; this is an initial valuation limitation.

Simple five-year EPS framework uses FY2027 GAAP guidance midpoint $20.24 as **year 1**, a 10% equity return hurdle, terminal P/E and approximately $5.52 annualized current dividend, with dividends assumed to grow with EPS. FY2031 terminal EPS therefore compounds for four years. It treats stock compensation in earnings and assumes buybacks only insofar as reflected in EPS growth.

| Case | Conventional / AI assumption | FY27–31 EPS CAGR; terminal P/E | Approx. PV/share | Interpretation |
|---|---|---:|---:|---|
| Bear | Mailchimp/tax pressure; zero uplift, model cost adverse | 2%; 13× | **$199** | Core growth slows; multiple contracts |
| Base | Durable conventional franchise; no separately credited AI uplift | 7%; 17× | **$304** | Below market price on these assumptions |
| Bull | 8% conventional growth + 3pp conditional AI/productivity contribution | 11%; 21× | **$426** | Requires broad capture absent today |

Formula: terminal value = $20.24 × (1+g)^4 × terminal P/E; discount terminal value and annual dividends at 10%. Rounded outputs are scenario results, not fair-value precision. At $321.57 and an 18× terminal multiple, the reverse calculation requires approximately **7.1% FY2027–31 EPS CAGR** after credit for growing dividends; at 15× it requires roughly **11.9%**. A one-point change in the return hurdle or terminal multiple changes value materially. G3 remains blocked because point-in-time shares and normalized cash flow have not been reconciled and the large post-results price move warrants source audit.

## Risks, falsifiers and alternative

Positive hypothesis: Intuit’s ledger, execution rails, tax workflow and experts let agents complete consequential work, raising price/retention and transaction profit faster than model and support costs.

Negative hypothesis: generic agents own the interface while ledgers become interchangeable. Intuit absorbs inference and verification costs, cannibalizes expert/seat revenue and competes through price. Xero makes this credible.

Falsifiers:

1. Agent-exposed cohorts show no sustained improvement in total spend/retention or show higher correction/support cost after two renewal cycles.
2. Xero or cross-vendor agents match completion quality while customers increasingly access QuickBooks only through third-party interfaces and Intuit’s effective price falls.
3. Conventional failure: Mailchimp declines for two years, TurboTax units keep contracting and GBS growth falls below high single digits despite buybacks.

Xero is the direct product alternative. Waiting for cohort economics is rational: current evidence does not make AI cash-certain.

## Priors, revisions, gates and confidence

| Dimension | Original prior | Proposed revision | Reason |
|---|---:|---:|---|
| Scarce asset | 5 | 4 | Workflow context is valuable; ownership and pooled-training rights are limited/unknown |
| AI leverage | 5 | 5 | Accounting, collections and tax are central workflows |
| Feedback | 4 | 3 | Outcomes are frequent, but lawful reuse, bias and correction labels are unresolved |
| Testability | 4 | 4 | Payment/reconciliation tests are fast and measurable; company disclosure is thin |
| Distribution | 5 | 5 | About 93m customers, accountant channel and embedded payments |
| Capture | 4 | 3 | Pricing and payment attach can capture value; seat/expert cannibalization and rival agents matter |

Revised structural score is **80/100** (prior 91). Capture-heavy sensitivity (capture 30%, feedback 5%) also equals 80, so the judgment is not weight-fragile.

| Gate | Status | Reason |
|---|---|---|
| G0 candidate | Pass | Explicit asset, mechanisms, capture route and falsifiers |
| G1 qualified business | Pass, moderate confidence | Profitable recurring franchise, low net debt; rights scope still incomplete |
| G2 operating thesis | Pass, low/moderate | E2 rollout, payment association and measurable route to stronger controlled evidence |
| G3 valued opportunity | Blocked | Dated price and scenarios exist, but point share count, normalized FCF and abrupt price repricing need audit |
| G4 portfolio eligible | Blocked | G3 incomplete; no portfolio sizing/correlation work |

Confidence: **mechanism high; deployment moderate; capture low; valuation moderate-low**.

## Source register

1. Intuit, [FY2026 Form 10-K](https://investors.intuit.com/sec-filings/all-sec-filings/content/0000896878-26-000037/intu-20260731.htm), filed 9 Sep 2026, Business, Risk Factors, MD&A and Notes 11/14/15; audited, but no AI attribution.
2. Intuit, [Q4/FY2026 results and FY2027 guidance](https://investors.intuit.com/news-events/press-releases/detail/1320/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance), 25 Aug 2026; management guidance.
3. Intuit, [AI agents launch](https://investors.intuit.com/news-events/press-releases/detail/1258/intuit-introduces-ground-breaking-virtual-team-of-ai-agents-to-fuel-growth-for-businesses), 1 Jul 2025; samples/economics undisclosed.
4. Intuit, [Data stewardship principles](https://www.intuit.com/privacy/data-stewardship-principles/), undated; not product-specific terms.
5. Intuit, [Technology / GenOS](https://www.intuit.com/technology/), undated; capability only.
6. Xero, [AI innovations at Xerocon US](https://www.xero.com/us/media-releases/new-ai-innovations-xerocon-denver/), 20 Aug 2026; unaudited challenger claims.
7. Xero, [Xerocon London](https://www.xero.com/us/media-releases/xero-announces-new-ai-innovations-xerocon-london/), 9 Jul 2026; scale and roadmap.
8. MarketWatch, [INTU dated close](https://www.marketwatch.com/data-news/intuit-inc-stock-outperforms-competitors-on-strong-trading-day-a32c9d2e-89642996b522), 11 Sep 2026; secondary quote.
9. Intuit, [TurboTax product page](https://turbotax.intuit.com/), retrieved 12 Sep 2026; marketing source.
10. IRS, [E-file free options](https://www.irs.gov/e-file-do-your-taxes-for-free), updated 2026; substitute evidence.

## Handoff for lead review

- **Three decisive claims to verify:** (1) the payment reminder result supports E2 only because assignment/sample/controls are undisclosed; (2) FY2027 guidance plus $321.57 price supports the 7.1% reverse-growth result at 18×; (3) data principles do not establish pooled model-training rights.
- **Strongest counterargument:** FY2026 growth and FY2027 margin guidance may already demonstrate platform capture even without product-level attribution; the conservative framework may under-credit an integrated franchise.
- **Blocking questions:** Point-in-time diluted/basic shares; AI-active cohort spend/retention; model and human-review cost; customer-specific training clauses; reconciliation accuracy/error rates; Mailchimp remediation.
- **Provisional disposition:** Watch. G3 and G4 blocked; E3/E4 absent.
- **File written:** `research/batch-01/dossiers/05-intuit.md`.
