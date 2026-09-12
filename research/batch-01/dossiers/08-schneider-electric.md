# Schneider Electric (C060) — initial evidence dossier

**Status:** unreviewed agent work; lead-review required. **Evidence cutoff / access date:** 12 September 2026. **Issuer/security:** Schneider Electric SE ordinary shares, Euronext Paris ticker **SU**, ISIN FR0000121972; quote and reporting currency EUR. **Industry:** D01 industrial automation and electrification.

## Provisional conclusion

Schneider has AVEVA recurring software, broad installed distribution and strong cash generation. Its clearest named AI deployment is a 20 kW green-hydrogen system reportedly run for more than 6,000 hours with levelized cost reduced by up to 10%. This remains vendor/customer-reported evidence without a disclosed counterfactual, uncertainty or implementation-cost bridge. Industrial Copilot’s “up to 50%” engineering-time saving is also self-reported. Evidence reaches **E2**, not E3/E4.

The current earnings acceleration is led by AI and cloud **data-center infrastructure demand**—power distribution, prefabricated systems, cooling and UPS—not demonstrated AI productivity inside Schneider or its customers. Data centers were about 30% of FY2025 orders, and H1 2026 data-center demand rose triple digits. This is a strong demand exposure, but it makes the stock more dependent on hyperscaler capex and raises the risk of attributing conventional volume/operating leverage to the incumbent-productivity thesis.

At the last completed official close available before cutoff, €287.40 on 10 September 2026, the shares were about 29.3x an explicitly illustrative €9.80 normalized FY2026 adjusted EPS. A five-year model requires 12.5% annual EPS/dividend growth at a 9% hurdle and 23x exit multiple. **Provisional disposition: watch; G2 passes narrowly, G3 is usable but does not qualify at this price on the initial model.**

## Conventional business and financial resilience

Energy Management supplies electrical distribution, secure power, cooling, building and grid technologies. Industrial Automation includes controls and AVEVA software. Products, Systems, and Software & Services sell through direct teams, integrators, panel builders and contractors. Products are cyclical; systems create backlog but require working capital; subscriptions and field service add recurrence.

