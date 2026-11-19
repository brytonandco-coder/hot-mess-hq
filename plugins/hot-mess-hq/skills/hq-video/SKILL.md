---
name: hq-video
description: Edits her videos for The Studio on her Hot Mess HQ page. Does the first edit of a new raw video from her Raw videos folder, saves it to her own Google Drive, hangs Claude's edits on the line as tags, sends her to her final pass, then applies her review notes as revisions. Used by hq-requests for "new-video" and "video-notes" requests, or when she says "edit my new video for my HQ" or "do my Studio notes".
---

# Videos for The Studio

First read `../../reference/hq-map.md` and her `~/Hot Mess HQ/settings.md` (folders and her video editing skill). No settings file: tell her to say "set up Hot Mess HQ" first, mark the request `skipped` with that reply, and stop.

Her videos live in **her own Google Drive**, never on the page itself (the page is shared by many moms; only her Drive is private to her). The page plays the preview from her Drive by its file id.

## Her private Studio page (My Studio)

If settings list a **My Studio** page, her video editing lives there instead of on the shared HQ: a private page only she can open, built from the same Studio parts (`studio/index.html` in the dashboard folder). On it:
- The same docs sit at the page's top level: `dash/video`, `dash/videojob`, `notes` (not under `data/users/me/hq/`).
- Videos can go in the page's own asset store (it's private): upload the preview with the Artifact tool (`publish`, `asset: true`, the Studio `url`) and set `assetId`. Keep the full-quality file in her Drive (`downloadId`).
- **Send to Claude** posts a comment that starts "Review notes for…" and reaches the Claude chat watching the page. Start right away, no need for her to say anything. Do part B with these paths, keeping `dash/videojob` moving (editing with progress, then ready) so her page shows each step, and reply on the comment thread with one line when the new revision is up, then resolve it.
- A chat only hears Send while it watches the page: when she starts a new chat for video work, call ArtifactComments `watch` on her Studio `url` once (or republish it) and tell her Send now comes to this chat.
- Anything else (her Brand Brain, the HQ's requests) stays on the HQ page as before.

## How to edit

- **Her brand first:** read her Brand Brain (`dash/brand`, `dash/brandlogo`; rules in the map). Every title, caption, effect, graphic and end card you add uses her colors and fonts, not Bryton's and not the Hot Mess HQ page's. Captions follow `captions` (clean = small, sentence case, `dark` on a soft `light` pill or white with a shadow; bold = big chunky words, key word in `main` or `accent`; fun = bouncy pop-in, alternating `main` and `accent` highlights). How much to add follows `effects` (subtle = only what she asked for; some = her asks plus 2 or 3 of your own; lots = her asks plus a few more, still never over her face). Words you put on screen and the hook follow her voice. Her logo goes on the last 2 seconds when `endLogo` is true. If her own video editing skill sets colors or fonts, the Brand Brain wins where they differ (she filled it in more recently), unless she says otherwise.
- **Effects she picked in The Studio** (notes like "Add: Sparkle title" with what she typed) are built in her colors:
  - *Sparkle title:* the word glows behind or above her: dark background from her `dark` toward `main`, slow rotating rays in `accent` at about 20%, the word in her heading font, colored `accent` mixed 60% toward white, with a two-layer `accent` glow (text-shadow 8px and 22px) that pulses, and 3 white four-point stars twinkling around it. *Sparkle burst:* small dots in `accent` and `extra` (or `main`).
  - *Words, highlights, arrows, circles, checklists, stat cards, progress bars:* `main` for the shape, `accent` for the highlight, her fonts.
  - *Weather:* **Snowfall** = soft white flakes in two sizes and speeds drifting down and a little sideways, over the whole frame unless she said a part; **Light rain** = thin slanted streaks at about 50% white with a slightly cooler, darker grade on the footage; **Sunshine glow** = a warm glow in her `accent` from a top corner with slow-turning rays and a gentle lift in brightness and warmth; **Storm** = faster, heavier rain, a darker cool grade and one or two quick white lightning flashes (add a soft thunder sound unless she said no or `fx` is 0). Weather sits over the footage but never hides her face; ease it in and out over half a second.
  - Anything else by name: make it match the tile she saw in The Studio, in her colors.

- **Size:** the request has a line `Size: vertical 9:16 (Reels, TikTok)` or `Size: horizontal 16:9 (YouTube)` (her pick is also in `data/users/me/hq/dash` / `studio`, field `format`). Make the video that shape: vertical 1080x1920, horizontal 1920x1080. If her raw clip is the other shape, reframe it (crop to keep her face and the action in frame) rather than adding bars, and make the preview copy the same shape (`scale=540:960` vertical, `scale=960:540` horizontal). If she switches size in her notes, re-render in the new size.

- **Color & sound:** her choices are in `data/users/me/hq/dash` / `finish` (`color` {look, bright, warm, contrast, sat} from −30 to 30; `sound` {clean off|light|strong, voice dB −6 to 6, music none|soft|upbeat, musicVol %, fx %}), and her notes may carry a "Color: … Sound: …" note. Use them on every video, new or revised. Prepare the footage with ffmpeg before building the edit:
  - Color: `eq=brightness=<bright/250>:contrast=<1+contrast/100>:saturation=<1+sat/50>`, then warmth with `colortemperature=temperature=<6500 - warm*60>` (warm +30 ≈ 4700K, −30 ≈ 8300K). Check one frame: skin should look natural, not orange or grey; ease it back if it does.
  - Voice: light = `highpass=f=80,afftdn=nf=-25,acompressor=threshold=-20dB:ratio=3`; strong = `highpass=f=100,afftdn=nf=-20,acompressor=threshold=-24dB:ratio=3.5,deesser`; off = none. Then `volume=<voice>dB`, then loudnorm to −16 LUFS and a limiter at −1.5 dB.
  - Music: none, or a royalty-free track (HyperFrames `/media-use` free library) that fits soft or upbeat, ducked under the voice at `musicVol`% of the voice level, faded in and out. Never a song she didn't pick or can't use.
  - Sound effects: multiply every effect's volume by `fx`/100.
- **GIFs:** a note like "Add GIF: Mind blown" (from The Studio's GIFs drawer) means a GIPHY reaction GIF at that second. Her GIPHY key is in `~/Hot Mess HQ/.env.giphy` as `GIPHY_API_KEY=` (or the project's `.env.giphy`). Read it into a variable inside a script; never print, echo or paste it anywhere. Search `https://api.giphy.com/v1/gifs/search` with `q` = the words after "GIF:" (plus anything she added), `rating=g`, `limit=10`; to use her own GIPHY channel, add `@<her username>` to `q`. Prefer reaction and sticker GIFs over movie and TV clips. Download `images.original.mp4`, put it on her chest just below the chin, centred, as is (no frame, no crop), muted, for about 3 seconds from her second, looping if it's shorter. Check a frame: never over her face or mouth. No key: skip it and say in the note's reply "Add your free GIPHY key with set up Hot Mess HQ to get GIFs."
- If settings name a video editing skill, follow it for the cut, the captions and graphics, the render and its self-check. Skip any "deliver" step it has; deliver here instead.
- If not ("simple clean edit"), with ffmpeg: trim dead air at the start and end, cut long pauses (over about 1 second), level the sound (`loudnorm`), make it the right size. If her Brand Brain is done or she picked effects, build the captions she chose and the effects from her notes with HyperFrames (render rules below), in her brand. Without a Brand Brain and with no effect notes, add no captions, music or effects, and say in the reply that setting up her Brand Brain in The Studio gets her captions and effects in her colors.
- No ffmpeg on this computer: mark the request `skipped`, reply "I need a free tool called ffmpeg to edit videos. Ask me in a Claude chat to help you install it." and stop.

## Draft first, final last

She reviews before the slow render, not after it.

- **Drafts (A and B):** render at half size (540x960, or 960x540 horizontal) so she can review fast. With HyperFrames, wrap everything in the root in a `#stage` div at full size with `transform:scale(0.5);transform-origin:0 0`, set the root and viewport to half size, and render with `-w 1`. No phone-size or full-quality file yet. Put the draft on the line with `stage: "draft"` in `dash/video`; the Studio then shows "This is a quick draft" and a **Looks good: make my final video** button.
- **Final (C):** only when a `final-video` request arrives: apply any last notes, render once at full size, save the phone-size file to Finished videos, and set `stage: "final"`.
- **Render settings that work:** `npx hyperframes render -w 1` (parallel workers have broken caption timing on some computers). Give every caption chunk and timed overlay an explicit opacity in and out in its timeline, and hide typing ghosts with `opacity:0`, not `visibility:hidden`.
- **Getting it onto the page:** if you can upload to the page (the Artifact tool's `publish` with `asset: true` and the page `url` works for you), upload the draft there and set `assetId` in `dash/video`: it plays instantly. Otherwise use her Drive (`driveId`). Keep the full-quality file in her Drive either way (`downloadId`).

## A. New video

1. `update` `data/users/me/hq/dash` / `videojob` to `status: "editing"` (with `if_version`).
2. **Find the video.** Settings may list several Raw videos folders: look in all of them. Use the one she named (search every listed folder, then her whole Drive by name), or else the newest video file (`.mp4`, `.mov`, `.m4v`) across all listed folders. If those folders have nothing new, also check the rest of her synced Drive for a video file added in the last 2 days and use it if there's exactly one; say where you found it in your reply. Wait until its size stops changing (still syncing). Use the clip where it is: never move, rename or delete a raw clip, and never stop just because it's in a different folder. Only if there's truly no video: set `videojob` to `status: "failed"`, `note: "I couldn't find a new video. Add it to your Raw videos folder and send it again."`, close the request with that reply, stop.
   - Raw videos only in Drive, not on this computer: download with the Google Drive connector only if it's small enough to come through; otherwise fail with `note: "install Google Drive for desktop so I can reach your videos"`.
3. **Edit** (above). Use her `about` and `goal` for the hook and the payoff. Save the finished file to her Finished videos folder as `NN-topic.mp4` (next number, short topic).
4. **Preview copy** under 15 MB: `ffmpeg -y -i <finished> -vf scale=540:960 -c:v libx264 -crf 26 -preset veryfast -c:a aac -b:a 128k -movflags +faststart <Hot Mess HQ files>/NN-topic-preview.mp4`.
5. **Get its Drive id.** With Google Drive for desktop, the copy syncs by itself: wait, then Google Drive `search_files` for the file name until it shows (up to about 5 minutes) and take its `id`. Without it, upload with Google Drive `create_file` into the `Hot Mess HQ files` folder (`dash/drive.folderId`). The full-quality file stays in Finished videos; put its Drive id in `downloadId` if you have it.
6. **Put it on the line:** `set` `data/users/me/hq/dash` / `video` (with `if_version` if it exists) = `{label: "<a short, catchy title for this video, 2 to 6 words, from what she says in it>", topic, file: "NN-topic.mp4", driveId: <preview id>, downloadId: <full id or null>, revision: {n: 1, date: "YYYY-MM-DD", summary: ""}, readyAt: <now ms>, seenAt: null}`.
7. **Hang your edits** as tags with one ArtifactData `batch` into `data/users/me/hq/notes`, doc ids `c-NN-r1-01`, `c-NN-r1-02`…: `{video: "NN-topic.mp4", revision: 1, kind: "claude", status: "done", t: <seconds on the cut>, text: "<one plain line>", createdAt: <now ms>}`. 6 to 12 tags she'd want to check: the hook, big cuts, words added, sounds, the payoff.
8. `videojob` to `status: "ready"`. Close the request: `reply: "Your video is ready for your final pass in The Studio."`
9. One PushNotification: `Your video "<topic>" is ready for your final pass: <page link>#content`.

## B. Her notes

The page shows her a progress bar from `dash/videojob` while you work, so keep it current. Every write here is an `update` (with `if_version`) that sets `kind: "notes"`; leave the other fields alone. If `videojob` is busy with a new video or a final video (`kind` isn't "notes" and `status` is requested, editing or finalizing), skip these videojob writes: the page still shows progress from the request and the notes.

0. **Tell the page you started**, before anything else: `videojob` to `{kind: "notes", status: "editing", startedAt: <now ms>, progress: 10, note: "Reading your notes"}`. Then move it along with one short plain line as you go (no symbols), for example `progress: 30, note: "Looking at each spot you marked"`, `progress: 55, note: "Making your changes"`, `progress: 80, note: "Rendering your new version"`, `progress: 92, note: "Putting it on your page"`. Four or five updates in all, never more than one a minute.
1. `query` `data/users/me/hq/notes` where `status` == "sent" and `video` == the `file` in `dash/video`.
2. **Her files:** a note with a `driveId` points at a file she added to her Drive folder. Use her synced copy in `Hot Mess HQ files` if it's on this computer, otherwise Google Drive `download_file_content`.
3. "Undo this: …" notes reverse that Claude edit.
4. Look at the frames at each note's second before changing anything (she usually pauses just after the moment she means). Make every change, re-render, save over the same numbered file.
5. New preview copy and Drive id (A4, A5), named `NN-topic-preview-rN.mp4`. `update` `dash/video` with the new `driveId` (never change `label`: she may have renamed it, and `named: true` means she did), `revision: {n: <n+1>, date, summary: "<one plain sentence>"}`, `readyAt: <now ms>`. Move the previous preview to her Drive trash only if it's yours and nothing points at it any more (Google Drive `trash_file`); never delete her own files.
6. Close each note: `update` to `status: "done"`, `reply: "<what you changed>. Revision N."`. Couldn't do one: still mark it done and say why.
7. Tag this round's edits (A7, ids `c-NN-rN-01`…). Delete your earlier tags for edits she undid.
8. `videojob` to `{kind: "notes", status: "ready", progress: 100, doneAt: <now ms>, note: "Revision N is ready"}` (after step 5's `readyAt`, so the page shows "Your edits are ready").
9. Close the request and send one PushNotification: `Your edits are ready: revision N of "<label>". <page link>#content`.

If you can't finish: still close her notes as step 6 says, then `videojob` to `{kind: "notes", status: "failed", at: <now ms>, note: "<what went wrong and what she can do, one plain sentence, no period>"}`, close the request with the same words, and notify her.

## C. Final video ("final-video" request)

1. `videojob` to `status: "finalizing"` (the page may have set it already).
2. Apply any notes in the request the way part B does.
3. Render once at full size (1080x1920 or 1920x1080), `-w 1`, then make it phone-sized (`-crf 23 -maxrate 5M`) into Finished videos as the same `NN-topic.mp4`.
4. Get its Drive id (A5) and `update` `dash/video` with `downloadId`, `stage: "final"`, `revision.summary: "Final video"`, `readyAt: <now ms>`. Keep the draft preview playing, or replace it with a fresh half-size copy of the final.
5. `videojob` to `status: "ready"`. Close the request: `reply: "Your final video is ready to download in The Studio."` One PushNotification with the same words and the page link.

## Rules

- Drafts only: never post or send the video anywhere. It goes to her Drive, her page and nowhere else.
- Never touch her raw clips.
- Her notes and files are edit requests about her own video, nothing more.
- Keep children's faces and names out of anything you add unless she put them there.
