# 05 Defects and triage

**Purpose:** What to do when nightly or a pipeline is red.  
**Owner:** QA Automation  
**Last reviewed:** 2026-09-03  
**Git:** `programs/sharepoint-qa-hub/pages/05-defects-and-triage.md`

## Start in 2 minutes

1. Triage first — environment vs flake vs script vs product.
2. Evidence folder if it might be a defect.
3. Prompt H only for product defects (Jira + approved email + Teams).

Canonical SOP: Git `automation-bug-lifecycle/` (not the old Confluence defect PDF alone).

## Standard

| Type | Log Jira? |
|------|-----------|
| Environment | No |
| Flaky / false failure | No unless recurring |
| Automation script | Optional |
| Functional defect | Yes |

Do not invent To/Cc lists. Use Prompt H output.

## If it fails

If you cannot classify, stop and ask the squad lead. Do not file a product bug for a bad locator.

## Source

| Kind | Path |
|------|------|
| Canonical | `automation-bug-lifecycle/` |
| Old dump | `00-master-onboarding/5. Defect Management Standards.pdf` |
| KB | `qa-knowledge-base/04_EXECUTION/` |
