#!/usr/bin/env python3
"""Reproduce 25 dated equity cases. Standard library only; no live data calls.

Source packets remain immutable inputs. Lead overrides are recorded in each output.
Five end-of-year dividend cash flows plus a year-five disposal value determine IRR.
"""
import copy
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'research/ranking-2026-09-12'

def read(name):
    return json.loads((OUT / name).read_text())

def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')

def pv(terminal, dividends, rate):
    return sum(d / (1 + rate) ** y for y, d in enumerate(dividends, 1)) + terminal / (1 + rate) ** 5

def irr(price, terminal, dividends):
    lo, hi = -.999, 10.0
    assert price > 0 and terminal > 0 and len(dividends) == 5
    assert pv(terminal, dividends, hi) < price, 'IRR outside supported bounds'
    for _ in range(150):
        mid = (lo + hi) / 2
        if pv(terminal, dividends, mid) > price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def calculate(c, s):
    # A forecast already representing year one receives FOUR subsequent growth years.
    anchor = s.get('earnings_year1', c['baseline_value'])
    periods = 4 if 'earnings_year1' in s else 5
    ordinary = anchor * (1 + s['growth_ex_ai']) ** periods
    terminal = ordinary * (1 + s['incremental_ai_terminal_earnings_pct']) * s['terminal_multiple']
    div = s['dividends5']
    annual = irr(c['price'], terminal, div)
    noai = irr(c['price'], ordinary * s['terminal_multiple'], div)
    return dict(earnings_anchor=anchor, growth_periods=periods,
                terminal_ordinary_earnings=ordinary,
                terminal_total_earnings=ordinary * (1 + s['incremental_ai_terminal_earnings_pct']),
                terminal_price=terminal, cumulative_dividends=sum(div), annual_irr=annual,
                total_return_no_reinvestment=(terminal + sum(div)) / c['price'] - 1,
                entry_prices={str(r): pv(terminal, div, r) for r in [.08, .10, .12]},
                annual_irr_without_incremental_ai=noai,
                ai_irr_percentage_points=(annual-noai)*100)

def scenario(g, multiple, ai, rationale):
    return dict(growth_ex_ai=g, terminal_multiple=multiple,
                incremental_ai_terminal_earnings_pct=ai, dividends5=[0]*5, rationale=rationale)

