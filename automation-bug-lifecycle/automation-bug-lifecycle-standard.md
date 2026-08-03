# Automation Bug Lifecycle — QA Automation Operating Standard

**Version:** July 24, 2026  
**Scope:** All QA Automation teams — UI, API, performance, any program  
**Repository:** `qa-automation-kb` (single source of truth per `qa-knowledge-base/00_SYSTEM/ROLE.md`)

---

## 1. Purpose

When regression fails — nightly V2 (Jenkins), V3 (GitLab), release, or smoke — teams need a **repeatable, evidence-driven** response:

| Question | Answer source |
|----------|---------------|
| Is this a real defect? | Triage decision tree (Section 2) |
| What evidence do we capture? | Evidence folder (Section 3) |
| How do we communicate? | Cursor Prompt H + leadership-approved templates (Section 4) |
| Who changed the code? | GitLab Project Manager (Section 5) |
| How do we close? | Resolution standard (Section 6) |

This standard is an **operating norm** — applicable to any team going forward.

---

## 2. Triage — Bug or Not?

**Not every failure is a defect.** Triage per `automation-bug-lifecycle/process/TRIAGE_RULES.md` and `automation-bug-lifecycle/process/FLAKINESS_PLAYBOOK.md`.

| Classification | Signals | Action | Log JIRA? |
|----------------|---------|--------|-----------|
| Environment | DB restricted, certs/helm, OKD down | Escalate infra | No |
| Flaky / false failure | Pass on retry; timing; locator | Flakiness playbook | No |
| Automation script | Test logic, wait, data | Fix in automation repo | Optional |
| Functional defect | Reproducible; app trace | Full bug cycle | Yes |

**Critical legitimate defects** may trigger `monolith/main` + `automation/main` lock — 10 AM SLA per Confluence `1a. Managing Monolith Repo Main Branch Locking.pdf`.

---

## 3. Evidence Collection

**Folder:** `automation-bug-lifecycle/evidence/regression-reports/[MMDDYYYY]/`

| Artifact | Example |
|----------|---------|
| Screenshots | `*.png` |
| Exception logs | `*_exception_failedresult.txt` |
| Test data | `Test Data.txt`, `*testcase_information.txt` |
| Console log | GitLab / Jenkins job output |
| Bug documentation | `[MMDDYYYY]_[Feature]_[IssueType].md` |

**Naming:** see `automation-bug-lifecycle/evidence/regression-reports/BUG_REPORTING_PROCESS.md`

---

## 4. Cursor Prompt H

**Location:** `qa-knowledge-base/00_SYSTEM/PROMPTS.md` → section **H) Bug Report: JIRA + Email + Teams**

**Steps:** (full guide in `qa-knowledge-base/05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md`)

1. Place artifacts in evidence folder
2. Copy Prompt H, fill placeholders, attach failure images in Cursor
3. One output file with: JIRA block · failure email · Teams message · resolution placeholder

**Templates:** Teams and email formats are **approved by leadership and senior QA resources**. Use standard To/Cc lists from Confluence Bug Handling PDFs.

---

## 5. GitLab Project Manager — Change Set

**Utility:** `C:\Development\Workspace\GitlabInfoProjUI` (separate repo)

| Step | Action |
|------|--------|
| 1 | Set date range: last green run → failure |
| 2 | Select project: `monolith` first, then `automation`, `qa-automation` |
| 3 | Merge Requests tab → filter Merged |
| 4 | Note: Author, Merged by, source → target branch, Merged At |
| 5 | Commits tab → authors, commit IDs, messages |
| 6 | Export or copy into JIRA / email Change Set section |

**Sample output fields:** MR Title · MR Link · Author · Reviewers · Merged by · Created At · Merged At · Branch flow · MR ID · State

---

## 6. Resolution

Per Confluence `1b. Automation Bug Resolution Follow-Up.pdf`:

1. Dev fixes or reverts
2. QA reruns impacted tests
3. JIRA updated with RCA → Closed
4. Resolution email (same To/Cc as failure)
5. Unlock main if locked
6. Update bug `.md` file

---

## 7. Multi-Failure Rollup

When many tests fail in one run — group by feature/plan, not per test method. See `04202026_DailyRegression_PipelineFailureRollup.md`.

---

## 8. Repository Cross-Reference

| Topic | Path |
|-------|------|
| Prompts | `qa-knowledge-base/00_SYSTEM/PROMPTS.md` |
| Role & constraints | `qa-knowledge-base/00_SYSTEM/ROLE.md`, `CONSTRAINTS.md` |
| Glossary | `qa-knowledge-base/00_SYSTEM/GLOSSARY.md` |
| Defect lifecycle | `automation-bug-lifecycle/process/DEFECT_LIFECYCLE.md` |
| Triage rules | `automation-bug-lifecycle/process/TRIAGE_RULES.md` |
| Flakiness | `automation-bug-lifecycle/process/FLAKINESS_PLAYBOOK.md` |
| RCA | `automation-bug-lifecycle/process/RCA_PROCESS.md` |
| Daily regression | `automation-bug-lifecycle/process/DAILY_REGRESSION.md` |
| Templates | `qa-knowledge-base/06_TEMPLATES/` |
| Bug SOP | `automation-bug-lifecycle/evidence/regression-reports/BUG_REPORTING_PROCESS.md` |
| Confluence exports | `automation-bug-lifecycle/reference/confluence-bug-handling/Bug Handling/` |

---

## 9. Deliverables in this module

| File | Purpose |
|------|---------|
| `deliverables/Automation-Bug-Lifecycle-Standard.pptx` | Standard overview deck |
| `deliverables/Automation-Bug-Lifecycle-Playbook.docx` | Detailed playbook |
| `prompts/`, `templates/`, `scripts/` | **Workflow kit** — triage through resolution |
| `tools/generate_deliverables.py` | Regenerate charts + documents |

```bash
python automation-bug-lifecycle/tools/generate_deliverables.py
```

### Recreate kit (for new users)

| Item | Path |
|------|------|
| Start here | `README.md` |
| Prompts (01–05) | `prompts/` |
| Evidence folder script | `scripts/new-evidence-folder.ps1` |
| Cursor skill | `cursor-kit/SKILL.md` → copy to `.cursor/skills/` |
| GitLab util setup | `reference/gitlab-project-manager-setup.md` |
