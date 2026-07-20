# Metrics verification checklist — 2026-07-17 leadership update

Use this list to replace **TBD** values in the leadership pack before the next meeting.

---

## Mobile 2 endpoint coverage

| Metric | Current in pack | Verification action | Command / file |
|--------|-----------------|---------------------|----------------|
| Automated endpoint count | 22 verified; 24 projected | Re-count from coverage matrix after `main` pull | Read `16-mobile2-coverage-matrix.md`; update rows for YTD + `GET mobilebanks/{id}` |
| Coverage % | 88% verified | Recalculate automated ÷ 25 | Manual from matrix |
| Master class count | 34 vs 36 conflict | Count `<class name=` in master XML | `rg '<class name=' mobile/mobile2/testsuites/master-regression-testng.xml` |
| QC4 master pass | TBD | Run batch script | `.\mobile\project-documents\scripts\run-qc4-all-suites.ps1` |
| Stage 1 master pass | 36/40 (stale) | Run batch script | `.\mobile\project-documents\scripts\run-stage1-all-suites.ps1` |
| Open MR count | TBD | GitLab MR filter | `gitlab` UI or `git log origin/main..HEAD` per branch |

---

## Mobile 1

| Metric | Verification |
|--------|--------------|
| Endpoint count still 27 | Re-open Dinesh workbook `API Endpoints - Mobile1.xlsx` (**not in repo — export required**) |
| Auth test pass QC4 + Stage 1 | `mvn -f mobile/mobile1/pom.xml test -Pmobile1-auth-regression -Pacceptance-qc4` |
| M1 sprint stories | Jira AMSQUAD 26.11 export |

---

## Performance

| Metric | Verification |
|--------|--------------|
| Scenario count | List `performance/mobile/unite-msc/jmeter/*.jmx` on perf repo |
| Jobs scheduled vs ad hoc | Jenkins `AGSUP_UNITE_MSC_ENDURANCE` configure page |
| QA-1228 status | Jira sprint board |
| Last successful MSC perf run | Jenkins build history link |

---

## Pipeline

| Metric | Verification |
|--------|--------------|
| GHA last green run | GitHub Actions workflow URL (**TBD** — workflow may live outside api-test-automation clone) |
| Nexus artifact version | `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md` §3 |
| GitLab nightly exists? | GitLab CI/CD schedules — expect **No** until story done |

---

## V2/V3 UI

| Metric | Verification |
|--------|--------------|
| Nightly pass rate | qTest or Jenkins nightly export |
| Open automation defects | Jira filter |
| V2/V3 scoped counts | `universal-platform-coverage/01-analysis/10-reconciliation-ledger.md` |

---

## GitLab data required (if web/API unavailable)

Export or screenshot:

1. Open MRs for `api-test-automation` — assignee, target branch, pipeline status
2. AMSQUAD Sprint 26.11 burndown / committed vs completed
3. Last 2 weeks commits by: Swapnil Patil, Dinesh Kumar, Venkatesh Mallela, Priti Choudhary, Sunil Godiyal
4. Jenkins Performance view job status screenshots
5. Prime/GitLab nightly job `.gitlab-ci.yml` reference for Mobile 2 story

---

## Sign-off gate checklist

- [ ] `main` @ commit hash recorded in updated sign-off doc
- [ ] QC4 master regression HTML report attached
- [ ] Stage 1 master regression HTML report attached
- [ ] Contribution Stage 1 failure root-caused (fixture vs app bug)
- [ ] Leadership sign-off email sent with `17-mobile2-api-automation-signoff.md` link

---

## Owner

| Area | Owner |
|------|-------|
| M2 metrics refresh | Swapnil Patil |
| M1 sprint metrics | Swapnil + M1 dev assignee TBD |
| Perf metrics | Priti Choudhary |
| Pipeline / nightly | Chaitanya + DevOps |
| V2/V3 nightly | UI automation lead **TBD** |
