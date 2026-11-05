# Team White - local copy of SharePoint (latest content only)

Source: https://ascensus0.sharepoint.com/sites/TeamWhiteCF (exported 2026-11-05). Only current pages were kept; templates, empty containers and obvious scrap were skipped. Passwords/secrets were replaced with `[REDACTED]`. Images remain as SharePoint links; architecture diagrams live in Miro boards linked from the pages.

Team White = middle tier / DOE platform team. Product-level documentation for the Ravens-supported DOE lives in [`../team-ravens/02-doe-product/`](../team-ravens/02-doe-product/README.md).

| Folder | Files | What is inside | Start with |
| --- | --- | --- | --- |
| [`00-overview/`](00-overview/) | 1 | Team home | `Team-White.md` |
| [`01-team-and-ways-of-working/`](01-team-and-ways-of-working/) | 13 | agreements, DoR/DoD, sprint planning, Scrum of Scrums, new-hire setup | `Teamwork-Agreement---Onboarding.md`, `New-Team-Member-Onboarding.md` |
| [`02-doe-product-and-business/`](02-doe-product-and-business/) | 31 | architecture, handoff document, framework, roadmap, PAS/Chorus/Cliff/Salesforce integrations, data dictionaries, environments, artifacts, KT | `Digital-Onboarding-Experience-Handoff-Document.md`, `Architecture.md`, `Useful-Links.md` |
| [`03-dev-and-devops/`](03-dev-and-devops/) | 32 | Kong, RabbitMQ/MassTransit, sagas, OTP/SecureAuth, Hangfire, encryption, tracing, feature flags | `List-of-services.md`, `Onboarding-Workflow-Saga.md`, `SecureAuth-OTP.md` |
| [`04-testing-and-qa/`](04-testing-and-qa/) | 18 | QA testing, Playwright, API strategy, performance, test coverage, access references | `DOE---QA-Testing.md`, `Onboarding-Project-Access-and-Application-Testing-References.md` |
| [`05-unqork/`](05-unqork/) | 5 | Unqork information, registration list, academy, data dump, API test harness | `Unqork-information.md` |
| [`06-releases-and-implementation-plans/`](06-releases-and-implementation-plans/) | 103 | release notes and implementation plans by year | latest 2026 files |
| [`07-background-dca-and-legacy/`](07-background-dca-and-legacy/) | 2 | DCA and older background | |
| [`_index/`](_index/) | 1 | partial page index (releases only) | |

## Reading order for a new QA lead
1. `02-doe-product-and-business/Digital-Onboarding-Experience-Handoff-Document.md` (who/what)
2. `02-doe-product-and-business/Architecture.md`
3. `04-testing-and-qa/DOE---QA-Testing.md` and the access-references page
4. `03-dev-and-devops/Onboarding-Workflow-Saga.md`
5. `05-unqork/Unqork-information.md`

## Known gaps
- Page hierarchy from SharePoint's page tree was not retrievable; folders are grouped by topic.
- Embedded Miro/Figma diagrams, videos and attachments (Excel/PowerPoint/PDF) were not downloaded.
