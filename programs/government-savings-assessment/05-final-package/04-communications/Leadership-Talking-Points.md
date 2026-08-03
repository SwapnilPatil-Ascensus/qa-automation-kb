# Government Savings — Business Coverage Summary

**As of:** 2026-07-21  
**Audience:** Government Savings leadership  
**Registers:** `government-savings-business-coverage-register.csv`, `verified-metrics-register.csv`

---

## 1. Executive position

Government Savings has **meaningful automation across every major business platform**, but maturity varies by **operational activation** — what is implemented in code, what runs on a recurring schedule, and what meets the full Definition of Done.

**There is no single Government Savings-wide coverage percentage.** Leadership should use **business platform narratives** supported by verified numerators, explicit denominators, and status labels.

**Headline truths today:**

| Platform | Position |
|----------|----------|
| **Unite MSC / Mobile Microservices** | Mobile 2 API automation **complete for automatable business scope**; recurring GitLab execution and refreshed sign-off are follow-up items |
| **Universal Platform / Modern Unite (V3)** | Core enrollment, IDP, and withdrawal journeys run in **active GitLab nightly regression** |
| **Legacy Unite (V2)** | **Majority of high-priority member portal journeys** have automation and referenced Jenkins nightly modules; extensive additional assets await reactivation |
| **Back-office / Batch** | Substantial automation implemented; weekly execution referenced — revalidation needed |
| **ASTRO / SFRP** | Substantial asset base; **inactive recurring execution** |
| **COPACS** | No validated automation identified — discovery required |

---

## 2. Coverage by Government Savings platform

### Unite MSC / Mobile Microservices

**Mobile 2 API** — Automation is **complete for the currently defined automatable business scope** (24/24 endpoints). Destructive operations (bank PUT/DELETE, contribution DELETE) are **implemented** and intentionally placed in smoke/module suites, not master regression. Latest documented master execution is **stale (22/25, 2026-07-14)**. **GitLab nightly not scheduled** (QA-1405). **GitHub Actions** validates Dashboard deployment slice — not full API regression.

**Mobile 1 API** — **Partial coverage with expansion in progress**: 6 of 27 documented endpoints implemented; 1 execution-verified (session). No CI schedule.

**Mobile Enrollment API** — Bootstrap/pilot framework only; endpoint inventory **not enumerated**.

**UniteMSC microservices** — Service-level BDD and JaCoCo in CI; application source-code coverage is **separate** from BFF API business automation.

**Do not publish a combined "Unite MSC ~70%" figure** — enrollment denominator unavailable.

### Universal Platform / Modern Unite (V3)

**Active nightly regression** covers Universal Enrollment (303 TestNG methods), IDP (56), and Withdrawals (20) in the approved nightly inventory. **Entity Platform** has 6 implemented scenarios — primary expansion area. **Universal metadata API** on GitLab schedule. Broader universal API modules (account, auth, financial) exist but are **not all scheduled**.

Conversational claims of "95%+ for UE/IDP" are **program estimates** — supported by near-complete regression scope, not verified business denominators.

### Legacy Unite (V2) — Member and CSR

**High-priority member portal:** Ten daily Jenkins modules (per platform documentation) cover enrollment, login/registration, balance, contributions, withdrawals, investment options, Sardine, and Empower plan flows. **Automation assets exist and recurring regression is referenced** — live Jenkins health not re-verified this pass.

**Lower-priority / deferred:** CSR Actions, greenscreens, management screens, and specialty plan flows — **automation assets exist but require revalidation, synchronization, and inclusion in the governed nightly suite**.

Historical "~80%+" or "~95% core flows" claims are **historical documentation estimates**, not verified denominators.

### Back-office / Batch

1,062 backoffice feature files implemented. Weekly backoffice regression **referenced** (Tue/Wed). Not on Modern Unite GitLab nightly. **Revalidation and schedule confirmation required.**

### ASTRO / SFRP

391 feature files; substantial ORS/employer/employee/CSR coverage in code. **No verified recurring execution.** Reactivation assessment required before representing as active coverage.

### COPACS

No automation repository identified. **Scope and ownership discovery** required.

### API automation outside Mobile

| Module | Pipeline status |
|--------|-----------------|
| Metadata | **Scheduled** GitLab Stage 1 |
| Enrollment, account, auth, financial, validation | Implemented — **manual / not scheduled** |
| ASTRO API | 5 classes — small footprint |

### Performance

IDP performance suite **scheduled weekdays** (Jenkins). Universal Enrollment and Entity journeys have assets — **not all scheduled**. MSC mobile perf scripts exist — **manual trigger only**.

### Reporting, qTest, and governance

qTest export **stale (2026-06-29)**. No harmonized live register yet. Python utilities can extend to read-only reconciliation once APIs are provisioned.

---

## 3. What is active in recurring regression

| Platform | Active recurring execution | Channel |
|----------|---------------------------|---------|
| Universal Enrollment + IDP + Withdrawals + Unite core UI | Yes | GitLab `scheduled_regression_job` |
| Universal metadata API | Yes | GitLab `scheduled_metadataweb_stage1` |
| Legacy Unite high-priority daily modules | Referenced | Jenkins `STAGE1-Daily-Unite-Prime-Regression` (docs) |
| IDP performance | Referenced | Jenkins `AGSUP_IDP_REGRESSION_SUITE` |
| Mobile 2 API master regression | **No** | QA-1405 pending |
| Mobile 1 API | **No** | — |
| ASTRO UI | **No verified** | — |
| Backoffice weekly | Referenced | Jenkins weekly (docs) |

