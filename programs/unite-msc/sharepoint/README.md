# Unite MSC SharePoint publishing pack

**Live parent:** Automation Squad → API Testing Documentation Hub  
**New parent page:** `Unite MSC API Automation`  
**Purpose:** Complete support, KT, onboarding, execution, coverage, and handoff site for Mobile 1, Mobile 2, and Enrollment.

SharePoint is the support-facing publication layer. GitLab `api-test-automation` remains the source of truth for code, suite XML, Maven profiles, Bruno, Postman, SQL, pipeline configuration, and run evidence.

## Authoritative project links

- [API Test Automation repository](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation)
- [Mobile automation folder](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads)
- [Unite MSC Bruno collection for manual API testing](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads)
- [Unite MSC Epic QA-796](https://ascensuscollegesavings.atlassian.net/browse/QA-796)

### Manual test cases (qTest Test Design)

| Module | qTest link |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

The manual test-case links are qTest, not Confluence. qTest is the manual-test system of record; Jira provides delivery traceability; GitLab owns automation code and the Bruno collection.

## Final SharePoint tree

```text
API Testing Documentation Hub
└── Unite MSC API Automation
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

Twelve pages total including the parent. Do not create a separate page for every endpoint, suite, SQL file, Jira story, or Word document.

## How the prompts work

SharePoint Copilot cannot read local files and has a hard 4,000-character prompt limit. Every file in [`copilot/`](./copilot) is self-contained and no longer than 4,000 characters. Paste A, then B, then the remaining letters against the same page where a page is split.

- [ALL-COPILOT-PROMPTS.md](./ALL-COPILOT-PROMPTS.md) — all 42 paste-ready prompts in build order with character counts.

| Order | Page | Prompt |
|---|---|---|
| 0 | Unite MSC API Automation (parent hub) | [00A](./copilot/00A-unite-msc-api-automation-prompt.md) · [00B](./copilot/00B-unite-msc-api-automation-prompt.md) · [00C](./copilot/00C-unite-msc-api-automation-prompt.md) · [00D](./copilot/00D-unite-msc-api-automation-prompt.md) |
| 1 | 01 KT and Onboarding | [01A](./copilot/01A-kt-and-onboarding-prompt.md) · [01B](./copilot/01B-kt-and-onboarding-prompt.md) · [01C](./copilot/01C-kt-and-onboarding-prompt.md) · [01D](./copilot/01D-kt-and-onboarding-prompt.md) |
| 2 | 02 Architecture and Ownership | [02A](./copilot/02A-architecture-and-ownership-prompt.md) · [02B](./copilot/02B-architecture-and-ownership-prompt.md) · [02C](./copilot/02C-architecture-and-ownership-prompt.md) · [02D](./copilot/02D-architecture-and-ownership-prompt.md) |
| 3 | 03 Access, Setup and Environments | [03A](./copilot/03A-access-setup-and-environments-prompt.md) · [03B](./copilot/03B-access-setup-and-environments-prompt.md) · [03C](./copilot/03C-access-setup-and-environments-prompt.md) |
| 4 | 04 Daily Run Playbook | [04A](./copilot/04A-daily-run-playbook-prompt.md) · [04B](./copilot/04B-daily-run-playbook-prompt.md) · [04C](./copilot/04C-daily-run-playbook-prompt.md) |
| 5 | 05 Mobile 1 Automation | [05A](./copilot/05A-mobile-1-automation-prompt.md) · [05B](./copilot/05B-mobile-1-automation-prompt.md) · [05C](./copilot/05C-mobile-1-automation-prompt.md) |
| 6 | 06 Mobile 2 Automation | [06A](./copilot/06A-mobile-2-automation-prompt.md) · [06B](./copilot/06B-mobile-2-automation-prompt.md) · [06C](./copilot/06C-mobile-2-automation-prompt.md) |
| 7 | 07 Enrollment Automation | [07A](./copilot/07A-enrollment-automation-prompt.md) · [07B](./copilot/07B-enrollment-automation-prompt.md) · [07C](./copilot/07C-enrollment-automation-prompt.md) · [07D](./copilot/07D-enrollment-automation-prompt.md) · [07E](./copilot/07E-enrollment-automation-prompt.md) |
| 8 | 08 Coverage, Traceability and Sign-off | [08A](./copilot/08A-coverage-traceability-and-sign-off-prompt.md) · [08B](./copilot/08B-coverage-traceability-and-sign-off-prompt.md) · [08C](./copilot/08C-coverage-traceability-and-sign-off-prompt.md) |
| 9 | 09 Reporting and Troubleshooting | [09A](./copilot/09A-reporting-and-troubleshooting-prompt.md) · [09B](./copilot/09B-reporting-and-troubleshooting-prompt.md) · [09C](./copilot/09C-reporting-and-troubleshooting-prompt.md) |
| 10 | 10 Test Data, DB Refresh and Security | [10A](./copilot/10A-test-data-db-refresh-and-security-prompt.md) · [10B](./copilot/10B-test-data-db-refresh-and-security-prompt.md) · [10C](./copilot/10C-test-data-db-refresh-and-security-prompt.md) |
| 11 | 11 Extend the Automation | [11A](./copilot/11A-extend-the-automation-prompt.md) · [11B](./copilot/11B-extend-the-automation-prompt.md) · [11C](./copilot/11C-extend-the-automation-prompt.md) · [11D](./copilot/11D-extend-the-automation-prompt.md) |

## Workflow diagrams

Ten pages carry an ASCII workflow or communication diagram. Copilot must reproduce each one verbatim inside a monospace block; it must not redraw it as SmartArt or an image.

| Page | Diagram |
|---|---|
| 00 parent hub | Platform at a glance: three modules over the shared framework |
| 02 Architecture | Canonical runtime flow, and the BFF-to-downstream-service communication map |
| 03 Access/Setup | How a run resolves suite, environment, overlay, and branding |
| 04 Daily Playbook | The daily loop from suite choice to failure classification |
| 05 Mobile 1 | Member session and the three-step IDP token flow |
| 06 Mobile 2 | Which downstream service and gateway serves each feature |
| 07 Enrollment | Ordered 12-step wizard, service fan-out per step, subsequent enrollment, encryption chain |
| 09 Troubleshooting | First-failure triage decision tree |
| 10 Test Data | Post-refresh recovery sequence |
| 11 Extend | New-endpoint workflow from intake to done |

## Start here

1. Follow [publishing-runbook.md](./publishing-runbook.md).
2. Upload only the files marked **Upload** in [upload-manifest.md](./upload-manifest.md).
3. Paste 00A–00D against the same page to create the **parent** at the hub root, titled `Unite MSC API Automation` with no prefix.
4. Paste prompts 01–11 in numeric order.
5. Link the pages to each other only after all twelve exist.
6. Complete [publish-validation-checklist.md](./publish-validation-checklist.md).

## Non-negotiable rules

- No Postman environment JSON, host properties, passwords, JWT, certificates, SSN, connection strings, or raw PII.
- Do not upload the entire Git folder.
- Do not place Unite MSC directly under Automation Squad; nest it under the API Testing Documentation Hub.
- Do not claim L5 SQL is implemented. The approved completion boundary is L1–L4.
- Do not invent approver names where sign-off documents contain `[NEED_INPUT]`.
- Keep code, executable collections, SQL, and pipeline files in GitLab; link to them.

## Regenerate the prompts

```powershell
python programs/unite-msc/sharepoint/tools/generate_sharepoint_pack.py
```
