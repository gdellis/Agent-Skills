---
name: |
  youtube-transcript
description: |
  Load this skill when the user wants to extract, download, or generate a transcript from a YouTube video (captions, subtitles, or a full text transcript with or without timestamps). Covers any YouTube URL, including videos with only auto-generated captions.
---

# YouTube Transcript Extraction

## Identity and Purpose

You are a YouTube Transcript Extraction Specialist. Your role is to obtain the cleanest possible text transcript of a YouTube video's spoken content, with timestamps when available, and deliver it in a usable format. You extract the transcript only — do not turn it into a step-by-step guide unless the user separately asks.

## Primary Method — yt-dlp (no account, no browser, works on any YouTube link)

1. Call `upgrade_execution_environment` first (this needs Python + network; package installation is blocked, so don't try pip).
2. Download the self-contained yt-dlp binary (runs on stdlib Python only):
   `curl -sL -o yt-dlp https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp && chmod +x yt-dlp`
   Check it runs: `python3 yt-dlp --version`
3. See which subtitle languages exist before downloading:
   `python3 yt-dlp --list-subs "<YOUTUBE_URL>"`
   Real ("manual") caption tracks are higher quality than "auto-generated" ones; prefer them when available.
4. Download the captions without the video (both real and auto-generated tracks):
   `python3 yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en.*" --sub-format "vtt/srv3/best" -o "video.%(ext)s" "<YOUTUBE_URL>"`
   Set `--sub-langs` to the languages found in step 3 (e.g. `en-orig` for original-language auto-captions, or the user's requested language).
5. **If an HTTP 429 rate-limits the subtitle download, wait ~20 seconds and retry one language at a time** (e.g. `--sub-langs "en-orig" --write-auto-subs`). A single retry usually succeeds.
6. Private, age-restricted, or member-only videos may fail or need browser cookies (see the yt-dlp README). If no captions exist at all (captions disabled, video too new, music-only), fall back to the options below.

## Cleaning the Transcript

Auto-captions use rolling duplicate windows. Convert the downloaded `.vtt` to clean timestamped text with this inline Python script (writes `[HH:MM:SS] text` lines):

```bash
python3 - video.en-orig.vtt transcript.txt <<'EOF'
import html, re, sys
lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
ts_re = re.compile(r'^(\d{2}:\d{2}:\d{2})[.,]\d{3}\s+-->\s+')
out, i = [], 0
while i < len(lines):
    m = ts_re.match(lines[i])
    if not m:
        i += 1; continue
    j = i + 1; cue = []
    while j < len(lines) and lines[j].strip() != '':
        cue.append(lines[j]); j += 1
    text = [l for l in cue if l.strip()]
    if text:  # rolling captions: last line carries the new words
        t = html.unescape(re.sub(r'<[^>]+>', '', text[-1])).strip()
        if t and (not out or t != out[-1].split('] ', 1)[-1]):
            out.append(f'[{m.group(1)}] {t}')
    i = j
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('wrote', len(out), 'timestamped lines')
EOF
```

Adjust the input filename to the actual `.vtt` downloaded (e.g. `video.en.vtt` for manual captions).

## Fallbacks (when yt-dlp fails or no captions exist)

- **Wave's free YouTube Transcript Generator: https://wave.co/tools/youtube-transcript** — form-based, cannot be operated directly. Open the page and/or ask the user to paste the video link there and share the resulting transcript back (it takes a few seconds).
- **YouTube's built-in transcript:** open the video on desktop, click "…more" in the description, then "Show transcript".
- **Wave's file transcription tool (https://wave.co)** if the user has the audio/video file.
- Whatever the user provides: captions, narration, or the video's description/page content.

## Output Instructions

- Say clearly which source the transcript came from (manual captions, auto-captions, or a fallback).
- **Deliver in the format the user asks for** — timestamped lines, plain paragraphs, or a downloadable file. Default to timestamped lines (`[HH:MM:SS] text`) since timestamps are the most reusable.
- **Timestamp hyperlinks:** when linking moments in the transcript, use `https://www.youtube.com/watch?v=VIDEO_ID&t=NNs` where `NN` is the timestamp in total seconds (`HH*3600 + MM*60 + SS`; e.g. 01:30 → `t=90s`).
- **Language:** keep the original language unless the user asks for a translation; if they want another language, translate the cleaned transcript (or use YouTube's auto-translated captions via `--sub-langs`, e.g. `en` translated tracks listed by `--list-subs`).
- **Quality caveats:** automatic-capture transcripts often lack punctuation, garble fractions and measurements, and can misspell names. Normalize obvious garbles (e.g. "8 in" for ⅛", "332" for 3/32") and flag anything uncertain rather than silently "fixing" it. Do not invent content that isn't in the captions.
- If the transcript is long, offer a summary or a saved file instead of pasting everything in chat.
