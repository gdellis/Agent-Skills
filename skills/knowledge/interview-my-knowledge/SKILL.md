---
name: "Interview my Knowledge"
description: "Internal interview phase of Knowledge onboarding. Load only from knowledge-onboarding, build-my-knowledge, or build-knowledge-from-connectors; do not select it directly from a user request."
---
# Interview my Knowledge

Run a short, adaptive Knowledge enrichment interview. Enrich at least two reusable pieces of the user's personal or professional context, visibly demonstrate how Knowledge works, and deliver a result that is materially better because of what Vibe knows.

A populated Knowledge Base is context for deeper questions, not a reason to skip the interview. Find knowledge that will reduce repeated prompting or improve a recurring task; do not complete a generic profile for its own sake.

## User-Facing Style

- Match the language of the previous user-visible assistant message throughout the interview.
- Never ask questions designed to elicit protected personal information or sensitive data.
- Never narrate internal inspection, tool calls, or file operations. A concise confirmation of what was added to Knowledge and why it will improve future help is a user-facing outcome, not internal narration.
- During the interview, use at most two short sentences before one clear question. Aim for fewer than 50 words total.
- Ask one single-focus question at a time. Do not use headings, questionnaires, nested questions, or explanatory bullet lists.
- Acknowledge an answer only when confirming a save, resolving ambiguity, or explaining a transition. Otherwise, ask the next question directly. Never acknowledge by merely repeating or paraphrasing the answer.
- Accept "skip" or "stop" without pressure. "Skip" skips only the current question and continues the interview; "stop" ends the interview immediately.
- Keep the onboarding narration concise, but briefly explain each transition so the user knows what was completed, what comes next, and why. The useful task produced at the end may be longer.
- Ask open-ended enrichment questions as normal chat text so the user can answer by typing, voice, or file. Use the top-level `ask_user_question` tool only for bounded choices such as selecting the final action or confirming a correction. Never batch the adaptive interview into one questionnaire.
- Make every question visually prominent. Put any question asked in chat on its own bold line. Keep `ask_user_question` questions and options as plain text because the UI provides their emphasis.

## Phase 1: Prepare and Ask

If `knowledge-onboarding` or `discover-knowledge` was loaded earlier in this conversation, it already introduced the benefit, user control, and privacy. Do not repeat that introduction.

Otherwise, before loading anything or inspecting Knowledge, send the control introduction as its own message: Give one short paragraph beginning with the bold, natural localized equivalent of "Before we continue: you're in control." Say that Knowledge can be inspected, corrected, deleted, or turned off, that saving sensitive information is controlled in Privacy settings, and that some highly sensitive information is never saved. End with the natural localized equivalent of "For example:" Put a blank line before exactly three short bullets: medical details require explicit permission and a direct save request; passwords are never saved; financial account details are never saved. It is not an interview question, so the sentence and bullet limits in User-Facing Style do not apply to it. Then, without waiting for a reply, continue with the steps below; the first-question message follows the opening rules below unchanged.

If `knowledge-mutations` is not already loaded in the current invocation, load and follow it. Then inspect the available Knowledge topic descriptions and read enough relevant topics to choose the starting path below. When a topic choice or guided start is needed, call one `ask_user_question` at a time and wait for its answer before asking the next question. Never batch sequential routing questions.

Treat persisted Knowledge, not account, profile, email, organization, workspace, environment, or session metadata, as the source of personal context for this interview. Those labels may belong to a test setup or shared workspace. Never challenge a saved name, role, company, or team because it differs from such metadata, and never spend the first question confirming identity that is already in Knowledge.

### Choose a Topic When Helpful

If at least two distinct existing topics contain meaningful reusable context, call the top-level `ask_user_question` tool before the first interview question. Ask the natural localized equivalent of: "I found a few areas in your Knowledge that we could build on. Which one would you like me to focus on?" Offer two or three short user-facing topic labels drawn from the user's actual Knowledge, prioritizing useful topics with room to deepen. Never expose paths or invent a topic. The user chooses one topic, not several. This routing choice does not count toward the interview question limit.

After a topic choice, focus the first interview question on the selected topic and follow the same interview rules below.

### Guide Empty or Very Thin Knowledge

If Knowledge is empty or contains only one meaningful fact, skip the topic choice and guide the user with two sequential closed questions before the first open question. Use the top-level `ask_user_question` tool for both. These choices only route the interview; never save them as facts.

First ask the natural localized equivalent of: "What would you like Knowledge to help with first?" Use exactly these localized options:

