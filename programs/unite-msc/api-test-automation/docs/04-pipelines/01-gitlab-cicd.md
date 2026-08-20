# GitLab CI/CD

Root `.gitlab-ci.yml` includes:

```yaml
include:
  - project: ascensus-gs/products/depot/qa-automation/includes
    file: .gitlab-ci.yml
```

Mobile job definitions and `PROFILE` values live in the **includes** project. Check `ascensus-gs/products/depot/qa-automation/includes` for current mobile regression jobs.

## Local repo examples

- `prepare` — Stage1 DB secure files
- `scheduled_metadataweb_stage1` — scheduled metadataweb profile
- `mobile2_dashboard_regression_stage1` — Mobile 2 dashboard regression (Stage1 nightly); see [Mobile MSC nightly regression CI](04-mobile-msc-nightly-regression-ci.md)

## Mobile2 via Nexus (GitHub Actions consumers)

See [GitHub Actions + Nexus pipeline](02-github-actions-nexus-pipeline.md).

## Regression support

1. Reproduce locally with module README command
2. Full QC4 batch: [scripts/run-qc4-all-suites.ps1](../../scripts/run-qc4-all-suites.ps1)
3. Stage1: [scripts/run-stage1-all-suites.ps1](../../scripts/run-stage1-all-suites.ps1)
