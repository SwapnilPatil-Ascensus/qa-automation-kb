# Automation Bug Lifecycle — End-to-End Workflow

**Purpose:** Shell guide for running the full regression-failure workflow using this repo, Cursor AI, and GitLab Project Manager.  
**Audience:** QA Automation engineers presenting or adopting the standard.  
**Time:** ~15 minutes per real defect (after triage confirms it is not env/flaky).

---

## What this solves

| Challenge | How this workflow addresses it |
|-----------|-------------------------------|
| **Visibility** — who changed what between last green run and failure | GitLab Project Manager change-set report |
| **Consistency** — every failure communicated the same way | Leadership-approved email/Teams templates via Prompt H |
| **Repeatability** — tribal knowledge, ad-hoc JIRA | One evidence folder + one prompt → all deliverables |
| **Accountability** — critical defects stall the pipeline | Main-branch lock; responsible party responds; 24-hour resolution target |

---

## Repository map (what lives where)

```
automation-bug-lifecycle/
├── evidence/regression-reports/MMDDYYYY/   ← DROP ZONE (screenshots, logs, reports)
├── prompts/                              ← Cursor prompts 01–05
│   ├── 01-triage-regression-failure.md
│   ├── 02-bug-report-prompt-h.md         ← Prompt H (JIRA + email + Teams)
│   ├── 03-gitlab-change-set.md
│   ├── 04-resolution-email.md
│   └── 05-multi-failure-rollup.md
├── process/                              ← Rules (triage, flakiness, lifecycle, RCA)
├── scripts/new-evidence-folder.ps1       ← Bootstrap dated evidence folder
├── cursor-kit/SKILL.md                   ← Copy to .cursor/skills/ (one-time)
├── reference/gitlab-project-manager-setup.md
├── assets/                               ← Workflow charts + GitLab PM screenshots
├── deliverables/                         ← Playbook DOCX + presentation PPTX
└── WORKFLOW.md                           ← This file
```

**KB cross-reference:** `qa-knowledge-base/00_SYSTEM/PROMPTS.md` section **H** (master Prompt H).

---

## Phase 0 — One-time setup

```powershell
# 1. Open repo in Cursor
cd C:\Workspace\GitLab\qa-automation-kb

# 2. Copy Cursor skill (once per machine)
#    cursor-kit/SKILL.md → .cursor/skills/automation-bug-lifecycle/SKILL.md

# 3. Clone & run GitLab Project Manager (separate repo)
#    See: reference/gitlab-project-manager-setup.md
#    Backend: http://localhost:8000/health
#    Frontend: http://localhost:3000
```

---

## Phase A — Detect & triage (~15 min)

**Trigger:** V2 Jenkins or V3 GitLab regression fails.

1. Record **failure timestamp** and **last known green run** date/time.
2. Open the CI report (TestNG / GitLab job).
3. Run triage — use `prompts/01-triage-regression-failure.md` or `process/TRIAGE_RULES.md`.

| Result | Next step |
|--------|-----------|
| **Environment** (DB, certs, OKD) | Escalate infra — **stop, no JIRA** |
| **Flaky / false failure** | `process/FLAKINESS_PLAYBOOK.md` — **stop, no JIRA** |
| **Automation script issue** | Fix in automation repo — optional JIRA |
| **Functional defect** | Continue to Phase B |

```text
┌─────────────┐     ┌─────────┐     ┌──────────┐     ┌─────────────────┐
│   Detect    │ ──► │ Triage  │ ──► │ Env/     │ ──► │ Fix locally /   │
│  (CI fail)  │     │         │     │ Flaky?   │     │ escalate — DONE │
└─────────────┘     └─────────┘     └────┬─────┘     └─────────────────┘
                                           │ Real defect
                                           ▼
                                    Continue ▼
```

---

## Phase B — Collect evidence (~10 min)

```powershell
.\automation-bug-lifecycle\scripts\new-evidence-folder.ps1 `
  -Date 07242026 `
  -Feature UniversalEnrollment
```

**Copy into the dated folder:**

| Artifact | Example |
|----------|---------|
| Screenshots | `failure_step3.png` |
| Exception log | `*_exception_failedresult.txt` |
| Console / CI log | GitLab job output or Jenkins console |
| Test data | `Test Data.txt` |
| Report URL | TestNG or GitLab job link |

