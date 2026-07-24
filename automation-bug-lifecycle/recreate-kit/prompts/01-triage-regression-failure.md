# Prompt 01 — Triage Regression Failure

**When:** A regression run reports new failure(s). Run this **before** logging JIRA.

**Copy everything below the line into Cursor. Fill `[PLACEHOLDERS]`. Attach failure screenshot if available.**

---

```
Triage assistant — regression failure.

Use ONLY these repo sources for rules:
- 04_EXECUTION/TRIAGE_RULES.md
- 04_EXECUTION/FLAKINESS_PLAYBOOK.md
- 04_EXECUTION/DAILY_REGRESSION.md
- automation-bug-lifecycle/automation-bug-lifecycle-standard.md (Section 2)

**Inputs:**
- Failure date/time: [FILL]
- Last known green run: [FILL]
- Suite: [V2 Jenkins / V3 GitLab / release / smoke]
- Environment: [e.g. Stage1, QC4]
- Feature/area: [FILL]
- Error summary (paste exception if available): [FILL or paste]
- TestNG or CI report URL: [FILL]
- Retry result (if rerun): [passed / failed / not run]

**Tasks:**
1. Classify as ONE of: Environment | Flaky/False failure | Automation script issue | Functional defect
2. List signals that support the classification (bullet table)
3. State clearly: **Log JIRA?** Yes / No / Optional
4. If Functional defect → list next 5 actions (evidence folder, Prompt H, GitLab change set, etc.)
5. If Environment or Flaky → list recommended action only (no full bug cycle)
6. If critical legitimate defect → note main-branch lock criteria (10 AM SLA)

**Output format:**
- Classification (one line, bold)
- Signal table (2 columns)
- Recommended next steps (numbered)
- Do NOT invent facts — use [NEED_INPUT] for missing data

Do not create JIRA content yet unless classification is Functional defect and user asks to proceed to Prompt H.
```
