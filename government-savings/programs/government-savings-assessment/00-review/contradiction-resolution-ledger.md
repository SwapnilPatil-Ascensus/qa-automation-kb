# Contradiction Resolution Ledger

**Re-audit date:** 2026-07-20 (rebuild for 2026-07-21 leadership review)  
**Status key:** Verified · Pending verification · Corrected · Unknown

| ID | Topic | Old claim (prior assessment) | Evidence | Corrected claim | Status | Reason |
|----|-------|------------------------------|----------|-----------------|--------|--------|
| C-01 | Mobile 2 coverage | 24/24 = **100%** in-scope | Sign-off **22/25 = 88%** @ `7ccaf46` (2026-07-14); code @ `cee0de9` adds YTD + `GET mobilebanks/{id}` | **Verified: 22/25 (88.0%)** · **Pending sign-off: 24/25 (96.0%)** projected | **Corrected** | Removed denominator manipulation excluding `mobilemembers`; helper endpoint stays out of automation numerator per sign-off |
| C-02 | Mobile 2 superseded | "88% superseded by code review" | Leadership baseline + sign-off path incomplete | **88% remains verified leadership baseline**; 96% is **pending** only | **Corrected** | Sign-off requires MR merge matrix refresh QC4/Stage1 rerun |
| C-03 | Mobile 1 coverage | **6/27 = 22.2% verified** | Workbook lists 1 automated @ 2026-07-09; 5 new classes on `main` @ `cee0de9` without QC4/Stage1 evidence | **Verified: 1/27 (3.7%)** · **Implemented pending: 5 endpoints (potential 6/27)** | **Corrected** | Code ≠ verified sign-off metric |
| C-04 | GitHub Actions | "Not implemented / not in repo" | `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md`; leadership pack Chaitanya validation | **Dashboard vertical slice externally validated**; module expansion in progress; workflow repo **not in audit clone** | **Corrected** | Separate from GitLab nightly regression |
| C-05 | CI "hard gate" | V3/metadataweb labeled **hard gate** implying merge block | `.gitlab-ci.yml` uses `only: schedules`; fails job on test errors | **Scheduled regression — hard-fail on run**; **not verified MR/deployment gate** | **Corrected** | Scheduled failure ≠ merge gate |
| C-06 | V2 recurring | Implied "verified recurring regression" | Jenkins job name/schedule not in repo; qTest PDF only | **Automation exists; recurring schedule Unknown** | **Corrected** | Ant targets documented; live Jenkins TBD |
| C-07 | Metadata API scope | "~269 methods" mixed with UP headline | Only `scheduled_metadataweb_stage1` in GitLab CI | **Metadataweb module on schedule**; other universal modules manual only | **Clarified** | Scope conclusion to scheduled job only |
| C-08 | ASTRO recurring | Listed with other GS areas without schedule proof | `ASTRO-TB-REFRESH` prep only; no nightly GitLab | **Automation exists; recurring execution not verified** | **Clarified** | No schedule evidence |
| C-09 | Backoffice vs nightly | 1077 scenarios inventory | Not in V3 GitLab `scheduled_regression_job` | **Large inventory; active nightly subset unverified** | **Clarified** | Separate from V3 nightly population |
| C-10 | COPACS | "COPACS" spelling inconsistent | No repo in reviewed set | **COPACS — scope Unknown; no validated automation identified** | **Clarified** | Requires platform owner |
| C-11 | JaCoCo/Sonar | Mixed with QA coverage % | `RUN_SONARQUBE: false`; JaCoCo on UniteMSC POMs | **Application source-code coverage: partial on services; not QA business metric; no Sonar gate** | **Clarified** | Metric type separation |

## Leadership narrative (approved wording)

The team has meaningful automation across Government Savings. The current limitation is not the ability to build automation; it is establishing a consistent, traceable coverage model across Jira, qTest, repositories, and CI execution. We can report verified platform-specific metrics now, but we should not publish one GS-wide percentage until the denominators and pipeline evidence are governed.
