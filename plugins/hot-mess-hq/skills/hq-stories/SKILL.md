---
name: hq-stories
description: Makes the story version of something she made in her Hot Mess HQ Content Studio (her edited video, Voice to Video, lesson, Day in the life reel or carousel), either reused as 2 to 5 story frames or as a 3 to 7 frame story sequence that sells her offer, in her Brand Brain look, and applies her frame-by-frame notes. Used by hq-requests for "story-make" and "story-notes" requests, or when she says "make a story version", "turn my video into stories" or "do my story notes".
---

# Story versions for Hot Mess HQ

First read `../../reference/hq-map.md` (Brand Brain rules, and "Studio makers" for where things go and how to deliver). Use the hyperframes skill for building and rendering.

Any words you write for her audience (hooks, on-screen words, headlines, captions) follow the map's "Her marketing method" section as well as her voice. Her own words and notes are never rewritten to fit it.

Stories aren't a tool of their own: every finished video and carousel in the Content Studio has a **Make a story version** button. The request says what it was made from and where to save the result: `makes/story-<src>` (src = video, voice, lesson, ditl or carousel). Deliver to that doc, not `makes/story`.

## 1. Plan the story

From the request: what it was made from (title, Drive or asset id, what's in it), the kind (**story version of this** or **sell my offer with it**), what she sells, the link and the sticker.

**Story version of this (reuse, 2 to 5 frames):** use what she made, don't start over.
- A video: cut its strongest 5 to 15 second moments into frames (the hook first, the payoff last). It's already 9:16 if it was a reel; a 16:9 lesson gets reframed to keep her and the action in view. Re-place any words so they sit inside the story safe area, and add short on-screen words (many people watch stories muted). The last frame invites them to the full post ("New video, tap to watch") with the sticker spot.
- A carousel: each slide (4:5) sits on a 9:16 background in her colors with a little room above and below, gently animated; 3 to 5 of the strongest slides, the last one with the sticker spot.

**Sell my offer with it (3 to 7 frames):** a story that sells, using what she made as the proof or the hook (below).

A story that sells moves in this order, squeezed to fit the frame count: **hook** (stop the tap-through: a question or a bold line about her buyer's problem), **the problem** (how it feels, in her buyer's words), **the answer** (her offer, named), **proof** (a real result, testimonial or screenshot she gave you; if she gave none, use a placeholder frame and ask for one in the reply), **the offer** (what they get, price only if she gave it), **the ask** (one clear action). Three frames = hook, answer, ask.

- One idea per frame, readable in 2 seconds: a headline of 3 to 8 words, at most one short line under it.
- Use what she made: its hook, a strong line from its transcript, or a slide, as a frame.
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
