# Story (QA board) — CST-469 / QIPS-413 — Manual validation: TVG calculator + microsecond create/update timestamps

**KB file:** `docs/jira-governance/upcoming-stories/STORY-QA-CST469-AKD-TVG-microsecond-timestamp-manual-validation.md`  
**Purpose:** Create a **QA Automation** Jira **Story** to **log time** while supporting **Naomi Bechar** on **Comet** work **[CST-469](https://ascensuscollegesavings.atlassian.net/browse/CST-469)** (*QIPS-413 — AKD — TVG Calculator Credits Incorrect Logic*). Includes **manual test cases** and **test data / SQL verification** design for **create** and **update** timestamps showing **microsecond** (fractional-second) precision on **every** update.

**Comet references (from export):**

| Item | Link / detail |
|------|----------------|
| Story | [CST-469](https://ascensuscollegesavings.atlassian.net/browse/CST-469) |
| Parent / Epic | [CST-472](https://ascensuscollegesavings.atlassian.net/browse/CST-472) — *AKD - TVG Calculator Credits Incorrect Logic - URGENT* |
| Problem | `SYSDATE` in SQL lacked **fractional seconds**; Oracle could not order rows deterministically → incorrect **guarantee** calculations. |
| Fix (summary) | Replace `SYSDATE` with **`LOCALTIMESTAMP`** (or equivalent) in relevant **XML**; backfill/update data so timestamps carry **fractional seconds** (e.g. tie-break using **calculation order** as fractional component — confirm exact implementation with Naomi / dev). |
| QA mention on ticket | *“Swapnil from the QA automation team suggested for validation…”* |

**Jira (QA) — after create, paste key here:** `QA-________`

| Field (suggested) | Value |
|-------------------|--------|
| **Issue type** | Story |
| **Project** | QA — QA Automation |
| **Summary** | `[CST-469][AKD/TVG] Manual validation — calculator credits + microsecond create/update timestamps` |
| **Priority** | Medium *(or match CST urgency — align with lead)* |
| **Labels** | `QA-Board-View`, `PlatformSupport` *(optional)*, `ManualTesting`, `CST-469` |
| **Links** | **Relates to** [CST-469](https://ascensuscollegesavings.atlassian.net/browse/CST-469); **Relates to** [CST-472](https://ascensuscollegesavings.atlassian.net/browse/CST-472) |
| **Story points** | 3–5 *(align to effort: design + data + execution + evidence)* |
| **Assignee** | Swapnil Patil |
| **AGS Scrum Team / Team** | QA Automation / Automation Squad *(per your Jira schema)* |

---

## 1. Description (paste into Jira *Description*)

Use wiki or markdown per project. Plain text below.

```text
h2. Purpose
Support Naomi Bechar (Comet / CST) on validation of *QIPS-413 / AKD — TVG Calculator Credits* fix delivered under CST-469 (parent CST-472). Focus: *manual* verification that credit/guarantee ordering is deterministic after moving from SYSDATE to timestamps with *fractional seconds* (microsecond precision in Oracle terms).

h2. Context
* Comet Story CST-469: replace SYSDATE with LOCALTIMESTAMP in relevant XML; update existing data to include fractional seconds.
* Risk addressed: identical wall-clock second → non-deterministic ordering → wrong guarantee calculations.

h2. Scope (this QA Story)
* Author and execute *manual* test cases: UI/calculator (where Client Services checks apply) + *database* checks that CREATE_DT / UPDATE_DT (or equivalent column names) reflect *microsecond* changes on successive updates.
* Prepare *test data* and queries to prove: (1) initial insert has fractional part; (2) each update advances UPDATE timestamp with a *different* fractional second when updates occur in quick succession; (3) ordering of dependent calculations matches expected sequence.

h2. Out of scope
* Production deployment (Comet).
* Automated UI suite for TVG (optional follow-up Story unless requested).

h2. Dependencies
* Target environment + schema build containing CST-469 code and DB changes (confirm with Naomi: branch, env, ctl_ins_* objects).
* Table/column list from dev (exact names for audit/create/update columns touched by the fix).

h2. Evidence
* Attach or link: spreadsheet / Ganesh calculator cross-checks if used; SQL output snippets (masked if PII); screenshots of calculator results; Jira comment on CST-469 with “QA Automation validation complete” and link to this QA Story.
```

---

## 2. Acceptance criteria (paste into Jira)

```markdown
- [ ] **Manual test pack delivered:** At least **8** manual cases documented (this file §3) — executed or explicitly *Blocked* with reason and owner.
- [ ] **Microsecond / fractional-second proof:** For agreed audit columns (**CREATE_DT**, **UPDATE_DT** or names from dev), SQL evidence shows:
  - [ ] Format/precision includes fractional seconds (e.g. `FF6` in `TO_CHAR`, or query comparing `EXTRACT` from fractional second).
  - [ ] **Two rapid successive updates** on the same logical row produce **distinct** `UPDATE_DT` values (not identical to second precision only).
- [ ] **Calculator / credits behavior:** At least one **positive** and one **edge** scenario (e.g. tied-second ordering resolved by fractional time or documented tie-break) match **expected** guarantee/credit outcome vs baseline spreadsheet or Naomi’s expected matrix.
- [ ] **CST linkage:** Comment on **CST-469** (or CST-472) with summary + link to this **QA-___** Story; log **Tempo / worklog** on **QA-___** for all time spent.
- [ ] **Test data doc:** §4 test-data recipe stored in Story comment or Confluence/Git link so reruns are reproducible.
```

---

## 3. Manual test cases (execute against post-fix build)

**Prefix:** `TVG-MS-###` (TVG + microsecond). Adjust UI steps to your actual AKD/TVG screens.

| ID | Title | Preconditions | Steps | Expected result |
|----|--------|---------------|-------|-----------------|
| TVG-MS-001 | DB — column type supports fractional seconds | DB access | Query `DATA_TYPE` / precision for **CREATE_DT**, **UPDATE_DT** (and any column used for ordering) on target table(s) from dev list. | `TIMESTAMP(n)` with **n ≥ 6** or `TIMESTAMP WITH LOCAL TIME ZONE` with sufficient precision; not `DATE`-only for ordering columns. |
| TVG-MS-002 | DB — new row has fractional **CREATE** | Clean insert path | Insert or trigger one new calculation row; `SELECT … TO_CHAR(create_dt,'YYYY-MM-DD HH24:MI:SS.FF6') FROM …`. | String shows **non-zero** fractional part (or documented default); not always `.000000` unless truly simultaneous. |
| TVG-MS-003 | DB — **UPDATE** advances fractional seconds | Row from MS-002 | Run **two** updates &lt; 1 second apart (script or app); capture `UPDATE_DT` after each. | Second `UPDATE_DT` **strictly greater** than first; both show microsecond granularity. |
| TVG-MS-004 | DB — ordering deterministic | Multiple rows same calendar second | Seed **N** rows in same second with different fractional parts (per Naomi/dev script); run the **same** credit/guarantee query twice. | **Identical** result set order both runs; matches documented tie-break rule. |
| TVG-MS-005 | App — calculator happy path | CSR or test URL | Enter standard AKD scenario (inputs from test data §4); submit; capture result totals. | Matches expected from spreadsheet / Naomi baseline; no error. |
| TVG-MS-006 | App — rapid repeat submit | Same session | Submit same scenario twice within 1 second; compare DB rows if applicable. | Each transaction or version row has **distinct** timestamp if design stores per run; no silent reuse of identical ordering key. |
| TVG-MS-007 | Regression — unrelated calculator | Control plan | Run one non-AKD or unchanged scenario. | No regression vs known good (document pass/fail). |
| TVG-MS-008 | Doc — evidence bundle | All above | Zip SQL outputs + screenshots; redact secrets. | Attached to QA Story or CST-469 comment. |

---

## 4. Test data design — microsecond create/update verification

### 4.1 Principles

1. **Oracle:** `DATE` has no subsecond precision; **`TIMESTAMP(6)`** / **`LOCALTIMESTAMP`** exposes **microseconds**. Validation must target columns that are actually **`TIMESTAMP`**, not `DATE`, post-migration.  
2. **Prove “every update”:** Use a **PL/SQL** block or two **sequential** `UPDATE` statements in one script with **no** `DBMS_LOCK.sleep` if possible; if timestamps still collide, add **minimal** sleep (e.g. 0.001 s) only after confirming with dev that real app can emit distinct timestamps without sleep.  
3. **Display in SQL*Plus or SQL Developer:**

```sql
-- Replace owner.table and column names from Naomi / dev
SELECT id,
       TO_CHAR(create_dt, 'YYYY-MM-DD HH24:MI:SS.FF6') AS create_ts,
       TO_CHAR(update_dt, 'YYYY-MM-DD HH24:MI:SS.FF6') AS update_ts
FROM   your_schema.your_table
WHERE  id = :test_id;
```

4. **Compare two updates:**

```sql
-- Capture t1, run update #1, capture t2, run update #2, capture t3
-- Expect t3 > t2 > t1 at fractional precision
```

### 4.2 Sample test row recipe (template — **do not run in prod**)

| Step | Action |
|------|--------|
| 1 | Create **one** AKD test account / scenario ID in **agreed** env (Naomi). |
| 2 | Note **before** `UPDATE_DT`. |
| 3 | Perform **calculation** or **save** that touches the fixed XML path **twice** in quick succession. |
| 4 | Note **after** each; compute `EXTRACT(SECOND FROM (ts2 - ts1))` or compare `FF6` strings. |
| 5 | If fractional part never changes, **escalate** — possible trigger still using `SYSDATE` or `DATE` cast. |

### 4.3 Negative / edge

| Case | Expectation |
|------|--------------|
| Bulk update same statement | Still **monotonic** `UPDATE_DT` per row if row-level triggers. |
| Clock skew N/A | `LOCALTIMESTAMP` is session/server local — document env. |

---

## 5. Time logging (Tempo)

- Log work to **`QA-___`** (this Story), not only CST-469, so **QA board** burn-down and capacity stay accurate.  
- Optional: small mirror comment on **CST-469** per day: *“QA validation in progress — work logged on QA-___.”*

---

## 6. Sub-tasks (optional on QA Story)

| Sub-task summary | Estimate |
|------------------|----------|
| Draft manual cases + SQL templates | 2h |
| Align table/column names with Naomi / dev | 1h |
| Execute MS-001–004 in test DB | 2h |
| Execute MS-005–007 UI + evidence | 2h |
| Close out: AC + CST comment | 1h |

---

## 7. Changelog

| Date | Author | Note |
|------|--------|------|
| 2026-05-12 | Swapnil / KB | Created from CST-469 Word export (QIPS-413, SYSDATE → LOCALTIMESTAMP, QA validation ask). |
