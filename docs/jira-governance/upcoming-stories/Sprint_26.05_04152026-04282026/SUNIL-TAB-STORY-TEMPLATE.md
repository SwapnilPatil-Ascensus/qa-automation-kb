# Template — V2 CSR: CSR Maintenance tab regression (one tab)

**Use after:** Spike **S2605-06** produces the gap matrix.  
**Clone:** One Jira Story per row in the “missing tabs” list.

---

**Summary:** `[V2][CSR][Maint] <TAB_NAME> — regression automation`

**Issue type:** Story  
**Assignee:** Sunil Godiyal  
**Reporter:** Swapnil Patil  
**Component/Area:** `v2`, `csr`, `jenkins` (or `pipeline` if run from GitLab per program standard)

**Labels (example):** `automation`, `regression`, `csr`, `v2`, `maintenance`, `qa-board-view`

---

**Description**

- **As a** QA engineer  
- **I want** automated regression coverage for the CSR **Account / Profile Maintenance** tab **`<TAB_NAME>`** on Stage 1 (V2 / legacy stack)  
- **So that** nightly regression detects regressions in that tab before production

**Scope**

- **Portal:** CSR only (not member).  
- **Stack:** V2 legacy (Ant/Jenkins execution model per program standard — **Needs Validation** for exact job name).  
- **In:** Scenarios and assertions agreed with SME for this tab; tags for smoke/regression per team standard (KB references `@regression`, `@dailyrun` on maintenance work in `jira-export.csv` for **QA-429** / Profile Maintenance).  
- **Out:** Other maintenance tabs (separate Story per tab).

**Evidence / references (KB)**

- Backlog story shape: `docs/jira-governance/backlog/stories.md` — **QA-S-V2-011** CSR Maintenance tabs.  
- Historical maintenance features: `jira-export.csv` — **PersonalInformation.feature**, **Profile Maintenance**, reports under `stage1-csr-acct-maintenance` (internal report URLs in export — use current report root for your env).

---

**Acceptance Criteria (GWT)**

```gherkin
Feature: CSR Maintenance <TAB_NAME>

  Scenario: Happy path coverage for tab
    Given a CSR session on Stage 1 with test data for <TAB_NAME>
    When the automation exercises the agreed happy path for <TAB_NAME>
    Then the UI reaches the expected completion state and assertions pass per SME checklist

  Scenario: Tagged for regression
    Given merged automation for <TAB_NAME>
    When the nightly CSR maintenance regression job runs
    Then scenarios for <TAB_NAME> execute with agreed tags (e.g. @regression / @dailyrun per program)
```

---

**Definition of Done**

- [ ] MR merged; tests stable on target Stage (evidence: report link or job URL).  
- [ ] Tags applied per program convention.  
- [ ] Included in **nightly regression** suite XML / job that already covers csr-acct-maintenance (or new suite entry documented).  
- [ ] No open Sev1/Sev2 on scope.

**Dependencies / Risks**

- Depends on spike **S2605-06** row for this tab marked “gap.”  
- Risk: shared test data collisions — document isolation approach in Story comment.
