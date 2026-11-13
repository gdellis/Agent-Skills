# Data Visualization

Charts, graphs, and compact visual answers. Read this before rendering any chart with `tools.ui.renderComponent`.

## Renderer

Default to `tools.ui.renderComponent` for compact inline visual answers and charts. If the visualization needs a durable canvas, filters, layout, multiple charts, custom controls, richer interaction, or a polished standalone presentation, use a React canvas instead.

Never use `text/html` for data visualization unless the user explicitly asks for standalone HTML or wants to edit an existing HTML canvas.

The `tools.ui.renderComponent` function enables you to render components from the design system, including charts.

You must inspect the `renderComponent` type definition carefully before using it. Call `search_tool_functions` with `mode: "best_match"` and `query: "renderComponent"`, then call `mode: "details"` for the exact returned function and build the component to match the accepted schema.

## Core Flow

1. Gather the information needed for the chart.
2. Call `search_tool_functions` with `mode: "best_match"` and `query: "renderComponent"`, then call `mode: "details"` for the exact returned function and follow its types exactly.
3. Render graph components with the `tools.ui.renderComponent` function inside `run_typescript`. Use components like `Chart` or `PieChart`. Whenever the values carry a unit (%, a currency like $/€/£, ms, GB, km, ...), you MUST set the chart's `unit` field so it shows in tooltips and axis ticks.
4. After `tools.ui.renderComponent` succeeds, place the returned `component://` URI in your assistant message as a Markdown link where the chart belongs.
5. Directly below the chart link in the final assistant message, add the exact chart data as a Markdown table so users can read, sort, copy, and download the precise values.

## When To Use Inline UI

Use inline UI when it adds real clarity:

- Side-by-side comparisons with multiple meaningful values, such as loan or mortgage scenarios, pricing plans, product options, benchmarks, or before/after results.
- Trends, forecasts, time series, rankings, distributions, proportions, cohorts, metrics, or grouped category comparisons.
- Compact summaries where cards, badges, or a small chart make several related numbers easier to scan.
- User requests that explicitly ask to "show", "chart", "plot", "visualize", "diagram", or "compare".

Do not use inline UI when prose or a small markdown table is clearer:

- single-number answers or one-step calculations.
- Plain explanations, drafting text, writing code, or step-by-step instructions.
- Answers with only one meaningful value and no comparison, trend, structure, or visual grouping.
- Cases where the visual would merely repeat the text without adding insight.

## Always Include The Data Table Below The Chart

Whenever you render a chart, also place the exact chart data as a Markdown table directly below the chart link. In chat, Markdown tables render with built-in sorting, copy, and download, so users can read precise values and export them without extra work.

Do not put the chart data table inside `tools.ui.renderComponent`. Put the functional Markdown table only in the final assistant message directly below the `component://` chart link.

- Use the same numbers shown in the chart; do not round differently or omit rows.
- Put the chart first, then the table immediately below it.
- Give the table clear headers: the x-axis label, then one column per series.

## Choosing A Graph

Pick the chart from what the data should reveal (guidance from data-to-viz.com):

- Evolution or trend over an ordered, usually time-based x-axis -> line chart. Use it when the trend shape matters or there are many ordered points; the x-axis must be ordered. For just a few discrete periods you are comparing, a bar chart is fine.
- Comparison or ranking across categories -> bar chart. This is the safest default for category values, before/after, one or two measures, and rankings.
- Part-of-a-whole that sums to 100% across a few segments -> `PieChart`. In most other cases prefer a bar chart, which the eye reads more accurately.
- Axis roles never flip: `xAxis` is the category/label field and `yAxis` is the numeric measure(s), even for horizontal bars where the category appears on the vertical side. For a ranking like companies by market cap, use `xAxis: "Company", yAxis: ["marketCap"]`.
- Give a chart at most one title, set on the chart's `title` prop. Do not repeat that title in a surrounding `Markdown` heading or `Typography`, and do not echo it as a heading in your assistant message — one title per chart. Add a title only when context or a takeaway helps. For units, set the chart's `unit` field (e.g. `unit: "%"` or `unit: "$"`) so the unit shows in tooltips and axis ticks instead of the title.
- Add concise `Markdown`, `Badge`, or `Alert` components only when they clarify the chart.

