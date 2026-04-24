# Platform Support Epic — Story drafts (Q2 · AMSQUAD Sprint 26.05 onwards)

**Epic name (paste in Jira Epic):**  
`Platform Support — AMSQUAD Sprint Q2 26.05 onwards`

**Reference export (labels, QA project, parent patterns):**  
`docs/jira-governance/data/Platform-support-jira-export.csv`

**Story points:** **Do not estimate** — leave **Story Points** / **Story point estimate** **empty** (or team convention **0** for capacity-only work). Same for **T-shirt** if unused.

**Suggested labels (all stories):**  
`platform-support` · `AMSQUAD` · `QA-Board-View` · `capacity` · `regression` (where applicable)

**Suggested components:** QA Automation · Platform / Operations (match your Jira catalog)

**Issue type:** **Story** (or **Task** if your board treats platform work as tasks only)

---

## Story 1 — Daily regression review & triage (V2 + V3)

### Summary (copy)

```
[Platform Support] Daily regression review & triage — V2 + V3 (Q2 26.05+)
```

### Description (copy)

```markdown
h2. Purpose
Ongoing *platform support* for overnight **Prime V2** and **Prime V3** automation: open latest scheduled pipelines, review Surefire/TestNG, categorize failures (legit vs flaky vs env/data), post status to squad channels, and log time for visibility.

h2. Scope
* Business-day cadence per AMSQUAD agreement (e.g. offshore morning triage).
* Link latest TestNG index, job IDs, qTest where used; escalate per bug-handling process.

h2. Out of scope
* Feature development (separate Stories). Root-cause *fixes* in app code owned by dev teams — link bugs.

h2. Notes
* Align structure with existing parent work in export (e.g. daily regression health check pattern under `Platform-support-jira-export.csv`).
```

### Acceptance criteria (copy)

```markdown
* ( ) Each business day in scope: latest *V2* and *V3* overnight jobs located and opened.
* ( ) Failures summarized (module/plan); *legit* vs *flake/env* noted in Story **comment** or linked sub-tasks.
* ( ) Teams / email per process when failures need PL visibility; links attached.
* ( ) Time **logged** to this Story (or child Sub-tasks) for transparency.
```

---

## Story 2 — Weekly regression summary, tagging & reporting

### Summary (copy)

```
[Platform Support] Weekly regression summary, tagging & reporting (Q2 26.05+)
```

### Description (copy)

```markdown
h2. Purpose
Consolidate week-over-week regression health: pass/fail trends, tagging hygiene, brief summary for chapter or leadership as required.

h2. Scope
* Aggregate from daily triage notes; update tags/labels in Jira where needed; optional Confluence or dashboard snippet.

h2. Cadence
* Weekly (define day with SM — e.g. Friday EOD offshore).
```

### Acceptance criteria (copy)

```markdown
* ( ) One weekly summary posted (Story comment, Teams, or Confluence link) covering V2/V3 highlights.
* ( ) Open *blockers* or *repeat flakes* called out with Jira keys.
* ( ) Tagging / board cleanup actions completed or deferred with reason.
```

---

## Story 3 — Tech meetings & engineering alignment

### Summary (copy)

```
[Platform Support] Tech meetings & engineering alignment (Q2 26.05+)
```

### Description (copy)

```markdown
h2. Purpose
Capacity for **tech chapter**, **program**, **architecture**, **security**, or **release readiness** meetings where AMSQUAD provides automation/regression perspective — not tied to a single feature Epic.

h2. Scope
* Attend agreed recurring forums; capture action items affecting automation, data, or pipelines; follow up or delegate.

h2. Out of scope
* Replacing SM/PO for decisions — *input only* unless delegated.
```

### Acceptance criteria (copy)

```markdown
* ( ) Recurring meetings listed in Story **description** or first comment (name + frequency).
* ( ) Each sprint in scope: **minutes** or **3–5 bullet outcomes** in Story comment (actions + owners).
* ( ) Automation-relevant decisions linked to feature Stories or Epics where applicable.
```

---

## Story 4 — Knowledge transfer, onboarding & setup support

### Summary (copy)

```
[Platform Support] KT, onboarding & tooling/environment setup (Q2 26.05+)
```

