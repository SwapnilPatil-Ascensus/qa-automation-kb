# UEPIPE-01 — Stage 1 Universal Enrollment integration suite (pipeline-ready, ≤10 min)

**Status:** Draft · **Suggested Story Points:** **8** · **Epic:** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600) · **Aha:** [ACS-5289](https://acscensus.aha.io/features/ACS-5289)

**Labels:** `automation`, `prime-v3`, `stage1`, `env-pipeline`, `universal-enrollment`, `ENVP`, `QA-Board-View`, `intake-upcoming`

**Parent links:** KB suite draft `docs/jira-governance/data/Env-Pipeline-Project/stage1-universal-enroll-integration.xml` · Repo module `unite/unite-universal-enrollment` (Prime Test Automation).

---

## Copy — Jira Summary

```
[ENVP][UE] Stage 1 Universal Enrollment integration suite — package for pipeline (≤10 min)
```

---

## Copy — Description

```markdown
## Context
Per *Update Automation for ENVP* ([ACS-5289](https://acscensus.aha.io/features/ACS-5289)) and Epic **QA-600**, we need **clearly scoped, runnable** automation that supports **environment pipeline** confidence. Universal Enrollment (UE) is the **first vertical** to package as a **Stage 1 integration** suite (UI-level integration using real Stage 1 traunches), distinct from pure API/unit gates described in Aha.

**Dong / team request (KB):** Integration suite for UE that can run within **10 minutes** in pipeline context.

**Baseline (reference run — `mvn test -P stage1-ue-integration-test` in `unite/unite-universal-enrollment`):**
- Maven total time ~**9 min 28 s**; Cucumber/suite elapsed ~**554 s** (~9.2 min).
- **30** scenarios executed; **29 passed, 1 failed** (build failure).
- Failure: *Single Universal Enrollment with Enrollment of Individual Account with Foreign Phone* (`UniversalEnrollmentPositive.feature` ~line 41) — `WebDriverWait` **30 s** timeout on `#firstName` in `completeUniAccountOwnerInformation` / `completeNextGenAccountOwnerInformation`. Retries: Run 1 pass, Run 2 fail, Run 3 pass — build still failed.

## User outcome
As **QA automation**, I want a **named Stage 1 UE integration suite** (TestNG + Maven profile + CI) that completes within **≤10 minutes** under agreed grid/parallelism, with **reporting artifacts** and a **documented scenario list** (`@integration` + `@intrun`), so **ENVP / Stage 1 gates** can consume a stable, intentional UE package.

## Scope — In
- Commit **suite definition** aligned with KB draft: `stage1-universal-enroll-integration.xml` (parallel tests, `thread-count` as agreed — draft uses **4**).
- Wire **Maven** profile (e.g. `stage1-ue-integration-test`) to run this suite in `unite-universal-enrollment`.
- **Time budget:** meet **≤10 min** wall clock (or document variance + follow-up if grid differs); capture **before/after** timings in Story comment.
- **CI:** GitLab job (MR and/or scheduled) publishing Surefire/HTML under `target/surefire-reports/` (same pattern as existing UE jobs).
- **Documentation:** short README or wiki section listing traunches, feature files, tags, and “UI integration” intent (supports Aha *clarity of test intent*).

## Scope — Out
- Fixing the Foreign Phone flake (**separate Story UEPIPE-02** — may block “green” gate).
- Full ENVP taxonomy / Confluence matrix (**UEPIPE-05**).
- Org-wide smoke policy (**UEPIPE-04**).

## Dependencies
- Selenium Grid availability and **parallel** capacity (see UEPIPE-06).
- Stable Stage 1 URLs per traunch (MDD, ILD, OHD, IDD, MOD, NMD, NJD, NYD).

## Links
- Aha: https://acscensus.aha.io/features/ACS-5289  
- Epic: https://ascensuscollegesavings.atlassian.net/browse/QA-600  
- KB suite XML: `docs/jira-governance/data/Env-Pipeline-Project/stage1-universal-enroll-integration.xml`
```

---

## Copy — Acceptance Criteria

```markdown
h3. Must pass

* ( ) TestNG suite file for **Stage 1 UE integration** lives in **prime-test-automation** under agreed path (mirror or replace KB draft `stage1-universal-enroll-integration.xml`).
* ( ) `mvn test -P stage1-ue-integration-test` (or agreed profile name) runs the suite against **Stage 1** without manual steps.
* ( ) **Wall-clock duration ≤ 10 minutes** on reference executor (document host/CI runner + grid used); if exceeded, Story documents bottleneck and links follow-up.
* ( ) Surefire reports / Cucumber HTML published as CI artifacts (path documented in Story comment).
* ( ) Suite runs only scenarios tagged **`@integration` and `@intrun`** per test definition parameters (matches KB XML intent).
* ( ) Story comment: scenario **count**, traunch list, and **timing table** (at least 3 runs).
* ( ) Linked child work: **UEPIPE-02** for Foreign Phone stability if suite still red.
```

---

## Copy — Sub-tasks (create under this Story)

Use one Sub-task per row; paste **Summary** + **Description** into Jira.

### Sub-task 1 — Suite file + TestNG wiring

**Summary:** `[UE][Sub] Add Stage 1 UE integration TestNG suite XML in unite-universal-enrollment`

**Description:**
```markdown
Add or align `stage1-universal-enroll-integration.xml` (from KB draft) in repo. Confirm `ParallelFeatureRunner` parameters: `features`, `traunch`, `tags` = `@integration and @intrun`. Validate listener `core.listener.PrimeResourceManager`. Document any deviation from KB draft.
```

---

### Sub-task 2 — Maven profile

**Summary:** `[UE][Sub] Maven profile stage1-ue-integration-test for UE integration suite`

**Description:**
```markdown
Add/verify Maven profile `stage1-ue-integration-test` pointing Surefire at the Stage 1 UE integration suite. Confirm local + CI command: `mvn test -P stage1-ue-integration-test` from `unite/universal-enrollment`. Document JVM/browser properties if required.
```

---

### Sub-task 3 — Timing baseline & budget

**Summary:** `[UE][Sub] Baseline timing — ≤10 min wall clock; document runs`

**Description:**
```markdown
Run suite minimum **3 times** on target CI (or equivalent grid). Record: Maven total time, Surefire elapsed, scenario count, parallel `thread-count`. Compare to **≤10 min** goal; if over, list bottleneck (grid wait, slow traunch, scenario count) and link tuning follow-up or UEPIPE-06.
```

---

### Sub-task 4 — GitLab CI job + artifacts

**Summary:** `[UE][Sub] GitLab CI — UE Stage 1 integration job + surefire artifacts`

**Description:**
```markdown
Add or update `.gitlab-ci.yml` (or included template) so UE integration suite runs on agreed trigger (MR pipeline stage and/or nightly). Publish `unite/universal-enrollment/target/surefire-reports/**` as artifacts. Link sample job in Story comment.
```

---

### Sub-task 5 — Intent / scope doc

**Summary:** `[UE][Sub] Document UE integration suite scope (UI vs API, tags, traunches)`

**Description:**
```markdown
Short doc (README section, Confluence stub, or module doc): list traunches, feature files, tags, and statement that suite is **UI integration** for ENVP Stage 1 — not a substitute for unit/API gates per ACS-5289. Cross-link Epic QA-600.
```

---

## Notes for implementers

- KB XML references `UniversalEnrollmentPositive.feature`, `UniversalEnrollmentPositiveOhio.feature`, `UniversalEnrollmentMultipleBeneficiaries.feature` — confirm paths match repo layout.
- Parallelism **4** × **9** `<test>` blocks affects grid load; reducing threads may improve stability but can break the **10 min** budget — tradeoff belongs in UEPIPE-06 + Story comment.
