"""Check release integrity, numeric priors, evidence gates and local links."""
from pathlib import Path
import csv,json,re,math
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
companies=json.loads((ROOT/'universe/companies.json').read_text())
areas=json.loads((ROOT/'industries/areas.json').read_text())
sources=json.loads((ROOT/'sources/source-register.json').read_text())
stats=json.loads((ROOT/'universe/statistics.json').read_text())
assert len(companies)==100 and len(areas)==36 and len(sources)==22
assert len({c['id'] for c in companies})==len({c['company'] for c in companies})==100
assert len({a['sector'] for a in areas})==11
ids={a['id'] for a in areas};sids={s['id'] for s in sources}
assert {c['primary_area'] for c in companies}==ids
for c in companies:
    for a in filter(None,c['secondary_areas'].split(';')): assert a in ids
    for s in filter(None,c['company_source_ids'].split(';')): assert s in sids
    nums=[c[x] for x in ['asset','ai_leverage','feedback','testability','distribution','capture']]
    assert all(isinstance(x,int) and 0<=x<=5 for x in nums)
    assert math.isclose(sum(x*w/5 for x,w in zip(nums,[20,20,15,10,15,20])),c['structural_prior'])
    assert c['valuation_status']=='NOT_ASSESSED' and c['investable_status']=='RESEARCH_ONLY'
    assert all(c[x]=='' for x in ['price','fair_value','valuation_score','valuation_date'])
    assert (c['evidence_stage']=='E0') == (c['company_source_ids']=='')
assert Counter(c['evidence_stage'] for c in companies)==stats['evidence']
assert sum(c['diligence_priority']=='P1' for c in companies)==18
with (ROOT/'universe/score-rationales.csv').open() as f:
    rationales=list(csv.DictReader(f))
assert len(rationales)==600 and all(r['rationale'] and r['status']=='HYPOTHESIS' for r in rationales)
assert len({(r['company_id'],r['dimension']) for r in rationales})==600
with (ROOT/'universe/companies.csv').open() as f:
    cc=list(csv.DictReader(f))
assert len(cc)==100 and [x['company'] for x in cc]==[x['company'] for x in companies]
for a in areas:
    assert (ROOT/a['path']).exists()
    assert set(a['source_ids'])<=sids
broken=[]
for p in ROOT.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if re.match(r'^(https?:|#|mailto:)',link):continue
        target=link.split('#')[0]
        if not (p.parent/target).exists(): broken.append((str(p.relative_to(ROOT)),target))
assert not broken,broken
# Validate the illustrative profit bridge, independently of slide labels.
profits=[20+40*e*r*c-1 for e,r,c in [(0.15,.4,.25),(.15,.6,.5),(.25,.8,.75)]]
assert all(math.isclose(x,y) for x,y in zip(profits,[19.6,20.8,25.0]))
assert math.isclose((profits[1]-20)/20,.04)
print('Validated 100 unique companies, 36 areas, 11 sectors, 22 sources, 600 score rationales, 18 priorities, evidence gates, valuation blanks, arithmetic and local document links.')
