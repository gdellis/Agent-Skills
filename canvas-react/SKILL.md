---
name: "canvas-react"
description: "Use this skill when the user asks you to build an application, a simulation, a game, or any UI that could be built with React. Covers the React canvas runtime contract, supported imports, targeted `edit` calls for existing React Canvases, and optional example files."
---
# React Canvas Files

This skill is intended to be used after the `canvas` skill has selected `react`. Do not reload `canvas` if it is already loaded.

Create or edit React Canvases at `/home/user/canvases/{name}/CANVAS.md` with `type: react` in the Canvas Frontmatter. The Canvas Body is the React source.

## Frontmatter

```md
---
name: interactive-dashboard
title: "Interactive Dashboard"
type: react
---

import React from "react";

export default function App() {
  return <h1>Interactive Dashboard</h1>;
}
```

The folder name must match `name`. Default Canvas directories contain only `CANVAS.md`; Spreadsheet Canvas directories contain exactly `CANVAS.md` plus the `.xlsx` workbook named by `entryPoint`. Do not delete or rename existing Canvas Files.

## Good Fits

- Components
- Dashboards
- Forms and workflows
- Small apps with local navigation
- Games and animated toys
- UI-heavy prototypes

## Output Contract

- Export exactly one default component.
- Do not require props for the top-level export.
- Keep everything in one Canvas File.
- Inline helper components, constants, and mock data in the same file.
- Use ordinary static ES imports at the top of the file.
- Reuse the same `name` on edits and preserve user changes unless asked to modify them.
- For existing React Canvas edits, `edit` is the default tool. Use it to patch imports, constants, component bodies, JSX subtrees, event handlers, styles, copy, and data arrays without rewriting unrelated code.
- Prefer several small, exact `edit` blocks over replacing the whole component. If you need to move code, patch the affected import/helper/component blocks separately.
- Full-file `write_file` edits are only for new Canvases, broad rewrites, invalid structure recovery, or explicit user requests.

## Runtime Contract

- The renderer bundles the Canvas Body with `esbuild-wasm` and mounts the default export.
- The component runs on the client and can use React state, effects, refs, timers, browser events, and normal JSX.
- Tailwind utility classes are generated from the Canvas Body, so `className` is the main styling path.
- Inline styles and inline SVG are also fine.
- Keep the Canvas self-contained. If you need a helper, write it inline instead of importing from app internals.
- Prefer embedded or mock data unless the user explicitly asked for a data-fetching example.
- Do not assume access to app hooks, backend clients, env vars, secrets, Next.js APIs, or repo internals.

## Package Imports

Only these package imports are available:

- `react`
- `recharts`
- `nucleo-sharp`
- `react-router-dom`
- `framer-motion`
- `@react-three/drei`
- `@react-three/fiber`
- `three`
- `uuid`

Import exact export names from every package above; importing a name a package does not export fails the build, which reports the closest valid names. For `nucleo-sharp` icons specifically, search `skills/canvas-react/references/nucleo-icons.txt` with `rg -i "<concept>"`; do not read the whole icon list into context.

## Local UI Imports

- Use `@/components/ui/<module>` subpaths only.
- Do not use the barrel import `@/components/ui`.
- Keep imports literal and simple. The runtime discovers local UI imports from the source text.
- Do not import `~/...`, relative app files, `next`, `trpc`, `@tanstack/react-query`, or any package not listed above.
- Safe local UI modules: `accordion`, `alert`, `alert-dialog`, `aspect-ratio`, `avatar`, `badge`, `button`, `calendar`, `card`, `carousel`, `checkbox`, `collapsible`, `command`, `context-menu`, `dialog`, `drawer`, `dropdown-menu`, `hover-card`, `input`, `label`, `menubar`, `navigation-menu`, `pagination`, `popover`, `progress`, `radio-group`, `resizable`, `scroll-area`, `select`, `separator`, `sheet`, `skeleton`, `slider`, `sonner`, `switch`, `table`, `tabs`, `textarea`, `toast`, `toaster`, `toggle`, `toggle-group`.
- If you need something outside that surface, build it inline.

## Good Defaults

- Use `MemoryRouter` for self-contained multi-view apps.
- Pair `recharts` with cards, tabs, selects, and badges for dashboards.
- Pair inputs, selects, checkboxes, switches, dialogs, sheets, and progress for forms and workflows.
- Use `framer-motion`, local state, timers, and pointer or keyboard events for toys and games.
- If the user asks for a polished UI, spend effort on spacing, hierarchy, icons, and motion rather than adding fake complexity.

## References

These files are optional examples. Read only one if you want a concrete pattern:

- `skills/canvas-react/references/component.md`
- `skills/canvas-react/references/dashboard.md`
- `skills/canvas-react/references/form-workflow.md`
- `skills/canvas-react/references/small-app.md`
- `skills/canvas-react/references/game.md`
- `skills/canvas-react/references/ui-heavy-prototype.md`