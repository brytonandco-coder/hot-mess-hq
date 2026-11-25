"""Growth Plan projection: questionnaire answers in, a month-by-month projection and targets out.

Same model as Bryton's own plan (the from-zero offer ladder), with her numbers turned into
settings that come from a client's answers. It's a planning model, not a forecast.

    python3 plan_model.py intake.json            # prints a summary and the targets
    python3 plan_model.py intake.json out.json   # also saves {settings, months, targets}
"""
import json
import sys


def settings_from_intake(a):
    """Turn questionnaire answers (see questionnaire.md) into model settings, using method.md defaults."""
    ladder = a.get('ladder', {})
    front = float(ladder.get('frontPrice', 1497))
    upgrade = float(ladder.get('upgradePrice', round(front * 3.33 / 100) * 100 - 3))
    cont = float(ladder.get('continuityPrice', 197))
    low = ladder.get('lowPrice')  # optional cheaper "stay connected" tier
    hist = a.get('adHistory') or {}
    cac_front = hist.get('costPerSale') or max(150.0, round(front * 0.26))
    list_size = a.get('listSize') or 0
    organic_front0 = 0.5 + min(2.0, list_size / 4000.0) + 0.5 * float(a.get('referralsPerMonth') or 0)
    hours = a.get('contentHours') or 8
    tier = 'full' if hours >= 11 else ('standard' if hours >= 6 else 'light')
    growth1 = {'full': 0.15, 'standard': 0.12, 'light': 0.08}[tier]
    max_1to1_new = a.get('maxNew1to1') or max(2, int((a.get('deliveryHours') or 12) / 1.5 / 3))
    return {
        'tier': tier,
        'frontPrice': front, 'upgradePrice': upgrade, 'upgradeRate': ladder.get('upgradeRate', 0.10),
        'upgradeDeliveryCost': ladder.get('upgradeDeliveryCost', 500), 'maxNew1to1': max_1to1_new,
        'continuityPrice': cont, 'continuityRate': ladder.get('continuityRate', 0.25),
        'continuityCost': ladder.get('continuityCost', 15), 'continuityChurn': 0.05,
        'lowPrice': low, 'lowRate': ladder.get('lowRate', 0.25 if low else 0.0),
        'lowKeep': ladder.get('lowKeep', (low or 0) * 0.9), 'lowChurn': 0.06,
        'refunds': a.get('refundRate', 0.08), 'payPlanShare': 0.5,
        'adPocket': a.get('adPocket', 500), 'adShare': a.get('adShare', 0.5), 'adCap': a.get('adCap', 45000),
        'cacFront': cac_front, 'cacLow': 143, 'frontShare': 0.8 if low else 1.0,
        'organicFront0': organic_front0, 'organicLow0': 3.0 if low else 0.0,
        'organicGrowth1': growth1, 'organicGrowth2': 0.05,
        'teamCost': a.get('teamCost', 6000), 'teamGate': a.get('teamGate', 30),
        'buildCost': a.get('buildCost', 0), 'buildMonths': a.get('buildMonths', 4), 'buildCash': a.get('buildCash', 12000),
        'fixedBase': a.get('fixedBase', 200),
        'maxNewClients': a.get('maxNewClients') or 50,
        'months': a.get('months', 24), 'firstMonth': a.get('firstMonth', '2027-01'),
        'goalProfit': a.get('goalProfit'),
    }


def month_label(first, i):
    y, m = map(int, first.split('-'))
    m += i
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    return f'{y:04d}-{m:02d}'


