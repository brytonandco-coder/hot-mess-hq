---
name: hq-growth-plan
description: Builds her custom growth plan with Bryton's method. Asks the Growth Plan questionnaire (her business, offers, numbers, audience, ad budget, time, goals), designs her offer ladder, content plan and self-funding ad plan, projects month by month, saves the plan to her Hot Mess HQ and puts the first week's tasks on her to-do list. Use when she says "build my growth plan", "make me a launch plan", "plan my launch", or sends a growth-plan request from the page.
---

# Build her growth plan

First read `../../reference/hq-map.md`, then `method.md` and `questionnaire.md` in this folder. The method is Bryton's strategy; apply it, don't invent a different one. (When this skill moves into the plugin, copy `method.md`, `questionnaire.md` and `tools/` from `growth-plan/` into this folder.)

Talk in short, plain sentences. One section of questions at a time. Rough numbers are fine; "I don't know" gets the default from the questionnaire.

## 1. Start

- `get` `dash/planintake`. If it has answers, say "I've got your answers from <date>. Want to update anything, or build from these?"
- `get` `dash/launchplan`. If a plan already exists, ask before replacing it: "You already have a plan running. Start a new one, or adjust the one you have?" Adjusting = the hq-plan-checkin skill.
- `get` `dash/brand` and `dash/memory` and use what's there instead of asking again (her business, audience, offers).

## 2. The questionnaire

Ask `questionnaire.md` sections 1 to 7 in order, skipping anything the Brand Brain or memory already answers. After each section, `set` or `update` `dash/planintake` with the fields so far (so nothing is lost if she stops), plus `updatedAt`.

## 3. Design the plan (method.md)

Work out, and show her in a short message before saving anything:
- **Her offer ladder:** front offer (12-week program), upgrade (with 1:1) and continuity offer, with names, prices and what's in each. Keep what she already sells where it fits; say why for anything you'd change.
- **Her content tier** from her hours, and what that means each week.
- **Her ad rule:** $<adPocket> a month out of pocket until income covers it, then <adShare> of last month's income, never more than $<adCap>.
- **The timeline:** prep weeks, catch-up weeks for her blackout dates, launch day.
- **The projection:** run `python3 tools/plan_model.py <intake file> <out file>` with her answers (write `dash/planintake` to a temp JSON first, adding a `ladder` object with the names and prices she agreed to and `firstMonth` = launch month). Show month 12 profit, year 1 profit, the month she reaches her goal, and the slower case beside it. If Python isn't available, explain that the projection needs it and skip to saving the calendar with targets left empty.

Say plainly: "These are planning numbers, not a promise. Every Monday I swap in your real numbers." Ask: "Want me to set this up in your HQ?" Wait for yes. Change anything she asks first.

## 4. Save it

1. Run `python3 tools/make_weeks.py <intake file> <plan file>`. Without Python, build the same weeks by hand from method.md section 5.
2. `set` `dash/launchplan` from the plan file (it has `weeks`, `added: []`, `reviews: []`, `targets`, `timezone`, `routine`). Use `file_path`.
3. The "Launch plan" list: `get` `dash/lists`. Add `{id: "launch", name: "Launch plan"}` to `custom` if it isn't there, keeping her other lists, `hidden` and `names`. Create the doc if it's missing.
4. Add the current plan week (the week whose `monday` is this Monday, or the first week if the plan starts later and it begins within 7 days): one doc per task in `data/users/me/hq/items`, doc id = the task `id`, `{text, bucket: "launch", due, quick, done: false, sample: false, createdAt: <now ms>, plan: "launch"}`. Use one batch. Then `update` launchplan with that week in `added`.
5. Optional, if she wants to keep it: a Claude Doc of her plan (summary, offer ladder, content plan, ad rule, the month-by-month table, the slower case).

## 5. Turn on the Monday check-in (only with her OK)

Explain in two sentences: "Every Monday morning I'll look at what you got done and how your sales and ads look, adjust your week, and add the week's tasks. It runs while the Claude app is open on your computer."

Then, using the scheduled-tasks tools (`list_scheduled_tasks` first; update instead of duplicating):

| taskId | cron (her local time) | prompt |
|---|---|---|
| `hot-mess-hq-plan-checkin` | `47 5 * * 1` | `Use the hq-plan-checkin skill from the hot-mess-hq plugin.` |

If her computer is usually off early Monday, suggest a later time on her first work day. If the task can't be created, say she can say "do my Monday check-in" any time.

## 6. Finish

Short list: her offers and prices, her weekly content, her ad rule, launch day, and "Week 1 is on your Launch plan list." Then: "Open your Hot Mess HQ to see it."

## Rules

- Her answers, her numbers and her plan are private: they stay in `data/users/me/hq`. Never put them in a file, post or anything someone else can see.
- No income promises. Always show the slower case, and call the numbers estimates.
- Never write account numbers, passwords or card details into her space.
