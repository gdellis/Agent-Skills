# Weather

Use the `Weather` component for general weather answers that should show one compact widget, such as current weather, today's weather, this weekend's weather, or a short forecast for one location.

Do not use this component when the user asks to compare weather data, rank locations, analyze historical climate, plot weather trends, build a table, or visualize weather measurements. Read `/home/user/skills/rich-ui/data-visualization.md` for those requests.

## Data Rules

- Gather fresh weather data before rendering.
- If the requested place is city-only and could refer to multiple countries or regions, call the top-level `ask_user_question` tool before calling `weather_search` or rendering the component. Do not ask the clarification as normal assistant text. Provide concrete location proposals in the question options, such as `options: ["Edinburgh, Scotland", "Edinburgh, Indiana, US"]`.
- Only use `tools.web_search.weather_search` for current weather and short forecasts. Discover it with `search_tool_functions` first if its type definition has not already been loaded, then call it with a full English natural-language weather request that includes the location and time period, such as `query: "weather in Paris, France upcoming week"`. Do not pass only the location, such as `query: "Paris"`.
- If the user asks for upcoming-hour conditions, or if you need hourly weather data to answer accurately, call `tools.web_search.weather_search` with `includeHourlyData: true`, such as `weather_search({ query: "current weather in Paris, France", includeHourlyData: true })`.
- Do not use `tools.web_search.web_search`, `tools.web_search.open_url`, or browsing tools to gather weather data for this component.
- Treat the returned `description` and `content` from `weather_search` as the source of truth. If the source does not provide current conditions and exactly 7 forecast days, do not render the component.
- If `weather_search` is unavailable, empty, or incomplete, do not render the component.
- Before rendering, confirm that the location in the returned `description` is the place the user asked for, not another or default city. If it is not, do not render the component, and never show another place's weather under the requested place's name.
- Keep data collection and rendering in separate tool calls. The data-gathering `run_typescript` call must return the gathered source data only, and the only weather data-gathering tool call is `weather_search`; it must not call `tools.ui.renderComponent`.
- After the data-gathering tool call returns, inspect the returned source data and prepare final props. Then call a second `run_typescript` whose only external tool call is `tools.ui.renderComponent`.
- Gather exactly 7 forecast days because the `Weather` component schema requires exactly 7 `forecast` entries.
- Do not fabricate live weather, forecasts, sources, or freshness.
- Only pass `source` when the weather API result explicitly provides a real source name. Never invent a generic source such as "Weather API", "weather_search", "Tako", or "web search". If the API result does not provide a source name, omit `source`.
- Do not invent fallback values when source content is incomplete or hard to parse. If the opened source does not clearly provide a value, omit optional props or do not render.
- Call `tools.ui.renderComponent` exactly once, only after all current weather, metrics, and forecast data are gathered and finalized.
- Never call `tools.ui.renderComponent` with placeholder, mock, draft, partial, example, or demonstration weather data.
- All numeric temperatures must be passed in Celsius. The component handles Fahrenheit display conversion itself.
- Pass user-facing text in the user's active language whenever possible. This includes `currentDate`, `conditionLabel`, forecast day `label`, forecast `conditionLabel`, metric labels, and `labels`.

## Props

- `location`: short display name, such as "Paris, France".
- `currentDate`: optional forecast date label, such as "Tue, Jul 21".
- `source`: optional source name for the weather data. Only use a source name explicitly returned by the weather API result. Omit it if the data source is unknown.
- `labels`: optional localized labels for fixed component text: `feelsLike`, `high`, `low`, and `source`. Use the user's active language. For English, use `{ feelsLike: "Feels", high: "H", low: "L", source: "Source" }`.
- `currentWeather`: current weather condition data:
  - `condition`: one of `sunny`, `partlyCloudy`, `cloudy`, `rain`, `snow`, `storm`, `fog`, or `windy`.
  - `conditionLabel`: optional human label if the source uses a more precise phrase.
  - `temperature`, `feelsLike`, `high`, and `low`: numeric temperatures in Celsius.
  - `metrics`: up to 4 short label/value rows, with optional icons: `humidity`, `precipitation`, `wind`, `sunrise`, `sunset`, `temperature`, or `uv`.
- `forecast`: exactly 7 forecast days when available, each with `label`, `condition`, `conditionLabel`, `high`, `low`, and optional `precipitationChance`. Never pass fewer or more than 7 entries.

## Example

```ts
await tools.ui.renderComponent({
  name: "Weather",
  props: {
    location: "Paris, France",
    currentDate: "Tue, Jul 21",
    source: "AccuWeather",
    labels: {
      feelsLike: "Feels",
      high: "H",
      low: "L",
      source: "Source",
    },
    currentWeather: {
      condition: "partlyCloudy",
      conditionLabel: "Partly cloudy",
      temperature: 26,
      feelsLike: 27,
      high: 28,
      low: 18,
      metrics: [
        { label: "Humidity", value: "48%", icon: "humidity" },
        { label: "Wind", value: "12 km/h", icon: "wind" },
        { label: "Precip", value: "10%", icon: "precipitation" },
      ],
    },
    forecast: [
      {
        label: "Mon",
        condition: "partlyCloudy",
        conditionLabel: "Partly cloudy",
        high: 28,
        low: 18,
        precipitationChance: 10,
      },
      {
        label: "Tue",
        condition: "rain",
        conditionLabel: "Rain",
        high: 22,
        low: 16,
        precipitationChance: 65,
      },
      {
        label: "Wed",
        condition: "cloudy",
        conditionLabel: "Cloudy",
        high: 23,
        low: 17,
        precipitationChance: 20,
      },
      {
        label: "Thu",
        condition: "sunny",
        conditionLabel: "Sunny",
        high: 25,
        low: 18,
        precipitationChance: 5,
      },
      {
        label: "Fri",
        condition: "windy",
        conditionLabel: "Windy",
        high: 24,
        low: 17,
        precipitationChance: 15,
      },
      {
        label: "Sat",
        condition: "fog",
        conditionLabel: "Fog",
        high: 21,
        low: 16,
        precipitationChance: 15,
      },
      {
        label: "Sun",
        condition: "snow",
        conditionLabel: "Snow",
        high: 3,
        low: -2,
        precipitationChance: 65,
      },
    ],
  },
});
```