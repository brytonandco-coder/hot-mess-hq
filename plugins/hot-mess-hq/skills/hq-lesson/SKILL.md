---
name: hq-lesson
description: Edits her course lessons, tutorials and YouTube videos (16:9) for the Lessons tab of her Hot Mess HQ Content Studio, in her Brand Brain look. Screen recordings get zooms, circles, step cards, tip cards and blurring of anything private; on-camera lessons get graphics beside her, chapter cards and an end card. Used by hq-requests for "lesson-make" and "lesson-notes" requests, or when she says "edit my lesson".
---

# Lessons for Hot Mess HQ

First read `../../reference/hq-map.md` (Brand Brain rules, and "Studio makers") and `~/Hot Mess HQ/settings.md` (her Raw videos folders: look in all of them for the file name). Use the hyperframes skill for building, transcribing and rendering. Lessons are 1920x1080.

## Always

- **Never cut her words.** Only trim pauses, leaving a little breathing room on both sides so nothing gets clipped. Play at 1.05x.
- Voice: `highpass=f=80,afftdn=nf=-25,deesser,acompressor=threshold=-20dB:ratio=3`, then loudness about -11.5 LUFS with a limiter at -1 dB.
- Soft sound effects on graphics, well under her voice. Captions (unless `makeprefs.captions` is false) in a band underneath, one highlighted word per line in her `accent`.
- Transcribe with `npx hyperframes transcribe` first; every graphic lands on her exact word.

## A. Screen recording

- The recording sits in a framed window (rounded corners, soft shadow) on a background in her colors, captions underneath.
- **Zoom** in on exactly what she clicks or points to (find the cursor and the clicked element in the real frames), and draw a hand-drawn circle around the button or link she names.
- **Step cards:** a "STEP n" title card between steps that pauses the picture and her voice for about 1.8 seconds, plus a small step label in a corner that never covers what she's clicking.
- **Tip cards** in a corner for anything she skipped, mis-said or should explain more (she won't refilm).
- Full-screen graphics over long stretches where the screen doesn't change.
- **Privacy, every frame:** blur the screen recorder's control bar if it shows, and blur API keys, passwords, tokens, email addresses and payment details. Scan every frame (read the text on frames at least twice a second), not a sample.

## B. On camera

- She sits in a framed card on one side; graphics play beside her. For big visuals her card shrinks to a corner, then grows back.
- Every idea gets a graphic that acts it out on her word: lists that tick, numbers that count up, screenshots, her own clips, before and after.
- Chapter title cards, and an end card pointing to the next lesson if the request names one.

## Check before rendering

`npx hyperframes check` and fix every error. A still at every zoom and circle: it must land on the right thing in the real frame, and no card may cover what she's clicking. A still in every graphic: no cut-off text or overlaps. Render with `-w 1`.

## Save and deliver

Full file to `Hot Mess HQ files/Lessons/NN-topic.mp4`; a phone-sized copy under 15 MB for the page. Deliver per the map with `size: "16:9"` and `scenes` = chapters and steps with their start seconds. The reply says how long it is and what you added (zooms, step cards, tip cards, anything blurred).

## Notes

Notes with a second. Quick changes: **Zoom in closer**, **Add a tip card here**, **Slower step cards** (2.5 s), **Less text**, **Blur something private here** (find it at that second and in every other frame where it shows). Re-render, bump the revision.
