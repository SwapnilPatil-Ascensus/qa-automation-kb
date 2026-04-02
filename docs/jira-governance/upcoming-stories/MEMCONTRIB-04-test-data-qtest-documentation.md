# MEMCONTRIB-04 — Test data, qTest mapping, and documentation for member contributions

**Status:** Draft · **Suggested Story Points:** **3** · **Epic:** `QA-E-V3-TXN` (confirm)

**Labels:** `automation`, `prime-v3`, `contributions`, `member-portal`, `qtest`, `documentation`, `stage1`, `QA-Board-View`, `Contrib`, `intake-upcoming`

**Runs parallel or after:** MEMCONTRIB-01; complete before **release sign-off** of MEMCONTRIB-02/03.

---

## Copy — Jira Summary

```
[V3][Contributions] Member portal contrib — test data, qTest, Confluence/docs
```

---

## Copy — Description

```markdown
## Context
CSR contribution automation relies on **shared test data**, **qTest** traceability, and **Confluence** coverage docs. **Member-portal** flows need the same **operational hygiene** so offshore, leads, and audits can trace **method → requirement** and refresh **accounts** safely.

## User outcome
As **QA chapter**, I want **documented data ownership**, **qTest** links, and **updated regression docs**, so **member** contribution scope is **auditable** like CSR.

## Scope — In
- **Test data sheet** (or DB seed doc): member usernames per traunch, account ids, bank profiles, **rotation** / **collision** rules; PII redacted in Jira.
- **qTest:** create or map test cases for new automation methods; link in Story or export snippet.
- **Docs:** update AM Regression / Confluence module for **Contributions** — add **Member portal (IDP)** subsection mirroring CSR table (paths to feature files, suite XML, traunch list).
- **Flaky baseline:** first 3 nightly runs — capture pass rate; open bugs for app vs test with labels.

## Scope — Out
- Implementing automation (Stories 01–02).  
- Pipeline YAML (Story 03) except **documentation** of job link in Confluence.

## Links
- CSR reference: `docs/jira-governance/data/MemberSingleContribution.feature`, `stage1-contributions.xml`
```

---

## Copy — Acceptance Criteria

```markdown
* ( ) **Data inventory** comment or attachment: traunch → member user strategy → bank/contribution prerequisites (no passwords in Jira).
* ( ) **qTest** project updated: new scenarios linked **or** waiver comment from PO if qTest not required for this slice.
* ( ) **Confluence** (or `AM_Regression_Reports/docs/...`) updated with **Member portal contributions** row: feature paths, suite name, Stage 1, tags.
* ( ) **Ownership**: named contact for **data refresh** when passwords expire or accounts lock.
* ( ) **Three** nightly or scheduled runs after pipeline merge: outcomes summarized in Story comment (pass %, linked defects).
```

---

## Copy — Definition of Done

```markdown
* PO/SM accepts doc + qTest state.
* Links from Story to Confluence page and qTest folder (if any).
```
