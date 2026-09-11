"""Reproducible initial universe. Manual priors are explicit and reviewable."""
from build_research import ROOT, DATE, AREAS, SM, build_areas, write
import csv, json
from collections import Counter

# Company | primary area | home market | asset hypothesis | central company-specific risk | six structural priors | direct source IDs
# These are company candidates, not verified security identifiers or an order list.
DATA='''
Sanofi|H01|France|Immunology and vaccine research, clinical cohorts and trial infrastructure|R&D productivity must translate into clinical successes beyond existing leading franchises|545355|S03
Roche|H01|Switzerland|Combined pharmaceutical research and diagnostic relationships|Diagnostic access does not automatically permit linking or reusing patient-level data|545355|
AstraZeneca|H01|United Kingdom|Oncology and broader clinical-development engine|Pipeline breadth can mask correlated clinical and commercial risks|545355|
Novartis|H01|Switzerland|Therapeutic expertise and global clinical-development operations|Portfolio simplification alone can explain productivity gains|545355|
Novo Nordisk|H01|Denmark|Metabolic disease expertise and longitudinal development experience|Concentration and competition may dominate any AI gain|544354|
Eli Lilly|H01|United States|Metabolic and neuroscience development and manufacturing knowledge|An excellent engine can still be a poor investment at an excessive price|545355|
Siemens Healthineers|H02|Germany|Imaging installed base and clinical workflow integration|Hospital data rights and reimbursement constrain capture|544354|
Medtronic|H02|Ireland|Device installed base and procedure-specific expertise|Regulatory execution and product quality may overwhelm workflow gains|434354|
Intuitive Surgical|H02|United States|Surgical platform, instruments and procedure ecosystem|Procedure data rights, clinical evidence and competing platforms|545355|
Thermo Fisher Scientific|H03|United States|Laboratory tools, consumables and service relationships|Customers may own the useful data and retain the productivity gain|444455|
Danaher|H03|United States|Diagnostics and life-science instrument workflows|End-market recovery can masquerade as structural productivity|444455|
IQVIA|H03|United States|Healthcare data assets and clinical-research operations|Restrictions on data use and sponsor procurement pressure|544354|
HCA Healthcare|H04|United States|Hospital operations and clinical capacity|Labor, reimbursement and care quality may absorb benefits|334352|
UnitedHealth Group|H04|United States|Care and insurance workflows across a complex organization|Clinical, governance and reimbursement risks demand a separate review|444352|
Munich Re|F01|Germany|Reinsurance exposure history, underwriting and specialty risk expertise|Tail events are sparse and historical correlations can fail|544255|
Swiss Re|F01|Switzerland|Global reinsurance portfolios and risk-modeling experience|Shared industry models can erode differentiation|544254|
Allianz|F01|Germany|Insurance distribution and diversified claims books|Complex integration and repricing may consume savings|444354|
Chubb|F01|Switzerland|Commercial insurance underwriting and claims expertise|Hard-market pricing must be separated from AI risk selection|544354|
Progressive|F01|United States|Auto claims and telematics-related pricing experience|Competitors and regulation can narrow incremental pricing advantage|555454|
AIA Group|F02|Hong Kong|Asian life-insurance distribution and policy relationships|Long-duration claims labels and regional regulation|434253|
BlackRock|F02|United States|Investment workflows, client distribution and Aladdin platform|Markets lift assets independently of AI and fee pressure persists|444355|
Manulife|F02|Canada|Life insurance and wealth-service customer relationships|Legacy systems and market-sensitive earnings|334253|
JPMorgan Chase|F03|United States|Deposit distribution, transaction history and credit outcomes|Credit cycles and funding costs can swamp measured AI gains|544454|S09
DBS Group|F03|Singapore|Integrated regional banking and digital workflows|Concentrated geographic and credit exposures|444454|
ICICI Bank|F03|India|Retail banking distribution and digital transactions|Rapid credit growth can hide vintage risk|444453|
Visa|F04|United States|Network fraud signals and merchant-issuer connectivity|Account-to-account alternatives and fee regulation|555455|S10
Mastercard|F04|United States|Payment network and risk-service relationships|Alternative rails and service commoditization|555455|
Adyen|F04|Netherlands|Merchant payments integration and cross-channel transaction context|Merchant concentration and pricing competition|444454|
S&P Global|F05|United States|Ratings, benchmarks, financial data and analytical workflows|Public data and licensing costs can limit proprietary advantage|544355|
Moody's|F05|United States|Credit expertise and analytics relationships|Credit issuance cycles and model commoditization|544355|
Experian|F05|Ireland|Consumer and business credit files and decision workflows|Consent, fairness and data portability constrain exclusivity|555454|
London Stock Exchange Group|F05|United Kingdom|Market data, benchmarks and financial workflow distribution|Supplier licensing and platform integration costs|544355|
Intercontinental Exchange|F05|United States|Exchange, data and mortgage workflow infrastructure|Financial cycles and uneven segment-level capture|544355|
RELX|I01|United Kingdom|Enriched professional content and decision workflows|Generic agents may weaken seats while trusted content retains value|554455|S04
Wolters Kluwer|I01|Netherlands|Tax, clinical and compliance content embedded in expert tools|Tenant data restrictions and willingness to pay for AI add-ons|544455|S06
Thomson Reuters|I01|Canada|Legal and tax content with verification and workflow tools|Customer content is not available for a pooled training flywheel|544455|S05
Intuit|I02|United States|Accounting, tax and small-business transaction workflows|Seat substitution, competition and support costs of autonomous work|554454|S07
Veeva Systems|I02|United States|Life-sciences commercial and development software workflows|Customer data rights and transition execution|544454|
Constellation Software|I02|Canada|Portfolio of niche vertical software customer relationships|Decentralized products vary widely in AI readiness and exposure|434454|
ADP|I02|United States|Payroll, employer distribution and regulatory workflows|Error liability and pricing of automated administration|444454|
SAP|I03|Germany|Enterprise processes, permissions and systems of record|Third-party agents could capture the user relationship|544455|S08
ServiceNow|I03|United States|Service workflows, permissions and enterprise integrations|AI spend may substitute for seats or invite competing orchestration|444455|
Salesforce|I03|United States|Customer workflows and installed CRM distribution|Customer-owned data and seat cannibalization|444454|
Synopsys|I04|United States|Chip design, verification and engineering toolchains|Compute cost, integration complexity and customer IP restrictions|554455|S16
Cadence Design Systems|I04|United States|Design and verification toolchains and solver expertise|Pricing may not capture all customer engineering savings|554455|
Dassault Systèmes|I04|France|Engineering workflows and digital product models|Complex implementations and customer data permissions|444454|
Autodesk|I04|United States|Design files, creation workflows and professional distribution|Agents may reduce seat demand and software differentiation|444454|
TSMC|I05|Taiwan|Process expertise, yield learning and foundry customer relationships|Geopolitical concentration and capital intensity|554354|
ASML|I05|Netherlands|Lithography systems, installed-base service and engineering know-how|Export constraints and customer capital-spending cycles|544354|
Applied Materials|I05|United States|Process equipment and service relationships|Cyclicality and restricted customer process data|444354|
KLA|I05|United States|Inspection and metrology workflows|Node transitions and customer capex confound productivity claims|554454|
Microsoft|I06|United States|Enterprise distribution, cloud and developer ecosystem|Compute spending, cannibalization and returns on AI infrastructure|554455|
Amazon|I06|United States|Cloud, retail fulfillment and operating feedback|Retail productivity and cloud AI capital returns must be separated|555455|S21
Alphabet|I06|United States|Search distribution, advertising feedback and cloud infrastructure|AI may cannibalize profitable search while adding compute cost|555454|
Accenture|I07|Ireland|Enterprise relationships and transformation delivery expertise|Fewer billable hours and client insourcing|334452|
Tata Consultancy Services|I07|India|Large delivery organization and customer process knowledge|Labor-arbitrage economics may weaken as coding automates|334452|
Palo Alto Networks|I08|United States|Security platform distribution and threat-response workflows|Bundling, integration and AI-enabled attacks|454454|
CrowdStrike|I08|United States|Endpoint telemetry and security operations workflows|Correlated service failures and adversarial adaptation|455454|S22
Siemens|D01|Germany|Industrial controls, engineering software and installed equipment|Customer integration costs and data access limit scale|544454|S20
Schneider Electric|D01|France|Power-management installed base and industrial software channels|AI infrastructure demand can obscure actual operating productivity|444454|
ABB|D01|Switzerland|Electrification and automation installed base|Business perimeter and customer deployment vary by division|444454|
Deere|D02|United States|Agricultural machines, dealer distribution and field workflows|Farm economics, interoperability and paid adoption|554454|
Caterpillar|D02|United States|Equipment fleets, dealers and service relationships|Commodity cycles and customer-owned operational data|444354|
Komatsu|D02|Japan|Construction and mining machinery and fleet knowledge|Hardware cycles and difficult field validation|444354|
DHL Group|D03|Germany|Shipment networks and route-level operating knowledge|Price competition and labor contracts pass savings through|444453|
UPS|D03|United States|Parcel network density and delivery history|Volume changes and labor costs dominate unit economics|444453|
Canadian National Railway|D03|Canada|Rail network and maintenance records|Safety constraints and traffic mix limit automation|434353|
Safran|D04|France|Civil engine and aircraft-equipment service knowledge|Long-tail engineering liabilities and certification|544254|
GE Aerospace|D04|United States|Engine fleet and service contract experience|Lower maintenance may reduce billable work under some contracts|544254|
Waste Management|D05|United States|Local route density, disposal assets and commercial contracts|Automation capex and municipal repricing|434353|
Cintas|D05|United States|Recurring service routes and customer relationships|Much of the work remains physical and labor-intensive|333353|
Linde|M01|United States|Industrial gas process plants and long customer contracts|Contract pass-through and energy prices determine retention|444354|
BASF|M01|Germany|Chemical processes, formulation knowledge and integrated plants|Commodity exposure and energy disadvantage can overwhelm AI|434352|
dsm-firmenich|M01|Switzerland|Nutrition, fragrance and formulation expertise|Integration, customer qualification and changing business perimeter|444354|
Rio Tinto|M02|United Kingdom|Orebody knowledge and large mining operations|Grade, commodity prices and project execution dominate|434353|
BHP|M02|Australia|Resource assets and processing operations|Commodity cycles, royalties and sustaining capital|434353|
Alibaba|C01|China|Commerce distribution, merchants and operating data|Governance, competition and regulatory constraints|544454|
MercadoLibre|C01|Uruguay|Commerce, logistics and payment relationships|Credit losses, currency and subsidized growth|555454|
Inditex|C01|Spain|Merchandising, store network and inventory feedback|Brand demand and inventory discipline may explain gains without AI|444454|
Uber|C02|United States|Mobility demand, matching and driver-market density|Autonomous fleet owners or agents may capture economics|554454|
Booking Holdings|C02|United States|Travel demand, supplier relationships and conversion history|AI agents may bypass discovery and reduce commissions|544454|
Amadeus IT Group|C02|Spain|Travel reservations and airline operating workflows|Airline bargaining power and distribution change|544454|
Toyota Motor|C03|Japan|Manufacturing knowledge and global service network|Product mix, EV competition and software execution|434353|
BMW|C03|Germany|Premium vehicles, engineering and manufacturing knowledge|Geographic competitiveness and price pressure can outweigh savings|434352|
Nike|C04|United States|Brand, product archive and distribution|Brand relevance and channel strategy overwhelm generic AI tools|333353|
LVMH|C04|France|Scarce brands, design history and customer relationships|AI content may dilute scarcity and luxury demand remains cyclical|333354|
Unilever|S01|United Kingdom|Brands, formulations and distribution|Retailer bargaining and promotions absorb savings|434353|
Nestlé|S01|Switzerland|Food research, brands and manufacturing networks|Product execution and input prices dominate small AI gains|434353|
Procter & Gamble|S01|United States|Consumer brands, process knowledge and retail distribution|Savings may flow into trade spending and price competition|434354|
Walmart|S02|United States|Store network, purchase data and fulfillment capacity|Low-price strategy intentionally shares productivity with customers|555453|S11
Costco|S02|United States|Membership and warehouse distribution|Deliberate low markups limit direct margin capture|433453|
Deutsche Telekom|T01|Germany|Network infrastructure and subscriber relationships|Tariff competition, subsidiaries and regulation dilute capture|434353|
Singtel|T01|Singapore|Regional connectivity and enterprise relationships|Business mix and affiliated operators complicate attribution|334353|
Meta Platforms|T02|United States|Audience distribution and advertising feedback|Ad saturation, privacy and growing compute costs|555454|
Netflix|T02|United States|Audience relationships and viewing feedback|Content economics and creative quality dominate recommendation gains|444454|
Shell|E01|United Kingdom|Energy assets, subsurface knowledge and operating history|Commodity prices and capital allocation dominate outcomes|434353|
SLB|E01|United States|Subsurface workflows and energy-service relationships|Customers may retain AI savings through contract repricing|444354|
Iberdrola|U01|Spain|Grid, renewable assets and operating data|Regulatory sharing and capital requirements limit retained gains|434352|
Prologis|R01|United States|Logistics property locations and tenant relationships|Lease structure can transfer energy savings to tenants|333352|
CBRE Group|R02|United States|Facilities workflows and property-service relationships|Client data rights and property cycles obscure AI profit|434453|S13
'''
DIMENSIONS=['asset','ai_leverage','feedback','testability','distribution','capture']
WEIGHTS=[20,20,15,10,15,20]
AM={a['id']:a for a in AREAS}
PRIORITY=['RELX','Wolters Kluwer','Thomson Reuters','Experian','Intuit','SAP','Siemens','Schneider Electric','Munich Re','Chubb','Visa','JPMorgan Chase','Sanofi','Roche','AstraZeneca','Linde','Deere','Amazon']
DIRECT_STAGE={'S03':'E1','S04':'E2','S05':'E1','S06':'E1','S07':'E1','S08':'E2','S09':'E2','S10':'E1','S11':'E2','S13':'E1','S16':'E1','S20':'E2','S21':'E1','S22':'E1'}
SECONDARY={'Amazon':'C01;D03','Alphabet':'T02','Microsoft':'I03','RELX':'F05;H03','Wolters Kluwer':'H02;I02','Roche':'H02','Schneider Electric':'I04;U01','Siemens':'I04','BlackRock':'I02','Alibaba':'I06','MercadoLibre':'F04','UnitedHealth Group':'F01','Linde':'E01','Deere':'I03','Amadeus IT Group':'I02'}
DEBATES={
'RELX':('Does a publisher-style valuation underweight paid decision workflows?','AI revenue per legal customer after seat and bundle changes','Thomson Reuters and specialist legal agents'),
'Wolters Kluwer':('Does fear of generic answers underweight regulated workflow depth?','Paid renewals and contribution after inference and expert review','Thomson Reuters, Intuit and new workflow agents'),
'Thomson Reuters':('Does content scarcity translate into revenue despite fewer research seats?','Customer-level bill and retention after CoCounsel deployment','RELX and legal AI entrants'),
'Experian':('Does the price reward data ownership without reflecting better decision services?','Marginal lift of proprietary attributes over lawful alternative data','Other credit bureaus and lender-built models'),
'Intuit':('Can automated bookkeeping expand customer value faster than it erodes software pricing?','Net customer spend and verified completed work after support costs','Xero, accountants using generic agents and tax alternatives'),
'SAP':('Does system-of-record control retain value when agents own the interface?','Incremental gross profit from completed agent workflows','Oracle and independent agent orchestration'),
'Siemens':('Does a cyclical hardware valuation omit recurring workflow economics?','Paid deployment across customers and software contribution margin','ABB, Schneider and independent industrial software'),
'Schneider Electric':('How much valuation already reflects AI infrastructure demand?','Separate internal productivity and recurring services from equipment demand','Siemens and independent energy optimization vendors'),
'Munich Re':('Can better risk selection add value beyond the reinsurance pricing cycle?','Accident-year and reserve-adjusted underwriting outcomes','Swiss Re, brokers and shared catastrophe models'),
'Chubb':('Can commercial underwriting expertise keep AI gains through renewals?','Cohort loss and expense ratios at equal risk mix','Other commercial carriers using common tools'),
'Visa':('Can AI risk services add profit beyond an already valued network moat?','Fraud and approval lift with net service fees','Mastercard, processors and account-to-account providers'),
'JPMorgan Chase':('Does scale deliver additional cash earnings after AI reinvestment?','Cost and credit performance normalized for funding and risk appetite','DBS, large US banks and focused fintechs'),
'Sanofi':('Does a traditional pharma valuation give little credit to a more productive R&D engine?','Prospective clinical cohort success and stage-adjusted R&D output','Roche, AstraZeneca and AI-native discovery platforms'),
'Roche':('Can diagnostic and research capabilities reinforce each other under actual data rights?','Evidence of permissible linkage and improved trial stratification','Sanofi, AstraZeneca and independent diagnostic platforms'),
'AstraZeneca':('Does pipeline strength leave any unpriced productivity upside?','Clinical productivity after controlling for oncology mix and acquisitions','Roche, Sanofi and therapeutic-area peers'),
'Linde':('Do contract structures let shareholders keep process optimization savings?','Plant-level savings reconciled to contract pass-through','Air Liquide and customer-led process optimization'),
'Deere':('Will farmers repeatedly pay for measured input and labor savings?','Renewal, customer payback and outcomes over full seasons','CNH, retrofit vendors and open farm software'),
'Amazon':('Are retail productivity improvements obscured by cloud AI capital spending?','Segment-level cash returns and cost per fulfilled unit','Walmart in retail, cloud peers in infrastructure'),
}

