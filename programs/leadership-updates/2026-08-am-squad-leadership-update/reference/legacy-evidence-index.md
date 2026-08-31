# Legacy Evidence Index

Raw exports from the original `AMSquad_OverallUpdate` dump. The curated 2026-08 leadership pack references these for full HTML reports and Jenkins logs.

**Base path:** `programs/leadership-updates-legacy/AMSquad_OverallUpdate/`

---

## GitLab exports

| File | Description |
|------|-------------|
| `Gitlab Details/AM Squad Merge to main - 04012026-0804-2026.csv` | All MRs merged to main (Apr–Aug) |
| `Gitlab Details/merged-work-items.csv` | Extended MR list with repository column |
| `Gitlab Details/merged-work-items - Priti MRs - 01012026 to 08052026.csv` | Priti-specific MR history |
| `Gitlab Details/user-summary.pdf` | GitLab user activity summary |

---

## V2 regression HTML reports (2026-08-04)

**Folder:** `V2 reports - 08042026/`

| Report | Methods |
|--------|--------:|
| Regression Test Suite - Enrollments.html | 147 |
| Regression Test Suite - Account or Profile Maintenance.html | 74 |
| Regression Test Suite - Empower Plan.html | 75 |
| Regression Test Suite - Withdrawals.html | 73 |
| Regression Test Suite - Contributions.html | 48 |
| Regression Test (Front Office) in Stage1 - Ugift.html | 36 |
| Regression Test Suite - Legacy Web Registration.html | 41 |
| Stage1 Sardine Regression Suite.html | 33 |
| Regression Test Suite - investment-options.html | 24 |
| Regression Test Suite - Legacy Web Login.html | 19 |
| Regression Test (Front Office) in Stage1 - Transfers.html | 12 |
| Regression Test Suite - Account Balance Page.html | 10 |

---

## V3 regression HTML reports (2026-08-04)

**Folder:** `V3 Report - 08042026/`

| Report | Notes |
|--------|-------|
| V3 Regression - Regression Test (Front Office) in Stage1 - IDP Login.html | 139 methods across 6 sub-suites |
| V3 Regression - Universal Enrollment Regression Test Suite - Stage1 Environment.html | UE module |

---

## Jenkins / performance exports

| File | Description |
|------|-------------|
| `Unite V2 regression - STAGE1-Daily-Unite-Prime-Regression.txt` | V2 nightly job config |
| `Smoke Suite - STAGE1-Daily-Empower-Regression.txt` | Empower nightly config + log |
| `Smoke Suite - STAGE5-Unite-Prime-SmokeTest.txt` | Stage 5 smoke |
| `Unite MSC regression.txt` | MSC endurance job config + log |
| `Perf Testing - Regression suite details.txt` | Regression suite Groovy script |
| `Perf Testing - Regression suite output.txt` | Suite execution output |
| `Perf Testing - Regg - idp-login-resources-remote.yaml - 603..608` | IDP perf run logs (6 files) |
| `Perf Testing - Regg - auth-server-delay-remote.yaml - 605..606` | Auth delay perf logs |
| `V3 Gitlab Regression raw log - scheduled_regression_job.txt` | GitLab CI nightly log |

---

## Screenshots

| File | Description |
|------|-------------|
| `Jenkins - Perf Testing dashboard.png` | Jenkins performance view |
| `AGSUP_ENDURANCE_THROUGHPUT.png` | Endurance job screenshot |

---

## How to use

1. **Leadership pack** (`programs/leadership-updates/2026-08-am-squad-leadership-update/`) has curated summaries, charts, and CSVs.
2. **This legacy folder** has the raw evidence for drill-down or audit.
3. Regenerate charts: `python programs/leadership-updates/tools/generate_leadership_charts.py`
