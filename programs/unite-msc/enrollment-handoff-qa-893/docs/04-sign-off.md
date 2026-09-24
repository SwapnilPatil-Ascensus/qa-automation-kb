# Enrollment API automation — sign-off

**QA-893 / QA-2043** · **As of:** 2026-09-14  
**Determination:** COMPLETE for MSC happy path + subsequent enrollment on **OK Direct** and **New York**. Conditional on named approvers.

## Scope statement

25 Java-automated endpoints / 28 catalog rows (89%). Core wizard 15/15. Three rows deferred (partner submit, Upromise, OAuth). Subsequent beneficiary / bank / recurring exist in Java but were missing from the original Excel catalog.

## Coverage KPIs

| Metric | Value |
|--------|--------|
| Catalog rows | 28 |
| Automated | 25 |
| Deferred | 3 |
| Test classes | 23 + EnrollmentBaseTest |
| @Test methods | 25 |
| Plants in CI | okdirect, newyork |
| Plants local only | nmdirect |
| GitLab nightly | Not created |

## Migration

| Kind | Count |
|------|--------|
| Migrated from legacy Cucumber/Postman | ping, plans, prospects, owner, beneficiary, bank-entered (and related) |
| New in MSC TestNG | liveness, certificate, states, country, content, enrollmentstarted, owner-address, routing verify, recurring, allocation funds, review-confirm, subsequent APIs |

## Exclusions (not defects)

| Item | Ticket / reason |
|------|-----------------|
| POST `/enrollments/submit` | QA-1808 partner |
| GET `/upromiseaccount` | QA-1807 |
| POST `/oauth/token` | Not MSC E2E |
| Negative payloads | Enhancement for receiving team |
| nmdirect in CI | Follow-up story |
| Enrollment GitLab nightly | Follow-up story |

## Target-plan evidence

| Plant | Regression / integration |
|-------|--------------------------|
| OK Direct | Yes — coded in suite XML |
| New York | Yes — coded in suite XML |
| NM Direct | localhost example only |

Store dated HTML in `api-test-automation/evidence/regression-runs/` when a Stage1 run is captured. Independent reviewer must confirm commands (QA-2047).

## Approvals

| Role | Name | Date |
|------|------|------|
| QA Automation Lead | `[NEED_INPUT]` | |
| Program / ACM | `[NEED_INPUT]` | |
| Engineering | `[NEED_INPUT]` | |
| Support | `[NEED_INPUT]` | |

Full endpoint table: `mappings/enrollment-endpoint-current-state.csv`.
