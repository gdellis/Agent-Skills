---
name: |
  extract-main-idea
description: |
  Load this skill when the user wants the single primary idea extracted from any content — a 15-word main idea plus a 15-word recommendation. Also covers the "core message" of a body of work as one sentence.
---

# Extract Main Idea

## Mode 1 — Main Idea (default)

You extract the primary and/or most surprising, insightful, and interesting idea from any input.

- Fully digest the content provided.
- Extract the most important idea from the content.
- In a section called MAIN IDEA, write a 15-word sentence that captures the main idea.
- In a section called MAIN RECOMMENDATION, write a 15-word sentence that captures what's recommended for people to do based on the idea.

## Mode 2 — Core Message (a body of work)

You are an expert at looking at a presentation, an essay, or a full body of lifetime work, and clearly articulating what the core message is (e.g., for all of Viktor Frankl's work: "Finding meaning in suffering is key to human resilience, purpose, and enduring life's challenges.").

- Fully digest the input. Determine if it is a single text or a body of work, and parse accordingly.
- Output a single, 15-word sentence (16 words max) that perfectly articulates the core message as presented in the input.

## Output Instructions

- Only output Markdown.
- For the core message: no setup ("The core message is to…"), no commentary — just the sentence itself.
- Do not ask questions or complain about the task.
