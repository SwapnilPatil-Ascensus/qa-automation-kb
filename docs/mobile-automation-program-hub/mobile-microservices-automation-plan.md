# Mobile Microservices API Automation — Plan of Action

**Audience:** Leadership review (Raju)  
**Author:** QA Automation  
**Status:** Draft for review  
**Scope:** UniteMSC API automation — **not** Appium/BrowserStack mobile UI automation

---

## 1. Objective

We will create a **separate Mobile Microservices automation area** inside the **existing API Automation Framework**. This structure will centralize **UniteMSC API automation** under QA ownership while reusing proven framework patterns (Java, Cucumber, Rest Assured, Maven).

This initiative covers **API/microservices regression** for Unite Enrollment, Unite Mobile 1, and Unite Mobile 2. It does **not** include mobile UI automation (Appium, BrowserStack, or Node WebDriver), which remains a separate future workstream.

---

## 2. Background

Today, UniteMSC API automation lives **inside application development repositories**, co-located with service code. Typical assets include:

| Asset type | Description |
|------------|-------------|
| Cucumber feature files | BDD scenarios near application code |
| Java step definitions | Rest Assured–based API steps |
| Config / properties | Environment-specific settings |
| SQL scripts | Database validation and setup |
| Test data | Payloads, often embedded in feature files |

These assets were built and maintained primarily by development teams. Execution has been **inconsistent**, and coverage is difficult to trust as a regression signal.

**Goal:** Extract **useful, validated automation coverage** from application repos into a **centralized, QA-owned framework** — without modifying source application repositories (read-only reference during migration).

---

## 3. Why This Work Is Needed

| Current challenge | Impact | Planned solution |
|-------------------|--------|------------------|
| Tests are mixed with application code | Weak QA ownership; tests treated like dev integration tests; hard to maintain long term | Create dedicated `mobile-microservices/` area in API Automation Framework under QA ownership |
| Tests are not consistently executed | No reliable regression signal; failures go unnoticed until late in the cycle | Centralize suites with smoke/regression tags; run locally and via CI/CD |
| Feature files contain heavy data | Hard to read, reuse, and switch environments | Externalize large payloads to `test-data/` with logical names |
| Environment handling needs cleanup | QC4/Stage configs outdated or inconsistent; env-specific failures | Align with existing framework property patterns; validate per environment |
| Regression suite is not centralized | Fragmented coverage across repos; no single execution entry point | One framework location with module-based structure (Enrollment → Mobile 1 → Mobile 2) |
| Leadership visibility is limited | Progress, risks, and coverage hard to report | Trackers, phased milestones, and CI reporting for leadership status |

---

## 4. Target Framework Decision

We will use the **existing Java + Cucumber + Rest Assured API Automation Framework**. This aligns with current team skills, shared libraries (`json-api`, `jsonapi-parent`, config patterns), and migration sources in UniteMSC app repos.

| Option | Recommendation | Rationale |
|--------|----------------|-----------|
| **Existing Rest Assured framework** | **Recommended** | Lower risk; team already skilled; faster delivery; easier migration from existing Cucumber/Rest Assured tests in app repos |
| Playwright API | Not recommended now | New stack; retraining cost; no migration path from current assets |
| Karate | Not recommended now | Different syntax and patterns; would slow migration and split maintenance |
| New framework from scratch | Not recommended | Duplicates existing investment; longer timeline; unnecessary rework |

**Decision summary:** Extend the proven API Automation Framework with a new `mobile-microservices/` module tree rather than introducing a parallel technology stack.

---

## 5. Proposed Folder Structure

### Top-level layout (within API Automation Framework)

```
api-automation/
├── universal/
├── json-api/
└── mobile-microservices/
    ├── unite-enrollment/
    ├── unite-mobile1/
    └── unite-mobile2/
```

### Detailed module structure — Unite Enrollment (pilot)

```
mobile-microservices/
└── unite-enrollment/
    ├── src/test/java/com/ascensus/mobilemicroservices/enrollment/
    │   ├── runners/
    │   ├── stepdefs/
    │   ├── actions/
    │   ├── clients/
    │   ├── models/request/
    │   ├── models/response/
    │   ├── validators/
    │   └── db/
    └── src/test/resources/
        ├── features/enrollment/
        ├── test-data/enrollment/
        ├── sql/enrollment/
        ├── config/
        └── suites/
```

**Note:** Unite Mobile 1 and Unite Mobile 2 will follow the same structural pattern under their respective module folders once the Enrollment pilot is proven.

