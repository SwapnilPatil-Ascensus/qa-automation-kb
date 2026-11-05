# Unqork & Retirement onboarding — starter notes

**Status:** Public / job-posting context only. Internal Ascensus SharePoint, Jira, and team naming (White, Ravens) are **[NEED_INPUT]** until you export or paste materials here.

## Unqork at Ascensus (public)

| Topic | Source |
|-------|--------|
| **Transition Services** owns onboarding methodology; **Unqork** called out as a product domain | [Digital Onboarding Product Owner (Ascensus careers)](https://careers.ascensus.com/jobs/digital-onboarding-product-owner-dresher-pennsylvania-united-states) |
| PO role: vision/backlog for Unqork domain, BDD acceptance criteria, scrum/UX, KPIs, Organizational Readiness | Same posting; mirror on [Built In](https://builtin.com/job/digital-onboarding-product-owner/10241169) |
| **Unqork + Cognizant** sponsor onboarding: digital portals, workflow orchestration, no-code amendments | [Unqork PDF — Transforming Retirement Plan Sponsor Onboarding](https://unqork.com/wp-content/uploads/2021/05/unqork-cognizant-transforming-retirement-plan-sponsor-onboarding.pdf) |
| Employer-facing digital onboarding (plan setup, e-sign) | [Ascensus — Digital Retirement Plan Onboarding](https://www.ascensus.com/resources/resources-for-employers/a-simpler-digital-onboarding-experience-for-your-retirement-plan/) |

## Team “White” and “Ravens”

| Finding | Detail |
|---------|--------|
| This repo (GS KB) | **No** matches for “Ravens” or a team named “White”. |
| Possible confusion | GS docs mention **Empower/Whitecap** (529 partner plan automation), not a squad named White. |
| Next step | Paste org chart, SharePoint hub link, or Confluence space name for Retirement squads into this file or `programs/` once you have access. |

## SharePoint access (agent)

Automated access to `ascensus0.sharepoint.com` stops at **Microsoft SSO** — the agent cannot complete sign-in on your behalf. GS site pattern (for reference): [Government Savings – Software Development](https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development). Retirement sites will be different; request membership from your manager or SharePoint admin.

**Ways to unblock documentation work:**

1. Export / PDF / sync Retirement onboarding pages to this repo under `retirement/`.
2. Add a Microsoft Graph or SharePoint MCP in Cursor after Entra admin consent (see `government-savings/programs/sharepoint-qa-hub/05-mcp-and-graph-plan.md` for the GS pattern).

## Suggested capture checklist (when you have internal docs)

- [ ] Unqork environment URLs (non-prod), release cadence, and who owns platform vs product backlog  
- [ ] Onboarding service delivery models (Transition Services) and handoffs to IT/QA  
- [ ] Squad White / Ravens: charter, Jira board, Definition of Ready/Done for Unqork stories  
- [ ] Test strategy: BDD locations, qTest/Jira linkage, regression scope for sponsor onboarding  
- [ ] Access: Unqork builder roles, SSO groups, any separate Retirement SharePoint hub  
