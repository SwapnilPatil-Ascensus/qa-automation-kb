# 00 — Access and constraints

## Live SharePoint

| Item | Value |
|------|--------|
| Tenant host | `ascensus0.sharepoint.com` |
| Site | `Government_Savings-_Software_Development` |
| Hub page URL | [GSSD Automation QA – Home & Documentation Hub](https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development/SitePages/GSSD-%E2%9C%85-Automation-QA-%E2%80%93-Home--Documentation-Hub-315559619.aspx) |
| Auth | Microsoft Entra SSO (Ascensus) |
| Agent fetch (2026-09-03) | Redirect to **Trying to sign you in** — no page body, no child list, no file download |

This agent **does not** have your browser cookies, OneDrive sync, or a Graph token for that tenant.

## What you can do (human, 15–30 min)

If the live SharePoint tree is newer than the local Confluence export, capture it **on your machine** and drop it under `qa-knowledge-base/10_IMPORTS_RAW/sharepoint_exports/` (create that folder when you have files). Preferred methods, in order:

1. **OneDrive sync** the site document library / Site Pages attachments (Settings → Add shortcut to OneDrive). Copy the folder into the import path. Best for Word/PDF/Excel.
2. **SharePoint “Copy to” / “Download”** on a library view (multi-select). Site Pages themselves are `.aspx` — Copilot/Graph is better than Save-as-PDF for those.
3. **PnP PowerShell** (if you already use it): `Connect-PnPOnline` then `Get-PnPPage` / `Export-PnPPage`. Requires your SSO session locally.
4. **Print to PDF** only for a handful of pages you care about; do not do this for 100+ children.

Do **not** commit OneDrive `desktop.ini` or files that look like credentials.

## Cursor MCP in this workspace (2026-09-03)

| Namespace | Status | Useful for SharePoint? |
|-----------|--------|------------------------|
| user-gitlab | ready | Repo files only |
| user-jira | ready | Tickets, not docs |
| user-qtest | ready | Test cases, not docs |
| user-Snyk | ready | Security scans |
| user-brave-search | ready | Public web research |
| user-http | **error** | Could have fetched public URLs; still would fail SSO |
| user-slack / user-git / user-1password | error | Unrelated |
| SharePoint / Microsoft Graph | **not installed** | Required for live read/write |

## Two creation paths (both valid)

### Path A — Copilot on SharePoint (now)

You stay in the browser. Cursor (this repo) drafts the IA and the prompt. You paste into Copilot on the hub page. Copilot lays out Hero, Quick links, sections, and callouts. This matches how you described the goal.

### Path B — Graph / SharePoint MCP (later)

After IT registers an Entra app (or you use a community MCP with device-code login that Conditional Access allows), this agent can list pages, download library files, and **create skeleton modern pages**. It still will not match Copilot’s visual design unless we only seed text and you run Copilot “redesign this page” once.

Recommended sequence: **Path A for the hub + first 8 numbered pages**, then Path B for bulk library inventory and keeping markdown in sync.

## Assumptions

1. You have Contribute or higher on the GSSD Software Development site.
2. The Confluence export in `auto-qa-dochub` is the same tree as the ugly SharePoint dump (same `pageId=315559619`).
3. “QA automation squad main TV project folder” is the local/SharePoint documentation tree you already copied into this KB (not a separate system this agent can see).
4. Leadership wants a **small published set**, not 110 public pages.
5. Azure Conditional Access may block device-code MCP login; Graph app + admin consent is the enterprise path.
