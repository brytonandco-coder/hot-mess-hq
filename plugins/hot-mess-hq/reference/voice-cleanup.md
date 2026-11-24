# Voice cleanup (every HQ video job uses this)

Studio-clean voice without Riverside or any paid tool. Step 1 is DeepFilterNet, a free AI noise remover that runs on her own computer (official program from github.com/Rikorose/DeepFilterNet, about 27 MB, nothing sent anywhere). Step 2 is a short ffmpeg polish. Bryton picked this in a side-by-side test (Nov 24, 2026) over plain ffmpeg cleanup and over Resemble Enhance (too slow, and needed patching).

## Where the program is

`~/Hot Mess HQ/tools/deep-filter.exe` on Windows, `~/Hot Mess HQ/tools/deep-filter` on a Mac. hq-setup installs it. Missing? Install it now (steps below), then carry on. If that fails, use the fallback at the bottom and say so in your reply.

## Her setting

The Studio's Voice & music drawer saves `sound.clean` in `data/users/me/hq/dash` / `finish`: `off`, `light` (the default) or `strong`. Notes can also say "cleaner sound".

- `off`: skip step 1 and the cleanup filters; still level the loudness.
- `light`: step 1 with `-a 24` (takes most of the background out but leaves a little room sound, so it still sounds like a real place).
- `strong`: step 1 with no limit (background almost silent).

## Steps

1. Pull the voice out as 48 kHz mono WAV: `ffmpeg -i <raw video> -vn -ac 1 -ar 48000 voice.wav`
2. Clean it: `deep-filter -D [-a 24] -o cleaned voice.wav` (writes `cleaned/voice.wav`). Always pass `-D`: it removes the model's tiny delay so her lips stay in sync. About 5 seconds per 25 seconds of audio on a normal computer.
3. Polish: `ffmpeg -i cleaned/voice.wav -af "highpass=f=80,equalizer=f=200:t=q:w=1:g=-2,equalizer=f=3500:t=q:w=1.2:g=2.5,equalizer=f=10000:t=h:w=1:g=1.5,deesser,acompressor=threshold=-22dB:ratio=3:attack=10:release=150,volume=<voice>dB,apad" -ar 48000 voice-clean.wav` (`<voice>` = her `sound.voice`, 0 if not set; `apad` keeps it as long as the video).
4. Use `voice-clean.wav` as the voice track in the edit (in place of the camera audio), then set the final loudness the way the job says (for example −16 LUFS, limiter at −1.5 dB) after music and effects are mixed in.
5. Listen check: compare a few seconds before and after. If her voice sounds watery, swirly or cut off at the ends of words, redo step 2 with `-a 18`. If it still does, use the fallback.

## Installing the program

Pick the file for her computer from the latest release at `https://api.github.com/repos/Rikorose/DeepFilterNet/releases/latest` (only this official repository):
- Windows: `deep-filter-<version>-x86_64-pc-windows-msvc.exe`, save as `~/Hot Mess HQ/tools/deep-filter.exe`
- Mac with Apple chip (M1 and newer): `deep-filter-<version>-aarch64-apple-darwin`, save as `~/Hot Mess HQ/tools/deep-filter`, then `chmod +x`
- Older Intel Mac: `deep-filter-<version>-x86_64-apple-darwin`, same as above

Check it runs with `deep-filter --version`. On a Mac, if it's blocked as "unidentified developer", run `xattr -d com.apple.quarantine ~/Hot\ Mess\ HQ/tools/deep-filter` and try again.

## Fallback (no DeepFilterNet)

- light: `highpass=f=80,afftdn=nf=-25,acompressor=threshold=-20dB:ratio=3`
- strong: `highpass=f=100,afftdn=nf=-20,acompressor=threshold=-24dB:ratio=3.5,deesser`
