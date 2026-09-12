# Siemens (C059) — initial evidence dossier

**Status:** unreviewed agent work; lead-review required. **Evidence cutoff / access date:** 12 September 2026. **Issuer/security:** Siemens Aktiengesellschaft, registered ordinary shares, Xetra ticker **SIE**, ISIN DE0007236101; quote and reporting currency EUR. There is no ADR conversion in this valuation. **Industry:** D01 industrial automation and electrification.

## Provisional conclusion

Siemens has a strong conventional business, real installed workflow access and reported production use of industrial copilots. The useful evidence reaches **E2**, not E3: product and customer sources show deployments, but disclosed comparisons do not establish sustained, quality-adjusted output against the current production baseline, and no source bridges AI to renewal economics or group cash profit. The stock also carries substantial direct AI-infrastructure demand: Smart Infrastructure’s data-center orders reached about €6 billion in the first nine months of FY2026. That demand is economically valuable but must not be mistaken for AI improving Siemens’ own/customer workflows.

At the 11 September 2026 close of €261.70, the shares were roughly 23.1 times the midpoint of FY2026 EPS pre-PPA guidance (€11.20–€11.50). A simple five-year earnings/dividend model requires about 10.8% annual EPS growth to reproduce the price at a 9% return hurdle and 19x exit multiple. This looks demanding against a conventional-business base, particularly because FY2025 continuing diluted EPS was €9.52 and the planned Healthineers distribution changes the security perimeter. **Provisional disposition: watch, do not promote. G2 passes narrowly; G3 is conditional rather than cleanly passed until the Healthineers distribution and pro-forma share/earnings bridge are verified.**

## Conventional business and financial resilience

Siemens combines factory automation and industrial software (Digital Industries, DI), electrification/buildings (Smart Infrastructure, SI), rail equipment and service (Mobility), a majority holding in separately listed Siemens Healthineers, and financing. DI sells automation hardware, PLM, EDA, simulation and data-driven services; its end markets and standard products remain cyclical. SI sells building controls, grid/electrification products, software and service through direct and partner channels. Mobility’s long projects and service backlog add duration. This mix is viable without incremental AI, but the value is not pure recurring software.

