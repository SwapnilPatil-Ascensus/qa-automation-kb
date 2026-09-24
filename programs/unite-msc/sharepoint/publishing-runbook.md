# Publishing runbook — Unite MSC API Automation

## 1. Prepare the library

1. Open the **API Testing Documentation Hub** SharePoint site.
2. In Documents, create `Unite MSC API Automation`.
3. Upload the 18 required files in [upload-manifest.md](./upload-manifest.md).
4. Confirm every file opens in SharePoint.
5. Do a filename review before creating pages; remove duplicates and environment files.

## 2. Create the parent page

1. From **API Testing Documentation Hub**, select **New → Site Page**.
2. Title it `Unite MSC API Automation`.
3. Paste [00A](./copilot/00A-unite-msc-api-automation-prompt.md) and publish at the hub root.
4. Paste [00B](./copilot/00B-unite-msc-api-automation-prompt.md), [00C](./copilot/00C-unite-msc-api-automation-prompt.md), and [00D](./copilot/00D-unite-msc-api-automation-prompt.md) against that same page, in order.
5. Confirm the final title is exactly `Unite MSC API Automation` with no prefix.
6. Add it under the API hub navigation.

## 3. Create the child pages

Repeat in numeric order:

1. Create a Site Page with the exact title in [README.md](./README.md).
2. Paste the matching `copilot/*-prompt.md` in full. For 08 and 11, paste A first, then B against the same page.
3. Link approved Word/CSV/XLSX attachments listed in the manifest.
4. Publish under `Unite MSC API Automation`.

Add parent, previous, and next quick links only after all twelve pages exist.

Do not ask Copilot to “fill gaps” or “improve metrics.” It must use the pasted content only.

## 4. Attachment placement

| Page | Primary attachments |
|---|---|
| 01 KT and Onboarding | Enrollment Documentation Index |
| 02 Architecture and Ownership | Enrollment Architecture/Setup |
| 03 Access, Setup and Environments | Enrollment Architecture/Setup |
| 04 Daily Run Playbook | Enrollment Execution/Troubleshooting |
| 05 Mobile 1 | M1 Sign-Off + M1 CSV |
| 06 Mobile 2 | M2 Sign-Off + M2 CSV + endpoint summary |
| 07 Enrollment | Enrollment Sign-Off + coverage matrix/catalog/CSV |
| 08 Coverage, Traceability and Sign-off | Three sign-offs + traceability DOCX/CSV + enhancement backlog |
| 09 Reporting and Troubleshooting | Enrollment Reporting + Execution/Troubleshooting |
| 10 Test Data, DB Refresh and Security | Enrollment DB Refresh Checklist |
| 11 Extend the Automation | Enrollment AI Scenario Guide + enhancement backlog |

## 5. Navigation

Use one nav node for the parent and child links beneath it. Do not add all attachments to left navigation.

```text
API Testing Documentation Hub
  Unite MSC API Automation
    01 KT and Onboarding
    ...
    11 Extend the Automation
```

## 6. Quality review

Run [publish-validation-checklist.md](./publish-validation-checklist.md). At minimum:

- Verify page titles and hierarchy.
- Verify no credentials or environment JSON.
- Verify GitLab links point to the canonical repo.
- Verify 26 M1, 24 in-scope M2, and 25/28 Enrollment are presented with their scope qualifiers.
- Verify L5 SQL says analysis/future enhancement, not implemented.
- Verify `[NEED_INPUT]` approvals were not silently replaced.
- Ask a second engineer to complete the “find → run → report → troubleshoot” path.

## 7. Maintenance

- Update Git first, then regenerate this pack and update SharePoint.
- Page owner reviews links quarterly and after repository/profile changes.
- Coverage numbers require a source CSV and review date.
- Superseded attachments are versioned/replaced in the same library; do not create `final-v2-final` copies.
- Use SharePoint version history rather than duplicate pages.
