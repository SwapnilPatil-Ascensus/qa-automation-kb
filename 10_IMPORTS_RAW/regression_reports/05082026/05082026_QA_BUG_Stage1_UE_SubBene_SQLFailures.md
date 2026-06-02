# QA Automation bug — Stage 1 Universal Enrollment & sub-bene SQL failures (05/08/2026)

**KB path:** `10_IMPORTS_RAW/regression_reports/05082026/05082026_QA_BUG_Stage1_UE_SubBene_SQLFailures.md`

| Field | Value |
|-------|--------|
| **Our JIRA** | **[QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821)** — *standalone QA record (not cloned from ODY).* |
| **Status** | **Resolved in environment** — automation/Stage 1 unblocked after DB work (05/08/2026). **JIRA closure pending** until **RCA** below is completed and signed off. |
| **Environment** | **Stage 1** |
| **Suite** | V3 regression — **Universal Enrollment** (`unite-universal-enrollment`) |
| **GitLab job (failure run)** | **14273272936** |

---

## 1. Summary (for JIRA — paste as title + first line)

**Ticket:** [QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821)

**Title:** `[Stage 1][Regression] Universal Enrollment + sub-bene — mass SQL failures (05/08/2026)`

**One-liner:** Nightly/regression UE run hit **SQL exceptions across plans** and **sub-bene** scenarios failed to complete; **pre-fix** evidence in job **14273272936** and folder artifacts below.

---

## 2. Description (for JIRA — our source of truth)

### What we observed (QA Automation)

- **Run:** V3 regression, **05/08/2026**.
- **Scope:** **Universal Enrollment** flow — failures **not isolated to one plan** (multiple plan codes affected).
- **Enrollment (positive / review steps):** Failures with **SQL exception** behavior during enrollment (automation reports **most UE cases failed**).
- **Sub-bene:** **First-step sub-bene** (and related) scenarios failed — e.g. **page not loading** / flow not completing when following enroll/sub-bene paths (see notes in `Bug - Enrollment & Sub Seq enrollment issue.txt`).

### Evidence (hard links)

| Artifact | URL |
|----------|-----|
| **Surefire index** | https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/14273272936/artifacts/unite/unite-universal-enrollment/target/surefire-reports/index.html |
| **Example — UE positive (NY)** | https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/14273272936/artifacts/unite/unite-universal-enrollment/target/surefire-reports/nyd.20260508001800624.UniversalEnrollmentPositive.feature_html_chrome_failedresult.html |
| **Example — sub-bene (NJ)** | https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/14273272936/artifacts/unite/unite-universal-enrollment/target/surefire-reports/njd.20260508031908800.UniversalEnrollmentFirstStepSubBene.feature_html_chrome_failedresult.html |

### Local folder (screenshots + scratch notes)

- `Bug - Enrollment & Sub Seq enrollment issue.txt` — quick repro notes + same links as above  
- `image.png`, `image (1).png`, `image (2).png`, `image (3).png`, `image-20260508-090654.png`

### Related product tickets (reference only)

- **ODY-2518** / **ODY-2519** were raised in **Teams** for similar **Stage 1** symptoms. **We do not rely on those tickets for our record** (thin description / not cloneable for our process). Link them in JIRA only under **“See also”** if required.

---

## 3. Impact

| Area | Impact |
|------|--------|
| **Automation** | High — **major UE regression failure** on Stage 1 for this run. |
| **Manual / product** | Per team channel, **enrollment** and **sub-bene** were treated as **blockers** on Stage 1 the same morning (handled outside this ticket body). |

---

## 4. Recovery (informational — not a substitute for RCA)

**Same day (05/08/2026):** Engineering identified a **missing DB promotion** relative to approved DB work; **MR !1615** (*Add total balance stored proc*) in **`uii-releases`** carries **`DB_PRs/mod100.0/PR_107560.sql`**. An **RT** was used to apply the **DBPR** on **Stage 1**; apply completed **without errors**. Team reported **enrollment** and **sub-bene** **working** again after apply.

**MR (reference):** https://ascensus-gs.gitlab.com/products/depot/uii-releases/-/merge_requests/1615  
*(Adjust GitLab base URL if your instance differs.)*

**Follow-up for QA:** Re-run regression on Stage 1 and attach **post-fix** job ID to this bug when closing.

---

## 5. RCA — **complete before closing [QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821)** (pending)

*Do not close the QA ticket on “environment works again” alone. Fill this section, then mark the bug **Done**.*

| Item | Status |
|------|--------|
| **RCA owner** | _Name_ |
| **RCA completed date** | _YYYY-MM-DD_ |
| **Final root cause (one paragraph)** | _Pending._ *Draft hypothesis from engineering thread: missed **`PR_107560`** (metrics / “total balance” proc, **EWW-330**) on Stage 1 → **semantic validation** path threw **SQL errors**, affecting UE and sub-bene. **Confirm with UP/DBA and paste final wording here.*** |
| **Contributing factors** | _e.g. promotion checklist gap, timing of app vs DB deploy, comms, … — TBD_ |
| **Evidence for RCA** | _e.g. Splunk/DB error text, object verification query results, RT number, change record — TBD_ |
| **Corrective action (done)** | _e.g. DBPR applied Stage 1 — date/owner — TBD_ |
| **Preventive action (process)** | _e.g. enforce DBPR-inventory check post-promote — TBD_ |

### Sign-off

- [ ] RCA text reviewed by **QA lead** (or delegate)  
- [ ] Post-fix **green** run linked (job ID): _______________  
- [ ] JIRA **Resolution** / **Comment** points to this file path  

---

## 6. Comms templates (QA-owned — no ODY dependency)

### Email — failure (archive)

**Subject:** `[QA-821] Stage 1 regression — Universal Enrollment SQL failures | job 14273272936`

Body: Stage 1 V3 regression failed mass UE + sub-bene scenarios with SQL errors. **Job:** 14273272936. **KB:** `10_IMPORTS_RAW/regression_reports/05082026/05082026_QA_BUG_Stage1_UE_SubBene_SQLFailures.md`. **JIRA:** [QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821).

### Email — resolved pending RCA

**Subject:** `[QA] Stage 1 UE regression unblocked | RCA pending | QA-821`

Body: Environment recovered after Stage 1 DBPR apply (see MR !1615 / PR_107560). **Re-run** regression and complete **RCA section** in KB before closing **[QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821)**.

### Teams — short

**Failure:** Stage 1 UE regression **SQL failures** — job **14273272936** — track **[QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821)** — KB `05082026_QA_BUG_Stage1_UE_SubBene_SQLFailures.md`  
**Update:** Env recovered same day; **close QA ticket only after RCA** filled in KB.

---

## 7. Metadata

| | |
|--|--|
| **Opened** | 05/08/2026 |
| **JIRA** | [QA-821](https://ascensuscollegesavings.atlassian.net/browse/QA-821) |
| **Detected by** | Automation (V3 regression) + team coordination |
| **KB maintainer** | QA Automation |
