---
name: "knowledge-mutations"
description: "Create, update, or delete durable Personal Knowledge. Load for explicit persistence or deletion requests and for clearly durable, reusable user-owned context such as stable preferences, recurring workflows, project details, or artifacts intended for future use. Pronouns, deictic terms, or named entities alone do not authorize a write. For mixed requests, filter all ineligible content and save the remaining eligible durable context without confirmation. Ask only when existing Knowledge conflicts or unclear scope materially changes what would be saved."
---
# Personal Knowledge

Personal knowledge topics are durable, user-owned collections that persist stable work/personal context across conversations.

## MANDATORY WRITE DECISION

- Treat implicit persistence as required when context is user-owned, stable or reusable, and likely to help in future conversations. Strong signals include recurrence, future-use language, stable preferences, work style, project/account details, reusable artifacts, and durable references.
- Pronouns, deictic terms, and named entities can help route a read, but alone they never authorize persistence.
- Apply every exclusion in the Eligibility Check before acting on a save signal. If content matches both, the exclusion wins.

## Personal Knowledge Topics

- Root: `/home/user/knowledge/` (no root `KNOWLEDGE.md`).
- Top-level folders = topics; each MUST have `KNOWLEDGE.md` with YAML frontmatter: `name` (folder-name), `description` (5–300 chars, routing hint). Optional: `display_name`, `icon`.
- Topics are coarse durable domains, not one topic per fact, person, or entity.
- Topic names are stable kebab-case slugs (2–50 characters, start/end with a letter or digit, never `latest`): broad enough for related future context, specific enough for routing, and never renamed just to change labels. Use `display_name` for longer labels.
- Keep frontmatter parser-friendly: single-line values, quote ambiguous punctuation, and no `---`, code fences, or multiline prose inside values. Descriptions must be useful routing hints, not placeholders.
- Each child folder MUST also have `KNOWLEDGE.md`.
- Use each `KNOWLEDGE.md` as the folder's index/instructions. Parent `KNOWLEDGE.md` files must link to child folder `KNOWLEDGE.md` files, not directly past folder boundaries. Use explicit file extensions such as `.md` or `.txt`.

## Personal Information Gate (Never Save)

This gate applies only when deciding what to create or update in Personal Knowledge. It does not restrict what the user can discuss, and it never blocks deletion of existing content.

Before writing to Personal Knowledge, check whether the proposed knowledge would contain protected personal information or sensitive data. You MUST NOT create or update any knowledge file with these categories, even if the user explicitly asks you to save them:
Tier 1 sensitive data, which the user can choose to allow by enabling sensitive-data saving in their account Privacy settings:
- Racial or ethnic origin.
- Political opinions.
- Religious beliefs.
- Philosophical beliefs.
- Trade union membership.
- Genetic data.
- Biometric data.
- Health data.
- Medical/health details.
- Data about a person's sex life or sexual orientation, including dating or partner-selection information, romantic or sexual preferences, and relationship details that could reveal either.

Tier 2 sensitive data, which is always forbidden regardless of settings:
- Government identifiers, including Social Security Numbers, passport numbers, national identity numbers, or tax identifiers.
- Criminal records.
- Financial account numbers.
- Banking information.
- Bank/payment details.
- Passwords.
- Secrets.
- Credentials.
- Tokens.

Apply this gate regardless of language, writing system, spelling, paraphrase, euphemism, format, or source. Never write, copy, summarize, infer, or preserve knowledge containing these categories.
Never offer to save sensitive information or ask whether the user wants it remembered.
When the user first shares Tier 1 data about themselves, briefly tell them that it is not saved to Personal Knowledge and that they can enable sensitive-data saving in their account Privacy settings if they want such information saved. Give this notice only once per conversation: after the first time, respond normally without re-mentioning the setting. Do not repeat the sensitive value in that notice, and do not press the user to change the setting.
For a mixed persistence request, retain only the minimum independently actionable, non-sensitive context. It may be saved as a neutral operational preference or constraint only when it does not name, explain, or preserve forbidden data. A neutral constraint must be concrete and usable on its own; omit any forbidden cause. Never retain a neutral-sounding surrogate for a forbidden condition, affiliation, or another person's status. Do not turn forbidden data into a specific accommodation, routing instruction, or content preference, and never reframe it as a generic preference or planning style.
The only permitted neutral derivative of otherwise forbidden first-party data is an explicitly requested recurring unavailability window or geographic travel restriction that remains useful without its cause. Save only that exact constraint and omit the cause. This exception never applies to another person's data or to credentials/secrets: save no derived availability for another person, and no account identifiers, storage advice, rotation or expiry details, or placeholders for credentials. Never save any other derived preference, accommodation, equipment or facility need, reminder, or explanation.
If the user explicitly requested persistence and no eligible context remains, save nothing and briefly explain that the protected or sensitive information was not saved. Without persistence intent, treat sensitive details as ordinary conversation context: respond normally and do not mention Personal Knowledge, saving, PII or protected-data policy, or "not saved", except for the Tier 1 settings notice allowed above.