Folder path example: `automation-bug-lifecycle/evidence/regression-reports/07242026/`

---

## Phase C — Cursor Prompt H → all communications (~5 min)

**What Prompt H does (plain English):**  
You give Cursor the failure facts and attach screenshots. It writes **one markdown file** containing a JIRA copy-paste block, a failure email draft, a Teams message, and a resolution email placeholder — all using leadership-approved formats.

1. Open `prompts/02-bug-report-prompt-h.md`.
2. Fill placeholders: date, feature, error, report URL, folder path, file list, last green run.
3. **Attach failure screenshots** in the Cursor chat.
4. Paste the prompt block and run.

**Output:** `[MMDDYYYY]_[Feature]_[IssueType].md` in the evidence folder.

Example reference: `evidence/regression-reports/04202026/04202026_UniversalEnrollment_ElementClickIntercepted_KIS.md`

---

## Phase D — JIRA + notify (~10 min)

1. Create JIRA on QA board — paste the **JIRA block** from the generated `.md`.
2. Attach screenshots from the evidence folder.
3. **Send failure email** — copy from generated `.md` (leadership-approved To/Cc — do not improvise).
4. **Post Teams message** — copy from generated `.md`; include JIRA link + report link.

**If critical legitimate defect:**

- Lock `monolith/main` + `automation/main` per Confluence locking policy.
- Responsible party must respond immediately.
- **Resolution target: within 24 hours** (revert or fix + verified regression).

---

## Phase E — Change set (~15 min)

**Tool:** GitLab Project Manager (`GitlabInfoProjUI` — local utility, read-only GitLab API).

1. Set **date range:** last green run → failure date.
2. Query **monolith** first → Merge Requests (Merged) + Commits.
3. Repeat for **automation**, **qa-automation** if needed.
4. Copy or export results.
5. Optional: run `prompts/03-gitlab-change-set.md` in Cursor to format a summary.
6. Paste **Change Set** section into JIRA comment and/or failure email.

**When JIRA exists:** paste the JIRA link + change-set extract back into Cursor to polish the update comment or email addendum.

```text
Evidence folder ──► Prompt H ──► JIRA + Email + Teams
                                      │
GitLab PM (date range) ──► Change set ─┘
                                      │
                              Update JIRA / email
```

---

## Phase F — Resolution (when fix lands)

1. Dev delivers fix or revert on affected branch.
2. QA reruns impacted scenarios.
3. JIRA: RCA documented → Verified → Closed.
4. Run `prompts/04-resolution-email.md` or fill **Resolution** section in the bug `.md`.
5. Send resolution email (same To/Cc as failure).
6. **Unlock** `monolith/main` + `automation/main` if locked.
7. Update bug `.md`: JIRA link, Status: Closed.

---

## Multi-failure nights

When many tests fail (e.g. 62/358), do **not** open one JIRA per test.

1. Use `prompts/05-multi-failure-rollup.md`.
2. Group by feature/plan with a failure matrix.
3. One JIRA per root cause (umbrella + children when needed).
4. Single combined email/Teams.

Example: `evidence/regression-reports/04202026/04202026_DailyRegression_PipelineFailureRollup.md`

---

## Quick command reference

| Action | Command / path |
|--------|----------------|
| New evidence folder | `scripts/new-evidence-folder.ps1 -Date MMDDYYYY -Feature Name` |
| Triage prompt | `prompts/01-triage-regression-failure.md` |
| Bug report (Prompt H) | `prompts/02-bug-report-prompt-h.md` |
| Change set format | `prompts/03-gitlab-change-set.md` |
| Resolution email | `prompts/04-resolution-email.md` |
| Rollup (many failures) | `prompts/05-multi-failure-rollup.md` |
| Regenerate PPT/DOCX | `python automation-bug-lifecycle/tools/generate_deliverables.py` |
| Checklist | `QUICK-START.md` |

---

## Presentation deliverables

| File | Use |
|------|-----|
| `deliverables/Automation-Bug-Lifecycle-Standard.pptx` | Team / leadership walkthrough |
| `deliverables/Automation-Bug-Lifecycle-Playbook.docx` | Detailed reference document |
| `assets/chart_*.png` | Workflow, triage, lifecycle diagrams |

Superseded versions: `deliverables/archive/`
