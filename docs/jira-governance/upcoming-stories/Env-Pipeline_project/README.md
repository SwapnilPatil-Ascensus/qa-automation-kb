# Env Pipeline / ENVP automation — upcoming Jira story drafts

**Epic (Jira):** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600)  
**Aha feature:** [ACS-5289 — Update Automation for ENVP (Automation)](https://acscensus.aha.io/features/ACS-5289)

**Purpose:** Copy-paste-ready **Story** and **Sub-task** drafts for Q work on Environment Pipeline test gates, starting with **Universal Enrollment (UE) Stage 1 integration** packaging and CI.

**Source material (repo):**

| Artifact | Path |
|----------|------|
| Links (Epic + Aha) | `docs/jira-governance/data/Env-Pipeline-Project/Important links.txt` |
| Proposed TestNG suite (UE Stage 1) | `docs/jira-governance/data/Env-Pipeline-Project/stage1-universal-enroll-integration.xml` |
| Meeting notes (scope, timing, grid) | `docs/jira-governance/data/Env-Pipeline-Project/Meeting minutes 04-01 @1.30PM.txt`, `Meeting minutes 04-09 @2PM.txt` |
| Aha/Jira narrative (ENVP automation criteria) | `docs/jira-governance/data/Env-Pipeline-Project/Jira Story QA-600 or Aha ticket - ACS-5289 details.docx` |

**Suggested labels (tune per board):**  
`automation` · `prime-v3` · `stage1` · `env-pipeline` · `universal-enrollment` · `ENVP` · `QA-Board-View`

**Execution-time note:** Leadership discussion referenced **3–5 minutes** for UI *smoke* in pipeline contexts; this quarter’s **UE integration** slice is explicitly targeted here at **≤10 minutes** wall clock (see UEPIPE-01). Reconcile both in QA/Tech lead alignment (UEPIPE-04).

---

## Stories in this folder

| File | Summary | Suggested points |
|------|---------|-----------------|
| [UEPIPE-01](UEPIPE-01-stage1-universal-enrollment-integration-suite.md) | **First priority:** Stage 1 UE integration suite — TestNG XML, Maven profile, **≤10 min**, CI wiring + baseline metrics | **8** |
| [UEPIPE-02](UEPIPE-02-harden-ue-foreign-phone-flaky-scenario.md) | Stabilize Foreign Phone UE scenario (`#firstName` timeout, retry/build semantics) | **5** |
| [UEPIPE-03](UEPIPE-03-retry-and-flake-policy-for-pipeline-ui.md) | Define flake vs regression handling when UI gates block deploy (process + tooling) | **3** |
| [UEPIPE-04](UEPIPE-04-ui-smoke-vs-integration-criteria-alignment.md) | QA + Tech lead: inclusion criteria, UI vs API, pass/fail, time budgets | **3** |
| [UEPIPE-05](UEPIPE-05-confluence-suite-taxonomy-mapping.md) | Confluence: map features ↔ API vs UI ↔ smoke / integration / nightly | **3** |
| [UEPIPE-06](UEPIPE-06-selenium-grid-load-and-parallelism.md) | Grid capacity, parallel thread-count vs duration, cost framing | **3** |
| [UEPIPE-07](UEPIPE-07-test-data-and-cleanup-spike.md) | Spike: data lifecycle / cleanup for pipeline UI tests | **5** |

**Version:** 1.0