def build():
    build_areas()
    companies=[]
    for n,line in enumerate(DATA.strip().splitlines(),1):
        name,area,market,asset,risk,scores,sids=line.split('|')
        a=AM[area]; vals=list(map(int,scores)); assert len(vals)==6
        score=sum(v*w/5 for v,w in zip(vals,WEIGHTS))
        stage=DIRECT_STAGE[sids] if sids else 'E0'
        c=dict(id=f'C{n:03}',company=name,primary_area=area,secondary_areas=SECONDARY.get(name,''),home_market=market,
            research_group=a['sector'],asset_hypothesis=asset,ai_use_case=a['mechanism'],feedback_hypothesis=a['asset']+' outcomes can improve decisions only if reusable rights and labels exist.',
            principal_risk=risk,proof_kpi=a['kpi'],evidence_stage=stage,company_source_ids=sids,
            source_scope='company-specific description' if sids else 'no company-specific source reviewed',
            evidence_confidence='limited' if sids else 'low',score_kind='analyst structural prior; not evidence-validated',
            structural_prior=round(score,1),**dict(zip(DIMENSIONS,vals)),
            valuation_status='NOT_ASSESSED',valuation_date='',price='',fair_value='',valuation_score='',
            diligence_priority='P1' if name in PRIORITY else 'P2',investable_status='RESEARCH_ONLY',as_of=DATE)
        companies.append(c)
    assert len(companies)==100
    assert len({c['company'] for c in companies})==100
    fields=list(companies[0])
    with (ROOT/'universe/companies.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(companies)
    write('universe/companies.json',json.dumps(companies,indent=2,ensure_ascii=False)+'\n')
    # Dimension-level rationales distinguish every prior from observed proof.
    reasons=[]
    for c in companies:
        a=AM[c['primary_area']]
        r={
            'asset':c['asset_hypothesis']+'. Verify exclusivity and practical reuse.',
            'ai_leverage':a['mechanism']+' Incremental financial materiality remains unmeasured.',
            'feedback':a['asset']+'. Useful outcome labels and lawful learning rights remain to be verified.',
            'testability':a['experiment'],
            'distribution':c['asset_hypothesis']+'. Verify the share of eligible workflows reachable through existing channels.',
            'capture':a['capture']+' Company-specific risk: '+c['principal_risk']+'.',
        }
        for d,w in zip(DIMENSIONS,WEIGHTS):
            reasons.append(dict(company_id=c['id'],company=c['company'],dimension=d,prior=c[d],weight=w,rationale=r[d],status='HYPOTHESIS',source_ids=c['company_source_ids']))
    with (ROOT/'universe/score-rationales.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(reasons[0]));w.writeheader();w.writerows(reasons)
    rows=[]
    for c in companies:
        rows.append(f"| {c['id']} | {c['company']} | {c['primary_area']} | {c['home_market']} | {c['structural_prior']:.0f} | {c['evidence_stage']} | {c['diligence_priority']} |")
    counts=Counter(c['evidence_stage'] for c in companies)
    write('universe/README.md',f'''# Initial candidate universe

**100 companies · 36 primary research areas · 11 broad sectors · {DATE}**

This is the stage-one universe requested in the source brief. Every name is a research candidate. None has passed the valuation gate. Company names identify businesses, not an executable securities list. Share classes, listings, issuer domicile, investability and corporate actions require verification during diligence. Home market is descriptive and does not represent revenue exposure.

## How to read the scores

The 0–100 structural prior organizes hypotheses. It is an analyst judgment about potential, not a measured quality score, probability, target return or buy signal. All six dimensions have written rationales in [score-rationales.csv](score-rationales.csv). Company-specific source coverage is deliberately separate. E0 means no direct company evidence was reviewed. An empty valuation field means unknown, never zero or cheap.

Source stages: {', '.join(f'{k}: {v}' for k,v in sorted(counts.items()))}. There are no E3 or E4 claims. Product descriptions and management statements support the researched leads but do not establish durable incremental profit. Most names are structural hypotheses awaiting primary-source work.

The 18 P1 names maximize information gained across mechanisms. Their priority is not an expected-return ranking and does not imply that other names are lower quality. Shared industry risks still create concentration even when sector labels differ.

| ID | Company | Area | Home market | Structural prior /100 | Evidence | Queue |
|---|---|---|---|---:|---|---|
'''+ '\n'.join(rows)+'\n\n## Downloads and next gate\n\n- [Full CSV](companies.csv)\n- [Full JSON](companies.json)\n- [18-company diligence queue](../research/priority-queue.md)\n- [Scoring definitions](../framework/scoring.md)\n- [Valuation protocol](../framework/valuation.md)\n')
    qrows=[]
    for rank,name in enumerate(PRIORITY,1):
        c=next(c for c in companies if c['company']==name);a=AM[c['primary_area']]
        debate,proof,challenger=DEBATES[name]
        path='research/companies/'+c['id'].lower()+'.md'
        src='\n'.join(f"- [{SM[s]['title']}]({SM[s]['url']}): {SM[s]['claim']} {SM[s]['limitation']}" for s in c['company_source_ids'].split(';') if s)
        if not src: src='No company-specific source has yet been reviewed. The asset and advantage statements below are research hypotheses. Obtain the latest annual report, relevant results and a direct product or deployment source before changing this status.'
        write(path,f'''# {name}: initial diligence brief

**ID:** {c['id']} · **Area:** [{a['name']}](../../{a['path']}) · **Evidence:** {c['evidence_stage']} · **Status:** research only

## Thesis to test

{c['asset_hypothesis']}. {a['mechanism']}

## Valuation debate

{debate} This is a question to investigate, not a claim about the current share price. Price, consensus, valuation and expected return have not been assessed.

## Observed evidence

{src}

## Decisive evidence request

{proof}. Require production scope, baseline, comparison group and a bridge to cash earnings. Compare the same task against {challenger}. Quantify whether the incumbent's unique assets improve the result after accounting for model access and total cost.

## Principal risk and disconfirmation

{c['principal_risk']}. Area-level falsifier: {a['falsifier']}.

## Provisional assessment

Structural prior: **{c['structural_prior']:.0f}/100**, entirely a hypothesis rather than a validated result. Asset {c['asset']}/5, AI leverage {c['ai_leverage']}/5, feedback {c['feedback']}/5, testability {c['testability']}/5, distribution {c['distribution']}/5, capture {c['capture']}/5. See [dimension rationales](../../universe/score-rationales.csv).

Management execution, data usability and financial resilience require separate evidence. Current downside valuation and AI contribution remain unknown. Confidence is low in a purchase decision until these gaps close.

## Next research packet

1. Latest annual report and results, segment economics, capital allocation and relevant material developments.
2. Data rights, independent customer evidence and competitor task comparison.
3. KPI history and matched baseline, including failed deployments.
4. Conventional-business valuation with zero incremental AI benefit, followed by explicit AI scenarios and a reverse valuation.

Use [the full memo template](../../framework/company-memo-template.md) to advance this brief. A favorable outcome would create an eligible investment candidate, not automatically authorize a trade.
''')
        qrows.append(f"| {rank} | [{name}](companies/{c['id'].lower()}.md) | {c['evidence_stage']} | {debate} | {proof} |")
    write('research/priority-queue.md','# First 18 diligence questions\n\nThis queue tests whether productivity optionality is underpriced. It does not assert that any of these companies is currently cheap. P1 selection balances content/workflow, risk decisions, physical operations and scientific discovery. Sequence within the queue is a research order, not a portfolio allocation.\n\n| Order | Company | Evidence | Valuation question | Decisive proof |\n|---:|---|---|---|---|\n'+'\n'.join(qrows)+'\n')
    write('universe/statistics.json',json.dumps(dict(companies=len(companies),areas=len(AREAS),sectors=len({a['sector'] for a in AREAS}),priority_count=len(PRIORITY),evidence=dict(counts),sector_counts=dict(Counter(c['research_group'] for c in companies))),indent=2)+'\n')
    print(json.dumps(dict(companies=len(companies),areas=len(AREAS),priority=len(PRIORITY),evidence=dict(counts))))

if __name__=='__main__': build()
