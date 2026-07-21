# Final Response — Michael Blake

**Subject:** Government Savings automation coverage, CI gates, and code-coverage controls  
**As of:** 2026-07-21 (revalidated: `api-test-automation` @ `cee0de9`, `prime-test-automation` @ `93f8628`, UniteMSC services)  
**Metric authority:** `03-analysis/verified-metrics-register.csv`

---

Michael,

Thank you for the questions. After revalidating repositories, pipeline YAML, and our verified metrics register: **there is no single Government Savings-wide automation or code-coverage percentage.** We report platform-specific metrics separately (implementation, execution, CI integration, and gates).

## Answers to your questions

**1. How much automated testing coverage do we have?** Platform-specific only. Mobile 2 API: **96% implemented** (24/25 endpoints in code); last documented execution **88% (22/25, stale 2026-07-14)**. Mobile 1 API: **22% implemented (6/27)**; **3.7% execution-verified**. V3 UI nightly inventory share **86.9% (379/436 TestNG methods)**. V2 UP-scoped qTest share **36% (268/744, stale export 2026-06-29)**. Application JaCoCo exists on UniteMSC services; this is a different metric from business test automation.

**2. Integrated CI gates now, or environment pipelines?** Both, by design. **Merge-request gates:** protected `main`, successful MR pipeline, Snyk, dual approval (including senior Code Review), discussion/change-request blocks, and related merge rules. **Environment/scheduled gates:** V3 UI and metadataweb API GitLab nightlies hard-fail on test failure; GitHub Actions validates the Mobile 2 Dashboard deployment slice; Jenkins runs performance and legacy V2 jobs.

**3. How are we tracking code coverage across repositories automatically?** **Partially.** UniteMSC services generate JaCoCo in CI; SonarQube is disabled (`RUN_SONARQUBE: false`). There is no central dashboard or automated cross-repo register today. QA automation repos do not measure application line coverage.

**4. Can we automatically reject a merge if code coverage decreases?** **Not today.** No verified repository compares branch coverage to `main`, publishes a required MR coverage check, and blocks merge on regression.

**5. Can authorized people override the gate?** **General merge bypass exists** (senior Code Review approvals). There is **no coverage-specific bypass with recorded justification and audit trail** today.

**6. Which repositories have this control?** **Zero** have a verified full coverage-delta merge gate. Some UniteMSC POMs define static JaCoCo thresholds (e.g., `unite-mobile2` 90%); most use 0%. These are not branch-vs-main regression gates.

## Recommended approach

Retain existing protected-branch, pipeline, Snyk, and senior-review controls. Add a **repository-specific** check measuring changed-code coverage and preventing material regression against `main`. Pilot on `unite-mobile2`: informational reporting first, then a required merge check after threshold tuning. Configure a restricted, auditable exception group.

In parallel, extend existing Python utilities into a read-only coverage register reconciling Jira scope, qTest inventory, repository implementation, and CI execution — without combining metrics into one number.

## Leadership support needed

1. Approve **domain-specific denominators** (not one enterprise %).  
2. Provision **read-only** qTest, Jira, and GitLab API access.  
3. Sponsor **QA-1405** (Mobile 2 API nightly) and a **named exception-approval group**.

Supporting artifacts: decision brief, repository matrix, and 30/60/90 plan. Happy to walk through on a call.

Regards,  
QA Automation
