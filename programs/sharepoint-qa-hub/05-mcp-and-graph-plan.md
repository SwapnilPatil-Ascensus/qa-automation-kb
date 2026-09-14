# 05 — MCP and Microsoft Graph plan

## Current state

This Cursor workspace has **no SharePoint connector**. Dynamic creation of Site Pages from the agent is **not possible until you add a server and tenant consent**.

## What we want the MCP to do

| Capability | Why | Graph-ish API |
|------------|-----|----------------|
| List site pages | Inventory live vs local export | Site Pages library / `sites/{id}/pages` |
| Read page canvas | Diff dump vs rewrite | `sitePage` + canvasLayout |
| Download drive items | Word/PDF libraries | `/drives/{id}/items/{id}/content` |
| Create modern page | Seed 00–14 from `pages/*.md` | create `sitePage` |
| Update navigation | Numbered left nav | Site navigation APIs (often extra consent) |
| Search | Find duplicates | Microsoft Search |

Copilot layout is **not** a first-class Graph resource. Plan on **seed in Graph, polish in Copilot**.

## Options (research, 2026)

| Option | Pros | Cons | Fit |
|--------|------|------|-----|
| [Microsoft MCP / Graph](https://github.com/microsoft/mcp) | Vendor path | SharePoint-specific server lagged community connectors (as of mid-2026 writeups) | Prefer if IT already uses it |
| Community SharePoint MCP (e.g. Graph `list_site_pages` / `read_site_page`, file download) | Read dump + libraries | Needs Entra app: `Sites.Read.All` or **`Sites.Selected`** | Best for **inventory** |
| [sharepoint-online-mcp](https://github.com/dYn36/sharepoint-online-mcp) (device code, `create_page`) | Can create/publish pages without a custom app id | Conditional Access often **blocks device code**; uses a public client id; IT may refuse | Try only if CA allows |
| PnP PowerShell on your laptop | You are already SSO’d | Not in Cursor unless you run scripts and drop files in the repo | Best **download all** today |
| SharePoint Copilot in browser | Best visual pages | Manual paste | **Do this first** |

## Enterprise consent (ask IT once)

Prefer **Sites.Selected** on site `Government_Savings-_Software_Development` over tenant-wide `Sites.Read.All` / `Sites.ReadWrite.All`.

App needs:

- `Sites.Selected` (read, then write)
- `Files.Read.All` or Files.Selected if libraries sit in the same site
- Admin grants the app **write** on that one site

Do **not** put client secrets in this Git repo. Use Cursor MCP env vars or Windows Credential Manager.

## Suggested Cursor `mcp.json` shape (do not commit secrets)

After IT provides `TENANT_ID`, `CLIENT_ID`, and a secret or certificate:

```json
{
  "mcpServers": {
    "sharepoint": {
      "command": "npx",
      "args": ["-y", "<approved-sharepoint-mcp-package>"],
      "env": {
        "SHAREPOINT_SITE_URL": "https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development",
        "AZURE_TENANT_ID": "<from-it>",
        "AZURE_CLIENT_ID": "<from-it>"
      }
    }
  }
}
```

Use the **package IT approves**. Do not install a random npm MCP against production SharePoint without a security review (Snyk MCP is already in this workspace for that).

## Hybrid workflow (recommended)

```
Repo markdown (pages/)  →  Copilot on SharePoint (visual)
                         ↘
IT Graph MCP (later)     →  list/download/diff  →  update inventory/
```

When MCP is live, first job is **read-only inventory**, not bulk publish.

## What this agent will do after MCP works

1. List Site Pages; mark dump vs `00–14`.
2. Download new Word/PDF not in `auto-qa-dochub`.
3. Seed missing numbered pages from `pages/*.md`.
4. Stop. You run Copilot redesign once per page.
