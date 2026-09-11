import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {Presentation, PresentationFile} from '@oai/artifact-tool';

const {REPO_DIR, TMP_DIR, SKILL_DIR, RUNTIME_PYTHON} = process.env;
for (const x of [REPO_DIR,TMP_DIR,SKILL_DIR,RUNTIME_PYTHON]) if (!path.isAbsolute(x||'')) throw Error('Set absolute runtime and build paths.');
const {resolvePresentationFont,applyPresentationChartFont,finalizePresentation}=await import(pathToFileURL(path.join(SKILL_DIR,'container_tools/artifact_tool_utils.mjs')));
const family=resolvePresentationFont({fontFamily:'Nimbus Sans'});
const P=Presentation.create({slideSize:{width:1280,height:720}});
const C={ink:'#14191B',paper:'#F3F0E8',white:'#FCFBF7',muted:'#626A6B',gold:'#C6A66A',light:'#B9C0BE',green:'#527D70'};
const sources=JSON.parse(await fs.readFile(path.join(REPO_DIR,'sources/source-register.json'),'utf8'));
const stats=JSON.parse(await fs.readFile(path.join(REPO_DIR,'universe/statistics.json'),'utf8'));
const noteText=[];
function text(s,t,x,y,w,h,size=28,color=C.ink,bold=false){
  const q=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
  q.text=t;q.text.style={typeface:family,fontSize:size,color,bold,autoFit:'none',verticalAlignment:'top'};
  return q;
}
function slide(title,{dark=false,subtitle='',notes='',refs=[]}={}){
  const s=P.slides.add();s.background.fill=dark?C.ink:C.paper;
  const n=P.slides.items.length;
  text(s,title,70,58,1130,114,47,dark?C.white:C.ink,true);
  if(subtitle) text(s,subtitle,72,170,1110,74,25,dark?C.light:C.muted);
  text(s,String(n).padStart(2,'0'),1175,665,40,28,17,dark?C.light:C.muted);
  const src=refs.map(id=>sources.find(s=>s.id===id)).filter(Boolean).map(r=>`${r.id}: ${r.title}. ${r.url} Published ${r.published}. Accessed ${r.accessed}. ${r.limitation}`).join('\n');
  const nt=notes+'\n\n'+src;
  s.speakerNotes.textFrame.setText(nt);
  noteText.push({n,title,notes:nt});return s;
}
function table(s,headers,rows,{x=72,y=250,w=1136,h=330,widths,size=25}={}){
  const vals=[headers,...rows],t=s.tables.add({rows:vals.length,columns:headers.length,left:x,top:y,width:w,height:h,values:vals,columnWidths:widths});
  t.styleOptions={headerRow:false,bandedRows:false};
  t.borders.assign({fill:'#D2D2C9',width:0.65,style:'solid'});
  for(let r=0;r<vals.length;r++){
    t.rows[r].height=r===0?50:(h-50)/rows.length;
    for(let c=0;c<headers.length;c++){
      const cell=t.getCell(r,c);cell.fill=r===0?C.ink:C.paper;
      cell.text.style={typeface:family,fontSize:r===0?20:size,color:r===0?C.white:C.ink,bold:r===0};
    }
  }
  return t;
}
function pair(s,label,body,y,{dark=false}={}){
  text(s,label,74,y,370,70,30,dark?C.gold:C.green,true);
  text(s,body,474,y,706,88,27,dark?C.white:C.ink);
}

