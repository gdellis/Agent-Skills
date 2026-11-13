---
name: "Build my Knowledge"
description: "Internal connected-source Knowledge setup across Notion, Slack, Gmail, Google Drive, Outlook, and SharePoint. It owns connector setup and Knowledge enrichment; do not select it directly from a user request unless the user instructs so."
---
# Build my Knowledge

Build or enrich a personal Knowledge Base from the user's connected sources (Notion, Slack, Gmail, Google Drive, Outlook, and SharePoint) in three phases: discover -> extract five knowledge domains -> clean up. This branch works whether Knowledge is empty or already populated; preserve and extend useful existing topics.

Every connected source is both how you find things and how you read them. That makes the run bounded by your context window rather than by how much material exists, so everything below is about spending that budget well.

The result must be precise, useful, and user-centered. It should explain the user's own work, current focus, collaborators, workflows, and durable preferences. Broader team or project context is valuable only when it helps future answers understand the user's work; it must not become most of the Knowledge Base.

## User-Facing Style

- Match the language of the previous user-visible assistant message.
- Keep every user-facing message short, warm, and easy to understand.
- "Connectors" is a product feature name and may be used. Do not expose internal terms such as discovery, extraction, domains, checkpoints, context windows, connector status, IDs, scopes, tool names, or fallback branches.

## Prepare Connected Sources

Being loaded means the user has chosen to continue with Connectors. Do not ask them to choose again. This Skill owns every connector interaction from this point.

Call `tools.connectors.listAvailableConnectors({})` exactly once inside `run_typescript`. Store and reuse the result for the rest of the invocation. If it is unavailable or fails, follow **No Connected Source** below.

Consider only these six sources. One source can be listed under several record names, and every record naming a source is that same source:

- Notion -- `notion`
- Slack -- `slack`
- Google Mail -- `gmail`, `gmail_mcp`
- Outlook -- `outlook`, `outlook_mcp`
- Google Drive -- `google_drive`, `google_drive_mcp`
- SharePoint -- `sharepoint`, `sharepoint_mcp`

Ignore every name not on that list, including near-misses like `notion-internal` that read as a listed name with something appended. A source is ready when any of its records is `connected`. Send at most one ID per source to the connector card and never two records of the same source: prefer a `connected` record, otherwise the record whose name matches the namespace the Step 1 census calls for that source, so authenticating it enables the tools the run will actually use. Preserve the exact returned IDs and never send duplicates or unrelated connectors to the connector card.

If every considered connector is already ready, continue to the start sequence below.

If any missing connector is available with `authentication_required`, call `tools.ui.ask_enable_connector({ connectorIds })` exactly once inside `run_typescript` with the IDs of those available, missing connectors; a missing connector that is not available at all is simply absent and is never sent to the card. In the same turn, emit one short visible sentence that names those connectors in bold and frames them as optional, for example "I can also read **Google Mail**, **Google Drive**, and **SharePoint** -- consider enabling these if you use them." Name only the ones on the card, never the ones already connected, and do not explain what each is for. After the card, combine already-ready connectors with `connectedConnectorIds`; never treat `deniedConnectorIds` as ready.

Continue with whichever of the six are now ready, even if the user skips, declines, or fails to connect some of them. When no connector of the six is ready, do not start enrichment; follow **No Connected Source** below. Do not retry the card or ask the user to locate connector IDs. A connector that is not ready is absent: its tools error, and the census treats that error as absence.

### No Connected Source

Never end the flow only because no source could be used. First check whether `interview-my-knowledge` was already loaded earlier in this conversation.

- If it was, in one short sentence say briefly why no source could be used and that the user can connect their sources from Connectors anytime, then finish. Do not announce more questions.
- Otherwise, in one short sentence say briefly why (Connectors cannot be used right now, none of the supported work apps is connected, or the connected sources did not provide enough useful information) and that you will start with a few quick questions instead. Then immediately load `interview-my-knowledge` with the top-level `skill` tool and follow it completely. It owns the rest of the flow and its completion message.

### Start the Build

Once at least one of the six connectors is ready, follow this sequence exactly:

1. For a new Build invocation, delete any existing `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md` checkpoint and start fresh. Keep it only when resuming the same interrupted invocation.
2. If `knowledge-mutations` is not already loaded in the current invocation, load and follow it. Never load it twice.
3. Emit one short visible message: "Building your Knowledge Base takes a few minutes. Check back shortly." In another language, provide a faithful, natural translation.

4. For a new Build invocation, in the same assistant turn immediately start Phase 1 by issuing the six census calls together in parallel: `tools.notion.notion_fetch({ id: "self" })`, `tools.slack.read_user_profile({ response_format: "detailed" })`, `tools.outlook.who_am_i({})`, `tools.gmail.list_labels({})`, `tools.google_drive_mcp.list_recent_files({ order_by: "lastModifiedByMe" })`, and `tools.sharepoint_mcp.find_site({})`. For a resumed invocation, read the existing checkpoint and continue from the next incomplete domain; do not call the census tools or repeat Phase 1. The visible message is a progress update, not a completion message. Do not stop after it, return control to the user, or treat the work as a background task.

Do not make any profile, search, read, or fetch call before the visible message. If one of the census calls fails, keep the successful result and retry only the failed call; a connector whose call still errors is absent for this run.

## Critical rules

**At least one connected source is required to start extraction.** Do not enter Phase 1 until at least one of the six connectors is ready. Once extraction has started, degrade gracefully if a ready connector later fails. Which connectors are actually usable is settled only by the Step 1 census -- never by a status panel, a connector listing, or a neighbouring connector's auth state. Notion is the richest discovery seed but never a requirement; the flow must work for a user with no Notion.