The audited [Siemens Report 2025](https://www.siemens.com/siemensreport) (published 1 December 2025; FY ended 30 September 2025) reports the following. Siemens’ FCF definition is operating cash flow less additions to intangible assets and property, plant and equipment; it is not a maintenance-only measure.

| €bn except per-share data | FY2025 | FY2024 | Comment |
|---|---:|---:|---|
| Revenue, continuing operations | 78.914 | 75.930 | +5% comparable; China revenue -9% comparable |
| Industrial Business profit / margin | 11.766 / 15.4% | 11.390 / 15.5% | Segment measure, not IFRS operating profit |
| Income before tax, continuing | 10.830 | 11.227 | Reconciliation burden nearly doubled |
| Net income, all operations | 10.387 | 8.992 | Included €2.059bn discontinued income |
| Diluted EPS, continuing / total | €9.52 / €12.11 | €10.27 / €10.38 | Total EPS flatters the recurring perimeter |
| Operating cash flow, continuing | 13.448 | 11.814 | Strong working-capital conversion |
| Capex/intangible additions | 2.445 | 2.088 | Reported cash additions |
| FCF, continuing / all-in | 11.004 / 10.812 | 9.726 / 9.494 | Exact reconciliation above |
| Industrial net debt / EBITDA | 12.160 / 0.9x | 9.421 / 0.7x | Total net debt €40.0bn includes SFS funding |
| Weighted average basic / diluted shares | 785.1m / 793.8m | 788.7m / 798.9m | 10.74m shares repurchased in FY2025 |

DI’s FY2025 revenue fell 4% to €17.8bn and profit fell 24% to €2.64bn (14.9% margin), reflecting automation destocking, lower software revenue, €356m severance and €135m Altair/Dotmatics burden. SI revenue rose 8% to €23.0bn and profit 22% to €4.51bn (19.6%), but profit included a €0.3bn disposal gain; data-center demand, volume, utilization and broad “productivity improvements” confound AI attribution. Siemens spent €9.3bn cash on Altair and €4.2bn on Dotmatics in FY2025, materially increasing integration and capital-allocation risk.

The latest [Q3 FY2026 release](https://press.siemens.com/global/en/pressrelease/record-third-quarter-outlook-raised) (6 August 2026; quarter ended 30 June) showed revenue €20.8bn, Industrial Business profit €3.5bn/17.3%, net income €2.6bn and all-in FCF €4.1bn. DI organic ARR reached €5.7bn (+11%) and software revenue grew 15%; SI data-center orders grew at a triple-digit rate to about €6bn over nine months. Management raised FY2026 EPS pre-PPA guidance to €11.20–€11.50. The release says the Healthineers spin-off can proceed after tax decisions; this dossier does not have a completed pro-forma perimeter, a decisive valuation limitation.

## Scarce asset and data-rights audit

| Input | Origin / owner | Exclusivity | Retrieval / inference | Training / pooled learning | Labels / quality | Replication threat |
|---|---|---|---|---|---|---|
| TIA Portal engineering projects, PLC code and automation libraries | Customer projects plus Siemens software/IP | Siemens IP is proprietary; customer project data is customer-controlled | Copilot is integrated through TIA Portal APIs; customer-specific use reported | Microsoft says customers retain control and data are not used to train underlying models; Siemens cross-customer improvement rights remain **unknown** | Compilation/simulation can label errors, but production safety and exceptions need human validation | Schneider, Rockwell and generic coding models; open APIs reduce lock-in |
| Xcelerator digital twins, product models and simulation | Siemens/Altair software plus customer designs | Software/schema proprietary; designs customer-owned | Contract-specific access plausible and demonstrated in named collaborations | Cross-customer training rights **unknown**; no pooled-rights evidence found | Physics/simulation creates synthetic labels; fidelity to plant remains limiting | Dassault, PTC, Ansys/Synopsys and hyperscaler tools |
| Machine telemetry and maintenance/work-order history | Usually customer/asset owner; Siemens may process via service/CMMS | Customer-specific, not a group-owned corpus | Siemens asset products process connected telemetry and CMMS records | Retention, portability, Siemens training and cross-customer rights **unknown** | Failures/downtime can label outcomes, but maintenance changes and censoring confound | Independent CMMS/condition monitoring, OEM-neutral integrators |
| Installed controls and service channel | Siemens hardware/software footprint and partners | Switching cost is real but not absolute | Direct route to deploy upgrades and service | Not itself a data right | Equipment configuration/domain knowledge improves grounding | ABB, Schneider, Rockwell; customers can multi-source |

The strongest verified rights claim comes from [Microsoft’s Siemens partnership announcement](https://news.microsoft.com/source/2023/10/31/siemens-and-microsoft-partner-to-drive-cross-industry-ai-adoption/) (31 October 2023): customers control their data and it is not used to train underlying models. This protects customers but weakens the claimed pooled feedback moat. No opened contract established that Siemens may train across customers. Data advantage should therefore rest on integration, proprietary engineering representations, installed distribution and validation expertise, not assumed ownership of plant data.

## Mechanisms, deployment and competition

**1. Automation engineering copilot/agents (generative assistance moving toward agentic execution).** Scarce asset: TIA Portal context, automation libraries and domain constraints. Task: generate, debug, configure and validate PLC automation. Deployment: [Siemens’ May 2025 agent announcement](https://press.siemens.com/global/en/pressrelease/siemens-introduces-ai-agents-industrial-automation) describes an orchestrator, Siemens and third-party agents and user control, but its “up to 50%” productivity is an aspiration. [Schaeffler and Siemens](https://press.siemens.com/global/en/pressrelease/ai-industry-schaeffler-and-siemens-bring-industrial-copilot-shopfloor) report engineers using the copilot with TIA Portal, which supports E2 production use, not causal savings. Economic line: software ARR/attach, engineering-services capacity or customer willingness to pay. Retention is unquantified; Microsoft/model cost, integration, verification and potential seat substitution are undisclosed.

**2. Maintenance and operations assistance (generative plus established ML).** Siemens’ [maintenance offering](https://press.siemens.com/global/en/pressrelease/siemens-expands-industrial-copilot-new-generative-ai-powered-maintenance-offering) combines plant documentation, error codes and maintenance information to support technicians. Its asset-management site claims 11,000+ organizations and billions of historical data points, but that establishes distribution and an offering, not that customer data can be pooled or that failures decline. Classical predictive maintenance and sensor analytics are already in the reported baseline; incremental GenAI must improve end-to-end resolution, not merely retrieval speed.

**3. Digital twins for plant design and throughput (simulation/optimization with AI).** [PepsiCo’s January 2026 announcement](https://www.pepsico.com/newsroom/press-releases/2026/pepsico-announces-industry-first-ai-and-digital-twin-collaboration-with-siemens-and-nvidia) describes plans to scale a Siemens/NVIDIA approach after a U.S. facility deployment. This is customer-reported production evidence, but scope, matched baseline, implementation cost, safety/quality constraints and realized cash savings were not disclosed in the opened material. Economics could appear through Siemens software subscriptions and service, while much of customer productivity may be competed away.

Competitively, Schneider’s [2026 Azure AI industrial-copilot release](https://www.se.com/ww/en/about-us/newsroom/news/press-releases/Schneider-Electric-unveils-next-generation-agentic-manufacturing-capabilities-powered-by-Microsoft-Azure-AI-at-Hannover-Messe-2026-69e08de2ddabef15890a48f3/) claims up to 50% engineering-time reduction. The same model supplier and similar claim show that Siemens does not uniquely own the generative layer. ABB, Rockwell, Dassault and OEM-neutral integrators can attack the same tasks. Siemens’ defensible advantage is safer embedding across engineering models, controllers and lifecycle software; interoperability and third-party agents also make complements easier to substitute.

## Evidence ledger

| Claim | Type | Source/date; section | Scope / stage | Confounder |
|---|---|---|---|---|
| FY2025 revenue €78.9bn, IB profit €11.8bn, continuing FCF €11.0bn | Fact | Siemens Report, 1 Dec 2025, pp. 15–21 | Audited group; E4 conventional | Segment profit differs from IFRS operating profit |
| Q3 FY2026 IB profit €3.5bn and FCF €4.1bn | Fact | Q3 release, 6 Aug 2026, key figures | Group quarter; conventional | Mix, volume, FX, restructuring |
| SI nine-month data-center orders about €6bn | Management fact | Q3 release, data-center paragraph | Direct AI-capex exposure; E2 demand | Does not evidence own/customer productivity |
| DI organic ARR €5.7bn, +11% | Management fact | Q3 release, DI paragraph | Monetization channel | AI attach/price/renewal not isolated |
| Industrial agents can execute workflows | Management claim | Siemens agent release, 12 May 2025 | Offering; E1 | Roadmap/availability varies by agent |
| Schaeffler engineers use Industrial Copilot with TIA Portal | Company/customer claim | joint release, 8 Nov 2023 | Named deployment; E2 | No comparator, sample or cash bridge |
| Customer data do not train underlying models | Partner fact | Microsoft, 31 Oct 2023 | Specific copilot architecture | Siemens improvement rights not fully specified |
| PepsiCo deployed digital-twin approach and plans scale | Customer claim | PepsiCo, 6 Jan 2026 | Named deployment; E2 | No disclosed net economics |
| €261.70 closing price | Third-party market fact | [Yahoo historical data](https://finance.yahoo.com/quote/SIE.DE/history/), 11 Sep 2026 | Ordinary share quote | Yahoo reports €261.70 while Google displayed €264.65; reviewer should reconcile venue/timestamp |

## KPI contract and retained-economics bridge

Minimum promotion threshold: a credible five-year path to **€0.59bn annual net operating benefit**, 5% of FY2025 Industrial Business profit. This is an analyst convention.

| KPI | Baseline/comparator | Eligible workload | Quality constraint | Known result | Next proof event |
|---|---|---|---|---|---|
| Engineering hours per accepted PLC change | Pre-rollout matched TIA teams | Copilot-eligible code/configuration | Compile, simulation, safety test, rollback and defect rate equal/better | Unknown; “up to 50%” target/claim is insufficient | FY2026 results/customer renewal cohort |
| Mean time to resolve / downtime hours | Same asset classes before/after or randomized rollout | Connected assets with usable documentation | Uptime, false action, safety incidents | Unknown | Named scaled customer with 12-month data |
| AI software ARR, attach and net retention | Existing DI ARR excluding acquisitions | Eligible TIA/Xcelerator customers | Gross margin after model/integration support | Not disclosed | FY2026 annual report / capital-markets update |

Illustrative cost route: `€4.0bn eligible customer/internal workflow economics × 20% efficiency × 60% realization × 50% Siemens retained share − €0.15bn recurring AI expense = €0.09bn`, only 0.8% of FY2025 IB profit. To reach €0.59bn on those assumptions requires about **€8.3bn eligible cost pool** (`(0.59+0.15)/(0.20×0.60×0.50)`). Inputs are assumptions, not forecasts. A revenue route could be larger, but must disclose incremental ARR, contribution margin, cannibalization and model cost; current evidence does not.

## Valuation and reverse valuation

Price €261.70 (11 September 2026); FY2025 diluted weighted shares 793.8m; implied equity value about €207.8bn. Industrial net debt was €12.2bn at 30 September 2025, but a clean enterprise bridge is inappropriate without separately valuing SFS and the listed Healthineers stake. The per-share model therefore uses management’s FY2026 EPS pre-PPA midpoint €11.35 as a starting proxy and explicitly includes dividends; it is not a sum-of-parts.

| Case | Five-year EPS growth | AI treatment | Exit P/E / return hurdle | PV dividends + terminal value | Value/share |
|---|---:|---|---|---:|---:|
| Bear | 0% | Zero; hardware cycle/integration burden | 15x / 10% | €20.3 + €105.7 | **€126** |
| Base | 5% | Existing digital execution only; no separately credited uplift | 19x / 9% | €23.9 + €178.9 | **€203** |
| Bull | 8% | Conditional AI attach plus strong electrification | 23x / 8% | €26.8 + €261.1 | **€288** |

Formula: PV of five annual dividends starting from €5.35 and growing with EPS, plus `€11.35×(1+g)^5×exit P/E/(1+r)^5`. At €261.70, 19x exit and 9% hurdle, required five-year EPS/dividend growth is **10.8% annually**. A one-turn exit-multiple change is material: at base EPS growth/9% hurdle, 17x gives about €184 and 21x about €222. The model overstates comparability if current guidance includes earnings/stake value that will leave via Healthineers distribution; G3 stays conditional pending pro-forma terms.

## Risks, falsifiers, priors and gates

Strongest positive hypothesis: Siemens bundles domain models, installed controllers, simulation and service distribution so customers pay recurring software/service fees for faster safe engineering and operations. Strongest negative: the model layer is shared, plant data stays customer-controlled, integrations are bespoke, and competition transfers productivity to customers while Siemens bears support cost. Conventional risks include China/cycle exposure, large acquisitions, software-accounting judgment, restructuring and the Healthineers perimeter change.

Falsifiers: (1) no disclosure by FY2027 of scaled paid AI ARR/attach or named renewal cohort; (2) controlled deployments show no sustained reduction in accepted engineering hours or downtime after full implementation and safety review; (3) AI gross margin/retention is diluted by model, integration or price competition. A core-business falsifier is DI automation/software margins staying below the mid-teens through recovery. A price falsifier is a valuation requiring >10% long-run earnings growth without comparable evidence.

| Dimension | Original prior | Proposed revision | Reason |
|---|---:|---:|---|
| Scarce asset | 5 | 4 | Strong installed/workflow IP, but customer owns key plant context |
| AI leverage | 4 | 4 | Core engineering/operations tasks are material |
| Feedback | 4 | 2 | Pooled improvement rights and reusable outcome loop unverified |
| Testability | 4 | 4 | Hours, defects and downtime can be matched; evidence not yet published |
| Distribution | 5 | 5 | TIA/Xcelerator/service channels and ARR verified |
| Capture | 4 | 3 | Monetization channel exists; incremental AI price/margin absent |

Revised structural score: **74/100** (capture-30%/feedback-5% sensitivity: 72/100), versus 87 prior. **G0 pass. G1 pass with acquisition/perimeter monitoring. G2 narrow pass** on E2 named deployments and a credible measurable path, though 5% materiality is not evidenced. **G3 conditional/blocked from promotion** because quote inputs are usable but Healthineers pro-forma earnings and distribution terms are unresolved. **G4 not assessed.** Confidence: mechanism moderate-high; deployment moderate; capture low; valuation low-moderate.

Peer/inaction alternative: compare Schneider’s more concentrated electrification exposure and ABB/Rockwell’s automation channels after equivalent evidence; wait for pro-forma Healthineers terms and paid AI cohort economics.

## Source register and reviewer handoff

1. Siemens, *Siemens Report 2025*, 1 Dec 2025, accessed 12 Sep 2026, pp. 7–21, 42–79, 142. Audited baseline; AI economics not isolated.
2. Siemens, *Record third quarter – Outlook raised*, 6 Aug 2026, accessed 12 Sep 2026. Latest trading update; management-reported non-GAAP measures.
3. Siemens, *Industrial AI agents*, 12 May 2025, accessed 12 Sep 2026. Offering/target; no controlled outcome.
4. Microsoft, *Siemens and Microsoft partner*, 31 Oct 2023, accessed 12 Sep 2026. Architecture and data-control statement; older/specific scope.
5. Siemens/Schaeffler, *Industrial Copilot to shopfloor*, 8 Nov 2023, accessed 12 Sep 2026. Named use; no economics.
6. Siemens, *Generative AI maintenance offering*, 17 Sep 2024, accessed 12 Sep 2026. Product capability only.
7. PepsiCo, *AI and digital twin collaboration*, 6 Jan 2026, accessed 12 Sep 2026. Customer source; rollout economics absent.
8. Schneider Electric, *Agentic manufacturing capabilities*, 31 Mar 2026, accessed 12 Sep 2026. Rival claim; not independently controlled.
9. Yahoo Finance, *SIE.DE historical data*, 11 Sep 2026, accessed 12 Sep 2026. Quote; reconcile with alternative close display.
10. Siemens, *Basic data and key share figures*, accessed 12 Sep 2026. Confirms ordinary-share identity; live 2026 close not supplied.

**Three decisive claims to verify:** (i) reconcile 11 September Xetra official close (€261.70 Yahoo versus €264.65 Google display); (ii) confirm the precise Healthineers distribution ratio/pro-forma FY2026 EPS before G3; (iii) verify whether any current customer contract permits Siemens to reuse operational outcomes across customers. **Strongest counterargument:** €6bn of data-center orders plus fast DI ARR growth may support earnings regardless of still-unproved AI productivity. **Blocking questions:** paid Industrial Copilot ARR/attach/renewal, controlled end-to-end results, and net model/integration cost. **Provisional disposition:** watch; G2 only, no purchase conclusion. **File written:** `research/batch-01/dossiers/07-siemens.md`.
