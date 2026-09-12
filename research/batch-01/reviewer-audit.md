# Lead audit notes — batch 01

Research cutoff and access date: 12 September 2026. These are independent checks by the lead reviewer, not a full reproduction of each agent's research. Final decisions are in [lead-review.md](lead-review.md).

## Data rights and distribution

**Thomson Reuters — checked.** The AI FAQ states that customer content and prompts are not used to train or improve CoCounsel, associated products or underlying models. This supports confidentiality; it does not support an unrestricted pooled customer-learning thesis. Proprietary editorial content and per-customer retrieval remain separate potential advantages. Source: [TR AI FAQ, “retain user content or prompts”](https://www.thomsonreuters.com/en/artificial-intelligence), undated.

**SAP — checked.** SAP describes tenant-level data isolation and customer data remaining within the customer's tenancy. Its Joule page alone cannot establish unrestricted cross-customer training rights. Source: [SAP Joule FAQ](https://www.sap.com/products/artificial-intelligence.html), undated.

**Challenger versus complement — checked.** Anthropic's legal offering illustrates workflows using a CoCounsel Legal connector and advertises a Harvey connector. This establishes offered integrations, not customer economics. Reviewer inference: an external AI interface could retain the need for trusted content while shifting control of the customer relationship. Neither total disintermediation nor full retention of incumbent pricing follows from the integration. Source: [Claude legal solutions](https://claude.com/solutions/legal), undated, sections on legal research and Harvey.

## Earnings comparability

**Intuit — material accounting-basis check.** FY2026 reported diluted EPS is $16.46; the old non-GAAP measure is $24.27. From 1 August 2026, Intuit includes share-based compensation in non-GAAP measures. FY2027 guidance is $20.12–20.36 GAAP and $22.88–23.12 on the new non-GAAP basis. Comparing the old $24.27 with the new guidance as if definitions were unchanged is invalid. A GAAP-to-GAAP valuation provides a straightforward initial check. Source: [FY2026 results and FY2027 guidance](https://investors.intuit.com/news-events/press-releases/detail/1320/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance), 25 August 2026, Financial Highlights and Non-GAAP Reporting Change.

At the lead's market-data observation of $321.57 (last trade timestamp 11 September 2026, 23:54:42 UTC), these verified EPS figures imply 19.54× trailing reported earnings and 15.89× the midpoint of guided FY2027 GAAP EPS. Calculations are arithmetic, not fair-value conclusions. The vendor's $16.44 EPS field differs slightly from the filing, so the filing controls the denominator. The quote is an observed web finance feed value, not an official exchange closing-price certification.

## Deployment versus profit

**Wolters Kluwer — checked.** The half-year report describes over 90% of U.S. Enterprise customers adopting UpToDate Expert AI and reports 5% group organic growth. These support a management-reported deployment assessment, not causal AI profit. Adjusted margin increased to 29.4%; the report also says product development spending is weighted toward the second half. Do not annualize that interim margin or attribute its entire improvement to AI. Source: [2026 half-year report](https://assets.contenthub.wolterskluwer.com/api/public/content/3775537-2026-08-05-wolters-kluwer-2026-half-year-results-7d85c04c6c?v=15135ed1), 5 August 2026, pp. 1–3 and divisional discussion.

## Review rules applied

The final review must distinguish confidence in a business mechanism from confidence in buying the security. An attractive scenario range does not automatically pass G3: price provenance, normalized earnings, rights, balance sheet and the no-additional-AI case still matter. No E3/E4 label will be inferred solely from product availability, user count, aggregate growth or a reported margin.

## Corrections made before acceptance

| Area | Finding and lead correction | Decision consequence |
|---|---|---|
| Thomson Reuters DCF | Original $73/$101/$132 figures did not reproduce stated inputs. Recalculated $69.77/$87.70/$106.13; reverse growth 8.5%. Existing AI investment is already in FCF and is not deducted twice. | Base value below price. |
| Intuit forward year | FY2027 guidance is year 1 in the FY2027–31 model: four growth intervals and five discount dates. Values are $198.54/$303.81/$426.19. | Reverse growth is 8.6% at base 17×, or 7.1% at 18×. |
| Intuit efficacy | Payment-reminder association lacks assignment/sample/quality controls. | Initial E3 characterization downgraded to E2. |
| Munich Re efficacy | Mortality risk proof of concept lacks disclosed comparative validation. | E1 for this mechanism, not E3; no profit credit. |
| Financial evidence | Some financial facts were graded E2. | Conventional financials sit outside the AI ladder; SAP ledger corrected. |
| Materiality | Reported annual/adjusted profits were sometimes called normalized. | Marked as scale proxies pending normalization; a 5% calculation does not prove feasibility. |
| Savings ownership | Some initial bridges risked mixing customer labor savings and company costs. | Own-cost pool required for cost savings; customer benefit monetizes through a separate revenue/contribution route. |
| Scores | Several initial sums and sensitivity totals were wrong. | All recalculated in the script. Chubb separately revised by lead to feedback 3/capture 3, total 80/80. |
| RELX | Segment reconciliation omitted print items; Legal revenue bridge used a half-year denominator. | Reconciliation added; £90.5m / annualized Legal revenue is 4.7%, not 9.4%. |
| Wolters Kluwer | Annualized H1 EPS and rerating made cheapness look robust. | Audited-EPS conservative €66.63/stress €33.71 cases added. Quote remains unresolved. |
| Experian | Q1 Consumer decline applied to North America. | Geographic scope corrected; global Consumer grew. |
| Siemens | Current guidance and the future ex-distribution security have different perimeters. | Credit distributed Healthineers value as well as remaining Siemens; a spin-off is not automatic destruction. |
| Schneider | AiDASH EV was being summed as if exact purchase cash consideration. | $350m is implied EV for a roughly 90% acquisition; exact shares, EPS and financing also unresolved. |
| Insurance value | Book, ROE, retention and capital return assumptions need consistency. | Do not substitute tangible book while keeping ROE unchanged. Zero incremental AI credit in lead base decision. |
| Gates | Some agents called an illustrative scenario a G3 pass. | All ten G3 remain incomplete for stated reasons. Absence of E4 is not itself a blanket investment prohibition. |

## Additional independent source checks

- **RELX:** opened H1 presentation/transcript, checked Protégé sales/renewal scope, token-cost scope and segment economics. [Presentation](https://www.relx.com/~/media/Files/R/RELX-Group/documents/results/interim-presentations/2026-first-half-presentation.pdf), [transcript](https://www.relx.com/~/media/Files/R/RELX-Group/documents/investors/transcripts/first-half-results-2026-transcript.pdf).
- **Wolters Kluwer:** opened adverse clinical benchmark study; identified September counterresponse but full text remained unavailable after bounded attempts. No blanket current-clinical-outcome conclusion. [Study](https://www.nature.com/articles/s41591-026-04431-5), [critique](https://doi.org/10.1038/s41591-026-04638-6).
- **Experian:** opened Q1 update for geographic scope and CFPB page for litigation status; allegations are not adjudicated conclusions. [Update](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/experian-fy27-q1-trading-update-announcement.pdf), [CFPB](https://www.consumerfinance.gov/enforcement/actions/experian-information-solutions-inc/).
- **SAP:** opened DSAG report and Q2 filing. Survey scope/fieldwork dates limit interpretation; order inclusion and active workflows are different denominators. [DSAG](https://impulsant.dsag.de/formate/pressemeldung/dsag-investment-report-2026-companies-are-investing-more-selectively-ai-is-becoming-established-cloud-computing-is-being-put-to-the-test/), [Q2 statement](https://www.sap.com/docs/download/investors/2026/sap-2026-q2-statement.pdf).
- **Industrials:** checked demand, distribution and acquisition issues in primary quarterly updates. [Siemens Q3](https://press.siemens.com/global/en/pressrelease/record-third-quarter-outlook-raised), [Schneider H1](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026).
- **Insurers:** opened Munich Re H1 and Chubb Q2/shareholder letter, checking catastrophe/renewal/underlying-ratio confounders. Chubb's precise expense target remains secondary-only. [Munich Re](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/half-year-financial-report.html), [Chubb letter](https://about.chubb.com/stories/2025-chubb-letter-to-shareholders.html). The Chubb Q2 link is in its dossier and the lead review.
- **Insurance regulation:** replaced broad reliance on 2019 life guidance with opened 2024 NYDFS underwriting/pricing guidance; its scope is not every insurance function. [Circular 7](https://www.dfs.ny.gov/industry-guidance/circular-letters/cl2024-07).

## Reproduction and limits

Run `python3 research/batch-01/audit-calculations.py` from the repository root. It reproduces all ten scenario/reverse valuations, structural weights and selected materiality bridges. It checks arithmetic, not forecast truth or quote authenticity; year-zero/forward-year conventions and insurers' hypothetical AI increments are explicit.

Lead source checking was selective and decision-driven, not a complete re-performance of ten audits or legal opinions on data rights. Current quote provenance, point shares, post-transaction financing/perimeters, sustainable earnings and retained AI economics remain open where stated. Source registers preserve the researchers' evidence; lead review does not silently upgrade unverified items.
