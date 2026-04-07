# Prime V3 Regression Documentation

**↑ Parent hub:** [Automation Regression Suite – docs hub](../README.md) · [full master TOC](../00-automation-regression-master-overview.md)

V3 Stage 1 front-office regression documented here focuses on the **combined** run: **Universal Enrollment** + **IDP Login**, driven by `suites/v3/stage1-regression-master.xml` and reported in a single TestNG HTML export.

**Confluence-style pages:** [modules/README.md](modules/README.md)

| Role | Document |
|------|----------|
| Parent (overview + combined metrics) | [modules/00-stage1-v3-combined-overview.md](modules/00-stage1-v3-combined-overview.md) |
| IDP Login (child) | [modules/01-idp-login-stage1.md](modules/01-idp-login-stage1.md) |
| Universal Enrollment (child) | [modules/02-universal-enrollment-stage1.md](modules/02-universal-enrollment-stage1.md) |

---

## GitLab pipeline & report URL

See **[modules/00-stage1-v3-combined-overview.md](modules/00-stage1-v3-combined-overview.md)** for:

- Nightly pipeline link (e.g. `#2397275412`)
- Jobs: **`prepare`**, **`scheduled_regression_job`**
- TestNG report URL pattern with `[JOB_ID]` (example job `13573736461`)

**Automation repo suite paths (source of truth):** `bin\regression\daily\stage1-regression-master.xml`, `universal-enrollment-stage1.xml`, `idp-login-stage1.xml` in **prime-test-automation**.

---

## Suite XMLs (KB mirror)

Located at: `suites/v3/` (mirrors `bin\regression\daily\` in the automation repo)

| XML | Role |
|-----|------|
| `stage1-regression-master.xml` | Master: includes UE then IDP |
| `universal-enrollment-stage1.xml` | UE only (26 tests) |
| `idp-login-stage1.xml` | IDP only (13 tests) |

---

## Reports

**Folder:** `reports/v3/` — keep **HTML exports only** (see `reports/v3/README.md`).

| File |
|------|
| `Regression Test (Front Office) in Stage1 - IDP Login & UE.html` |
| `Regression Test (Front Office) in Stage1 - IDP Login & UE 2.html` |
| `Regression Test (Front Office) in Stage1 - IDP Login & UE 3.html` |

---

## Related PDFs

| Resource | Location |
|----------|----------|
| **Master Overview (all suites)** | `AM_Regression_Reports/reports/Automation Regression Suite – Master Overview.pdf` |
| V3 Overview (Confluence archive) | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/2. Unite  Prime V3 Regression Suite – Overview.pdf` |
| UE Coverage (Confluence archive) | `10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/regression-master-overview/2.1. Universal Enrollment Regression Coverage – Prime V3.pdf` |

---

*Broader V3 counts (e.g. 325+ TCs including CSR) may include scopes outside these three XML files — align with your GitLab pipeline and leadership slides.*
