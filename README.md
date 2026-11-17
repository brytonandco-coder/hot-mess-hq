# Hot Mess HQ helpers

The helpers behind Hot Mess HQ. They run inside your own Claude app on your computer, and they only work with your private Hot Mess HQ page (you need an invite to it).

## Install

You don't need to type any of this yourself. Open your Hot Mess HQ page, and the **Finish setting up** checklist on your Morning Briefing gives you a message to copy and paste into the Claude app (Code tab). Claude installs everything for you.

If you'd rather do it by hand, in the Claude app's Code tab:

```
/plugin marketplace add brytonandco-coder/hot-mess-hq
/plugin install hot-mess-hq@hot-mess-hq
```

Then start a new chat and say **Set up Hot Mess HQ**.

## What's inside

One plugin, `hot-mess-hq`:

| Skill | What it does | When |
|---|---|---|
| `hq-setup` | Connects your Claude to your HQ, finds your folders, turns on the helpers (with your OK) | Once, "Set up Hot Mess HQ" |
| `hq-requests` | Picks up what you sent from the page: new video, video notes, email check times, recipes | Every 2 hours, 8am to 8pm |
| `hq-inbox-sweep` | Reads your email (never sends or deletes) and puts what needs you on the page | Your chosen times |
| `hq-weather` | Today's forecast and one nudge on the Morning Briefing | 6am |
| `hq-video` | First edit and revisions of your videos, saved to your own Google Drive | When you ask from the Content Studio |
| `hq-brand`, `hq-business`, `hq-carousel`, `hq-kitchen` | Brand Brain, business numbers, animated carousels, recipes and grocery lists | When you ask from the page |

The helpers only run while the Claude app is open on your computer.

## For Bryton: shipping an update

Edit the files here, raise `version` in `plugins/hot-mess-hq/.claude-plugin/plugin.json`, check with `claude plugin validate .`, then commit and push. Everyone with auto-update gets it the next time their Claude app starts.