### Description (copy)

```markdown
h2. Purpose
**KT sessions**, **new hire / contractor onboarding**, IDE/repo/pipeline **setup** assistance, and **runbook** walkthroughs so the team can execute regression and releases without single-person dependency.

h2. Scope
* Pairing, recorded sessions (if allowed), checklist updates in KB/Confluence.
* Password vault, VPN, GitLab access, qTest — *process* support not credential storage in Jira.
```

### Acceptance criteria (copy)

```markdown
* ( ) Each KT/onboarding event: **date**, **topic**, **attendees** (roles OK) in Story comment.
* ( ) **Artifacts**: link to recording, doc path, or checklist updated.
* ( ) Open **gaps** (e.g. missing runbook) logged as follow-up Story or Task.
```

---

## Story 5 — CI/CD & pipeline platform coordination

### Summary (copy)

```
[Platform Support] CI/CD & pipeline coordination — non-feature (Q2 26.05+)
```

### Description (copy)

```markdown
h2. Purpose
Time for **DevOps alignment**: job failures due to *infra*, agent pools, secrets rotation, artifact retention, GitLab/Jenkins config questions — without owning product feature delivery.

h2. Scope
* Triage pipeline-as-platform issues; open tickets to platform teams; verify after fix.
* Document job names and links in squad KB when changed.
```

### Acceptance criteria (copy)

```markdown
* ( ) Pipeline/infra issues **documented** with job URL + error snippet in comment or linked Task.
* ( ) **Resolution** or **handoff** noted when not owned by QA Automation code.
* ( ) No **Story points**; effort visible via **work log** only.
```

---

## Story 6 — Learning & continuous improvement (boxed)

### Summary (copy)

```
[Platform Support] Learning time — skills, tools & certifications (Q2 26.05+)
```

### Description (copy)

```markdown
h2. Purpose
Protected capacity for **learning**: new frameworks, Jira/qTest admin, performance tooling, security training, internal tech talks — improves long-term platform quality.

h2. How to use
* SM allocates **hours per sprint** (e.g. 4h/person) logged here or on personal sub-tasks under this Story.

h2. Evidence
* Short note per session: what was learned + link to course/doc (no PII).
```

### Acceptance criteria (copy)

```markdown
* ( ) Per sprint: at least **one** learning entry per active FTE (comment or sub-task) OR explicit *skip* with reason (e.g. release crunch).
* ( ) **Optional:** certificate or badge name in comment if completed.
* ( ) **Story points** left **blank**.
```

---

## Optional Story 7 — Jira / qTest / Confluence governance hygiene

### Summary (copy)

```
[Platform Support] Jira, qTest & KB hygiene — squad governance (Q2 26.05+)
```

### Description (copy)

```markdown
h2. Purpose
Keep **boards**, **filters**, **Epic links**, and **documentation** aligned with `docs/jira-governance` practices: stale Story cleanup, duplicate keys, export refresh (`Platform-support-jira-export.csv`).

h2. Cadence
* Bi-weekly or end-of-sprint — agree with SM.
```

### Acceptance criteria (copy)

```markdown
* ( ) Each hygiene cycle: **what changed** (3–5 bullets) in Story comment.
* ( ) Export or backlog file updated when team policy requires (link commit or Confluence page).
```

---

## Jira field cheat sheet

| Field | Value |
|-------|--------|
| **Epic Link** | *Your new Epic key after creation* |
| **Fix Version** | e.g. `AMSQUAD Sprint 26.05`, `26.06`, … or program `Q2-2026` — match your train |
| **Story Points** | **Empty** |
| **Priority** | Medium / Low (typical for platform support) |

---

## Sub-task pattern (optional, like export QA-542)

You can hang **Sub-tasks** under Story 1 mirroring export structure, for example:

* `Prime V2 – Morning regression review`
* `Prime V3 – Morning regression review`
* `Prime V2 – Failure reproduction & confirmation`
* `Prime V3 – Failure reproduction & confirmation`
* `Prime V2 / V3 – Communications (daily status / failure email)`

Paste the same **checklist-style acceptance** from those sub-tasks in `Platform-support-jira-export.csv` if you want identical wording.

**Version:** 1.0 · **Draft:** 2026-04
