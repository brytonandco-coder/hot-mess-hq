---
name: hq-stories
description: Makes an Instagram story sequence that sells (3 to 7 frames, 9:16) for the Stories tab of her Hot Mess HQ Content Studio, in her Brand Brain look, and applies her frame-by-frame notes. Used by hq-requests for "story-make" and "story-notes" requests, or when she says "make stories for my offer", "turn my video into stories" or "do my story notes".
---

# Stories for Hot Mess HQ

First read `../../reference/hq-map.md` (Brand Brain rules, and "Studio makers" for where things go and how to deliver). Use the hyperframes skill for building and rendering.

## 1. Plan the story

From the request: what she sells, the link, where to start (her offer, her latest Studio video, or a topic), details, how many frames, which sticker, and any example screenshots.

A story that sells moves in this order, squeezed to fit the frame count: **hook** (stop the tap-through: a question or a bold line about her buyer's problem), **the problem** (how it feels, in her buyer's words), **the answer** (her offer, named), **proof** (a real result, testimonial or screenshot she gave you; if she gave none, use a placeholder frame and ask for one in the reply), **the offer** (what they get, price only if she gave it), **the ask** (one clear action). Three frames = hook, answer, ask.

- One idea per frame, readable in 2 seconds: a headline of 3 to 8 words, at most one short line under it.
- From her latest video: pull the hook and one or two strong lines from its transcript; the ask is "watch the full video" with the link sticker.
- Example screenshots: copy their structure, pacing and how text sits on the frame. Never their words, pictures, prices or logo.
- Only claims and numbers she gave you or that are in her Brand Brain or memory. Never invent results or testimonials.

## 2. Build each frame

1080x1920, 5 to 8 seconds each, her Brand Brain colors, fonts and logo:
- **Safe area:** nothing important in the top 250px or the bottom 340px (Instagram's name bar and reply bar).
- **Motion:** a headline rises in word by word, a checklist ticks, a price pops with a little bounce, a before and after wipes, a quote fades in line by line. Something moves slowly in every frame. Hold the finished frame still and readable for the last 2 seconds.
- **Her clips and photos:** if she named a video or added photos, use them as the background of a frame with a soft dark layer under the text so it reads.
- **The ask frame:** leave a clearly marked empty spot (a dashed rounded box with a small "your sticker here" label in her `main` color, about 600x220, centred around y=1300) for Instagram's sticker, which can't be built into a video. Pick the sticker if she let you: link sticker when there's a link, poll for "which one are you", question box for "ask me anything about...". Put it in the doc's `sticker` field as one plain line, like "Link sticker on frame 5 in the dashed box, pointing to <link>".
- No sound by default (most people watch stories muted), unless the frame uses her own clip.

## 3. Save and deliver

Render each frame to MP4 (`-w 1`). Save to `Hot Mess HQ files/Stories/NN-topic/` as `frame-01.mp4`, `frame-02.mp4`... plus `all-frames.zip`. Deliver per the map: `parts` = one per frame with `label` (Hook, Problem, Offer...), `zip`, `sticker`, `size: "9:16"`.

## Notes

Notes name the frame ("frame 3: bigger price"). Quick changes mean: **Stronger hook** = rewrite frame 1 sharper and more specific; **Shorter text** = cut every frame's words by about a third; **Make the offer clearer** = say exactly what they get and what to do; **Add a frame** = add the missing beat (usually proof); **Change the order** = apply a better order and say it in the summary. Re-render only the frames that changed, rebuild the zip, bump the revision.

## Rules

- Her words and her offer only. Never Bryton's brand for a client.
- Never post anything. It goes to her Drive and her page.
