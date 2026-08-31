# Regression Run Evidence

Maven batch-run logs and summary CSVs captured during QC4 and Stage1 validation sessions. **Do not commit these to `api-test-automation`** — store here only.

## Files

| File | Environment | Notes |
|------|-------------|-------|
| `qc4-module-suites-results.csv` | QC4 | Per-profile pass/fail summary (Jul 2026) |
| `qc4-module-suites-results.log` | QC4 | Full console output |
| `qc4-all-suites-results.log` | QC4 | Batch runner output |
| `qc4-master-regression-run.log` | QC4 | Master regression |
| `qc4-contribution-regression.log` | QC4 | Contribution failures (pre-fix) |
| `qc4-contribution-regression-after-fix.log` | QC4 | Contribution re-run |
| `dashboard-regression-qc4.log` | QC4 | Dashboard regression |
| `stage1-module-suites-results.csv` | Stage1 | Per-profile summary |
| `stage1-module-suites-results.log` | Stage1 | Full console |
| `stage1-all-suites-results.log` | Stage1 | Batch runner |
| `stage1-master-regression-run.log` | Stage1 | Master regression |
| `stage1-*-nmd-*.log` | Stage1 | NMD IDP master reruns |
| `stage1-mobile2-*.log` | Stage1 | Mobile2 Stage1 runs |
| `stage1-contribution-regression.log` | Stage1 | Contribution |

## How to regenerate

From `qa-automation-kb`:

```powershell
.\programs\unite-msc\api-test-automation\scripts\run-qc4-all-suites.ps1
.\programs\unite-msc\api-test-automation\scripts\run-stage1-all-suites.ps1
```

Copy new `mobile/*.log` and `mobile/*.csv` outputs here, then delete from `api-test-automation/mobile/`.

## Sign-off use

Link these artifacts in endpoint mapping sign-off docs under `docs/06-coverage/` and refresh `mappings/*.csv` after a green run.

See [Cursor prompt — endpoint sign-off documentation](../docs/06-coverage/CURSOR-PROMPT-endpoint-signoff-documentation.md) for building the full sign-off package.