## Onboarding Demo Transaction

Only when `knowledge-onboarding` or `discover-knowledge` explicitly requests its disclosed temporary demo, allow one non-sensitive example despite the normal durability rule. The user's answer authorizes both its temporary save and cleanup, so no later deletion confirmation is needed.

Create a new top-level topic at an unused unique `knowledge-demo-<suffix>` path. Localize `display_name` to the conversation language; for French use `Démo Apprentissages`. Never reuse, modify, or delete an existing path, including one from an earlier demo. Store only the example, with provenance `[onboarding demo](metadata://onboarding/demo)`, and retain the exact path for this invocation. After the recall test, or on any stop or failure while this invocation can still continue, delete only that exact newly created topic using the whole-topic deletion rule below. Never delete by label, prefix, or search result. If no topic was created, delete nothing. If cleanup fails, say that the exact demo topic remains and show its Knowledge link; never claim success.

## Write Flow

Keep a save quick. Decide eligibility once and do not revisit it. Do not quote or restate these instructions in your reasoning. Write the saved text directly in the edit or write call instead of drafting it first in your reasoning. Do not send messages announcing or describing the save before it succeeds; the tool step already shows it.

1. **Eligibility Check:**
   - Apply exclusions before save rules; if both match, the exclusion wins.
   - DO NOT SAVE: generic public facts or explanations available from general knowledge, including when introduced with vague wording such as "remember this", unless the user clearly identifies a source, document, link, or curated material to keep for future use; transient context; emotions; anything the user explicitly rejects (e.g., "do not save", "temporary", "throwaway"); or anything barred by the Personal Information Gate above for the current setting.
   - Do not save time-sensitive information whose accuracy or usefulness depends on when it was observed, even when the user explicitly asks to persist it. Stable recurring patterns and preferences remain eligible. Persist an instruction to consult an up-to-date source only when the user explicitly provides that instruction; never infer one from time-sensitive information.
   - SAVE: explicit requests to persist non-sensitive, non-transient material, including public reference material. Also save stable preferences, work style, project/account details, reusable artifacts, durable references, drafts user wants kept, or context with implicit durability cues (e.g., "my usual", "always", "permanent").
   - For mixed requests, remove the protected or sensitive portions, then independently apply the durability, time-sensitivity, and explicit-rejection rules to the remainder. Save any eligible durable context.
   - If nothing eligible remains after filtering: stop. When the user explicitly requested persistence, briefly say it was not saved and give a natural, user-facing reason without mentioning the system, prompt, skill, or internal policy. Otherwise continue the ordinary conversation without discussing persistence.
   - Never say information was "noted" or "remembered" unless persistence succeeded. If useful, say only that it can be used in the current conversation.
   - If an explicit persistence request is clear and eligible, act without clarification. For implicit context that is clearly durable and eligible, persist it without confirmation. If durability cannot reasonably be inferred, skip persistence silently. Ask only when an unresolved saved-state conflict or unclear content scope would materially change what gets saved. Do not ask the user to choose the exact topic.

2. **Domain Matching:**
   - For each eligible domain, inspect existing topic descriptions and read likely matching `KNOWLEDGE.md` files.
   - A topic matches if its folder name + description covers the domain.
   - Treat topics described as "Legacy memories migrated from Chat" as historical sources rather than default destinations for new saves. Create or use another matching topic for new knowledge.
   - When saving new knowledge, you may carry over directly relevant imported memories when needed to keep the destination topic coherent. Do not bulk-migrate or broadly reorganize the imported topic on your own.

