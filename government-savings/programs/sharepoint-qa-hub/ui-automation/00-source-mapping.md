# Old Master Onboarding tree → UI Automation Hub

Screenshot + local PDFs (`00-master-onboarding/`, `general-dod-dor-jira/`). Same names as SharePoint children of `GSSD-00.-QA-Automation---Master-Onboarding-Guide-310458333.aspx`.

## Consolidate (do not republish 1:1)

| Old page (SharePoint / PDF name) | New live page |
|----------------------------------|---------------|
| 00. QA Automation - Master Onboarding Guide | **01 Start Here** (syllabus only) + hub cards |
| 00. AM Squad: Individual Onboarding (person trackers) | **Archive** — checklist pattern reused on 01, names/dates stay archive |
| 01. QA Automation - Charter & Squad Purpose | **AM Squad Team** (already exists). One sentence on hub. Not a UI page. |
| 02. Environment Access & Setup | **02 Environment & Access** |
| 02a. Environment: General Environment setup | **02** (Putty/Frogger/SQL Developer steps) |
| 2.1.1 PuTTY/Linux Stage 1 | **02** (Freshservice Linux form) |
| 2.1.2 Oracle / 2.1.3 SQL Server | **02** (short rows) + **08 Reference** for extra screenshots |
| 03. Tech Stack & Tooling Overview | **03 Framework Setup** (UI tools only) |
| 03a. GitLab Setup & Project Cloning | **03** |
| 03b. IntelliJ Local Setup parent + 3.2.1 V2 Ant + 3.2.2 V3 Maven | **03** (two short sections: V2 vs V3) |
| 03c. Eclipse | **08 Reference** (legacy). IntelliJ is default. |
| Cursor AI PRIME V3 Local Setup | **03** (V3 subsection) |
| 7. Prime Automation Framework v2 Developer Guide | **03** entry + **08** for deep pages |
| 04A. Best Practices & Standards Manual | **04 Development Standards** |
| 04a. Naming & Folder Structure | **04** |
| 04b. QA GitLab Standards | **04** |
| 04B. GS Automation KT Video Follow-Up Tracker | **06 KT Center** (index + links, not 20 video pages) |
| 05. Defect Management Standards | **07 Defect Management** + Git `automation-bug-lifecycle/` |
| 06. DRAFT 4-Week Execution Roadmap | **01 Start Here** (Day 1 / Week 1 / Week 2). Drop “DRAFT” novel. |
| 06a. DRAFT Testing Workflow Full Lifecycle | **05 Execution Workflow** |
| 1. Automation Testing DoR | **05** |
| 2. Automation Testing DoD | **05** |
| 3. JIRA Kanban QA Project KT | **05** + **06** |

## Leave out of UI hub (other hubs or Archive)

| Content in old Master Onboarding | Where it belongs |
|----------------------------------|------------------|
| Taurus, bzt, JMeter, BlazeMeter, New Relic (perf) | Performance Engineering Hub |
| Rancher / Helm / K8s | Performance / DevOps — not Day-1 UI |
| API Postman/Newman as primary | API Testing Hub (link only) |
| Mobile / VS Code mobile setup | Mobile Automation Hub |
| Hiring, 4-week Sr Engineer essay | Archive |
| Individual named onboarding tables (Venkatesh, Sagar, …) | Archive |
| RT mailbox instructions | Archive — replace with Freshservice |

## Freshservice (current)

Old PDFs still say RT / `uii-access@rt.acs529.com`. Live process:

| Need | How (from dump + later trackers) |
|------|----------------------------------|
| Local admin | Freshservice → Request a Service → Security → **Local Admin Request** |
| Linux / PuTTY / Frogger | Freshservice catalog **Linux User Account Creation**. Server `gwtpsshrelay01` (aliases `sshrelaywt1`, `frogger`). Group offshore `satellite(8000)`. Mirror `swpatil`. |
| GitLab | Freshservice **Gitlab_Users**. SSO + 2FA + SSH. Clone dest `C:\Workspace\Gitlab\Automation` |
| Jira / Tempo / qTest / Jenkins / L: drive / VM | Freshservice. Mirror Swapnil Patil (or assigned buddy). qTest projects: Automation Unite, Automation Astro, Astro, Unite Platform, Entity Management, GS-Delivery |
| CSR app | Email `csapppermission@ascensus.com`, CC manager, list Stage1/2/PROD links, name who to mirror |

Exact Freshservice item URLs: `[NEED_INPUT]` — paste catalog links on page 02 when you have them.

## UI stack (from 03 Tech Stack PDF — keep)

- Java **17**, Maven **3.9+**, Ant **1.9.6** (V2 only)
- Selenium, TestNG, Cucumber
- IDE: **IntelliJ** default; Cursor for V3; Eclipse archive
- Copy tools from `L:\...\UII-QA\Cucumber_Automation\automation-env` when L: is granted
- GitLab: `ascensus-gs/products/depot/automation` (V2 family) and `.../qa-automation/prime-test-automation` (V3)

## GitLab merge rules (from 04b — keep on page 04)

- Never commit to `main`
- Branch: `STORY-1234-short-description`
- Two approvals; reviewers include Nick / Pallavi / Swapnil / Santiago (no self-review of own commits)
- Rebase onto `main` before merge
