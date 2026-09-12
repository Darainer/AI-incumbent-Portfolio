# C045 — Cadence Design Systems evidence dossier

**Unreviewed agent work.** Cadence Design Systems; Nasdaq common stock CDNS, USD quote/reporting. Cutoff/retrieval 12 September 2026. Latest period: Q2 2026 ended 30 June, published 27 July 2026.

## Business and financial anchor

Cadence Design Systems sells electronic-design-automation software, verification hardware/software and semiconductor IP into chip and system design. Recurring time-based licenses, maintenance and IP royalties are supported by high switching cost, foundry certification and signoff risk. FY2025 Core EDA grew 13% and IP nearly 25%; annual filing is latest audited. The latest release reported revenue **$1.584bn** and **GAAP operating margin 28.4%**. The source is [Cadence Design Systems latest results](https://investor.cadence.com/news-releases/news-release-details/cadence-reports-second-quarter-2026-financial-results). Reported versus non-GAAP measures must stay separate; deferred revenue, backlog, acquisition accounting and hardware timing can move quarterly margins and cash.

Its scarce assets are decades of algorithms, foundry-qualified flows, reusable IP, installed customer workflows and design telemetry. Cerebrus and generative/agentic workflows search implementation choices and optimize power, performance and area. However, chip designs, PDKs and much IP belong to customers, foundries or licensors. Therefore technical access is not universal training permission. Conventional resilience depends on semiconductor R&D intensity and oligopoly, while export controls, customer consolidation and integration are key risks. China export controls and dependence on third-party IP/licenses constrain deployment; AI may reduce seats or shift value to compute vendors.

## Asset and rights audit

| Input | Owner/exclusivity | Permitted use/training | Quality | Replication threat |
|---|---|---|---|---|
| Customer chip designs, constraints and failures | Customer; vendor receives under license/confidentiality | Run contracted EDA and customer-specific optimization; cross-customer training is not established | High-value PPA/verification labels but each design/process differs | Customers can multi-tool; foundries see process-wide data |
| Tool telemetry and optimization trajectories | Mixed vendor/customer context | Product improvement scope depends on agreement; retention and pooling terms undisclosed | Frequent reward signals, biased toward adopted flows | Rival tools generate comparable telemetry |
| Foundry process design kits | Foundry IP | Strict NDA and approved-tool/use scope; no general model-training permission | Physically validated but node-specific | Foundries license multiple EDA vendors |
| Reusable semiconductor IP blocks | Vendor and many third parties | License field-of-use, sublicensing and confidentiality control inference/output | Validated IP valuable; security/version risk | ARM, internal customer IP and rival catalogs |

Third-party IP rights are material. Neither access to a customer design nor a PDK authorizes pooled foundation-model training. Generated RTL/layout may accidentally reproduce licensed patterns; provenance, indemnity and confidentiality terms are decisive but not fully public.

## Mechanisms and competition

1. **Reinforcement-learning optimization (classical ML):** design state and PPA feedback → search implementation choices → tapeout-quality result with fewer engineer iterations → subscription value and customer time saving. Public product evidence establishes capability and named deployments, usually E2 management/customer reports; benchmark wins are not automatically E3 because designs, compute budgets and human effort differ.
2. **Verification/RTL assistance (generative/agentic):** specifications, code and tool logs → draft RTL, tests and debug actions → engineer-approved closure → more project throughput or premium product revenue. Availability is E1; accepted output, escapes and full compute/review cost are mostly undisclosed.
3. **AI-infrastructure demand:** more complex AI chips require more EDA/IP. This can lift ordinary revenue, but it is demand exposure, not proof that AI improves the vendor's own productivity. It is kept outside the productivity mechanism.

The incumbent challenger is the other member of the EDA duopoly/triopoly, while Siemens EDA and internal/open-source tools are substitutes. Nvidia is both customer, compute supplier and collaborator; nonexclusive partnerships mean it can support rivals. Customer savings can be competed into license price, while usage/cloud pricing can let the vendor retain some value. Seat cannibalization is possible if agents perform more work per engineer; outcome/usage pricing could offset it but is not disclosed.

## Evidence ledger

| Claim | Type | Stage | Confounder |
|---|---|---|---|
| Latest revenue and profitability above | Filing/release fact | Financial | acquisition, mix and non-GAAP adjustments |
| Named AI optimization product is commercially available | Vendor product fact | E1/E2 | marketing, selection bias |
| AI can improve reported PPA or engineering time on named designs | Vendor/customer claim | E2, not E3 absent matched design | compute/human budget differs |
| Customer design and third-party IP rights are limited | Filing risk/contract inference | Rights fact/inference | contracts unavailable |
| Rival offers a directly comparable AI flow | Rival product fact | Challenger E1 | effectiveness not compared |
| Export/licensing restrictions can interrupt access | Filing/regulatory fact | Adverse | policy may change |
| AI-chip demand contributes to design complexity | Management claim | Ordinary demand | not internal productivity |

## KPI, economics and falsification

| KPI | Baseline/comparator | Eligible/quality condition | Known result | Closing evidence |
|---|---|---|---|---|
| Engineer-hours to timing/power closure | same design and compute budget with prior flow | adopted designs; signoff and silicon quality unchanged | selected examples only | randomized/matched project portfolio |
| Verification escapes per million gates | prior flow/matched designs | AI-generated tests/RTL; coverage and severity held | unknown | post-silicon cohort |
| AI ARR/usage less seat cannibalization | same customer before AI | AI SKU users; serving/compute and discounts deducted | unknown | renewal cohort and segment disclosure |

The 5% hurdle uses a labeled reported-profit scale because normalized post-transaction profit is unavailable: $22.5m per $450m quarterly GAAP operating-profit scale, or $90m annualized with seasonality caveat. Illustrative cost bridge: $800m eligible cost × 15% × 60% × 50% − $50m = $22m. All inputs are assumptions and customer engineering savings are not vendor cost. A revenue bridge must use incremental contribution after displaced seats, discounts, cloud compute and support.

Positive hypothesis: entrenched signoff flows, PDK trust and rapid objective feedback let AI increase tool value and customer throughput. Negative: customers own designs, foundries/third parties restrict data, rivals access similar signals and compute/model suppliers capture economics.

Falsifiers: matched projects show no time/PPA improvement at equal compute and signoff quality; AI SKU revenue fails to exceed seat cannibalization/serving cost; IP leakage or license restrictions prevent pooled learning. Confidence mechanism **high**, deployment **medium**, capture **low-medium**. G0/G1 provisional pass; G2 incomplete without controlled quality and retained cash. G3/G4 deferred. Original prior 95 preserved; no new score.

## Sources and handoff

Opened 12 Sep 2026: [latest results](https://investor.cadence.com/news-releases/news-release-details/cadence-reports-second-quarter-2026-financial-results) (financial period above); [SEC filings](https://www.sec.gov/edgar/browse/?CIK=813672) (annual/quarterly financial and IP risks); [Cadence.AI](https://www.cadence.com/en_US/home/ai.html) (product scope); [Nvidia-Synopsys collaboration](https://nvidianews.nvidia.com/news/nvidia-synopsys-partnership) (1 Dec 2025, explicitly nonexclusive); [Siemens EDA](https://eda.sw.siemens.com/en-US/ic/) (substitute); [U.S. BIS](https://www.bis.gov/) (export-control authority); [IEEE 1735 security study](https://arxiv.org/abs/2112.04838) (third-party research, 2021, IP protection adverse); [Synopsys.ai](https://www.synopsys.com/ai.html) (challenger). Some customer contracts and product metrics were inaccessible; unknowns remain explicit.

Handoff [c045.json](../capsules/c045.json). Verify latest GAAP/non-GAAP reconciliation, rights language for customer/third-party IP, and whether named benchmarks control compute/human/signoff quality. Research-only; G2 incomplete.

A proper experiment must pre-register design block, process node, constraints, engineer skill and compute budget. It should measure wall-clock time, human hours, tool/cloud cost, PPA and signoff violations through tapeout, then observe silicon escapes. Vendor-selected best runs overstate expected portfolio results. For generative code, provenance and security review are workload, not free safeguards. Renewal evidence should separate price, extra modules, acquisition cross-sell and AI usage. These controls are necessary before moving a mechanism beyond E2 or attributing consolidated growth to AI.
