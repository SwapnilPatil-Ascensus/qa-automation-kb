# Retirement day-one brief — Team White, Unqork, access

**Captured:** 2026-11-02, signed in as Swapnil Patil in the Cursor browser.  
**Out of scope:** Government Savings. That portfolio is closed for this assignment.

This is a reading map so you can coordinate quality practice without downloading pages one by one. It is not a copy of every SharePoint page.

## What business you are in

**Team White** owns the **middle tier as a product** so Ascensus **Retirement** can run digitally. The SharePoint home says the space holds backlog, service docs, schedules, and meeting notes. Pages were last reviewed around **March 2023** and were lifted from Confluence space **MTP** (macros on some pages did not render).

Site: [Team White](https://ascensus0.sharepoint.com/sites/TeamWhiteCF)

The product they are building is **plan onboarding**, not 529 / Government Savings:

| Stage | What it means |
|-------|----------------|
| Sales | Interactions before a plan exists (IK Sales Portal) |
| Plan initiation | After sales, plan starts |
| Plan design | Plan rules, funds, and related design |
| Plan completion and activation | Documents signed, plan goes live |

Source: [Architecture](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Architecture-294981599.aspx) (Max Shakirov).

Green boxes on that diagram are the **Unqork** experience. The page says **Axo** was the partner helping Team White build that Unqork UX. DCA is planned to integrate into the Unqork dashboard. Your note that a third party took the project and it did not land cleanly matches “Axo + Unqork” as the named partner path. **[NEED_INPUT]** from your scrum master on whether Axo is still engaged. February 2026 pages still record Unqork production-style fixes (DocuSign, browser back button, PAS documents), so Unqork work did not stop in 2024.

## Tech stack (different from GS)

| Layer | What Team White uses |
|-------|----------------------|
| Experience | **Unqork** (no-code). Designer + runtime apps under `retsupport-*.unqork.io` |
| SSO into Unqork | SecureAuth: DEV `https://mfadev.ascensus.com/secureauth21`, QA `https://mfaqa.ascensus.com/secureauth21`, PRO `https://mfa.ascensus.com/secureauth21` |
| Direct Unqork logins (page text) | DEV `https://retsupport-dev.unquork.io/` (spelled **unquork** on the wiki), QA `https://retsupport-qa.unqork.io/`, PRO designer `https://retsupport-designer.unqork.io/` |
| APIs Team White builds | **Onboarding.API** (main passthrough Unqork calls), **Sales.API**, **Branding.API** (styling; may not stay an API) |
| Gateway | **Kong** in front of Onboarding.API |
| Orchestration | Plan onboarding workflow / saga — Onboarding.API does not do the work itself |
| Record / data | **Sybase** called out for SQEs. DCA is a separate system integrated into the dashboard |
| Build / release (SQE checklist) | **TeamCity** `http://teamcity.ascensus.com/`, **Octopus** `https://octopus.ascensus.com/` |
| Legacy work tracking | **TFS** `http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/Team%20White` (link on the SQE page is truncated in the HTML) |
| Other tickets | **TrakIT** (tasks), **Summit** (or current ticketing system) |
| Source control you were given | Azure DevOps Git repo [Retirement](https://dev.azure.com/ascensus/_git/Retirement) — **you can open it; it is empty** (“Add some code”) |
| Service desk | [servicedesk.ascensus.com](https://servicedesk.ascensus.com) — SSO works in this browser |

Unqork environment list: [Unqork information](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Unqork-information-294981398.aspx).

API test harness (QA workspace, application, `OnboardingAPI-QA` service, runtime `https://retsupport-qax.unqork.io/app/test-harness-onboarding-api`): [Onboarding API Test Harness (Unqork)](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Onboarding-API-Test-Harness-(Unqork)-305959989.aspx). That page lists a **shared mailbox and a shared password**. Do **not** copy that password into git, chat, or tickets. Ask the team for your own Unqork user.

Training: [Unqork Academy](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Unqork-Academy-294981693.aspx) points at `https://academy.unqork.com`.

## SQE onboarding checklist (Team White)

Page: [New Hire Setup for SQEs in Team White](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-New-Hire-Setup-for-SQEs-in-Team-White-33196168.aspx) (Chris Reynolds).

1. Confluence work agreement: `https://confluence.ascensus.com/display/MTP/Work+Agreement` (space may now live only on this SharePoint site).
2. TeamCity, Octopus, TFS, intranet `http://newintranet.ascensus.com/SitePages/Home.aspx`.
3. Visual Studio with Ascensus email. Local admin on the workstation.
4. Nice-to-have: SourceTree, Sublime.
5. **Sybase** access, **TrakIT** tasks, **Summit** (or replacement ticketing).
6. Learn the test framework, teams, and peers.

Wiki sections you already saw in the page tree (not all opened): Team, Deployment / Implementation, Implementation Schedule, Knowledge / How To (401k / DCA, glossary, Control-M, test mailboxes, TrakIT, Sybase KT), Meetings, **Projects → Onboarding**, Testing application documents, Completed Projects, Self-Directed Brokerage, Force-Outs, Scrum, Standards, Team Gold support, Testing, SecureAuth OTP.

## Access checked today

| System | Result |
|--------|--------|
| SharePoint Team White | **Yes.** Account shown as Swapnil Patil. |
| Service desk ticket [1638036](https://servicedesk.ascensus.com/support/tickets/1638036) | **Yes.** Portal title says “Request for Manish Jha”; the fields are **your** request: **Admin Account / Enable / account `swpatil`**, workstation admin so you can install dev tools. Stage **Requested**. Approvals show **Approved** by Chandu Chitikam (Mon Nov 2, 12:03 PM). Status option highlighted as **Being Processed**. Agent group: **SD Ops Engineer**. |
| Azure DevOps `ascensus` / Git **Retirement** | **Yes, after SSO.** Repo is **empty**. No boards, pipelines, or hours model live in that repo yet. |

Time entry (“spot hours”) is **not** documented on the pages opened today. The SQE list points at **TFS**, **TrakIT**, and **Summit**, not at the empty ADO repo. **[NEED_INPUT]** from Pamela Barone (Senior Scrum Master on the Team White home page) or your manager: which tool is the system of record for capacity and time in 2026.

## What you can do this week (quality coordination)

You are not re-platforming GS Selenium/Jenkins here. First job is access plus a quality map of **Unqork onboarding**.

1. Finish ticket **1638036** (local admin) so Visual Studio and tools can install.
2. Open service-desk requests, using the SQE page as justification, for: **Sybase**, **TrakIT**, **Summit** (confirm the name), **TeamCity**, **Octopus**, **Unqork** (personal user, not the shared harness password), **TFS Team White** if that server is still in use.
3. Ask who owns boards: TFS project vs a real Azure DevOps **project** (the Git repo named Retirement is only an empty container). Do not initialize that repo with a README until the team agrees it is the new home.
4. Read, in order: Unqork information → Architecture → Onboarding API test harness → Projects / Onboarding in the page tree → recent 2026 Unqork implementation notes (DocuSign, back button).
5. With the team, write a one-page quality scope: environments (DEV/QA/PRO), what the API harness proves, what is still manual in Unqork, and where defects are filed. That becomes the Retirement quality process. Do not import GS regression suites.

## Still unknown

- Team **Ravens** — no SharePoint hits in an earlier org search; not on the Team White home page.
- Whether **Axo** is still the delivery partner.
- 2026 timekeeping tool.
- Whether Confluence `MTP` is still authoritative or SharePoint `TeamWhiteCF` replaced it.
