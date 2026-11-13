---
name: "doc-coauthoring"
description: "Guide users through a structured workflow for co-authoring documentation. Use when user wants to write proposals, technical specs, decision docs, RFCs, or similar structured content. Triggers on mentions of writing docs, creating proposals, drafting specs, or documentation tasks."
---
# Document Co-Authoring Workflow

## When to use

Activate when the user mentions: "write a doc", "draft a proposal", "create a spec", or specific document types like "PRD", "design doc", "decision doc", "RFC", "brief", "report".

## Three-stage process

### Stage 1: Context Gathering

1. Ask meta-context questions:
   - What type of document? (report, proposal, spec, brief)
   - Who is the primary audience?
   - What should the reader do after reading?
   - Any format requirements or constraints?
   - What's the deadline?

2. Encourage the user to dump all background info:
   - Prior discussions and decisions
   - Alternatives considered
   - Organizational context and constraints
   - Stakeholder concerns
   - Data or evidence available

3. Use available connectors (Slack, Google Drive, SharePoint) to pull context directly when possible.

4. Ask 5-10 clarifying questions to fill gaps.

**Exit criteria:** You have enough understanding to address edge cases and trade-offs without needing basics explained.

### Stage 2: Refinement & Structure

1. Propose a document outline based on gathered context
2. Build section by section, for each:
   a. Ask 3-5 specific questions about the section content
   b. Brainstorm 5-10 approaches/angles
   c. Let user curate (keep/remove/combine)
   d. Check for gaps
   e. Draft the section
   f. Iterate until satisfied
3. Start with sections having the most unknowns
4. At 80% completion, re-read the entire document checking for:
   - Flow between sections
   - Consistency in terminology and tone
   - Redundancy
   - Contradictions
   - Filler that can be cut

### Stage 3: Reader Testing

Test the document for blind spots:

1. Predict 5-10 questions a reader might ask
2. Check: Does the document answer each one?
3. Identify unstated assumptions
4. Look for ambiguous statements that could be misread
5. Suggest final improvements

## Guidelines

- Favor specific over vague ("reduced latency by 40ms" over "improved performance")
- Cut ruthlessly — after 3 rounds without substantial changes, ask what can be removed
- Match the depth to the audience (exec summary vs. technical deep-dive)
- End every document with clear next steps or a decision to be made