**A connector that answered the census gets examined.** Every connector present at Step 1 ends Phase 1 with hits, or with a zero that a query actually produced. Container names -- sites, labels, folders -- tell you what to ask for, never what is there; ruling a source out because its containers look unpromising is a guess, and reporting it as empty is worse than not having run it. Stop only when discovery returns nothing from every connector the census found, and never while a present connector is still unexamined.

**Context is the budget.** You have room for roughly 10-15 full `notion.notion_fetch` calls across the entire run. Mine `notion.notion_search` highlights first -- most facts can be extracted from highlights alone with no fetch. When you do fetch, mine the page completely for all five domains in that pass and route each fact into the appropriate existing or new topic immediately. Every fetch spent on a thin page is a fact you will not get from a dense one.

**Identity matching before attributing any fact to a person.** A first-name-only mention is never sufficient. Require a full name, or a user ID, email, or Slack handle from page metadata or message authorship. Compare identifiers in full -- user IDs share long prefixes. If you cannot confirm who is meant, write the fact as an unattributed observation or skip it.

**Channels only.** Never read or use direct messages or group DMs. Public and private channels are in scope; direct conversations are not. Drop a hit marked `is_im` or `is_mpim`, or whose conversation ID begins with `D`, before it reaches the source list.

**Graceful degradation.** If any connector fails after this branch starts -- Slack scopes, a Notion timeout, an Outlook auth mismatch -- continue with what you have. If no source yields usable material, clean up the temporary checkpoint, then follow **No Connected Source** below.

## How to pull data

### Two search modes

Getting this wrong is the fastest way to burn the run.

| Mode | Where | Purpose | Settings |
| --- | --- | --- | --- |
| Discovery | Phase 1 | Build a candidate list: IDs and titles | `page_size: 25`, `max_highlight_length: 200`, no Slack context |
| Domain | Phase 2 | Harvest evidence | `max_highlight_length: 500` |

A discovery pass returns 25 hits and most will be calendar entries and noise. At 500 characters each that is thousands of wasted tokens before you have read a single fact. Keep discovery cheap; spend on the topic passes.

**Search per domain, not per document.** Do not build a list of 40 pages and then read them. Run a handful of targeted searches for each domain and harvest the highlights. Search is cheap; fetch is not.

Fetch only when all three hold:

1. The highlights show the page is dense on a topic you still need.
2. The snippet is truncated mid-fact.
3. You have fetch budget left.

Conditions 1 and 2 assume a preview. A Drive candidate never has one, and a SharePoint candidate found by `browse` rather than `search` does not either. For those, the Step 5c ranking -- title, recency, mime type -- substitutes for the first two conditions; the budget condition still applies. Without this a snippet-less candidate could never be read at all, which for Drive would mean discovering files and never opening one.

**Source priority.** Before extracting, build a small shortlist per domain. Rank sources highest when they are current, user-authored or user-owned, and directly explain the user's active work. Use current requirement docs, roadmaps, project briefs, strategy, research/design, operating, policy/process, customer/account, and project/task-tracker documents to add context after identifying the user's slice. Use rolling 1:1s, meeting logs, transcripts, and calendar events only to discover leads or names unless a dated section directly supports a durable historical fact.

**Adaptive recency.** Start with current and recent sources, but do not overfit to the last few days. If that window is thin or repetitive, broaden to older durable sources. Recency is strict for active focus, roles, ownership, project status, deadlines, headcount, account/case/deal/deployment state, and next steps. Older sources may support about-me context, terminology, completed work, historical decisions, stable relationships, and long-running responsibilities when dated.

**Slack: search, do not read channels.** `slack.read_channel` dumps recent messages regardless of relevance. `slack.search_public_and_private` with a targeted query returns matched messages with surrounding context. Reserve `slack.read_thread` for a thread whose search hit is clearly the opening of a substantive discussion.

**Gmail: search threads, never sweep the mailbox.** `gmail.search_threads` returns matched threads with snippets and no bodies; that is the discovery call. Reserve `gmail.get_thread` for a thread whose snippet is clearly about the user's work, and expect to spend few of them. `gmail.list_labels` is a scoping hint like a channel list, never a source. Ignore drafts: unsent text is not evidence of anything.

**Outlook filters, it does not parse a query language.** `outlook.search_outlook` takes named parameters, so there is no operator string to construct and none of Gmail's `category:` exclusions exist. Noise control comes from folders instead: `outlook.list_mail_folders` first, then scope the search. Results are message-level and sorted most recent first, so the first page is genuinely the newest, and `outlook.open_outlook_email` returns one body rather than a whole thread.

**Drive search returns no text.** `google_drive_mcp.search_files` gives titles, mime types, owners, and timestamps -- no highlights, no snippets. Every Drive fact therefore costs a `google_drive_mcp.read_file_content`, which is the one thing the fetch budget exists to ration. Treat a Drive read like a `notion_fetch`: it comes out of the same 10-15, and a read spent on a deck of screenshots is a fact you will not get from a doc. Never `google_drive_mcp.download_file_content`; it returns base64, and `read_file_content` already gives you prose with comments attached.

**SharePoint search returns snippets, and its index lags.** `search` is the pass that scales: one call crosses every library the connection can see and comes back with a snippet you can judge before spending a read. What it does not see is the last hour. The index is a crawl, so a file is visible to `browse` immediately and to `search` between fifteen minutes and an hour later. That gives zero a third meaning found nowhere else: not a bad query, not an empty corpus, but a document that exists and has not been crawled yet. `browse` is the check on that, and since a zero here means no on-topic snippet rather than no results, never report SharePoint as empty without a `browse` that agrees.

