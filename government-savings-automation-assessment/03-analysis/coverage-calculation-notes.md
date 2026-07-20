# Coverage Calculation Notes

**Assessment date:** 2026-07-20  
**Principle:** Percentages are reported only where numerator, denominator, and counting unit are documented.

---

## 1. What we measure vs what we do not

| Metric type | Measured in this assessment? | Evidence |
|-------------|------------------------------|----------|
| **Business / test automation coverage** | Yes — primary metric | Endpoint matrices, qTest/TestNG inventories, suite XML |
| **Application source-code coverage (JaCoCo/Sonar)** | Noted separately | UniteMSC POMs; `RUN_SONARQUBE: false` on service CI |
| **Pipeline quality gates** | Yes — execution model | `.gitlab-ci.yml`, Jenkins tracker, Ant targets |
| **Manual test coverage** | Excluded | qTest manual cases not counted as automated |

**Leadership clarification for Michael Blake:** If "code coverage" means JaCoCo on application repos, that is **not** the same as automated business scenario coverage. No verified **QA automation pipeline** enforcing application code-coverage thresholds was identified. Service repos may run unit tests in build pipelines; Sonar is disabled in reviewed UniteMSC template variables.

---

## 2. Verified percentages (defensible)

### Universal Platform — V2 UI (inventory share)

| Field | Value |
|-------|------:|
| Numerator | 268 executed qTest cases mapped to UP workstreams |
| Denominator | 744 executed qTest cases (V2 source population) |
| **Result** | **36.0%** inventory share |
| Basis | `universal-platform-coverage/01-analysis/10-reconciliation-ledger.md` |
| SME sign-off | July 1, 2026 |
| **Not** | Requirement-level or functional completeness % |

### Universal Platform — V3 UI (inventory share)

| Field | Value |
|-------|------:|
| Numerator | 379 TestNG methods (UE 303 + IDP Login 56 + Member Withdrawal 20) |
| Denominator | 436 TestNG methods in nightly source population |
| **Result** | **86.9%** inventory share |
| Basis | Same reconciliation ledger |
| Execution | GitLab `scheduled_regression_job` on `prime-test-automation` |

### Unite MSC — Mobile 2 API (endpoint automation)

| Field | Value |
|-------|------:|
| Numerator | 24 automated business endpoints (L3+ TestNG) |
| Denominator | 24 in-scope (25 documented minus `mobilemembers` exclusion) |
| **Result** | **100%** in-scope endpoint automation |
| Evidence | `api-test-automation` @ `cee0de9` — 20 test classes, dynamic contribution fixture |
| Prior baseline | 88% (22/25) @ `7ccaf46` on 2026-07-14 — **superseded** by code review 2026-07-20 |
| CI integration | **0%** scheduled — nightly job not in `.gitlab-ci.yml` (QA-1405 pending) |

### Unite MSC — Mobile 1 API (endpoint automation)

| Field | Value |
|-------|------:|
| Numerator | 6 endpoint identities with canonical tests |
| Denominator | 27 documented business endpoints (Dinesh workbook — **workbook not in repo**) |
| **Result** | **22.2%** (6÷27) |
| Endpoints | session, owner, owner menu, profile menu, beneficiary by ext, bank info by routing |
| Evidence | `mobile/mobile1/src/test/java` @ `cee0de9` |
| Prior baseline | 3.7% (1/27) — **superseded** |

### Universal Platform — API operations

| Field | Value |
|-------|------:|
| Numerator | 11 unique HTTP operations (Enrollment 5, IDP 4, Withdrawal 2) |
| Denominator | UP-scoped operation catalog only |
| **Result** | TBD % of full GS API surface |
| Basis | `universal-platform-coverage/01-analysis/csv/api-operation-mapping.csv` |

### Performance — business journeys

| Field | Value |
|-------|------:|
| Numerator | 15 in-scope journeys (UP ledger) |
| Denominator | 36 JMX / 53 Taurus assets total |
| **Result** | Journey-level inventory — not % of GS performance scope |
| MSC-specific | 6 JMX under `performance/mobile/unite-msc/` — manual Jenkins job only |

---

## 3. TBD — denominator not verified

| Area | Why TBD |
|------|---------|
| Full V2 Unite UI | 2,176 scenarios exist; no approved GS business denominator |
| V2 backoffice only | 1,077 scenarios — scope vs nightly subset unclear |
| ASTRO/SFRP | 1,236 scenarios — not mapped to leadership scope |
| COPACS | No automation repository identified |
| Full GS microservice API catalog | Universal modules exceed UP 11-operation subset |
| qTest approved in-scope cases | Exports not refreshed in this assessment |
| Current V2/V3 nightly **pass rates** | Requires live GitLab/Jenkins artifact refresh |

---

## 4. Rules applied

1. **Do not sum V2 + V3** — different frameworks; overlapping journeys possible.
2. **Do not use inventory-share % as requirement coverage** (UP assessment rule).
3. **PUT/DELETE banks + DELETE contribution** count as automated but excluded from master regression by design.
4. **Service-level Cucumber** in UniteMSC ≠ BFF acceptance in `api-test-automation`.
5. **Code in repo ≠ scheduled regression** — execution model column required in matrix.

---

## 5. Recommended leadership-safe statements

**Safe:**
- "V3 Universal Experience has a **verified GitLab nightly regression** on Stage 1 with **379 scoped TestNG methods** in the scheduled master suites."
- "Mobile 2 API automation covers **all 24 in-scope documented endpoints** in canonical TestNG; **nightly GitLab scheduling is pending** DevOps (QA-1405)."
- "Mobile 1 API automation has advanced to **6 of 27** documented endpoints (**22%**), up from 1 endpoint in July."

**Avoid without refresh:**
- "Government Savings has X% total test coverage."
- "863 UI tests all pass nightly" (historical Apr 2026 demand-planning figure).
- "GitHub Actions validates Mobile 2" (workflow file not present in repo).

---

*Cross-reference: `government-savings-coverage-matrix.csv`, `evidence-register.md`*
