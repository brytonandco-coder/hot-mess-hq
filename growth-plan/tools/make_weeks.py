"""Growth Plan task calendar: questionnaire answers in, a `launchplan` document out.

Builds the prep weeks, launch week and months 1 to 3 the way Bryton's own plan does (method.md, section 5),
sized to the client's content tier and work days, with targets from plan_model.py.

    python3 make_weeks.py intake.json launchplan.json
"""
import datetime as dt
import json
import sys

import plan_model

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def monday_of(d):
    return d - dt.timedelta(days=d.weekday())


def first_weekday_in(monday, wday):
    return monday + dt.timedelta(days=wday)


def routine(tier, long_form):
    """Weekly content routine per tier: (day index into her work days, text, quick)."""
    if tier == 'full':
        return [(0, f'Record {long_form} 1', False), (1, 'Review episode 1 and pick its 5 clips', True),
                (2, f'Record {long_form} 2', False), (3, 'Review episode 2 and pick its 5 clips', True),
                (-1, "Approve next week's carousels, schedule posts and send the newsletter", False)]
    if tier == 'standard':
        return [(0, f'Record this week\'s {long_form}', False), (1, 'Review it and pick its 5 clips', True),
                (-1, "Approve next week's daily posts, schedule them and send the newsletter", False)]
    return [(0, f'Record this week\'s {long_form}', False),
            (-1, "Pick 3 clips and 3 posts, schedule them and send the newsletter", False)]


