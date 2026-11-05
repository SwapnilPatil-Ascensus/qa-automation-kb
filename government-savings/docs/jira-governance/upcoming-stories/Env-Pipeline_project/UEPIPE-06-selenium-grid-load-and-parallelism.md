# UEPIPE-06 — Selenium grid: parallelism, duration, and capacity for ENVP UI suites

**Status:** Draft · **Suggested Story Points:** **3** · **Epic:** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600)

**Labels:** `automation`, `env-pipeline`, `infrastructure`, `selenium`, `ENVP`

**Source:** Meeting 04-01 (Nick: grid load, ~10–15 parallel UI tests, ~30 ideal; Rajib #8–#9).

---

## Copy — Jira Summary

```
[ENVP] Assess Selenium grid capacity vs UE (and future) parallel UI suites
```

---

## Copy — Description

```markdown
## Context
UE Stage 1 integration suite draft uses **parallel="tests"** with **thread-count="4"** and **9** TestNG `<test>` blocks — real concurrency and session count affect **duration** and **flakes** (see UEPIPE-02).

ENVP scale implies **multiple products** may add UI gates; grid could become the bottleneck.

## Goal
- Document **current** grid limits (max parallel sessions, queue behavior).
- Recommend **max parallel UI tests** per pipeline job and per org-wide concurrent jobs.
- Optional: **cost vs reliability** note for expanding grid (addresses meeting question on cost efficiency).

## Outputs
Short appendix for UEPIPE-01 Story comment + input to UEPIPE-04/05.
```

---

## Copy — Acceptance Criteria

```markdown
h3. Must pass

* ( ) Grid limits documented (numbers + source: runbook or Infra ticket).
* ( ) Recommendation for UE suite `thread-count` and for future suites.
* ( ) If expansion needed: linked request or “no change” decision with rationale.
```
