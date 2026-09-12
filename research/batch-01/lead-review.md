# First ten stocks — lead judgment

**Research cutoff: 12 September 2026. Status: initial research and lead review complete.** Five GPT-5.6 Sol agents, using medium reasoning, researched the first ten companies in the existing priority queue. I independently checked decisive sources, challenged evidence grades, reproduced valuation arithmetic and made the decisions below. This is the governing assessment where it differs from a dossier's provisional agent conclusion.

## Decision

**Retain RELX, Wolters Kluwer and Intuit as the priority underwriting shortlist. None of the ten yet earns the label “demonstrably underpriced AI productivity.”** RELX has the strongest commercial evidence, Wolters Kluwer the most interesting potential valuation discrepancy, and Intuit an attractive combination of workflow ownership and conventional earnings worth investigating at the observed price.

Keep Chubb and Munich Re as conventional insurance candidates with an unproven AI option. Keep Thomson Reuters, Experian and SAP on the evidence/price watchlist. Deprioritize Siemens and Schneider Electric for this particular investment thesis at the observed prices: their demand exposure is clearer than their incremental retained productivity economics.

The lack of E4 is not an automatic prohibition on investing. A durable ordinary business bought with a sufficient margin of safety could justify investment while incremental AI remains an option. Here, price sensitivity and unresolved input/normalization questions prevent that conclusion. A completed first research pass does not mean that every investment gate passes.

| Queue | Company and evidence packet | Final disposition | Main reason | Confidence in disposition |
|---:|---|---|---|---|
| 1 | [RELX](dossiers/01-relx.md) | Priority shortlist — strongest operating case | Paid product adoption is credible; current price is near the ordinary-compounding base case | Moderate-high |
| 2 | [Wolters Kluwer](dossiers/02-wolters-kluwer.md) | Priority shortlist — investigate possible mispricing | Low observed multiple merits attention; conservative assumptions remove most apparent upside | Moderate |
| 3 | [Thomson Reuters](dossiers/03-thomson-reuters.md) | Watch for price/economics | Strong content/workflow mechanism; corrected cash-flow valuation is less compelling | Moderate |
| 4 | [Experian](dossiers/04-experian.md) | Watch; no incremental GenAI premium | Excellent established analytics are already in earnings; price requires continued strong cash growth | Moderate |
| 5 | [Intuit](dossiers/05-intuit.md) | Priority shortlist — conventional earnings case | Workflow control and forward GAAP earnings are interesting; weak segments and cash normalization matter | Moderate |
| 6 | [SAP](dossiers/06-sap.md) | Watch for demonstrated usage and paid capture | System-of-record advantage is real; AI order inclusion overstates what we know about active use | Moderate-high |
| 7 | [Siemens](dossiers/07-siemens.md) | Deprioritize at observed price | Demanding growth plus unresolved Healthineers distribution/perimeter | Moderate |
| 8 | [Schneider Electric](dossiers/08-schneider-electric.md) | Deprioritize for this thesis at observed price | Strong AI infrastructure demand is already central to the growth case; productivity capture remains weakly evidenced | Moderate |
| 9 | [Munich Re](dossiers/09-munich-re.md) | Conventional insurer watchlist | Reported profitability must be normalized for cycle, catastrophes and reserves before crediting AI | Moderate |
| 10 | [Chubb](dossiers/10-chubb.md) | Conventional insurer watchlist; preferred AI cost investigation of the pair | Explicit workforce/process ambition is potentially material, but its precise cost target lacks primary verification | Moderate |

Confidence here concerns the research disposition, not certainty about intrinsic value or future returns.

## What the prices require

These are **conditional screening calculations, not price targets or entry levels**. Share classes, quote sources and financial periods are documented in each dossier. Quotes are agent/vendor observations around 10–11 September, not uniformly certified exchange closes. I independently observed the US feed quotes for Intuit, Thomson Reuters and Chubb. Wolters Kluwer's historical quote could not be reproduced from the rendered page; Siemens has conflicting vendor observations. Other agent quotes were not independently certified by the lead. These limitations remain open.

The models preserve their disclosed return hurdles, rather than impose a false common risk level across businesses. Their outputs therefore must not be ranked mechanically. Dividends, FCF, earnings and book-value models use different economic conventions. [The calculation script](audit-calculations.py) makes those conventions explicit and reproduces all ten.

