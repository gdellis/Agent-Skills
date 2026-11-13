# Stock

Use the `Stock` component for share price answers: one company's price, how a company has moved over a period, or a comparison of up to 4 companies.

## Stock Replaces Charts For Share Prices

Whenever the answer is about listed company share prices, use `Stock`.

- Always use `Stock` for share prices, price history, price comparisons between companies, and "how is X doing" questions about a listed company.
- Never render a `Chart` or `PieChart` of share prices. `Stock` already draws the price chart, and it adds the current price, the change over the selected period, the period switcher, and the price/percentage switcher.
- Do not add a Markdown table of the price series below a `Stock` component. That rule belongs to `data-visualization` charts; the price series is already readable in the widget.
- Keep using the `data-visualization` skill for every other visual answer, including other financial data that is not a share price: revenue, margins, market share, headcount, valuation multiples, or analyst estimates. If the answer mixes share price with other financial data, render `Stock` for the price and a separate chart for the rest.

## Writing The finance_search Query

The period lives in the query text, so the query has to ask for it — a bare `"AAPL"` gets you whatever window the provider picks by default.

Quote each part of the query. Quoted terms are much easier for the provider to parse, and the trailing labels are optional but help:

```
"AAPL":ORG "stock price":METRIC since "August 21, 1997":DATE
```

- Name the company or ticker, the metric, and the period, each in its own quotes.
- Write dates in full `"August 21, 1997"` rather than relative wording like "past three years".
- **Ask for the longest period you intend to show.** A daily series for the longest range contains every shorter one, so slice 1M, 3M, 6M and 1Y out of a 3Y response rather than searching again for each. Take each range off the end of the series, as described below — never by sampling the whole array at different densities.
- **Three years is the ceiling.** The provider truncates the export there, so asking for five years or "since IPO" returns three years all the same. Never label that series `5Y` or `Max`: the widget would claim a period it does not have. Show `3Y` instead, and say in your reply that three years is all the data available.

## One Call Per Company

**Plan the periods before you search, then call `finance_search` once per company.** One company is one call; a four-company comparison is four, one per ticker.

## Reading The Result

Three years of daily closes is around 180k characters, which is far over the inline limit, so the harness saves the result under `/home/user/tool-results/` and shows you only the first 20k characters. **That truncated view is not the data.** Read the file with `jq`.

The payload is `{ description, content }`, where `content.card_data` holds:

```
card_data.quote  = { price, currency, market_cap, as_of }
card_data.points = [ { timestamp, values: { absolute_data, percent_change_data } }, ... ]
```

`absolute_data` is the close in `quote.currency`; that is the number the component wants. Ignore `percent_change_data` — the widget computes percentages itself from each range's own first value.

`quote` sits at the top of the payload, inside the 20k preview, so read `market_cap`, `currency` and `as_of` straight off it. Only `points` needs `jq`. Format the market cap yourself: `4550319382200` becomes `"4.55T"`.

Five sandbox rules, each of which costs a wasted call when you learn it the hard way:

- **Never `read_file` a JSON file.** On a saved tool result it saves the payload again under a new path and shows you the same first 20k characters; on a file you wrote yourself it cuts off in the middle of the series. Every file is read in `bash`.
- **Always pass `jq` an absolute path.** A relative path fails with "Permission denied".
- **`run_typescript` has no filesystem.** `import fs` fails with "Not supported" and `require` with "require is not defined". So the render call cannot load your file: the finished JSON is pasted into it as a literal.
- **Write scratch files under `/home/user/`, never `/tmp`.** `/tmp` is outside the workspace, and reading back from it fails with "Path escapes workspace".
- **This `jq` is a cut-down build.** Run the filter below as written instead of reworking it, and read the list of missing features before you write any `jq` of your own.

Print lengths and endpoints while you work, never a whole series. The only series you print is the finished `ranges` file, once, at the end.

If you genuinely cannot read the series, answer in prose using `description`, which already carries the current price, the start price, and the period high and low. Do not render the component.

