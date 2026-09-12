# Medtronic — evidence packet

**Identity/boundary.** Medtronic plc ordinary shares trade NYSE:MDT in USD; Irish-domiciled issuer, reporting currency USD. Cutoff/retrieval 12 September 2026. Latest full period is FY2026 ended 24 April 2026, released 3 June 2026. This unreviewed packet excludes MiniMed valuation and any ranking. Conclusion: Medtronic has regulatory distribution, installed devices and genuine production AI, with the strongest causal evidence in computer-aided colonoscopy; evidence that Medtronic retains a group-material cash gain is absent.

## Existing business and resilience

Medtronic sells cardiovascular, neuroscience and medical-surgical devices, with diabetes being separated. Revenue includes implanted capital equipment, consumables and service, so clinical adoption and installed base can compound, but hospitals and payers bargain over price. FY2026 revenue was **$36.4bn**, up 8.4% reported and 5.8% organic; GAAP operating profit **$6.467bn**, adjusted operating profit **$8.856bn**; cash from operations **$7.330bn**, free cash flow **$5.426bn**; cash and investments **$9.2bn**. GAAP diluted EPS was $3.73 versus adjusted $5.53. [FY2026 SEC-filed release](https://www.sec.gov/Archives/edgar/data/1613103/000162828026040034/exhibit991-fy26q4earningsr.htm), 3 June 2026. Free cash flow equals operating cash less capital expenditure under the company definition; adjusted profit excludes acquisition, restructuring and other charges. FY2027 guidance called for 6.8–7.3% organic revenue growth and adjusted EPS $5.90–$6.00, but tariffs, MiniMed separation and business mix confound comparison.

The core survives with zero incremental AI: cardiac rhythm, ablation, structural-heart, spine, neuromodulation, surgical and monitoring franchises solve regulated physical needs. Risks include recalls/product liability, procedure cycles, hospital budgets, competitive launches and tariffs. Capital allocation returned $4.2bn in FY2026; dividends have increased for 49 years, while acquisitions and R&D absorb cash.

## Assets and lawful use

| Input | Owner / exclusivity | Inference | Training / reuse | Quality / replication |
|---|---|---|---|---|
| GI Genius procedure video | Hospital/patient with Medtronic device/software rights | Real-time inference under cleared use | Cross-site training consent/contracts undisclosed | Pathology-confirmed lesions are useful labels; Olympus/Fujifilm and entrants compete |
| Touch Surgery video | Provider/patient; uploaded under customer agreement | Customer workflow analysis | Pooled training and retention terms not established in public product page | Expert phase annotations costly; video standards portable |
| Implant/navigation telemetry | Patient/provider plus device/service contract | Product and service inference likely | Cross-customer reuse unknown | High-frequency signals, but outcome linkage and drift matter |
| Surgical maps/models | Medtronic and licensed imaging; patient scan rights | Case-specific planning | Secondary training bounded | Regulated integration and installed hardware are scarcer than generic models |

Medtronic’s advantage is workflow position and regulatory clearance, not universal ownership of patient data. Customer-specific inference may improve a procedure without permitting pooled learning. NVIDIA supplies infrastructure and hospitals retain clinical responsibility.

## Mechanisms and challengers

1. **GI Genius computer-aided detection (deep vision ML).** Colonoscopy video → real-time lesion flag → higher adenoma detection at no worse non-neoplastic resection → software/device revenue and installed-base defense. A 2025 multicenter quasi-randomized study of 795 patients reported ADR 59.1% with GI Genius versus 46.6% control and no significant NNRR difference. This is E3 for a defined clinical task, not proof of mortality benefit or Medtronic margin.
2. **Touch Surgery Performance Insights/Aide (vision ML and intraoperative assistance).** Video is segmented into phases and instruments for post-operative review; Medtronic describes production installations and in 2026 an NVIDIA-based platform intended to run AI during procedures. Output should be review time, protocol adherence and complications at equal case mix. No controlled end-to-end outcome or paid attach denominator was found: E2 deployment, E1 economics.
3. **Stealth AXiS mapping/navigation.** FDA-cleared system integrates imaging, robotics and navigation; for cranial procedures Medtronic says AI automatically generates brain maps. Clearance and availability establish E2 product deployment, not comparative clinical benefit.

Olympus is the incumbent challenger in endoscopy, while Fujifilm and independent AI vendors are substitutes. Intuitive is the surgical-platform challenger; generic video models and hospital analytics can bypass Touch Surgery if data export is workable. Surgeon review, liability and regulatory change slow autonomous execution.

## Evidence ledger

| Claim | Type/source/date | Scope | Stage | Confounder |
|---|---|---|---|---|
| FY26 revenue $36.4bn; GAAP OP $6.467bn; FCF $5.426bn | Fact, SEC release, 3 Jun 2026 | Group | financial | FX, MiniMed, adjustments |
| GI Genius ADR 59.1% vs 46.6% in 795-patient study | Peer-reviewed fact, [PubMed](https://pubmed.ncbi.nlm.nih.gov/40018072/), 2025 | Specific centers/patients | E3 | Quasi-randomized; endoscopist subgroup; no mortality/economics |
| NNRR did not significantly worsen (15.1% vs 17.1%) | Same study | Same | E3 | Power/generalizability |
| Touch Surgery offers AI-enabled postoperative video analysis | Vendor fact/claim, [product page](https://www.medtronic.com/en-us/healthcare-professionals/products/digital-surgery/touch-surgery-performance-insights.html), opened 12 Sep 2026 | Product | E2 | No site denominator or controlled result |
| Touch Surgery Aide intended for intraoperative AI | Management claim, [Medtronic story](https://news.medtronic.com/How-AI-is-changing-the-way-your-doctor-performs-surgery), 21 Jul 2026 | Platform | E1/E2 | Marketing; intended applications differ by clearance |
| Stealth AXiS received expanded FDA clearance | Fact, [FDA clearance report](https://www.reuters.com/business/healthcare-pharmaceuticals/medtronic-gets-us-fda-nod-use-surgical-system-cranial-ent-surgeries-2026-03-27/), 27 Mar 2026 | Cranial/ENT | E2 | Clearance is not superiority |
| Surgical VLMs struggle with spatial/temporal reasoning | Research counterevidence, [preprint](https://arxiv.org/abs/2504.02799), 3 Apr 2025 | 13 datasets | E3 capability negative | Research datasets, not Medtronic product |

## KPI contract and materiality

| KPI | Baseline/comparator | Eligible workload | Quality condition | Known | Close gap |
|---|---|---|---|---|---|
| ADR per completed colonoscopy | Concurrent conventional colonoscopy | Cleared GI Genius procedures | NNRR, withdrawal time and adverse events non-inferior | +12.5 percentage points in one study | Multisite production cohorts plus renewal/price data |
| Minutes to review and coached actions adopted | Existing manual review | Touch Surgery recorded cases | Blinded skill score and complications no worse | Unknown | Stepped-wedge hospital study |
| Paid AI attach and gross profit/site/year | No AI module | Compatible installed systems | Support/compute included | Unknown | Segment disclosure/renewals |

The annual 5% hurdle is **$323m** (5% × FY26 GAAP operating profit $6.467bn). Illustrative recurring bridge: 6,000 eligible sites × $150,000 annual AI/software revenue × 45% adoption × 65% contribution margin × 80% retention after hospital sharing = **$211m/year**. Add GI Genius: 20,000 systems/procedure rooms × $15,000 × 50% paid attach × 65% × 80% = **$78m/year**, for $289m before central recurring AI cost. With assumed $60m platform expense, net $229m, below the hurdle. Required first-module adoption holding other inputs is `(323+60-78)/(6000×150×.65×.8)=56.6%`. These are assumptions, not guidance; clinical benefit cannot be counted as Medtronic revenue without a payment mechanism.

## Hypotheses, falsifiers, gates

Positive: regulated hardware distribution and workflow data let Medtronic sell demonstrably better detection and navigation across a large installed base. Negative: clinically useful point solutions remain small, hospitals capture savings, video models commoditize and validation/liability prevent broad agentic use.

Falsifiers: paid AI attach remains immaterial after three renewal cycles; multisite GI Genius studies fail to reproduce quality-adjusted ADR lift; Touch Surgery produces no matched reduction in review time or complications after case-mix adjustment. Questions: exact installed/paid counts, pooled-video rights, pricing, compute/support cost, and adverse-event liability allocation.

Confidence: mechanism medium-high; deployment medium; capture low. G0 pass; G1 provisional pass subject to device/legal review; G2 provisional because one scoped E3 result and multiple E2 products exist but material retained economics do not. G3/G4 deferred.

## Sources

1. Medtronic, FY2026 results, 3 Jun 2026, opened 12 Sep: https://www.sec.gov/Archives/edgar/data/1613103/000162828026040034/exhibit991-fy26q4earningsr.htm
2. Medtronic, FY26 Q4 presentation, 3 Jun 2026, opened 12 Sep: https://filecache.investorroom.com/mr5ir_medtronic/921/Q4FY26-Earnings-Presentation.pdf
3. Lui et al., AI-assisted colonoscopy study, 2025, opened 12 Sep: https://pubmed.ncbi.nlm.nih.gov/40018072/
4. Medtronic, Touch Surgery Performance Insights, undated, opened 12 Sep; marketing limits: https://www.medtronic.com/en-us/healthcare-professionals/products/digital-surgery/touch-surgery-performance-insights.html
5. Medtronic, AI and surgery, 21 Jul 2026, opened 12 Sep: https://news.medtronic.com/How-AI-is-changing-the-way-your-doctor-performs-surgery
6. Reuters, Stealth AXiS clearance, 27 Mar 2026, opened 12 Sep: https://www.reuters.com/business/healthcare-pharmaceuticals/medtronic-gets-us-fda-nod-use-surgical-system-cranial-ent-surgeries-2026-03-27/
7. Rau et al., surgical VLM evaluation, 3 Apr 2025, opened 12 Sep; preprint: https://arxiv.org/abs/2504.02799

Capsule: [c008.json](../capsules/c008.json). Reviewer checks: FY26 GAAP/adjusted reconciliation; GI Genius E3 scope; assumed attach arithmetic. Unreviewed.