// 1: editorial cover, with native editable foreground text.
{
 const s=P.slides.add();s.background.fill=C.ink;
 s.images.add({blob:new Uint8Array(await fs.readFile(path.join(REPO_DIR,'deck/assets/incumbent-cover.jpg'))),contentType:'image/jpeg',alt:'Conceptual illustration of an archive beside industrial equipment',fit:'cover',position:{left:0,top:0,width:1280,height:720}});
 text(s,'THE INCUMBENT\nADVANTAGE',72,180,670,225,73,C.white,true);
 text(s,'AI can make scarce business\nassets more productive',76,430,640,96,31,C.light);
 text(s,'Ryan Matthews\nInvestment research thesis · September 2026',76,607,760,63,20,C.light);
 const notes='Original investment hypothesis developed from the supplied AI Incumbent Productivity Regime. No affiliation, endorsement, track record or investment return is claimed. Cover is a generated conceptual illustration, not a real company facility. Research version 0.1.';
 s.speakerNotes.textFrame.setText(notes);noteText.push({n:1,title:'The incumbent advantage',notes});
}
{
 const s=slide('Abundant intelligence can make\nscarce assets more valuable',{dark:true,notes:'Central hypothesis, not an established law. If model access becomes widespread, complementary assets can become a source of differentiated returns. Counter-hypothesis: model commoditization lowers entry barriers and reduces incumbent rents.'});
 text(s,'The model is available to many firms.',74,257,1090,64,38,C.light);
 text(s,'The clinical history, customer relationship\nand installed network may take decades to build.',74,348,1110,128,39,C.white,true);
 text(s,'The investment question is who converts those assets into retained cash earnings.',74,565,1110,76,28,C.gold);
}
{
 const s=slide('Four paths to better economics',{subtitle:'Each path starts with an existing asset and ends with a testable operating result.',notes:'These are analytical archetypes derived from the supplied regime. They are proposed mechanisms, not forecasts for all firms.'});
 pair(s,'Better decisions','More profitable transactions and underwriting at the same risk',264);
 pair(s,'Scientific throughput','More clinically useful output per research euro',358);
 pair(s,'Work inside the workflow','More completed tasks from trusted content and systems of record',452);
 pair(s,'Physical productivity','Higher useful output from existing equipment and networks',546);
}
{
 const s=slide('Productivity depends on the task',{subtitle:'Evidence supports careful measurement. It does not support a universal uplift.',refs:['S01','S02','S18'],notes:'S01 revised November 2024: 5,172 customer support agents, 15% average increase in issues resolved per hour. METR July 2025 randomized trial: 16 experienced developers and 246 tasks, 19% more completion time with early-2025 tools. Different samples, tasks and outcome measures. The February 2026 follow-up suggests newer tools may help more, but selection and timing problems prevent a clean current estimate. Neither study measures shareholder capture.'});
 table(s,['Setting','Observed result','Investment implication'],[
 ['Customer support\n5,172 agents','15% more issues\nresolved per hour','Some workflows can\nproduce more useful output'],
 ['Experienced developers\nEarly-2025 tools','19% longer\ntask completion time','Review and context costs\ncan offset assistance'],
 ['METR 2026 follow-up','Selection bias obscures\nthe current effect','Historical results need\nretesting with current tools']
 ],{y:260,h:335,widths:[360,335,441],size:26});
 text(s,'Different tasks and metrics. Neither result establishes a company-wide profit gain.',74,626,1110,34,20,C.muted);
}
{
 const s=slide('Pharma: better choices before\nexpensive clinical failures',{subtitle:'Sanofi, Roche and AstraZeneca are research candidates for a more productive R&D engine.',refs:['S03'],notes:'The Sanofi source describes AI methods for discovery and clinical data integration, updated September 2023. No claim is made that any named company has demonstrated better Phase II/III success from AI. The Roche and AstraZeneca references are candidate hypotheses, not sourced deployment conclusions. Sources of advantage require rights, usable historical failures and prospective validation.'});
 pair(s,'Scarce asset','Experimental history plus the ability to run new science',275);
 pair(s,'AI mechanism','Better selection, earlier rejection and sharper patient stratification',386);
 pair(s,'Proof that matters','Stage-adjusted clinical success and R&D output after full cost',497);
 text(s,'Clinical validation remains the bottleneck. More candidates alone are weak evidence.',74,627,1115,34,20,C.muted);
}
{
 const s=slide('Trusted content can support\nmore valuable professional work',{subtitle:'The opportunity is paid task completion inside established customer workflows.',refs:['S04','S05','S06'],notes:'RELX describes Protégé in its 2025 annual report. Thomson Reuters and Wolters Kluwer offer AI-enabled professional tools. Product descriptions do not establish net profit. Thomson Reuters says customer content and prompts are not used to train or improve CoCounsel or underlying models. Separate content ownership, customer context and pooled learning rights.'});
 table(s,['Candidate','Potential advantage','Decisive test'],[
 ['RELX','Enriched content and\ncitation-aware workflows','Revenue per customer\nafter seat substitution'],
 ['Thomson Reuters','Legal and tax content\ninside CoCounsel','Paid renewals and\nnet contribution'],
 ['Wolters Kluwer','Domain knowledge inside\nexpert workflows','Completed work at\nequal accuracy']
 ],{y:270,h:315,widths:[265,430,441],size:26});
 text(s,'Data access does not automatically confer cross-customer training rights.',74,625,1100,35,21,C.green,true);
}
{
 const s=slide('Physical assets create a second\nroute to productivity',{dark:true,subtitle:'Existing deployment channels connect better software to real operating work.',refs:['S20','S21'],notes:'Siemens May 2025 release describes available industrial copilots and customer implementations. Its headline productivity ambition is not an achieved result. Amazon describes DeepFleet for robot coordination. Siemens reports customer use. Amazon announces the new model. Neither source establishes controlled evidence of consolidated profit.'});
 text(s,'Siemens',74,279,440,58,37,C.gold,true);
 text(s,'Controls and engineering workflows\ncan distribute AI across a plant.',74,365,510,118,30,C.white);
 text(s,'Amazon',698,279,450,58,37,C.gold,true);
 text(s,'Fulfillment networks generate\noperating feedback at scale.',698,365,500,118,30,C.white);
 text(s,'The proof is useful output after integration, capital expenditure and human oversight.',74,582,1115,66,27,C.light);
}
{
 const s=slide('Task savings can shrink before\nthey reach shareholders',{subtitle:'Illustrative operating profit, starting at 20 monetary units. These are assumptions, not forecasts.',notes:'Derived from framework/valuation.md. Revenue 100, cost 80, operating profit 20, eligible cost 40 and recurring AI expense 1. Net benefit = eligible cost × task efficiency × realization × retained share − recurring expense. Weak capture: .15 × .40 × .25 gives profit 19.6. Central: .15 × .60 × .50 gives 20.8. Strong: .25 × .80 × .75 gives 25.0. Incremental capital spending and tax are not included in this operating-profit illustration. They must be added in a valuation.'});
 const ch=s.charts.add('bar',{position:{left:74,top:267,width:680,height:350},categories:['Starting profit','Weak capture','Central case','Strong capture'],series:[{name:'Operating profit',values:[20,19.6,20.8,25],fill:C.green,points:[{idx:0,fill:'#9BA5A0'},{idx:1,fill:'#BC7B63'},{idx:3,fill:C.gold}],valuesFormatCode:'0.0'}],barOptions:{direction:'column',grouping:'clustered',gapWidth:75},hasLegend:false,xAxis:{textStyle:{fontSize:20,typeface:family,fill:C.ink},line:{fill:'#BBBDB6',width:1}},yAxis:{min:0,max:30,majorUnit:10,numberFormatCode:'0',textStyle:{fontSize:18,typeface:family,fill:C.muted},majorGridlines:{fill:'#D6D7CE',width:0.5}},dataLabels:{showValue:true,position:'outEnd',textStyle:{fontSize:26,typeface:family,fill:C.ink,bold:true}},chartFill:C.paper,plotAreaFill:C.paper});
 applyPresentationChartFont(ch,{fontFamily:family});
 text(s,'Central illustration',815,282,375,40,24,C.green,true);
 text(s,'15% task efficiency\n60% realization\n50% retained share',815,340,380,150,29,C.ink);
 text(s,'4% profit increase\nafter recurring AI cost',815,525,380,90,30,C.ink,true);
 text(s,'Assumptions: revenue 100, eligible cost 40, recurring AI expense 1.',74,630,1100,34,20,C.muted);
}
{
 const s=slide('The contract determines\nwho keeps the gain',{subtitle:'A stronger operating result becomes an investment advantage only when value stays with the business.',notes:'These capture mechanisms are analytical hypotheses. Contract-level diligence is mandatory. The table does not claim actual pass-through percentages.'});
 table(s,['Business model','Potential retention','Main leakage'],[
 ['Professional software','Paid workflows and renewal','Seat loss and model costs'],
 ['Insurance','Risk selection and lower expenses','Renewal pricing and reserves'],
 ['Industrial services','Availability and service contracts','Customer-owned data and capex'],
 ['Regulated utilities','Incentive sharing where allowed','Rate resets and required investment'],
 ['Hourly IT services','More projects or outcome pricing','Fewer billable hours']
 ],{y:264,h:342,widths:[285,428,423],size:23});
}
{
 const s=slide('A global universe built\nfrom explicit industry theses',{dark:true,notes:'Counts generated from universe/statistics.json and the 100-company register. All 11 broad equity sectors have coverage. Research groupings are not official GICS classifications. There are 86 E0 names, 9 E1 and 5 E2 at initial release. No E3/E4 or completed valuations. Breadth is not evidence of diversification.'});
 text(s,String(stats.companies),74,250,430,142,115,C.white,true);
 text(s,'company candidates',78,410,430,60,30,C.light);
 text(s,String(stats.areas),598,250,240,142,115,C.gold,true);
 text(s,'research areas',602,410,290,60,30,C.light);
 text(s,String(stats.sectors),958,250,235,142,115,C.gold,true);
 text(s,'broad sectors',962,410,260,60,30,C.light);
 text(s,'14 names have direct company-source coverage.\n86 begin as structural hypotheses. All valuations remain open.',78,553,1115,92,26,C.light);
}
{
 const s=slide('The first 18 diligence targets',{subtitle:'A research queue chosen to test different mechanisms. No current buy ratings or weights.',notes:'Derived from research/priority-queue.md. These names are chosen for information gain across mechanisms, not a claimed expected-return rank. Company-specific source coverage and evidence stage are visible in the repository. The initial queue does not establish undervaluation.'});
 table(s,['Mechanism','Candidates'],[
 ['Trusted workflows','RELX, Wolters Kluwer, Thomson Reuters,\nExperian, Intuit, SAP'],
 ['Risk decisions','Munich Re, Chubb, Visa, JPMorgan Chase'],
 ['Physical operations','Siemens, Schneider Electric, Linde, Deere, Amazon'],
 ['Scientific output','Sanofi, Roche, AstraZeneca']
 ],{y:275,h:325,widths:[290,846],size:27});
}
{
 const s=slide('The valuation question is\nwhat the price already requires',{subtitle:'The desired opportunity is a strong existing business with underappreciated incremental productivity.',notes:'No current security prices, consensus estimates, fair values or expected returns have been assessed. This slide states the valuation method and desired investment profile. Use a no-incremental-AI downside case, explicit adoption scenarios and reverse valuation. Avoid double counting pipeline, margin and multiple effects.'});
 pair(s,'Conventional business','Cash earnings and downside with no incremental AI benefit',272);
 pair(s,'Incremental productivity','Adoption, quality, retained economics and capital cost',381);
 pair(s,'Market expectations','The growth and margins implied by the current share price',490);
 text(s,'A low multiple is a question to investigate. It is not evidence that AI upside is free.',74,624,1115,40,21,C.muted);
}
{
 const s=slide('The strongest bear case\nis cheaper competition',{dark:true,notes:'Alternative hypothesis: commoditized intelligence lowers entry barriers, lets agents bypass incumbent interfaces, enables data portability, shifts surplus to consumers and suppliers, and raises verification costs. This is a core part of the investment thesis rather than a generic disclaimer.'});
 pair(s,'Agents bypass the interface','The incumbent becomes a low-price data or execution layer.',267,{dark:true});
 pair(s,'Data loses exclusivity','Portable or synthetic substitutes narrow the information gap.',375,{dark:true});
 pair(s,'Productivity passes through','Customers, employees or suppliers retain the benefit.',483,{dark:true});
 text(s,'A framework that calls every incumbent an AI winner has failed.',74,625,1115,36,25,C.gold,true);
}
{
 const s=slide('Conviction follows operating proof',{subtitle:'The thesis can be ambitious while the investment standard remains strict.',notes:'Current release completes G0 candidate architecture and a first research universe. G1 qualification, G2 operating evidence, G3 valuation and G4 portfolio review remain company-specific future work. No fund track record, return projection or capital allocation is presented.'});
 table(s,['Gate','Evidence that advances the candidate'],[
 ['Business quality','Durable economics, financial resilience and usable assets'],
 ['Operating advantage','Material deployment and a defensible comparison'],
 ['Economic capture','Incremental cash earnings after all relevant costs'],
 ['Valuation and portfolio','Adequate expected return with downside and overlap reviewed']
 ],{y:267,h:321,widths:[300,836],size:27});
 text(s,'The next decision: which companies pass these gates at an attractive price?',74,628,1120,36,25,C.green,true);
}
{
 const s=slide('AI productivity is an\nownership question',{dark:true,notes:'Closing statement of the investment hypothesis. No guarantee is implied. The programme seeks a future evidence-supported and price-sensitive shortlist, while this release supplies the industry framework, preliminary universe and research priorities.'});
 text(s,'Who owns the scarce asset?',76,282,1110,70,41,C.white);
 text(s,'Who can make it more productive?',76,377,1110,70,41,C.white);
 text(s,'Who keeps the economic gain?',76,472,1110,70,41,C.gold,true);
 text(s,'The research begins with 100 candidates.\nThe portfolio will depend on the answers.',76,593,1105,66,26,C.light);
}
{
 const s=slide('Evidence and research access',{subtitle:'Source links and qualifications accompany the relevant slides in speaker notes.',notes:'All 22 primary-source records, the original user-provided thesis and source brief, industry hypotheses, scoring definitions and research templates are in the repository. This deck summarizes a research programme and contains no audited fund performance or offer terms.'});
 text(s,'Research',74,263,270,54,30,C.green,true);
 text(s,'Brynjolfsson, Li and Raymond: Generative AI at Work\nMETR: 2025 randomized trial and February 2026 update',380,263,810,100,25,C.ink);
 text(s,'Company evidence',74,379,295,54,30,C.green,true);
 text(s,'Sanofi, RELX, Thomson Reuters, Wolters Kluwer,\nIntuit, SAP, JPMorganChase, Visa, Siemens and Amazon',380,379,810,104,25,C.ink);
 text(s,'Full repository',74,503,295,54,30,C.green,true);
 text(s,'github.com/Darainer/AI-incumbent-Portfolio',380,503,810,54,26,C.ink,true);
 text(s,'Version 0.1 · 11 September 2026 · Provisional research universe',74,625,1120,35,21,C.muted);
}