**Mail has no channels-versus-DMs line to hide behind.** Every thread is direct correspondence, so the boundary is the fact, not the container. Write facts about the user's own work: what they own, decided, shipped, agreed. Never write a fact about someone else's private situation, never quote a third party's personal content, and never mine a thread that is not about work. If a fact would embarrass the person who wrote the mail, it does not go in the file.

**Never fetch the same page twice.** Record each fetch under `# Run` in `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md`.

**Topic files are append-and-extend, not one-shot.** A write means "create this topic, or add to it if it exists." Before appending, read the file so you place the fact under the right section and do not duplicate something already there. That makes the run resumable and lets later runs extend the same knowledge base rather than overwrite it.

**Stop searching a domain when two consecutive queries return only hits you have already seen.** Repeated hits are the only saturation signal you get. Trust it.

## Phase 1 - Discover

### Step 1: About me and the connector census (already collected in the start sequence)

```
tools.notion.notion_fetch({ id: "self" })
-> { user: { id: "a71f...", name: "Shepherd McFlockface" }, workspace: { ... } }

tools.slack.read_user_profile({ response_format: "detailed" })
-> { user_id: "U0BKR...", name: "Shepherd McFlockface", tz: "Europe/Paris", ... }

tools.outlook.who_am_i({})
-> { displayName: "Shepherd McFlockface", mail: "shep@...", userPrincipalName: "..." }

tools.gmail.list_labels({})
-> user labels, which double as domain names

tools.google_drive_mcp.list_recent_files({ order_by: "lastModifiedByMe" })
-> the user's own recent work, titles only

tools.sharepoint_mcp.find_site({})
-> the sites this connection can reach; their names are domain vocabulary
```

These six calls are how you find out which connectors you have. A connector is present if its call answers and absent if it errors; that is the only admissible evidence. Never infer availability from a status panel, a connector listing, or a neighbouring connector's auth state: a calendar connector needing auth says nothing about a mail connector, and silently dropping a source is the one failure this run cannot detect later. Tool paths below are written `tools.<connector>.<function>`; look up each connector's exact function names with the tool-discovery search before calling -- the Drive group is `google_drive_mcp`, while Google Mail and Outlook are `gmail` and `outlook`, and SharePoint is `sharepoint_mcp` (`sharepoint` on tenants that expose the older group).

Extract `user_name`, `notion_user_id`, `slack_user_id`, and the user's own addresses into an address set. These drive every subsequent query. Do not call the census tools again and never ask the user for these IDs. One person often holds several addresses -- work, personal Outlook, personal Gmail -- so a match on any member identifies the user, and a mismatch alone never proves two accounts are different people.

Only three calls feed the set: the email from `notion.notion_fetch({ id: "self" })`, the Slack profile email, and `mail` / `userPrincipalName` from `outlook.who_am_i`. The `owner` on every `google_drive_mcp.list_recent_files` result is a file owner, usually a colleague who shared something, and never enters it. SharePoint returns no identity at all -- no address, no handle -- so it proves presence and nothing more. The set extends on one test only -- a self-forward linking a new address to a member -- never from a `to`/`cc` list, a shared mailbox, or a lookalike name. When in doubt leave it out: a missing address costs a few facts, a wrong one attributes a colleague's work to the user.

Ask Slack for the full profile, not `concise`. Concise returns the handle and the email but not `user_id`, which every authorship query needs. The same choice governs search: `slack.search_public_and_private` must also request `response_format: "detailed"`, because concise search results carry only channel names and dates, without the channel IDs, message timestamps, and permalinks that citations need.

The last three census calls cost nothing, so they run here rather than waiting for Steps 5b, 5c, and 5e. They are also the fallback domain seed: if Notion is absent or thin, Drive titles, Gmail labels, and SharePoint site names are where Step 3's keywords come from instead.

### Step 2: Three Notion search passes

| Pass | Query | Filters | What it finds |
| --- | --- | --- | --- |
| Name | `"{user_name}"` | none | Pages that mention you: 1:1s, weeklies, planning docs |
| Author | `"{first_name}"` | none | Pages where you are cited as author or contributor. Notion has no `author:` operator; a query like `author:kris` is matched as literal text and finds nothing |
| Domain (2-4 calls) | keywords inferred from the name-pass highlights | `filters: { created_by_user_ids: [notion_user_id] }` | Pages you created in your work areas |

Name and Author calls:

```
notion.notion_search(
  query: <see table>,
  query_type: "internal",
  page_size: 25,
  max_highlight_length: 200
)
```

Domain calls only:

```
notion.notion_search(
  query: <domain keyword>,
  query_type: "internal",
  page_size: 25,
  max_highlight_length: 200,
  filters: { created_by_user_ids: [notion_user_id] }
)
```

You are building a candidate list here, not reading evidence. Expect most hits to be calendar events and other noise; that is fine at 200 characters and expensive at 500. The higher setting belongs in Phase 2.

### Step 3: Infer domains for the domain pass

If the user does not specify their domains, extract them from the name-pass highlights and from the Drive titles, Gmail labels, and SharePoint site names the Step 1 census already returned. Notion is the richest seed but not a required one: if it is absent or thin, the other three carry the step on their own. Look for team names, project names, and recurring keywords. If the highlights contain "Shepherd McFlockface Eng (Sheep Platform -- agentic herding)", the domain queries become "agentic herding RFC" and "sheep toolkit retrieval".

Run 2-4 domain queries maximum. More returns diminishing results due to overlap.

