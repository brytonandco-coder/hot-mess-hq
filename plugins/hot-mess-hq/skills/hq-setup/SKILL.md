---
name: hq-setup
description: Connects this Claude to her Hot Mess HQ page and turns on its background jobs (requests from the page, inbox sweep, morning weather), one question at a time and only with her OK. Use when she says "set up Hot Mess HQ", "connect my HQ", "turn on my helpers", "my HQ isn't updating", or when another Hot Mess HQ skill finds no settings file.
---

# Set up Hot Mess HQ on this computer

First read `../../reference/hq-map.md` (the map of her page and private space).

She probably got here from the "Finish setting up" checklist on her Morning Briefing, after pasting "Set up Hot Mess HQ". Talk in short, plain sentences. Ask one question at a time and wait for her answer. Assume she has never used a terminal.

## 1. Check the page connects

1. ArtifactData `get`, `url` = the page, `collection` `data/users/me/hq/dash`, `doc_id` `profile`.
   - Found with a `name`: say "Hi <name>, I can see your Hot Mess HQ." and go on.
   - Not found: say "Open your Hot Mess HQ page once and answer the welcome questions, then come back and say set up Hot Mess HQ." Stop.
   - The tool is missing or refuses: say "I can't reach your Hot Mess HQ from here. Make sure you're signed in to the same Claude account you open Hot Mess HQ with." Stop.
2. Check the connectors she'll need, without changing anything: Gmail (inbox sweep), Google Drive (videos and files). For any that's missing, say in one sentence what it adds and that she can connect it in Claude's settings under Connectors. Carry on without it.

## 2. Her folders (only if she wants video edits)

Ask: "Do you want me to edit your videos for The Studio?" If no, skip to step 3.

If yes:
1. Ask whether she has Google Drive for desktop on this computer (a "Google Drive" or "My Drive" folder in File Explorer or Finder). Look for it yourself first: `G:/My Drive`, `~/Google Drive/My Drive`, `~/Library/CloudStorage/GoogleDrive-*/My Drive`.
2. First look for folders she already drops videos into (names with "raw", "video" or "footage", and where her phone's Google Drive uploads land) and ask: "Is this where your videos from your phone go?" Keep every yes as a Raw videos folder; editing reads all of them, so she never has to move a file. Then in her Drive make (or find) the folder `Hot Mess HQ files`, and inside it `Raw videos` and `Finished videos`. With Drive for desktop, make them on disk. Without it, use the Google Drive connector's `create_file` with the folder mime type `application/vnd.google-apps.folder`, and tell her editing will need the files on this computer: big videos can't pass through the connector.
3. Ask: "Want reaction GIFs in your videos? It needs a free GIPHY key." If yes, walk her through it one step at a time: developers.giphy.com, sign in or make a free account, Create an App, pick API, copy the key. Have her paste it into a new file `~/Hot Mess HQ/.env.giphy` as `GIPHY_API_KEY=<key>` (open it for her in Notepad or TextEdit), so it never goes through the chat. Test it with one search inside a script that never prints the key.
4. Ask which video editing skill she uses, if any (for example one she made in Bryton's video brand lesson). If none, the hq-video skill does a simple clean edit.

## 2b. Her Brand Brain

`get` `data/users/me/hq/dash` / `brand`. If `done` is true, say "I've got your Brand Brain: <business>, <her colors as names>." and move on.

If not, explain in one sentence: "Your Brand Brain tells me your colors, logo, fonts and voice, so every effect, caption and note I make looks and sounds like you." Then ask: "Want to fill it in on your page (the Brand Brain button in The Studio), or answer it here with me?"
- On the page: tell her where it is and carry on.
- Here: follow the hq-brand skill, part A.

## 3. Save her settings

Write `~/Hot Mess HQ/settings.md` (make the folder):

```
# Hot Mess HQ settings (made by the hq-setup skill)
Page: <the page link from the map>
Name: <her name>
Google Drive on this computer: <path or "none">
Raw videos (look in all of these, newest first):
- <path or Drive folder id>
- <each folder she already uses>

Finished videos: <path or Drive folder id>
Video editing skill: <skill name or "simple clean edit">
Set up: <today's date>
```

## 4. Turn on the background jobs

Explain in two sentences: "These run by themselves while the Claude app is open on this computer. They only read your email, never send or delete anything." Then ask her OK for each one (one question listing all three is fine: "Turn on all three?").

Use the scheduled-tasks tools. Before creating, `list_scheduled_tasks`; if a task id already exists, update it instead of making a second one.

| taskId | cron (her local time) | prompt |
|---|---|---|
| `hot-mess-hq-requests` | `0 8-20/2 * * *` | `Use the hq-requests skill from the hot-mess-hq plugin to pick up new requests from my Hot Mess HQ page. Work quietly.` |
| `hot-mess-hq-inbox-sweep` | from her email check times (below) | `Use the hq-inbox-sweep skill from the hot-mess-hq plugin. Read-and-note only.` |
| `hot-mess-hq-weather` | `0 6 * * *` | `Use the hq-weather skill from the hot-mess-hq plugin to put today's forecast on my Hot Mess HQ.` |

Email check times: ArtifactData `get` `data/users/me` / `mailprefs`. Hours = `start`; twice = `start, start+6`; three times = `start, start+4, start+8` (start defaults to 8, freq to 2). Cron `0 <hours> * * <1-5 if skipWeekends else *>`. If `freq` is 0, don't make the inbox task. After saving the task, `update` mailprefs (with `if_version`) to `sync: "done"` and `synced` = the value in its `requested` field (if there is one).

Skip the weather task if `dash/weather` has no `place`; say she can add her town on the Morning Briefing any time and then ask you to turn the weather on.

If a task can't be created (the tool is missing or refuses), don't work around it. Tell her the job is off and that she can say "check my HQ" any time to run it by hand.

## 5. Run each one once now

Run hq-requests, then hq-weather (if on), then hq-inbox-sweep (if on), so she sees it work. Then tick the "Turn on your helpers" step of the setup checklist on her page: ArtifactData `update`, `collection` `data/users/me/hq/dash`, `doc_id` `profile`, `data` `{"helpersOn": "<today as YYYY-MM-DD>"}` (merge, keep her other fields). Then say what's on, in a short list, and: "Open your Hot Mess HQ to see it."
