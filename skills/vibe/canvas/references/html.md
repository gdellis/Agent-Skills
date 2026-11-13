# HTML Canvases

Optional extra guidance for `text/html`.

- Use `text/html` only for standalone HTML deliverables, raw browser-platform demos, edits to an existing HTML canvas, or when the user explicitly asks for HTML.
- If the user wants charts, dashboards, data exploration, components, polished UI, or interaction that benefits from state and reusable controls, use a React canvas instead.
- Use a full HTML document by default for predictable rendering.
- The preview is rendered with `iframe srcDoc` and uses the raw HTML content.
- Inline `<style>` and inline `<script>` are fine.
- Write plain browser HTML, CSS, and JavaScript only. Do not use JSX, TypeScript, npm imports, or bundler assumptions.
- The canvas sandbox uses a restrictive CSP and cannot load external scripts from the internet. Do not use CDN URLs such as unpkg, jsDelivr, esm.sh, cdnjs, or remote `<script src="...">` tags.
- Keep the page self-contained. Prefer inline CSS, inline SVG, inline JavaScript, embedded data, and browser-native APIs. External assets, fonts, embeds, and network calls may also be blocked by CSP.
- Users will be able to download the HTML from the canvas UI.
- When editing an existing HTML Canvas, use `edit` for the specific
  element, style rule, script block, copy, or attribute that changed. Do not
  rewrite the whole HTML document for localized UI, CSS, or copy edits.

Use a full HTML document by default for predictable rendering:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Canvas HTML</title>
    <style>
      :root {
        font-family: Inter, system-ui, sans-serif;
        color: #111827;
        background: #f8fafc;
      }
    </style>
  </head>
  <body>
    <main id="app"></main>
    <script>
      const app = document.getElementById("app");
      app.innerHTML = "<h1>Hello</h1>";
    </script>
  </body>
</html>
```