### Step 4: Filter and deduplicate

From all results, keep only entries where `type == "page"`. Drop:

- calendar events
- issue-tracker items
- external drive files
- `is_archived == true`

Deduplicate by full page ID, never a prefix.

### Step 5: Slack channels

```
slack.search_channels(keywords=["<domain keyword>"], natural_language_query="<domain keyword>", limit=20)
slack.search_public_and_private(keywords=["{user_name}", "<domain keyword>"], natural_language_query="<domain keyword>", limit=20, include_context=false, response_format="detailed")
```

Search by topic, not author: channels are named after work, not people. Do not use `from:me`; it mostly surfaces direct messages, which are out of scope. `include_context=false` matters. With context on, this call returns surrounding messages for every hit and becomes the largest thing in the run. Request the detailed format: concise search results drop the channel IDs, message timestamps, and permalinks that citations need. You are after channel IDs and thread timestamps here, not conversation. Read threads later in Phase 2 only where a domain search points at one.

Extract channel IDs and keep individual thread timestamps where a hit looks substantive. A thread is a source; a channel is only a discovery hint. Cite facts to threads, not bare channel IDs. If Slack fails after this branch starts, continue with the other sources.

Typical discovery output: 30-50 Notion pages, 5-15 Slack channels, 5-15 Gmail threads, 5-20 Drive files, 5-15 Outlook messages, and 5-15 SharePoint documents.

### Step 5b: Gmail threads

`gmail.search_threads` takes Gmail's search-operator syntax, not natural language. Two passes, both bounded:

```
from:me newer_than:6m (<domain keyword> OR <domain keyword>)

newer_than:6m (subject:<domain keyword> OR subject:<domain keyword>) -category:promotions -category:social -category:updates -category:forums
```

Authorship first: `from:me` finds what the user actually wrote, which is the highest-signal mail there is and the cheapest query to run. Mail is the exception to Step 5's `from:me` ban: every message is direct correspondence rather than a channel post, so the authored half is in scope here and the mail-privacy rule sets the boundary. Then subject, never bare content: a free-text term matches message bodies and returns the mailbox's automated traffic -- build notifications, ticket updates, calendar spam. Constrain to `subject:` and exclude the notification categories. If a known sender dominates the noise, add `-from:` for it and move on; do not tune a query more than twice.

Then the received side, which is where most of the signal lives. `from:me` finds only what the user sent; things that happen to the user -- contracts for signature, bookings, decisions taken elsewhere -- never appear in it:

```
to:me newer_than:6m (subject:<domain keyword> OR subject:<domain keyword>) -category:promotions -category:social -category:updates -category:forums
```

Bound the window: `newer_than:6m` by default. A mailbox spans years and this flow wants current work; older mail is only worth reaching for a durable historical fact you already have reason to believe exists. In a query string, the `label:` operator takes the label name, not the label ID; an ID returns zero results from a full label and makes it look empty.

Results carry subject, sender, recipients, date, snippet, and label IDs -- no bodies. Keep the `threadId` of anything whose snippet reads like a decision, a commitment, or a status, and spend `gmail.get_thread` on it in Phase 2 only where a domain search points there. Threads come back 20 at a time with a page token; take the first page and stop unless the estimated match count says the tail is worth a second call. If Gmail fails, continue with the other sources. Typical output: 5-15 threads worth keeping out of far more returned.

### Step 5c: Google Drive files

`google_drive_mcp.list_recent_files` already ran in the census; work from those results rather than calling it again. One structured search per domain from here. The syntax is Drive's own, and `owner = 'me'` is the authorship filter -- the same move as `created_by_user_ids` in Notion and `from:me` in Gmail:

```
owner = 'me' and modifiedTime > '<6mo ago, RFC 3339, e.g. 2026-03-01T00:00:00Z>' and (title contains '<domain keyword>' or fullText contains '<domain keyword>')
```

That filter needs a full RFC 3339 timestamp. A bare `YYYY-MM-DD` -- the form Step 5d uses for Outlook -- is rejected and returns nothing, which is not the same thing as an empty Drive.

Run both halves, bounded. `owner = 'me'` finds what the user made; `sharedWithMe = true` finds what arrived. The second is noisy unbounded -- it is every deck anyone ever shared -- so always pair it with recency and a keyword:

```
sharedWithMe = true and modifiedTime > '<6mo ago, RFC 3339, e.g. 2026-03-01T00:00:00Z>' and (title contains '<domain keyword>' or fullText contains '<domain keyword>')
```

Skip neither. A contract sent for signature, a review of the user's work, a document drafted by outside counsel -- all are shared, none are owned, and an owner-only pass cannot see any of them.

Titles are the only signal at this stage: rank on title, recency, and mime type, and prefer documents over spreadsheets and presentations over images. A file whose title does not say what it is about is usually not worth a read. Keep the `fileId` of anything whose title reads like a plan, a decision record, or a spec; spend `google_drive_mcp.read_file_content` on it in Phase 2, sparingly, and take the comments with it -- Drive comments are where the disagreement lives. If Drive fails, continue with the other sources.

### Step 5d: Outlook messages

```
outlook.list_mail_folders({})

outlook.search_outlook(query="<domain keyword>", folder_id="inbox", after="<6mo ago, YYYY-MM-DD>")

outlook.search_outlook(query="<domain keyword>", folder_id="sentitems", after="<6mo ago, YYYY-MM-DD>")
```

