# C005 — Novo Nordisk evidence dossier

**Unreviewed agent work.** Issuer: Novo Nordisk A/S; listed B shares NOVO B on Nasdaq Copenhagen (DKK) and NYSE ADR NVO (one ADR represents one B share); reporting currency DKK. Cutoff/retrieval: 12 September 2026. Latest financial period: H1/Q2 ended 30 June 2026, published 4 August 2026; FY2025 is the latest audited year.

## Provisional conclusion and ordinary business

Novo Nordisk owns unusually deep metabolic-disease biology, decades of trial and manufacturing experience, strong brands and global distribution. AI partnerships could improve target, molecule and document decisions. Evidence reaches E1 for expanded discovery programs and reported production for generative clinical-report drafting, but it does not establish better clinical transition rates or shareholder cash. Core economics are currently dominated by GLP-1 competition, realized prices, semaglutide exclusivity and capacity—not AI. September 2026 ziltivekimab trial terminations underscore that faster discovery cannot be equated with clinical success.

FY2025 sales were **DKK309.064bn**, operating profit **DKK127.658bn** (41.3% margin), net profit DKK102.434bn and diluted EPS DKK23.03. Operating profit fell 0.5% reported but rose 6% at constant exchange rates; roughly DKK8bn of restructuring and acquired Catalent-site effects complicate comparison. R&D was DKK52.039bn. Company-defined FCF was **DKK28.295bn**, after PP&E capex of DKK60.1bn; intangible purchases were another DKK30.0bn, mainly Akero. Year-end net debt was **DKK95.424bn** (the annual-report convention displays debt as a negative figure), after the Catalent manufacturing transaction and capacity expansion. See the [FY2025 financial-performance page](https://annualreport.novonordisk.com/2025/strategic-aspirations/financial-performance.html) and [five-year table](https://annualreport.novonordisk.com/2025/introducing-novo-nordisk/five-year-overview.html). FCF and net debt are non-IFRS.

The latest [H1 2026 report](https://ml-eu.globenewswire.com/Resource/Download/59861be7-056f-420d-985b-a7e976f8426d) showed Q2 sales DKK78.488bn and reported operating profit DKK27.061bn; adjusted operating profit was DKK33.389bn, up 11% at CER. Q2 included DKK6.3bn non-cash pipeline impairments. H1 FCF was DKK55.3bn. Guidance was raised to adjusted sales and operating-profit growth of 0% to -6% at CER, from -4% to -12%; these adjusted measures exclude the 340B provision reversal. These unusual provisions and impairments make reported-versus-adjusted separation essential.

Commercially, Ozempic, Wegovy and Rybelsus produce concentrated diabetes/obesity economics. FY2025 diabetes sales were DKK207.109bn and obesity DKK82.347bn. Lilly's tirzepatide products, lower US realized prices, patent expiry in some markets and compounded/generic alternatives threaten price and share. Manufacturing capacity is a real scarce asset, yet high capex means released R&D time cannot be assumed to become cash. Novo Holdings/Foundation controls voting power through unlisted A shares; B shares and ADRs have minority economics.

## Asset and data-rights audit

| Input | Owner/exclusivity | Inference/training rights | Labels and quality | Replication threat |
|---|---|---|---|---|
| Historic metabolic assays and molecule series | Novo/licensors | Internal use plausible; license and partner boundaries undisclosed | Repeated pharmacology and disposition labels; legacy cleaning unknown | Lilly and other pharma have deep proprietary archives |
| Trial participant data and biosamples | Participants/sites/sponsor under consent and law | Study-specific purpose, privacy and transfer restrictions; pooled foundation-model rights unknown | Prospective outcomes high-quality but slow, selected and indication-specific | Registries, public results and licensed RWE reduce exclusivity |
| Valo Opal Computational Platform and joint outputs | Valo background IP; allocation governed by contract | Up to 20 programs; ownership of model improvements/data reuse not public | Human-centric longitudinal data plus Novo assays claimed | Valo can partner elsewhere; AI-native entrants can license data |
| AWS/Anthropic-generated reports and cloud telemetry | Mixed company, cloud and model-provider context | AWS partnership describes secure foundation; retention/training terms not disclosed publicly | Regulatory documents have structured review and error labels | Cloud providers can sell equivalent tools to competitors |

Possession of longitudinal patient information does not establish consent for cross-program training. The public Valo and AWS announcements are commercial-scope evidence, not a complete rights schedule. Generated clinical documents remain sponsor responsibility and require human quality controls.

## Mechanisms, deployment and competition

1. **Computational discovery (ML/generative science):** metabolic experimental history and Valo models → rank targets and small molecules → fewer assays and earlier termination → potentially higher stage-adjusted pipeline output. The 2023 Valo agreement covered 11 programs; the January 2025 expansion increased scope to up to 20 and included $190m upfront with potential milestones. This is E1: programs are contracted, but public sources do not identify clinical nominations or transition-rate improvement.
2. **Clinical study report drafting (generative assistance):** trial tables, protocols and approved language → draft study-report sections → reviewer-approved document at lower elapsed time/cost. An [AWS customer account](https://aws.amazon.com/) describes work with Anthropic Claude and MongoDB. It supports production intent/use but search landing-page access did not expose a controlled quality result; classify E2 only where company-reported deployment exists, not E3.
3. **Target-to-first-human workflow on AWS (AI infrastructure and assistance):** secure compute plus biological models → integrate research decisions and operational handoffs → shorter elapsed discovery cycle. The August 2026 partnership is E1; targets, workloads, baseline and outcome remain undisclosed.

The incumbent challenger is **Eli Lilly**, whose branded tirzepatide franchise competes directly and whose [TuneLab](https://investor.lilly.com/news-releases/news-release-details/lilly-launches-tunelab-platform-give-biotechnology-companies) exposes models trained on disposition, safety and preclinical datasets covering hundreds of thousands of molecules through federated learning. The substitute/entrant is Valo or another AI-native biotech that can own candidate economics and auction programs among sponsors. Generic model/cloud vendors can compress document work across the industry, passing benefits to customers or regulators rather than producing a durable Novo edge.

| Claim | Type | Opened source/date | Scope/stage | Main confounder |
|---|---|---|---|---|
| FY2025 sales DKK309.064bn, OP DKK127.658bn | Fact | Annual Report financial performance, 3 Feb 2026 | Financial fact | Restructuring, FX, Catalent effects |
| FY2025 FCF DKK28.295bn; net debt DKK95.424bn | Fact | Annual Report five-year overview, 2026 | Financial fact | FCF/net debt are non-IFRS |
| Q2 adjusted OP DKK33.389bn | Fact | H1 report, 4 Aug 2026 | Financial fact | 340B adjustment and impairments |
| Valo scope expanded to up to 20 programs | Partner claim | [Valo release](https://www.valohealth.com/), 8 Jan 2025 landing content | E1 | No named clinical output |
| AWS selected as strategic AI partner | Management/partner claim | [Novo news archive](https://www.novonordisk.com/news-and-media/news-and-ir-materials.html), 10 Aug 2026 | E1 | Scope and economics undisclosed |
| Generative clinical-report workflow exists | Supplier claim | AWS customer page, accessed 12 Sep 2026 | E2, narrow | No controlled end-to-end result surfaced |
| Two ziltivekimab studies were stopped after low probability of benefit | Fact/adverse | [Reuters](https://www.reuters.com/legal/litigation/novo-scraps-two-more-heart-drug-trials-further-dimming-growth-beyond-obesity-2026-09-07/), 7 Sep 2026 | Clinical outcome | Not shown to be AI-generated |
| 2026 sales/profit pressure reflects price, competition and patent factors | Fact/management outlook | Annual Report outlook; H1 report | Core business | Guidance may change |

## Measurement contract and materiality

| KPI | Baseline/comparator | Eligible workload and quality | Known result | Next proof event |
|---|---|---|---|---|
| Phase II→III and III→approval by entry cohort | Pre-tool cohorts matched by area/modality | Valo/AWS-supported programs; safety and efficacy unchanged | Unknown | Program provenance and 5–8-year cohort disclosure |
| Cost/time to nominated candidate | Same target class before platform | Up to 20 Valo programs; potency/toxicity gates | No result disclosed | Candidate milestone or IND disclosure |
| Report authoring hours and calendar days | Matched study reports | Reports using generative workflow; factual-error and audit findings capped | Deployment described, effect unknown | Controlled quality study or audited transformation KPI |

Five percent of FY2025 reported operating profit is **DKK6.383bn annual pre-tax** (`0.05 × 127.658bn`). There is no valid disclosed monetary bridge. Program NPV cannot be compared with annual operating profit. The consistent break-even is `annualized, probability-weighted incremental contribution from AI-attributable programs + realized annual operating savings − annual model/validation/partner cost ≥ DKK6.383bn`. This needs matched transition probabilities, program cash-flow timing, Novo's retained economics and full cost, none public. Separately, a document-efficiency bridge would require eligible authoring cost × measured improvement × realization × retained share minus run cost; every input is undisclosed. R&D cost of DKK52.039bn is context, not an assumed savings pool.

## Competing hypotheses, falsifiers and gates

Positive hypothesis: unusually dense metabolic feedback and integrated development/manufacturing allow Novo to kill weak programs earlier and retain patent economics on successful ones. Negative hypothesis: Lilly and AI-native firms have comparable models, while clinical biology, manufacturing and price access dominate; Novo pays partners and cloud suppliers while patients/payers capture efficiency. Concentration makes core-business deterioration more material than administrative automation.

Falsifiers: (1) matched Valo/AWS cohorts do not improve time-to-termination or stage transitions after modality control; (2) no Valo-originated program reaches clinical nomination on disclosed timelines; (3) AI run/partner costs and extra experiments rise without improved risk-adjusted output. Confidence: mechanism **medium**, deployment **low-medium**, capture **low**. G0 passes; G1 provisional given strong franchise but concentration, debt and pricing pressure; G2 insufficient because no controlled clinical productivity or retained economics exists. G3/G4 deferred by user. Original prior 85 is preserved without a new score.

Unresolved: Which programs use Valo/AWS? What are output-IP and pooled-learning rights? How many scientists/reports use the tools? What matched quality/time result exists? How much of restructuring savings is AI-attributable? What full recurring and milestone cost does Novo bear?

## Source register

Opened 12 Sep 2026: [FY2025 financial performance](https://annualreport.novonordisk.com/2025/strategic-aspirations/financial-performance.html) and [five-year overview](https://annualreport.novonordisk.com/2025/introducing-novo-nordisk/five-year-overview.html) (Novo Nordisk, 3 Feb 2026); [H1 2026 report](https://ml-eu.globenewswire.com/Resource/Download/59861be7-056f-420d-985b-a7e976f8426d) (Novo Nordisk, 4 Aug 2026, PDF); [financial-results hub](https://www.novonordisk.com/investors/financial-results.html) (event confirmation); [Valo original collaboration](https://www.valohealth.com/) (24 Sep 2023 landing page) and [expanded release copy](https://www.globenewswire.com/news-release/2025/01/08/3006249/0/en/Valo-Health-and-Novo-Nordisk-expand-collaboration-to-discover-and-develop-novel-treatments-in-cardiometabolic-disease.html) (8 Jan 2025; partner-issued); [Novo news archive](https://www.novonordisk.com/news-and-media/news-and-ir-materials.html) (10 Aug 2026 AWS announcement listing); [AWS customer page](https://aws.amazon.com/) (supplier landing evidence, detailed case text incompletely accessible); [Lilly TuneLab release](https://investor.lilly.com/news-releases/news-release-details/lilly-launches-tunelab-platform-give-biotechnology-companies) (9 Sep 2025); [Reuters adverse trial report](https://www.reuters.com/legal/litigation/novo-scraps-two-more-heart-drug-trials-further-dimming-growth-beyond-obesity-2026-09-07/) (7 Sep 2026).

Handoff: [c005.json](../capsules/c005.json). Verify FY2025/H1 adjustments, the up-to-20-program Valo scope/rights, and the ziltivekimab stop. Strongest counterargument: price/share and clinical outcomes swamp unmeasured AI productivity. Provisional disposition research-only; G2 incomplete.
