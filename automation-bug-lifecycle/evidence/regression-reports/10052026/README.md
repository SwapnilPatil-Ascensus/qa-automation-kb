# Evidence Folder — 10052026

Regression failure evidence for **Member Personal Info Update**.

## Checklist

- [x] Screenshot(s) — `MemberPersonalInfo_EditContact_SomethingWentWrong.png`
- [ ] Exception log — linked from GitLab artifacts (not downloaded locally)
- [ ] Test data — linked from GitLab artifacts (PII not copied into repo)
- [ ] Console / job log — GitLab job `16928002062`
- [x] TestNG report URL noted below
- [x] Bug doc created — `10052026_MemberPersonalInfo_SubmitError.md`

## Key dates

| Field | Value |
|-------|-------|
| Failure detected | 10/05/2026 |
| Last known green run | [NEED_INPUT] |
| Environment | Stage 1 |
| Plan | NYD |
| Suite | V3 Unite |

## TestNG / CI report

- Job: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts
- Failed HTML: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646278.MemberPersonalInformation.feature_html_chrome_failedresult.html
- Exception: https://ascensus-gs.gitlab.io/-/products/depot/qa-automation/prime-test-automation/-/jobs/16928002062/artifacts/unite/unite/target/surefire-reports/nyd.20261005032646302.MemberPersonalInformation.feature_exception_failedresult.txt

## JIRA

[QA-2315](https://ascensuscollegesavings.atlassian.net/browse/QA-2315)

## Next steps

1. Triage complete — functional defect
2. Prompt H bug doc created
3. Change set — GitLab Project Manager + `prompts/03-gitlab-change-set.md` (last green → job 16928002062)

**Do not commit secrets, tokens, or customer PII.**