`outlook.search_outlook` takes named parameters -- `query`, `folder_id`, `after` / `before` as ISO `YYYY-MM-DD` dates, `limit`, `message_from`, `message_to`, `has_attachments`, `mailbox` -- not a query language, so there is no operator string to construct and none of Gmail's `category:` exclusions exist. Noise control comes from folders instead: list them once, then scope each search. `message_from` and `message_to` take one exact address -- not a name, not a bare domain -- so they are only usable for a counterparty whose address a discovery result already showed you; where you have no address, put the terms in `query` and scope by folder instead. Do not guess an address; a wrong one returns nothing and reads like an absence.

Both halves, by folder. `sentitems` is what the user wrote; `inbox` is what arrived. Outlook is the one connector where that split is a parameter rather than a trick, so use it -- and expect the inbox side to carry more, because in most organizations the things that matter arrive rather than get sent.

Snippets include a body preview, so judge from the result list and spend `outlook.open_outlook_email` only where the preview reads like a decision, a commitment, or a status -- and expect it to add little. Transactional mail is boilerplate around an attachment, and attachments are not extracted, so the read often returns less than the snippet did; where Drive's read is the only way to get anything, Outlook's is frequently the cheapest thing to skip. `message_id` is opaque -- copy it whole. Shared mailboxes are out of scope for a personal Knowledge Base; never pass `mailbox`. If Outlook fails, continue with the other sources.

### Step 5e: SharePoint documents

```
sharepoint_mcp.find_site()                                        # once, in Step 1
sharepoint_mcp.search({ query: "<domain keyword>" })               # primary; tenant-wide, snippets
sharepoint_mcp.list_libraries({ site_id: <site> })                 # only when search is not enough
sharepoint_mcp.browse({ drive_id: <library>, folder_id: "root" })  # confirms a zero, reaches the uncrawled
sharepoint_mcp.get_info_by_url({ url: <a link you already have> }) # skips the walk entirely
```

**Search first, browse to confirm.** Lead with one `search` per domain keyword: it covers every library at once and returns snippets, so you can judge a hit without reading it. Query it with the domain keyword alone -- plain keywords, not Drive's `owner = 'me'` DSL. Drop to `list_libraries` -> `browse` when a domain you have reason to believe is covered comes back with no on-topic snippet -- that, not a zero count, is what a SharePoint miss looks like -- or when the user has said something was added in the last hour, which the index will not show yet and no result can reveal. Browsing is a folder walk with no snippets and filenames that are often worthless; it does not scale past a library or two.

**A link you already have is a shortcut.** When the user supplies a SharePoint URL, or one turns up in mail or Slack, `get_info_by_url` resolves it straight to the item -- no `find_site`, no `list_libraries`, no walk.

**There is no authored half.** No author filter exists at query or response level -- `browse` returns name, type, size, and modified time, nothing more. The closest thing to authorship is the library itself: a library the user created or works out of is their work. Treat that as weak evidence and never attribute a document to a person from its location alone.

**The received half is site-shaped, not item-shaped.** `find_site` returns the sites this connection can reach, which is permission-as-visibility -- the equivalent of `sharedWithMe` one level of granularity coarser. There is no per-item equivalent, and the list is not exhaustive: sites nest, so a site missing from `find_site` may still exist as a subsite of one that is there. `list_subsites` is the only way to see them.

**`search` has no relevance floor.** With nothing to match it returns the tenant's best-ranked documents rather than zero -- a query for an absent project came back with ten annual reports at ranks 0-9. The count means nothing; judge every hit on its snippet. On a real tenant the filler is plausible, so it will not announce itself.

**No date filter, and `search` returns no date.** Its hits carry null `date`, `title` and `description` -- the filename in the snippet is all you get. Only `browse` and `get_info` return `last_modified_date_time`, so a window can be enforced on those two and never on `search`.

**`search` is tenant-wide.** It crosses every library the connection can see, which is the point -- it reaches sites you would never have thought to open. The `url` on each hit is what tells you where it came from, so read it before attributing a document to a site.

Snippets come back with `search` results, so unlike Drive you can judge before reading. The read itself is not cheap -- a paper-sized PDF returns tens of thousands of characters -- so `sharepoint_mcp.read` draws on the same 10-15 budget as a `notion_fetch`. Never `read_binary_file`: like Drive's `download_file_content` it hands back bytes you cannot use, and `read` already gives you prose. Keep the `drive_id` and `item_id` pair for anything worth reading in Phase 2.

**Readable is not yours.** SharePoint is the broadest org content of any connector here and the only one with no ownership signal, so the boundary has to be drawn at the fact. Check the hit's `url` host against the domain of the user's own mail address: a site on another tenant belongs to an organisation the user is not part of, and nothing from it is a fact about them. Within the user's own tenant, a document being readable is not a reason to mine it -- skip HR and personnel files, other teams' reviews, and anything that is not about the user's work. If SharePoint fails, continue with the other sources.

### Step 6: Write the temporary onboarding checkpoint

Your context may be compacted during this run. Before Phase 2, write `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md` with everything needed to continue: who the user is, the domain order, and every source found. This is chat-scoped workflow state, not Personal Knowledge. Never create a Knowledge topic for it or cite it to the user.

Use the exact Markdown structure below: `#` sections, one source per `-` bullet, and a metadata link at the end of each source line.

