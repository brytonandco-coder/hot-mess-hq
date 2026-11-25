---
name: hq-plan-checkin
description: The Monday check-in for her growth plan. Reviews last week's launch tasks and her sales, ads and list numbers against her plan's targets, makes small adjustments with Bryton's rules, adds this week's tasks to her Hot Mess HQ Launch plan list and leaves three short check-in notes. Runs early Monday, or when she says "do my Monday check-in", "check my plan" or "add this week's tasks".
---

# Monday check-in

First read `../../reference/hq-map.md` and section 7 of `method.md` (in the hq-growth-plan skill folder).

Her to-dos are in `data/users/me/hq/items`. Only docs whose id starts with `launch-` or `review-` are yours. Never change or delete any other to-do, never delete a launch task and never untick one. Unfinished tasks from past weeks stay as they are (they keep showing on her Today screen); don't duplicate them. Every write to an existing doc passes `if_version`.

Times are her `launchplan.timezone`. "Today" is this Monday (if run on another day, use this week's Monday).

## 1. Read

- `dash/launchplan` (keep the version). No plan: stop with "No plan yet. Say build my growth plan to make one."
- `dash/biz` (her business numbers: sales, crm, ads, list, each with `updatedAt`), `dash/brand` (her voice).
- Query `items` where `plan == "launch"`.

## 2. Check in on last week

The plan week whose `monday` is 7 days before today. Skip if it isn't in `added`.
- Done vs total for that week's launch tasks. One real win, and what slipped.
- From launch month on: compare `dash/biz` (sales this month, ad spend and cost per result, list growth, leads) with this month in `targets.months` and with the last entry in `reviews`. If `dash/biz` is missing or older than 8 days, plan the quick to-do "Update your business numbers (tell Claude: update my business numbers)". Don't guess numbers.

## 3. Adjust (small changes, each explained in one line)

- Under 60% done: move up to 2 non-essential tasks out of this week into a later week in `launchplan`. Never move launch day, workshops, legal, checkout, lessons or the group call.
- Content tasks missed 2 weeks running: drop this week to the next lighter content tier (method.md section 2) and change this week's tasks to match.
- Cost per buyer above `targets.costPerProgramBuyer.holdAbove` for 2 weeks, or refunds above `targets.refundsMax`: add "Hold ad spend this week and fix the ad, workshop or page" to this week.
- Sales at or above target and cost per buyer under the hold line: note she can spend the full share of last month's income on ads this month.
- Sales behind target 2 months running: add "Test a new workshop title and offer ending".
- On track: change nothing and say so.

## 4. Add this week's tasks

The plan week whose `monday` is today, if it isn't in `added`: one doc per task, doc id = task `id`, `{text, bucket: "launch", due, quick, done: false, sample: false, createdAt: <now ms>, plan: "launch"}`, in one batch. Past the last planned week, build the week from `launchplan.routine` (her weekly content routine) plus: check ads (Monday, quick), the weekly group call, a free workshop every other week (weekly from month 7), the monthly Q&A on the first work day of the month that falls on her group call day, and a monthly numbers review in the last week of each month. Ids `launch-wNN-NN`; append the week to `weeks`.

## 5. Check-in notes on her HQ

Up to 3 to-dos, ids `review-<today>-1..3`, bucket `launch`, due today, quick, `plan: "launch"`, each under 160 characters:
1. "Last week: X of Y done. <one real win>."
2. "Numbers: <the one number that matters vs plan>." (skip before launch month)
3. "This week: <the focus or the one change>."

Warm, plain, a little playful, never guilt. Her voice from the Brand Brain if it's done. No em dashes.

## 6. Save

`update` `dash/launchplan` with `if_version`: the week added to `added`, a new entry in `reviews` `{week, monday, at, done, total, numbers, summary, changes}`, and any task changes from step 3.

## 7. Finish

2 or 3 short sentences: what got done, the key number, this week's focus. If something failed (no access to the page, a refused write), say exactly what and stop. Scheduled run: one PushNotification with the same sentences.
