# ASTRO / SFRP — Reactivation Assessment

**As of:** 2026-07-21  
**Repositories:** `astro-test-automation` (Ant/Cucumber), `api-test-automation/astro/` (API)

---

## Executive summary

ASTRO has a **substantial existing automation asset base** (391 feature files in the current repository scan). **Recurring execution has not been verified** in this assessment pass. Suites require **revalidation, environment readiness, and a governed schedule decision** before they can be represented as active regression coverage.

**Do not** present ASTRO as "~75–80% complete" without an approved business denominator. That figure is **not substantiated** in current evidence.

---

## Inventory (verified from repository code)

| Asset | Count | Unit | Status |
|-------|------:|------|--------|
| UI feature files | 391 | Cucumber `.feature` | Verified from repository code |
| UI scenarios (prior scan) | ~1,236 | scenario lines | Historical scan — reconfirm if needed |
| API test classes | 5 | TestNG classes | Verified in `api-test-automation/astro/` |
| Business functions covered | ORS, CAS, ILS, employer/employee flows, payroll, contributions, withdrawals, CSR panels | qualitative | Verified from testsuite tree |

---

## Major business functions (qualitative)

- Employer: payroll, employees, representatives  
- Employee: registration, contributions, withdrawals, profile/security  
- CSR: employer and employee profile, panel operations  
- Backoffice: ORS operational flows (per testsuite structure)

---

## Execution status

| Item | Finding | Evidence |
|------|---------|----------|
| Recurring nightly | **Not verified** | No GitLab schedule; not in V3 `scheduled_regression_job` |
| Testbed refresh | `ASTRO-TB-REFRESH` referenced | Environment prep only — not regression gate |
| Latest execution evidence | **Unknown** in current pass | No fresh Jenkins console in workspace |
| Disabled / inactive suites | Not fully audited line-by-line | Sample suites show commented parallel configs |

---

## Framework health

| Area | Assessment |
|------|------------|
| Framework | Ant + TestNG + Cucumber — mature legacy pattern |
| Environment | TB1 / Stage1 dependency; TB refresh required before runs |
| CI integration | Jenkins/Ant — **not** on Modern Unite GitLab nightly |
| Ownership | QA Automation (legacy squad) + program SME for scope |

---

## Leadership-safe wording

> "ASTRO has a substantial existing automation asset base, but recurring execution has been inactive and the suites require revalidation before they can be represented as active regression coverage."

**Differentiate:**
- **Asset coverage** — extensive code exists  
- **Active execution coverage** — not demonstrated on a recurring schedule today

---

## Effort to restore regression (order of magnitude)

| Phase | Activity | Owner | Horizon |
|-------|----------|-------|---------|
| 1 | Scope confirmation with business (in/out of GS priority) | Program + SME | 2–4 weeks |
| 2 | TB refresh + smoke run on representative suite | QA | 1–2 weeks |
| 3 | Identify disabled/quarantined scenarios | QA | 2–3 weeks |
| 4 | Jenkins schedule reactivation or GitLab migration decision | DevOps + QA | 4–8 weeks |
| 5 | qTest / traceability refresh | QA Governance | Parallel |

**Estimated effort:** 1–2 sprints for assessment + smoke; 1–2 quarters for full governed nightly if approved.

---

## Dependencies

- ASTRO testbed availability (TB1)  
- Business priority vs Universal Platform / Legacy Unite  
- Jenkins job naming and schedule confirmation  
- Ownership for ongoing maintenance

---

## Recommended actions

1. Leadership decision: ASTRO in/out of GS active regression scope  
2. Run controlled smoke on frontoffice ORS employer/employee paths  
3. Publish module-level execution baseline  
4. Link to qTest inventory where case IDs exist  
5. Do not count ASTRO assets in Modern Unite nightly metrics

---

*Cross-reference: `government-savings-business-coverage-register.csv`, `legacy-unite-module-status.csv`*