---

## 6. Design Principles

- Keep **source application repositories read-only** — no edits to application code during migration
- Do **not copy everything blindly** — evaluate each scenario before migration
- Start with **Unite Enrollment as the pilot module**
- Create the **framework skeleton first** before bulk scenario migration
- Add **one dummy smoke test first** to prove compile, run, and reporting path
- Migrate **3–5 vertical slice scenarios** before full module migration
- **Externalize large test data** from feature files into JSON/resources
- Keep **step definitions thin** — business flow readable in Gherkin
- Use **action / client / validator layers** for maintainability and reuse
- Apply **smoke and regression tags consistently** across all modules

---

## 7. Execution Phases

| Phase | Name | Description | Output |
|-------|------|-------------|--------|
| **0** | Framework Skeleton | Create `mobile-microservices/` parent and Unite Enrollment module structure; wire Maven to existing framework parent | Compilable module skeleton in API Automation Framework |
| **1** | Dummy Smoke Test | Add placeholder scenario with `@smoke` tag; prove local Maven execution and reporting | One passing (or compilable) smoke test; validated run command |
| **2** | Legacy Enrollment Discovery | Inventory feature files, steps, endpoints, SQL, configs, and test data in source app repo (read-only) | Legacy discovery report; migration tracker populated |
| **3** | Enrollment Vertical Slice | Migrate 3–5 high-value scenarios; stabilize on QC4 (and Stage1 as applicable) | Vertical slice green; pattern documented for team |
| **4** | Enrollment Full Migration | Migrate remaining approved scenarios; document exclusions | Full Enrollment regression suite with smoke/regression tags |
| **5** | Suite and Pipeline Integration | Validate Maven commands; integrate QC4 smoke and Stage1 verification in CI/CD | Pipeline runs smoke; reports published as artifacts |
| **6** | Repeat for Mobile 1 | Apply same discover → slice → full migration pattern | Mobile 1 smoke + regression suites executable |
| **7** | Repeat for Mobile 2 | Apply same pattern; address BFF/auth and cross-service dependencies | Mobile 2 smoke + regression suites executable |

---

## 8. Vertical Slice Strategy

Before full migration, we will migrate **only 3–5 high-value Unite Enrollment scenarios** to prove end-to-end feasibility:

| Capability | What we prove |
|------------|---------------|
| Request creation | Payloads build correctly from externalized test data |
| Auth / config loading | Environment properties load for QC4 (and Stage1 when ready) |
| Environment switching | Same scenarios run against different env configs without feature edits |
| Test data loading | Logical data names resolve from `test-data/` |
| Rest Assured execution | API calls execute through framework client/action layers |
| Response validation | Status codes and key JSON fields asserted reliably |
| SQL validation (if needed) | Optional DB assertions for records created by test |
| Maven execution | Module runs via standard Maven command with tag filters |
| Reporting | Results visible in framework reporting (local and CI artifacts) |

**Gate:** Vertical slice must be stable before bulk migration of remaining Enrollment scenarios.

---

## 9. Suite Strategy

| Suite | Tag | Purpose |
|-------|-----|---------|
| Smoke | `@smoke` | Fast critical validation — default for PR/merge feedback |
| Regression | `@regression` | Full module validation before release |
| Debug | `@debug` | Troubleshooting only — not for default CI |
| DB Validation | `@dbValidation` | Scenarios requiring database assertions |
| Module | `@uniteEnrollment` | Run Unite Enrollment module only (Mobile 1/2 use `@uniteMobile1`, `@uniteMobile2`) |
| All Mobile Microservices | `@mobileMicroservices` | Run full mobile microservices suite across modules |

**Tag composition example:** `@mobileMicroservices and @uniteEnrollment and @smoke`

---

## 10. Sample Commands

Examples for local and CI execution (exact module paths to be validated against framework POM during Phase 0):

```bash
mvn clean test -Dmodule=mobile-microservices -Dservice=unite-enrollment -Denv=qc4 -Dtags="@smoke"
```

```bash
mvn clean test -Dmodule=mobile-microservices -Dservice=unite-enrollment -Denv=stage1 -Dtags="@regression"
```

Additional examples (to be documented in runbook after validation):

```bash
# Enrollment smoke only
mvn clean test -Dmodule=mobile-microservices -Dservice=unite-enrollment -Denv=qc4 -Dtags="@mobileMicroservices and @uniteEnrollment and @smoke"

# Full mobile microservices regression (future — all modules)
mvn clean test -Dmodule=mobile-microservices -Denv=qc4 -Dtags="@mobileMicroservices and @regression"
```

