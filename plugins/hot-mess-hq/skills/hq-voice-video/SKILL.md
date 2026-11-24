---
name: hq-voice-video
description: Turns her voice memo into a whole branded video with nobody on camera, for the Voice to Video tab of her Hot Mess HQ Content Studio. Cleans her voice, builds scenes that act out every line on her exact words, adds sound effects and captions in her Brand Brain look, and applies her notes. Used by hq-requests for "voice-make" and "voice-notes" requests, or when she says "make a video from my voice memo".
---

# Voice to Video for Hot Mess HQ

First read `../../reference/hq-map.md` (Brand Brain rules, and "Studio makers" for where things go and how to deliver) and `~/Hot Mess HQ/settings.md` (her folders). Use the hyperframes skill for building, transcribing and rendering. Her voice sets the timing: never build a silent version and fit her voice to it afterwards.

Any words you write for her audience (hooks, on-screen words, headlines, captions) follow the map's "Her marketing method" section as well as her voice. Her own words and notes are never rewritten to fit it.

## 1. Get the memo

From the request: the memo (an uploaded file id, or a file name in her Raw videos folders), what it's about, the size (9:16 = 1080x1920, 4:5 = 1080x1350, 16:9 = 1920x1080) and captions yes or no. Any audio or video file works; take only the sound. Never move or delete her original (only a "raw-cleanup" request, hq-video part E, clears it out later).

Remember the memo you used: `update` `makes/voice` with `sources: [{name, driveId, folder}]` (her Drive id for the file, and the folder it was in; an uploaded page asset has no Drive file, so leave it out). Once the video is scheduled or posted, her page asks her whether to delete it.

## 2. Clean her voice

With ffmpeg, in this order:
- Clean her voice with `../../reference/voice-cleanup.md` (DeepFilterNet, light unless she picked strong), then the polish step in that file.
- Pauses: every pause longer than 0.15 seconds becomes a short breath (about 0.12 s). Start right on her first word. Check the cuts against the transcript so no word loses its start or end.
- Speed: up to 1.05x with `atempo`, never faster.
- Loudness about -15 LUFS (`loudnorm=I=-15:TP=-1.5`).
- **Never cut her words.** If she said a line twice, keep the better take (clearer, fewer stumbles) and say in the reply which one you kept.

## 3. Transcribe and plan

`npx hyperframes transcribe` on the cleaned voice for word timings. Plan one scene per line, each acting out what she says, timed to her exact words:
- a point = a big headline; naming things = a list that ticks as she names each one; a number = it counts up; a conversation = a chat window that types; posting = a phone that posts; a change = before and after; her screenshots, photos or clips if she gave any. Anything you need and don't have: a clean placeholder, and ask for it in the reply.
- Something new every 1 to 2 seconds, and slow movement (drift, zoom, parallax) in every scene so nothing sits still.
- 2 or 3 full-screen moments on her biggest lines: the name of the thing, a big number, the finished result.

## 4. Build it

In her Brand Brain colors, fonts and logo:
- **Sound effects** on the graphics (pop, swoosh, click, typing, a soft ding on the payoff), clearly audible but always under her voice (about 12 to 16 dB below). Every audio and video element needs an id, or it renders silent or frozen.
- **GIFs:** if `~/Hot Mess HQ/.env.giphy` has a key, 1 to 3 reaction GIF stickers that fit the moment (no TV or movie clips), fetched the way hq-video does it. Never show the key.
- **Captions** only if she said yes: a band near the bottom, one highlighted word per line in her `accent`.
- **Safe areas:** keep text out of the top 220px, the right 140px and the bottom 380px (Instagram covers them); for 16:9 keep 80px clear all round.
- The video ends right after her last word. No extra seconds.

## 5. Check before rendering

- `npx hyperframes check`, and fix every error.
- A still inside every scene: fix cut-off text, overlaps, and anything in the covered areas.
- Render with `-w 1`, then make a phone-sized copy (`-crf 24 -maxrate 5M`).

## 6. Save and deliver

`Hot Mess HQ files/Voice videos/NN-topic.mp4` (and the phone copy). Deliver per the map: `parts` = the video, `scenes` = one line per scene with its start second, `size`. The reply says how long it is and anything she should send (photos for placeholders, which take you kept).

## Notes

Plain-English notes with a second ("at 0:14: bigger headline"). Quick changes: **Bigger headlines**, **Less text** (cut on-screen words by about half, keep the headline), **More movement**, **Use a photo of me here** (placeholder until she sends one; ask for it), **Quieter sound effects** (down 4 dB). Change only what she asked, re-render, bump the revision.
