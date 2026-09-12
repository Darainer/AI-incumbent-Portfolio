# Ranking and valuation — 12 September 2026

Status: complete for100 operating ranks and25 valued candidates (75 scenarios). This directory supersedes the evidence-phase deferral for the new ranking and cases only; original research remains preserved.

The user has authorized explicit ranking and base/bull cases, with the highest available model quality. The lead makes the final judgments. Independent challenges and bounded valuation work use GPT-6 Astra with extra-high reasoning; no lower-tier model is used for this phase.

## Decision structure

1. Review all 100 companies and order their suitability for the AI incumbent productivity regime. This is a price-independent, evidence-informed underwriting order, not an entry recommendation. Do not disguise missing valuation work as a current-price investment ranking.
2. Build dated, five-year base and bull cases for approximately 20–25 leading or decision-relevant candidates. Include a downside case because a bull/base comparison alone cannot establish margin of safety. Preserve weak or unattractive results; selection for valuation does not imply a favorable conclusion.
3. Rank the valued candidates by conventional-business resilience, achievable owner return, downside exposure and confidence in retained incremental AI economics. Explain why the ordering differs from a mechanical sort by projected return.

## Rules for scenarios

- Use a verified latest available price with listing, currency and timestamp. A quote after the market close is not relabeled the official closing price. If an exact cutoff price is unavailable, disclose the actual date; exclude incompatible observations from strict cross-sectional return comparisons.
- Use annual normalized earnings, conservative owner cash or sector-appropriate equity earnings. Keep reported financial inputs separate from analyst normalization and scenario assumptions. Do not use market-feed headline P/E as the earnings model.
- For an equity earnings model, debt and interest are already reflected in net earnings: do not subtract debt a second time. Assess leverage and cash conversion separately. For an enterprise-value model, explicitly reconcile debt, cash, leases and other claims.
- Forecast ordinary-business growth separately from incremental AI. Existing ML, deployed automation and AI already embedded in reported earnings belong in the baseline. No assumed clinical-success uplift enters a pharma base case without evidence. Do not count the same pipeline candidate in both baseline growth and AI optionality.
- Treat stock compensation as an economic cost. Do not use unadjusted FCF that adds it back while assuming costless share-count stability. Per-share growth may include a stated net-buyback assumption; do not add buyback yield again to returns.
- Deduct recurring AI costs and share gains with customers/workers/vendors before assigning incremental terminal earnings. Reflect investment and capital intensity through conservative earnings/cash normalization and justified terminal multiples. A speculative AI uplift cannot fix an impaired conventional case.
- Assumptions are conditional underwriting judgments, not consensus forecasts or probability estimates. Base and bull are not guaranteed outcomes. Do not assign probability-weighted expected returns without a defensible probability model.

## Reproducible equity scenario

For the common five-year earnings model (TRI uses an equity owner-cash multiple):

`ordinary earnings/share in year 5 = normalized annual earnings/share × (1 + ordinary per-share growth)^5`

`total earnings/share in year 5 = ordinary earnings/share × (1 + incremental retained AI uplift in year 5)`

`terminal share value = total year-5 earnings/share × terminal multiple`

Exception: when a supplied forecast already represents year1 (Intuit and Salesforce), use `year1 earnings × (1+growth)^4` for year5, while retaining a five-year holding period. Do not compound a forward annual estimate through an extra year. The script records the number of growth periods explicitly.

Use annual dividends as separate cash flows and solve the investor IRR from the observed share price. Dividends are not assumed reinvested at the terminal price. An entry threshold discounts those same dated cash flows at a 10% nominal annual return hurdle; show 8% and 12% sensitivity. The 10% hurdle is an explicit research convention, not a user-provided required return. Local-currency returns exclude investor tax, fees and EUR exchange-rate effects. No position sizing or trading is authorized by this analysis.

## Interpretation of evidence

G2 requires E2 and a credible route to controlled evidence and material retained economics; it does not require E4 already. A strong conventional stock with unproved AI can be attractive on conventional value, but must not be labeled a proven regime beneficiary. Source-review PASS is not an investment pass. Materiality illustrations in the earlier packets are not valuation inputs unless normalized and independently justified.

## Completed outputs

- [Final lead judgment](lead-decision.md): the decision, top priorities, case assumptions and limits.
- [100-company operating ranking](universe-ranking.md): price-independent fit with the regime.
- [25-company investment ranking](investment-ranking.md): lead ordering at dated prices, with conditional statuses.
- [75-scenario comparison](scenario-table.md) and [sensitivities](sensitivity.md).
- [Machine-readable cases](valued-candidates.json), [lead judgments](lead-judgments.json), [reproduction script](../../scripts/value_ranked_candidates.py) and [validation](validation.json).
- Agent inputs and source bridges: [Europe](valuation-europe.md), [health/insurance](valuation-health.md), [platforms](platform-normalization.md), [other normalization](normalization-other.json), [lead cases](valuation-lead.json) and [independent challenge](independent-challenge.md).

The lead-reviewed cases and results supersede preliminary agent scenario outputs. Lead changes include zero separate base AI premium, more demanding platform downside assumptions, dividend-timed IRR rather than terminal-wealth CAGR, corrected forward-year timing, an evidence-backed TRI SBC deduction and AZN after-hours quote sensitivity. Raw agent packets remain available for traceability.

The other75 companies have completed evidence reviews and operating ranks but no current-price case in this release. LSEG retains an approximate diluted-earnings bridge. Platforms/marketplaces require capital recovery; pharma cases use analyst replacement-cost reserves. None of these conditions is resolved by arithmetic validation. No probabilities, trades, portfolio weights or automatic G3 promotion are implied.
