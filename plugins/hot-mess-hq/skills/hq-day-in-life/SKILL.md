---
name: hq-day-in-life
description: Cuts her phone clips into a Day in the life reel in the style she saved on the Day in the life tab of her Hot Mess HQ Content Studio (cozy, fast and fun, clean, or home movie), with words on screen and music in her Brand Brain look, and applies her notes. Used by hq-requests for "ditl-make" and "ditl-notes" requests, or when she says "make my day in the life".
---

# Day in the life for Hot Mess HQ

First read `../../reference/hq-map.md` (Brand Brain rules, and "Studio makers") and `~/Hot Mess HQ/settings.md`. Use the hyperframes skill for building and rendering.

## 1. Gather the clips

Her clips are in `Hot Mess HQ files/Day in the life clips` in her Google Drive (create the folder if it's missing, and tell her it's there), plus any uploaded in the request. Use the clips added since her last Day in the life video (the newest batch). Never move, rename or delete her clips. Look at a few frames of each to know what's in it, and sort them into the order of her day (the request may list it; otherwise morning to night by what you see and the file times).

## 2. Her style

From `makeprefs.ditl.style`:
- **cozy** (Cozy and calm): 2 to 3 seconds a clip, soft cross-fades, slow push-ins, a warm grade, small lowercase words in her heading font, soft acoustic music.
- **fun** (Fast and fun): 0.6 to 1.2 seconds a clip, cut on the beat, quick zoom moves, punchy color, bold words that pop in her `main` and `accent`, upbeat music.
- **clean** (Clean and simple): about 1.5 seconds a clip, straight cuts, a neutral grade, one small line of text with lots of space, light piano.
- **film** (Home movie): about 2 seconds a clip, film grain and a slightly faded warm grade, the date small in a corner in a typewriter font, handwritten-style words, dreamy lo-fi music.
- If she linked a reel she loves (`makeprefs.ditl.example`), match its pacing, cut rhythm and how text sits, never its words, pictures or music.

## 3. Build it

- Words on screen tell the day in short bits ("7:02 am", "school run", "client call #2"), timed to their clip, kept out of the top 220px, the right 140px and the bottom 380px.
- The message she gave goes on the last 2 to 3 seconds, bigger. Her logo small at the end if her Brand Brain has `endLogo`.
- Music: royalty-free only (the hyperframes media-use free library), fitting the style, faded in and out. Keep a clip's own sound only where someone is talking, with the music ducked under it.
- Steady shaky clips lightly (`deshake`), match the grade across clips, and crop to her size (9:16 1080x1920 unless she picked another) keeping the action in frame.
- Keep children's faces and names out of any words you add.
- `npx hyperframes check`, a still in every section (no cut-off words), render with `-w 1`, then a phone-sized copy.

## 4. Save and deliver

`Hot Mess HQ files/Day in the life/NN-topic.mp4`. Deliver per the map, `scenes` = each part of her day with its start second. The reply says how long it is and which clips you used.

## Notes

Quick changes: **Faster cuts**, **Slower and calmer**, **Different music**, **Bigger words**, **Use a different clip here** (swap the clip at that second for another from the batch). Re-render, bump the revision.
