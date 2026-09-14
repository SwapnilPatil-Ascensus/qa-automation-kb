# SharePoint — Automation QA Documentation Hub

**Owner:** QA Automation (AM Squad)  
**SharePoint site:** [Government Savings – Software Development](https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development)  
**Hub page (migrated Confluence dump):** [GSSD Automation QA – Home & Documentation Hub](https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development/SitePages/GSSD-%E2%9C%85-Automation-QA-%E2%80%93-Home--Documentation-Hub-315559619.aspx) (`pageId=315559619`)  
**Related squad page:** [GSSD Automation Squad](https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development/SitePages/GSSD-Automation-Squad-229118272.aspx)  
**Last updated:** 2026-09-03

## What this program is

The Confluence **Automation QA – Home & Documentation Hub** was lifted into SharePoint as a dump: long titles, emoji, nested children, and pages that do not read like modern SharePoint. Microsoft Copilot on the site can produce clean Site Pages. This folder is the **repo control plane** for that rebuild.

| Layer | Role |
|-------|------|
| This Git folder | Source of truth for IA, page copy, Copilot prompts, keep/rewrite/archive decisions |
| Local imports | Preserve the old Confluence/SharePoint dump (PDFs, markdown already in this repo) |
| SharePoint Site Pages | Published UX for the squad and partners |
| Dashboards (later) | Lists, Power BI, or Viva — not in this first cut |

## Direct answers (2026-09-03)

| Question | Answer |
|----------|--------|
| Can this agent sign into SharePoint and walk parent + children? | **No.** Fetch hits Microsoft SSO (`Trying to sign you in`). Same finding as [`programs/qc4-enablement/04-sharepoint-access.md`](../qc4-enablement/04-sharepoint-access.md). |
| Is a SharePoint MCP connected in this Cursor session? | **No.** Available MCPs: GitLab, Jira, qTest, Snyk, Brave. HTTP / Slack / Git / 1Password servers are in error. There is **no** SharePoint or Microsoft Graph MCP. |
| Can we download the live SharePoint tree from here? | **No.** You (or IT) must export, OneDrive-sync, or add a Graph MCP with tenant consent. |
| Do we already have the documentation locally? | **Yes — a large Confluence export**, which is the same hub (`pageId=315559619`). See [01-source-inventory.md](./01-source-inventory.md). |
| Best way to create beautiful pages **now**? | Write copy here → paste the prompts in [04-copilot-prompts.md](./04-copilot-prompts.md) into **SharePoint Copilot** on the site. |
| Best way to create pages **dynamically later**? | Add a Microsoft Graph / SharePoint MCP after Entra consent. Plan: [05-mcp-and-graph-plan.md](./05-mcp-and-graph-plan.md). Graph can create modern pages; Copilot still wins on visual layout. |

## How to use this folder

1. Read [00-access-and-constraints.md](./00-access-and-constraints.md) so expectations stay honest.
2. **UI Automation first:** [`ui-automation/README.md`](./ui-automation/README.md) — hub + New Engineer Start Here, then one page at a time.
3. Use [02-information-architecture.md](./02-information-architecture.md) for the four-hub tree (do not recreate Master Onboarding).
4. Apply [03-page-design-system.md](./03-page-design-system.md) on every new page.
5. Copilot prompts for UI: [`ui-automation/copilot/`](./ui-automation/copilot/). After a page is live, archive the old dump per [06-archive-and-lifecycle.md](./06-archive-and-lifecycle.md).

## Folder map

```
programs/sharepoint-qa-hub/
├── README.md
├── 00-access-and-constraints.md
├── 01-source-inventory.md
├── 02-information-architecture.md
├── 03-page-design-system.md
├── 04-copilot-prompts.md
├── 05-mcp-and-graph-plan.md
├── 06-archive-and-lifecycle.md
├── 07-build-sequence.md
├── inventory/                    # what we already have locally
├── pages/                        # SharePoint-ready markdown (numbered)
├── templates/                    # one layout for every child page
└── scripts/                      # local inventory only (no SharePoint login)
```

## Local source (already in this repo)

Do not re-download these unless SharePoint has **newer** content than the Confluence export:

- Hub PDFs: `qa-knowledge-base/10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/` (**110 PDFs**)
- Performance hub (mixed docs + Jenkins/JMeter noise): `qa-knowledge-base/10_IMPORTS_RAW/Performance QA – Home & Documentation Hub/`
- Curated markdown already rewritten: `qa-knowledge-base/10_IMPORTS_RAW/AM_Regression_Reports/docs/`, `qa-knowledge-base/00_SYSTEM` … `05_ONBOARDING`

## Non-negotiables

1. **This repo stays source of truth.** SharePoint is the published view.
2. **Do not paste secrets** (tokens, `secretKeyStage`, passwords) onto Site Pages. The Performance import folder contains files that must never be republished.
3. **Rewrite, do not migrate 1:1.** Hiring packs, drafts, and duplicate archival PDFs stay in Archive.
4. **Numbered IA** on SharePoint matches this folder (`00` hub, `01` Start here, …).
