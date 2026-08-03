# SYN-443 Barcode API — Performance Test Results & Handover

**Epic:** [SYN-443](https://ascensuscollegesavings.atlassian.net/browse/SYN-443)  
**Status:** **GO** (Stage 1)  
**Executed by:** Priti Choudhary  
**Sign-off:** Swapnil Patil, QA Automation  
**Date:** 2026-07-31

---

## 1. Executive summary

Performance testing for the **Returned Mail Barcode API** is **complete**. **GO** from QA Automation based on **Stage 1** results with production-like client certificate authentication.

| Environment | Sign-off role | Result |
|-------------|---------------|--------|
| **Stage 1** | **Authoritative — GO/NO-GO** | **Pass** at 30/45/60 scans/min |
| QC4 | Reference only | Intermittent failures (JAR bypass lost on daily deploy) — **not a blocker** |

---

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| `PUT /api/v1/plans/unite/returnmail/{barcodeId}` | UI / Kofax scanner |
| Stage 1 load tests (organic auth + cert) | Production load test |
| QC4 smoke attempts | Functional/manual regression |
| BlazeMeter / Taurus execution | |

---

## 3. API under test

| Item | Stage 1 |
|------|---------|
| Method | PUT |
| URL | `https://api.stage1.acs529.com/api/v1/plans/unite/returnmail/{barcodeId}` |
| Body | `{"scanResultCode":"RETURNED"}` |
| Auth | Client cert `kofaxapi.stage.acs529.com.pfx` |
| Tool | BlazeMeter (Taurus/BZT) |

QC4 uses `SCAN_RESULT_CODE` (uppercase) and no client cert — not used for sign-off.

---

## 4. Performance test cases executed

| ID | Name | Target load | Max VUs | Duration | Pass criteria |
|----|------|-------------|---------|----------|---------------|
| **TC03** | `unite_returnmail_put_stage1_tc03_30spm` | 30 scans/min | 10 | 11 min | 2xx, error rate ~0%, stable latency |
| **TC04** | `unite_returnmail_put_stage1_tc04_45spm` | 45 scans/min | 15 | 11 min | Same |
| **TC05** | `unite_returnmail_put_stage1_tc05_60spm` | 60 scans/min | 20 | 11 min | Same |

### Results summary

| TC | Avg throughput | Avg response | 90th %ile | Error rate | HTTP codes |
|----|----------------|--------------|-----------|------------|------------|
| TC03 | 28.99 hits/s | 54 ms | 91 ms | 0.01% | 2xx |
| TC04 | 43.01 hits/s | 52 ms | 85 ms | 0% | 2xx |
| TC05 | 56.71 hits/s | 55 ms | 88 ms | 0% | 2xx |

---

## 5. Artifacts location

All files under `programs/barcode-syn-443/artifacts/`:

| File | Description |
|------|-------------|
| `UNITE-RETURNMAIL-PERFORMANCE-TEST-EXECUTION-REPORT-v1.2.docx` | Formal execution report (Priti) |
| `unite_returnmail_put_stage1_tc03_30spm.png` | BlazeMeter summary — TC03 |
| `unite_returnmail_put_stage1_tc04_45spm.png` | BlazeMeter summary — TC04 |
| `unite_returnmail_put_stage1_tc05_60spm.png` | BlazeMeter summary — TC05 |
| `unite-returnmail-put-stage1.csv` | Stage 1 test data (~200 barcode IDs) |
| `unite-returnmail-put-qc4.csv` | QC4 test data (reference) |
| `RE Sign-off Requested...eml` | Email thread reference |

**BlazeMeter project:**  
https://a.blazemeter.com/app/#/accounts/406482/workspaces/516742/projects/2587606/tests

---

## 6. Setup documentation (handover)

| Topic | Document |
|-------|----------|
| Project overview | `README.md` |
| Postman — Priti handoff | `docs/PRITI-HANDOFF.md` |
| Stage 1 cert setup | `docs/07-stage1-postman-cert-setup.md` |
| QC4 curl / smoke | `api/curl-from-suresh.md` |
| Stage 1 curl | `api/curl-stage1-from-suresh.md` |
| Postman collection | `postman/SYN-443-Barcode-API.postman_collection.json` |
| Postman env Stage 1 | `postman/SYN-443-Barcode-API-Stage1.postman_environment.json` |
| Postman env QC4 | `postman/SYN-443-Barcode-API-QC4.postman_environment.json` |
| Meeting decisions | `docs/06-meeting-2026-07-28-decisions.md` |
| Load profile draft | `docs/03-load-profile.md` |

---

## 7. Retest policy

Retest **Stage 1** performance when:

1. New deployment to Stage 1 or Prod for this API
2. Cert/auth/infra changes
3. Endpoint or Mailstop logic changes
4. Business requests higher load than 60 scans/min

**Notify QA Automation at deploy time** — include Swapnil / Priti on deployment emails.

---

## 8. QC4 known issue (historical)

Daily QC4 build removes DevOps partner-auth bypass JAR → **404/503**. Suresh confirmed JAR must be re-applied post-build. Not used for GO decision.

---

## 9. Contacts

| Role | Name |
|------|------|
| Perf execution | Priti Choudhary |
| QA Automation lead | Swapnil Patil |
| Dev / API | Suresh Mahto |
| PM | Brenda Montoya |
| Perf strategy | Rajib Akhter |
