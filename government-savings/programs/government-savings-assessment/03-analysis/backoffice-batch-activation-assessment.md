# Back-office / Batch — Activation Assessment

**As of:** 2026-07-21  
**Repository:** `unite-test-automation` (Legacy Unite / V2)

---

## Executive summary

Legacy Unite includes a **large back-office automation corpus** (1,062 feature files in the backoffice subtree of the current repository scan). Automation is **implemented in code** but **not part of the Modern Unite (V3) GitLab nightly**. Historical documentation references **weekly backoffice regression** (Tuesday/Wednesday). Live schedule was **not re-verified** in this pass.

---

## Inventory (verified)

| Asset | Count | Unit | Status |
|-------|------:|------|--------|
| Backoffice feature files | 1,062 | Cucumber features | Verified from repository code |
| Prior scenario estimate | ~1,077 | scenarios | Consistent with earlier scan |
| Full V2 repository | 1,538 | features total | Includes frontoffice + backoffice |
| Kofax / feed flows | Present in backoffice tree | qualitative | Requires SME mapping |

---

## Nightly inclusion status

| Suite type | Documented schedule | Verified live | Gate type |
|------------|--------------------:|---------------|-----------|
| Daily frontoffice (10 modules) | Jenkins nightly Mon–Fri | Referenced — not live-verified | Functional regression |
| Weekly backoffice | Tue/Wed Wed per AM docs | Referenced — not live-verified | Feed/batch validation |
| V3 GitLab nightly | N/A for backoffice | Confirmed absent | — |

---

## Leadership-safe wording

> "Back-office and batch automation assets are substantially implemented in the Legacy Unite repository. Recurring inclusion in a governed nightly suite requires revalidation, environment confirmation, and schedule activation — they are not represented in the Modern Unite GitLab pipeline today."

---

## Revalidation effort required

| Work item | Description | Owner |
|-----------|-------------|-------|
| Feed inventory | Map Kofax/batch/feed scenarios to business owners | BA + QA |
| Data dependencies | Confirm Stage1 DB and feed file availability | DevOps + QA |
| Suite health | Identify quarantined or stale scenarios | QA Automation |
| Schedule confirmation | Verify Jenkins weekly backoffice jobs | DevOps |
| Traceability | Link critical feeds to qTest / Jira | QA Governance |
| Modernization path | Decide Ant/Jenkins vs migration candidate | Architecture |

**Estimated effort:** 2–4 weeks for inventory + smoke; 1–2 quarters for governed weekly regression if approved.

---

## Distinction from member portal

| Tier | Scope | Active regression |
|------|-------|-------------------|
| **A — High-priority member portal** | Balance, contributions, withdrawals, login, UGift, etc. | 10 daily Jenkins modules (referenced) |
| **B — Back-office / batch** | Feeds, batch jobs, Kofax-related flows | Weekly (referenced) — revalidation needed |
| **C — CSR / greenscreen / management** | Operational CSR screens | Assets exist — deferred from daily nightly |

---

## Recommended actions

1. Confirm Jenkins weekly backoffice job names and last green run  
2. Publish critical-feed short list for leadership  
3. Separate backoffice metrics from member-portal metrics in reporting  
4. Do not imply batch coverage is active without execution evidence

---

*Evidence: `unite/bin/build.xml`, `testsuite/backoffice/`, AM_Regression_Reports/docs/CICD/02-automation-v2-pipelines.md*
