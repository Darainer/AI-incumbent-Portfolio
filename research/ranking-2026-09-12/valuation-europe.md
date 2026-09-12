# European valuation scenarios — 12 September 2026

**Wolters Kluwer is the only one of these five whose conventional base case clears a 10% return hurdle, and the headroom is narrow. RELX remains the stronger operating-evidence candidate. Neither conclusion establishes that incremental AI is underpriced.** All five can be valued conditionally; none receives an unconditional buy conclusion from this work.

This packet supersedes the initial batch-01 screening valuations. Decisive prices and annual/interim financial sources were reopened on the cutoff date. September 12 is a Saturday. The observations below are explicitly dated September 11 vendor prices, with the original reporting/listing currencies reconciled. They are not represented as independently certified exchange auction closes. In particular, RELX's reopened historical row is **2,475p**, replacing the earlier 2,446p. Wolters Kluwer's **€66.24** September 11 row also reproduces the previously unresolved €66.20 September 10 observation.

## Comparable current-price results

The 10% hurdle is a nominal local-currency equity return before personal tax and dealing costs, chosen for this review rather than inferred from market consensus. Endpoint prices are five-year conditional outcomes, not near-term targets. Bull cases require both conventional performance and separately specified net AI capture; they are not assigned probabilities.

| Company | Sep 11 price | Normalized EPS | Current P/E | Downside IRR | Base IRR | Bull IRR | Base entry at 10% |
|---|---:|---:|---:|---:|---:|---:|---:|
| RELX | £24.75 | £1.330 | 18.6× | -1.59% | 8.23% | 14.69% | £22.92 |
| Wolters Kluwer | €66.24 | €5.198 | 12.7× | -6.13% | 10.85% | 19.29% | €68.65 |
| Experian | £27.82 | £1.322 | 21.0× | -4.44% | 8.88% | 15.92% | £26.48 |
| Munich Re | €503.40 | €37.156 | 13.5× | -4.83% | 6.56% | 11.94% | €435.78 |
| SAP | €177.26 | €6.347 | 27.9× | -5.11% | 6.49% | 14.85% | €151.47 |

**Valuation method.** Each model values equity earnings, with financing expense, leases/depreciation, tax and minority interests already reflected. It does not add cash or subtract net debt again. Adjusted EPS is not free cash flow: acquisition intangibles, recurring transaction costs, capitalization and working capital still matter. Those limitations are explicit below. Cash generation is a plausibility check; there is no unbridged EPS-to-FCF substitution.

For year `t = 1…5`, `D_t = D_0 × (1 + dividend_growth)^t`. `EPS_5 = normalized_EPS × (1 + conventional_growth)^5 × (1 + terminal_AI_uplift)`. `P_5 = EPS_5 × terminal_P/E`. Entry price at hurdle `r` is `Σ[D_t/(1+r)^t] + P_5/(1+r)^5`. Annual IRR solves the same equation at the observed purchase price. Dividends are gross and approximated at year-end; annual IRR differs slightly from wealth CAGR because it recognizes interim distributions. The JSON contains both, every dividend, and full precision.

SBC remains an expense, and diluted shares are used. Buybacks enter only the per-share growth assumption; no buyback yield is added. Reported buybacks are not automatically sustainable future buybacks. Dividend growth follows conventional earnings; bull AI only affects terminal earnings, so no AI dividend benefit is separately added. Historical/TTM baseline metrics are held as the earning-power snapshot at the cutoff: there is no invented stub-period forecast. This conservatism matters most where the audited annual baseline is older.

**Base cases book zero separate incremental AI.** Existing analytics and currently embedded product innovation belong in conventional earnings. Bull AI uplift is a percentage of conventional year-five after-tax earnings, after model/implementation cost and cannibalization. It is never an annual growth percentage. Growth and terminal multiples are analyst assumptions anchored to observed business mix and results, not fabricated consensus. Terminal P/Es reflect cash conversion, growth durability and structural/cycle risk; no claimed peer-multiple dataset is used.

## Hurdles and reverse valuation