- "Help me achieve my goals"
- "Remember context about my project"
- "Prepare for meetings"

Then ask one follow-up based on the selected area:

- **Help me achieve my goals:** Ask "What kind of goal should I help with?" with "A work goal", "A personal goal", and "A habit or routine".
- **Remember context about my project:** Ask "What project context matters most?" with "Goals and scope", "Decisions and constraints", and "People and roles".
- **Prepare for meetings:** Ask "What should I tailor first?" with "Audience and purpose", "Agenda and format", and "Recurring context".

After those two choices, ask one corresponding open question as normal chat text on its own bold line:

- A work goal: "What work goal are you currently trying to achieve?"
- A personal goal: "What personal goal are you currently working toward?"
- A habit or routine: "What habit or routine would you like help maintaining?"
- Goals and scope: "What outcome should I keep in mind for this project?"
- Decisions and constraints: "What project constraint or decision should I remember?"
- People and roles: "Who should I remember on this project, and what is their role?"
- Audience and purpose: "Who are your meetings usually for, and what should they help achieve?"
- Agenda and format: "What meeting format should I default to?"
- Recurring context: "What recurring meeting context should I account for?"

Ask a third closed question only when a free-text routing answer is too ambiguous to select an appropriate open question. Never turn this guided start into a profile questionnaire.

Adapt the interview to the available Knowledge:

- **Useful Knowledge Base:** infer a likely pain from missing context or relationships around existing topics. Do not re-collect or ask the user to verify known profile facts.
- **Thin Knowledge Base:** use what exists as an anchor, then follow the guided empty-or-thin path above.
- **Empty Knowledge Base:** follow the guided empty-or-thin path above without requesting a biography.

Prioritize the most likely user pain that the current Knowledge Base cannot yet solve: repeated explanation, a recurring task that still gets generic results, or missing context such as a useful preference, default, constraint, relationship, decision rule, or exception. Choose the lowest-effort useful question, a fallback area if it is hard to answer, and one or two realistic payoff candidates. Treat inferred pains as hypotheses, not facts to save.

When following the existing-topic path, begin the first-question message with one short user-facing sentence using the natural localized equivalent of: "I checked what's already in your Knowledge and found {stable current fact}. Let's build on it to make Vibe more useful for you." Include a labeled Markdown Knowledge link on the fact. Then ask the easiest useful question suggested by the missing context around that fact. Compare every date with the current date: never present a past deadline or potentially stale status as current. Avoid an uncertain fact instead of asking the user to audit it, unless a clear contradiction blocks the flow. This is the first visible proof that Knowledge is already useful. Do not inventory the Knowledge Base.

When following the guided empty-or-thin path, begin the first closed-question turn with one short sentence matching the actual state. If empty, use the natural localized equivalent of: "Your Knowledge Base is currently empty, so two quick choices will help me find the most useful place to start." If it contains one meaningful fact, say instead that the Knowledge Base is still light. Do not imply that anything else was already known or saved, and do not repeat this explanation before the open question.

Begin the first open interview question on a new paragraph.

End that first open-question message with a separate italicized line, preceded by a blank line, conveying that a short answer, voice note, or relevant file is fine. Wrap the whole sentence in Markdown italics (`*...*`) and translate it naturally into the interview language. Include this hint only with the first open question; never attach it to an `ask_user_question` prompt or repeat it later.

Ground each question in what is already known when possible, without reciting the Knowledge Base or sounding intrusive. Use at most one short clause to say what the answer would help Vibe do better.

## Phase 2: Interview

With useful existing Knowledge, usually ask two or three meaningful questions. Keep an internal count of every question that requires a reply. Never ask a fifth question unless the user explicitly chooses to continue. Do not transition after one shallow answer. A rich voice answer or file may cover several gaps, but ask at least one intelligent follow-up unless the user says "stop".

For the guided empty-or-thin path, ask the mapped open question and at most one focused open follow-up when the first answer is too vague. Never ask more than two open questions. The closed routing choices do not count.

Complete the interview only when all of these are true:

1. At least two distinct reusable facts, examples, preferences, constraints, decision rules, or workflow details were improved or confirmed. They may belong to the same topic. In the guided empty-or-thin path, one specific durable fact is sufficient when it can support a strong personalized payoff.
2. At least one eligible durable fact was saved.
3. There is enough specific context to attempt a strong personalized payoff.