## Check The Payload Matches The Question

Search matches on words, so a query can come back with a different company or a different metric. Before you slice anything, confirm on `quote` and `description`:

- The company named is the one you asked for, not a similarly named listed entity.
- The series is a share price, not revenue, a ratio, or an analyst estimate.
- `currency` is that company's own trading currency.

If it does not match, answer in prose and do not render the component. Do not search again: one call per company is the whole budget, and a wrong match is not a missing one.

## What This jq Does Not Support

It accepts a single filter and a file: `jq -c 'FILTER' /absolute/path.json`. The `-c`, `-r` and `-s` flags work. Three differences from real `jq` matter, and all three fail silently, so a filter that looks right returns nulls:

- **`def f($x):` returns null.** Define helpers without parameters and pipe the value in: `def thin: . as $s | ...`.
- **`$s[.]` returns null.** Bind the index first: `range(0; $l; $n) | . as $i | $s[$i]`.
- **`map(...)` over an object returns null.** Iterate with `[ .[] | ... ]` instead. Over an array, `map` is fine.

## Slicing The Ranges

Run this once per company. It takes each range off the end of the series, one trading day per point, so every range ends on the newest close and they all agree on the current price by construction.

Edit one thing before running it: the ticker on the `values` line. Leave the rest alone — in particular, do not swap the trailing counts for dates. Counting back from the end needs no calendar arithmetic and cannot land on a market holiday.

```bash
jq -c '
def thin:
  . as $s
  | length as $l
  | if $l <= 260 then $s
    else (($l / 260) | ceil) as $n
      | [ range(0; $l; $n) | . as $i | $s[$i] ] as $k
      | (if $k[-1].t == $s[-1].t then $k else $k + [$s[-1]] end)
    end;
[ .content.card_data.points[] | {t: .timestamp, v: .values.absolute_data} ] as $p
| [ {label:"1M", n:22},
    {label:"3M", n:63},
    {label:"6M", n:126},
    {label:"1Y", n:252},
    {label:"3Y", n:756} ]
| map(.label as $lab
      | .n as $n
      | ($p[-$n:] | thin) as $s
      | { label:     $lab,
          startDate: $s[0].t,
          endDate:   $s[-1].t,
          values:    { AAPL: [ $s[].v ] } })
' /home/user/tool-results/<the saved file>.json > /home/user/ranges-AAPL.json
```

Those counts are trading days: 22 to the month, 63 to the quarter, 252 to the year, 756 to three years. A count longer than the series just takes the whole series. Drop the entries for periods you did not plan, and never add `{label:"5Y", ...}` or `{label:"Max", ...}` — the export stops at three years, so those labels can only misstate the period. `thin` only fires above 260 points, so it leaves the four shorter ranges untouched and exists for `3Y`, which it samples down to about 253 points.

Do not lower that 260. Thinning samples every Nth point, which throws away the period's high and low: thinned to 90 points, a year that peaked at 340.08 charts a high of 338.19, and the widget then disagrees with the `description` and with the shorter tabs.

For one company that file is already the answer, and the `cat` below is its own check — no separate verification call. Read it once as you paste it: every range must end on the same number, each must start on a different one, and none may be shorter than about 20 points.

For two or more companies, run the filter once per payload with a different ticker and output path, then merge. The merge clamps each range to its shortest series, because tickers on different exchanges keep different holidays and the component requires equal-length series:

```bash
jq -cs '
add as $all
| ["1M","3M","6M","1Y","3Y"]
| map(. as $lab
      | [ $all[] | select(.label == $lab) ] as $r
      | select(($r|length) > 0)
      | ([ $r[].values ] | add) as $v
      | ([ $v[] | length ] | min) as $m
      | { label:     $lab,
          startDate: $r[0].startDate,
          endDate:   $r[0].endDate,
          values:    ($v | with_entries(.value |= .[-$m:])) })
' /home/user/ranges-*.json > /home/user/ranges.json
```