| Company | Entry at 8% | Entry at 10% | Entry at 12% | 10% entry / quote − 1 | Required conventional EPS growth at 10% |
|---|---:|---:|---:|---:|---:|
| RELX | £25.00 | £22.92 | £21.05 | -7.40% | 7.88% |
| Wolters Kluwer | €74.80 | €68.65 | €63.12 | 3.64% | 4.11% |
| Experian | £28.93 | £26.48 | £24.28 | -4.83% | 9.18% |
| Munich Re | €473.53 | €435.78 | €401.81 | -13.43% | 7.88% |
| SAP | €165.55 | €151.47 | €138.82 | -14.55% | 13.79% |

Reverse growth holds each base terminal multiple and dividend path fixed. It does not claim the market literally uses this model. The JSON also contains a 3×3 entry grid with EPS growth ±2 points and terminal multiples ±2 turns. The range matters more than a two-decimal entry number. A 10% entry value is a hurdle-equivalent price, not an additional margin of safety.

For a EUR investor, GBP/EUR must be applied to each RELX and Experian cash flow; there is no assumed FX return. Experian also reports in USD, so its GBP results hold USD/GBP at the verified September 11 **1.3520**, replacing the old 1.3501 input. A sterling listing does not turn its largely USD earnings into a sterling economic asset. EUR listings likewise retain substantial operating currency exposure. No FX hedge or tax-reclaim benefit is included.

## RELX (C034)

**Operating-quality leader; current price falls short of 10% base hurdle.**

