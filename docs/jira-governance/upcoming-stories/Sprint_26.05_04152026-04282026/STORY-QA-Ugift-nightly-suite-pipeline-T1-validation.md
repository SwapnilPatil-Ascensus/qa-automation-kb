# Story (draft) — Ugift — Nightly suite + pipeline + day-after validation

**KB path:** `docs/jira-governance/upcoming-stories/Sprint_26.05_04152026-04282026/STORY-QA-Ugift-nightly-suite-pipeline-T1-validation.md`  
**Sprint pack:** [README.md](README.md) · [SPRINT-26.05-jira-import.csv](SPRINT-26.05-jira-import.csv)

**Jira key after create:** `QA-________`

| Field | Suggested value |
|-------|-----------------|
| **Summary** | `[V2][Ugift][Pipeline] Nightly suite — wire CSR+Member Ugift jobs + T+1 validation` |
| **Issue type** | Story |
| **Project** | QA — QA Automation |
| **Assignee** | Swapnil Patil *(pipeline / regression ownership; adjust if Venkatesh owns end-to-end)* |
| **Priority** | Medium |
| **Story points** | 3 *(suite XML + Jenkins/GitLab change + 2 nightly triage cycles)* |
| **Labels** | `automation`, `v2`, `ugift`, `jenkins`, `gitlab`, `regression`, `dailyrun`, `qa-board-view` |
| **Relates to** | [QA-626](https://ascensuscollegesavings.atlassian.net/browse/QA-626) — CSR Ugift post-spike · [QA-627](https://ascensuscollegesavings.atlassian.net/browse/QA-627) — Member Ugift post-spike |
| **Optional** | [QA-728](https://ascensuscollegesavings.atlassian.net/browse/QA-728) — if reopened/superseded for *general* flaky hardening; **this** Story stays scoped to **Ugift** pipeline + first nights only |

---

## 1. Description (paste into Jira)

```text
h2. Purpose
Complete the *release* foot-print for Ugift after implementation Stories QA-626 (CSR) and QA-627 (Member): define or extend the *regression suite*, add Ugift scenarios to the *nightly* job, and *validate* results the *next calendar day* (and subsequent night if hotfixes needed).

h2. Context
* QA-626 / QA-627 deliver automated Ugift flows (post-spike S2605-03).
* Remaining work: suite composition, CI job wiring, first overnight run(s), triage, flake/doc handoff — often not fully captured inside dev-only Stories.

h2. Scope
* *In:* TestNG/Ant suite file(s) or tag groups that *only* include merged Ugift CSR + Member tests; naming aligned to prime-test-automation conventions (**Needs Validation** exact paths).
* *In:* Update nightly regression pipeline (Jenkins and/or GitLab — **Needs Validation**) to invoke the Ugift suite or include agreed tags in existing nightly target.
* *In:* **T+1 validation** — morning after each nightly: open report, classify failures (product vs data vs env vs flake), log defects, open follow-up if QA-728-style hardening is needed.
* *Out:* New Ugift *business* scenarios (belongs in QA-626/627 or new feature Stories).

h2. Dependencies
* **Blocked until** QA-626 and QA-627 (or agreed subset) merged to branch the nightly job tracks.
* Job name + report URL pattern from program (**Needs Validation**).

h2. Definition of Done (summary)
See Acceptance Criteria; worklog on this Story for suite + pipeline + triage time.
```

---

## 2. Acceptance criteria

```markdown
- [ ] **Suite artifact:** Documented TestNG suite XML / Ant target / tag list that runs **Ugift CSR + Member** merged tests only (or clearly named combined suite); path or MR link in Story comment.
- [ ] **Nightly wired:** Pipeline config MR merged; Ugift suite **runs** as part of nightly (or dedicated nightly child job linked from parent); **first** successful scheduled run URL captured.
- [ ] **T+1 validation (minimum 2 nights):** For **each** of the first **two** post-merge nightlies: comment with date, job URL, pass/fail, triage table (test → category → Jira key if defect).
- [ ] **No silent noise:** Any flake &gt; agreed threshold has a **linked** follow-up (e.g. spike or QA-728 family) or stabilization MR; none left unlogged.
- [ ] **Stakeholder ping:** One-line summary on QA-626 or QA-627 (or team channel) — “Ugift on nightly as of &lt;date&gt;”.
```

---

## 3. T+1 triage checklist (copy per night)

| Check | Done |
|-------|------|
| Job completed (not aborted) | ☐ |
| Ugift tests discovered count matches suite expectation | ☐ |
| Failures: each has category (Defect / Data / Env / Flake / Unknown) | ☐ |
| Compare vs prior night for same failure signature | ☐ |
| Attach or link HTML / Jenkins console artifact | ☐ |

---

## 4. CSV import row

Same row exists in `SPRINT-26.05-jira-import.csv`; re-import only if your Jira allows duplicate-safe merge.

---

## 5. Changelog

| Date | Note |
|------|------|
| 2026-05-12 | Drafted; ties to board QA-626 / QA-627 and nightly follow-through. |
