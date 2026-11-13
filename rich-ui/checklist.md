# Checklist

Use the `Checklist` component for an interactive list of checkboxes: tasks, steps, criteria, packing lists, or any ordered set of items the user can tick off. It renders one level of nesting, so a parent item can group its sub-steps.

Do not use it for reference answers that the user only reads, such as an ingredient list, a list of options, or explanatory steps (use plain `Markdown` bullets or numbered lists for those), for rankings or comparisons (use `data-visualization`), or to present choices where exactly one option should be picked (a checklist implies multiple, independent toggles).

Render it only when the user explicitly asks for a checklist, a to-do list, or items to tick off, or when the conversation clearly establishes that they want to track completion. Being list-shaped is not enough: an ingredient reference stays a plain bullet list, and steps that explain how something works stay numbered prose. An explicitly requested checklist, such as a shopping checklist, is always rendered as a `Checklist`.

## Props

- `title`: optional short title shown above the list.
- `items`: the list of items, in the order they should appear.
  - `text`: the item label.
  - `checked`: optional, whether the item starts checked. Omit it for an unchecked default.
  - `children`: optional, up to one level of nested items. Each child has its own `text` and optional `checked`. Children cannot nest further children.

## Writing The Items

- Keep each `text` short and scannable. One action per item.
- Order items by the order the user would work through them.
- Use `children` only when an item genuinely breaks into sub-steps. A flat list is clearer than a single-child parent.
- Set `checked: true` only for items that are already done. Do not pre-check items to "look complete" — the checklist reflects real state, not aspiration.
- Write item text in the user's active language.

## Guardrails

- Use the inline `Checklist` component only for an explicitly requested checklist or to-do list, or when the conversation clearly establishes completion tracking. Answer other lists with plain `Markdown` bullets or numbered lists. Do not create a Canvas for it.
- Do not fabricate progress. If you do not know which items are done, leave `checked` off.
- Keep the list focused. A checklist of more than about 20 top-level items is hard to read; split it or use a different layout.
- Call `tools.ui.renderComponent` exactly once, only after the list is final. Never render with placeholder or example items.
- The component is self-contained: do not add a `Markdown` list of the same items below it.