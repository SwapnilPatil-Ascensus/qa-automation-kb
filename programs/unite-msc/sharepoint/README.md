# Unite MSC SharePoint publishing pack

**Live parent:** Automation Squad → API Testing Documentation Hub  
**New parent page:** `Unite MSC API Automation`  
**Purpose:** Complete support, KT, onboarding, execution, coverage, and handoff site for Mobile 1, Mobile 2, and Enrollment.

SharePoint is the support-facing publication layer. GitLab `api-test-automation` remains the source of truth for code, suite XML, Maven profiles, Bruno, Postman, SQL, pipeline configuration, and run evidence.

## Authoritative project links

- [API Test Automation repository](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation)
- [Mobile automation folder](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads)
- [Unite MSC Bruno collection for manual API testing](https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads)
- [Manual test cases in qTest Test Design](https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign)
- [Unite MSC Epic QA-796](https://ascensuscollegesavings.atlassian.net/browse/QA-796)

The manual test-case link is qTest, not Confluence. qTest is the manual-test system of record; Jira provides delivery traceability; GitLab owns automation code and the Bruno collection.

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

SharePoint Copilot cannot read local files and has a hard 4,000-character prompt limit. Every file in [`copilot/`](./copilot) is self-contained and no longer than 4,000 characters. Paste A, then B, then C/D against the same page where a page is split.

- [ALL-COPILOT-PROMPTS.md](./ALL-COPILOT-PROMPTS.md) — all 17 paste-ready prompts in build order with character counts.

| Order | Page | Prompt |
|---|---|---|
| 0 | Unite MSC API Automation (parent hub) | [00A](./copilot/00A-unite-msc-api-automation-prompt.md) · [00B](./copilot/00B-unite-msc-api-automation-prompt.md) · [00C](./copilot/00C-unite-msc-api-automation-prompt.md) · [00D](./copilot/00D-unite-msc-api-automation-prompt.md) |
| 1 | 01 KT and Onboarding | [Prompt](./copilot/01-kt-and-onboarding-prompt.md) |
| 2 | 02 Architecture and Ownership | [Prompt](./copilot/02-architecture-and-ownership-prompt.md) |
| 3 | 03 Access, Setup and Environments | [Prompt](./copilot/03-access-setup-and-environments-prompt.md) |
| 4 | 04 Daily Run Playbook | [Prompt](./copilot/04-daily-run-playbook-prompt.md) |
| 5 | 05 Mobile 1 Automation | [Prompt](./copilot/05-mobile-1-automation-prompt.md) |
| 6 | 06 Mobile 2 Automation | [Prompt](./copilot/06-mobile-2-automation-prompt.md) |
| 7 | 07 Enrollment Automation | [Prompt](./copilot/07-enrollment-automation-prompt.md) |
| 8 | 08 Coverage, Traceability and Sign-off | [08A](./copilot/08A-coverage-traceability-and-sign-off-prompt.md) · [08B](./copilot/08B-coverage-traceability-and-sign-off-prompt.md) |
| 9 | 09 Reporting and Troubleshooting | [Prompt](./copilot/09-reporting-and-troubleshooting-prompt.md) |
| 10 | 10 Test Data, DB Refresh and Security | [Prompt](./copilot/10-test-data-db-refresh-and-security-prompt.md) |
| 11 | 11 Extend the Automation | [11A](./copilot/11A-extend-the-automation-prompt.md) · [11B](./copilot/11B-extend-the-automation-prompt.md) |

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
