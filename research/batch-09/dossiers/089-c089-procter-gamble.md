# C089 — Procter & Gamble evidence dossier

**Unreviewed agent work.** Procter & Gamble; PG (NYSE, USD quote/reporting). Cutoff/retrieval 12 September 2026. Latest period: FY2026 ended 30 June, released 29 July 2026.

## Business and financial anchor

Procter & Gamble sells high-frequency consumer goods/retail services through massive distribution. Its scarce-asset hypothesis is brand/category histories, retailer sell-through, consumer research, formulation/manufacturing know-how and global distribution. AI could forecast demand, design media/product concepts and optimize plants/supply so gross margin and full-price volume improve. Classical forecasting, optimization and automation already embedded in current margins remain the ordinary baseline.

Latest results reported **$87.0bn net sales**, **about $19.75bn GAAP operating income implied by the reported 22.7% operating margin; net earnings $16.1bn**, and **$19.6bn operating cash flow; adjusted FCF productivity 100%**. Sources: [latest results](https://us.pg.com/newsroom/news-releases/PG-Announces-Fourth-Quarter-and-Fiscal-Year-2026-Results/) and [annual report](https://s204.q4cdn.com/332108499/files/doc_financials/2026/ar/2026_annual_report.pdf). FCF/adjusted measures differ from GAAP. FY2026 core operating margin fell 70bp and ordinary productivity, restructuring, mix, commodity/tariff and pricing actions confound any AI attribution. Revenue is a poor benefit denominator because product/merchandise cost passes through; operating profit and cash after inventory/capex are more relevant.

The zero-incremental-AI business has scale purchasing, trusted brands/store access and repeat demand. It faces retailer/supplier bargaining, private label/digital competitors, commodity/tariff/FX exposure and changing consumers. Dividends/buybacks coexist with capital needs; automation can require distribution, robotics and data capex.

## Rights audit

| Input | Owner/exclusivity | Permitted inference/training | Labels/quality | Replication threat |
|---|---|---|---|---|
| Point-of-sale/search/basket | retailer/customer; supplier receives contracted feeds | customer service/analytics under privacy and retailer agreements; cross-retailer pooling not universal | frequent sell-through labels, promotions confound | Amazon, retailers and syndicated-data vendors |
| Loyalty/membership/advertising | customer/platform | consent, purpose and opt-out constraints; clean-room terms apply | identity improves attribution, but walled-garden bias | retail-media networks and card issuers |
| Product/formulation/consumer tests | manufacturer and research participants | internal R&D/marketing within consent; agency/vendor rights vary | expert/consumer labels, samples may not predict market | rivals conduct comparable research; public reviews |
| Supplier inventory/logistics | supplier/retailer/carrier | operations under contract; training/reuse terms undisclosed | availability and fulfillment observable; substitutions distort | suppliers and logistics vendors multi-home |

Scale does not create universal ownership. Clean rooms/customer-specific inference can be valuable without allowing raw data extraction or pooled training. Generated packaging/media also raises copyright, endorsement and claims-review obligations.

## Mechanisms and challengers

1. **Demand/replenishment (classical ML).** Store/SKU demand, price and inventory → order/allocate → higher in-stock with lower waste/markdown/working capital → gross profit/cash. A Microsoft customer story names Azure IoT Operations and edge predictive models at P&G plants and reports up to 90% less time to deploy a new model version. This is supplier-reported E2 deployment/process evidence; it is not an OEE, downtime or cash result.
2. **Media/search/personalization (ML/generative).** Consumer context and product claims → choose/generate content/ranking → incremental quality-adjusted purchase → contribution or ad revenue. Feature availability is E1/E2; ROAS can be biased by targeting and cannibalization.
3. **Operations/agentic automation.** Orders, plant/fulfillment state → schedule or execute work → more units/orders per labor hour at equal quality/safety → cost/capacity benefit. Robots/process systems and AI must be separated; hours saved become cash only when removed or redeployed into valued output.

Direct challengers are **Unilever and private label**. Syndicated data, agencies, commerce platforms and generic models are substitutes/suppliers. Retailers can use their own data to bargain; consumer brands may pay retail-media tolls. Lower costs can pass through prices. An AI shopping agent can weaken brand/store interface and emphasize price.

| Claim | Type/source | Stage | Confounder |
|---|---|---|---|
| Latest financials above | Company fact | Financial | tariff, mix, price, currency |
| Forecast/automation tools operate at scale | Company claim | E2 baseline | capex/process redesign |
| GenAI/search/content capabilities exist | Company/product claim | E1/E2 | adoption and incrementality |
| Transaction feedback is frequent | Business inference | E0 mechanism | promotions and selection |
| Customer/retailer/supplier rights are bounded | privacy/contract inference | Rights | contracts unavailable |
| Rival has comparable data/tools | rival filing/product | Challenger | effectiveness differs |
| FY2026 core operating margin fell 70bp and ordinary productivity, restructuring, mix, commodity/tariff and pricing actions confound any AI attribution | results/adverse fact | Financial/adverse | multiple drivers |

## KPI and materiality

| KPI | Comparator | Eligible/quality | Known result | Closing evidence |
|---|---|---|---|---|
| In-stock and waste/markdown per store-SKU | randomized/matched prior model | exposed SKUs; price/promotion/weather controlled | aggregate claims only | versioned store cohort |
| Contribution per incremental ad/search conversion | holdout/no exposure | eligible audience; returns/cannibalization/fees included | unknown | clean holdout and P&L bridge |
| Units/orders per paid labor hour | same facility before tool | adopted lines/sites; safety, quality and capex constant | unknown | matched rollout and cash proof |

The 5% convention is **about $987.5m annual pre-tax (5% of implied $19.75bn GAAP operating income)**. Illustration: **assumed $15bn eligible SG&A/supply cost × 10% efficiency × 60% realization × 40% retention − $250m = $110m**. All cost-pool, efficiency, realization, retention and run-cost inputs are assumptions. It does not count consumer savings or supplier benefit. A revenue mechanism must deduct cannibalization, discounts, ad/serving cost and incremental inventory/capex.

Positive: dense daily feedback plus distribution/execution makes small improvements scalable. Negative: data is shared, retailers/suppliers/platforms capture gains, and ordinary productivity or price actions explain results.

Falsifiers: controlled store/SKU cohorts show no gross-profit lift; AI media/search adds no incremental contribution after holdout; automation savings fail after capex/depreciation and quality. Confidence mechanism **medium-high**, deployment **medium**, capture **low-medium**. G0/G1 provisional; G2 incomplete without controlled incremental cash. G3/G4 deferred. Original prior preserved (77 P&G; 90 Walmart).

## Sources and handoff

Opened 12 Sep 2026: [Microsoft P&G customer story](https://www.microsoft.com/en/customers/story/25077-procter-and-gamble-iot-operations) (21 Aug 2025, supplier-reported named deployment and model-deployment-time claim); [latest results](https://us.pg.com/newsroom/news-releases/PG-Announces-Fourth-Quarter-and-Fiscal-Year-2026-Results/); [annual report](https://s204.q4cdn.com/332108499/files/doc_financials/2026/ar/2026_annual_report.pdf); [privacy](https://privacypolicy.pg.com/); [Unilever annual report](https://www.unilever.com/investors/annual-report-and-accounts/) (challenger); [Nielsen data policy](https://www.nielsen.com/legal/privacy-principles/) (syndicated-data boundary); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [FTC AI guidance](https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check) (claims/adverse); [company investor hub](https://www.pginvestor.com/). Controlled cohorts and commercial contracts unavailable.

Handoff [c089.json](../capsules/c089.json). Verify operating-profit denominator, data allocation and versioned store/product economics. Research-only; G2 incomplete.

A rigorous study must pre-register stores/SKUs/categories, season, price, promotions, weather and supply constraints; preserve holdouts long enough for repeat purchase, returns and waste; and include labor, cloud, robotics, inventory and depreciation. Marketing experiments should report incremental contribution rather than attributed sales. Aggregate productivity programs combine simplification, sourcing, automation and restructuring, so they cannot establish AI E4.

The measurement contract also needs explicit denominator reconciliation. “Eligible” should mean transactions or tasks on which the versioned system actually made a decision, excluding outages, missing data, mandated assortments and manual overrides. Report adoption, override, false-positive and exception rates. Inventory benefit should reconcile beginning inventory plus purchases less cost of sales, write-downs and ending inventory; otherwise timing can masquerade as productivity. Labor benefit should reconcile paid hours, wage rate, severance, overtime and contractor substitution. Revenue lift needs an incrementality holdout and contribution after product cost, returns, promotion, delivery and retail-media expense. Where a consumer brand buys retailer data or media, the retailer may capture most surplus. Where a retailer uses supplier allowances, accounting classification may shift gross margin without operational gain. Generative content must pass legal substantiation, brand-safety, copyright and demographic-bias review. A faster draft that adds review burden has no quality-adjusted output. Supplier concentration and tariff changes can also alter availability and margin independently. These controls should be reported for at least two seasonal cycles, because promotional calendars and holidays create spillovers. Absent this evidence, feature availability and employee-use counts stay below E3, and an enterprise productivity target stays outside the AI evidence ladder.

That remains decision material.