def build(a):
    s = plan_model.settings_from_intake(a)
    rows = plan_model.run(s)
    L = a.get('ladder', {})
    front, upgrade, cont = L.get('frontName', 'the Program'), L.get('upgradeName', 'the Program + 1:1'), L.get('continuityName', 'the membership')
    fp, up, cp = s['frontPrice'], s['upgradePrice'], s['continuityPrice']
    magnet = L.get('leadMagnet', 'free download')
    workshop = L.get('workshopTitle', 'your free workshop')
    long_form = L.get('longForm', 'podcast episode')
    work = [DAYS.index(d) for d in (a.get('workDays') or DAYS[:5])]
    pocket = int(s['adPocket'])

    launch = monday_of(dt.date.fromisoformat(a['launchDate']))
    blackout_mondays = {monday_of(dt.date.fromisoformat(b)) for b in a.get('blackouts', [])}
    # 4 prep weeks before launch (6 when she has no offer selling yet), skipping her blackout weeks as catch-up weeks
    prep_count = 4 if (a.get('salesPerMonth') or 0) > 0 else 6
    prep, catchups = [], []
    d = launch - dt.timedelta(days=7)
    while len(prep) < prep_count:
        (catchups if d in blackout_mondays else prep).append(d)
        d -= dt.timedelta(days=7)
    prep.reverse()

    def day(monday, i):
        return first_weekday_in(monday, work[i if i >= 0 else len(work) + i]).isoformat()

    prep_tasks = [
        [(0, f'Put the {launch:%B} {launch.day} launch date on your calendar', True),
         (0, f'Set up {front} on {a.get("salesTool", "your course platform")}: ${fp:,.0f} and ${up:,.0f} (with 1:1), each with a 3-payment option', False),
         (1, f'Outline the free workshop "{workshop}": 3 teaching points and the offer at the end', False),
         (2, f'Make the {magnet} in the HQ', False),
         (-1, f'Record 2 {long_form}s to bank for launch', False),
         (-1, 'Book a lawyer to review your offer and refund terms', True)],
        [(0, f'Write the {front} sales page with both options (HQ drafts, you edit)', False),
         (1, 'Record lesson 1 and its worksheet', False),
         (2, 'Record lesson 2 and its worksheet', False),
         (-1, 'Turn on checkout and test a purchase on both options', True)],
        [(0, 'Have the HQ draft your emails: 5 welcome, 3 workshop reminders, 2 replay, 5 sales', False),
         (1, 'Review and schedule the welcome series and workshop emails', False),
         (2, 'Set up the weekly group coaching call: day, time, link and a first-call outline', False),
         (-1, 'Write the welcome email for new clients and record a short welcome video', False)],
        [(0, 'Finish the workshop slides and do one practice run', False),
         (1, f'Set up your {a.get("adsTool", "ads")} account and tracking; have ${pocket:,} ready for launch month', True),
         (2, 'Cut 3 or 4 test ads from your best clips', False),
         (-1, 'Schedule free workshop 1 for 2 weeks after launch and open registration', True)],
    ]
    if prep_count == 6:
        prep_tasks = [[(0, f'Write the promise of {front}: who it is for and the result in 12 weeks', False),
                       (1, 'Outline the 12 lessons', False), (-1, 'Ask 3 past clients what helped most', True)],
                      [(0, 'Plan your content: topics for the first 8 weeks', False),
                       (-1, f'Record 2 {long_form}s to bank for launch', False)]] + prep_tasks

    weeks = []

    def add_week(monday, title, tasks):
        items = []
        tasks = sorted(tasks, key=lambda t: day(monday, t[0]))
        for i, (di, text, quick) in enumerate(tasks, 1):
            items.append({'id': f'launch-w{len(weeks) + 1:02d}-{i:02d}', 'text': text[:160], 'due': day(monday, di), 'quick': quick})
        weeks.append({'week': len(weeks) + 1, 'monday': monday.isoformat(), 'title': title, 'tasks': items})

    all_prep = sorted([(m, 'prep') for m in prep] + [(m, 'catch') for m in catchups])
    p = 0
    for monday, kind in all_prep:
        if kind == 'catch':
            add_week(monday, 'Catch-up and rest week', [(0, 'Catch-up week: finish anything left from the launch checklist, then rest', False)])
        else:
            add_week(monday, f'Prep week {p + 1}', prep_tasks[p])
            p += 1

    for w in range(13):  # launch week + 12 weeks
        monday = launch + dt.timedelta(days=7 * w)
        tasks = list(routine(s['tier'], long_form))
        tasks.append((0, 'Check ads: cost per buyer this week', True))
        if w <= 9:
            tasks.append((1 if len(work) > 1 else 0, f'Record lesson {w + 3} and its worksheet', False))
        if w >= 1:
            tasks.append((-2 if len(work) > 2 else -1, 'Run the weekly group coaching call', False))
        if w == 0:
            title = 'Launch week'
            tasks.append((0, f'Launch day: sales page live, welcome series on, ads on at ${pocket:,} (test 3 or 4 ads)', False))
        else:
            title = f'Month {w // 4 + 1}, week {w % 4 + 1}'
        if w in (1, 5, 9):
            tasks.append((0, 'Send the workshop invite to your email list', True))
        if w in (2, 6, 10):
            tasks.append((2 if len(work) > 2 else -1, f'Host free workshop: "{workshop}"', False))
            tasks.append((-1, 'Send the workshop replay emails', True))
        if w in (4, 8, 12):
            mname = (monday).strftime('%B')
            tasks.append((0, f"Set {mname}'s ad budget: half of last month's income (at least ${pocket:,})", True))
            tasks.append((-1, 'Look at last month: email sign-ups, workshop show-up and sales against the plan', False))
        if w in (4, 8, 12):
            tasks.append((-2 if len(work) > 2 else -1, 'Host the monthly Q&A', False))
        if w == 4:
            tasks.append((1, 'Pick the clips with the most saves and shares and make 2 new test ads', False))
        if w == 8:
            tasks.append((1, 'Ask your first students for testimonials', True))
            tasks.append((2 if len(work) > 2 else -1, 'Draft the CEO meeting scorecard template', False))
        if w == 11:
            tasks.append((1, f'Open {cont} (${cp:,.0f} a month) for your first graduates', False))
            tasks.append((-2 if len(work) > 2 else -1, 'Run the week 12 group CEO session for your first students', False))
        if w == 12:
            title = 'Plan month 4'
            tasks.append((1, 'Plan month 4: workshops every 2 weeks from now on', False))
        add_week(monday, title, tasks)

    return {
        'name': f'{a.get("ladder", {}).get("frontName", "Launch")} plan',
        'list': 'launch',
        'start': weeks[0]['monday'],
        'launch': launch.isoformat(),
        'timezone': a.get('timezone'),
        'tier': s['tier'],
        'weeks': weeks,
        'added': [],
        'reviews': [],
        'targets': {
            'note': 'From the Growth Plan model. Month 1 = launch month. Program sales per month; ads = the month budget; members = continuity + low tier at month end.',
            'costPerProgramBuyer': {'plan': round(s['cacFront']), 'holdAbove': round(s['cacFront'] * 1.15)},
            'refundsMax': 0.1,
            'oneOnOneShare': s['upgradeRate'],
            'goalProfit': s.get('goalProfit'),
            'months': plan_model.targets(rows)[:12],
        },
        'routine': [t[1] for t in routine(s['tier'], long_form)],
    }


def main():
    a = json.load(open(sys.argv[1]))
    plan = build(a)
    n = sum(len(w['tasks']) for w in plan['weeks'])
    print(f"{len(plan['weeks'])} weeks, {n} tasks, launch {plan['launch']}, tier {plan['tier']}")
    for w in plan['weeks'][:2] + plan['weeks'][-2:]:
        print(w['week'], w['monday'], w['title'])
        for t in w['tasks']:
            print('   ', t['due'], t['text'])
    if len(sys.argv) > 2:
        json.dump(plan, open(sys.argv[2], 'w'), indent=1)


if __name__ == '__main__':
    main()
