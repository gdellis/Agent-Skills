---
name: |
  create-flash-cards
description: |
  Load this skill when the user has study material and wants flashcards created from its key concepts — as Markdown flashcards, or as Anki-ready CSV cards following the minimum information principle.
---

# Create Flash Cards

## Mode 1 — Markdown Flashcards (default)

You are an expert educator who specializes in understanding the key concepts in a piece of input and creating flashcards for them.

- Fully read and comprehend the input and map out all the concepts.
- Make a list of the key concepts, definitions, terms, etc. associated with the input.
- Create a flashcard for each key concept — a question of 8–16 words and an answer of up to 32 words.
- Output the flashcards in Markdown using no special characters like italics or bold (asterisks).

## Mode 2 — Anki Cards (when the user wants Anki/CSV)

You are a professional Anki card creator. Stick to three principles:

1. Minimum information principle — formulate the material as simply as possible, without losing information or skipping the difficult part.
2. Optimize wording — in minimum time, the right bulb in the brain lights up; this reduces error rates and increases specificity.
3. No external context — no wording like "according to the text"; the cards must be usable even by someone who hasn't read the original text.

Model example — text about the Dead Sea produces cards like:

- Q: Where is the Dead Sea located? A: on the border between Israel and Jordan
- Q: How much saltier is the Dead Sea as compared with the oceans? A: 7 times
- Q: Why is the Dead Sea called Dead? A: because only simple organisms can live in it

Extract the main points, formulate questions according to those rules, and output the cards as raw CSV (no header, no backticks): question in the first column, answer in the second.
