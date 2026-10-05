# [UNITE-MSC][SharePoint] Publish Unite MSC API Automation support & KT site

**Epic:** [QA-796](https://ascensuscollegesavings.atlassian.net/browse/QA-796)  
**Assignee:** Swapnil Patil  
**Suggested story points:** **5**  
**Labels:** `QA-Board-View` · `UNITE-MSC` · `SharePoint` · `documentation` · `KT`

---

## Summary (Jira title)

`[UNITE-MSC][SharePoint] Publish Unite MSC API Automation hub — support, KT, and operating docs`

---

## Description

### Context

Unite MSC API automation (Mobile 1, Mobile 2, and Enrollment) is delivered in GitLab. Teams need a single published place on SharePoint for knowledge transfer, onboarding, daily execution, coverage/sign-off, troubleshooting, and how to extend the suite — without relying on private chat history.

This story publishes that documentation under **API Testing Documentation Hub**.

**Systems of record (stated on the site):**
- **GitLab** — automation code, suites, Bruno collection (executable source of truth)
- **qTest** — manual test cases
- **Jira** — delivery tracking (Epic QA-796)
- **SharePoint** — operating guidance and KT (this deliverable)

### User outcome

Anyone on the Automation Squad (or supporting engineers) can open the SharePoint hub and: onboard, run suites safely, find coverage/sign-off, triage failures, and know how to extend automation — without asking for private walkthroughs.

### In scope

- Create and publish the parent page and eleven child pages under **API Testing Documentation Hub** (structure below).
- Link GitLab repo / mobile folder / Bruno collection, Epic QA-796, and the four qTest manual modules.
- Attach approved support artifacts (sign-off docs, endpoint/coverage matrices, handoff checklists) in the document library and link them from the right pages.
- Keep secrets out of SharePoint (no passwords, tokens, certificates, connection strings, or raw PII).
- Document the approved validation bar: **L1–L4 required**; L5 SQL reconciliation is optional / not the completion gate.
- Peer walkthrough to confirm a second person can use the site end-to-end.

### Out of scope

- New automation coding or suite changes in GitLab (separate stories).
- Claiming L5 SQL field reconciliation as implemented.
- Putting credentials or environment secrets on SharePoint pages.

### SharePoint folder / page structure

```text
API Testing Documentation Hub
└── Unite MSC API Automation                    (parent hub)
    ├── 01 KT and Onboarding
    ├── 02 Architecture and Ownership
    ├── 03 Access, Setup and Environments
    ├── 04 Daily Run Playbook
    ├── 05 Mobile 1 Automation
    ├── 06 Mobile 2 Automation
    ├── 07 Enrollment Automation
    ├── 08 Coverage, Traceability and Sign-off
    ├── 09 Reporting and Troubleshooting
    ├── 10 Test Data, DB Refresh and Security
    └── 11 Extend the Automation
```

### What each page covers

| Page | Purpose |
|---|---|
| **Unite MSC API Automation** (parent) | Hub overview, Quick Links, modules at a glance, validation bar (L1–L4), links to GitLab / Bruno / qTest / QA-796 |
| **01 KT and Onboarding** | Prerequisites, first-time setup, build/run path, standards, definition of done for onboarding |
| **02 Architecture and Ownership** | Runtime flow, BFF-to-service map, module ownership |
| **03 Access, Setup and Environments** | Access, local setup, environments/plans (OKD / NYD / NMD), safe config practices |
| **04 Daily Run Playbook** | How to pick a suite, run it, read the report, classify failures |
| **05 Mobile 1 Automation** | Mobile 1 scope, endpoints, suites, sign-off links |
| **06 Mobile 2 Automation** | Mobile 2 scope, endpoints, suites, sign-off links |
| **07 Enrollment Automation** | Enrollment wizard flow, coverage, sign-off and handoff links |
| **08 Coverage, Traceability and Sign-off** | Coverage matrices, legacy-to-canonical traceability, sign-off status |
| **09 Reporting and Troubleshooting** | Report location, triage tree (env / data / automation / product) |
| **10 Test Data, DB Refresh and Security** | Data expectations, post-refresh checklist, security rules |
| **11 Extend the Automation** | How to add a new endpoint end-to-end (intake → code → suite → review) |

### Authoritative links (to publish on the parent)

| Resource | URL |
|---|---|
| Unite MSC Epic | https://ascensuscollegesavings.atlassian.net/browse/QA-796 |
| API Test Automation (GitLab) | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation |
| Mobile automation folder | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile |
| Unite MSC Bruno collection | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection |
| qTest — Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| qTest — MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| qTest — MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| qTest — MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

---

## Acceptance Criteria

- [ ] Parent page **Unite MSC API Automation** published under **API Testing Documentation Hub**
- [ ] Exactly **11** child pages published (01–11) matching the structure above
- [ ] Parent links to every child; each child links back to the parent
- [ ] Parent Quick Links include GitLab, Bruno, Epic QA-796, and all four qTest modules
- [ ] Module pages (05–07) link to sign-off / coverage artifacts in the document library
- [ ] Coverage / sign-off page (08) links matrices and formal sign-off docs
- [ ] Site states clearly: SharePoint = guidance; GitLab = code; qTest = manual cases; Jira = delivery
- [ ] Validation bar documented as **L1–L4 required**; L5 called out as optional / not the gate
- [ ] No passwords, tokens, certificates, connection strings, or raw PII on any page or attachment
- [ ] A second person (not the author) can complete: find module → find run guidance → find report/triage → find how to extend — without private chat help
- [ ] Story comment includes the live SharePoint parent URL

---

## Definition of Done

- All acceptance criteria met
- Site is usable for KT, daily run, triage, and extension without the author present
- Publish comment on this Story with parent URL and confirmation that security rules were followed
- Story closed; any missing SME names or follow-ups tracked as linked work (not left silent)

---

## Paste-ready for Jira Cloud

### Description

```
Context
Unite MSC API automation (Mobile 1, Mobile 2, Enrollment) is in GitLab. This story publishes the support / KT / operating documentation on SharePoint under API Testing Documentation Hub so the team can onboard, run, triage, and extend without private chat history.

Systems of record
• GitLab — automation code and Bruno (executable source of truth)
• qTest — manual test cases
• Jira — delivery (Epic QA-796)
• SharePoint — operating guidance (this deliverable)

Outcome
Published hub with 1 parent + 11 child pages, Quick Links to GitLab / Bruno / qTest / QA-796, approved sign-off and coverage artifacts attached, L1–L4 validation bar documented, no secrets on SharePoint.

SharePoint structure
API Testing Documentation Hub
└── Unite MSC API Automation                    (parent)
    ├── 01 KT and Onboarding
    ├── 02 Architecture and Ownership
    ├── 03 Access, Setup and Environments
    ├── 04 Daily Run Playbook
    ├── 05 Mobile 1 Automation
    ├── 06 Mobile 2 Automation
    ├── 07 Enrollment Automation
    ├── 08 Coverage, Traceability and Sign-off
    ├── 09 Reporting and Troubleshooting
    ├── 10 Test Data, DB Refresh and Security
    └── 11 Extend the Automation

Page purpose (summary)
• Parent — hub overview, Quick Links, L1–L4 bar, links to GitLab / Bruno / qTest / QA-796
• 01 — KT / first-time setup / onboarding DoD
• 02 — architecture, ownership, service map
• 03 — access, environments, plans (OKD / NYD / NMD), safe setup
• 04 — daily run playbook (choose suite → run → report → classify)
• 05 / 06 / 07 — Mobile 1, Mobile 2, Enrollment scope + suites + sign-off links
• 08 — coverage, traceability, sign-off
• 09 — reporting and troubleshooting
• 10 — test data, DB refresh, security rules
• 11 — how to extend the automation

Out of scope
New coding in GitLab; claiming L5 SQL as implemented; publishing credentials or PII.
```

### Acceptance Criteria

```
( ) Parent "Unite MSC API Automation" under API Testing Documentation Hub
( ) Exactly 11 child pages 01–11 in the approved structure; parent↔child links live
( ) Quick Links: GitLab, Bruno, QA-796, and four qTest modules
( ) Sign-off / coverage artifacts linked from module and coverage pages
( ) L1–L4 documented as required; L5 optional / not the completion gate
( ) No secrets or PII on pages or attachments
( ) Second-person walkthrough passes (onboard → run → triage → extend)
( ) Story comment has live SharePoint parent URL
```

### Definition of Done

```
( ) All AC met
( ) Site usable for KT / run / triage / extend without the author present
( ) Publish comment with parent URL; security rules followed
( ) Story closed; follow-ups linked if any
```
