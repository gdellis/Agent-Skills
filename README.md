# Agent Skills Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A snapshot of my personal Vibe skills library (91 skills, synced November 13, 2026).

## Structure

Each skill is a folder containing its `SKILL.md` file (the instructions loaded when the skill is used). Some skills also include `references/` support files, scripts, or quick-start guides.

Skills live under `skills/<category>/<skill>/` — the catalog layout supported by the [`skills` CLI](https://github.com/vercel-labs/skills), so `npx skills add gdellis/Agent-Skills` discovers them natively. Skill folder names (and the `name:` frontmatter) are unchanged; only the location moved.

| Category | Contents |
| --- | --- |
| [`analysis/`](./skills/analysis/) | Analyze and critique content — claims, papers, prose, patents, scripture, arguments, thinking |
| [`extraction/`](./skills/extraction/) | Pull specific things out of content — ideas, insights, references, recipes, predictions |
| [`summarization/`](./skills/summarization/) | Structured summaries of any content — meetings, lectures, papers, newsletters, video |
| [`writing/`](./skills/writing/) | Create and refine written content — essays, emails, tweets, LaTeX, blog posts, stories |
| [`learning/`](./skills/learning/) | Study helpers — flashcards, quizzes, mnemonics, reading plans, explanations |
| [`research/`](./skills/research/) | Source-backed research and multi-source synthesis |
| [`knowledge/`](./skills/knowledge/) | Vibe Personal Knowledge — set up, enrich, query, and clean up a knowledge base |
| [`vibe/`](./skills/vibe/) | Vibe platform skills — Canvas, artifacts, rich UI, Vibe onboarding |
| [`meta/`](./skills/meta/) | Skill creation, prompt structuring, tagging, and other meta tooling |
| [`tools/`](./skills/tools/) | Utility tools — fetching and converting content |

## Installing into a coding agent

These folders follow the open [Agent Skills](https://agentskills.io) standard, so they work with any compatible agent.

### Option 1: `npx skills` CLI (recommended)

The [`skills`](https://github.com/vercel-labs/skills) CLI (requires Node.js 22.20+) installs skills into whichever coding agents you use. Run it from your project:

```bash
npx skills add gdellis/Agent-Skills
```

You will be prompted to pick the skills and the agents to install them for. Skills install into the current project by default; add `-g` to make them available across all your projects.

Because this repository is private, the CLI uses your existing Git credentials. Any of these works:

```bash
gh auth login                 # GitHub CLI (tried after normal git credentials)
# or a configured git credential helper / SSH key
# or export GITHUB_TOKEN=ghp_xxx   # for GitHub API access
```

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

Skills such as `canvas`, `canvas-react`, `rich-ui`, `artifacts`, `userLibrary`, `knowledge-*`, `build-*`, `sanitize-knowledge`, `discover-knowledge`, `mistral-self-knowledge`, and `vibe-work-onboarding` reference Vibe-specific features (Canvas files, connectors, Personal Knowledge) and only make sense inside Vibe. The rest (summarization, writing, analysis, extraction, research skills, and so on) are plain Agent Skills markdown and work in any compatible coding agent.

## Credits

A large portion of these skills are converted from the [patterns](https://github.com/danielmiessler/Fabric/tree/main/data/patterns) in [Daniel Miessler's Fabric](https://github.com/danielmiessler/Fabric) project. The original pattern definitions are worth a look on their own.

## Notes

- Auto-generated runtime bundles (Python environments under `skills/analysis/data-analysis/library/.bundled`) are intentionally excluded; only the portable skill definitions and support files are included.
- To restore into Vibe, copy each `skills/<category>/<skill>/` folder back into Vibe's flat skills directory (drop the category level).

## Skills

### `analysis/` — Analyze claims, papers, prose, patents, scripture, and thinking — critique, fact-check, and evaluate content.

| Skill | Description |
| --- | --- |
| [`analyze-claims`](./skills/analysis/analyze-claims/) | Load this skill when the user wants the truth claims in a piece of content analyzed and rated — for each claim, supporting evidence, counter-evidence, fallacies commit... |
| [`analyze-paper`](./skills/analysis/analyze-paper/) | Load this skill when the user shares a research paper and wants a critical analysis of its scientific rigor and quality — findings, study quality breakdown (design, sa... |
| [`analyze-patent`](./skills/analysis/analyze-patent/) | Load this skill when the user shares a patent application and wants an examiner-style analysis — field, problem, solution, advantages, novelty and inventive-step asses... |
| [`analyze-prose`](./skills/analysis/analyze-prose/) | Load this skill when the user shares a piece of writing and wants an expert evaluation of its quality — letter grades (A–F) for novelty, clarity, and prose, improvemen... |
| [`analyze-prose-pinker`](./skills/analysis/analyze-prose-pinker/) | Load this skill when the user shares prose and wants it critiqued according to Steven Pinker's The Sense of Style — style analysis, positive and critical assessments w... |
| [`analyze-scripture`](./skills/analysis/analyze-scripture/) | Load this skill when the user shares a scripture passage (biblical or LDS-specific) and wants structured study notes — passage identification, key insights and doctrin... |
| [`capture-thinkers-work`](./skills/analysis/capture-thinkers-work/) | Load this skill when the user names a philosopher, notable figure, thinker, writer, author, or philosophy and wants a structured profile of what they/it taught — encap... |
| [`challenge-my-thinking`](./skills/analysis/challenge-my-thinking/) | Use this skill when the user wants to pressure-test their thinking. |
| [`check-falsifiability`](./skills/analysis/check-falsifiability/) | Load this skill when the user wants to know whether a claim, definition, framework, or argument is falsifiable — can it be proven wrong? |
| [`data-analysis`](./skills/analysis/data-analysis/) | Use this skill for substantive computation, data analysis and transformation, mathematical or statistical modeling, simulation, and optimization, with a prepared Pytho... |
| [`deconstructive-lens`](./skills/analysis/deconstructive-lens/) | Use this skill when the user shares a text and wants a Derridean or post-structuralist close reading that reveals the text's architecture — binary oppositions, hierarc... |
| [`detect-mind-virus`](./skills/analysis/detect-mind-virus/) | Load this skill when the user wants content, proposals, ideologies, or arguments checked for manipulative reasoning patterns — ideas that spread via fear, guilt, ident... |
| [`dialog-with-socrates`](./skills/analysis/dialog-with-socrates/) | Use this skill when the user wants a Socratic dialogue — having their beliefs examined through probing questions rather than receiving direct answers. |
| [`document-review`](./skills/analysis/document-review/) | Use this skill when the user wants to review documents for completeness, compliance, consistency, or quality. |
| [`find-hidden-message`](./skills/analysis/find-hidden-message/) | Use this skill when the user shares a political speech, article, advertisement, or message and wants a cynical analysis of its overt versus hidden political messages. |
| [`find-logical-fallacies`](./skills/analysis/find-logical-fallacies/) | Load this skill when the user shares an argument, article, or piece of text and wants all the logical fallacies in it identified and named — each with its type and an... |
| [`get-wow-per-minute`](./skills/analysis/get-wow-per-minute/) | Load this skill when the user wants to know the "wow-factor density" of content — a 0-10 score per minute for surprise, novelty, insight, value, and wisdom, plus an ov... |
| [`job-interview-feedback`](./skills/analysis/job-interview-feedback/) | Load this skill when the user shares a job interview transcript or recording and wants structured, actionable feedback on their performance — strengths, areas for impr... |
| [`judge-ultimate-law`](./skills/analysis/judge-ultimate-law/) | Use this skill when the user presents a scenario or dispute and wants verdicts derived strictly from the Ultimate Law rulebook — a pure, rule-by-rule logical derivatio... |
| [`sherlock-freud-mind-model`](./skills/analysis/sherlock-freud-mind-model/) | Use this skill when the user shares text or dialogue produced by or about a person and wants an evidence-based psychological model of that subject — personality struct... |

### `extraction/` — Pull specific things (ideas, insights, references, recipes, predictions…) out of content.

| Skill | Description |
| --- | --- |
| [`extract-book-insights`](./skills/extraction/extract-book-insights/) | Load this skill when the user gives a book name and wants its most important content pulled out — 50-100 of its most surprising and interesting ideas, or 50-100 of its... |
| [`extract-ideas`](./skills/extraction/extract-ideas/) | Load this skill when the user wants a comprehensive list of ALL the ideas in a piece of content, without ranking or filtering — every idea captured as a short bullet p... |
| [`extract-insights`](./skills/extraction/extract-insights/) | Load this skill when the user wants the most surprising, powerful, and novel insights from content — the top 10, ranked by surprise and importance, written as 8-word b... |
| [`extract-main-idea`](./skills/extraction/extract-main-idea/) | Load this skill when the user wants the single primary idea extracted from any content — a 15-word main idea plus a 15-word recommendation. |
| [`extract-most-redeeming-thing`](./skills/extraction/extract-most-redeeming-thing/) | Load this skill when the user wants the single most redeeming thing about a person, body of work, or content extracted — even if they're mostly horrible. |
| [`extract-patterns`](./skills/extraction/extract-patterns/) | Load this skill when the user has a collection of ideas, data, or observations and wants the recurring, surprising patterns found — where the same idea kept coming up... |
| [`extract-predictions`](./skills/extraction/extract-predictions/) | Load this skill when the user wants all the predictions made in a piece of content extracted — each prediction with its date, confidence level, and how to verify it, p... |
| [`extract-primary-problem-solution`](./skills/extraction/extract-primary-problem-solution/) | Load this skill when the user wants a single sentence articulating what an author or body of work believes is the primary problem with the world — or the primary solut... |
| [`extract-questions`](./skills/extraction/extract-questions/) | Load this skill when the user wants all the questions asked by an interviewer in a conversation extracted word-for-word — from podcasts, 1-on-1 interviews, or multi-pa... |
| [`extract-recipe`](./skills/extraction/extract-recipe/) | Load this skill when the user shares cooking content and wants the recipe extracted — a short description (difficulty, spiciness, time), ingredients with measurements,... |
| [`extract-recommendations`](./skills/extraction/extract-recommendations/) | Load this skill when the user wants the concise, practical recommendations extracted from a piece of content — those explicitly made or that naturally flow from it, up... |
| [`extract-references`](./skills/extraction/extract-references/) | Load this skill when the user wants all the references in a piece of content listed — books, papers, art, stories, literature, and other sources of learning that were... |
| [`extract-skills`](./skills/extraction/extract-skills/) | Load this skill when the user has a job description and wants all the skills extracted and classified — output as a two-column table of skill name and hard/soft type. |
| [`extract-song-meaning`](./skills/extraction/extract-song-meaning/) | Load this skill when the user gives a song name, lyrics, or other information about a song and wants to know what the song means — a summary sentence, the meaning in d... |
| [`extract-video-instructions`](./skills/extraction/extract-video-instructions/) | Load this skill when the user shares a video (uploaded file or link) and wants clear, actionable, step-by-step written instructions extracted from it — e.g. |
| [`extract-wisdom`](./skills/extraction/extract-wisdom/) | Load this skill when the user shares content (podcast, talk, article, interview) and wants the surprising, insightful, and interesting material extracted — ideas, insi... |

### `summarization/` — Summaries of content of any kind — articles, meetings, lectures, debates, newsletters, papers, videos.

| Skill | Description |
| --- | --- |
| [`summarize`](./skills/summarization/summarize/) | Load this skill when the user shares content of any kind and wants a structured Markdown summary — a one-sentence summary, the 10 most important points, and the 5 best... |
| [`summarize-debate`](./skills/summarization/summarize-debate/) | Load this skill when the user shares a debate or discussion transcript and wants a super concise summary of where the parties disagree, the arguments each side makes,... |
| [`summarize-git-changes`](./skills/summarization/summarize-git-changes/) | Load this skill when the user wants git activity summarized — a changelog-style update from recent repo changes, a conventional commit message from a diff, or a summar... |
| [`summarize-lecture`](./skills/summarization/summarize-lecture/) | Load this skill when the user has a lecture or long-video transcript and wants a structured summary with topic headlines, definitions, timestamps for each topic, tools... |
| [`summarize-legislation`](./skills/summarization/summarize-legislation/) | Load this skill when the user shares a political proposal, bill, or piece of legislation and wants an unbiased summary — key points, proposed changes, plus the positiv... |
| [`summarize-meeting`](./skills/summarization/summarize-meeting/) | Load this skill when the user has a meeting transcript and wants structured meeting notes — overview, key points, tasks, decisions, challenges, timeline, references, a... |
| [`summarize-micro`](./skills/summarization/summarize-micro/) | Load this skill when the user wants an ultra-short summary of any content — a micro version with one-sentence summary, 3 main points, and 3 takeaways, each in 12 words... |
| [`summarize-newsletter`](./skills/summarization/summarize-newsletter/) | Load this skill when the user receives a newsletter and wants the most meaningful and useful content extracted from it — summary, key content, opinions, tools, compani... |
| [`summarize-paper`](./skills/summarization/summarize-paper/) | Load this skill when the user provides an academic paper's full text and wants a structured summary of its technical approach — goal, methodology, distinctive features... |
| [`youtube-summary`](./skills/summarization/youtube-summary/) | Load this skill when the user has a YouTube video transcript and wants a concise, structured summary with headings and [HH:MM:SS] timestamps for key points, ending wit... |

### `writing/` — Create, refine, and reshape written content — essays, emails, tweets, LaTeX, blog posts, stories.

| Skill | Description |
| --- | --- |
| [`create-aphorisms`](./skills/writing/create-aphorisms/) | Load this skill when the user gives a topic and wants a list of 20 real, known aphorisms about it — each attributed to the real person who said it. |
| [`create-golden-rules`](./skills/writing/create-golden-rules/) | Load this skill when the user has a codebase, documentation, or set of team practices and wants the implicit rules extracted into clear, enforceable "golden rules" — w... |
| [`create-story`](./skills/writing/create-story/) | Load this skill when the user provides a psychological profile (or profiles) of one or two people — real or fictional, traits, fears, motivations, background — and wan... |
| [`create-story-explanation`](./skills/writing/create-story-explanation/) | Load this skill when the user has complex content (a paper, talk, article, interview) and wants it transformed into a short, conversational, story-like narrative summa... |
| [`doc-coauthoring`](./skills/writing/doc-coauthoring/) | Guide users through a structured workflow for co-authoring documentation. |
| [`enrich-blog-post`](./skills/writing/enrich-blog-post/) | Load this skill when the user has a Markdown blog post that needs enriching for static-site rendering — fixing formatting and structure, and turning ❝ symbols or NOTE-... |
| [`humanize-writing`](./skills/writing/humanize-writing/) | Load this skill when the user has AI-generated (or AI-sounding) text and wants it rewritten to sound natural and conversational, like a real person wrote it — short se... |
| [`improve-academic-writing`](./skills/writing/improve-academic-writing/) | Load this skill when the user provides text that needs to be refined into professional academic or scientific writing — formal, clear, easy to understand, free of word... |
| [`improve-writing`](./skills/writing/improve-writing/) | Load this skill when the user provides text (any language) and wants it refined and improved for clarity, coherence, grammar, and style — without changing its meaning. |
| [`proofread-text`](./skills/writing/proofread-text/) | Load this skill when the user wants text proofread and cleaned up — fixing typos, spelling, punctuation, grammar, and broken formatting (weird line breaks, missing cap... |
| [`write-essay`](./skills/writing/write-essay/) | Load this skill when the user wants a clear, illuminating essay written on a topic — in the style of a named author (defaults to Paul Graham's concise, simple style),... |
| [`write-formal-email`](./skills/writing/write-formal-email/) | Load this skill when the user wants to write or respond to a formal or professional email — polished, concise, properly formatted business correspondence with greeting... |
| [`write-latex`](./skills/writing/write-latex/) | Load this skill when the user wants a LaTeX document created — a complete, syntactically correct .tex file (preamble, document body, proper environments) that compiles... |
| [`write-tweet`](./skills/writing/write-tweet/) | Load this skill when the user wants content turned into an engaging tweet — a concise, punchy message within the 280-character limit, in plain simple language, with sp... |

### `learning/` — Study tools — flashcards, quizzes, mnemonics, reading plans, and explanations.

| Skill | Description |
| --- | --- |
| [`create-flash-cards`](./skills/learning/create-flash-cards/) | Load this skill when the user has study material and wants flashcards created from its key concepts — as Markdown flashcards, or as Anki-ready CSV cards following the... |
| [`create-mnemonic-phrases`](./skills/learning/create-mnemonic-phrases/) | Load this skill when the user gives a list of words and wants memorable mnemonic sentences — the words kept in exact order and spelling, bolded, embedded in five short... |
| [`create-quiz`](./skills/learning/create-quiz/) | Load this skill when the user provides learning objectives and wants review questions generated — up to three challenging questions per objective, with answers, adapte... |
| [`create-reading-plan`](./skills/learning/create-reading-plan/) | Load this skill when the user gives an author name or topic and wants a three-phase reading plan — core, extended, and exploratory books (plus articles/essays), each w... |
| [`explain-docs`](./skills/learning/explain-docs/) | Load this skill when the user has documentation or instructions for a tool and wants better instructions generated — an overview of what it does and why people use it,... |
| [`explain-math`](./skills/learning/explain-math/) | Load this skill when the user provides mathematical equations or concepts and wants them explained in easy-to-understand terms — step-by-step problem solving, techniqu... |
| [`explain-terms`](./skills/learning/explain-terms/) | Load this skill when the user has content with advanced or obscure terms and wants a glossary — each term with a 2-sentence definition, an analogy, and why it matters. |

### `research/` — Source-backed research and multi-source synthesis.

| Skill | Description |
| --- | --- |
| [`deep-research`](./skills/research/deep-research/) | Use when the user asks for thorough research, source-backed synthesis, market or technical landscape analysis, or an evidence-based brief. |
| [`research-synthesis`](./skills/research/research-synthesis/) | Use this skill when the user has multiple sources, notes, files, or search results and wants them synthesized into a structured brief, comparison, or recommendation. |

### `knowledge/` — Vibe Personal Knowledge — set up, enrich, query, and clean up a personal knowledge base.

| Skill | Description |
| --- | --- |
| [`build-knowledge-from-connectors`](./skills/knowledge/build-knowledge-from-connectors/) | Set up or enrich Personal Knowledge from connected Notion, Slack, Gmail, Google Drive, Outlook, and SharePoint sources. |
| [`build-my-knowledge`](./skills/knowledge/build-my-knowledge/) | Internal connected-source Knowledge setup across Notion, Slack, Gmail, Google Drive, Outlook, and SharePoint. |
| [`create-skill-from-knowledge`](./skills/knowledge/create-skill-from-knowledge/) | Turn a repeatable workflow already supported by Personal Knowledge into a reusable Skill. |
| [`discover-knowledge`](./skills/knowledge/discover-knowledge/) | Explain what Knowledge is and how it helps through a short save, recall, and cleanup demo, then offer to build the user's Knowledge. |
| [`interview-my-knowledge`](./skills/knowledge/interview-my-knowledge/) | Internal interview phase of Knowledge onboarding. |
| [`knowledge-mutations`](./skills/knowledge/knowledge-mutations/) | Create, update, or delete durable Personal Knowledge. |
| [`knowledge-onboarding`](./skills/knowledge/knowledge-onboarding/) | Onboard or broadly enrich a user's Knowledge Base by demonstrating its value through a short adaptive interview. |
| [`sanitize-knowledge`](./skills/knowledge/sanitize-knowledge/) | Sanitize Personal Knowledge by finding unsafe, stale, conflicting, duplicated, poorly organized, or non-reusable content and proposing careful fixes. |
| [`userLibrary`](./skills/knowledge/userLibrary/) | User Library are user-curated collections of uploaded documents indexed for semantic search. |

### `vibe/` — Vibe platform skills — Canvas, artifacts, rich UI, and Vibe onboarding (only useful inside Vibe).

| Skill | Description |
| --- | --- |
| [`artifacts`](./skills/vibe/artifacts/) | Create or publish downloadable files, and read or edit previously published artifacts. |
| [`canvas`](./skills/vibe/canvas/) | Use this skill when the user likely wants a separately rendered artifact instead of a chat reply, explicitly mentions a canvas, wants to view or edit a supported exist... |
| [`canvas-react`](./skills/vibe/canvas-react/) | Use this skill when the user asks you to build an application, a simulation, a game, or any UI that could be built with React. |
| [`mistral-self-knowledge`](./skills/vibe/mistral-self-knowledge/) | Mistral AI and Vibe (formerly Le Chat): how to use Vibe (what it can do, where a feature or setting is, desktop and mobile apps, interface language, voice, files, imag... |
| [`rich-ui`](./skills/vibe/rich-ui/) | Always use this skill when an inline UI component or a visual answer would be clearer than a text-only answer, regardless of the user's language. Available components... |
| [`vibe-work-onboarding`](./skills/vibe/vibe-work-onboarding/) | Run this reusable onboarding flow when a user wants to set up or discover Work mode, Skills, Connectors, and useful first tasks in Vibe Work. |

### `meta/` — Skill creation, prompt structure, tagging, and other meta tooling.

| Skill | Description |
| --- | --- |
| [`convert-to-markdown`](./skills/meta/convert-to-markdown/) | Load this skill when the user has content in another format (HTML page, pasted article, export, messy text) and wants it converted to clean Markdown — a complete, fait... |
| [`create-fabric-pattern`](./skills/meta/create-fabric-pattern/) | Load this skill when the user wants to create a new Fabric pattern from a description of what they want to accomplish (e.g. |
| [`create-tags`](./skills/meta/create-tags/) | Load this skill when the user wants tags/keywords extracted from text content, e.g. |
| [`infographic-outline-creator`](./skills/meta/infographic-outline-creator/) | Create infographic outlines and visual content structures. |
| [`skill-creator`](./skills/meta/skill-creator/) | Load this skill before creating, updating, or deleting Skills, or whenever you plan to modify your own Skill files under skills/. |
| [`structure-prompt`](./skills/meta/structure-prompt/) | Load this skill when the user wants to convert rough input, a task description, or an idea into a well-structured, production-ready AI prompt with IDENTITY, STEPS, OUT... |

### `tools/` — Utility tools — fetching and converting content.

| Skill | Description |
| --- | --- |
| [`youtube-transcript`](./skills/tools/youtube-transcript/) | Load this skill when the user wants to extract, download, or generate a transcript from a YouTube video (captions, subtitles, or a full text transcript with or without... |
