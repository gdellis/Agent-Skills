---
name: "Create a Skill from my Knowledge"
description: "Turn a repeatable workflow already supported by Personal Knowledge into a reusable Skill. Use when Knowledge contains enough stable process, preference, and output guidance to automate recurring work; do not create Skills from isolated facts or transient context."
---
# Create a Skill from my Knowledge

Find a genuinely repeatable workflow in the user's Personal Knowledge and turn it into a reusable Skill after the user confirms the proposal. A Skill must automate a recurring outcome; it must not merely restate, summarize, or package facts.

## Assess the Knowledge Base

Inventory the topic hierarchy, then read the topics most likely to contain workflows, recurring tasks, communication preferences, decision rules, templates, and quality standards.

Adapt to what exists:

- **Empty:** explain that there is not enough Knowledge to create a Skill and suggest "Set up my Knowledge" or "Build my Knowledge from Connectors".
- **Thin but actionable:** propose one Skill only when the available context defines a clear recurring trigger, outcome, and useful constraints. Ask for one missing critical detail when that would make the proposal viable.
- **Thin and non-actionable:** do not force a Skill. Offer to let the user describe one recurring task, or stop.
- **Large:** use topic descriptions to narrow the search, then read the strongest workflow candidates. Do not turn every project or preference into a Skill.
- **Interesting but non-reusable:** reject biography, trivia, isolated preferences, one-off events, temporary status, and facts with no repeatable action.
- **Conflicting or stale:** do not build on uncertain instructions. Name the affected topic and suggest sanitizing or clarifying it first.
- **Sensitive:** never use protected personal information, secrets, credentials, banking data, or other sensitive content as Skill instructions or proposal details. Suggest sanitizing the affected topic without repeating the content.

## Qualify candidates

A candidate is viable only when Knowledge provides enough evidence for most of these:

- a recurring trigger or situation;
- a concrete result the user repeatedly needs;
- stable steps, constraints, preferences, or decision rules;
- identifiable inputs or sources;
- a recognizable output format or quality bar; and
- meaningful time saved or consistency gained on future runs.

Prefer workflows such as recurring updates, meeting preparation, review checklists, decision briefs, or repeatable drafting processes only when the user's Knowledge actually supports them. Never invent a workflow from a topic label.

Check the user's existing Skills before proposing a new one. If a Skill already covers the workflow, offer to improve it instead of creating a duplicate.

## Propose, then create

Present at most three candidates, ranked by likely repeat frequency and value. For each, give:

- a short Skill name;
- when it would be used;
- what it would produce;
- which saved context makes it personalized; and
- any missing detail or freshness risk.

If no candidate clears the quality bar, say that plainly. Do not create a generic Skill just to complete the flow.

Use the top-level ask_user_question tool to let the user choose one candidate, provide a different recurring workflow, or stop. Before creating or updating anything, summarize the selected Skill's behavior and get explicit confirmation.

After confirmation, load skill-creator with the top-level skill tool and follow it completely. Carry forward the confirmed trigger, steps, inputs, output, quality bar, and boundaries.

Keep personal facts in Personal Knowledge rather than copying them into the Skill. The created Skill should read the relevant Knowledge when it runs, so future Knowledge updates remain effective. Include only stable workflow instructions in the Skill itself.

Use the response language established by the conversation. Never expose filesystem paths, filenames, tool names, or internal routing details.