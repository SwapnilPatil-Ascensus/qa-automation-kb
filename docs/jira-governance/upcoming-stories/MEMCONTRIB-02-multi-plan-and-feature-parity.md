# MEMCONTRIB-02 — Member portal: multi-plan + AIP / recurring / negatives (CSR parity)

**Status:** Draft · **Suggested Story Points:** **8** · **Epic:** `QA-E-V3-TXN` (confirm)

**Labels:** `automation`, `prime-v3`, `contributions`, `member-portal`, `idp`, `stage1`, `QA-Board-View`, `Contrib`, `intake-upcoming`

**Depends on:** MEMCONTRIB-01 (foundation patterns merged).

**Mirrors CSR suite:** `docs/jira-governance/data/stage1-contributions.xml` — NYD, NYA, NYB, MID patterns; `AbleMemberSingleContribution.feature`; `AIPContribution.feature`; `AIPAddEditDeleteNonCustom.feature`; `AIPAddEditDelete.feature`; `MemberContributionNegative.feature`.

---

## Copy — Jira Summary

```
[V3][Contributions] Expand member-portal contributions — multi-plan, AIP, negatives
```

---

## Copy — Description

```markdown
## Context
CSR suite `stage1-contributions.xml` covers **multiple traunches** and **feature files**: direct/advisor/able single contribution, **AIP** single and **recurring** (add/edit/delete), and **negative** CSR scenarios. After MEMCONTRIB-01 proves **member portal** single contribution on **one** traunch, this story **scales** the same *member-login* approach to **additional plans** and **additional feature files**.

## User outcome
As **QA**, I want **member-portal** automation for **multiple traunches** and the **same contribution-related feature breadth** as CSR (where member UI exists), so **Stage 1** regression matches program risk.

## Scope — In
- **Multi-plan:** Add member-portal tests for traunches aligned with CSR suite priority, e.g. **nyd**, **nya**, **nyb**, **mid** (confirm with SME which support **member IDP** vs legacy).
- **Feature parity (member path),** each with member login only:
  - Single contribution extended Examples: *EBT (3 Funds)*, additional rows SME approves.
  - **AIP** one-time contribution (mirror `AIPContribution.feature` intent).
  - **AIP recurring** add/edit/delete (mirror `AIPAddEditDeleteNonCustom.feature` / `AIPAddEditDelete.feature` — split sub-tasks if large).
  - **Negatives** (mirror `MemberContributionNegative.feature` intent for member portal).
- Separate `@ablerun` tagging only if **ABLE** member portal scope is included for nyb.

## Scope — Out
- New pipeline job wiring (Story 03).  
- CSR suite changes (unless required for shared step defs).

## Dependencies
- MEMCONTRIB-01 **Done** (patterns + folder structure).  
- SME matrix: which **traunch + feature** combinations exist on **member** UI for Stage 1.

## Links
- CSR XML: `docs/jira-governance/data/stage1-contributions.xml`
```

---

## Copy — Acceptance Criteria

```markdown
h3. Multi-plan

* ( ) At least **3 traunches** run green for **member-portal single contribution** (e.g. nyd + nya + one non-IDP or advisor per SME matrix), **or** documented waiver in Story for plans without member UI.
* ( ) Each added traunch has **test data** + **credentials** documented in Story comment (secrets redacted in Jira; real values in secure store).

h3. Feature breadth

* ( ) **AIP** member-portal scenario(s) pass for **at least one** IDP and **one** non-IDP traunch *if both exist* in Stage 1 (align with CSR “IDP / Non-IDP” split in XML).
* ( ) **AIP recurring** add/edit/delete covered for **at least one** traunch per SME priority (remaining traunches as sub-tasks or follow-up).
* ( ) **Negative** member-portal contribution scenario(s) pass with **expected errors** and **no** partial commit per assertions.

h3. Quality

* ( ) No duplicate CSR tests removed; **member** tests are **additive**.
* ( ) Tags aligned: `@regression`, `@dailyrun` where nightly applies; `@ablerun` for ABLE-only if in scope.
* ( ) TestNG report linked in Story after full suite run on Stage 1.
```

---

## Copy — Definition of Done

```markdown
* SME matrix (plan × feature × member-available Y/N) attached or linked.
* All in-scope scenarios merged; CI green.
* Story 03 linked for pipeline inclusion.
```

---

## Suggested sub-tasks (Jira)

1. Multi-traunch single contribution (member)  
2. Member AIP one-time  
3. Member AIP recurring  
4. Member negatives  
5. ABLE tagging / nyb (if in scope)
