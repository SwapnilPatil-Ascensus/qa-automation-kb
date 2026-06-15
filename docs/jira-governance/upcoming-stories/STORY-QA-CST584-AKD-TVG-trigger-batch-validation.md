# Story (QA board) — CST-584 — AKD TVG trigger fix: Control-M batch validation with Naomi

**KB file:** `docs/jira-governance/upcoming-stories/STORY-QA-CST584-AKD-TVG-trigger-batch-validation.md`  
**Purpose:** QA **testing-only** Story to log time while validating **[CST-584](https://ascensuscollegesavings.atlassian.net/browse/CST-584)** (*AKD TVG — Create a trigger — 529 June Release*) with **Naomi Bechar**. Covers **Control-M batch** execution, **`ctl_rec_status = X`** rerun from **04/26** forward, and SQL/calculator evidence for Comet epic **[CST-472](https://ascensuscollegesavings.atlassian.net/browse/CST-472)**.

**Related QA work:** [STORY-QA-CST469-AKD-TVG-microsecond-timestamp-manual-validation.md](./STORY-QA-CST469-AKD-TVG-microsecond-timestamp-manual-validation.md) (fractional-second / trigger intro — **CST-469**)

**Jira (QA) — after create, paste key here:** `QA-________`

---

## Comet linkage

| Item | Detail |
|------|--------|
| **Comet Story** | [CST-584](https://ascensuscollegesavings.atlassian.net/browse/CST-584) — *AKD TVG - Create a trigger - 529 June Release* |
| **Epic** | [CST-472](https://ascensuscollegesavings.atlassian.net/browse/CST-472) — *AKD - TVG Calculator Credits Incorrect Logic - URGENT* |
| **Prior Comet** | [CST-469](https://ascensuscollegesavings.atlassian.net/browse/CST-469) — QIPS-413; SYSDATE → LOCALTIMESTAMP / fractional seconds |
| **Fix version** | 529 June Release *(confirm in Jira)* |
| **QA assignee** | Swapnil Patil |
| **Dev/SME partner** | Naomi Bechar (Comet) |
| **CSR manual baseline** | Ganesh Excel spreadsheet calculator (Client Services workaround until fix deployed) |

---

## Problem summary (from Naomi / epic — for test design)

| Issue | Detail |
|-------|--------|
| **Root symptom** | AKD TVG calculator wrong guarantee when **multiple transactions** share the same calculation run date |
| **Original cause** | `SYSDATE` in SQL lacked **fractional seconds** → Oracle non-deterministic tie-break |
| **CST-469 / trigger work** | Row-level trigger introduced for **`ctl_upd_dttm`** fractional seconds — **Swapnil + Naomi tested**; fractional seconds now distinct for same-day multiples |
| **Remaining risk (Naomi)** | **`ctl_upd_dttm` is not reliable for ordering** — ticket/SQL maintenance can touch rows (e.g. RT 490026, 49,190 rows on 12/16/2024) without reflecting calculation order |
| **CST-584 direction** | **Trigger-based fix** on target tables; use **`calculation date`** and **`calculation order`** (available from **08/09/2024** onward) rather than **`ctl_upd_dttm`** alone |
| **Historical gap** | Calculations before **07/28/2024** barebones job / before **08/09/2024** may lack calculation date/order — migration may be manual per account |

**Tables (from epic):** `tu_tuition_credit_acct_txn`, `tu_tuition_credit_balance` (and related CTL columns per Naomi’s analysis)

---

## Work already performed (log on this Story)

| Date | Activity | Owner |
|------|----------|-------|
| Recent | Paired with Naomi — validated trigger / fractional-second job behavior post CST-469 path | Swapnil + Naomi |
| Recent | Ran **TVG calculator batch** via **Control-M** in test/agreed env | Swapnil |
| Recent | Set **`ctl_rec_status = 'X'`** on affected population and **reran batch from 04/26** through current calculation date to reprocess | Swapnil + Naomi |
| Pending | Formal evidence bundle + CST-584 / CST-472 sign-off comment | Swapnil |

---

## Jira fields (QA Automation Story)

| Field | Value |
|-------|-------|
| **Issue type** | Story |
| **Project** | QA |
| **Summary** | `[CST-584][AKD/TVG] Manual validation — trigger fix + Control-M batch rerun (04/26+)` |
| **Priority** | High *(production exposure — align with CST-472)* |
| **Labels** | `ManualTesting`, `CST-584`, `CST-472`, `PlatformSupport`, `AKD`, `TVG` |
| **Epic Link** | QA epic if used; **Relates to** [CST-584](https://ascensuscollegesavings.atlassian.net/browse/CST-584), [CST-472](https://ascensuscollegesavings.atlassian.net/browse/CST-472) |
| **Story points** | 5 *(1–2 days per epic estimate — design + batch + SQL + evidence)* |
| **Assignee** | Swapnil Patil |
| **Collaborators** | Naomi Bechar (primary); Ganesh (spreadsheet cross-check if needed) |

---

## Description (paste into Jira)

```text
h2. Purpose
Manual QA validation for Comet *CST-584* (AKD TVG — create trigger — 529 June Release) under epic *CST-472*. Partner with *Naomi Bechar* to prove the trigger fix and batch reprocessing produce correct guarantee/credit ordering after the 04/26 rerun.

h2. Context
* AKD TVG calculator failed when multiple transactions occurred on the same calculation date (SYSDATE / ordering issues — see CST-469, Naomi email 06/10/2026).
* QA (Swapnil) previously tested fractional-second behavior on ctl_upd_dttm with Naomi; Naomi identified ctl_upd_dttm alone is unreliable when ticket work updates rows.
* CST-584 delivers trigger-based fix for June release.
* Validation executed via *Control-M* batch job; affected rows marked ctl_rec_status = 'X' and batch rerun from *04/26* through target date.

h2. Scope (testing only)
* Verify batch completion and job logs (Control-M).
* SQL validation: calculation date, calculation order, ctl_rec_status transitions, guarantee/credit balances for sample accounts (including multi-transaction same-day cases from Naomi examples).
* Compare results to Ganesh spreadsheet / Naomi expected matrix where available.
* Document impacted population counts to support leadership questions (# accounts, # transactions — coordinate with Naomi).

h2. Out of scope
* Code changes (Comet / Naomi).
* Full production migration of pre-08/09/2024 history (design decision — track separately).
* Automated regression suite (optional follow-up).

h2. Dependencies
* Naomi: env, account list, SQL scripts, Control-M job name, ctl_rec_status rerun procedure.
* DB read access to UII0 / tuition credit tables in agreed env.
* Ganesh spreadsheet for CSR parity checks (optional).

h2. Evidence
* Attach SQL outputs (redacted), Control-M run IDs, before/after balances, Jira comment on CST-584 with link to this QA Story.
```

---

## Acceptance criteria

```markdown
- [ ] **Control-M batch:** Document job name, run date/time, env, and **Successful** completion (or documented failure with owner).
- [ ] **Rerun procedure:** Evidence that `ctl_rec_status` was set to **`X`** and batch rerun executed from **04/26/2026** (or agreed start) through target calculation date per Naomi script.
- [ ] **Multi-transaction same-day accounts:** At least **2** known problematic accounts (from Naomi/Ganesh examples) show **correct** guarantee/credit ordering vs spreadsheet baseline.
- [ ] **Calculation order columns:** For post-08/09/2024 rows, `calculation date` + `calculation order` populated and used for ordering — **not** relying solely on `ctl_upd_dttm` where ticket-touched rows exist.
- [ ] **Fractional seconds / trigger:** For new runs, audit timestamps show distinct fractional precision where multiple rows share calendar second (confirm trigger active — not disabled).
- [ ] **Population metrics:** Provide Naomi/Arun summary: # accounts rerun, # transactions reprocessed, any remaining exceptions (gain/loss estimate if available from Comet).
- [ ] **CST linkage:** Comment on **CST-584** and **CST-472** — "QA validation complete" + link to **QA-___**; log all hours on QA Story.
- [ ] **Manual test pack:** Execute or mark Blocked all cases **TVG-CM-001** through **TVG-CM-010** (§3).
```

---

## Manual test cases — Control-M + batch rerun

**Prefix:** `TVG-CM-###` (TVG + Control-M)

| ID | Title | Steps | Expected |
|----|-------|-------|----------|
| TVG-CM-001 | Control-M — job submission | Run TVG calculator batch via Control-M (document chain/job name with Naomi). | Job completes **OK**; logs retained. |
| TVG-CM-002 | Pre-rerun — identify population | Run Naomi’s SQL to list accounts/transactions needing rerun from **04/26+**. | Count documented; matches Comet expectation. |
| TVG-CM-003 | Mark for rerun | Apply `ctl_rec_status = 'X'` (or agreed flag) per Naomi script. | Row count matches TVG-CM-002; no prod schema error. |
| TVG-CM-004 | Batch rerun | Re-execute Control-M batch for date range **04/26 → target date**. | Job completes; `ctl_rec_status` transitions to processed state per design. |
| TVG-CM-005 | Multi-txn same calc date — ordering | Query `tu_tuition_credit_acct_txn` (and balance) for sample account with **multiple txns same calculation date**. | **Last calculated transaction** used for credit balance matches Ganesh/Naomi formula; `calculation order` monotonic. |
| TVG-CM-006 | Ticket-touched row control | Include account/row known touched by maintenance (e.g. aggregation flag update) if in test set. | Ordering uses **calculation date/order**, not stale/misleading `ctl_upd_dttm` alone. |
| TVG-CM-007 | Fractional timestamp check | `TO_CHAR(ctl_upd_dttm,'…FF6')` or equivalent on fresh calc rows. | Distinct fractional seconds for rapid sequential calcs. |
| TVG-CM-008 | Trigger status | Verify trigger(s) on target tables **ENABLED** (not disabled — per recent Stage1 trigger incident pattern). | `USER_TRIGGERS.STATUS = 'ENABLED'`. |
| TVG-CM-009 | Calculator UI / CSR spot-check | Optional: one CSR-facing calculator check vs spreadsheet. | Matches Ganesh spreadsheet within agreed tolerance. |
| TVG-CM-010 | Evidence bundle | SQL + Control-M screenshots + summary table for Arun scope questions. | Attached to QA Story + CST-584 comment. |

---

## SQL templates (replace schema/names with Naomi)

```sql
-- Trigger status (CST-584)
SELECT trigger_name, status, table_name
FROM   all_triggers
WHERE  table_name IN ('TU_TUITION_CREDIT_ACCT_TXN','TU_TUITION_CREDIT_BALANCE')
AND    owner = 'UII0';

-- Same-day multiple transactions — ordering check
SELECT account_id,
       calculation_date,
       calculation_order,
       TO_CHAR(ctl_upd_dttm, 'YYYY-MM-DD HH24:MI:SS.FF6') AS ctl_upd_ts,
       ctl_rec_status,
       credit_balance  -- adjust column names
FROM   uii0.tu_tuition_credit_acct_txn
WHERE  account_id = :test_account
AND    calculation_date = :calc_date
ORDER BY calculation_date, calculation_order;

-- Rerun population (04/26+)
SELECT COUNT(*) AS acct_cnt, COUNT(DISTINCT account_id) AS distinct_accts
FROM   uii0.tu_tuition_credit_acct_txn
WHERE  calculation_date >= DATE '2026-04-26'
AND    ctl_rec_status = 'X';  -- adjust per Naomi script
```

---

## Scope metrics for leadership (Arun email 06/10/2026)

Populate after validation and attach to CST-472 comment:

| Question | Source | Result (fill) |
|----------|--------|---------------|
| # accounts impacted | Naomi rerun SQL | |
| # transactions reprocessed | Batch logs / SQL | |
| Financial gain/loss exposure | Comet / Finance | |
| Manual workaround | Ganesh spreadsheet | In use by CSR until deploy |
| Effort: targeted fix vs redesign | Naomi recommendation | CST-584 = targeted trigger; full redesign = separate initiative |

---

## Sub-tasks (optional)

| Sub-task | Estimate |
|----------|----------|
| Align env, Control-M job, and rerun script with Naomi | 2h |
| Execute TVG-CM-001..004 (batch + rerun) | 3h |
| Execute TVG-CM-005..008 (SQL + triggers) | 3h |
| TVG-CM-009..010 evidence + Jira comments | 2h |

---

## Time logging

- Log all work to **`QA-___`** (this Story).  
- Daily mirror on **CST-584**: *"QA validation — work on QA-___"*  
- Relate to **CST-472** for epic traceability.

---

**Version:** 1.0 · **Created:** 2026-06 · **Author:** Swapnil Patil
