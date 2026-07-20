# Evidence Register

**Assessment date:** 2026-07-20  
**Rebuild validated:** 2026-07-21

| ID | Conclusion | Evidence type | Path / reference | Commit / date | Confidence |
|----|------------|---------------|------------------|---------------|------------|
| E-001 | V3 GitLab scheduled regression | Pipeline YAML | `prime-test-automation/.gitlab-ci.yml` | 2026-07-20 | High |
| E-002 | V3 scoped 379 TestNG methods | Reconciliation ledger | `universal-platform-coverage/.../10-reconciliation-ledger.md` | SME 2026-07-01 | High |
| E-003 | V2 UP 268 qTest cases | Reconciliation ledger | Same | 2026-06-29 Stale | High |
| E-004 | Metadataweb API scheduled GitLab | Pipeline YAML | `api-test-automation/.gitlab-ci.yml` | 2026-07-20 | High |
| E-005 | Mobile 2 **22/25 verified 88%** | Sign-off package | `.../17-mobile2-api-automation-signoff.md` | `7ccaf46` 2026-07-14 | **High — leadership baseline** |
| E-006 | Mobile 2 YTD + banks GET in code | Code scan | `MobileYtdSummaryRequestTest`, `getMobileBankById` | `cee0de9` 2026-07-20 | Medium — pending sign-off |
| E-007 | Mobile 1 **1/27 verified** | Workbook matrix | `03-document-postman-coverage-matrix.md` | 2026-07-09 | High |
| E-008 | Mobile 1 five endpoints in code | Code scan | `mobile/mobile1/src/test/java` | `cee0de9` | Medium — pending evidence |
| E-009 | Mobile 2 nightly NOT in GitLab | YAML absence | `api-test-automation/.gitlab-ci.yml` | 2026-07-20 | High |
| E-010 | GHA Dashboard slice validated | Leadership pack + Nexus doc | `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md` | 2026-07 | Medium — external |
| E-011 | GHA workflow repo not in clone | Audit limitation | No `.github/workflows` in api-test-automation | 2026-07-20 | High |
| E-012 | JaCoCo on UniteMSC; Sonar off | POM + CI | `unite-mobile1/.gitlab-ci.yml` | 2026-07-20 | High |
| E-013 | **Rejected:** M2 24/24 = 100% | Prior assessment error | Contradiction ledger C-01 | — | — |
| E-014 | **Rejected:** M1 6/27 verified | Prior assessment error | Contradiction ledger C-03 | — | — |

## Evidence not obtained

1. Live GitLab schedule screenshots  
2. Fresh Mobile 2 QC4/Stage 1 master run post-`cee0de9`  
3. GHA workflow repository URL  
4. Jenkins V2 UI job name + schedule  
5. qTest/Jira live API exports  