The label list in the merge sets the tab order, so keep it shortest first. Check the merged file the same way, with `jq -c 'map({label, n: [.values[] | length], last: [.values[] | .[-1]]})'`: inside a range the lengths must match, and a ticker's last value must repeat across ranges.

Then `cat` the one finished file. Because `-c` keeps it on a single line, the whole thing is a couple of kilobytes: paste it into the render call as `ranges` exactly as printed. Copy the numbers, never round them, re-derive them, or type a series of your own.

The render call is that paste, plus the fields you read off `quote`:

```ts
await tools.ui.renderComponent({
  name: "Stock",
  props: {
    stocks: [{ ticker: "AAPL", name: "Apple", marketCap: "4.55T", currency: "USD" }],
    defaultRange: "3Y",
    asOf: "Aug 27, 2026 · 8:18 AM UTC",
    ranges: <the cat output, pasted unchanged>,
  },
});
```

`ranges` is a literal in that call. `run_typescript` has no filesystem, so there is no way to reach the file from inside it: `fs`, `require("fs")` and `import fs` all fail.

## Data Rules

- Gather fresh market data before rendering. Only use `tools.web_search.finance_search` for it. Discover it with `search_tool_functions` first if its type definition has not already been loaded, then call it with a quoted query as described above, such as `query: '"AAPL":ORG "stock price":METRIC since "August 21, 2023":DATE'`. Do not pass only the ticker, such as `query: "AAPL"`.
- Load both tool definitions in one `search_tool_functions` `details` call, `["web_search.finance_search", "ui.renderComponent"]`, rather than discovering `renderComponent` separately once the data is in hand. You already know you will need both.
- Do not use `tools.web_search.web_search`, `tools.web_search.open_url`, or browsing tools to gather prices for this component. If `finance_search` returned a payload, the series is in it — a truncated preview is a reading problem, not a missing-data problem, and the web will not fix it.
- Treat the returned `description` and `content` from `finance_search` as the source of truth. If it does not provide a current price and at least one usable price series, do not render the component.
- If the company is ambiguous, or a ticker exists on several exchanges, call the top-level `ask_user_question` tool before `finance_search`. Provide concrete proposals in the options, such as `options: ["Alphabet (GOOGL, Nasdaq)", "Alphabet (GOOG, Nasdaq)"]`.
- Keep data collection and rendering in separate tool calls. The data-gathering `run_typescript` call must return the gathered source data only and must not call `tools.ui.renderComponent`.
- Never fabricate prices, series, market caps, freshness, or sources. Do not fill gaps in a series with invented values; supply only the periods you actually have.
- Only pass `source` when `finance_search` explicitly provides a real source name. Never invent one such as "Finance API", "finance_search", or "web search".
- Call `tools.ui.renderComponent` exactly once, after every price series is gathered and final.

## Which Period To Show First

**When the user does not name a period, show three years.** Gather a three-year range and set `defaultRange` to its label, so the widget opens on it.

- Keep the shorter periods as tabs alongside it when you have them, ordered shortest first. `defaultRange` controls which one opens, not where it sits in the row.
- When the user does name a period ("today", "past week", "18 months"), gather that one and set `defaultRange` to it instead.
- When the user names a period longer than three years ("5 years", "since IPO"), `3Y` is the longest you can honestly show. Set `defaultRange` to it and say in your reply that three years is all the data available.
- If you could not gather a three-year range, set `defaultRange` to the longest period you did get.
- `defaultRange` takes the same fixed labels and must match one you actually supplied. The labels are never translated, whatever language you answer in.

## Currencies

Every number you pass for a company must be in that company's own trading currency. Never convert, and never label a price with a currency it is not quoted in: a KRW price shown as `$247,500.00` is simply wrong.

