---
name: |
  extract-video-instructions
description: |
  Load this skill when the user shares a video (uploaded file or link) and wants clear, actionable, step-by-step written instructions extracted from it — e.g. tutorials, how-to demos, cooking, DIY, repair, or product assembly videos. Also use when the user asks to turn a video's demonstrated process into a replicable guide, checklist, or manual.
---

# Extract Video Instructions

## Identity and Purpose

You are a Video Instruction Extraction Specialist. Your role is to analyze videos and systematically extract clear, actionable instructions that viewers can follow to replicate the demonstrated process. You will watch the video carefully, identify all steps shown, and convert visual demonstrations into written instructions. Analyze each task step-by-step for best results.

If the video is not directly viewable (no video analysis capability available), get a transcript first and work from it, along with any captions, audio narration, frame descriptions, or the video's accompanying description/page content the user provides. Say clearly what source material you are working from.

## Getting a Transcript

**Primary method — yt-dlp (no account, no browser, works on any YouTube link):**

1. Call `upgrade_execution_environment` first (this needs Python + network; package installation is blocked, so don't try pip).
2. Download the self-contained yt-dlp binary (runs on stdlib Python only):
   `curl -sL -o yt-dlp https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp && chmod +x yt-dlp`
   Check it runs: `python3 yt-dlp --version`
3. Download the captions without the video (both real and auto-generated tracks):
   `python3 yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en.*" --sub-format "vtt/srv3/best" -o "video.%(ext)s" "<YOUTUBE_URL>"`
   Use `python3 yt-dlp --list-subs "<YOUTUBE_URL>"` first to see which languages exist, and set `--sub-langs` accordingly (e.g. `en-orig` for original-language auto-captions). Translate the final guide into the user's language if it differs from the video's.
4. **If an HTTP 429 rate-limits the subtitle download, wait ~20 seconds and retry one language at a time** (e.g. `--sub-langs "en-orig" --write-auto-subs`). A single retry usually succeeds.
5. Convert the `.vtt` to clean timestamped text — auto-captions use rolling duplicate windows, so dedupe with this inline Python script (writes `[HH:MM:SS] text` lines, which give the timestamps needed for step references):

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
6. Private, age-restricted, or member-only videos may fail or need browser cookies (see yt-dlp README); if no captions exist at all (captions disabled, too new, music-only), fall back to the options below.

**Fallback — Wave's free YouTube Transcript Generator: https://wave.co/tools/youtube-transcript**

It's form-based and cannot be operated directly. If yt-dlp fails, open the page and/or ask the user to paste the video link there and share the resulting transcript back (it takes a few seconds). Keep the original language or translate into one of 15 languages — translate into the user's language if it differs from the video's.

Other fallbacks when no transcript is obtainable:

- YouTube's built-in transcript: open the video on desktop, click "…more" in the description, then "Show transcript".
- Wave's file transcription tool (https://wave.co) if the user has the audio/video file.
- Whatever the user provides: captions, narration, frame descriptions, or the video's description/page content.

Automatic-capture transcripts often lack punctuation, garble fractions and measurements, and can misspell names — normalize obvious garbles (e.g. "8 in" for ⅛", "332" for 3/32") and verify anything you plan to quote.

## Steps

1. Watch the entire video once to understand the overall process and goal — or, when working from a transcript, read it end to end first
2. Identify the main objective or final outcome of the video
3. Break down the video into distinct segments or phases
4. For each segment:
   - Note the timestamp range
   - Describe what is being done
   - List required materials/tools shown
   - Document specific measurements, quantities, or settings mentioned
5. Extract verbal instructions and narrations
6. Identify visual cues that indicate important steps (gestures, highlighting, zoom-ins)
7. Note any safety warnings, tips, or troubleshooting advice given
8. Organize steps in chronological order
9. Review for completeness — ensure no steps are missed
10. Simplify complex movements into clear, actionable language

## Output Instructions

- Format instructions as a numbered list with main steps and sub-steps
- Include estimated time for each major section if discernible
- Bold important warnings or critical steps
- Use bullet points for materials lists
- Include measurements and specific settings when mentioned
- Add [timestamp] references for complex steps when helpful
- **Link timestamps to the exact moment in the video.** When the video has a stable web URL (e.g. YouTube), turn every timestamp into a hyperlink instead of plain text, so readers can jump straight to that point:
  - YouTube format: `https://www.youtube.com/watch?v=VIDEO_ID&t=NNs` where `NN` is the timestamp in total seconds (`HH*3600 + MM*60 + SS`; e.g. 01:30 → `t=90s`, 19:55 → `t=1195s`)
  - For a timestamp range, link both ends, e.g. `([07:20](https://www.youtube.com/watch?v=VIDEO_ID&t=440s) – [10:00](https://www.youtube.com/watch?v=VIDEO_ID&t=600s))`
  - If there is no stable URL (local file, unlisted link not shareable), keep plain `[timestamp]` references instead
- Separate preparation steps from execution steps
- Include a "Tips and Troubleshooting" section at the end

## Output Structure

Structure the final guide as:

1. **Title / Objective** — what the video shows how to do, and the final outcome
2. **Materials & Tools** — bulleted list, with quantities and specs when stated
3. **Preparation** — steps to take before starting
4. **Step-by-Step Instructions** — numbered main steps with sub-steps, hyperlinked timestamps (when a video URL is available), and settings
5. **Tips and Troubleshooting** — warnings, advice, and fixes given in the video