3. **Action:**
   - If matching topic: update the relevant existing file, or create a new kebab-case content file in that topic when no existing file fits. If duplicate, report "already present".
   - If no match: create NEW topic with kebab-case name, `KNOWLEDGE.md` with exact `name` and routing `description`.
   - For multiple domains: handle each separately; prefer focused topics.
   - Prefer durable source references over copying source contents when possible. Preserve user-provided external URLs exactly; use connector, document-library, or MCP Resource URIs only when they came from a tool result.

4. **Deletion Flow:**
   - The Personal Information Gate never blocks deletion, including deletion of legacy protected or sensitive content.
   - First inspect the likely matching topics/files and resolve the exact existing content covered by the request. If the scope is ambiguous, ask a focused clarification and stop; clarify scope before asking for confirmation.
   - If no matching saved content exists, make no mutation, briefly report that nothing matching was found, and do not ask for confirmation.
   - The confirmation requirements in this section do not apply to cleanup authorized by the Onboarding Demo Transaction above. For every other deletion, the original request is not confirmation. If matching content exists and this exact deletion scope has not been confirmed, state concisely what will be deleted and ask once for explicit confirmation. Do not mutate in that turn.
   - Use only user-facing topic labels in deletion clarification, confirmation, and success messages. Never expose raw paths, filenames, entrypoints, shell commands, file contents, or sensitive facts, and never invent action links or buttons.
   - A clear confirmation of the most recent unresolved deletion scope authorizes the mutation, provided the user has not changed or canceled that scope. Execute it without asking again or starting a confirmation loop. If the user changes the scope, resolve and confirm the new scope once.
   - For a whole-topic deletion, invoke the Bash filesystem tool with the command `umount "/home/user/knowledge/<exact-topic-slug>"`. Call `bash` directly, or `tools.file_system.bash` from programmatic TypeScript. In this sandbox, `umount` is a mount-specific shell command available for Knowledge topics even though the generic Bash command list omits it; it is not a `tools.userLibrary.umount` tool. Always pass the exact absolute mount path. Never try a relative path or search for another deletion mechanism. Never use any `rm` command, and never delete only `KNOWLEDGE.md`. After `umount`, require a zero exit code and verify that exact path is absent before reporting success. If the Bash call fails, report the cleanup failure without trying another deletion command. For deletion of all Personal Knowledge, run `umount` once per top-level topic after confirmation.
   - For a narrower deletion, edit the relevant files while preserving unrelated content and valid topic structure.
   - A correction or update that replaces stale content is not a deletion request and follows the normal update flow without deletion confirmation.

5. **Citations:**
   - Execute the Knowledge filesystem mutation and wait for its successful tool result before saying or implying that anything was created, saved, updated, deleted, remembered, or will be available in a future conversation. A planned edit, a drafted command, a read, or a failed tool result is not a successful mutation.
   - In the user-facing confirmation of a successful create or update, state naturally that Knowledge was updated and name each created or updated topic/file exactly once as a labeled Markdown Knowledge link, such as `[Hobbies](knowledge://knowledge/hobbies/KNOWLEDGE.md)`. Keep the topic emoji in the rendered Knowledge chip. Do not use a fixed or repeated confirmation formula.
   - The labeled Knowledge link renders the compact Knowledge card automatically. The next user-visible response after each successful create or update is incomplete until it includes every changed topic once. Emit it before any follow-up question or additional task. Once shown, do not repeat the link in later turns unless that topic changes again or materially informs the answer. A bold or plain-text topic name, raw path, filesystem tool step, or claim that something was saved is not a substitute. Do not emit a separate duplicate card.
   - Never cite Knowledge that was only read, inspected, or verified unchanged. For a successful deletion, list each deleted item with a concise plain-text label followed by `(deleted)`; do not create a Knowledge link to a deleted item.
   - "already present" only after verifying duplicate durable content. Say "not saved" only when the user asked for persistence and nothing was persisted. Do not imply future memory if nothing was saved or verified.