---

## 4. Existing automation awaiting reactivation or pipeline inclusion

- Mobile 2 API master suite → GitLab nightly (QA-1405)  
- Mobile 1 API → CI schedule after execution evidence  
- Universal API modules beyond metadata → GitLab candidates  
- Entity Platform scenarios → confirm nightly inclusion  
- Legacy CSR / greenscreen / management → revalidation + suite governance  
- ASTRO full regression → scope decision + schedule  
- Backoffice weekly → confirm Jenkins health  
- Adjacent V3 inventory (contributions, CSR maintenance, web registration) → confirm nightly scope

---

## 5. API and performance coverage

**API:** Strongest operational integration is **metadataweb** (scheduled). Mobile 2 is **implementation-complete** for automatable scope but **not scheduled**. Universal scoped operations (11) mapped; full service catalog not reconciled.

**Performance:** IDP on schedule; UE/Entity/MSC uneven. Definition of Done expects performance coverage where applicable — program moving incrementally.

---

## 6. Current merge and CI controls

GitLab protected-branch controls are substantive: protected `main`, MR pipeline success, Snyk, dual approval including senior Code Review, discussion/change-request blocks, merge dependencies, draft/rebase rules, conditional auto-merge.

These are **merge hygiene and security gates** — not business regression or code-coverage-delta gates.

---

## 7. Missing code-coverage-delta control

No verified repository compares branch JaCoCo coverage to `main`, publishes a required MR check, blocks merge on regression, and records auditable coverage exceptions. JaCoCo exists on UniteMSC services; Sonar disabled.

---

## 8. Automated reporting / tooling position

Partial today: Python scanners, verified metrics register, business coverage register (this rebuild). Blocked: live Jira, qTest, GitLab API (expired token). **Feasible** to extend existing utilities — no large new application required.

---

## 9. Recommended actions

| Priority | Action |
|----------|--------|
| P0 | Schedule Mobile 2 API GitLab nightly (QA-1405) |
| P0 | Refresh Mobile 2 execution sign-off |
| P1 | Provision read-only qTest/Jira/GitLab APIs |
| P1 | Publish weekly business coverage register |
| P1 | JaCoCo coverage-delta pilot on `unite-mobile2` |
| P2 | ASTRO scope + reactivation plan |
| P2 | Backoffice weekly schedule confirmation |
| P2 | COPACS discovery |
| P2 | Legacy CSR/greenscreen revalidation sprint |

---

## 10. Leadership decisions / support required

1. Approve **business-platform denominators** — reject single GS-wide %  
2. Sponsor **QA-1405** and Mobile 2 execution refresh  
3. Approve **ASTRO in/out** of active GS regression  
4. Assign **COPACS** ownership for scope discovery  
5. Provision **read-only ALM/CI credentials**  
6. Approve **Definition of Done** model for "fully automated" capabilities

---

## Definition of Done (target quality model)

A capability is **not fully automated** merely because functional code exists. Target state includes:

- Manual test coverage  
- Functional automation  
- API automation where applicable  
- Performance coverage where applicable  
- Suite/profile integration  
- Environment execution evidence  
- CI/CD integration  
- Documentation  
- Traceability  
- Support ownership  

The program is advancing toward this model **incrementally**.

---

## Platform summary table

| Platform | Current automation position | Active regression / CI | Existing assets not currently active | Next action | Confidence |
|----------|----------------------------|------------------------|--------------------------------------|-------------|------------|
| Unite MSC — Mobile 2 API | Complete for automatable business scope | GHA deployment validation only; no GitLab nightly | Master suite not on schedule | QA-1405 + execution refresh | High |
| Unite MSC — Mobile 1 API | Partial (6/27 endpoints) | None | 21 endpoints + execution evidence | Sprint expansion + CI | High |
| Unite MSC — Enrollment API | Bootstrap pilot | None | Full endpoint program | Define scope + inventory | Medium |
| Unite MSC — Microservices | Service BDD + JaCoCo | Service CI build/test | BFF regression separate | Coverage-delta pilot | High |
| Universal Platform (Modern Unite) | Near-complete for core nightly scope (UE/IDP/Withdrawal) | GitLab nightly + metadata API | Entity, adjacent modules, unscheduled APIs | Entity nightly inclusion + API scheduling | High |
| Legacy Unite — member portal | Majority of high-priority journeys automated | Jenkins daily referenced | UGift/transfers suite placement | Confirm Jenkins health | Medium |
| Legacy Unite — CSR / greenscreen | Assets exist | Not in daily nightly | Management/case screens | Revalidation sprint | Medium |
| Back-office / Batch | Substantial implementation | Weekly referenced | Not on V3 GitLab | Confirm weekly jobs | Medium |
| ASTRO / SFRP | Substantial asset base | None verified | Full UI + API suites | Scope decision + reactivation | High |
| COPACS | Unknown | None | N/A | Business discovery | Low |
| Performance | IDP scheduled; others partial | Jenkins IDP weekdays | UE/Entity/MSC periodic | Expand scheduled journeys | Medium |
| Reporting / Governance | Registers maintained | Partial automation | Live ALM/CI collectors | API credentials | High |

---

*Technical appendix: endpoint matrices, qTest populations, inventory-share percentages, repository paths — see `03-analysis/` supporting CSVs.*