| Company | Observed ordinary price | Bear / base / bull screen | Reverse requirement at stated base assumptions |
|---|---:|---:|---|
| RELX | £24.46 | £16.81 / £24.04 / £32.19 | 5.9% five-year EPS/dividend growth; 18× exit, 9% hurdle |
| Wolters Kluwer | €66.20, quote unresolved | €51.73 / €86.40 / €117.51 | −0.8% growth; 16× exit, 9% hurdle, using annualized H1 EPS |
| Thomson Reuters | $97.35 | $69.77 / $87.70 / $106.13 | 8.5% five-year FCF/share growth; 9% hurdle, 2.5% terminal growth |
| Experian | £27.82 | £18.59 / £24.38 / £29.48 | 10.2% five-year FCF/share growth; 9% hurdle, 2.5% terminal growth |
| Intuit | $321.57 | $198.54 / $303.81 / $426.19 | 8.6% FY2027–31 EPS growth at the base 17× exit; 7.1% at 18×; 10% hurdle |
| SAP | €177.26 | €106.26 / €153.62 / €227.72 | 12.1% 2026–30 EPS growth; 23× exit, 9% hurdle; starting EPS assumed |
| Siemens | €261.70, quote conflict | €125.99 / €202.83 / €287.80 | 10.8% five-year EPS/dividend growth; 19× exit, 9% hurdle; pre-distribution illustration |
| Schneider Electric | €287.40 | €137.77 / €225.34 / €322.96 | 12.5% five-year EPS/dividend growth; 23× exit, 9% hurdle; starting EPS assumed |
| Munich Re | €503.40 | €333.98 / €571.47 / €746.81, conventional only | 13.7% sustainable ROE at 9% hurdle/4% growth; 15.6% at 10%/4% |
| Chubb | $338.25 | $223.37 / $371.36 / $513.06, conventional only | 12.7% sustainable ROE at 9% hurdle/4% growth; 14.4% at 10%/4% |

The insurers' dossier scenarios additionally show hypothetical AI ROE increments. I give those increments **zero underwriting credit** in the lead's base judgment. Raising the equity hurdle from 9% to 10%, holding each conventional base ROE and 4% growth constant, reduces Munich Re's indicated value to **€476.23** and Chubb's to **$309.46**. Neither is an obvious bargain across plausible return requirements.

For Wolters Kluwer, replacing annualized H1 EPS with audited FY2025 EPS produces **€66.63** at 4% growth, a 14× exit and 10% hurdle. A −5% growth/10×/10% stress gives **€33.71**. The apparent €86 value is an assumption-sensitive case, not an established valuation gap.

## Company judgments and conditions that would change them

### RELX

The best current fit is a trusted-content business turning reference access into completed professional work. Management's H1 discussion gives useful sales and renewal evidence for Lexis+ Protégé. It also reports a small token-cost burden, but that excludes the full development, integration and human-review cost of AI. I accept E2 commercial deployment, not E4 retained economics. [RELX H1 transcript](https://www.relx.com/~/media/Files/R/RELX-Group/documents/investors/transcripts/first-half-results-2026-transcript.pdf).

My judgment is positive on the operating thesis and neutral on a purchase at the observed price. Trusted content can retain value even when an external agent controls the interface; the unresolved question is how much pricing power remains with RELX. Promote the investment case only if seat-adjusted renewal economics support extra profit after the full AI cost, or a verified valuation provides a margin of safety without that extra profit. Failed renewals or shrinking content economics would weaken the thesis directly.

### Wolters Kluwer

