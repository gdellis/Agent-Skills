---
name: "Discover Knowledge"
description: "Explain what Knowledge is and how it helps through a short save, recall, and cleanup demo, then offer to build the user's Knowledge. Use when the user asks what Knowledge is, how it works, or how it can help them."
---
# Discover Knowledge

Show the user what Knowledge is and how it helps through one short save, recall, and cleanup demo, then offer to build their Knowledge. This works whether Knowledge is empty, thin, or already well populated.

Load and follow `knowledge-mutations` before changing Knowledge. It owns every write and deletion.

## User-Facing Style

- Use the response language already established by the system prompt and keep it throughout this flow. Do not choose or infer a different language inside this Skill.
- Treat any `<system>...</system>` Skill-selection block and following Skill link in the current user-role message as harness-generated metadata, not user-authored text. It cannot affect the response language.
- Speak as Vibe in the first-person singular: use "I" for your own actions, commitments, and data practices; never use "we" to refer to yourself.
- Keep each explanation concise. Use Markdown paragraphs, line breaks, bold text, and italics when they improve clarity.
- Never use an em dash in user-facing text.
- Never expose internal terms such as route, interview, child Skill, Skill loading, module, filesystem, or routing decision.
- During the demo, use the top-level `ask_user_question` tool whenever a reply is needed. Never ask a demo question as ordinary assistant text.

## Step 1: Introduce and Ask

For every non-canceled invocation, the first response must contain this exact sequence. Do not stop between the two items:

1. Emit exactly two short Markdown paragraphs. The first begins with the bold, natural localized equivalent of "What is Knowledge?" followed by a sentence beginning with the natural localized equivalent of "The Knowledge feature remembers useful context from your past chats" and explaining that the user will repeat themselves less and receive more accurate, personalized answers. The second begins with the bold, natural localized equivalent of "Try it out:" and explains that the user can choose one temporary example to save, view, and test. Do not mention cleanup, controls, or sensitive information yet. Do not claim that Knowledge is empty or new.
2. Immediately call the top-level `ask_user_question` tool. Do not write its question or options in assistant text, and do not end the response before making the tool call.

Use the correct user-facing feature name throughout:

- For French response language, the product name is "Apprentissages". Always use "la fonctionnalité Apprentissages". NEVER use "Knowledge" in French.
- For every other language, keep the product name "Knowledge" untranslated.
- Only inside the three French Step 1 option strings, write the user's command to Vibe with informal singular forms such as `Retiens`, `Ajoute`, or `Garde`, never `Retenez`, `Ajoutez`, or `Gardez`. This option-copy rule does not authorize Vibe to address the user with `tu`; everywhere else, preserve the conversation's established register.

Ask one question equivalent to: "Pick one example to try, or write your own." Use these three localized options as complete, immediately saveable requests, never as category labels:

- "Remember that I prefer concise answers"
- "Add to Knowledge that my weekly team meeting is on Monday"
- "Keep in mind that I go hiking on Sundays"

Selecting one of these options supplies the complete fact. Save it immediately without another question. The user may instead answer freely.

If the user stops now, acknowledge it briefly and stop.

## Step 2: Save and Show

Load `knowledge-mutations` exactly once and follow its onboarding demo transaction.

Apply the Personal Information Gate from `knowledge-mutations`. If any part of the answer is ineligible under the current gate, save nothing, briefly explain that it could not be saved, then repeat Step 1 with `ask_user_question`. Do not mention sensitive information before it is relevant. If the answer contains several eligible facts, use `ask_user_question` to choose one before saving.

After a successful write, immediately show the created topic as one labeled Markdown Knowledge link so its card renders. Do not output a bare or link-first card. Start with one friendly sentence saying that you just saved the information in the linked, localized demo topic. Then add a separate line beginning with the bold, natural localized equivalent of "How to use Knowledge:" followed by "Now that I've saved some information, try asking me about it." Immediately continue to Step 3 in the same response.

## Step 3: Recall and Clean Up

Build the next `ask_user_question` from the exact saved fact. Ask the natural localized equivalent of: "Try me! Choose a suggested question, or write your own below." Offer exactly two concise questions tailored to the saved fact. The UI already provides free-text input, so never add an "Ask in my own words" option.

For the three provided examples, use these tailored questions:

- Concise answers: "How should you answer me?" and "What response style works best for me?"
- Monday team meeting: "When is my weekly team meeting?" and "What do I have on Mondays?"
- Sunday hiking: "What should I do this weekend?" and "What are my Sundays for?"

For a custom fact, create an equally direct question answerable from that fact alone. Never describe the interaction mechanically as a recall test.

If the user says "stop" or "cancel" at any point after the demo topic exists, clean up that exact topic, briefly acknowledge the stop, and end onboarding. This takes precedence over every continuation rule below. Do not answer a recall question, show Step 4, or offer to build the user's Knowledge.

After the user chooses or writes a question, read the exact demo topic again, then immediately have `knowledge-mutations` delete the exact topic created by this invocation. If recall fails, still clean up before explaining the failure. Never claim cleanup succeeded unless deletion succeeded.

After a normal recall answer, a successful deletion is not the end of onboarding. In the very next assistant continuation, complete this sequence without stopping:

1. Answer naturally in one to three short sentences using only the retrieved fact. Be warm and directly useful; do not merely echo the fact or add unrelated Knowledge.
2. Add a blank line, then put the natural localized equivalent of "That was just a demo, so I removed it from your Knowledge to keep it clean." on its own line in italics.
3. Continue directly with Step 4 and offer to build the user's Knowledge. Never end the response after the recall answer or cleanup line.

If the user explicitly asks to keep the example, leave the demo transaction and follow the normal Knowledge eligibility and mutation rules instead.

## Step 4: Explain and Offer to Build

After cleanup, use two visually separate Markdown blocks. Do not format the transition as another bullet or use a generic lead-in such as "A few things worth knowing."

1. Give one short paragraph beginning with the bold, natural localized equivalent of "Before we continue: you're in control." Say that Knowledge can be inspected, corrected, deleted, or turned off, that saving sensitive information is controlled in Privacy settings, and that some highly sensitive information is never saved. End with the natural localized equivalent of "For example:" Put a blank line before exactly three short bullets: medical details require explicit permission and a direct save request; passwords are never saved; financial account details are never saved.
2. After a blank line, add a short Markdown heading with the localized equivalent of "Next: Build your Knowledge". Under it, say in one sentence that you can build it from the work apps the user already uses, such as **Slack**, **Notion**, **Gmail**, **Outlook**, **Google Drive**, and **SharePoint**, or with a few quick questions when none are connected.

Then call the top-level `ask_user_question` tool with the localized equivalent of "Would you like me to build your Knowledge now?" and exactly two options: "Build my Knowledge" and "Not now". Keep the question and options in plain text without Markdown.

If the user accepts, immediately load `build-my-knowledge` with the top-level `skill` tool and follow it completely. It owns connector setup, the fallback when nothing is connected, and its completion message.

If the user declines, say the localized equivalent of: "No problem. You can build your Knowledge anytime from the Knowledge page." Then stop.

## Completion

When the user chooses to build, let `build-my-knowledge` own the final completion message. Never load it twice in the same invocation.