# MEMCONTRIB-03 — Contributions: add member-portal suite to CI / nightly pipeline

**Status:** Draft · **Suggested Story Points:** **3** · **Epic:** `QA-E-V3-TXN` (confirm)

**Labels:** `automation`, `prime-v3`, `contributions`, `member-portal`, `idp`, `cicd`, `stage1`, `QA-Board-View`, `Contrib`, `intake-upcoming`

**Depends on:** MEMCONTRIB-01 (minimum); preferably MEMCONTRIB-02 for stable breadth.

---

## Copy — Jira Summary

```
[V3][Contributions] Wire member-portal contribution tests into Stage 1 regression pipeline
```

---

## Copy — Description

```markdown
## Context
CSR contributions are already in `stage1-contributions.xml` (and likely a parent Stage 1 master suite). **Member-portal** contribution tests from MEMCONTRIB-01/02 must run on **schedule** (nightly or same cadence as CSR contributions) with **artifacts** (TestNG HTML) retained.

## User outcome
As **DevOps + QA**, I want **member-portal contribution** tests in the **approved pipeline**, so failures are visible **without** local-only runs.

## Scope — In
- New **TestNG suite XML** *or* **`<test>` blocks** added to existing contributions suite — team choice:
  - *Option A:* `stage1-contributions-member.xml` (parallel file, member-only tests).  
  - *Option B:* same `stage1-contributions.xml` with clearly named `<test name="... Member Portal ...">` entries.
- Pipeline (GitLab/Jenkins): invoke the suite or parent master that includes member tests; **artifact publish** matches CSR pattern (Surefire / report index URL).
- **Failure triage** owner documented (AMSquad daily process per `jira-export.csv` / QA-542 pattern).

## Scope — Out
- Changing **schedule** of entire monolith (coordinate with program).  
- Performance testing.

## Dependencies
- MEMCONTRIB-01 merged (tests exist).  
- DevOps approval for job duration / parallelism (`thread-count` aligned with CSR suite).

## Links
- Baseline CSR XML: `docs/jira-governance/data/stage1-contributions.xml`
```

---

## Copy — Acceptance Criteria

```markdown
* ( ) Member-portal contribution tests are referenced from **version-controlled** suite XML on integration branch.
* ( ) **At least one** successful **pipeline** run (scheduled or manual) completed with **green** or **known-linked** failures only.
* ( ) **TestNG index** (or equivalent) URL pattern documented in Story comment — same retention as existing contribution job.
* ( ) **Parent** master regression suite (if used) includes the new suite or tests; **no** silent skip.
* ( ) Run uses **Stage 1** config and correct **Maven profile** (document profile name in Story).
* ( ) If job runtime exceeds threshold, **parallelism** or split documented with PO approval.
```

---

## Copy — Definition of Done

```markdown
* Job name + link in Story; screenshot or paste of green run optional.
* Daily triage checklist can reference `stage1-contributions` **and** member block (update triage doc or QA-542 child text if applicable).
```
