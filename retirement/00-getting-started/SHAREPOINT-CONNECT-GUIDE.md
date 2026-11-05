# SharePoint access — what works on day one

You asked to “connect SharePoint and save SSO” so the agent can browse for you. Here is the honest boundary and the **fastest path that actually works** for a new hire.

## What the agent cannot do (security, not choice)

| Request | Reality |
|---------|---------|
| Save your Ascensus password or SSO session permanently | **Not allowed** — Conditional Access, MFA, and audit rules block storing corporate credentials in Cursor, MCP env, or this repo. |
| Log in as you without you at the keyboard | **No** — Microsoft sign-in requires **your** account + MFA on your device. |
| Install a random SharePoint plugin with full tenant access | **Needs IT/security review** — enterprise SharePoint apps use Entra app registration + admin consent. |

The GSSD site is **Microsoft 365 SharePoint Online** (`ascensus0.sharepoint.com`), not classic on-prem IIS SharePoint. Retirement may use **other** site URLs; add them below when your manager sends links.

## What works today (you + agent in one session)

### Option A — Cursor browser (best for “show me around”)

**Update:** When you are already signed into Microsoft 365 on your machine, the **Cursor Browser** tab can reuse that session (shown as your account in the header). The agent can navigate and read pages **in that tab** without storing your password.

1. Open the **Browser** panel in Cursor (a tab may already be on `ascensus0.sharepoint.com`).
2. If you see **Sign in**, complete Ascensus email + MFA **once** in that tab.
3. Paste your **Retirement / Unqork** site URL in chat (GSSD alone does not index Unqork — org search for `Ravens` returned no hits; `Unqork` may live on a different site you were not granted yet on day one).
4. The agent walks pages and summarizes into `retirement/` for you.

Session ends when the tab closes or tokens expire; sign in again when prompted. That is normal — it is not the agent “forgetting,” it is SSO token lifetime.

### Option B — Bulk export once (best for “don’t download one by one”)

Run the script below **on your laptop** while logged into M365 in Edge. It pulls Site Pages and document libraries into this repo under `retirement/sharepoint-export/` so the agent can search everything offline.

```powershell
cd c:\Development\workspace\qa-automation-kb\qa-automation-kb\retirement\tools
.\Export-SharePointSite.ps1 -SiteUrl "https://ascensus0.sharepoint.com/sites/<YOUR-RETIREMENT-SITE>"
```

Replace `<YOUR-RETIREMENT-SITE>` with the path your manager gives you (GSSD example: `Government_Savings-_Software_Development`).

First run installs `PnP.PowerShell` for **your user** and uses **interactive** login (same SSO you use in Edge).

### Option C — IT-backed MCP (best long-term)

Ask IT for an Entra app with **`Sites.Selected`** on your Retirement site only. Template and rationale:  
`government-savings/programs/sharepoint-qa-hub/05-mcp-and-graph-plan.md`

Do **not** put client secrets in Git. Put them in Cursor MCP env (local only).

## IT ticket you can copy-paste

> New hire on Retirement / Unqork onboarding. Need read access to SharePoint site(s): `[URL]`.  
> Request: Entra app registration for Cursor MCP with **Sites.Selected** (read-only first) on that site, or membership in `[site name]` for `[your UPN]`.  
> Purpose: bulk documentation export into internal Git KB repo `qa-automation-kb` (no customer PII in repo).

## After export lands in the repo

Tell the agent: **“Ingest `retirement/sharepoint-export/`”** — it can map Unqork/onboarding docs, team White/Ravens pages, and build a reading order for your first week.

## Sites to collect from your manager [NEED_INPUT]

| Name | URL | Owner |
|------|-----|-------|
| Retirement / Unqork onboarding | | |
| Team White | | |
| Team Ravens | | |
| Transition Services | | |