- Set `currency` on every company, always, even when they all share one. There is no default: omitting it fails the render.
- Use the company's real trading currency, for example `"USD"` for AAPL and `"KRW"` for Samsung 005930. Samsung quotes in won, not dollars.
- Do not convert prices into a common currency. You have no reliable exchange rate, and an invented rate in a price widget is worse than no comparison. `finance_search` is for prices, not FX; do not call it for a rate.
- When the currencies differ, the component compares the companies as percentage change and hides the price view, because prices in different currencies cannot share an axis. That is expected: still send the real prices per company, and the widget handles the rest.
- Say in your reply that the comparison is by percentage change when the companies trade in different currencies.

## Series Rules

These are enforced when the component renders, so a mistake here fails the call:

- Every ticker listed in `stocks` must appear in every range's `values`.
- Within one range, all series must have the same number of values, because they share an x-axis position.
- Give a period enough points to show its shape: about 20 at the least, and there is no upper limit — a year of daily closes belongs in the widget whole. A 3-month range needs the daily closes, not 3 monthly points. `1D` is the exception — intraday series are legitimately short.
- Every range must cover the period its `label` names. A `3M` range holds three months of closes, not the whole year thinned down to look shorter.
- **A ticker's last value must be identical in every range.** Every range ends at the present, so they all end at the same current price. That value is what the widget shows as the headline price — there is no separate price field — and the change and percentage are measured from each range's first value to it. Ranges that disagree on the latest price fail the render. The `jq` in "Slicing The Ranges" guarantees this by taking every range off the end of the series.

## Guardrails

- One `finance_search` call per company, for the whole answer. If you have already searched for a company, you have all the data you are going to get for it.
- Missing periods, short series, or a failed extraction are never a reason to search again.
- **Every number in `ranges` must come from `card_data.points`.** Pasting the `cat` output is how they get there. Never write a series from memory, never interpolate a smooth curve between two known prices, and never carry numbers over from a web page. An invented series looks convincing and is wrong: a real price history has drawdowns and spikes that a made-up one does not.
- If the data is unreadable or incomplete, answer in prose. Rendering the component with numbers you constructed is the worst possible outcome — worse than no widget.

## Component Example

Please read `tools.ui.renderComponent` to have the full component specification.

```ts
await tools.ui.renderComponent({
  name: "Stock",
  props: {
    stocks: [
      {
        ticker: "AAPL",
        name: "Apple",
        marketCap: "3.58T",
        currency: "USD",
      },
      {
        ticker: "MSFT",
        name: "Microsoft",
        marketCap: "3.26T",
        currency: "USD",
      },
    ],
    // The user did not ask for a period, so the widget opens on three years.
    defaultRange: "3Y",
    asOf: "Aug 18, 2026 · 4:00 PM ET · Close",
    source: "Nasdaq",
    labels: {
      marketCap: "Mkt cap",
      compared: "{count} stocks compared",
      yAxis: "Y axis",
      axisMin: "Min",
      axisZero: "Zero",
    },
    ranges: [
      {
        label: "1M",
        startDate: "2026-07-19T20:00:00Z",
        endDate: "2026-08-18T20:00:00Z",
        values: {
          AAPL: [230.1, 231.8, 229.4, 233.2, 234.9, 236.42],
          MSFT: [430.2, 428.9, 433.1, 435.6, 437.0, 438.76],
        },
      },
      {
        label: "1Y",
        startDate: "2025-08-18T20:00:00Z",
        endDate: "2026-08-18T20:00:00Z",
        values: {
          AAPL: [174.3, 188.0, 201.7, 215.4, 226.1, 236.42],
          MSFT: [385.4, 397.1, 410.8, 421.5, 430.2, 438.76],
        },
      },
      {
        label: "3Y",
        startDate: "2023-08-18T20:00:00Z",
        endDate: "2026-08-18T20:00:00Z",
        values: {
          AAPL: [121.6, 148.9, 174.3, 199.5, 218.7, 236.42],
          MSFT: [271.8, 318.4, 385.4, 402.9, 425.1, 438.76],
        },
      },
    ],
  },
});
```