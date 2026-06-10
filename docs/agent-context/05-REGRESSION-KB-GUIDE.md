# Regression KB Guide

The **primary regression documentation** lives under:

`10_IMPORTS_RAW/AM_Regression_Reports/`

This is the most content-rich and frequently updated area of the repo.

---

## Hub entry points

| Audience | Start here |
|----------|------------|
| Full TOC (V2 + V3 + mermaid map) | `docs/00-automation-regression-master-overview.md` |
| Doc hub index | `docs/README.md` |
| Folder README | `AM_Regression_Reports/README.md` |
| Prime V2 nightly | `docs/v2/README.md` |
| Prime V3 Stage1 (UE + IDP) | `docs/v3/README.md` |
| CI/CD landscape | `docs/CICD/01-master-qa-automation-cicd-landscape.md` |

---

## V2 regression (Prime V2 — Legacy, still active)

**Environment:** Stage1  
**CI:** Jenkins (Ant-based)  
**Role:** Main monolith regression gate for Unite / legacy UI / CSR flows

### Structure

```
AM_Regression_Reports/
├── docs/v2/
│   ├── 00-v2-regression-overview.md      ← purpose, schedule, env
│   ├── 01-v2-module-coverage.md          ← coverage by module
│   ├── 02-v2-suite-and-job-details.md    ← XML ↔ Jenkins mapping
│   ├── 03-v2-documentation-delta.md      ← vs legacy Confluence PDFs
│   └── modules/
│       ├── 01-enrollment.md
│       ├── 02-withdrawals.md
│       ├── … (14 modules total)
│       └── 14-other-specialty.md
└── suites/v2/
    ├── daily/          ← nightly suites
    ├── smoke/
    ├── release/
    ├── weekly/
    └── archive/
```

### V2 modules (14)

| # | Module file | Typical area |
|---|-------------|--------------|
| 01 | enrollment | Universal Enrollment |
| 02 | withdrawals | Withdrawals |
| 03 | login-idp | IDP Login |
| 04 | csr-maintenance | CSR Account Maintenance |
| 05 | contributions | Contributions |
| 06 | transfers | Transfers |
| 07 | account-balance-page | Account Balance |
| 08 | sardine-regression | Sardine |
| 09 | investment-options | Investment Options |
| 10–14 | various | Specialty modules |

**When to open:** Nightly V2 failure triage, coverage reviews, Confluence paste for a module.

---

## V3 regression (Prime V3 — future-facing)

**Environment:** Stage1  
**CI:** GitLab CI (Maven-based, Nexus artifacts)  
**Scope:** Universal Enrollment + IDP Login (Stage1 combined)

### Structure

```
docs/v3/
├── README.md
└── modules/
    ├── 00-stage1-v3-combined-overview.md   ← parent Confluence page
    ├── 01-idp-login-stage1.md
    └── 02-universal-enrollment-stage1.md

suites/v3/
└── stage1-*.xml
```

**When to open:** V3 nightly failures, UE/IDP Stage1 pipeline work.

---

## CI/CD documentation

**Master:** `docs/CICD/01-master-qa-automation-cicd-landscape.md`

| Stream | Framework | Platform | Status |
|--------|-----------|----------|--------|
| V2 UI | Ant + TestNG + Cucumber + Selenium | Jenkins | Active (legacy label) |
| V3 UI | Maven + TestNG + Cucumber | GitLab CI | Active, expanding |
| API | REST Assured (TBD) | Pipeline exists | In progress / blocked |
| Performance | JMeter | Jenkins | Ad hoc → scheduling |
| Microservices | V3-related | GitHub Actions | Metadata MS |
| Mobile | TBD | Jenkins | Needs validation |

### Child pages

| File | Topic |
|------|-------|
| `02-automation-v2-pipelines.md` | V2 Jenkins details |
| `03-automation-v3-pipelines.md` | V3 GitLab details |
| `04-api-testing-pipelines.md` | API CI |
| `05-performance-testing-pipelines.md` | JMeter pipelines |
| `06-github-workflow-coverage.md` | GitHub Actions |
| `07-mobile-testing-pipelines.md` | Mobile Jenkins |
| `08-pipeline-support-devops-dependencies.md` | DevOps support |
| `09-pipeline-roadmap-future-state.md` | Future state |

**Important:** This repo does **not** contain Jenkinsfiles or GitLab CI YAML. Suite XML is reference only. Mark unconfirmed details as `NEEDS_VALIDATION`.

---

## TestNG reports

| Topic | Path |
|-------|------|
| Export/cleanup guide | `docs/GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md` |
| Reports storage | `reports/v2/`, `reports/v3/` — **gitignored** |
| Suite XML reference | `suites/v2/`, `suites/v3/` — **checked in** |

### Report workflow

1. Download HTML from Jenkins/GitLab
2. Clean duplicates, rename per guide
3. Optionally move under `reports/v2` or `v3`
4. Use in Prompt **I** to refresh module doc

---

## Module doc template

**Template:** `docs/TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md`

**Required sections:**
- Title block (module, XML, suite, framework, env, pipeline)
- Inputs table
- Suite at a glance
- Purpose
- Latest report summary
- Coverage summary
- Module & plan coverage table
- Test scenarios table
- What's covered
- Report & artifacts
- Notes

**Examples:** `v2/modules/01-enrollment.md`, `v3/modules/02-universal-enrollment-stage1.md`

---

## Bug evidence (separate from module docs)

**Location:** `10_IMPORTS_RAW/regression_reports/MMDDYYYY/`

| Content | Purpose |
|---------|---------|
| Screenshots, `.txt` logs | Evidence |
| `[date]_[Feature]_[Issue].md` | JIRA + email + Teams package |

**Not the same as** `04_EXECUTION/regression/` area rollup docs.

---

## Maintenance checklist

After regression doc changes:

- [ ] Module page updated (Prompt **I**)
- [ ] Parent indexes synced (Prompt **J**)
- [ ] Mermaid map in `00-automation-regression-master-overview.md` accurate
- [ ] Unconfirmed Jenkins/GitLab details marked `NEEDS_VALIDATION`
