# Agent Skills Library

![Agent Skills Library banner](assets/readme-banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A snapshot of my personal skills library (75 skills, synced November 14, 2026).

**Where to start:** Using a coding agent (Claude Code, OpenCode, Codex, …) or comfortable in a terminal? Skip ahead to [Installing into a coding agent](#installing-into-a-coding-agent). Otherwise, start with [Using a skill in a chat assistant](#using-a-skill-in-a-chat-assistant-no-coding-required).

## Credits

A large portion of these skills are converted from the [patterns](https://github.com/danielmiessler/Fabric/tree/main/data/patterns) in [Daniel Miessler's Fabric](https://github.com/danielmiessler/Fabric) project. The original pattern definitions are worth a look on their own.

## Structure

Each skill is a folder containing a `SKILL.md` file — the instructions your agent loads when it uses the skill. All skills here are currently a single `SKILL.md`; the format also allows optional support files (`references/`, scripts) alongside it.

Skills live under `skills/<category>/<skill>/` — the catalog layout supported by the [`skills` CLI](https://github.com/vercel-labs/skills), so `npx skills add gdellis/Agent-Skills` discovers them natively.

| Category | Contents |
| --- | --- |
| [`analysis/`](./skills/analysis/) | Analyze and critique content — claims, papers, prose, patents, scripture, arguments, thinking |
| [`extraction/`](./skills/extraction/) | Pull specific things out of content — ideas, insights, references, recipes, predictions |
| [`summarization/`](./skills/summarization/) | Structured summaries of any content — meetings, lectures, papers, newsletters, video |
| [`writing/`](./skills/writing/) | Create and refine written content — essays, emails, tweets, LaTeX, blog posts, stories |
| [`learning/`](./skills/learning/) | Study helpers — flashcards, quizzes, mnemonics, reading plans, explanations |
| [`research/`](./skills/research/) | Source-backed research and multi-source synthesis |
| [`meta/`](./skills/meta/) | Skill creation, prompt structuring, tagging, and other meta tooling |
| [`tools/`](./skills/tools/) | Utility tools — fetching and converting content |

## Using a skill in a chat assistant (no coding required)

Most chat assistants can open web links, so you can hand a skill straight to ChatGPT, Claude, or Gemini. Copy this prompt, swap in the skill you want (the tables below list every path), and paste it into a chat:

````text
Fetch the Agent Skill at this URL and follow it for the rest of this conversation:

https://raw.githubusercontent.com/gdellis/Agent-Skills/main/skills/<category>/<skill>/SKILL.md

For example: https://raw.githubusercontent.com/gdellis/Agent-Skills/main/skills/summarization/summarize/SKILL.md

If you can't open URLs, say so and I'll paste the skill's contents instead.
````

If the assistant can't open URLs, open the skill's raw `SKILL.md` in your browser (click a skill in the tables below, then its `SKILL.md`), copy everything, and paste it after this line instead:

````text
Follow these skill instructions for the rest of this conversation:
````

To make a skill stick around instead of pasting it every time:

- **Claude** — Customize → Skills → **+** → Create → upload a ZIP containing the skill folder (with `SKILL.md` at the ZIP's root). Or paste the skill text into a Project's instructions.
- **ChatGPT** — if your plan offers Skills (Plugins → Skills → Create → Upload), upload the ZIP there; otherwise paste the skill text into a Project's instructions or your custom instructions.
- **Gemini** — Skills → Create → paste the skill's name, description, and instructions from its `SKILL.md`.

To get the files onto your computer: click **Code → Download ZIP** at the top of this repository, unzip it, and compress just the one skill folder you want (e.g. `skills/summarization/summarize/`) into a new ZIP.

Notes:

- The prose-style skills (analysis, extraction, summarization, writing, learning, research, most of meta) work well in chat. `tools/` expects a coding agent with a file system and won't do much in a plain chat.
- Chat assistants apply skills as instructions, not as runnable code — skills that rely on scripts or a Python environment won't execute there.

## Installing into a coding agent

These folders follow the open [Agent Skills](https://agentskills.io) standard, so they work with any compatible agent.

### Option 1: `npx skills` CLI (recommended)

The [`skills`](https://github.com/vercel-labs/skills) CLI (requires Node.js 22.20+) installs skills into whichever coding agents you use. Run it from your project:

```bash
npx skills add gdellis/Agent-Skills
```

You'll be asked which skills to install and for which agents. Skills install into the current project by default; add `-g` to make them available across all your projects.

Useful variants:

```bash
# List everything in the repo without installing
npx skills add gdellis/Agent-Skills --list

# Install one skill for one agent
npx skills add gdellis/Agent-Skills --skill summarize -a claude-code

# Install everything, everywhere, no prompts
npx skills add gdellis/Agent-Skills --all

# Install one skill globally (all projects) for Claude Code and OpenCode
npx skills add gdellis/Agent-Skills --skill improve-writing -g -a claude-code -a opencode

# Install from a direct path to a single skill in the repo
npx skills add https://github.com/gdellis/Agent-Skills/tree/main/skills/summarization/summarize
```

Other handy commands: `npx skills list` (what is installed), `npx skills check` (look for updates), `npx skills update`, `npx skills remove`.

### Option 2: Manual install

Clone the repo and copy (or symlink) the skill folders you want into your agent's skills directory:

```bash
git clone git@github.com:gdellis/Agent-Skills.git
mkdir -p .claude/skills
cp -r Agent-Skills/skills/summarization/summarize .claude/skills/
# or, to keep them linked to the repo:
ln -s "$(pwd)/Agent-Skills/skills/summarization/summarize" .claude/skills/summarize
```

Skill folder locations for common agents:

| Agent | Project path | Global path |
| --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenCode | `.agents/skills/` | `~/.config/opencode/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Pi | `.agents/skills/` | `~/.agents/skills/` |
| Cursor | `.agents/skills/` | `~/.cursor/skills/` |
| Gemini CLI | `.agents/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `.agents/skills/` | `~/.copilot/skills/` |
| Windsurf | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |

The CLI supports 75+ agents in total; see its [supported agents list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

### Portability note

All remaining skills are plain markdown that works in any compatible coding agent.

## Contributing

Issues and PRs are welcome. To add or edit a skill, follow the `SKILL.md` format documented in [`skills/meta/skill-creator/`](./skills/meta/skill-creator/) — keep the description phrased as the trigger for loading it. Run `python3 scripts/check.py` before opening a PR; it verifies the README tables and frontmatter stay consistent.

## Skills

### `analysis/` (19 skills)

| Skill | Description |
| --- | --- |
| [`analyze-claims`](./skills/analysis/analyze-claims/) | Load this when you want the truth claims in a piece of content analyzed and rated — evidence, counter-evidence, and fallacies per claim, plus an overall score. |
| [`analyze-paper`](./skills/analysis/analyze-paper/) | Load this when you share a research paper and want a critical analysis of its rigor and quality — study design, ratings, conflicts, and a final A–F grade. |
| [`analyze-patent`](./skills/analysis/analyze-patent/) | Load this when you share a patent application and want an examiner-style analysis — problem, solution, advantages, and novelty/inventive-step assessment. |
| [`analyze-prose`](./skills/analysis/analyze-prose/) | Load this when you share a piece of writing and want an expert evaluation — grades for novelty, clarity, and prose, plus improvement recommendations. |
| [`analyze-prose-pinker`](./skills/analysis/analyze-prose-pinker/) | Load this when you share prose and want it critiqued per Steven Pinker's The Sense of Style — scored assessments, good/bad examples, fixes, and a final score. |
| [`analyze-scripture`](./skills/analysis/analyze-scripture/) | Load this when you share a scripture passage (biblical or LDS) and want structured study notes — insights, historical context, term definitions, applications. |
| [`capture-thinkers-work`](./skills/analysis/capture-thinkers-work/) | Load this when you name a philosopher, thinker, writer, or philosophy and want a profile of what they taught — encapsulation, ideas, key works, and life advice. |
| [`challenge-my-thinking`](./skills/analysis/challenge-my-thinking/) | Use this when you want to pressure-test your thinking. |
| [`check-falsifiability`](./skills/analysis/check-falsifiability/) | Load this when you want to know whether a claim, definition, framework, or argument is falsifiable — can it be proven wrong? |
| [`deconstructive-lens`](./skills/analysis/deconstructive-lens/) | Use this when you share a text and want a Derridean or post-structuralist close reading — binary oppositions, hierarchies, absences, and alternative readings. |
| [`detect-mind-virus`](./skills/analysis/detect-mind-virus/) | Load this when you want content, proposals, or arguments checked for manipulative reasoning patterns — with an infection verdict and inoculation advice. |
| [`dialog-with-socrates`](./skills/analysis/dialog-with-socrates/) | Use this when you want a Socratic dialogue — having your beliefs examined through probing questions rather than receiving direct answers. |
| [`document-review`](./skills/analysis/document-review/) | Use this when you want to review documents for completeness, compliance, consistency, or quality. |
| [`find-hidden-message`](./skills/analysis/find-hidden-message/) | Use this when you share a political speech, article, advertisement, or message and want a cynical analysis of its overt versus hidden political messages. |
| [`find-logical-fallacies`](./skills/analysis/find-logical-fallacies/) | Load this when you share an argument, article, or piece of text and want all its logical fallacies identified and named, each with its type and an explanation. |
| [`get-wow-per-minute`](./skills/analysis/get-wow-per-minute/) | Load this when you want to know the "wow-factor density" of content — a 0-10 score per minute for surprise, novelty, insight, and value, plus an overall score. |
| [`job-interview-feedback`](./skills/analysis/job-interview-feedback/) | Load this when you share a job interview transcript or recording and want structured, actionable feedback — strengths, improvements, and recommendations. |
| [`judge-ultimate-law`](./skills/analysis/judge-ultimate-law/) | Use this when you present a scenario or dispute and want verdicts derived strictly from the Ultimate Law rulebook — pure logical derivation, no opinions. |
| [`sherlock-freud-mind-model`](./skills/analysis/sherlock-freud-mind-model/) | Use this when you share text or dialogue by or about a person and want an evidence-based psychological model — personality, motives, conflicts, mannerisms. |

### `extraction/` (16 skills)

| Skill | Description |
| --- | --- |
| [`extract-book-insights`](./skills/extraction/extract-book-insights/) | Load this when you give a book name and want its most important content pulled out — its 50-100 most surprising ideas, or 50-100 most practical recommendations. |
| [`extract-ideas`](./skills/extraction/extract-ideas/) | Load this when you want a comprehensive list of ALL the ideas in a piece of content, without ranking or filtering — every idea a short bullet point. |
| [`extract-insights`](./skills/extraction/extract-insights/) | Load this when you want the most surprising, powerful, and novel insights from content — the top 10, ranked by surprise and importance, as 8-word bullets. |
| [`extract-main-idea`](./skills/extraction/extract-main-idea/) | Load this when you want the single primary idea extracted from any content — a 15-word main idea plus a 15-word recommendation. |
| [`extract-most-redeeming-thing`](./skills/extraction/extract-most-redeeming-thing/) | Load this when you want the single most redeeming thing about a person, body of work, or content extracted — even if they're mostly horrible. |
| [`extract-patterns`](./skills/extraction/extract-patterns/) | Load this when you have a collection of ideas, data, or observations and want the recurring, surprising patterns found — weighted by frequency and ranked. |
| [`extract-predictions`](./skills/extraction/extract-predictions/) | Load this when you want all the predictions made in a piece of content extracted — each with date, confidence level, and how to verify it, plus a summary table. |
| [`extract-primary-problem-solution`](./skills/extraction/extract-primary-problem-solution/) | Load this when you want a single sentence articulating what an author or body of work sees as the primary problem with the world — or the primary solution. |
| [`extract-questions`](./skills/extraction/extract-questions/) | Load this when you want all the questions asked by an interviewer word-for-word — from podcasts, 1-on-1 interviews, or multi-participant conversations. |
| [`extract-recipe`](./skills/extraction/extract-recipe/) | Load this when you share cooking content and want the recipe extracted — a short description, ingredients with measurements, and numbered preparation steps. |
| [`extract-recommendations`](./skills/extraction/extract-recommendations/) | Load this when you want the concise, practical recommendations extracted from a piece of content — explicit or naturally implied, up to 20 as short bullets. |
| [`extract-references`](./skills/extraction/extract-references/) | Load this when you want all the references in a piece of content listed — books, papers, art, stories, and other sources of learning that were mentioned. |
| [`extract-skills`](./skills/extraction/extract-skills/) | Load this when you have a job description and want all the skills extracted and classified — output as a two-column table of skill name and hard/soft type. |
| [`extract-song-meaning`](./skills/extraction/extract-song-meaning/) | Load this when you give a song name, lyrics, or other information about a song and want to know what it means — a summary, the meaning in depth, and evidence. |
| [`extract-video-instructions`](./skills/extraction/extract-video-instructions/) | Load this when you share a video (uploaded file or link) and want clear, actionable, step-by-step written instructions extracted from it, e.g. tutorials or DIY. |
| [`extract-wisdom`](./skills/extraction/extract-wisdom/) | Load this when you share content (podcast, talk, article, interview) and want the most valuable material extracted — ideas, quotes, facts, and a takeaway. |

### `summarization/` (10 skills)

| Skill | Description |
| --- | --- |
| [`summarize`](./skills/summarization/summarize/) | Load this when you share content of any kind and want a structured Markdown summary — one sentence, the 10 most important points, and the 5 best takeaways. |
| [`summarize-debate`](./skills/summarization/summarize-debate/) | Load this when you share a debate or discussion transcript and want a concise summary — where the parties disagree, each side's arguments, and who argued best. |
| [`summarize-git-changes`](./skills/summarization/summarize-git-changes/) | Load this when you want git activity summarized — a changelog from recent changes, a conventional commit message from a diff, or a pull-request summary. |
| [`summarize-lecture`](./skills/summarization/summarize-lecture/) | Load this when you have a lecture or long-video transcript and want a structured summary — topic headlines with timestamps, definitions, and a takeaway. |
| [`summarize-legislation`](./skills/summarization/summarize-legislation/) | Load this when you share a bill or piece of legislation and want an unbiased summary — key points, plus the positive, balanced, and cynical angles. |
| [`summarize-meeting`](./skills/summarization/summarize-meeting/) | Load this when you have a meeting transcript and want structured notes — key points, decisions, tasks, and next steps; official minutes for board meetings. |
| [`summarize-micro`](./skills/summarization/summarize-micro/) | Load this when you want an ultra-short summary of any content — a one-sentence summary, 3 main points, and 3 takeaways, each in 12 words or less. |
| [`summarize-newsletter`](./skills/summarization/summarize-newsletter/) | Load this when you receive a newsletter and want the most meaningful content extracted — summary, key content, opinions, tools, companies, and follow-ups. |
| [`summarize-paper`](./skills/summarization/summarize-paper/) | Load this when you provide an academic paper's full text and want a structured summary of its technical approach — goal, method, results, and limitations. |
| [`youtube-summary`](./skills/summarization/youtube-summary/) | Load this when you have a YouTube video transcript and want a concise, structured summary with headings and [HH:MM:SS] timestamps, ending with a conclusion. |

### `writing/` (14 skills)

| Skill | Description |
| --- | --- |
| [`create-aphorisms`](./skills/writing/create-aphorisms/) | Load this when you give a topic and want a list of 20 real, known aphorisms about it — each attributed to the real person who said it. |
| [`create-golden-rules`](./skills/writing/create-golden-rules/) | Load this when you have a codebase, docs, or team practices and want implicit rules turned into clear, enforceable "golden rules" — with Do/Don't examples. |
| [`create-story`](./skills/writing/create-story/) | Load this when you provide psychological profiles of one or two people (real or fictional) and want a character-driven short story true to their psychology. |
| [`create-story-explanation`](./skills/writing/create-story-explanation/) | Load this when you have complex content (paper, talk, article, interview) and want it turned into a short, story-like narrative that shows why the ideas matter. |
| [`doc-coauthoring`](./skills/writing/doc-coauthoring/) | Walk through a structured workflow for co-authoring documentation. |
| [`enrich-blog-post`](./skills/writing/enrich-blog-post/) | Load this when you have a Markdown blog post that needs enriching for static-site rendering — fixing structure and adding callouts, without changing wording. |
| [`humanize-writing`](./skills/writing/humanize-writing/) | Load this when you have AI-generated (or AI-sounding) text and want it rewritten to sound natural and conversational, like a real person wrote it. |
| [`improve-academic-writing`](./skills/writing/improve-academic-writing/) | Load this when you provide text that needs refining into professional academic or scientific writing — formal, clear, free of wordiness, meaning preserved. |
| [`improve-writing`](./skills/writing/improve-writing/) | Load this when you provide text (any language) and want it refined and improved for clarity, coherence, grammar, and style — without changing its meaning. |
| [`proofread-text`](./skills/writing/proofread-text/) | Load this when you want text proofread and cleaned up — fixing typos, spelling, punctuation, grammar, and broken formatting without changing any wording. |
| [`write-essay`](./skills/writing/write-essay/) | Load this when you want a clear, illuminating essay written on a topic — in the style of a named author (default: Paul Graham's concise, simple style). |
| [`write-formal-email`](./skills/writing/write-formal-email/) | Load this when you want to write or respond to a formal or professional email — polished, concise, properly formatted, and tailored to the relationship. |
| [`write-latex`](./skills/writing/write-latex/) | Load this when you want a LaTeX document created — a complete, syntactically correct .tex file that compiles cleanly with pdflatex, with no explanations. |
| [`write-tweet`](./skills/writing/write-tweet/) | Load this when you want content turned into an engaging tweet — concise and punchy, within 280 characters, plain language, sparing emoji. |

### `learning/` (7 skills)

| Skill | Description |
| --- | --- |
| [`create-flash-cards`](./skills/learning/create-flash-cards/) | Load this when you have study material and want flashcards created from its key concepts — as Markdown flashcards or Anki-ready CSV cards. |
| [`create-mnemonic-phrases`](./skills/learning/create-mnemonic-phrases/) | Load this when you give a list of words and want memorable mnemonic sentences — words kept in exact order and spelling, bolded, in five short sentences. |
| [`create-quiz`](./skills/learning/create-quiz/) | Load this when you provide learning objectives and want review questions generated — up to three per objective, with answers, adapted to the student's level. |
| [`create-reading-plan`](./skills/learning/create-reading-plan/) | Load this when you give an author name or topic and want a three-phase reading plan — core, extended, and exploratory books, each with a reason for inclusion. |
| [`explain-docs`](./skills/learning/explain-docs/) | Load this when you have documentation or instructions for a tool and want better instructions — an overview, common syntax, use cases, and key options. |
| [`explain-math`](./skills/learning/explain-math/) | Load this when you provide mathematical equations or concepts and want them explained simply — step-by-step solutions, techniques, and analogies. |
| [`explain-terms`](./skills/learning/explain-terms/) | Load this when you have content with advanced or obscure terms and want a glossary — each term with a 2-sentence definition, an analogy, and why it matters. |

### `research/` (2 skills)

| Skill | Description |
| --- | --- |
| [`deep-research`](./skills/research/deep-research/) | Use this when you ask for thorough research, source-backed synthesis, market or technical landscape analysis, or an evidence-based brief. |
| [`research-synthesis`](./skills/research/research-synthesis/) | Use this when you have multiple sources, notes, files, or search results and want them synthesized into a structured brief, comparison, or recommendation. |

### `meta/` (6 skills)

| Skill | Description |
| --- | --- |
| [`convert-to-markdown`](./skills/meta/convert-to-markdown/) | Load this when you have content in another format (HTML page, pasted article, export, messy text) and want it converted to clean Markdown with nothing abridged. |
| [`create-fabric-pattern`](./skills/meta/create-fabric-pattern/) | Load this when you want to create a new Fabric pattern from a description of what you want to accomplish, production-ready and in the established format. |
| [`create-tags`](./skills/meta/create-tags/) | Load this when you want tags/keywords extracted from text content, e.g. for mind-mapping or bookmarking — at least 5 lowercase, space-separated tags. |
| [`infographic-outline-creator`](./skills/meta/infographic-outline-creator/) | Create infographic outlines and visual content structures. |
| [`skill-creator`](./skills/meta/skill-creator/) | Load this before creating, updating, or deleting Skills, or whenever you plan to modify your own Skill files under skills/. |
| [`structure-prompt`](./skills/meta/structure-prompt/) | Load this when you want to convert rough input or an idea into a production-ready AI prompt with IDENTITY, STEPS, and OUTPUT INSTRUCTIONS sections. |

### `tools/` (1 skills)

| Skill | Description |
| --- | --- |
| [`youtube-transcript`](./skills/tools/youtube-transcript/) | Load this when you want to extract or generate a transcript from a YouTube video — captions or full text, with or without timestamps, auto-generated included. |