---

## 11. Timeline Estimate

| Workstream | Estimated duration |
|------------|-------------------|
| Unite Enrollment discovery and skeleton | 1 week |
| Unite Enrollment vertical slice | 1 week |
| Unite Enrollment full migration and stabilization | 2–3 weeks |
| Pipeline and regression integration | 1 week |
| Mobile 1 migration | 2–4 weeks |
| Mobile 2 migration | 2–4 weeks |

### Summary

| Scope | Realistic estimate |
|-------|-------------------|
| **Unite Enrollment (pilot)** | **4–6 weeks** |
| **All three API modules** | **8–14 weeks** — depending on blockers, environment stability, test data issues, and Dev/Postman coordination |

*Timeline assumes dedicated QA capacity, timely Dev support for auth/config/Postman, and no major environment outages.*

---

## 12. Risks and Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Legacy tests depend on application classes | Migration blocked or brittle tests | Refactor to framework clients/actions; exclude scenarios that cannot decouple (document reason) |
| Environment configs are outdated | False failures; blocked execution | Partner with Dev; validate QC4/Stage via Postman first; align `jsonapi-lib` property patterns |
| Test data embedded in feature files | Slow migration; env-specific edits | Externalize to `test-data/` during vertical slice |
| SQL / database validation may fail | DB drift vs API expectations | Scope DB checks to test-created records; document setup/cleanup; use `@dbValidation` tag |
| APIs may have changed since tests were last run | Scenarios obsolete or failing | Discovery phase maps endpoints to current OpenAPI; update or exclude with approval |
| Pipeline permissions may be missing | CI integration delayed | Engage DevOps early; document secrets in pipeline vault only |
| Leadership may expect unrealistic AI-based timeline | Commitment pressure without proof | Phased delivery: skeleton → dummy smoke → vertical slice → full suite; report milestones not promises |

---

## 13. Deliverables

- [ ] Mobile microservices folder structure in API Automation Framework
- [ ] Unite Enrollment skeleton (packages, resources, Maven wiring)
- [ ] Dummy smoke test (compile + run proof)
- [ ] Legacy discovery report (Enrollment inventory)
- [ ] Scenario migration tracker (decisions: migrate / update / exclude)
- [ ] Vertical slice scenarios (3–5) passing on target environment
- [ ] Full Enrollment regression suite (with documented exclusions)
- [ ] Smoke and regression tags applied consistently
- [ ] Validated Maven execution commands (documented in runbook)
- [ ] Pipeline integration (QC4 smoke; Stage1 verification as policy allows)
- [ ] Runbook (local run, env switch, common failures, CI re-run)
- [ ] Repeatable migration pattern documented for Mobile 1 and Mobile 2

---

## 14. Final Target Outcome

The final achievement is a **centralized, maintainable, QA-owned Mobile Microservices API Automation regression suite** that:

- Lives in the **existing API Automation Framework** under `mobile-microservices/`
- Supports **Unite Enrollment**, **Unite Mobile 1**, and **Unite Mobile 2** as separate modules
- Runs **locally** (Maven + tags + environment) and through **CI/CD** (smoke on PR, regression on release path)
- Provides **leadership-visible progress** via trackers, phased milestones, and pipeline status
- Establishes a **repeatable migration pattern** so Mobile 1 and Mobile 2 follow Enrollment without reinventing structure

---

## 15. Leadership Summary

> **Executive summary (copy-ready for email or status update):**
>
> We are starting the Mobile Microservices API Automation migration by creating a separate **mobile-microservices** structure inside the existing API Automation Framework. **Unite Enrollment** will be used as the pilot module. The first milestone is to create the framework skeleton and validate one dummy smoke test. After that, we will analyze the existing Enrollment automation from the application repo, migrate **3–5 vertical slice scenarios**, stabilize them locally, and then expand into the full regression suite. Once Enrollment is stable, we will apply the same approach to **Mobile 1** and **Mobile 2**.

---

**Related documentation:** [Mobile Automation Program Hub](./README.md) | [Target Framework Architecture](./03-target-framework-architecture.md) | [Migration Strategy](./04-migration-strategy.md)

**Version:** 1.0 · **Review with:** Raju · **Next step:** Approve plan and authorize Phase 0 (Framework Skeleton) sprint work