```markdown
# Notion

- "Q3 planning 2026" -- projects, people; authored by the user [notion](metadata://notion/7f46ba59a7fe8022af23e7fb7e943815)
- "Sheep Platform team page" -- about-me, people [notion](metadata://notion/9a26ba59a7fe80b1c8d34f0a21e5b7c6)
- "Herding glossary" -- glossary [notion](metadata://notion/2c81aa03a7fe80d47b19e6c3f8a2d059)
- "Weekly update 2026-03-06" -- projects [notion](metadata://notion/5db4e117a7fe809e3c62b8d17f40ae23)

# Slack

- #sheep-platform -- projects, glossary [slack](metadata://slack/channel/C09FK3M2TQL)
- "MS1 status" thread -- projects [slack](metadata://slack/thread/C09FK3M2TQL/1784301576.221900)
- "naming argument" thread -- glossary, preferences [slack](metadata://slack/thread/C0AK4B7SDPQ/1783700850.884300)

# Gmail

- "MS1 slip -- revised dates" -- projects [gmail](metadata://gmail/thread/18f2a9c4d1e07b3a)
- "re: herding contract signed" -- projects, people [gmail](metadata://gmail/thread/18e7b02fa93c14dd)

# Drive

- "Flock 3.1 launch plan" -- projects; owned by the user [google_drive_mcp](metadata://google_drive_mcp/file/1aB2cD3eF4gH5iJ6kL)
- "Herding metrics Q1" -- projects, glossary [google_drive_mcp](metadata://google_drive_mcp/file/1zY9xW8vU7tS6rQ5pO)

# Outlook

- "RE: flock charter sign-off" -- projects, people; inbox [outlook](metadata://outlook/message/AAMkAGI2YjVkNzRlLTg0YzUtNDVjYy05YjdlLWFlN2Q3MmRkZjYxYgBGAAAAAAA3K3pBbdFrSKqUy7vN6cBwBwCdhXFDmVTIQqZ3WXYQAAAAAADhAAACdhXFDmVTIQqZ3WXYQAAAAAAE5J9AAA=)
- "Q1 herding budget" -- projects; sentitems [outlook](metadata://outlook/message/AAMkAGI3YmEzZDc1LWIxMTQtN2Q3Zi05YjdlLWFlN2Q3MmRkZjYxYgBGAAAAAAA3K3pBbdFrSKqUy7vN6cBwBwCdhXFDmVTIQqZ3WXYQAAAAAADhAAACdhXFDmVTIQqZ3WXYQAAAAAAE5K1AAB=)

# SharePoint

- "Flock Handbook.docx" -- glossary, preferences; Herding Ops library [sharepoint](metadata://sharepoint_mcp/b!abc.../01XYZ...)
- "Q3 flock review.pptx" -- projects [sharepoint](metadata://sharepoint_mcp/b!abc.../01QRS...)

# Run

- User is Shepherd McFlockface, Europe/Paris, Sheep Platform, handle `shep` [notion](metadata://notion/self)
- Domain order: about-me -> people -> projects -> glossary -> preferences
```

List every source discovery returned, not a sample: one bullet each, with its title, which topics its highlights point at, and its metadata link. The resource ID in that link is how you reach it again after compaction; the title and tags are how you decide whether it is worth reaching for.

Append as you go, never rewrite. Under `# Run`, add one line for each event -- `Fetched "Q3 planning 2026" [notion](metadata://notion/<page_id>)`, `Completed about-me in profile`, `Completed people in collaborators` -- and leave existing lines alone. Rewriting costs more than the information is worth.

On resume, the start sequence reads `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md` top to bottom. `# Notion`, `# Slack`, `# Gmail`, `# Drive`, `# Outlook`, and `# SharePoint` are the candidate set, and `# Run` restores the user's identity, domain order, completed domains, actual target topics, and fetched or read pages. Then list the topic folders on disk to confirm. Rely on this checkpoint, not memory, for progress.

## Phase 2 - Extract five knowledge domains

The Drive column is Drive query DSL. SharePoint shares the column because both are filename-shaped, but `sharepoint_mcp.search` takes plain keywords -- never send it `owner = 'me'`, `title contains`, or anything else from this column's syntax. The `about-me` row has no SharePoint form at all: with no author filter, ownership cannot be expressed, so that row is Drive-only.

| Domain / default topic | Default icon | Notion / Slack (prose) | Gmail / Outlook (subject line) | Drive / SharePoint (filename) | What to extract |
| --- | --- | --- | --- | --- | --- |
| about-me | 👤 | `"{user_name} role"`, `"team responsibilities"` | `from:hr OR subject:(onboarding OR offer OR contract)` | `owner = 'me'` and recency alone | Role, team, location, timezone, handles |
| people | 👥 | `"team colleague reports to"`, `"{user_name} and"` | `subject:(intro OR welcome OR 1:1 OR review)` | `title contains '1:1'` | Name, role, team, relationship to the user |
| projects | 🚀 | `"project roadmap milestone"`, `"status update shipping"` | `subject:(kickoff OR launch OR signature OR invoice OR statement)` | `title contains '<project noun>'` | Project name, status, stakeholders, recent decisions |
| glossary | 📖 | `"acronym definition means"`, `"internally we call"` | rarely productive | rarely productive | Term, definition, context |
| preferences | ⚙️ | `"prefer async"`, `"schedule meeting style"` | `subject:(invitation OR reschedule OR OOO)` | rarely productive | Work habits, scheduling, communication patterns |

**Query shape is per corpus, not per domain.** The same phrase behaves differently across text distributions: Notion is prose and takes concept phrases; Slack is conversational and takes the short form people actually type; Gmail and Outlook subject lines are written by machines in transactional vocabulary -- confirmed, invoice, signature, reservation, declaration -- and almost never contain a phrase like "project roadmap milestone"; Drive gives you filenames only, so nouns, and often not even useful ones. Outlook shares Gmail's vocabulary but not its syntax: the operator strings in that column are Gmail-only. Translate them -- the terms go in `query`, `from:` becomes `message_from`, `to:` becomes `message_to`, and the `-category:` exclusions have no equivalent at all. `message_from` and `message_to` take one exact address (Step 5d), so where you have no address, put the terms in `query` and scope by folder instead. A domain that reads as productive in Notion may be barren in Gmail and Drive. That is expected -- mark it and move on rather than forcing a query.

