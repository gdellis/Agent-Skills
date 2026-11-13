---
name: "userLibrary"
description: "User Library are user-curated collections of uploaded documents indexed for semantic search. Always load this skill before calling userLibrary tools."
---
# User Library

User Library are user-curated collections of uploaded documents (PDFs, slides, text files, etc.) indexed for semantic search. They are not files on disk; only the dedicated library tools can access them.

Before using library tools, call `search_tool_functions` with `mode: "best_match"` and a specific document-library capability query, then call `mode: "details"` for the exact returned function and follow its TypeScript declaration exactly.

## Resources and URIs
Library tools return **resources** identified by `doclib://` URIs:
- A library URI is `doclib://{library_id}`.
- A document URI is `doclib://{library_id}/{document_id}`.
- A **resource link** (`search_documents`, `list_documents`) points to a document you can open. It does not contain the full content.
- A **content chunk** (`search_documents`, `read_document`, `grep_document`) contains text from a document at a position.

## How to use the tools
- **search_documents**: semantic search. Returns content chunks plus one resource link per matching document. Pass `uri` to scope to a library or document.
- **read_document**: open a resource link's `uri` to read its content. This is how you open a link returned by search.
- **list_documents**: browse documents (one resource link each), optionally scoped by library `uri` or `name_contains`.
- **grep_document**: find an exact substring inside one document by its `uri`.

## Rules
- Prefer knowledge connectors (Notion, Google Drive, SharePoint) unless a library clearly matches the request; search them in parallel when unsure.
- When a library is selected, scope tool calls to it via the `uri` parameter.
- Never pass a bare library UUID as `uri`; use the full `doclib://{library_id}` URI.

## Citing documents
A document's name is always a link. Every time you write one, it is the text of a markdown link whose target is that document's own `doclib://{library_id}/{document_id}` URI, copied character for character out of the resource link:

`The rules are in [Handbook.pdf](doclib://1234/5678), which lists every step.`

A name left as plain text is not a citation: the reader cannot open it and the document is missing from the answer's sources. This holds for every mention, repeats included — unlike other sources, which are linked on first use only. A library is named the same way, with its own `doclib://{library_id}` URI.

Never assemble a link out of the ids yourself: a `/libraries/...` path you write is not a citation, and an id copied into a path is an id that can be copied wrong.