## Chart Caveats

Apply these rules so a chart stays honest and easy to read:

- Bar charts keep a zero baseline so bar length stays proportional to value; do not set `yMin` to cut the axis. Rows render in the order you send them, so sort them yourself: order bars by value for rankings when the category has no natural order, and keep naturally ordered categories in their own order, running left to right from oldest to newest for time periods, first to last for stages, and smallest to largest for sizes. Use a horizontal bar chart when labels are long or there are many categories: `{ variant: "bar", orientation: "horizontal" }`. To compare several series, pass multiple `yAxis` keys for grouped bars side by side; the chart never stacks, which keeps each group comparable.
- Line charts need an ordered x-axis (usually time). Before rendering a time series, sort the chart rows chronologically from oldest to newest so the left side is the earliest point and the right side is the latest point. Parse the real date or period before sorting; do not sort display labels alphabetically. For rolling windows such as "last 12 months", start with the oldest period and end with the most recent period. They always start from a zero baseline so the trend is never visually exaggerated; do not set a non-zero `yMin` to magnify small differences. Avoid the "spaghetti" effect: keep to about 5 series or fewer, because more lines become unreadable. With more series, split into multiple charts or plot only the key ones.
- Pie charts are hard to read because the eye judges angles poorly. Use `PieChart` only for a part-to-whole split of a few segments (about 5 max) that sum to 100% and differ clearly in size. Never use a pie for trends, time, rankings, or negative values; when unsure, use a bar chart.
- Across every chart: keep the series and legend count small (reconsider past about 7); use color only to encode a series, never for decoration, and keep series colors consistent with any summary cards; and double-check that totals and proportions make sense before rendering.

## Summary Cards Above Charts

For statistical charts, add summary cards above the chart only when 2-3 headline numbers make the chart easier to scan.

- Use a `Row` of compact `StatisticCard` components before the chart.
- Use exactly 2 or 3 `StatisticCard` components; never create more than 3 summary cards.
- Each `StatisticCard` should contain a short title, a primary label/value pair, and optional `metrics` rows for secondary values.
- A card's `swatchColor` is a legend marker, so set it only when that exact color appears in the chart: the card must map to its own chart series (a distinct `yAxis` key). The chart colors series strictly by position, so assign card colors the same way and match the chart legend exactly: 1st series `brand`, 2nd `blue`, 3rd `green`, 4th `purple`, 5th `teal`, 6th `red`, 7th `pink`, 8th `yellow`, 9th `cyan`, 10th `bluedeep`. The card for the Nth series always uses the Nth color — never skip, reorder, or pick a color by preference. Use `gray` for a neutral reference value. If the chart plots the scenarios or categories as a single series (every bar shares one color), omit `swatchColor` on every card — a colored marker with no matching bar in the chart is misleading.
- For custom summary layouts, use `Typography` for prominent values and semantic deltas. Use `variant: "success"` for positive values and `variant: "destructive"` for negative values when that direction is good or bad in context.
- For scenario comparisons, use one `StatisticCard` per scenario, up to 3 scenarios. Give the cards distinct `swatchColor`s only when each scenario is its own chart series so the colors actually appear in the chart; when you compare a single metric with the scenarios as bars of one series (the common case for a one-metric ranking), leave the swatches off. For time series, choose the 2-3 most useful cards from the latest value, change over period, peak or low, or average.
- Do not add summary cards when there are fewer than 2 useful headline numbers.
- Do not add summary cards when the cards would merely repeat the axis labels.
- Do not duplicate the summary card values as a markdown table. This does not apply to the chart's data table, which you always include below the chart (see "Always Include The Data Table Below The Chart").

## Simple Example

Call `tools.ui.renderComponent` from `run_typescript` with a component definition like:

```ts
await tools.ui.renderComponent({
  name: "Column",
  props: {
    gap: "md",
    children: [
      {
        name: "Markdown",
        props: {
          content: "Here's the comparison for a €100,000 loan over 20 years:",
        },
      },
      {
        name: "Row",
        props: {
          gap: "md",
          children: [
            {
              name: "StatisticCard",
              props: {
                swatchColor: "brand",
                title: "3.5% interest",
                label: "Monthly payment",
                value: "€580",
                metrics: [
                  { label: "Total interest", value: "€39,190" },
                  { label: "Total repaid", value: "€139,190" },
                ],
              },
            },
            {
              name: "StatisticCard",
              props: {
                swatchColor: "blue",
                title: "7.5% interest",
                label: "Monthly payment",
                value: "€806",
                metrics: [
                  { label: "Total interest", value: "€93,342" },
                  { label: "Total repaid", value: "€193,342" },
                ],
              },
            },
          ],
        },
      },
      {
        name: "Chart",
        props: {
          title: "Loan cost comparison",
          unit: "€",
          variant: "bar",
          orientation: "horizontal",
          xAxis: "metric",
          yAxis: ["3.5% interest", "7.5% interest"],
          data: [
            {
              metric: "Monthly Payment",
              "3.5% interest": 579.96,
              "7.5% interest": 805.59,
            },
            {
              metric: "Total Interest",
              "3.5% interest": 39190.33,
              "7.5% interest": 93342.37,
            },
            {
              metric: "Total Repayment",
              "3.5% interest": 139190.33,
              "7.5% interest": 193342.37,
            },
          ],
        },
      },
    ],
  },
});
```

Then use the URI returned by the tool in your response:

```md
The loan comparison is here: [Loan cost comparison](component://abc12345)

| Metric | 3.5% interest | 7.5% interest |
| ------ | ------------- | ------------- |
| Monthly Payment | €579.96 | €805.59 |
| Total Interest | €39,190.33 | €93,342.37 |
| Total Repayment | €139,190.33 | €193,342.37 |
```

## Grouped Data

- When comparing groups over the same x-axis, build one row per x-axis value and one numeric property per group.
- Pass all group property names to `yAxis` as an array, for example `yAxis: ["desktop", "mobile", "tablet"]`.
- Use a line chart for grouped time series and a bar chart for grouped category comparisons.
- Keep group names short because they appear in the legend and tooltip.

## Guardrails

- Do not fabricate live or missing data. Use data from the conversation, provided files, or tool results.
- Compute any underlying numbers before rendering and pass exact values into the component.
- Keep chart labels short and human-readable. Category labels get about a third of the chart's width (roughly 20 characters when charts sit side by side in a `Row`) and are cut with "…" beyond that, so use a short name and keep the details for the data table.
- Always show units when the values have one, such as currency ($, €, £), %, ms, GB, or km. For every `Chart` or `PieChart` whose values carry a unit you MUST set the `unit` field — without it, tooltips and axis ticks show bare numbers. Components with no unit field still need the unit embedded as text: every `StatisticCard` value, label, and metric string, and the Markdown data table.
- The chart `unit` renders after the value (`7.9%`, `12ms`) or before it for currency symbols (`$1.2M`); do not also repeat the unit in the `title`. Axis ticks have little room and every tick repeats the `unit`, so a long unit makes ticks overlap or disappear: keep it to a symbol or short abbreviation. Counts of things (members, users, downloads, tokens) are not units: leave `unit` unset and say what is counted in the `title`, so the ticks show plain numbers.
- Send raw values: the chart shortens large numbers itself (`2K`, `1.5M`), so never pre-scale values or put a magnitude in the unit. Send `11400000`, not `11400` with `unit: "K members"`.
- Prefer a compact chart with clear axes over a dense chart that requires explanation.
- Do not hide important assumptions inside the chart. State them briefly in text.
- Do not nest `Card` components inside `Card` components.
- Do not repeat a chart's title. Set it once on the chart's `title` prop; never add a `Markdown`/`Typography` heading or an assistant-message heading that restates the same title.
- A summary card's `swatchColor` must be the exact color the chart legend shows for that series. Assign strictly by series position (1st `brand`, 2nd `blue`, 3rd `green`, ...); never give a card a color that differs from its series in the chart.
- Do not put chart data tables in `Markdown` components inside `tools.ui.renderComponent`; they lose chat table affordances and duplicate the final table.
- Always include the chart's data as a Markdown table below the chart link in the final assistant message so users can read exact values, sort, copy, and download them. If the data has no meaningful chart, use a Markdown table instead.