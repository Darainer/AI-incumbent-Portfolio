# Five-year valuation inputs: healthcare and Chubb

Research cutoff and source access: **12 September 2026**. These are conventional equity valuation sensitivities for the lead reviewer, with five separately constrained AI options. **No pharma base case assumes a higher clinical success probability from AI.** The inputs support calculation; they do not by themselves establish G3/G4 or an underpriced stock. Detailed assumptions and sources are in [valuation-health.json](valuation-health.json).

Three findings change the earlier dossiers: Roche's commonly traded non-voting security is now **ROP participation certificate**; AstraZeneca's NYSE security is now a **direct ordinary share**, making the former half-share ADS conversion invalid; and Novartis's H1 net debt is **$39.4bn**, well above the FY2025 $21.9bn anchor. Chubb's audited statutory-capital disclosure provides more support than the earlier dossier's missing consolidated-ratio discussion.

## Price and security audit

| ID | Security used | Price | Date and scope | Reopened source |
|---|---|---:|---|---|
| C001 | Euronext Paris SAN ordinary | €73.26 | 11 Sep2026, exchange valuation close | [Euronext](https://live.euronext.com/en/product/equities/FR0000120578-XPAR) |
| C002 | SIX ROP participation certificate | CHF344.20 | 11 Sep2026,17:30:17 Zurich dated last quote | [Google quote](https://www.google.com/finance/quote/ROP:SWX) |
| C003 | NYSE AZN ordinary | $160.17 | 11 Sep2026,16:00:08 New York close | [Google quote](https://www.google.com/finance/quote/AZN:NYSE) |
| C004 | NYSE NVS ADR,1 ordinary/ADR | $137.16 | 11 Sep2026,16:00:04 New York close | [Google quote](https://www.google.com/finance/quote/NVS:NYSE) |
| C018 | NYSE CB ordinary common | $338.25 | 11 Sep2026,16:00:10 New York close | [Google quote](https://www.google.com/finance/quote/CB:NYSE) |

Roche's quote page retains the old “Genussscheine” label. The issuer identifies ROP, ISIN CH1499059983, and states that participation certificates share earnings/liquidation participation rights with bearer shares. The March2026 AGM approved the exchange. Issued securities comprise702.5627m certificates plus106.691m bearer shares, distinct from807m H1 diluted weighted shares. [Issuer security details](https://www.roche.com/investors/bonds), [H1 report](https://assets.roche.com/f/176343/x/8a0b362d66/hy26e.pdf).

AstraZeneca's ordinary shares began NYSE trading on2 February2026. Its price page also displays **$156.10 after hours** after the same-day SERENA-4 news. The precise after-hours timestamp is unavailable; use that price only as a separately labelled sensitivity. The primary input remains the regular close, which is not a fully post-event market verdict. [Listing announcement](https://www.astrazeneca.com/media-centre/press-releases/2026/astrazeneca-to-complete-direct-listing-on-NYSE.html), [trial update](https://www.astrazeneca.com/media-centre/press-releases/2026/update-serena-4-phase-iii-trial.html).

Novartis confirms one ordinary share per ADR. Dividends are declared in CHF and converted for ADR holders, so USD dividends require a separate FX assumption. [Issuer FAQ](https://www.novartis.com/investors/shareholder-information/frequently-asked-questions).

## Method and normalization

Year5 equity value is normalized EPS × (1+conventional growth)^5 × terminal multiple × (1+incremental AI terminal earnings fraction). Add each year's assumed dividend at its actual model year; do not simply treat early dividends as a year5 cash flow for IRR. The lead reviewer calculates the10% hurdle and8%/12% sensitivity. All growth rates are **nominal in the security's model currency**, not a mechanical extrapolation of constant-currency guidance.

These are EPS equity models: interest, tax, partner economics and noncontrolling earnings remain in the earnings numerator. Debt, leases and pensions are reviewed for resilience and assumptions, **not deducted a second time from EPS-based equity value**. No excess-cash addition, future buyback distribution, or automatic future share-count shrinkage is included. SBC remains an expense, with dilution separately reflected or reserved. Investor tax, withholding, ADR fees and transaction costs are outside the model.

The pharma cash-quality reserves are **analyst assumptions**, not company “normalized” results or a substitute for a complete product-level DCF. They recognize cash restructuring, replacement investment and the fact that excluding acquisition amortization does not make replenishing the portfolio free. Do not apply the same haircut again downstream.

| Company | Verified earnings bridge | Model annual EPS | Normalization and period |
|---|---|---:|---|
| Sanofi | FY2025 business basic€7.83 − H1 2025€3.39 + H1 2026€3.97 =€8.41 | **€6.66** | TTM Jun2026;80% cash/replacement factor ×99% assumed dilution reserve |
| Roche | FY2025 core dilutedCHF19.46 −11.08 +10.85 =CHF19.23 | **CHF15.38** | TTM Jun2026;80% cash/replacement factor |
| AstraZeneca | FY2025 core basic$9.16 ×1550m basic/1562m diluted | **$7.27** | FY2025;80% cash/replacement factor; no automatic2026 uplift |
| Novartis | FY2025 core basic$8.98 −4.69 +4.39 =$8.68; ×1939/1955 FY2025 dilution ratio | **$7.32** | TTM Jun2026;85% cash/replacement factor |
| Chubb | FY2025 core diluted$24.79 minus50% of$1.133bn favorable reserve development after assumed19% tax/401.513338m shares | **$23.65** | FY2025; keeps all$2.921bn catastrophe losses; no benign-H1 annualization |

Sanofi's FY2025 IFRS total EPS€6.40 includes€2.35 discontinued-operations EPS; continuing EPS is€4.05. Business EPS excludes material acquisition/restructuring items. FY2025 FCF€8.089bn was84.7% of business net income and excluded major business acquisitions. H1 FCF€3.724bn was78.2% of business net income. The exact diluted count was not extracted, hence an explicitly assumed1% reserve; no separate value is credited to retained Opella. [FY2025 PDF,pp.10–11,18–20](https://www.sanofi.com/assets/dotcom/pressreleases/2026/2026-01-29-06-30-00-3228191-en.pdf), [H1 PDF,pp.11–12,18–21](https://www.sanofi.com/assets/dotcom/pressreleases/2026/2026-07-30-05-30-00-3335767-en.pdf).

Roche's FY2025 FCFCHF11.807bn was below core group net incomeCHF16.575bn; the simple71% ratio mixes group/NCI scopes and is a quality warning, not exact parent payout capacity. Core diluted EPS is already parent-specific. H1 cash has tax-timing effects. [FY2025 presentation,pp.24,38–40](https://assets.roche.com/f/176343/x/2aefa879f4/irp260129-a.pdf), [H1 report,pp.36,40,72,80](https://assets.roche.com/f/176343/x/8a0b362d66/hy26e.pdf).

AstraZeneca's FY2025 reported basic EPS$6.60 compares with core$9.16. Operating cash$14.575bn less PPE$2.810bn leaves$11.765bn before$3.095bn intangible purchases. This limits how much “core” earnings should be treated as sustainable owner earnings. H1 core EPS$5.21 and reaffirmed low-double-digit CER EPS guidance establish continuing growth, but do not eliminate reinvestment or failed-indication risk. [FY2025 PDF,pp.1,18,23,26](https://www.astrazeneca.com/content/dam/az/PDF/2025/Q4-FY/Full-year-Q4-2025-results-announcement.pdf), [H1 PDF,pp.1,18–20](https://www.astrazeneca.com/content/dam/az/PDF/2026/h1q2/H1-and-Q2-2026-results-announcement.pdf).

Novartis's FY2025 company FCF$17.596bn subtracts PPE$1.548bn from operating cash$19.144bn, while excluding$2.352bn intangible purchases and acquisitions. Core EPS is explicitly **basic**; annual-report diluted EPS/share denominators prevent a misleading label. H1 core EPS fell to$4.39 from$4.69. [Annual report,pp.51,57–58,102,174,F-27](https://www.novartis.com/sites/novartis_com/files/novartis-annual-report-2025.pdf), [Q2 release](https://www.novartis.com/news/media-releases/novartis-delivered-sales-growth-q2-and-further-advanced-pipeline-full-year-guidance-reaffirmed).

Chubb's$24.79 core EPS excludes specified investment/market-risk/tax/integration adjustments versus$25.68 GAAP. The reserve-release normalization is an analyst convention, not a claim that half the reserves were wrong. Keeping the full2025 catastrophe burden avoids assuming good weather. [FY2025 release](https://news.chubb.com/2026-02-03-Chubb-Reports-Fourth-Quarter-Net-Income-of-3-21-Billion,-Up-24-7-,-and-Core-Operating-Income-of-2-98-Billion,-Up-21-7-Consolidated-Net-Premiums-Written-of-13-1-Billion,-Up-8-9-,-with-P-C-and-Life-Insurance-Up-7-7-and-16-9-Record-P-C-Combined-Ra), [10-K,pp.50,209](https://s201.q4cdn.com/471466897/files/doc_financials/2025/ar/Chubb-Limited-2025-10-K-Final.pdf).

## Capital and latest operating checks

| Company | Latest financial position verified | Implication |
|---|---|---|
| Sanofi | Jun2026 company net debt€15.513bn; financial debt€21.672bn; cash€6.350bn; separate leases€1.904bn | Acquisitions, dividend and repurchases consume headroom; model includes no further buyback uplift. |
| Roche | Jun2026 debtCHF31.805bn; cash/securitiesCHF9.734bn; net debtCHF22.071bn; leasesCHF1.503bn; pension liabilityCHF2.398bn | Net debt alone understates fixed claims; no costless AI option. |
| AstraZeneca | Jun2026 gross debt$32.239bn including$2.748bn leases; cash/investments$4.968bn; net debt$26.912bn after net derivatives | Manufacturing/investment demands matter; do not double-count leases. |
| Novartis | Jun2026 net debt$39.4bn vs$21.9bn at2025 year end; H1 M&A/intangibles/other acquisition cash$15.3bn | Failed acquired assets increase capital-allocation risk and narrow buyback flexibility. |
| Chubb | Dec2025 P&C statutory surplus$55.554bn and life$9.160bn;2026 subsidiary dividends available without prior approval$9.6bn; Jun2026 BVPS$195.45/TBVPS$131.93 | Audited capital evidence supports resilience; amounts are not immediately distributable excess shareholder capital. |

Sources: [Sanofi H1,pp.12,21–22](https://www.sanofi.com/assets/dotcom/pressreleases/2026/2026-07-30-05-30-00-3335767-en.pdf), [Roche H1,pp.36,40](https://assets.roche.com/f/176343/x/8a0b362d66/hy26e.pdf), [AstraZeneca H1,p.20](https://www.astrazeneca.com/content/dam/az/PDF/2026/h1q2/H1-and-Q2-2026-results-announcement.pdf), [Novartis Q2 capital section](https://www.novartis.com/news/media-releases/novartis-delivered-sales-growth-q2-and-further-advanced-pipeline-full-year-guidance-reaffirmed), [Chubb10-K Note22,p.211](https://s201.q4cdn.com/471466897/files/doc_financials/2025/ar/Chubb-Limited-2025-10-K-Final.pdf), [Chubb Q2](https://investors.chubb.com/News--Events/news/news-details/2026/Chubb-Reports-Second-Quarter-Per-Share-Net-Income-of-7-30-and-Per-Share-Core-Operating-Income-of-7-26-Up-18-2-Consolidated-Net-Premiums-Written-of-14-7-Billion-Up-3-6-with-PC-and-Life-Insurance-Up-3-0-and-7-5-PC-Combined-Ratio-of-83-8/default.aspx). Chubb states statutory requirements were met and rating-agency capital requirements exceed regulatory minima; no unsupported consolidated solvency ratio is inserted.

## Scenario inputs

All entries are assumptions. Dividends are gross per-share payments in the same currency as the model, ordered years1–5. AI fractions are terminal one-time earnings increments, not annual growth rates.

| Company | Case | Conventional EPS CAGR | Terminal P/E | Incremental AI terminal EPS | Dividends years1–5 |
|---|---|---:|---:|---:|---|
| C001 Sanofi | base | 4% | 11× | 0% | 4.12, 4.20, 4.29, 4.37, 4.46 |
| C001 Sanofi | bull | 8% | 14× | 3% | 4.12, 4.33, 4.54, 4.77, 5.01 |
| C001 Sanofi | downside | -5% | 8× | 0% | 3.50, 3.50, 3.50, 3.50, 3.50 |
| C002 Roche | base | 4% | 17× | 0% | 9.80, 9.95, 10.10, 10.25, 10.40 |
| C002 Roche | bull | 7% | 20× | 4% | 9.80, 10.09, 10.40, 10.71, 11.03 |
| C002 Roche | downside | -2% | 13× | 0% | 9.80, 9.80, 9.80, 9.80, 9.80 |
| C003 AstraZeneca | base | 7% | 18× | 0% | 3.23, 3.33, 3.43, 3.53, 3.64 |
| C003 AstraZeneca | bull | 10% | 22× | 3% | 3.23, 3.39, 3.56, 3.74, 3.93 |
| C003 AstraZeneca | downside | 1% | 13× | 0% | 3.23, 3.23, 3.23, 3.23, 3.23 |
| C004 Novartis | base | 3% | 16× | 0% | 4.50, 4.59, 4.68, 4.78, 4.87 |
| C004 Novartis | bull | 7% | 19× | 3% | 4.50, 4.68, 4.87, 5.06, 5.26 |
| C004 Novartis | downside | -3% | 12× | 0% | 4.00, 4.00, 4.00, 4.00, 4.00 |
| C018 Chubb | base | 5% | 13× | 0% | 4.08, 4.24, 4.41, 4.59, 4.77 |
| C018 Chubb | bull | 8% | 15× | 4% | 4.08, 4.32, 4.58, 4.86, 5.15 |
| C018 Chubb | downside | -2% | 10× | 0% | 4.08, 4.08, 4.08, 4.08, 4.08 |

Dividend anchors are Sanofi€4.12; RocheCHF9.80 approved at the2026 AGM; AstraZeneca latest$1.06 interim plus prior$2.17 second interim, so model$3.23 is a forward assumption; NovartisCHF3.70, translated to assumed$4.50 at **assumed1.216216USD/CHF**, not asserted spot FX; and Chubb approved$4.08 annually. The JSON supplies primary links and every future dividend schedule. Growth of future dividends is discretionary and not promised.

**Sanofi.** Base4% growth assumes approved launches and existing Dupixent indications outweigh legacy erosion, but is far below short-term guidance. The11× terminal multiple reflects concentration and the2031 patent-transition risk rather than assuming stable perpetual peak margins. The July release says amlitelimab will not proceed to global submission and itepekimab/balinatunfib programs were discontinued; those assets contribute no base rescue. Bull8% needs stronger conventional commercial execution. Falsifiers are prolonged weak replacement output, debt rising despite cash generation, and faster Dupixent price/share erosion. [H1 results](https://www.sanofi.com/en/media-room/press-releases/2026/2026-07-30-05-30-00-3335767). The2031 horizon is independently discussed in [Reuters' January results report](https://www.reuters.com/business/healthcare-pharmaceuticals/sanofi-targets-high-single-digit-sales-growth-2026-plans-share-buyback-2026-01-29/); exact legal protection/erosion remains uncertain.

**Roche.** Base4% CHF EPS growth assumes existing Ocrevus/Hemlibra/Vabysmo/Phesgo economics and diagnostics support the group through mature-drug erosion. It contains no unapproved obesity blockbuster or numerical clinical-probability uplift. Bull7% requires stronger conventional execution and diagnostics recovery;20× is reserved for durable replenishment. A failed upfront giredestrant combination is not restored in the base. Falsifiers: sustained diagnostics pricing pressure, product-level competition, and cash conversion failing to recover. [H1 update](https://www.roche.com/investors/updates/inv-update-2026-07-23), [persevERA update](https://www.roche.com/media/releases/med-cor-2026-03-09).

**AstraZeneca.** Base7% recognizes marketed oncology/rare-disease growth while Farxiga US erosion, China procurement and replacement spend remain burdens. Neither CARDIO-TTRansform nor the failed SERENA-4 upfront indication contributes prospective rescue revenue. Existing approved SERENA-6 economics may remain in ordinary portfolio growth; the different indications must not be conflated. Bull10%/22× demands sustained conventional execution and cash conversion. Falsifiers: another material indication loss, sustained capitalized replacement spending above the reserve, or growth dependent on targets lacking risk-adjusted support. [H1 release](https://www.astrazeneca.com/content/dam/az/PDF/2026/h1q2/H1-and-Q2-2026-results-announcement.pdf), [11 September trial update](https://www.astrazeneca.com/media-centre/press-releases/2026/update-serena-4-phase-iii-trial.html).

**Novartis.** Base3% assumes Kisqali/Kesimpta/Pluvicto/Scemblix and ordinary remaining launches offset Entresto/Promacta/Tasigna erosion. The two failed primary endpoints remove confidence in a simple mid-term target extrapolation; no del-desiran DM1 or pelacarsen cardiovascular blockbuster is assumed. Bull7% requires stronger viable marketed/remaining-pipeline execution, not reversal of trial outcomes. Falsifiers: weak post-generic recovery, further acquired-asset failures and leverage persisting without earnings support. [Q2 release](https://www.novartis.com/news/media-releases/novartis-delivered-sales-growth-q2-and-further-advanced-pipeline-full-year-guidance-reaffirmed), [HARBOR update](https://www.novartis.com/news/media-releases/novartis-provides-update-delpacibart-etedesiran-del-desiran-phase-iii-harbor-study-treatment-myotonic-dystrophy-type-1-dm1), [Lp(a)HORIZON update](https://www.novartis.com/news/media-releases/novartis-announces-lpahorizon-phase-iii-topline-results-pelacarsen-patients-elevated-lpa-and-established-cardiovascular-disease-cvd).

**Chubb.** Base5%/13× requires conventional exposure growth and adequate underwriting/investment returns with retained capital. There is no extra AI loss-ratio reduction or automatic buyback EPS accretion. Q2 current-accident-year ex-cat ratio82.2% versus82.3% shows that aggregate results do not establish AI attribution. Bull8%/15× requires stronger conventional execution. Falsifiers are persistent rate/mix-adjusted deterioration, adverse casualty reserves, restricted capital distributions or claims-service damage. [Q2 release](https://investors.chubb.com/News--Events/news/news-details/2026/Chubb-Reports-Second-Quarter-Per-Share-Net-Income-of-7-30-and-Per-Share-Core-Operating-Income-of-7-26-Up-18-2-Consolidated-Net-Premiums-Written-of-14-7-Billion-Up-3-6-with-PC-and-Life-Insurance-Up-3-0-and-7-5-PC-Combined-Ratio-of-83-8/default.aspx).

## AI option and evidence limits

The bull AI increments—Sanofi3%, Roche4%, AstraZeneca3%, Novartis3%, Chubb4%—are **capped sensitivities, not measured outcomes or expected-value clinical forecasts**. They assume incremental workflow/administrative value can be converted to removed expense or paid output, retained after supplier/customer sharing, and net of compute, validation, human review and implementation. No benefit is also counted as a separate pipeline-value asset, revenue uplift or buyback return. No phase-transition rate is changed.

Roche's cap includes pathology workflow economics; the other pharma caps concern research/trial/regulatory operations. Chubb's cap concerns administration and claims handling; it does not assume AI eliminates catastrophe, severity or long-tail reserving risk. If quality or cash conversion is not demonstrated, set every incremental AI input to zero. A three-percent earnings option cannot justify an unsupported high conventional growth rate or multiple.

These remain coarse portfolio earnings scenarios. A full investment decision needs a drug-by-drug exclusivity/indication revenue bridge, recurring replacement investment schedule, exact current diluted/security counts where identified, and independently measured AI cash effects. Normalize pharma reserves across10–30% rather than treating the selected20%/15% values as precise. For Chubb test zero favorable reserve releases, a larger catastrophe allowance and recurring integration expense. The lead reviewer should report failure to meet the chosen hurdle where the arithmetic warrants it; the price fall or AI narrative alone establishes no margin of safety.