def models():
    result = []
    for filename in ['valuation-europe.json', 'valuation-health.json', 'valuation-lead.json']:
        for original in read(filename):
            c = copy.deepcopy(original)
            c['input_packet'] = filename
            c['lead_overrides'] = []
            if filename == 'valuation-health.json':
                for target, old in [('baseline_value','value'),('baseline_period','period'),('baseline_source','source'),('baseline_adjustments','adjustments')]:
                    c[target] = c[old]
            c.setdefault('valuation_status', c.get('status', 'ANALYST_NORMALIZATION'))
            if c['id'] == 'C003':
                c['price'] = 156.10
                c['price_quality'] = 'Google Finance September 11 after-hours indication, retrieved September 12; exact after-hours trade time not shown. Regular close 160.17 and finance-feed late timestamp disagree. Indicative case, excluded from strict executable-price comparisons.'
                c['price_timestamp'] = 'After-hours indication; exact trade time unavailable'
                c['alternative_quote'] = 160.17
                c['lead_overrides'].append('Use displayed post-news after-hours 156.10 instead of regular close160.17; retain regular-close sensitivity and unresolved exact timestamp.')
                c['valuation_status'] = 'CONDITIONAL_PRICE_AND_PHARMA_NORMALIZATION'
            result.append(c)
    quote = {q['ticker']:q for q in read('quotes-us.json')}
    raw = read('platform-normalization.json')
    names = {'MSFT':'Microsoft','GOOGL':'Alphabet','AMZN':'Amazon','META':'Meta Platforms'}
    for a in raw['companies']:
        q = quote[a['ticker']]
        c = dict(id=a['id'],company=names[a['ticker']],ticker=a['ticker'],listing='Nasdaq '+('Class A common share' if a['ticker'] in ['GOOGL','META'] else 'common share'),
                 currency='USD',price=a['price_usd'],price_date=q['timestamp_text'],price_source=q['source'],
                 price_quality='Latest finance-feed trade, not independently verified official close',
                 baseline_value=a['scenario_eps_usd'],baseline_metric='Normalized annual diluted EPS; earnings valuation conditional on capital recovery',
                 baseline_period=a['financial_period'],baseline_source=[raw['sources'][s]['url'] for s in a['source_ids']],
                 baseline_adjustments=[a['normalization_formula'],a['scenario_denominator_note'],a['sbc_treatment']],
                 balance_sheet=a['annual_capital_cash_crosscheck'],valuation_status=a['capital_recovery_status'],
                 input_packet='platform-normalization.json',horizon_years=5,scenarios={},lead_overrides=[],
                 uncertainties=['Cash after current investment is substantially below normalized earnings; maintenance versus growth capex cannot be estimated reliably.',
                 'The terminal earnings multiple requires adequate future returns on capex, leased capacity and AI counterparties. This is not a verified owner-FCF valuation.',
                 'Ordinary growth already includes existing AI products, recommendation/ML and announced business execution. Bull AI is only the additional net retention above that path.',
                 'No uncommenced lease or purchase commitment is mechanically added twice to debt.'])
        for s in a['scenarios']:
            key=s['scenario']
            c['scenarios'][key] = dict(growth_ex_ai=s['ordinary_eps_cagr_assumption'],terminal_multiple=s['terminal_pe_assumption'],
                incremental_ai_terminal_earnings_pct=s['incremental_ai_terminal_eps_change_assumption'],
                dividends5=[s['current_annual_common_dividend_usd']*(1+s['dividend_growth_assumption'])**y for y in range(1,6)],
                rationale='Lead-reviewed conventional growth and valuation assumptions; capital recovery remains a binding condition.')
        c['scenarios']['base']['incremental_ai_terminal_earnings_pct']=0
        c['lead_overrides'].append('Zero separate base AI premium; already deployed AI remains in baseline/conventional execution. Recompute dividend-timed IRR, replacing agent terminal-wealth CAGR.')
        if a['ticker'] in ['MSFT','AMZN','GOOGL']:
            c['scenarios']['downside']['growth_ex_ai'] = -.03 if a['ticker']=='GOOGL' else 0
            c['lead_overrides'].append('Stronger downside: ordinary EPS stagnation for MSFT/AMZN and3% annual decline for GOOGL; agent positive-growth downside did not adequately test failed capital recovery.')
        uplift = c['scenarios']['bull']['incremental_ai_terminal_earnings_pct']
        net = a['normalized_net_income_usd_bn'] * uplift
        c['ai_bridge'] = (f'Bull-only {uplift:.0%} terminal earnings uplift requires an additional ${net:.2f}bn annual net earnings at present scale, '
            f'or ${net/.4:.2f}bn genuinely incremental revenue at an assumed40% after-tax contribution after model, service, depreciation and compensation costs. '
            'This is a scale requirement, not observed economics. Alternatively, measured net internal savings can supply part, but cannot also be counted in product margins. '
            'Growth in AI infrastructure sales already inside conventional EPS growth does not qualify again. Without a funded capital-recovery bridge, the bull remains conditional.')
        result.append(c)
    params = {
        'MELI':[(.05,22,0),(.18,30,0),(.25,35,.08)],
        'UBER':[(-.05,16,0),(.15,23,0),(.20,28,.08)],
        'NOW':[(.05,30,0),(.20,40,0),(.27,48,.10)]}
    why = {
        'MELI': ['Credit losses, shipping subsidies and investment absorb most volume growth; no normalization of a credit boom.',
                 'Commerce, ads and payments support18% per-share growth from a depressed but unadjusted-for-expansion-cost starting margin. No tax windfall or AI premium.',
                 'Stronger ordinary scale and credit execution support25% EPS growth; additional AI conversion/distribution retention adds8% only after model, delivery, funding and risk costs.'],
        'UBER': ['AV providers bypass the aggregator, insurance and driver costs rise and competition pressures take rate.',
                 'Trips, delivery and ordinary operating leverage support15% EPS growth with compensation retained; no separate buyback yield or permanent low tax.',
                 'Marketplace demand and ordinary operating leverage compound20%; a further8% AI benefit requires durable net distribution/dispatch economics after AV partners take their share.'],
        'NOW': ['Five-percent earnings growth despite continuing revenue growth reflects agent cannibalization, acquisition finance and persistent compensation cost;30x is still a premium.',
                'Twenty-percent earnings growth requires both continued workflow demand and ordinary GAAP margin expansion from a low base.40x terminal EPS already assumes substantial durability.',
                'Twenty-seven-percent conventional EPS growth and48x value require strong acquisition integration and GAAP cash conversion; additional10% AI uplift needs paid net economics beyond those improvements.']}
    for a in read('normalization-other.json')['companies']:
        q = quote[a['ticker']]
        n = a['normalization']
        numerator = n.get('normalized_common_net_income', n.get('normalized_net_income'))
        baseline = numerator/n['diluted_share_proxy_millions']
        c=dict(id=a['id'],company=a['company'],ticker=a['ticker'],listing=('NYSE' if a['ticker'] in ['UBER','NOW'] else 'Nasdaq')+' common share',currency='USD',
               price=q['price'],price_date=q['timestamp_text'],price_source=q['source'],price_quality='Latest finance-feed trade; official close not verified',
               baseline_value=baseline,baseline_metric='GAAP-derived normalized annual diluted EPS; SBC and acquisition amortization retained',
               baseline_period=a['basis'],baseline_source=[s['url'] for s in a['sources']],baseline_adjustments=[n['formula']]+a['limits'],
               balance_sheet=a['cash_and_capital'],uncertainties=a['limits'],valuation_status='CONDITIONAL_CAPITAL_AND_NORMALIZATION',
               input_packet='normalization-other.json',lead_overrides=['Lead sets all scenarios independently; strict annual numerator/share bridge rather than rounded EPS.'],horizon_years=5,scenarios={})
        for key,p,rationale in zip(['downside','base','bull'],params[a['ticker']],why[a['ticker']]):
            c['scenarios'][key]=scenario(*p,rationale)
        u=c['scenarios']['bull']['incremental_ai_terminal_earnings_pct']
        c['ai_bridge']=(f'Bull-only{u:.0%} net terminal uplift equals ${numerator*u:.0f}m additional annual earnings at present scale. '
            f'At an assumed35% after-tax incremental contribution, this needs ${numerator*u/.35:.0f}m revenue beyond the conventional growth path, after model/service/credit or insurance costs. '
            'Net internal cost removal could substitute, but must be separately measured and cannot be counted again as product-margin improvement. '
            'No released working capital, customer balances, insurance reserves or acquisition addbacks count as recurring AI earnings.')
        result.append(c)
    return result

