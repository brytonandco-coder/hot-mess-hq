# Growth Plan system (draft, not live)

This folder saves the planning system Bryton built for her own launch so it can later be offered to clients. Nothing here ships to members yet: the plugin only installs `plugins/hot-mess-hq`, and this folder sits outside it.

What it does for a client, once it's live:

1. **Questionnaire.** She answers questions about her business, offers, numbers, ad budget, time and goals (`questionnaire.md`).
2. **Plan.** Claude turns her answers into a custom plan using Bryton's method (`method.md`): her offer ladder and prices, a content plan sized to her hours, an ad plan that grows out of income, member-count gates, and a month-by-month projection (`tools/plan_model.py`).
3. **Tasks.** The plan becomes a week-by-week task calendar (`tools/make_weeks.py`) saved in her private HQ space. Each week's tasks drop into a "Launch plan" list on her HQ to-dos.
4. **Weekly check-in.** Every Monday morning Claude reviews what she finished and how her sales and ads look against her targets, adjusts the coming week, adds that week's tasks, and leaves 3 short check-in notes on her HQ.

## What's in here

| File | What it is |
|---|---|
| `questionnaire.md` | The intake questions, grouped, with why each one matters and what it feeds |
| `method.md` | Bryton's strategy as rules: offer ladder, pricing, content tiers, the ad rule, gates, targets and check-in adjustments |
| `skills/hq-growth-plan/SKILL.md` | Draft skill: runs the questionnaire in chat, builds the plan, saves it, adds week 1 |
| `skills/hq-plan-checkin/SKILL.md` | Draft skill: the Monday check-in (review, adjust, add the week's tasks) |
| `tools/plan_model.py` | Projection model: answers in, monthly sales, members, ads, costs, profit and targets out |
| `tools/make_weeks.py` | Task calendar generator: answers in, the `launchplan` document out |
| `examples/intake-example.json` | A filled-in sample questionnaire to test with |

Try it with the example:

```
cd growth-plan/tools
python3 plan_model.py ../examples/intake-example.json        # projection and targets
python3 make_weeks.py ../examples/intake-example.json out.json  # task calendar
```

## Where things live in her HQ (private space, page link in `plugins/hot-mess-hq/reference/hq-map.md`)

| What | `collection` | `doc_id` |
|---|---|---|
| Her questionnaire answers | `data/users/me/hq/dash` | `planintake` |
| Her plan: weeks, tasks, targets, check-ins | `data/users/me/hq/dash` | `launchplan` |
| The "Launch plan" to-do list | `data/users/me/hq/dash` | `lists` (`custom: [{id: "launch", name: "Launch plan"}]`, keep her other lists) |
| Her plan tasks and check-in notes | `data/users/me/hq/items` | `launch-wNN-NN`, `review-<date>-N` |

The page already shows any to-do with a `due` date on her Today screen when that day comes, and shows custom lists, so no page change is needed for the tasks. `launchplan` has the same shape as Bryton's own plan (weeks, added, targets, reviews).

## Rolling it out (when ready)

1. Move `skills/hq-growth-plan` and `skills/hq-plan-checkin` into `plugins/hot-mess-hq/skills/`, and copy `method.md`, `questionnaire.md` and `tools/` into the hq-growth-plan folder (the skills read them from there).
2. Add the three rows above to `plugins/hot-mess-hq/reference/hq-map.md`.
3. Add the Monday job to hq-setup's scheduled jobs (task id `hot-mess-hq-plan-checkin`, cron `47 5 * * 1`, prompt: "Use the hq-plan-checkin skill from the hot-mess-hq plugin."), only with her OK.
4. Optional: a "Build my growth plan" button on the page that sends a `growth-plan` request, and a form version of the questionnaire.
5. Raise the plugin version, `claude plugin validate .`, commit and push.

Bryton's own plan runs separately: her answers are hers, her plan lives in her private space, and her Monday check-in is a cloud scheduled task ("Monday launch plan and check-in").

## Before selling it

- The projection is a planning model with assumptions (cost per buyer, upgrade and join rates, churn). Every plan should say that in plain words, and clients should replace the assumptions with real numbers after 60 to 90 days.
- No income promises: show the plan as "if these numbers hold", with a weaker case beside it.
- Have a lawyer look at how plan results are described in sales copy.