LSE: REL ordinary; ISIN GB00B2B0DG97; reporting currency GBP. Quote: [£24.75, 2026-09-11](https://uk.investing.com/equities/reed-elsevier-historical-data).

**Earnings bridge:** Normalized diluted adjusted equity EPS; reconstructed TTM, Twelve months ended 2026-06-30; modeled £1.330135 per diluted share.

- Adjusted attributable earnings £2,358m - H1 2025 £1,171m + H1 2026 £1,225m = £2,412m.
- TTM diluted weighted shares reconstructed from rounded disclosed averages: 1843.5m + (1794.1m - 1854.9m)*181/365 = 1,813.350m; potential small rounding error.
- Headline adjusted EPS is basic. Divide adjusted net earnings by diluted shares; do not double H1 EPS.
- SBC remains expensed (FY2025 £63m); acquired-intangible amortization and company acquisition/disposal adjustments are excluded. No SBC cash-flow addback and no separate buyback yield.

Financial source(s): [Source 1](https://www.relx.com/~/media/Files/R/RELX-Group/documents/press-releases/2026/results-2025-pressrelease.pdf), [Source 2](https://www.relx.com/~/media/Files/R/RELX-Group/documents/press-releases/2026/first-half-results-2026-pressrelease.pdf).

**Evidence and calibration.** H1 underlying revenue/profit momentum remains supportive, but leverage rose to 2.3×. Management's Protégé sales/renewal mix and low token-cost comments support commercial deployment; they do not disclose full product contribution, seat-adjusted renewal uplift or controlled retained AI economics. [H1 transcript](https://www.relx.com/~/media/Files/R/RELX-Group/documents/investors/transcripts/first-half-results-2026-transcript.pdf).

The base 6% nominal per-share growth rate is below recent constant-currency EPS growth. Its approximate 4.5% sales, 0.5-point operating-leverage and 1-point net-share contributions allow margin/currency pressure and limit extrapolation of the accelerated repurchase program. An 18× exit recognizes recurring, capital-light professional workflows while allowing continued interface competition. Downside 14× recognizes partial commoditization; bull 21× requires durable growth and successful capture. Lower acquisition spending cannot be credited while assuming acquisition-driven growth.

| Case | EPS CAGR excluding new AI | Terminal P/E | Terminal AI uplift | Year-5 price | Five dividends total | Annual IRR | Entry at 10% |
|---|---:|---:|---:|---:|---:|---:|---:|
| Downside | 1.00% | 14× | 0.00% | £19.57 | £3.38 | -1.59% | £14.71 |
| Base | 6.00% | 18× | 0.00% | £32.04 | £4.03 | 8.23% | £22.92 |
| Bull | 8.00% | 21× | 6.00% | £43.51 | £4.28 | 14.69% | £30.21 |

The bull case without the separate AI increment returns **13.46%**, compared with 14.69% including it. Thus the modeled AI increment adds **1.24 percentage points** of annual IRR; conventional growth and rerating explain the rest.

**AI requirements, analyst assumptions:** Bull-only net terminal uplift 6%: about 4% group earnings from Legal product contribution, requiring roughly one-third incremental Legal earnings at a circa 12% group-profit weight, plus 2% internal net savings. Illustrative present-scale internal bridge: eligible cost GBP1562m (25% of FY adjusted cost base) x15% task efficiency x60% realization x50% retention minus GBP10m recurring cost, after 22.5% tax, is GBP46.7m or about 2% FY adjusted net profit. This is a calibrated analyst upper case, not a disclosed company result; no released labor is also counted in product contribution.

**Strongest objection:** Trusted content can remain necessary while third-party agents control customer budgets and compress per-seat economics; the 18x base multiple still assumes a durable franchise.

**Falsifiers:**

- Two reporting periods of Legal underlying growth below 5% together with flat/negative seat-adjusted renewal revenue.
- Current-version controlled tests fail to reduce completion plus verification cost against credible rivals.
- Net debt/EBITDA persists above 2.5x without corresponding organic profit growth.

**Remaining uncertainties:** Current price is a vendor close, not independently certified exchange auction print. Acquired-intangible replacement economics and acquisition spending are not fully captured by adjusted EPS; terminal multiples and lower growth compensate only approximately. All AI attribution remains below controlled net-economics evidence; interface ownership, licensing rights and cohort economics unresolved. Leverage rose; 2026 accelerated buybacks cannot be perpetually extrapolated.

**10% entry sensitivity at base dividend path:**

| EPS growth | P/E 16× | P/E 18× | P/E 20× |
|---|---:|---:|---:|
| 4.00% | £19.10 | £21.11 | £23.12 |
| 6.00% | £20.71 | £22.92 | £25.13 |
| 8.00% | £22.44 | £24.87 | £27.29 |

## Wolters Kluwer (C035)

**Most interesting price among these five, but narrow base return edge and large structural downside.**

Euronext Amsterdam: WKL ordinary; ISIN NL0000395903; reporting currency EUR. Quote: [€66.24, 2026-09-11](https://www.investing.com/equities/wolters-kluwer-historical-data).

**Earnings bridge:** FY diluted adjusted equity EPS after recurring-cost allowance, FY2025, conservatively held as cutoff earning-power anchor; modeled €5.197714 per diluted share.

- Start disclosed diluted adjusted EPS EUR5.29, not doubled H1 EPS or IFRS5.64 containing divestment gains.
- Deduct EUR28m pretax recurring allowance (25 acquisition costs +1 integration +2 employee-benefit financing) at 23.6% assumed tax /231.8m diluted shares = EUR0.092286/share.
- FY adjusted earnings exclude divestment gains and acquired-intangible amortization; SBC EUR26m remains expensed.
- No mechanical uplift to FY earnings for2026 buybacks or H1 profit. This conservative hold partly offsets FRR divestment and H2 product spending; it is not exact pro-forma2026 earnings.

Financial source(s): [Source 1](https://assets.contenthub.wolterskluwer.com/api/public/content/3118646-2026-02-25-wolters-kluwer-2025-full-year-results-7391945524?v=2c966da9), [Source 2](https://assets.contenthub.wolterskluwer.com/api/public/content/3775537-2026-08-05-wolters-kluwer-2026-half-year-results-7d85c04c6c?v=15135ed1).

**Evidence and calibration.** The H1 recurring mix and organic cloud growth support conventional resilience; product development is weighted to H2 and guided at 12–13% of revenue. Thus twice H1 EPS is not a normalized annual estimate. The held FY anchor plus explicit recurring-cost allowance avoids that shortcut. [H1 report](https://assets.contenthub.wolterskluwer.com/api/public/content/3775537-2026-08-05-wolters-kluwer-2026-half-year-results-7d85c04c6c?v=15135ed1).

Five percent base EPS growth is below high-single-digit constant-currency guidance and incorporates translation, spending and divestment risk. At 14×, the base allows a modest rerating from the normalized starting multiple; it is not a no-rerating promise. Bull 18× recovers some franchise confidence but creates a substantial part of bull upside. The adverse medical benchmark evidence prevents capitalizing presumed proprietary-answer superiority. The study tests particular tools/tasks, not all procurement, integration or renewal value. [Nature Medicine study](https://www.nature.com/articles/s41591-026-04431-5).

**Interpretation:** a roughly 3.6% gap between quote and hurdle-equivalent entry is too thin to call a robust margin of safety. A one-point lower growth assumption, lower exit multiple, or a stricter acquired-intangible charge can eliminate it. This is a priority diligence candidate, not established AI mispricing.

| Case | EPS CAGR excluding new AI | Terminal P/E | Terminal AI uplift | Year-5 price | Five dividends total | Annual IRR | Entry at 10% |
|---|---:|---:|---:|---:|---:|---:|---:|
| Downside | -5.00% | 10× | 0.00% | €40.22 | €9.14 | -6.13% | €31.94 |
| Base | 5.00% | 14× | 0.00% | €92.87 | €14.62 | 10.85% | €68.65 |
| Bull | 7.00% | 18× | 5.00% | €137.78 | €15.51 | 19.29% | €97.16 |

The bull case without the separate AI increment returns **18.23%**, compared with 19.29% including it. Thus the modeled AI increment adds **1.06 percentage points** of annual IRR; conventional growth and rerating explain the rest.

**AI requirements, analyst assumptions:** Bull-only 5% terminal net uplift. Present-scale illustration: EUR1110m eligible cost (25% of adjusted cost base) x20% task improvement x60% realization x60% retention -EUR20m recurring implementation/inference expense = EUR59.9m pretax, EUR45.7m after 23.6% tax; add circa EUR14.5m distinct net product contribution to reach about 5% of normalized current earnings. No customer time-saving claim is booked as WK cash. Incremental investment is included in the net uplift; residual capitalization risk remains.

**Strongest objection:** The low multiple may correctly anticipate structural erosion; even a regulated content workflow can lose pricing power before subscription attrition becomes visible.

**Falsifiers:**

- Recurring organic revenue growth below 3% for two consecutive half-years.
- UpToDate/CCH renewal value per institution declines after discounts and seat changes while development spend remains12-13% of sales.
- Controlled current-product tests and renewals fail to establish paid workflow value beyond general models.

**Remaining uncertainties:** FRR divested business contribution is not fully isolated; held FY baseline is conservative judgment, not a precise ongoing-company pro forma. H1 margins cannot be annualized because development spend is H2-weighted. USD translation materially affects EUR results despite EUR listing. Adoption and product bundling do not prove willingness to pay; independent clinical benchmarks are adverse but task-bounded. Entry headroom is small and disappears with one-point lower growth or a lower multiple.

**10% entry sensitivity at base dividend path:**

| EPS growth | P/E 12× | P/E 14× | P/E 16× |
|---|---:|---:|---:|
| 3.00% | €55.88 | €63.36 | €70.84 |
| 5.00% | €60.41 | €68.65 | €76.89 |
| 7.00% | €65.30 | €74.35 | €83.41 |

## Experian (C031)

**Good conventional compounder; price remains above10% base entry.**

LSE: EXPN ordinary; ISIN GB00B19NLV48; reporting currency USD. Quote: [£27.82, 2026-09-11](https://tradingeconomics.com/expn:ln).

**Earnings bridge:** FY2026 diluted benchmark equity EPS translated at fixed spot USD/GBP, FY ended2026-03-31; modeled £1.321746 per diluted share.

- Published diluted benchmark EPS USD1.787 /1.3520 USD per GBP, September11 dated FX row. No currency-mixed P/E.
- FY2026 diluted weighted shares919m; FY2027 guidance880-885m is BASIC WANOS and is not substituted as a diluted denominator.
- SBC USD138m plus USD17m associated social-security expense remains in income; no SBC addback. Benchmark EPS excludes acquisition amortization, exceptional/restructuring/transaction expenses and financing remeasurements; these remain normalization uncertainty.
- No explicit buyback yield is added. Baseline contains existing credit analytics/ML; net future share reduction belongs only in EPS-growth assumption.

Financial source(s): [Source 1](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/reports/2026/experian-annual-report-2026.pdf), [Source 2](https://www.investing.com/currencies/gbp-usd-historical-data).

**Evidence and calibration.** The latest trading update maintains a conventional platform-growth thesis but also shows consumer breach-contract run-off. Existing ML, bureau updates, credit volumes and platform migrations already belong in baseline earnings. [Q1 FY2027 update](https://www.experianplc.com/content/dam/marketing/global/plc/en/assets/documents/results-and-presentations/2026/experian-fy27-q1-trading-update-announcement.pdf).

Eight percent base EPS growth assumes approximately 6% net business earnings growth and 2 points from net share reduction; it deliberately sits below a simple addition of revenue guidance, margin guidance and near-term repurchases. Twenty times terminal earnings recognizes recurring bureau/decisioning economics but retains credit-cycle and data-quality risk. Zero growth/15× is a conventional cyclical and regulatory stress. Bull 24× needs continued strong growth and distinct new paid capture, rather than calling old analytics growth AI upside.

**Currency discipline:** USD1.787 diluted benchmark EPS and USD0.6925 dividend are both divided by the same 1.3520 USD/GBP rate. The local-currency return is therefore conditional on constant USD/GBP. [Dated FX history](https://www.investing.com/currencies/gbp-usd-historical-data).

| Case | EPS CAGR excluding new AI | Terminal P/E | Terminal AI uplift | Year-5 price | Five dividends total | Annual IRR | Entry at 10% |
|---|---:|---:|---:|---:|---:|---:|---:|
| Downside | 0.00% | 15× | 0.00% | £19.83 | £2.56 | -4.44% | £14.25 |
| Base | 8.00% | 20× | 0.00% | £38.84 | £3.15 | 8.88% | £26.48 |
| Bull | 10.00% | 24× | 5.00% | £53.64 | £3.44 | 15.92% | £35.87 |

The bull case without the separate AI increment returns **14.85%**, compared with 15.92% including it. Thus the modeled AI increment adds **1.07 percentage points** of annual IRR; conventional growth and rerating explain the rest.

**AI requirements, analyst assumptions:** Bull-only 5% terminal net uplift, deliberately smaller than headline existing-analytics claims. Present-scale USD82m after-tax increment on USD1642m benchmark earnings implies approximatelyUSD110m pretax at 25.5% tax. A distinct net 2% revenue addition at50% incremental contribution margin would supply aboutUSD84m pretax; aboutUSD26m net internal savings completes it. Revenue contribution is after data/model/servicing costs; released labor is not counted twice. These are analyst requirements, not observed conversion economics.

**Strongest objection:** Parallel bureau records and lender-owned outcomes limit unique AI lift; the current21x normalized multiple already pays for substantial conventional compounding.

**Falsifiers:**

- Organic B2B growth below 4% and benchmark margin fails to improve over two reporting periods.
- Controlled lending experiments show no better quality-adjusted approvals at fixed loss/fairness after data and model costs.
- Growth in agent engagements fails to improve retained marketplace contribution or Patient Access net contract economics.

**Remaining uncertainties:** GBP returns vary with USD/GBP; EUR investor also bears GBP/EUR or can analyze underlying USD exposure directly. Transaction/restructuring expenses recur and benchmark earnings may overstate owner earnings. Exact future diluted shares after ongoing buybacks unknown; no point-in-time market-cap denominator is needed for this EPS model. Credit cycle, bureau data quality/remediation and consumer breach-contract run-off can swamp incremental AI benefits.

**10% entry sensitivity at base dividend path:**

| EPS growth | P/E 18× | P/E 20× | P/E 22× |
|---|---:|---:|---:|
| 6.00% | £22.13 | £24.32 | £26.52 |
| 8.00% | £24.06 | £26.48 | £28.89 |
| 10.00% | £26.15 | £28.79 | £31.44 |

## Munich Re (C015)

**Conventional insurer watchlist; material price gap to normalized10% entry.**

Xetra: MUV2 registered ordinary; ISIN DE0008430026; reporting currency EUR. Quote: [€503.40, 2026-09-11](https://tradingeconomics.com/muv2:gr).

**Earnings bridge:** Through-cycle normalized diluted equity EPS; explicit cat/reserve adjustment, FY2025 normalized to expected major-loss load; modeled €37.156413 per diluted share.

- Start audited EPS €47.15; weighted shares129.745410m, no dilution reported.
- P&C reinsurance net insurance revenue €17,316m; actual major losses9.4% versus17% expectation. Deduct7.6points times revenue after analyst22% tax.
- Reserve releases5.0points; deduct2.0points and retain3.0points as ordinary reserve prudence. This is analyst normalization, not management adjusted EPS.
- Normalized EPS =47.15 -(0.076+0.020)*17316*0.78/129.745410 =37.156413. Removing all5reserve points would reduce it further.
- No insurer FCF model. Compensation expense stays within IFRS income; no equity-incentive addback. No extra dividend or buyback yield beyond stated dividends and per-share earnings growth.

Financial source(s): [Source 1](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf), [Source 2](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/half-year-financial-report.html).

**Evidence and calibration.** The full catastrophe bridge is decisive. FY P&C reinsurance major losses were 9.4% of net insurance revenue against a 17% expectation. The model replaces the entire 7.6-point gap, then removes 2 of 5 reserve-release points while retaining 3 points as ordinary reserve prudence. It uses an analyst 22% marginal tax assumption. This gives €37.16 EPS, about 21% below the reported €47.15. Removing all reserve releases, instead of retaining 3 points, lowers the earning anchor by a further roughly €3.12; GSI and investment normalization could reduce it again. [Annual report, business performance and Note 66](https://www.munichre.com/content/dam/munichre/mrwebsiteslaunches/2025-annual-report/MunichRe-Group-Annual-Report-2025-en.pdf/_jcr_content/renditions/original./MunichRe-Group-Annual-Report-2025-en.pdf).

H1's €6.3bn full-year guidance is not substituted for through-cycle earnings: benign catastrophe experience, market gains and weaker renewal pricing coexist. The reported 304% solvency figure also excludes a deduction for the eventual 2026 dividend. [H1 update](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/half-year-financial-report.html).

Base 4% per-share growth is approximately 2% net-income growth plus 2 points of net share reduction. At the terminal 12× P/E, 2% annual repurchases cost about 24% of earnings; the modeled dividend is around 62%, leaving roughly 14% for capital growth. That is compatible with about 2% book growth at mid-teens ROE, but near-term repurchases at today's higher normalized P/E need adequate capital buffers. No separate excess-capital value is added. Nine/12/14× downside/base/bull multiples recognize the cyclicality, tail risk and capital intensity; even bull AI is only 2% of terminal earnings.

| Case | EPS CAGR excluding new AI | Terminal P/E | Terminal AI uplift | Year-5 price | Five dividends total | Annual IRR | Entry at 10% |
|---|---:|---:|---:|---:|---:|---:|---:|
| Downside | -2.00% | 9× | 0.00% | €302.28 | €100.00 | -4.83% | €263.51 |
| Base | 4.00% | 12× | 0.00% | €542.48 | €131.24 | 6.56% | €435.78 |
| Bull | 6.00% | 14× | 2.00% | €710.05 | €139.25 | 11.94% | €545.48 |

The bull case without the separate AI increment returns **11.55%**, compared with 11.94% including it. Thus the modeled AI increment adds **0.39 percentage points** of annual IRR; conventional growth and rerating explain the rest.

**AI requirements, analyst assumptions:** Bull-only 2% net terminal earnings uplift; present-scale equivalent circa EUR96m after tax on normalizedEUR4.82bn earnings. AroundEUR123m pretax equates to circa20bp of FY group insurance revenue, after model and implementation costs. This requires verified expense/selection improvement at unchanged risk and capital; no realized catastrophe luck, reserve release or investment gain counts asAI. Base and downside receive zeroAI.

**Strongest objection:** Even adjusted earnings may still capitalize unusually favorable reserve, investment and GSI experience; the apparent low headline P/E is not a through-cycle bargain.

**Falsifiers:**

- Risk-adjusted renewal pricing remains worse than-5% without corresponding exposure exits or risk reduction.
- Several normalized accident years generate ROE below 12% or adverse development reverses retained reserve prudence.
- Solvency falls toward 200% while distributions and buybacks continue at planned pace.
- Matched risk/capital cohorts fail to show retained AI economics by FY2028.

**Remaining uncertainties:** Normalization assumes3points sustainable reserve releases and uses analyst22% marginal tax; GSI/life/ERGO and investment results are not fully cycle-normalized. Renewal price softening, climate and casualty/social-inflation tails may impair capital faster than EPS implies. H1 annualized profitability is inflated by benign losses and financial markets;2026 EUR6.3bn guidance is not a through-cycle baseline. Book capital and share repurchases require future reconciliation; assumed buybacks must be financed from distributable income, not capital needed for risk.

**10% entry sensitivity at base dividend path:**

| EPS growth | P/E 10× | P/E 12× | P/E 14× |
|---|---:|---:|---:|
| 2.00% | €353.67 | €404.61 | €455.56 |
| 4.00% | €379.64 | €435.78 | €491.92 |
| 6.00% | €407.69 | €469.44 | €531.19 |

## SAP (C041)

**Price watchlist; conventional base does not support current quote at10% hurdle.**

Xetra: SAP ordinary; ISIN DE0007164600; reporting currency EUR. Quote: [€177.26, 2026-09-11](https://www.investing.com/equities/sap-ag-historical-data).

**Earnings bridge:** Diluted TTM non-IFRS equity EPS with SBC normalization, Twelve months ended2026-06-30; modeled €6.346867 per diluted share.

- Use auditedFY non-IFRS attributable net profit €7,156m, not January preliminary release; addH1 2026 €3,833m and subtractH1 2025 €3,432m =€7,557m.
- Reconstructed diluted TTM shares1175m +(1163m-1175m)*181/365 =1169.0493150684931m.
- SBC retained in SAP non-IFRS earnings. TTM SBC1,695 − 949 + 753 = 1,499m; restore annualFY1695m charge because H1 decline partly reflects falling share price. Deduct extra196m at analyst30% tax =137.2m net; earning base7419.8m.
- Non-IFRS removes acquired-intangible/restructuring/litigation expenses and volatile equity gains. Audited IFRS6.10 diluted EPS versus basic6.14 corroborates scale; unbridged assumedEUR7EPS is rejected.
- Do not capitalize reportedFCF directly: SAP cash-flow definition excludes interest and adds property/intangible sale proceeds. EPS contains financing costs; no net-cash or buyback-yield addition.

Financial source(s): [Source 1](https://www.sap.com/docs/download/investors/2025/sap-2025-annual-report-form-20f.pdf), [Source 2](https://www.sap.com/docs/download/investors/2026/sap-2026-q2-statement.pdf).

**Evidence and calibration.** The audited annual report supersedes the preliminary January Q4 statement: audited diluted IFRS EPS was €6.10, and company non-IFRS earnings retained SBC. The TTM bridge normalizes the recent reduction in SBC expense because share-price declines affect compensation accounting. It does not treat falling compensation expense as productivity. [Audited 20-F](https://www.sap.com/docs/download/investors/2025/sap-2025-annual-report-form-20f.pdf).

The €2.50 dividend anchor is the approved FY2025 ordinary payment. [SAP dividend record](https://www.sap.com/investors/en/stock/dividends.html).

The base 10% nominal EPS rate allows cloud migration, margin mix and modest share reduction, below the near-term constant-currency operating ambition. The July acquisition-related profit-guidance reduction, legacy support decline and cash costs constrain it. Cloud backlog and AI inclusion in orders cannot be converted into incremental AI earnings without renewal and usage evidence. [Q2 statement](https://www.sap.com/docs/download/investors/2026/sap-2026-q2-statement.pdf).

A 22× base terminal multiple retains a premium for critical enterprise workflows while allowing slower mature growth. Downside17× reflects ordinary migration disappointment; bull27× requires a stronger-duration franchise as well as the separately modeled 10% AI uplift. The DSAG survey is a limited DACH sample, but demonstrates that SAP order messaging and widespread active SAP AI usage are not interchangeable. [DSAG survey](https://impulsant.dsag.de/formate/pressemeldung/dsag-investment-report-2026-companies-are-investing-more-selectively-ai-is-becoming-established-cloud-computing-is-being-put-to-the-test/).

| Case | EPS CAGR excluding new AI | Terminal P/E | Terminal AI uplift | Year-5 price | Five dividends total | Annual IRR | Entry at 10% |
|---|---:|---:|---:|---:|---:|---:|---:|
| Downside | 3.00% | 17× | 0.00% | €125.08 | €12.50 | -5.11% | €87.14 |
| Base | 10.00% | 22× | 0.00% | €224.88 | €15.84 | 6.49% | €151.47 |
| Bull | 12.00% | 27× | 10.00% | €332.20 | €16.79 | 14.85% | €218.77 |

The bull case without the separate AI increment returns **12.76%**, compared with 14.85% including it. Thus the modeled AI increment adds **2.09 percentage points** of annual IRR; conventional growth and rerating explain the rest.

**AI requirements, analyst assumptions:** Bull-only 10% net terminal earnings uplift. Present-scale normalized earningsEUR7.42bn implyEUR742m net, around EUR1.06bn pretax at 30% tax. Distinct net 5% group revenue uplift at45% incremental contribution margin supplies aboutEUR828m pretax; roughlyEUR232m net internal savings completes the requirement. Contribution margins include model/cloud/service cost and net seat cannibalization; do not also count product-development capacity as removed payroll. This is demanding and conditional, not paidAIARR guidance.

**Strongest objection:** Migration is a strong conventional growth engine, but customers can place non-SAP agents over SAP data; a27x bull terminal multiple and10%AI uplift jointly require unusually good capture.

**Falsifiers:**

- Cloud backlog growth falls below 15% while support/licenses continue high-single/double-digit declines.
- Cloud gross margin remains below 72% or acquisition and serving costs eliminate ordinary operating leverage.
- Authorized production workflows and AI renewal contract value fail to become material by FY2028.
- Repeated large restructuring/litigation adjustments or higher equity-compensation cost prevent reported EPS catching up with adjustedEPS.

**Remaining uncertainties:** Audited annual numbers supersede preliminaryQ4 statement; use only audited-plusH1 bridge. SBC responds to share price and new grants; a rising bull price can increase future compensation cost. Recurring restructuring/acquisition costs and capitalized development weaken the equality of adjusted earnings and owner cash. Cloud backlog is not incrementalAI revenue; renewals, active workflow execution, inference costs and license-design friction unresolved. FY2026 operating guidance is at constant currencies, while EPS model is nominal reportedEUR.

**10% entry sensitivity at base dividend path:**

| EPS growth | P/E 20× | P/E 22× | P/E 24× |
|---|---:|---:|---:|
| 8.00% | €127.64 | €139.23 | €150.81 |
| 10.00% | €138.77 | €151.47 | €164.16 |
| 12.00% | €150.74 | €164.63 | €178.52 |

## Review conclusion and practical limits

Within this packet, prioritize Wolters Kluwer for potential valuation discrepancy and RELX for operating quality. Experian is a credible conventional compounder at a somewhat demanding price. SAP needs a lower entry or stronger sustainable earnings and paid capture. Munich Re needs a lower entry after catastrophe normalization, or a demonstrably better through-cycle earnings case.

These are analyst scenarios; they do not establish fair value to the cent or guarantee any return. The biggest model risks are terminal durability for content/software and normalized underwriting earnings for insurance. Current exchange certification, precise ongoing-company acquisition/disposal bridges and causal AI contribution remain open. Those limitations qualify the valuations rather than being concealed with invented data. The companion JSON is the reproducible source of arithmetic.
