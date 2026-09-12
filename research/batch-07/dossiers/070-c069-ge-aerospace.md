# C069 — GE Aerospace evidence dossier

**Unreviewed agent work.** GE Aerospace; ordinary stock GE (NYSE, USD quote/reporting). Cutoff/retrieval 12 September 2026. Latest period: Q2 2026, published 16 July 2026.

## Business and financial anchor

GE Aerospace sells aircraft engines/equipment and long-duration aftermarket services. Installed engines create decades of shop visits, spare-parts demand and operational data, but original equipment may have lower economics to seed the service base. Defense, interiors/equipment and commercial engine exposures have different cycles. Certification, safety, engineering IP, repair networks and installed fleets are the conventional moat.

Latest results reported **$9.7bn segment revenue (GAAP total presentation differs)**, **$2.7bn segment profit**, and **$3.0bn company-defined free cash flow and $3.3bn GAAP operating cash flow**. FY2025 GAAP revenue $45.9bn, GAAP profit $10.0bn; adjusted operating profit $9.1bn. Sources: [latest results](https://www.geaerospace.com/news/press-releases/ge-aerospace-announces-second-quarter-2026-results) and [annual results/report](https://www.geaerospace.com/investor-relations/annual-report). Adjusted/recurring measures are non-IFRS/non-GAAP and differ from consolidated statutory presentation. Engine deliveries, aftermarket mix, pricing, FX, hedges, acquisitions and supply recovery confound margin. Service volume and price drove results, while casting bottlenecks led to a proposed $11.75bn CPP acquisition funded with cash/debt; supply execution dominates near-term economics.

The zero-additional-AI business has a large installed base/backlog and scarce certified repair capacity. Cash supports R&D and returns, but safety liabilities, program guarantees, working capital and acquisitions matter. AI cannot bypass physical inspection, material availability, FAA/EASA certification or fleet-grounding risk.

## Assets and rights

| Input | Owner/exclusivity | Permitted inference/training | Labels/quality | Replication threat |
|---|---|---|---|---|
| Engine sensor/flight data | airline/operator; manufacturer receives contracted streams | Fleet monitoring and support within agreement; cross-airline training/export rights undisclosed | High frequency but operating context and sensor changes matter | airline, airframer and rival engine maker see overlapping data |
| Shop-visit/part histories | service network, operator and OEM | Contract/warranty/service use; pooling terms vary | Failure/removal labels valuable but maintenance selection biased | MROs and partners observe repairs |
| Design/test/certification data | OEM and joint-venture partners | Internal engineering and program-specific JV rights; defense/export restrictions | Physically validated but costly/sparse failures | partner and regulators hold copies; simulation vendors generic |
| Maintenance manuals/IP | OEM/licensors | Controlled technical-data access; no unrestricted model training | Authoritative versions, configuration-specific | independent MRO manuals and airframer platforms |

Airline/customer and cfm/safran partner data creates mixed ownership. CFM data/economics are shared between GE and Safran. Possession does not prove permission to pool operator, defense or partner data. Model/cloud suppliers may receive only isolated context, and exact retention/training terms are not public.

## Mechanisms and competition

1. **Predictive maintenance (classical ML).** Sensor and removal history → estimate failure/remaining life → schedule inspections/parts → higher availability and fewer disruptions at equal safety → service retention, fewer warranty costs or outcome fees. Digital monitoring is in production (E2), but no current controlled fleet-level avoided-cost/cash result was located.
2. **Shop and supply optimization (classical ML/agentic execution).** Workscope, parts and routing data → sequence repairs/material → more engines returned per shop-day → service revenue/working-capital benefit. Company operating systems and analytics are deployed, but lean process, added labor/capacity and supply recovery are major confounders.
3. **Engineering assistance/digital twins (ML/generative assistance).** Design/test history plus simulation → prioritize designs and tests → certified performance with fewer iterations → lower R&D or faster program. E1 capability; certification and physical tests remain, and program cash is years away.

The incumbent challenger is **RTX/Pratt & Whitney and Rolls-Royce**. Airbus Skywise and independent MRO/analytics vendors are substitutes that can own the airline interface. Airlines can demand reliability guarantees or lower service prices; suppliers can capture scarce-parts economics. Outcome-based service contracts may allow OEM capture but also make prediction errors costly.

| Claim | Type/source | Stage | Confounder |
|---|---|---|---|
| Latest revenue/profit/FCF above | Company result fact | Financial | mix, price, delivery recovery |
| Fleet monitoring/analytics is available | OEM product fact | E1/E2 | no causal fleet comparator |
| Predictive maintenance can change scheduling | Mechanism inference | E0 until quantified | safety/human review |
| Digital-twin/design tools are used | Company/supplier claim | E1/E2 narrow | simulation and physical validation |
| Service growth drove profit | Results fact | Ordinary business | air traffic, price and installed base |
| Partner/customer data rights are contract-bound | Contract/legal inference | Rights | agreements inaccessible |
| Supply/certification bottlenecks persist | Filing/results fact | Adverse | cycle may improve |

## KPI and materiality

| KPI | Comparator | Eligible/quality | Known result | Closing evidence |
|---|---|---|---|---|
| Unscheduled removals per 1,000 flight hours | matched engine vintage/operator without new model | monitored fleet; safety events and deferred maintenance controlled | unknown | prospective fleet cohort |
| Shop turnaround days and first-time yield | same shop/workscope before tool | AI-routed visits; parts/labor/capex controlled | consolidated improvement only | shop-level matched rollout |
| Test cycles to certified milestone | prior comparable engine/module | tool-supported designs; certification and durability equal | unknown | program audit |

The 5% convention is **$455m annual pre-tax (5% of FY2025 adjusted operating profit)**. Illustration: assumed €/$2bn eligible shop/support cost × 15% task efficiency × 60% realization × 50% retention − €/$80m run cost = **€/$10m**, far below hurdle. A capacity route needs incremental shop visits × contribution after parts/labor/capex, without also counting labor savings. Customer delay savings are not OEM cost. No public disclosure supports a mechanism-level E4 bridge.

Positive: unique installed-fleet and repair labels improve availability and throughput, with long service contracts capturing part. Negative: rights are shared, physical/safety constraints dominate and customers/suppliers capture gains; favorable cycle explains margins.

Falsifiers: matched fleet removal rates do not improve; shop turnaround gains disappear after capacity/parts controls; outcome pricing/model cost produces no incremental service contribution. Confidence mechanism **medium-high**, deployment **medium**, capture **low-medium**. G0/G1 provisional pass; G2 incomplete without controlled quality/cash. G3/G4 deferred. Original prior 83 preserved.

## Sources and handoff

Opened 12 Sep 2026: [latest results](https://www.geaerospace.com/news/press-releases/ge-aerospace-announces-second-quarter-2026-results); [annual report/results](https://www.geaerospace.com/investor-relations/annual-report); [FAA predictive maintenance guidance](https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_43-218.pdf) (regulatory quality); [EASA AI roadmap](https://www.easa.europa.eu/en/domains/research-innovation/ai) (regulatory); [Airbus Skywise](https://aircraft.airbus.com/en/services/enhance/skywise) (substitute); [Rolls-Royce IntelligentEngine](https://www.rolls-royce.com/media/our-stories/discover/2018/intelligentengine.aspx) (challenger); [company privacy](https://www.geaerospace.com/privacy) (rights); [GE-Safran CFM](https://www.cfmaeroengines.com/about/) (joint-venture scope). Contract terms and controlled outcomes were unavailable.

Handoff [c069.json](../capsules/c069.json). Verify financial definitions, operator/JV data rights, and any fleet/shop matched outcome. Research-only; G2 incomplete.

A proper fleet comparison should stratify engine type, age, route, climate, operator practice and maintenance program, with enough time for rare safety events. Shop comparisons must include parts availability, overtime, added tooling and work-scope severity. Consolidated service growth cannot establish AI causality because traffic, pricing and fleet aging move simultaneously. These controls prevent ordinary aftermarket strength from being relabeled as AI productivity.

Rights diligence must inspect long-term service agreements, airline data-transfer schedules, CFM governance, defense technical-data clauses and cloud subprocessor terms. The economic denominator should distinguish manufacturer warranty cost from airline disruption cost and service revenue. Better prediction can defer a shop visit, reducing near-term OEM revenue, or bring it forward, raising revenue without creating lifetime value. Likewise, faster turnaround only creates profit when demand exceeds capacity and added output earns contribution after scarce parts and labor. Model false positives may create unnecessary removals; false negatives carry safety and warranty exposure. These asymmetric errors require calibration by engine family and operating environment. Cybersecurity also matters because maintenance recommendations and technical manuals affect safety-critical activity. Until disclosure connects a versioned model to an eligible fleet, quality outcomes and contract cash, evidence remains E2 at best. The next useful event is a customer-identified, multi-year fleet cohort or a shop rollout with pre-registered controls and reconciled economics.
