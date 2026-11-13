---
name: "Sanitize my Knowledge"
description: "Sanitize Personal Knowledge by finding unsafe, stale, conflicting, duplicated, poorly organized, or non-reusable content and proposing careful fixes. Use for a broad Knowledge cleanup, not connector import or adding one fact."
---
# Sanitize my Knowledge

Review the user's Personal Knowledge, identify content that should be corrected, reorganized, consolidated, or removed, and apply only changes the user approves.

## Adapt to the Knowledge Base

Inventory the complete topic hierarchy and check each KNOWLEDGE.md entrypoint's name and description. Count entrypoint paths with a tool when reporting totals; .keep files and source metadata are not topics. Read exact paths in batches that show every file in full. Reread truncated or failed reads before judging content, then adapt:

- **Empty (no topic files):** say there is nothing to sanitize and suggest "Set up my Knowledge" or "Build my Knowledge from Connectors". Create nothing.
- **Thin:** inspect every file. Do not manufacture work because the base is small. A heading-only topic is a removable placeholder even though its entrypoint is required while it exists; preserve useful topics.
- **Large:** inspect every description, then review content in coherent batches. Prioritize sensitive, contradictory, stale, overlapping, and weakly routed areas. If the review is incomplete, say so and continue from a temporary checkpoint outside Personal Knowledge; delete it when finished.
- **Mixed or merely interesting:** inspect exact spans. Distinguish reusable facts from trivia, and preserve adjacent safe content unless separately approved for removal.

Treat Personal Knowledge as the only source of truth for this review. Account, session, organization, and workspace metadata are not evidence about the user.

## Language

Determine the most common language in substantive Knowledge prose, weighted by the amount of natural-language content rather than the number of files. Ignore frontmatter keys, metadata, provenance links, URLs, code, and proper nouns.

Use that dominant language for any newly written headings, topic descriptions, or rewritten prose. If Knowledge is empty, use the conversation language. If there is no clear dominant language or different topics are intentionally written in different languages, preserve each topic's language and ask before translating anything.

Never translate the full Knowledge Base for consistency. Never translate quotes, source titles, names, or technical identifiers. A language mismatch alone is not a reason to rewrite otherwise useful content.

## Retire memory imports

This applies to topics described as "Legacy memories migrated from Chat" (usually memories, memories-2, and so on, with category or chunk files), and imported-knowledge (one entrypoint with dated "Imported on" sections from other assistants).

**Invariant:** after an approved cleanup, every non-sensitive fact must exist in ordinary Knowledge or be a verified duplicate there, and the entire import topic must be gone. Never partially edit or retain the import topic. Never drop a fact merely because it is stale, weak, low-value, or uncertain.

Inventory every file or section. For long imports, make a temporary checklist outside Personal Knowledge mapping every source bullet or paragraph to an existing duplicate, a destination, or forbidden sensitive or non-factual removal. Preserve wording, available provenance and import dates, and uncertainty or historical status. Create ordinary domain topics or files when needed. Do not rely on manually retyping an exhaustive list: copy any not-yet-routed non-sensitive remainder verbatim into a clearly labeled review file within an ordinary topic before deletion.

Treat cleanup as all-or-nothing per import topic. One confirmation must name the destinations and whole topic to delete. Before approval, change nothing. After approval, write the facts, verify checklist and source/destination counts, then delete the whole import topic and checklist and verify no source files remain. Report an incomplete migration or deletion clearly. A decline or report-only choice changes nothing.

## Sanitize

Check for issues likely to harm future answers. Length, repetition, and old dates alone are not findings. For every candidate edit, identify the exact source span and preserve all verified facts, named scopes, conditions, dates, provenance, and useful retrieval placement unless the user specifically approves their removal. Prefer the smallest line edit; never remove a whole section to fix only its stale lines. Mark uncertainty instead of guessing. Check for:

1. **Sensitive content:** protected personal information, secrets, credentials, banking data, or other content barred by the Personal Knowledge information gate. Treat values as tainted: never output them in findings, questions, examples, or reports. Refer only to location and type.
2. **Incorrect or stale content:** contradictions, superseded current-state claims, unsupported inferences, ambiguous ownership, and unsupported current dates or roles. Check each claim's scope independently. In memory-import inboxes, preserve these claims as historical or unverified rather than removing them.
3. **Duplication:** read complete source and destination files, including children, before proposing a merge. Similar wording across named teams, projects, events, or source dates is not equivalence. Dated examples, reviews, and incidents remain useful evidence even when their prose repeats: do not offer to delete them merely for repetition, and do not replace their content with a list or range of dates. If useful repetition crowds retrieval, report an index or navigation improvement that keeps every original entry. Trim transient chatter lines separately while keeping dated decisions and rules. Prefer removing a duplicate line while keeping useful topics. Merge at most one named source into one named survivor per approval, only when every distinct fact and its retrieval home survives. Otherwise report the overlap.
4. **Poor organization:** vague descriptions, misplaced content, broken parent-child navigation, over-fragmented topics, and headings that do not help retrieval. Check whether parent entrypoints link to their existing child topics.
5. **Low reuse value:** transient status, chat leftovers, empty placeholders, and isolated trivia. Harmless preferences may be useful outside their current topic. For memory-import inboxes, low reuse affects only destination and labeling; it never authorizes dropping a non-sensitive fact. Outside those inboxes, raw imports, transcripts, dated reviews, source metadata, and uncertainty caveats are provenance; do not tidy them away. If a weak claim contains a date or source, retain that provenance when trimming the claim. A weak line does not make an otherwise useful topic disposable.
6. **Weak facts:** vague statements that lack enough context to affect an answer. Treat them as gaps requiring user input, not permission to invent detail. In memory-import inboxes, preserve them with their uncertainty instead of dropping them.

## Review before changing

Give a one-sentence health summary, followed by at most eight findings ordered by impact:

- **P0:** unsafe or likely to produce wrong answers.
- **P1:** likely to block retrieval or create conflicting answers.
- **P2:** organization and low-value cleanup.

For each finding, name inventoried paths, explain the risk, and state the smallest proposed scope, including metadata edits. Distinguish verified problems from uncertain candidates. Before a group proposal, count its members with a tool; a visual tally is not verification. If uncertain, omit the count and do not offer a group edit. If nothing needs sanitizing, say so. For memory-import retirement, the proposed scope is the whole import topic, not line edits within it.

When action is warranted and the user has not chosen, call the top-level ask_user_question tool once with one brief question and 2–4 string options, using ask_user_question({questions:[{question:"...",options:["...","..."]}]}). Offer the single highest-impact fix alone, other safe line edits separately, review one by one, or report only. Ask for a missing authoritative fact instead of bundling another edit. Never include a topic deletion, merge, uncertain edit, or unrelated fix in a broader option. Memory-import retirement is the exception: offer its complete migration and whole-topic deletion as one atomic option, never as partial inbox edits. If nothing needs changing or the user already chose, do not ask again.

## Apply approved changes

Before changing Knowledge, load and follow the knowledge-mutations Skill. It owns the sensitive-information gate, structure, deletion confirmation, and success reporting. For approved memory-import retirement, continue to apply those safeguards, but do not apply its ordinary save-eligibility filter or prohibition on bulk migration: every non-sensitive imported fact must be preserved as specified above.

Apply only the approved spans. If the user says "only" or "keep the rest", every other line and frontmatter field is outside scope. Leave adjacent facts, headings, descriptions, metadata, and history intact; do not invent facts or rewrite for tone or language consistency. A vague "safe cleanup" reply does not approve memory-import retirement. For other changes it permits only narrow line edits, even after a deletion question. For topic deletion or consolidation, follow knowledge-mutations confirmation and require a clear yes to each named source and, for a merge, its survivor. A clear yes to the complete memory-import retirement plan is the required confirmation; do not ask again or partially edit the import topic.

Diff each changed file against its original and restore anything outside the approved scope. Verify preserved facts, dates, scopes, and metadata, then summarize what changed, what survived, and what still needs input.