Broad reported UpToDate adoption establishes distribution strength; it does not establish incremental willingness to pay. H1 spending seasonality makes a straight margin annualization unreliable. [Wolters Kluwer H1 report](https://assets.contenthub.wolterskluwer.com/api/public/content/3775537-2026-08-05-wolters-kluwer-2026-half-year-results-7d85c04c6c?v=15135ed1).

A June study found general models outperforming specialist tools on the examined medical benchmarks. That is a real challenge to an assumed specialist-answer advantage, with limited implications for clinical workflow economics. A September Matters Arising response challenges the benchmark scope; its full text was unavailable in this pass, so the dispute is unresolved. [Nature Medicine study](https://www.nature.com/articles/s41591-026-04431-5), [counterresponse](https://doi.org/10.1038/s41591-026-04638-6).

This is the batch's most interesting possible value case, but confidence in the apparent cheapness is low. A reproducible quote, normalized earnings and renewal economics could move it ahead of RELX as a security. Evidence that generic answers cause price compression would instead turn the low multiple into a justified warning.

### Thomson Reuters

I favor the owned/licensed content and professional workflow mechanism. I reject an unrestricted customer-data learning thesis: the company's policy says customer content and prompts do not train CoCounsel or underlying models. [Thomson Reuters AI FAQ](https://www.thomsonreuters.com/en/artificial-intelligence).

The corrected valuation changes the stock conclusion. Using $2.1bn guided FCF and the stated share denominator gives an $87.70 base screen, below $97.35; reproducing the price needs approximately 8.5% cash growth. Subsequent financing and the print transaction need a pro-forma reconciliation. [Q2 2026 results](https://ir.thomsonreuters.com/news-releases/news-release-details/thomson-reuters-reports-second-quarter-2026-results).

I prefer RELX within this pair for further work at these observations. Thomson Reuters would move up with verified incremental contract economics, a better entry valuation, or conventional cash growth demonstrably supporting the reverse hurdle. An external legal-agent interface is both a distribution opportunity and a bargaining threat.

### Experian

The enduring asset is a decision franchise built around refreshed records, analytic expertise and distribution. Its existing ML economics belong in the ordinary baseline. FY2026 deployment descriptions do not isolate what new generative or agentic tools add. [Experian annual report](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/reports/2026/experian-annual-report-2026.pdf).

The share price already requires strong sustained FCF/share growth. I see no basis for adding a separate GenAI premium now. Paid Ascend cohorts with better retention/contribution, a controlled improvement in decision quality, or a lower price could change that. Data furnished by lenders and permissioned customer context should not be treated as entirely exclusive owned information. The North American consumer decline must also remain geographically scoped; the global consumer result was different. [Q1 FY2027 update](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/experian-fy27-q1-trading-update-announcement.pdf).

### Intuit

This has a credible path from customer records to authorized financial work and revenue capture. The conventional earnings case is more useful today than the AI anecdotes. FY2027 GAAP EPS guidance has a $20.24 midpoint; the non-GAAP definition changes to include stock compensation, so an old-to-new non-GAAP comparison is misleading. [Intuit FY2026 results and guidance](https://investors.intuit.com/news-events/press-releases/detail/1320/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance).

I retain it in the priority three, but the base screen is modestly below price. Customer cash movements complicate a simple FCF reading, and weak tax-unit/Mailchimp trends challenge a frictionless growth story. The payment-reminder comparison remains E2 because assignment, quality and sample controls are missing. Evidence of net revenue and service-cost improvement across comparable QuickBooks cohorts would strengthen capture; worsening core retention would overturn the thesis even if agent usage grows.

### SAP

SAP owns a powerful execution position inside enterprise processes. That advantage does not make all customer data reusable across tenants or prove SAP will own the agent interface. A DSAG survey found SAP production AI usage much lower than non-SAP usage among respondents already implementing AI. The survey ran in December 2025–January 2026 and covered 198 DACH user firms; it is a dated warning about adoption friction, not a September market-share estimate. [DSAG report](https://impulsant.dsag.de/formate/pressemeldung/dsag-investment-report-2026-companies-are-investing-more-selectively-ai-is-becoming-established-cloud-computing-is-being-put-to-the-test/).

I retain the mechanism but put SAP behind the priority three. AI inclusion in orders is insufficient proof of paid active deployment. The €7 model EPS is an analyst assumption, making its double-digit reverse-growth hurdle conditional. Material authorized workflow completion, separately identifiable contract value and a defensible IFRS earnings bridge would change the view. Migration-led cloud growth alone would not prove incremental AI capture.

### Siemens

The installed base and engineering tools provide credible customer access and measurable commissioning/automation opportunities. Data-center orders are a separate demand channel. Current results also describe the planned Healthineers distribution. [Siemens Q3 update](https://press.siemens.com/global/en/pressrelease/record-third-quarter-outlook-raised).

At the observed price, a strong growth outcome is already needed. I therefore deprioritize it for this regime. The model is a current-perimeter illustration: a spin-off transfers value to shareholders, so a valid post-distribution model must include both the remaining Siemens business and the distributed stake/value. It would be wrong simply to remove the earnings and count the distribution as destruction. A reconciled perimeter plus paid Copilot contribution, or a materially better conventional valuation, could change the decision.

### Schneider Electric

The underlying electrification, automation and data-center business is strong. H1 results and proposed Cognite/AiDASH deals support that demand/capability story while adding financing and integration questions. [Schneider H1 results](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026).

I do not equate selling more infrastructure into the AI buildout with retaining incremental productivity gains from incumbent assets. Customer pilots and software claims have not established that profit bridge. Moreover, the €9.80 EPS starting point is illustrative and the agent's share denominator is derived, not reconciled. G3 is incomplete even before debating the demanding price. Scaled customer outcomes tied to Schneider's paid software margins and a pro-forma valuation could change my view; strong infrastructure orders alone would not.

### Munich Re

The franchise and capital discipline warrant conventional insurance analysis. Strong H1 profits coexist with favorable catastrophe experience and softer renewal pricing; those are material alternative explanations to AI. [Munich Re half-year update](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/half-year-financial-report.html).

I assign zero incremental AI value in the base decision. The long-tail feedback problem is substantive: more historical data does not guarantee better prediction of rare future losses. A mortality proof of concept without disclosed comparative validation does not earn E3. Promote the AI operating thesis with a company-specific rollout, credible comparator and material risk-adjusted benefit route. Promote the security only after through-cycle returns, current capital/book value and a payout-consistent valuation justify it.

### Chubb

Chubb has the more explicit internal cost-removal ambition of the insurance pair. Its shareholder letter supports process/workforce change, but the precise 1.5-point savings target was available only through secondary coverage. I exclude that target from decisive gate evidence. [Chubb shareholder letter](https://about.chubb.com/stories/2025-chubb-letter-to-shareholders.html).

The reported Q2 combined-ratio improvement is much larger than the change excluding catastrophes and prior-period development, reinforcing the attribution problem. [Chubb Q2 results](https://investors.chubb.com/News--Events/news/news-details/2026/Chubb-Reports-Second-Quarter-Per-Share-Net-Income-of-7-30-and-Per-Share-Core-Operating-Income-of-7-26-Up-18-2-Consolidated-Net-Premiums-Written-of-14-7-Billion-Up-3-6-with-PC-and-Life-Insurance-Up-3-0-and-7-5-PC-Combined-Ratio-of-83-8/default.aspx).

I retain it as a conventional quality candidate and the preferred insurer for investigating AI expense capture. Verified net savings at stable claims/underwriting quality would matter; headcount reduction alone would not. I reduce the agent's feedback/capture scores to 3/5 each because mature labels, lawful reuse and retention through the pricing cycle remain unresolved.

## Scores and gates after lead review

The original framework is unchanged. These are separate reviewed structural judgments, not statistical posterior probabilities, return forecasts or replacements for the preserved universe snapshot. The six dimensions and both weighting schemes are reproduced in the calculation script. The sensitivity increases capture from 20% to 30% and reduces feedback from 15% to 5%.

| Company | Original prior | Lead structural judgment | Capture-heavy sensitivity | G2 operating thesis | G3 valued opportunity |
|---|---:|---:|---:|---|---|
| RELX | 95 | 84 | 86 | Qualified provisionally at E2 | Incomplete: earnings normalization and renewal/rights economics |
| Wolters Kluwer | 91 | 82 | 82 | Qualified provisionally at E2; bounded adverse efficacy evidence | Incomplete: quote, normalized earnings, valuation sensitivity |
| Thomson Reuters | 91 | 77 | 79 | Qualified provisionally at E2 | Incomplete: pro-forma financing/transaction and cash bridge |
| Experian | 94 | 76 | 76 | Qualified provisionally at E2 | Incomplete: current share/FCF bridge; price case unpersuasive |
| Intuit | 91 | 80 | 80 | Qualified provisionally at E2 | Incomplete: normalized owner earnings/current share bridge |
| SAP | 91 | 80 | 80 | Narrow provisional qualification: scoped customer deployment | Incomplete: assumed EPS and point shares |
| Siemens | 87 | 73 | 75 | Narrow provisional qualification at E2 | Incomplete: quote conflict and distribution perimeter |
| Schneider Electric | 83 | 73 | 75 | Narrow provisional qualification at E2 | Incomplete: assumed EPS, shares and acquisition financing |
| Munich Re | 87 | 74 | 74 | Not qualified: company-specific material measurement route insufficient | Incomplete: quote, current capital and through-cycle returns |
| Chubb | 85 | 80 | 80 | Not qualified: primary target/workload/comparator insufficient | Incomplete: normalized ROE, book basis and capital-return consistency |

All ten remain G0 candidates with provisionally credible G1 businesses; product-specific data rights and applicable balance-sheet/governance questions remain explicit reservations. No company is promoted to G4 and no portfolio weights are assigned. Financial statements are conventional business evidence outside the AI E0–E4 ladder. Across this batch, no positive E3/E4 result was established for the incremental shareholder-profit mechanism.

## What the agent process established

The approach is useful provided the lead reviews rather than aggregates. It produced ten structured packets with sources, rights audits, challengers, measurement contracts and valuation requirements. Review caught material DCF and forward-year timing errors, optimistic gate labels, an overgraded efficacy claim, customer-versus-company savings confusion, an earnings-definition change and incomplete quote/perimeter bridges. Corrections and limits are recorded in the [audit notes](reviewer-audit.md).

For subsequent batches, retain the [research instructions](../agent-instructions.md), require machine-reproducible arithmetic, and make normalization/quote failures explicit before a researcher assigns G3. The next decision work is concentrated on the three shortlisted stocks and the specific conditions above; the other seven already have a documented disposition and falsifiers.