### Topic admission and altitude

- **about-me** is the user only, from `self` and `read_user_profile()`: role, title, team, location, and timezone. A table row or roster mentioning the user is evidence for people, not about-me. Raw identifiers are query handles, not facts to write.
- **people** leads with full name, role or work area, relationship to the user, and why that person matters. Prefer mapping people to projects or durable collaboration patterns over inventing team buckets. A one-off interaction, calendar attendance, cc, reviewer mention, or tag is not a relationship.
- **projects/current focus** save areas and projects, not implementation tasks. A project or area needs the user's role, what it is, why it matters, who is involved, and current status, a next step, open decision, or recent outcome. For completed projects, save impact or learnings rather than stale milestone lists.
- **tools/workflows/glossary** save explicit recurring tool usage, processes, and definitions. A tool merely mentioned in a project is not the user's workflow. A glossary term needs a definition, not only an occurrence.
- **preferences** are observed behavior: what the user did, chose, or scheduled repeatedly. A position argued in a document is not a preference, even if the user wrote it.

Before writing a candidate fact, apply the usefulness test:

1. Would it help answer a future question, draft an update, prepare a meeting, route a tool call, or personalize output?
2. Is it likely to stay true or useful beyond a few days?
3. Is it specific enough to help, but not merely a random event?
4. If it is broader project or team context, does it explain the user's work, collaborators, decisions, or next steps?

Save fewer facts when necessary. Do not pad thin domains, but do not make a narrow user the rule for everyone: transverse users may need more project and collaborator context when it passes the same test.

Treat the table names as knowledge domains and default slugs for newly created topics, not mandatory folder names. Before processing each domain, inspect the existing topic descriptions as required by `knowledge-mutations`. Extend a semantically matching topic when one exists; create the default topic only when no existing topic covers that domain. Multiple domains may belong in the same existing topic. Never create a duplicate topic merely to reproduce the table.

Process the domains in the order above, skipping any that `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md` already records as completed. Record the actual topic used for each domain so a resumed run follows the same routing.

**Sequence domains, parallelize inside them.** Finish one domain before starting the next: extract -> write or extend the selected topic -> append a line to `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md` -> move on. Only that boundary is serial. Within a domain, issue several searches at once.

Per-domain loop:

1. Run the domain searches in parallel across every connector that appears in the checkpoint, using that connector's query shape from the table above. `max_highlight_length: 500` is a Notion parameter and applies to the Notion pass only.
2. Extract every fact possible from highlights and snippets alone. Drive returns neither, so a Drive candidate is a title you have to decide about blind.
3. Rank remaining candidates by on-topic signal.
4. Fetch at most one or two, only when all three fetch conditions hold. `notion.notion_fetch`, `slack.read_thread`, `gmail.get_thread`, `google_drive_mcp.read_file_content`, `outlook.open_outlook_email`, and `sharepoint_mcp.read` all draw on the same budget.
5. Mine each fetched page for all five domains. Put on-domain facts in the selected topic and route other facts through the matching existing or default topic for their domain. Write one file at a time; do not defer facts.
6. Append `Completed <domain> in <actual-topic>` and any `Fetched ...` lines under `# Run`, then move on.

**Fact density.** There is no minimum. For a narrow domain, 3-8 high-value facts is often enough. A transverse user may justify more when the facts remain useful and non-duplicative. If a domain yields no eligible durable facts, record that only in `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md`; never create or modify a user topic with an empty placeholder.

**Every fact needs verbatim support.** If you cannot point to a source sentence that says essentially the same thing, do not write the fact. There is no edit UI; a wrong fact is permanent until the user finds it.

Extract specifics, not summaries. Strong facts carry numbers, names, dates, and verbatim positions, scoped appropriately for their topic.

| Weak - do not write | Strong - write this |
| --- | --- |
| "The team shared a broad update" | "The customer onboarding program moved account guidance into a reusable rollout plan [Customer onboarding plan](<connector-returned Notion URL>)" |
| "Nadia is involved in the project" | "Nadia Vasquez -- Program Manager; owns the customer onboarding rollout plan [Customer onboarding plan](<connector-returned Notion URL>)" |
| "People discussed ownership" | "Nadia confirmed the onboarding rollout remains with Program Management; Ewan owns the technical handoff [Ownership decision thread](<connector-returned Slack permalink>)" |

**Capture disagreement.** If two people take opposing positions, write both with attribution. A contradiction is a fact about the organization, not a problem to resolve.

**Recency.** When two sources disagree on current state, write the newer claim, rewrite the older one as dated history when it is still useful, or save nothing. A rolling document is not one moment in time: use the date of the relevant section, not only the page's `last_edited_time`. From historical sections, keep only stable decisions, things that happened, impact, or learnings -- never a current role, status, or headcount. Confirm transcript-only spellings and acronyms against a written source.

### Quality gates

Apply before writing:

- `high`: fact appears in 2+ distinct sources -- write it.
- `single_source`: one source only -- write with `<!-- confidence: single_source -->`.
- `review_required`: plausible but the source is ambiguous or truncated -- do not write it; optionally present it later as a review note.
- `stale`: contradicted by a newer source -- do not write. For a current-state claim, a source last edited six or more weeks ago with nothing newer confirming it is likely superseded.
- `low`: inferred with no direct citation -- do not write.

## Output format