await fs.mkdir(TMP_DIR,{recursive:true});
const draft=path.join(TMP_DIR,'candidate.pptx');
await (await PresentationFile.exportPptx(P)).save(draft);
const final=path.join(REPO_DIR,'deck/AI-Incumbent-Portfolio.pptx');
await finalizePresentation({workspaceDir:path.dirname(REPO_DIR),candidatePath:draft,finalPath:final,pythonExecutable:RUNTIME_PYTHON,
 integrityValidatorPath:path.join(SKILL_DIR,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(SKILL_DIR,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...[4,6,9,11,14].flatMap(n=>['--require-native-table-slide',String(n)])],
 requiredNativeTableOwnerSlides:[4,6,9,11,14],requiredNativeChartOwnerSlides:[8],materializeLiteralChartWorkbooks:true,
 fontPolicy:{basis:'design',families:[family]},verifyArtifactToolImport:true,receiptPath:path.join(TMP_DIR,'validation.json')});
await fs.writeFile(path.join(REPO_DIR,'deck/speaker-notes.md'),'# Investor deck narrative\n\n'+noteText.map(q=>`## ${q.n}. ${q.title}\n\n${q.notes}`).join('\n\n')+'\n');
await fs.writeFile(path.join(TMP_DIR,'slide-copy.json'),JSON.stringify(noteText,null,2));
console.log(JSON.stringify({final,slides:P.slides.items.length,font:family}));