The 2025 [full-year results presentation](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf?p_File_Name=2025+Full+Year+Presentation&p_enDocType=EDMS) (26 February 2026; FY ended 31 December 2025) and [2025 Universal Registration Document](https://www.se.com/ww/en/download/document/2025-URD/) (27 March 2026) support the baseline.

| €bn except per-share | FY2025 | FY2024 | Comment |
|---|---:|---:|---|
| Revenue | 40.152 | 38.153 | +8.9% organic |
| Adjusted EBITA / margin | 7.520 / 18.7% | 7.083 / 18.6% | +12.3% organic EBITA; non-IFRS measure |
| EBIT | 6.699 | 6.449 | After restructuring and PPA amortization |
| Net income, group share | 4.163 | 4.269 | -2%, including €0.388bn associate impairment |
| Adjusted net income / EPS | 4.829 / €8.59 | 4.664 / €8.32 | Adjusted denominator; reported diluted EPS not captured in opened extracts |
| Operating cash flow | 6.748 | 6.308 | Before working-capital movements in company bridge |
| Net capex | 1.496 | 1.364 | FCF bridge input |
| Free cash flow | 4.635 | 4.216 | After €0.617bn total working-capital outflow |
| Net debt / adjusted EBITDA | 13.721 / 1.60x | 8.147 / 1.00x | Increase includes €5.5bn SEIPL minority purchase |
| Dividend per share | €4.20 | €3.90 | FY2025 dividend paid May 2026 |

The 2025 gross margin fell 50bp reported to 42.1% as price/raw materials/tariffs, lower-margin Systems mix and investment offset volume. AI infrastructure can raise revenue while pressuring mix. Industrial Automation adjusted EBITA margin was 14.2% versus Energy Management’s 21.8%. AVEVA ARR grew 12%; the €25bn “digital flywheel” includes connected products and services, not pure software or AI.

Latest [H1 2026 results](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026) (30 July 2026; period ended 30 June) showed revenue €21.226bn (+14% organic), adjusted EBITA €4.093bn/19.3%, net income €2.488bn, adjusted EPS €4.79 and FCF €1.631bn. H1 FCF benefited from comparison with a €207m French fine in 2025, though operating cash flow rose €811m. Net debt rose to €15.36bn after €2.41bn dividends and buybacks. Management raised FY2026 organic adjusted-EBITA growth guidance to 14–19%, combining 10–13% revenue growth and 70–100bp margin expansion. It also agreed to pay $3.1bn for Cognite and $350m enterprise value for about 90% of AiDASH, both pending at H1, adding execution/debt risk.

A 9 September 2026 [Schneider announcement reported by Reuters](https://www.reuters.com/business/schneider-electric-invest-150-million-france-close-plant-2026-09-09/) described €150m French investment and a planned plant closure affecting 145 positions amid pricing pressure. This is adverse/real-world evidence that conventional footprint restructuring, not disclosed AI savings, drives part of internal productivity.

## Scarce asset and data-rights audit

| Input | Origin / owner | Exclusivity | Retrieval / inference | Training / pooled learning | Labels / quality | Replication threat |
|---|---|---|---|---|---|---|
| AVEVA PI/MES/engineering data models | AVEVA software/IP; operating data generally customer-owned | Schema/workflow IP proprietary; customer facts not exclusive | Contract-specific ingestion, contextualization and analytics are core products | Terms granting Schneider cross-customer training were **not found; unknown** | Dense time series and MES events; outages, maintenance and process changes create confounding | Siemens, AspenTech, Honeywell, Cognite independently, cloud data platforms |
| EcoStruxure connected-device telemetry | Customer assets through Schneider devices/edge/cloud | Installed access and device semantics are differentiated | Product functionality supports monitoring/inference | Retention, portability and pooled-learning rights **unknown** | Electrical/thermal state is frequent; causal failure labels sparse | Eaton, Siemens, ABB, independent DCIM/energy vendors |
| Automation logic, engineering documents and simulation | Customer projects plus Schneider EcoStruxure Automation Expert IP | Platform/IP proprietary; project artifacts customer-controlled | Copilot generates/configures within workflow | Azure/model and Schneider improvement rights **unknown** | Compilation/simulation/commissioning can validate; safety needs humans | Siemens TIA, Rockwell, Codesys/open automation; generic agents |
| Cognite knowledge graph / Atlas AI | To be acquired; customer enterprise/operational data federated | Software/IP proprietary; source data remains customer-specific | Contextualization is explicit product capability | Acquisition does not establish ownership or pooled rights; unknown | Knowledge graph improves context, not necessarily counterfactual labels | Customers can buy Cognite/competitors; closing/integration pending |
| Installed channel and field service | Schneider products, partners, service relationships | Durable distribution, not exclusive | Enables commissioning, maintenance and software attach | Not itself a training permission | Field-work outcomes may be observable but reuse rights unknown | Multi-vendor facilities and integrators reduce lock-in |

No opened license established ownership, retention, training or cross-customer learning rights. Schneider’s “data federation” describes architecture, not legal permission. Automation Expert’s portability can lower switching costs. The moat is **customer-specific context plus installed execution rights**; pooled learning is unproved.

## Mechanisms, deployment and challenger comparison

**1. Industrial Copilot and agentic engineering (generative/agentic).** EcoStruxure Automation Expert supplies reusable control logic, simulation, validation and edge execution; Azure supplies cloud/model orchestration. Schneider’s [16 April 2026 announcement](https://www.se.com/ww/en/about-us/newsroom/news/press-releases/Schneider-Electric-unveils-next-generation-agentic-manufacturing-capabilities-powered-by-Microsoft-Azure-AI-at-Hannover-Messe-2026-69e08de2ddabef15890a48f3/) says engineering teams report up to 50% time savings and changes once taking weeks take hours. It also calls some co-innovation demonstrations early-stage. Deployment is E2 for identified users/projects, but the absence of cohort, baseline definition, accepted-output/defect rate and cost prevents E3. Economics could be incremental software subscription/attach or service capacity, less Azure inference, integration, validation and cannibalization.

**2. Autonomous process control / predictive maintenance (classical ML, optimization and AI execution).** The [h2e Power case](https://www.se.com/in/en/about-us/newsroom/news/press-releases/Schneider-Electric-demonstrates-how-AI%E2%80%91powered-open-software%E2%80%91defined-automation-transforms-green-hydrogen-and-complex-industries-with-Microsoft-69e06a0d3e2258a29904a8f8/) reports more than 6,000 hours stable operation on a 20 kW solid-oxide electrolyser, predictive maintenance and up to 10% lower levelized hydrogen cost. It extrapolates €500,000 annual savings to a typical 10 MW plant, 500 times the demonstrated unit’s capacity. There is no disclosed control system, pre-period, confidence interval, allocation between AI/control/hardware or commercial invoice. It is valuable E2 and a route to E3, not E3 itself.

**3. Industrial data/energy optimization (established software plus incremental AI).** AVEVA contextualizes PI/MES data and EcoStruxure advisors monitor energy and condition. An [AVEVA/Braincube Maple Leaf case](https://www.aveva.com/en/perspectives/blog/data-driven-strategies-to-reduce-industrial-material-waste/) reports a 10–12% plant gross-profit boost within three months, but Braincube performed AI analytics and the item is vendor-published; baseline and attribution are unclear. A much older [Henkel AVEVA case](https://www.aveva.com/en/perspectives/success-stories/henkel/) reports €8m annual energy savings, demonstrating conventional MES value already in the baseline rather than incremental GenAI.

Siemens’ TIA Portal/Xcelerator agents cover the same engineering tasks. ABB, Rockwell/Honeywell and AspenTech compete in controls; Cognite and Braincube show that customers can pair AVEVA with third-party analytics. Schneider’s open architecture expands its addressable base but weakens lock-in. Differentiation lies in power, cooling and automation context at the edge, not Azure AI access.

## Evidence ledger

| Claim | Type | Source/date; section | Scope / stage | Confounder |
|---|---|---|---|---|
| FY2025 revenue €40.152bn, adjusted EBITA €7.520bn, FCF €4.635bn | Fact | FY2025 presentation, 26 Feb 2026, pp. 32, 39, 43 | Financial baseline; ladder N/A | Adjusted EBITA/non-IFRS; FCF working capital |
| H1 2026 revenue +14% organic, adjusted EBITA +22.1% organic | Fact | H1 release, 30 Jul 2026, pp. 1, 8 | Latest group results; ladder N/A | Data-center volume, price, mix, FX |
| Data centers about 30% FY2025 orders and triple-digit H1 demand | Management fact | FY2025 presentation p.13; H1 release pp.2–4 | AI-infrastructure demand | Not own/customer productivity |
| AVEVA ARR +11% at June 2026 | Management fact | H1 release, software section | Paid recurring channel | AI contribution/NRR not isolated |
| Industrial Copilot saves up to 50% engineering time | Management/customer claim | Schneider, 16 Apr 2026 | Deployed tasks; E2 | Self-selected teams, no quality/cost comparator |
| h2e system ran >6,000 hours and LCOH fell up to 10% | Joint vendor/customer claim | Schneider India, 16 Apr 2026 | One 20 kW deployment; E2 | Hardware/control/AI attribution; extrapolation |
| Cognite $3.1bn and AiDASH $350m deals pending | Fact | H1 release, portfolio updates | Capital allocation | Closing, integration, acquired growth |
| Pooled industrial-data rights | Research gap | No opened contract | E0 | Architecture/possession is not permission |
| €287.40 official close | Fact | [Euronext](https://live.euronext.com/fr/product/equities/FR0000121972-XPAR), 10 Sep 2026 | Ordinary share, last full close before cutoff | 11 Sep page was intraday at retrieval |

## KPI contract and retained economics

Minimum materiality threshold: a credible path to **€0.376bn net annual benefit**, 5% of FY2025 adjusted EBITA. This is an analyst convention.

| KPI | Baseline/comparator | Eligible workload | Quality constraint | Known result | Review event |
|---|---|---|---|---|---|
| Accepted engineering hours/change | Matched teams/projects using current Automation Expert | Copilot-eligible configurations/docs | Same defects, safety tests, uptime and commissioning rework | Up to 50%, no distribution/baseline | FY2026 results or named renewal cohort |
| Energy/LCOH per good unit | Pre-rollout or randomized/matched assets | Similar loads/process conditions | Output purity, stack wear, safety, availability | Up to 10% at one h2e deployment; uncertainty unknown | 10 MW commercial cohort/12-month audit |
| AI/digital ARR, attach, NRR and gross margin | AVEVA/EcoStruxure baseline excluding acquired Cognite | Eligible installed accounts | After cloud, inference, support and implementation | AVEVA ARR +11%; AI slice unknown | FY2026 annual report/CMD |
| Internal realized cost | Pre-program functions/plants | Tasks actually redesigned | Service level, revenue and working capital | “Productivity” positive but AI share unknown | Program savings reconciliation |

Illustrative **internal-cost** bridge: `€3.0bn eligible Schneider cost ×20% efficiency ×60% realization ×50% retained − €0.12bn recurring AI cost = €0.06bn`, under 1% of adjusted EBITA. At those assumptions, reaching €0.376bn needs **€8.27bn eligible cost** (`(0.376+0.12)/(0.20×0.60×0.50)`). Customer gains require a separate revenue bridge: incremental AI ARR × contribution margin, less seat/service cannibalization and implementation/model cost. None of those inputs is disclosed, so the 5% route is plausible via scale but unproved.

## Valuation and reverse valuation

Price €287.40 (official Euronext close, 10 September 2026). FY2025 diluted average shares are approximated at 570.5m from the published €4.588bn FCF / €8.04 per-share reconciliation; reviewer should replace this derived denominator with the audited exact share note. Implied equity value is about €164.0bn and enterprise value about €179.4bn using 30 June net debt €15.36bn, before the $3.45bn announced Cognite/AiDASH purchase consideration. Because reported diluted EPS was not captured in the opened extracts, valuation uses adjusted EPS and labels it.

Starting adjusted EPS is an illustrative **€9.80**, close to annualized H1 €4.79 and above FY2025 €8.59; it is not company guidance. Python-reproduced formula: five dividends starting at €4.20 grow with EPS, plus `€9.80×(1+g)^5×exit P/E/(1+r)^5`.

| Case | Five-year EPS growth | AI / conventional treatment | Exit P/E / hurdle | PV dividends + terminal | Value/share |
|---|---:|---|---|---:|---:|
| Bear | 2% | No AI uplift; data-center cycle/mix normalization | 18x / 10% | €16.8 + €120.9 | **€138** |
| Base | 7% | Current digital execution, no separately credited AI | 23x / 9% | €19.9 + €205.5 | **€225** |
| Bull | 10% | Sustained data-center growth plus paid AI attach | 28x / 8% | €22.2 + €300.8 | **€323** |

At €287.40, 9% hurdle and 23x exit multiple, the model requires **12.52% annual EPS/dividend growth for five years**. That exceeds Schneider’s 2025–30 organic revenue target of 7–10% but could be reached temporarily through margin expansion/buybacks; it also assumes the premium exit multiple persists. Base value moves by about €17.9 per two turns of exit P/E (21x roughly €207; 25x roughly €243). The stock prices significant conventional data-center and margin success before giving credit to unmeasured incumbent productivity.

## Risks, falsifiers, priors and gates

Strongest positive hypothesis: Schneider combines electrical/thermal installed context, AVEVA operational data, open automation and field execution, monetizing optimization through subscriptions, services and hardware pull-through. Strongest counterargument: common Azure models and portable/open automation make the AI layer contestable; customer-owned data block pooled learning; direct AI-capex demand and operating leverage explain reported earnings without any AI productivity moat.

Core risks are hyperscaler-capex concentration, Systems mix/working capital, tariffs/materials, China/buildings cycles, AVEVA/Cognite integration, higher debt, convertible dilution and restructuring. Negative evidence includes FY2025 gross-margin pressure, Industrial Automation’s 14.2% margin, the €207m legal fine, a current French plant closure, and the need to buy rather than organically demonstrate Cognite/AiDASH capabilities.

Falsifiers: (1) no disclosed paid AI attach/retention and gross-margin cohort by FY2027; (2) controlled 10 MW-scale or multi-plant studies fail to reproduce h2e/engineering gains after safety, implementation and energy/load controls; (3) data-center orders or backlog reverse while the stock still requires double-digit EPS growth. AI-capture failure is distinct from a core failure such as adjusted EBITA margins falling below 18% through a normal demand year.

| Dimension | Original prior | Proposed revision | Reason |
|---|---:|---:|---|
| Scarce asset | 4 | 4 | Strong installed/software context; customer data ownership limits exclusivity |
| AI leverage | 4 | 4 | Engineering, energy and maintenance are core tasks |
| Feedback | 4 | 2 | Pooled-learning rights and incremental predictive loop unknown |
| Testability | 4 | 4 | Hours, energy, downtime and defects measurable; current studies weak |
| Distribution | 5 | 5 | Global product/channel base and AVEVA ARR |
| Capture | 4 | 3 | Paid channels exist; AI contribution and margin not isolated |

Python-checked revised structural score: **73/100**; capture-30%/feedback-5% sensitivity **75/100**, versus 83 prior. **G0 pass. G1 pass with debt/acquisition monitoring. G2 narrow pass** on E2 named deployment and a feasible measurement/materiality route. **G3 assessed but not qualified**: security/price/share bridge is usable with disclosed denominator limitation, while initial price-implied growth is demanding. **G4 not assessed.** Confidence: mechanism moderate-high; deployment moderate; capture low; valuation moderate.

Peer/inaction alternative: Siemens has deeper controller/engineering integration but a complicated Healthineers perimeter; Eaton offers more direct electrification exposure; ABB/Rockwell offer automation comparators. Waiting for a data-center normalization test and paid AI economics is preferable to underwriting the productivity thesis at the current implied growth rate.

## Source register and reviewer handoff

1. Schneider Electric, *FY2025 Results Presentation*, 26 Feb 2026, accessed 12 Sep 2026, pp. 6–8, 31–59. Primary financial/strategy source; adjusted measures.
2. Schneider Electric, *2025 Universal Registration Document*, 27 Mar 2026, accessed 12 Sep 2026. Audited filing landing/download; large PDF limited extraction.
3. Schneider Electric, *H1 2026 Results*, 30 Jul 2026, accessed 12 Sep 2026, pp. 1–23. Latest reviewed interim results.
4. Schneider Electric, *Next-generation agentic manufacturing*, 16 Apr 2026, accessed 12 Sep 2026. Product/deployment claims; no control.
5. Schneider Electric India, *AI-powered autonomous green hydrogen with h2e*, 16 Apr 2026, accessed 12 Sep 2026. Named customer/project; scale extrapolation.
6. AVEVA, *Maple Leaf data-driven waste reduction*, 2025 (page date not shown in opened result), accessed 12 Sep 2026. Vendor case; third-party Braincube confounder.
7. AVEVA, *Henkel success story*, undated/legacy deployment, accessed 12 Sep 2026. Conventional MES baseline, not GenAI proof.
8. Euronext, *Schneider Electric FR0000121972*, 10–11 Sep 2026, accessed 12 Sep 2026. Primary venue price; 11 Sep only intraday at retrieval.
9. Reuters, *Schneider to invest €150m in France, close plant*, 9 Sep 2026, accessed 12 Sep 2026. Current adverse development; secondary reporting.
10. Siemens, *Industrial AI agents*, 12 May 2025, accessed 12 Sep 2026. Incumbent challenger; target rather than controlled result.

**Three decisive claims to verify:** (i) audited FY2025 diluted shares/reported diluted EPS and exact 10 September market-cap bridge; (ii) h2e’s 10% LCOH methodology, comparator and whether €500k is observed or solely 10 MW extrapolation; (iii) AVEVA/EcoStruxure/Cognite contractual rights for training and pooled cross-customer learning. **Strongest counterargument:** direct data-center demand and planned 250bp margin expansion can justify earnings growth even if the productivity moat fails. **Blocking questions:** AI-specific ARR/NRR/gross margin, controlled scaled outcomes, and post-deal leverage. **Provisional disposition:** watch; good business, narrow G2, price not qualified in initial G3. **File written:** `research/batch-01/dossiers/08-schneider-electric.md`.