For a newly created default topic, write one `KNOWLEDGE.md` whose frontmatter includes the corresponding emoji from the Phase 2 table as `icon`. When extending an existing topic, preserve its name, display name, description, icon, structure, and unrelated content unless a change is required by the new facts. Group facts under `#` section headings. Sections emerge from the material: project phases, sides of an argument, or settled versus open questions.

Every connector-sourced fact is a single-line `-` bullet with one clean, human-readable source link at the end. Use the source title as the link label and the exact Notion URL, Slack permalink, Gmail thread URL, Drive file link, or SharePoint `web_url` returned by the connector, for example `[Weekly - Knowledge Base](<connector-returned Notion URL>)`. Never construct, transform, guess, or hardcode a workspace URL. Never emit a blank, comma-only, generic, or duplicated source link.

About-me facts copied directly from `notion.notion_fetch(id="self")` or `slack.read_user_profile()` are the only citation exception: write only fields directly returned by those profile calls and leave them uncited. Never cite `notion:self` or a raw profile ID.

A `KNOWLEDGE.md` file is a fact list under headings, not an essay; it is read by search, not front to back.

Date claims that go out of date. "Alodie Boissonnet is the AI Engineer" goes stale silently; "was the AI Engineer as of March 2026" stays true and tells the reader to check.

Do not write:

- Existence assertions such as "X is a project" or "Y is a glossary source".
- Connective tissue, lead-in sentences, summaries, or "worth noting".
- Working-state entries, fetch status, or run metadata.
- Calendar event titles used as citations.
- Things the user saw that are not about the user's work.
- Example content from this skill such as PastureBench or Shepherd McFlockface.

Bold only the subject of a fact, such as a person's or project's name, never for emphasis.

```markdown
---
name: projects
description: The three efforts Shepherd is running -- status, owners, and the
  open blockers on each
icon: 🚀
---

# Sheep Platform

- Shepherd leads the customer onboarding rollout; all six launch items were reported done on 2026-03-10 [Customer onboarding plan](<connector-returned Notion URL>)
- **Ewan Ramsbottom** owns the technical handoff; **Nadia Vasquez** owns the program rollout [Customer onboarding plan](<connector-returned Notion URL>)

# Open blockers

- The customer onboarding rollout is blocked on the technical handoff, which slipped from end of July to late August [Onboarding status thread](<connector-returned Slack permalink>)
- **Milo Bramble** flagged that the handoff process skips a required approval step; no fix planned [Handoff thread](<connector-returned Slack permalink>) <!-- confidence: single_source -->
```

The `description:` line must say specifically what the topic covers. "Active projects" is weak; the example above is useful when the file is later recalled by search.

Use connector URLs and identifiers exactly as returned by the tool. Copy them whole, character for character. Do not shorten them, drop a suffix, add or remove dashes, construct a workspace URL, or retype them from memory. Preserve decimals in Slack timestamps.

What a link can be differs by corpus. Gmail: use the thread URL the connector returned; if it returned none, cite the `threadId` bare and leave it unlinked. Drive: document, spreadsheet, and presentation files sit on different hosts, so never build a Drive URL -- use the link the connector returned with the file, and if it returned none, cite the `fileId` bare and leave it unlinked. Outlook: the subject is the title, and since there is no per-message URL the link is a search over it -- `[<subject>](https://outlook.cloud.microsoft/mail/?q=<percent-encoded subject>)`. That re-finds the message wherever it has since been filed, which a message URL would not: the `message_id` encodes the folder chain and dies the moment the mail is moved. SharePoint: use the `web_url` the item returned, never a constructed one; if it returned none, cite the `drive_id`/`item_id` pair bare and leave it unlinked. A returned `web_url` carries literal spaces, and library names keep doubled ones (`Herding  Ops  Test`), so percent-encode every space as `%20` and preserve the runs -- two spaces become `%20%20`. Change nothing else about it.

## Phase 3 - Clean up

When all five domains have been processed:

1. Confirm each topic that was created or extended has valid frontmatter and preserves unrelated existing Knowledge.
2. Delete the temporary `/home/user/tool-results/knowledge-onboarding/cold-start-sources.md` checkpoint. It served the run and is not part of the user's Knowledge Base.
3. Tell the user what was written and mention any area where the connected sources provided little useful information. In this user-facing summary, name each topic actually created or extended exactly once as a labeled Markdown Knowledge link. Do not link an unchanged topic merely to make the list reach five. Do not expose tool-call counts, read budgets, source plans, coverage statistics, or verification ledgers.

Optionally present at most five unresolved review notes that were not written because their evidence was ambiguous or truncated.

Keep the temporary checkpoint until all five domains have been processed. The only early-deletion exception is when no source yields usable material and the flow ends under the graceful-degradation rule above.

## Final rules

- Present the output to the user for review before marking done.
- Every connector-sourced fact cites one clean, direct source link; directly returned profile facts remain uncited.
- Never write low-confidence or stale facts.
- Write each topic file as it is finished, one at a time. Never batch writes to the end and never write two files at once.
- Remind the user that they can inspect, correct, or remove anything.
- After the summary and reminder, say the localized equivalent of: "Your Knowledge base is ready to use. What would you like to do next?" This readiness sentence must appear before the suggestions below.
- Then warmly invite the user to try the Knowledge Vibe just gathered. Suggest two or three concise, personalized next steps grounded in their actual projects, people, workflows, or preferences: lead with a useful question they can ask about their current context, and optionally include a concrete task Vibe can now do better with that Knowledge. Do not suggest Knowledge maintenance such as updating the entire Knowledge Base or a topic unless the user asks for it.