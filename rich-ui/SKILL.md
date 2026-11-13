---
name: "rich-ui"
description: "Always use this skill when an inline UI component or a visual answer would be clearer than a text-only answer, regardless of the user's language.\nAvailable components: data-visualization, weather, stock, checklist\nYOU MUST use it when the user message mentions a component name (e.g. \"weather\"), when the user explicitly asks for a checklist or to-do list or wants to tick items off, or when the answer contains data that reads better as visual structure: comparisons, tradeoffs, trends, rankings, proportions, time series, forecasts, metrics, benchmarks, pricing, share prices, loan or mortgage comparisons, or dashboards."
---
# Rich UI

Always use this skill when a compact inline UI component would provide a better understanding than a text-only answer.
## Available Components

- `data-visualization`: Charts, graphs, and compact visual answers for comparisons, trends, rankings, proportions, metrics, forecasts, and dashboards. It is the fallback for anything without a dedicated component below. You MUST read `/home/user/skills/rich-ui/data-visualization.md` before calling `tools.ui.renderComponent` for any chart.
- `Weather`: Current weather and short forecast for one location. Use for general weather questions. Before rendering it, read `/home/user/skills/rich-ui/weather.md`.
- `Stock`: Share price and price history for up to 4 listed companies. Use it for every share price answer, in place of a chart. Before rendering it, read `/home/user/skills/rich-ui/stock.md`.
- `Checklist`: interactive list of checkboxes for tasks, steps, criteria, or packing lists, with up to one level of nesting. Use it only when the user explicitly asks for a checklist or to-do list, or the conversation clearly establishes that they want to track completion by ticking items off; otherwise answer reference lists, such as ingredients, options, or explanatory steps, with plain Markdown bullets or numbered lists. Before rendering it, read `/home/user/skills/rich-ui/checklist.md`.

## Choosing A Component

- Prefer a dedicated component over `data-visualization` whenever one covers the subject. It already carries the right layout, units, and controls for that domain.
- Share prices go to `Stock`, never to a chart. `data-visualization` used to answer those; it no longer does. It stays the right choice for every other visual answer, including financial data that is not a share price, such as revenue, margins, or market share.
- Use `data-visualization` for everything else that needs a visual.

## Core Flow

1. Pick the relevant rich UI component from the list above.
2. Read that component's spec file before calling `tools.ui.renderComponent`.
3. Gather the data needed by the spec. Do not fabricate live data.
4. Call `search_tool_functions` with `mode: "best_match"` and `query: "renderComponent"`, then call `mode: "details"` for the exact returned function and follow its type definition.
5. Keep data gathering and rendering in separate tool calls. Any `run_typescript` call that fetches, searches, opens, browses, or gathers source data must not call `tools.ui.renderComponent`.
6. Call `tools.ui.renderComponent` exactly once, only after the component data is complete and final. Never render with placeholder, mock, draft, partial, example, or demonstration data.
7. Render the component with `tools.ui.renderComponent` inside a separate `run_typescript` call whose only external tool call is `tools.ui.renderComponent`.
8. After `tools.ui.renderComponent` succeeds, place the returned `component://` URI in your assistant message where the UI belongs. Never write, invent, or serialize your own `component://` URL. Only use the exact opaque URI returned by `tools.ui.renderComponent`.

## Guardrails

- Do not use rich UI just to decorate an answer. Use it when it makes information clearer.
- Keep any prose outside the rendered component short.