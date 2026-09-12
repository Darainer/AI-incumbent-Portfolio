# C079 — Inditex evidence dossier

**Unreviewed agent work.** Inditex; ITX (BME, EUR quote/reporting). Cutoff/retrieval 12 September 2026. Latest period: H1 FY2026 ended 31 July, released 9 September 2026.

## Business and financial anchor

Inditex operates a high-frequency consumer platform. Its scarce asset hypothesis is RFID-linked inventory, daily store/online demand, vertically coordinated design/sourcing and premium store network. The AI mechanism is to forecast demand, allocate inventory and assist design/content so more full-price sales occur with less markdown and working capital. Existing optimization and recommender systems are already embedded in reported economics and belong in the ordinary baseline; only incremental, versioned improvement qualifies.

Latest results reported **€19.755bn sales**, **€2.980bn net income; €5.513bn EBITDA**, and **€2.299bn free cash flow and roughly €11bn net cash**. FY2025 annual report published 11 March 2026; sales about €39.9bn and operating margin 20.1%. Sources: [latest results](https://www.inditex.com/itxcomweb/en/press/press-releases) and [annual report/filing](https://static.inditex.com/annual_report_2025/en/). Reported, adjusted and free-cash-flow definitions differ. Mix, currency, acquisitions/disposals, incentives, store/fleet footprint, tax and working capital can move results without AI. fashion causality is hard: merchandising, weather, FX, store optimization and lead-time decisions dominate; Shein has faster digital feedback and price pressure.

The conventional business remains viable through brand/network liquidity, distribution, scale purchasing/marketplace density and operational execution. Capital allocation must fund technology and physical/logistics needs; net cash/FCF does not make every growth investment productive.

## Data-rights audit

| Input | Owner/exclusivity | Permitted inference/training | Labels/quality | Replication threat |
|---|---|---|---|---|
| Customer transactions/search/location | Customer/platform under privacy and contract | Service/personalization purpose; consent, retention and cross-context limits apply | Frequent purchase/completion labels; intent and counterfactual missing | customers multi-home; ad/commerce platforms see behavior |
| Supply/inventory/provider availability | Platform and suppliers/providers | Operational optimization; partner data use limited by contract | Real-time availability, cancellations and fulfillment observable | suppliers/providers use rival platforms and own systems |
| Prices/promotions/incentives | Platform decision plus market response | Internal experimentation plausible; regulation/fairness constraints | Rapid elasticity labels, non-stationary and strategic | competitors scrape/observe public prices |
| Customer-specific content/payment | Customer/merchant/payment partner | Transaction execution only for authorized purpose; pooling not universal | High relevance, sensitive and regulated | processors/merchants/models control adjacent interface |

A privacy policy establishes governance, not exclusivity. Cross-user or cross-merchant learning must have lawful purpose and contract support. Location, biometrics and worker decisions create special regulatory risk. Supplier-provided catalog/design data cannot be assumed available for generative training.

## Mechanisms and challenge

1. **Forecasting/matching/allocation (classical ML).** Demand and supply state → choose inventory/dispatch/offer → completed transaction with lower wait/markdown/cancellation → contribution and working-capital gain. It is deeply deployed (E2), but consolidated growth does not isolate a new model's causal effect.
2. **Personalization/generative interface.** Context → rank or generate product/trip/support response → accepted outcome at equal returns/safety/satisfaction → higher conversion or lower service cost. Availability is E1/E2; controlled retained economics are undisclosed.
3. **Agentic execution.** An agent can reorder/rebalance/resolve or, for mobility, coordinate autonomous supply. This may expand transactions, but authorization, errors and partner capture matter. Announcements/pilots are E1; scaled paid use is required for E2.

Direct challengers are **H&M and Shein**. Generic models, commerce/search interfaces and supplier-owned apps are substitutes. The platform does not automatically own the customer relationship when an agent initiates a purchase/ride. Price transparency and multi-homing pass gains to users/providers; model/payment/AV suppliers can take fees.

| Claim | Type/source | Stage | Confounder |
|---|---|---|---|
| Latest financial figures above | Company fact | Financial | mix/currency/incentives |
| Core optimization is deployed | Company product/filing fact | E2 | already in baseline |
| Generative/agentic features exist | Company claim | E1/E2 narrow | adoption and error unknown |
| Transaction data creates rapid feedback | Inference from platform operation | E0 mechanism | outcomes not causal labels |
| Customer/partner data rights are bounded | Privacy/contract fact/inference | Rights | contracts unavailable |
| Rival has comparable digital feedback | Rival filing/product fact | Challenger | quality not directly compared |
| fashion causality is hard: merchandising, weather, FX, store optimization and lead-time decisions dominate; Shein has faster digital feedback and price pressure | Filing/external fact and inference | Adverse | multiple drivers |

## KPI and materiality

| KPI | Baseline/comparator | Eligible/quality | Known result | Closing evidence |
|---|---|---|---|---|
| Contribution per eligible transaction | randomized prior model/policy | exposed transactions; returns, cancellations, safety/fraud controlled | unknown | versioned experiment and P&L bridge |
| Forecast error/availability or ETA | same category/market/season | eligible SKUs/trips; service quality constant | selected operational claims only | matched cohort |
| Support cost per quality-adjusted resolution | current workflow | adopted cases; reopen/escalation/satisfaction non-inferior | unknown | controlled rollout and removed-cost proof |

No clean H1 operating-profit figure was opened; using H1 EBITDA only as a scale proxy, 5% is €275.7m for the half year and is not annualized. Illustration: **assumed €10bn eligible inventory purchases × 1% markdown/obsolescence improvement × 60% realization × 50% retention − €30m cost = €0m**. Every cost-pool/efficiency/realization/retention/run-cost input is assumed. Customer savings are not company cost; released capacity cannot be counted again as added revenue. Existing ML expense and benefit remain in baseline.

Positive: frequent transactions, direct experimentation and execution rights make improvement testable and scalable. Negative: data is shared/nonexclusive, interfaces shift to agents, competitors imitate, and counterparties capture the benefit.

Falsifiers: versioned tests show no contribution lift after quality; repeat/retention fails to improve; supplier/regulatory/model costs exceed gains or bypass grows. Confidence mechanism **high**, deployment **medium-high for classical ML and low for incremental agentic**, capture **low-medium**. G0/G1 provisional; G2 incomplete because current incremental E3/E4 evidence is absent. G3/G4 deferred. Original prior preserved (83 Inditex; 91 Uber).

## Sources and handoff

Opened 12 Sep 2026: [latest results](https://www.inditex.com/itxcomweb/en/press/press-releases); [annual report/filing](https://static.inditex.com/annual_report_2025/en/); [privacy](https://www.inditex.com/itxcomweb/en/privacy); [H&M annual reports](https://hmgroup.com/investors/reports/) (challenger); [Shein privacy](https://www.sheingroup.com/privacy-policy/) (entrant/substitute); [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) (rights/governance); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) (quality); [company investor hub](https://www.inditex.com/itxcomweb/en/investors) (reports). Detailed contracts and controlled cohorts unavailable.

Handoff [c079.json](../capsules/c079.json). Verify latest financial definitions, cross-party rights and a versioned contribution cohort. Research-only; G2 incomplete.

Testing must hold geography, season, customer mix, price and supply constant. For allocation, measure sell-through, markdown, stockouts, transfers and returns together; a lower forecast error can still reduce gross margin. For mobility, compare wait, cancellations, safety, driver/courier earnings, incentives and contribution. Autonomous trips require separate partner economics and capital/liability treatment. Aggregate margin cannot distinguish these channels.

Measurement also needs a legal/operational incident ledger. Record model version, jurisdiction, eligible transaction, human override, complaint, refund, fraud or safety event, and final economic disposition. An apparent conversion gain may arise from higher discounting or looser risk thresholds; a lower wait time may require higher provider incentives; better availability may reflect added inventory or supply. Each must be netted. Data drift is acute because fashion preferences, weather, events, road conditions, competitor promotions and regulation change quickly. Randomization should avoid spillovers where inventory or drivers serve both test and control. Rights review should identify controller/processor roles, purpose limitation, retention, deletion, portability and model-provider training status. Agentic interfaces add mandate and authentication questions: the platform needs evidence that the user authorized the transaction and that the agent presented price/alternatives faithfully. These conditions affect both quality and liability, so gross transactions cannot close the evidence gap. The next useful disclosure is a stable, versioned cohort with contribution, quality and retained cash, not another feature count.
