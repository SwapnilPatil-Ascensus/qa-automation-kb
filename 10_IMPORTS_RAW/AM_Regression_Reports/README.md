# AM Regression Reports – Folder Index

This folder contains the QA Automation regression suite documentation, TestNG suite XMLs, and execution report references for the nightly automation program.

---

## Folder Structure

```
AM_Regression_Reports/
├── docs/                           # ✅ CHECK IN — Confluence-ready documentation
│   ├── README.md                   # Hub → Master Overview PDF + V2/V3 entry points
│   ├── 00-automation-regression-master-overview.md  # Full TOC (parent for all doc pages)
│   ├── CICD/                       # CI/CD landscape (Confluence-ready): master + V2/V3/API/perf/GitHub/mobile
│   ├── v2/                         # Prime V2 overview + per-module docs
│   │   ├── README.md               # Start here for V2
│   │   ├── 00-v2-regression-overview.md
│   │   ├── 01-v2-module-coverage.md
│   │   ├── 02-v2-suite-and-job-details.md
│   │   ├── 03-v2-documentation-delta.md
│   │   └── modules/               # Per-module Confluence pages (1 per module)
│   │       ├── 01-enrollment.md
│   │       ├── 02-legacy-web-registration.md
│   │       ├── 03-legacy-web-login.md
│   │       ├── 04-csr-account-maintenance.md
│   │       ├── 05-contributions.md
│   │       ├── 06-withdrawals.md
│   │       ├── 07-account-balance-page.md
│   │       ├── 08-sardine-regression.md
│   │       ├── 09-investment-options.md
│   │       ├── 10-empower-plan.md
│   │       ├── 11-smoke-suites.md
│   │       ├── 12-release-suites.md
│   │       ├── 13-weekly-backoffice.md
│   │       └── 14-other-specialty.md
│   └── v3/                         # Prime V3 docs (Stage 1 UE + IDP)
│       ├── README.md
│       └── modules/
│           ├── README.md
│           ├── 00-stage1-v3-combined-overview.md
│           ├── 01-idp-login-stage1.md
│           └── 02-universal-enrollment-stage1.md
│
├── suites/                         # ✅ CHECK IN — TestNG suite XML files (organized)
│   ├── v2/
│   │   ├── daily/                  # 10 active nightly suites
│   │   ├── smoke/                  # CAT / Stage 5 / Stage 2
│   │   ├── release/                # Release-gate suites
│   │   ├── weekly/                 # Backoffice feed (Tue/Wed)
│   │   ├── other/                  # Specialty (Flywire, SSgA, ACH)
│   │   └── archive/               # Superseded monolithic suites
│   └── v3/
│       ├── stage1-regression-master.xml
│       ├── universal-enrollment-stage1.xml
│       └── idp-login-stage1.xml
│
├── reports/                        # 🚫 GITIGNORED (mostly) — Raw HTML reports; see docs/GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md
│   ├── README.md                   # Optional: local policy pointer (may be ignored — canonical guide is under docs/)
│   ├── v2/                         # TestNG HTML per module (clean up *_files/, rename per guide)
│   └── v3/
│
```

---

## What to Check In

| Folder | Check In? | Why |
|--------|-----------|-----|
| `docs/` | **Yes** | Confluence-ready documentation; lightweight Markdown |
| `suites/` | **Yes** | TestNG suite XMLs; small reference files |
| `reports/` | **No** | Raw HTML reports; large, regenerable from Jenkins (gitignored) |

---

## Quick Start

- **Master documentation hub (parent for all pages):** [`docs/README.md`](docs/README.md) · full TOC [`docs/00-automation-regression-master-overview.md`](docs/00-automation-regression-master-overview.md) · PDF [`reports/Automation Regression Suite – Master Overview.pdf`](reports/Automation Regression Suite – Master Overview.pdf)
- **CI/CD & pipelines (Jenkins / GitLab / GitHub, etc.):** [`docs/CICD/README.md`](docs/CICD/README.md)
- **V2 documentation:** [`docs/v2/README.md`](docs/v2/README.md)
- **V2 per-module details:** [`docs/v2/modules/`](docs/v2/modules/)
- **V3 documentation:** [`docs/v3/README.md`](docs/v3/README.md) · [`docs/v3/modules/`](docs/v3/modules/)
- **Suite XMLs:** [`suites/`](suites/)

---

## Related

| Resource | Location |
|----------|----------|
| **Master Overview PDF (local)** | `AM_Regression_Reports/reports/Automation Regression Suite – Master Overview.pdf` |
| Old Confluence PDFs (archive) | `10_IMPORTS_RAW/confluence_exports/Automation QA - Home & Documentation Hub/Automation Regression Suite - Master Overview/` |
| Bug reporting process | `10_IMPORTS_RAW/regression_reports/BUG_REPORTING_PROCESS.md` |
| Leadership updates | `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/` |
