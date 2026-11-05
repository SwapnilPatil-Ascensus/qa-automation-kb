# Enrollment — execution and troubleshooting

**QA-893 / QA-2041**

## Run (from `api-test-automation` root)

Smoke (Stage1):

```powershell
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=LT12800.properties"
```

Regression (Stage1 — replace host file with yours):

```powershell
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=LT12800.properties"
```

Integration (QC4):

```powershell
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-integration,acceptance-qc4" "-Denvironment.properties=qc4.properties" "-Dhost.properties=qc4.properties"
```

CI uses the **same** profiles with controlled secure files. Enrollment nightly is not present in current `.gitlab-ci.yml`; do not claim a Mobile 2 or Enrollment nightly without verifying the current job and schedule.

## First failure — classify

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| 401 / decrypt error | Wrong cert, double encrypt, stale JWT | New prospect; encrypt from plaintext |
| 426 | x-app-version too low | Use 1.8.0+ or plan SQL min version |
| Timeout to Oracle | Relay/access or personal overlay unavailable | Verify approved relay access and local overlay; do not share values |
| 500 on prospect | Extra owner fields / empty body | Minimum prospect payload |
| Class skipped in regression | Test group `functional` | `MobileMemberSessionRequestTest` is smoke-only |
| nmdirect missing | Not in CI XML | Known gap — not a product defect |

## Reports

Open HTML under `mobile/enrollment/target/` (or shared `mobile-ms-report` if wired). Never commit `target/`. Never paste Bearer tokens into tickets.

Evidence for sign-off: keep dated HTML in GitLab `api-test-automation` (do not commit `target/`).
