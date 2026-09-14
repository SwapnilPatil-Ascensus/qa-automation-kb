# 04 — Copilot prompts (paste into SharePoint)

Open the target **Site Page** (or Create → Site page) while signed into Ascensus. Paste **one** prompt. Then paste the markdown from `pages/` into a Text web part and ask Copilot to **redesign using the design system**.

Replace `{{MARKDOWN}}` with the file contents.

## Prompt 0 — Hub home (00)

```
You are redesigning the GSSD Automation QA documentation hub on this SharePoint site.

Goal: a modern Microsoft 365 product-style home page. Not a Confluence dump.

Constraints:
- Title: 00 Automation QA — Home
- No emoji in titles
- Hero: one sentence — "Operating home for Government Savings automation: how we onboard, run regression, triage failures, and find pipelines."
- Six Quick links labeled: Start here, Access, Regression, Defects, Pipelines, Performance
- Two-column layout under the hero: main content + right rail (Owners, Last reviewed)
- At most five H2 sections
- Add a short "Archive" note at the bottom: old Confluence pages are under 99 Archive and are not the source of truth
- Do not invent Jenkins URLs, passwords, or coverage percentages
- Use the following copy exactly for body text:

{{MARKDOWN}}
```

Use [pages/00-hub-home.md](./pages/00-hub-home.md).

## Prompt 1 — Any numbered child page

```
Create or redesign this Site Page as a concise runbook.

Title format: {{NN}} {{Short name}}
Audience: QA automation engineers on AM Squad.
Layout: hero (no stock photo), then two-thirds + one-third.
H2 limit: five.
Prefer tables.
Include a right-rail People web part placeholder for the page owner.
Do not add emoji.
Do not copy archival or hiring content.
Body copy:

{{MARKDOWN}}
```

## Prompt 2 — Rewrite from an ugly migrated page

Use this **on the old dump page** if you would rather transform in place, then rename/move into the numbered IA.

```
This page was migrated from Confluence and is hard to use.

Rewrite it as a modern SharePoint page:
- Cut anything dated, duplicated, or "DRAFT"
- Keep only procedures a new engineer would run this week
- Convert walls of text into tables and numbered steps
- Add a banner: "Source of truth is being moved to the numbered Automation QA hub (00–14). This page will be archived."
- Do not add new facts that are not on the current page
```

## Prompt 3 — After Copilot drafts (quality gate)

```
Audit this page:
- Remove emoji and Confluence macros leftover
- Ensure every link has a human-readable label
- Collapse duplicate sections
- Add footer: Owner, Last reviewed date, Git path programs/sharepoint-qa-hub/
```

## What Copilot will not do well

- Stay consistent across 16 pages unless you paste the design system each time.
- Know our Git paths unless they are in the markdown you paste.
- Create the left navigation tree — you (or a site owner) still set **Site navigation**.

## Optional: Graph later

If an MCP can `create_page`, still run Prompt 1 in Copilot afterward (“redesign this page for Fluent layout”). Graph-created pages are usually empty canvas + text.