def run(s):
    front_net = (s['frontPrice'] * 0.971 + s['upgradeRate'] * ((s['upgradePrice'] - s['frontPrice']) * 0.971 - s['upgradeDeliveryCost'])) * (1 - s['refunds'])
    cont_keep = s['continuityPrice'] * 0.971 - s['continuityCost']
    low = cont = 0.0
    grads = [0.0, 0.0, 0.0]
    oc, ol = s['organicFront0'], s['organicLow0']
    cash = last_in = 0.0
    plan_cash = [0.0] * (s['months'] + 3)
    build_start = None
    team_on = False
    rows = []
    for m in range(1, s['months'] + 1):
        if m > 1:
            g = s['organicGrowth1'] if m <= 12 else s['organicGrowth2']
            oc *= 1 + g
            ol *= 1 + g
        ads = max(s['adPocket'], min(s['adCap'], s['adShare'] * last_in))
        # never buy more clients than she can take: stop raising ads at her monthly client cap
        room = max(0.0, s['maxNewClients'] - oc)
        for _ in range(3):
            scale = 1 + 0.15 * max(0, (ads - 10000) / 10000)
            ads = min(ads, max(s['adPocket'], room * s['cacFront'] * scale / s['frontShare']))
        ads = round(ads / 250) * 250
        scale = 1 + 0.15 * max(0, (ads - 10000) / 10000)
        if s['buildCost'] and build_start is None and cash >= s['buildCash']:
            build_start = m
        front = min(s['maxNewClients'], ads * s['frontShare'] / (s['cacFront'] * scale) + oc)
        upgrades = min(front * s['upgradeRate'], s['maxNew1to1'])
        if not team_on and front >= s['teamGate']:
            team_on = True
        grad = grads.pop(0)
        grads.append(front)
        low = low * (1 - s['lowChurn']) + ads * (1 - s['frontShare']) / (s['cacLow'] * scale) + ol + grad * s['lowRate']
        cont = cont * (1 - s['continuityChurn']) + grad * s['continuityRate']
        members = low + cont
        fixed = s['fixedBase'] + (2000 if members > 300 else 0) + (4000 if members > 800 else 0) + (s['teamCost'] if team_on else 0)
        build = s['buildCost'] / s['buildMonths'] if (build_start and build_start <= m < build_start + s['buildMonths']) else 0
        gross = front * s['frontPrice'] + upgrades * (s['upgradePrice'] - s['frontPrice']) + low * (s['lowPrice'] or 0) + cont * s['continuityPrice']
        income_kept = front * front_net + low * s['lowKeep'] + cont * cont_keep
        profit = income_kept - ads - fixed - build
        full = front * (1 - s['payPlanShare']) * front_net
        part = front * s['payPlanShare'] * front_net / 3
        for k in range(3):
            plan_cash[m + k] += part
        cash_in = low * s['lowKeep'] + cont * cont_keep + full + plan_cash[m]
        cash = max(0.0, cash + cash_in - ads - fixed - build)
        last_in = cash_in
        rows.append({
            'month': month_label(s['firstMonth'], m - 1), 'n': m,
            'frontSales': round(front, 1), 'upgrades': round(upgrades, 1),
            'members': round(members), 'continuity': round(cont), 'low': round(low),
            'gross': round(gross), 'ads': ads, 'team': s['teamCost'] if team_on else 0, 'build': round(build),
            'costs': round(gross - profit), 'profit': round(profit),
        })
    return rows


def weak_case(s):
    """The 'if things go slower' case every plan shows beside the main one."""
    w = dict(s)
    w['cacFront'] = s['cacFront'] * 1.3
    w['upgradeRate'] = s['upgradeRate'] * 0.5
    w['continuityRate'] = s['continuityRate'] * 0.6
    w['organicGrowth1'] = s['organicGrowth1'] * 0.6
    return run(w)


def targets(rows):
    return [{'month': r['month'], 'programSales': round(r['frontSales']), 'ads': r['ads'], 'members': r['members']} for r in rows]


def main():
    a = json.load(open(sys.argv[1]))
    s = settings_from_intake(a)
    rows = run(s)
    goal = s.get('goalProfit')
    hit = next((r for r in rows if goal and r['profit'] >= goal), None)
    y1 = sum(r['profit'] for r in rows[:12])
    print(f"Content tier: {s['tier']}. Front ${s['frontPrice']:,.0f}, upgrade ${s['upgradePrice']:,.0f}, continuity ${s['continuityPrice']:,.0f}/mo, cost per buyer ${s['cacFront']:,.0f}")
    print(f"Month 12 profit ${rows[11]['profit']:,}  year 1 profit ${y1:,}  month {s['months']} profit ${rows[-1]['profit']:,}")
    print(f"Goal ${goal:,}/mo reached: month {hit['n']} ({hit['month']})" if hit else f"Goal not reached within {s['months']} months")
    weak = weak_case(s)
    whit = next((r for r in weak if goal and r['profit'] >= goal), None)
    print(f"Slower case: month 12 profit ${weak[11]['profit']:,}, year 1 ${sum(r['profit'] for r in weak[:12]):,}, goal " + (f"month {whit['n']}" if whit else f"not within {s['months']} months"))
    for r in rows[:12]:
        print(r)
    if len(sys.argv) > 2:
        json.dump({'settings': s, 'months': rows, 'slower': weak, 'targets': targets(rows)}, open(sys.argv[2], 'w'), indent=1)


if __name__ == '__main__':
    main()