An answer is meaningful only if it adds specific, durable information that could change future assistance. A vague answer does not count. Ask a focused follow-up instead of saving a broad paraphrase or pretending it enables a useful action.

Keep the interview adaptive rather than following a mandatory question sequence. Choose each next question by balancing low user effort, likely information gain, and future usefulness.

Questions must require only one mental operation and be answerable from immediate memory in one sentence or one tap. Prefer a simple preference, default, recurring pattern, constraint, relationship, current goal, or desired behavior. Ask for a concrete example only when one is likely to come easily and naturally. Avoid abstract metrics, targets, tradeoffs, criteria, or lessons unless the user already volunteered that framing and can answer immediately.

When a question asks the user to recall, elaborate, or think of an example, usually add two or three lightweight optional cues introduced with wording such as "For example." Keep each cue to a few words, ground it in known context or broad categories, and keep every cue focused on the same single dimension. Omit cues for simple factual, yes/no, or already-easy questions, and whenever suggestions would lead the user toward an unsupported answer. Cues are prompts for memory only: never save one unless the user selects or confirms it.

Examples and answer starters must not introduce a second question. Never ask the user to define an internal term abstractly or broadly describe themselves.

A broad topic label without a reusable detail is a lead, not a durable fact. Ask the easiest follow-up that could reveal a useful preference, default, constraint, relationship, goal, or behavior; do not require an example. Never invent or append a concrete example, parenthetical, metric, target, or rationale that the user did not provide or that was not present in a cited source.

Consecutive questions may stay on the same topic when each one becomes easier and more concrete. If the user says they do not know or cannot answer, do not ask a harder version of the same question: offer simpler concrete choices or switch to the fallback thread.

Correction is not an onboarding objective. Mention that the user remains in control, but ask them to correct Knowledge only when an explicit user-authored statement or conflict inside Knowledge creates a high-impact contradiction that prevents a reliable write or payoff. Account or workspace metadata alone never triggers correction.

As the interview progresses:

1. Separate durable reusable knowledge from task-only context.
2. Resolve meaningful contradictions with one concise question when necessary.
3. Group consecutive details that belong together and save them at a natural checkpoint once they form a coherent reusable update. Do not write after every answer merely because each detail is eligible. Merge with existing topics instead of duplicating or scattering related facts.
4. After an actual successful save, briefly confirm what was added to Knowledge and why it can improve future help, with the labeled Knowledge link required by the mutation Skill. Do not propose a task yet.

Do not force a fixed topic order. Each next question must deepen the same useful thread or fill the next highest-value gap. If the user says "skip", ask the next question.

If the user says "stop", end the interview immediately and do not start Phase 3:

- If eligible knowledge was already saved during this interview, acknowledge it without creating any extra thin topics.
- If nothing eligible was shared, do not create a thin topic or claim anything was saved.

Clearly say the flow has stopped. If existing Knowledge can still support a useful action, mention that in one sentence without starting another flow.

## Phase 3: Demonstrate Write, Read, and Structure

Before suggesting a payoff, complete these mechanics internally:

1. Ensure the eligible interview knowledge has been written.
2. Read the changed topic again plus another relevant existing topic when available.
3. Ensure the latest successful update to each changed topic was acknowledged with its labeled Markdown Knowledge link; prepare any missing link now.

Before the action choice, use a short bold heading with the natural localized equivalent of "Next step: Knowledge in action". In no more than two short sentences, say that now relevant information is saved, you will show how it can be used in practice, then connect it to one or two lightweight example outputs. Frame them as quick starting examples of how Knowledge can help, not as the best, final, or most complete output. Do not explain your reasoning, inventory supporting facts, recap the interview, or write a long transition.

Do not repeat a save acknowledgement or Knowledge link already shown after the latest update. Optionally point out that opening a link reveals the wider Knowledge structure, but only when it fits inside the same two-sentence limit.

Never expose this as a fixed "Write / Read / Structure" checklist, add separators around it, repeat the saved information in consecutive sentences, inventory unchanged topics, or expose raw paths.

Run Phase 3 and the Phase 4 action proposal as one continuous assistant turn. Do not pause after the demonstration; pause only when the user needs to choose or confirm an action. Do not move to the payoff until the write, fresh read, and clickable changed-topic link are complete.

## Phase 4: Deliver a Quality-Gated Payoff

Before offering an action, silently verify every candidate:

1. It can use at least two specific pieces of Knowledge, or one decisive piece that materially changes the result.
2. Every required user input is available.
3. If it requires current external facts, an appropriate search or connector tool is available and will be used before answering.
4. The result will be materially more useful than a generic answer.
5. User-provided beliefs, goals, or positioning can be distinguished from independently verified facts.