def clean_text(value):
    if isinstance(value,str): return value
    return json.dumps(value,ensure_ascii=False)

def prose_spacing(value):
    """Improve packet prose while preserving URLs, markdown links, code and IDs."""
    parts=re.split(r'(\[[^\]]*\]\([^)]*\)|https?://\S+|`[^`]+`|\bC\d{3}\b)',value)
    for i in range(0,len(parts),2):
        parts[i]=re.sub(r'(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])',' ',parts[i])
        parts[i]=re.sub(r'(?<=[,;])(?=[A-Za-z0-9])',' ',parts[i])
    return ''.join(parts)

def run():
    cases=models()
    ranks={x['id']:x for x in read('universe-ranking.json')}
    judgments={x['id']:x for x in read('lead-judgments.json')}
    assert len(cases)==25 and len({c['id'] for c in cases})==25
    assert set(judgments)=={c['id'] for c in cases}
    assert sorted(x['investment_rank'] for x in judgments.values())==list(range(1,26))
    for c in cases:
        c['lead_judgment']=judgments[c['id']]
        c['regime_rank']=ranks[c['id']]['regime_rank']
        c['regime_rationale']=ranks[c['id']]['rationale']
        c['current_normalized_multiple']=c['price']/c['baseline_value']
        c['results']={key:calculate(c,s) for key,s in c['scenarios'].items()}
        assert len(c['results'])==3
        base=c['scenarios']['base']; b=c['results']['base']
        divpv=sum(d/1.1**y for y,d in enumerate(base['dividends5'],1))
        required_terminal=(c['price']-divpv)*1.1**5
        periods=b['growth_periods']; anchor=b['earnings_anchor']
        c['required_ordinary_growth_for_10pct']=(required_terminal/(anchor*base['terminal_multiple']*(1+base['incremental_ai_terminal_earnings_pct'])))**(1/periods)-1
        c['sensitivity']={}
        for label,variable,change in [('growth_minus_2pp','growth_ex_ai',-.02),('growth_plus_2pp','growth_ex_ai',.02),('multiple_minus_20pct','terminal_multiple',.8),('multiple_plus_20pct','terminal_multiple',1.2)]:
            s=copy.deepcopy(base)
            s[variable]=s[variable]+change if variable=='growth_ex_ai' else s[variable]*change
            c['sensitivity'][label]=calculate(c,s)
        for factor in [.9,1.1]:
            clone=copy.deepcopy(c); clone['baseline_value']*=factor;s=copy.deepcopy(base)
            if 'earnings_year1' in s: s['earnings_year1']*=factor
            c['sensitivity'][f'earnings_anchor_times_{factor}']=calculate(clone,s)
        if 'alternative_quote' in c:
            clone=copy.deepcopy(c);clone['price']=c['alternative_quote']
            c['sensitivity']['regular_close_quote']={key:calculate(clone,s) for key,s in c['scenarios'].items()}
        # Sequential terminal-value bridge: growth, AI, multiple. Not a causal attribution.
        bull=c['scenarios']['bull']; u=c['results']['bull']
        ordinary_bull_at_base_multiple=u['terminal_ordinary_earnings']*base['terminal_multiple']
        ai_bull_at_base_multiple=u['terminal_total_earnings']*base['terminal_multiple']
        c['bull_terminal_value_bridge']={
            'base_terminal_value':b['terminal_price'],
            'ordinary_growth_and_anchor_change':ordinary_bull_at_base_multiple-b['terminal_price'],
            'additional_ai_at_base_multiple':ai_bull_at_base_multiple-ordinary_bull_at_base_multiple,
            'terminal_multiple_change':u['terminal_price']-ai_bull_at_base_multiple,
            'bull_terminal_value':u['terminal_price'],
            'note':'Order-dependent arithmetic bridge; dividends excluded. No causal/probabilistic attribution.'}
        for key,s in c['scenarios'].items():
            z=c['results'][key]
            assert len(s['dividends5'])==5 and min(s['dividends5'])>=0
            assert math.isclose(pv(z['terminal_price'],s['dividends5'],z['annual_irr']),c['price'],rel_tol=1e-10)
            assert z['entry_prices']['0.08']>z['entry_prices']['0.1']>z['entry_prices']['0.12']
        assert c['results']['downside']['annual_irr']<b['annual_irr']<c['results']['bull']['annual_irr']
    cases.sort(key=lambda c:c['regime_rank'])
    write('valued-candidates.json',cases)
    table=['# Five-year scenarios for 25 candidates','',
        'Snapshot:12 September2026. Quotes are dated individually, mostly September11 sessions/after-hours. Returns are annual investor IRRs in listing currency, with annual dividends and no investor tax, fees or FX. These are conditional scenarios, not probability-weighted forecasts. Order below follows operating-regime fit; see lead-decision.md for the separate investment judgment.',
        '', 'Base cases assign zero **additional** AI premium. Existing AI economics remain in the baseline and ordinary execution. Entry10% is the price producing a10% IRR under the stated base case, not a price target or user-specified hurdle. Downside is a scenario, not a maximum possible loss.', '',
        '| Fit rank | Company / currency | Quote | Annual earnings anchor | Downside IRR | Base IRR | Bull IRR | Base entry10% | Bull AI contribution |',
        '|---:|---|---:|---:|---:|---:|---:|---:|---:|']
    for c in cases:
        r=c['results'];anchor=r['base']['earnings_anchor']; flag=' Y1' if r['base']['growth_periods']==4 else ''
        table.append(f"|{c['regime_rank']}|[{c['company']}](cases/{c['id']}.md) · {c['currency']}|{c['price']:.2f}|{anchor:.2f}{flag}|{r['downside']['annual_irr']:.1%}|{r['base']['annual_irr']:.1%}|{r['bull']['annual_irr']:.1%}|{r['base']['entry_prices']['0.1']:.2f}|{r['bull']['ai_irr_percentage_points']:.2f}pp|")
    table+=['','Y1 means an explicit next-year earnings forecast, followed by four growth years and a five-year holding period. Every other anchor receives five growth years. AstraZeneca uses an indicative after-hours quote with an unresolved precise timestamp; the regular-close sensitivity is in its case. TRI/LSEG normalization and seven platform/marketplace capital assumptions require additional evidence before actionable promotion. Pharma reserves are portfolio-level assumptions, not drug-by-drug risk-adjusted DCFs.','',
             'Full inputs, source links, capital checks and sensitivities: [machine-readable cases](valued-candidates.json), [sensitivity table](sensitivity.md), [lead judgment](lead-decision.md).']
    (OUT/'scenario-table.md').write_text(prose_spacing('\n'.join(table)+'\n'))
    investment=['# Investment ranking of 25 valued candidates','',
        'Lead judgment at dated September2026 quotes. This ordering considers achievable return, conventional resilience, retained AI economics and evidence confidence; it is not a sort by modeled return. Conditional cases are priority research judgments, not actionable valuation passes. Adjacent positions have limited precision. See [lead decision](lead-decision.md) and the separate [100-company operating ranking](universe-ranking.md).','',
        '| Rank | Company / currency | Quote | Downside IRR | Base IRR | Bull IRR | Base entry10% | Decision |',
        '|---:|---|---:|---:|---:|---:|---:|---|']
    for c in sorted(cases,key=lambda x:x['lead_judgment']['investment_rank']):
        r=c['results'];j=c['lead_judgment']
        investment.append(f"|{j['investment_rank']}|[{c['company']}](cases/{c['id']}.md) · {c['currency']}|{c['price']:.2f}|{r['downside']['annual_irr']:.1%}|{r['base']['annual_irr']:.1%}|{r['bull']['annual_irr']:.1%}|{r['base']['entry_prices']['0.1']:.2f}|{j['decision']}|")
    investment+=['','All returns are five-year annual dividend-timed IRRs in listing currency, before investor tax, fees and FX. Base entry10% is conditional on the stated cash flows;10% is a research convention. No probability weighting is used. Full rationale and change-of-view triggers are in each linked case and [lead judgments](lead-judgments.json).']
    (OUT/'investment-ranking.md').write_text(prose_spacing('\n'.join(investment)+'\n'))
    sensitivity=['# Base-case sensitivity','',
       'Entry prices discount identical base dividends and terminal equity values. The growth hurdle holds the base terminal multiple and dividends fixed. Y1 forecast cases solve the remaining four growth years. Sensitivities change one variable at a time and do not assign probabilities.','',
       '| Company / currency | Entry8% | Entry10% | Entry12% | Growth needed for10% | Base IRR, earnings−10% | Base IRR, multiple−20% | Base IRR, growth−2pp |',
       '|---|---:|---:|---:|---:|---:|---:|---:|']
    (OUT/'cases').mkdir(exist_ok=True)
    for c in cases:
        r=c['results'];e=r['base']['entry_prices'];s=c['sensitivity']
        sensitivity.append(f"|{c['company']} · {c['currency']}|{e['0.08']:.2f}|{e['0.1']:.2f}|{e['0.12']:.2f}|{c['required_ordinary_growth_for_10pct']:.1%}|{s['earnings_anchor_times_0.9']['annual_irr']:.1%}|{s['multiple_minus_20pct']['annual_irr']:.1%}|{s['growth_minus_2pp']['annual_irr']:.1%}|")
        quote_link=c['price_source'] if str(c['price_source']).startswith('https://') else '../quotes-us.json'
        j=c['lead_judgment']
        lines=[f"# {c['company']} — {c['id']}",'',f"Lead-reviewed case,12 September2026. **{c['valuation_status']}**. Operating-fit rank{c['regime_rank']} of100; investment rank{j['investment_rank']} of25.",'',
               f"**Decision: {j['decision']}.** {j['rationale']}",'',f"**What changes the decision:** {j['trigger']}",'',
               f"{c['listing']}. Quote **{c['price']:.2f} {c['currency']}**; {c['price_date']}. [Quote source]({quote_link}). {c.get('price_quality','See original packet for quotation timestamp/venue quality.')}",'',
               f"Normalized annual anchor **{c['baseline_value']:.4f} {c['currency']} per share**. {c['baseline_metric']}. Period: {c['baseline_period']}.",'',
               '## Normalization and source evidence','']
        adjustments=c.get('baseline_adjustments',[])
        if not isinstance(adjustments,list):adjustments=[adjustments]
        lines += ['- '+clean_text(a) for a in adjustments]
        sources=c['baseline_source']; sources=[sources] if isinstance(sources,str) else sources
        lines+=['']+ [f'- [Financial source {i}]({url})' for i,url in enumerate(sources,1)]+['',f"Detailed evidence and capital bridge: [{c['input_packet']}](../{c['input_packet']}).",'',
                 '## Five-year cases','', '| Scenario | Ordinary per-share growth | Additional terminal AI | Terminal earnings/cash multiple | Year5 price | Five dividends | Annual IRR |',
                 '|---|---:|---:|---:|---:|---:|---:|']
        for k in ['downside','base','bull']:
            a=c['scenarios'][k];z=r[k]
            lines.append(f"|{k}|{a['growth_ex_ai']:.1%}|{a['incremental_ai_terminal_earnings_pct']:.0%}|{a['terminal_multiple']:.1f}×|{z['terminal_price']:.2f}|{z['cumulative_dividends']:.2f}|{z['annual_irr']:.1%}|")
        lines+=['', 'Dividends are paid annually, not all at disposal. For an explicit Y1 earnings input, apply only four subsequent growth years. Inputs are analyst assumptions, not reported forecasts except where expressly identified.']
        for k in ['downside','base','bull']:
            a=c['scenarios'][k]
            lines+=['',f"**{k.capitalize()}:** {a.get('rationale','')}"+(f" Year1 EPS={a['earnings_year1']:.4f}; four later growth years." if 'earnings_year1' in a else '')]
        lines+=['','## Incremental AI and valuation discipline','',clean_text(c.get('ai_bridge','AI uplift is a capped bull option for net retained operational savings; see scenario rationale. No AI-driven change in clinical success or insurance risk is modeled.')),'',
                f"At the stated quote, the base case returns **{r['base']['annual_irr']:.1%}**. The10% base entry is **{e['0.1']:.2f} {c['currency']}**, versus{e['0.08']:.2f} at8% and{e['0.12']:.2f} at12%. Holding base multiple/dividends fixed requires **{c['required_ordinary_growth_for_10pct']:.1%}** ordinary earnings growth for10% investor IRR.",'',
                f"In the bull case, the separate AI increment adds{r['bull']['ai_irr_percentage_points']:.2f} percentage points of annual IRR. The remainder comes from the conventional earnings path, starting price, multiple and dividends; the whole bull return cannot be attributed to AI.",'',
                f"Base IRR falls to{s['earnings_anchor_times_0.9']['annual_irr']:.1%} with a10% lower earnings anchor, {s['multiple_minus_20pct']['annual_irr']:.1%} with a20% lower terminal multiple, and{s['growth_minus_2pp']['annual_irr']:.1%} with ordinary growth2points lower.",'',
                '## Limits and what must hold','', c['regime_rationale'],'']
        lines+=['- '+clean_text(x) for x in c.get('uncertainties',[])]
        if c.get('falsifiers'):lines+=['']+['- Falsifier: '+clean_text(x) for x in c['falsifiers']]
        if c['lead_overrides']:lines+=['','Lead overrides of agent inputs:','']+['- '+x for x in c['lead_overrides']]
        if 'alternative_quote' in c:lines+=['',f"Regular-close sensitivity at{c['alternative_quote']:.2f}: base{s['regular_close_quote']['base']['annual_irr']:.1%}, bull{s['regular_close_quote']['bull']['annual_irr']:.1%}. Exact after-hours timing remains unresolved."]
        lines+=['','These local-currency equity returns exclude investor tax, fees and FX. Interest is already in earnings; debt is not deducted again. SBC remains an economic cost. Scenario downside is not a loss floor.','']
        (OUT/'cases'/f"{c['id']}.md").write_text(prose_spacing('\n'.join(lines)))
    (OUT/'sensitivity.md').write_text(prose_spacing('\n'.join(sensitivity)+'\n'))
    # Meaningful independent identities: zero-dividend analytic IRR and known Y1 timing.
    assert math.isclose(irr(100,200,[0]*5),2**.2-1,rel_tol=1e-12)
    toy={'price':100,'baseline_value':999};sc=scenario(.1,10,0,'test');sc['earnings_year1']=2
    assert math.isclose(calculate(toy,sc)['terminal_price'],2*1.1**4*10,rel_tol=1e-12)
    write('validation.json',{'companies':25,'cases':75,'unique_ids':True,'investment_ranks_1_to_25':'PASS','cashflow_irr_identities':'PASS','entry_hurdle_ordering':'PASS','scenario_ordering':'PASS','zero_dividend_closed_form':'PASS','year1_four_growth_years':'PASS','source_verification':'See source packets; mathematical validation is not independent source verification.'})
    for c in sorted(cases,key=lambda x:-x['results']['base']['annual_irr']):
        r=c['results'];print(c['id'],f"{c['company']:26s}",f"{c['currency']} {c['price']:8.2f}",f"D/B/U {r['downside']['annual_irr']:7.2%} {r['base']['annual_irr']:7.2%} {r['bull']['annual_irr']:7.2%}",f"entry10 {r['base']['entry_prices']['0.1']:.2f}")

if __name__=='__main__':
    run()