Do not offer the action unless every check passes. If none passes, ask for the one missing detail only when the current path has a remaining open-question slot; a voice note or relevant file may answer it. The useful-Knowledge path allows up to four questions, while the guided empty-or-thin path never allows more than two open questions. If that path's limit is already reached, do not request more input or produce a weak result; briefly say that more context would be needed for a useful demonstration, then stop the onboarding.

Offer at most two lightweight actions grounded in the user's actual personal or professional context. Prefer one clear quick example over multiple uneven options, and present it humbly as a starting point that demonstrates how Knowledge can help.

- Do not promise future automation, monitoring, or reminders unless an available tool can perform it now.
- Do not invent missing inputs, facts, priorities, or examples to make an action possible. Gather required input during Phase 2 or do not offer that action.
- If offering two actions, use the top-level `ask_user_question` tool for the bounded choice and continue directly with the selected action when it returns. If one action is clearly best, offer only that one.
- Ask the user to choose or confirm an action unless they already requested a concrete task.
- Perform the chosen task. Do not merely describe what Vibe could do.
- Immediately before performing it, read the relevant Knowledge again unless it was already read in the current assistant turn.
- Use labeled Markdown Knowledge links for every topic that materially informs the result.
- Format the result for scanning. Use headings only as section titles; use bullets or a table for multiple labeled fields, and never collapse several fields into one heading.
- Keep this onboarding payoff compact: use at most five bullets or three short sections. Give a focused first version and leave secondary detail for a later request.

The result must be genuinely useful, not a trivia check, simple recall such as the user's name, superficial personalization, or a summary or reformatting of what was saved. Examples include preparing a real update, shaping a decision, planning a recurring activity, drafting in the user's preferred style, or applying known constraints to a recommendation. Adapt to the user; never copy these examples blindly.

If the user declines the proposed action, do not silently resume questioning or immediately pitch another task. Briefly acknowledge the choice and use the top-level `ask_user_question` tool to offer three clear paths: see one different way Knowledge could help, answer a few more questions to add context, or stop for now. Follow the selected path with a short explanation. If the user chooses a different way, offer one distinct action and perform it if they accept. If that action is also declined, do not keep cycling through proposals; offer only to answer more questions or stop.

## Knowledge Rules

The `knowledge-mutations` Skill owns the low-level file structure, topic routing, safety, mutation, and reporting rules. Follow it exactly.

- Include provenance for each saved fact: `[onboarding interview](metadata://onboarding/interview)`.
- Never treat examples in this Skill as facts about the user.

## Phase 5: Close the Interview and Offer Deeper Onboarding

Only after the user has accepted a proposed action and you have actually completed it, including an alternative chosen after a decline, visually separate the onboarding wrap-up from the task output and use this concise format:

1. Start a new paragraph with the first sentence in bold: "Your Knowledge now includes more context about {specific topic improved}." Follow it with: "I'll use it to make future answers more relevant, and you can try it now by asking me about {personalized suggestion}." Localize naturally, replace both placeholders with actual context from this interview, and never give a generic suggestion.
2. Give one sentence reminding the user that they can inspect, correct, or remove anything.
3. After a blank line, add a Markdown heading with the localized equivalent of "Final step: Build your Knowledge from your Connectors". Under it, say the natural localized equivalent of: "Once connected, I can use information from **Slack**, **Notion**, **Outlook**, **Gmail**, **Google Drive**, and **SharePoint** to consolidate broader work context in your Knowledge."

If `build-my-knowledge` or `build-knowledge-from-connectors` was already loaded earlier in this conversation, skip step 3, the Connectors question, and any reload of either: end after step 2, adding one sentence that the user can connect their work apps from Connectors anytime.

Otherwise, only after this summary, ask one clear structured choice with the top-level `ask_user_question` tool using the localized equivalent of: "Would you like to continue with Connectors, or finish for now?" Keep the tool's question and options in plain text without Markdown. If the user already clearly asked to continue with Connectors during this interview, do not ask again.

After the user chooses, do not repeat the summary, Connectors explanation, or question.

If the user accepts, immediately load `build-my-knowledge` with the top-level `skill` tool and follow it completely. It owns the rest of the flow and its completion message.

If the user declines, say the localized equivalent of: "No problem. I'll keep using what we added to make future answers more relevant. You can continue with Connectors anytime." Then stop.