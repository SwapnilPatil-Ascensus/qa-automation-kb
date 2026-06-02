# May 2026 — V2 regression gap stories (Jira-ready pack)

**Folder:** `docs/jira-governance/upcoming-stories/MAY-2026-V2-Regression-Gaps/`  
**CSV import:** [MAY-2026-V2-regression-jira-import.csv](MAY-2026-V2-regression-jira-import.csv)  
**Evidence used**

| Source | Use |
|--------|-----|
| [MAY 2026 - QA Regression.pdf](../../data/MAY%202026%20-%20QA%20Regression.pdf) | Quarterly **Prod May 15, 2026** context; regression approach; embedded **GSSD Confluence** links (Prefill, Ugift529, UgiftAble, CSR Account Maintenance, CSR Contribution green screen, CSR Withdrawal, CSR Transfers, CSR Exchanges, CSR Ugift, CSR fee, etc.). |
| [Platform-support-jira-export.csv](../../data/Platform-support-jira-export.csv) | **Prefill:** `PrefillEnrollmentPositive.feature`, `frontoffice/csr/prefillenroll`, **QA-470** (Save and Send / plans WFD PAD VGI NUV). **PAG:** **QA-513** Universal Enrollment PAG sub-bene. **Flywire:** **QA-279–286** IND `INDMODDistribution.feature`, `@regression @dailyrun`, DB `type = Flywire`. **NYA/NYB/NYD** exchange/custom exchange plans lists. |
| User / Confluence | [Prefill Online Enrollment Test Cases](https://confluence.ascensus.com/display/GSSD/Prefill+Online+Enrollment+Test+Cases), [UgiftAble Test Cases](https://confluence.ascensus.com/display/GSSD/UgiftAble+Test+Cases), [CSR fee Test Cases](https://confluence.ascensus.com/display/GSSD/CSR+fee+Test+Cases). |
| Unite Regression Automation (screenshot) | **NVU** plan catalog **12** test names (error suite + positive AIP/ROLLOVER/UGMA/EBT/PAYROLL) — table in **Story 2** below. |

**Reporter:** Swapnil Patil (adjust in Jira). **Project:** QA — QA Automation. **Epic:** Map to your May 2026 / Platform regression epic (**Needs Validation**).

---

## Story 1 — `[V2][Enrollment][PAG] GSP enrollment scenarios missing from regression`

**Intent:** Partner **GSP** enrollment paths for **PAG** are absent from the V2 regression footprint; add them so the May quarterly regression matches program expectations.

**Description (paste)**

```text
h2. Problem
GSP (partner) enrollment scenarios for plan traunch *PAG* are not represented in the current V2 regression suite, creating release risk for the May 2026 quarterly cycle.

h2. Scope
* Inventory *prime-test-automation* (or owning repo) for existing PAG enrollment and GSP/partner load patterns (export mentions GSP/Partner load tests in broader narratives).
* Add TestNG scenarios + suite XML entries for agreed GSP enrollment flows for *PAG*; document data prerequisites.

h2. Evidence / refs
* KB: docs/jira-governance/data/MAY 2026 - QA Regression.pdf (May 15 2026 prod context).
* Platform-support-jira-export.csv: PAG-related work (e.g. Universal Enrollment PAG sub beneficiary QA-513) — align naming with subordinate tasks.

h2. Acceptance criteria
* [ ] SME-signed list of GSP+PAG flows to automate (or explicitly deferred with reason).
* [ ] Merged automation + suite XML; at least one green Stage 1 run linked in comment.
* [ ] qTest / cycle mapping if required by program.
```

---

## Story 2 — `[V2][CSR][Prefill] Prefill Online Enrollment regression expand beyond NVU baseline`

**Intent:** Align automation with **GSSD** [Prefill Online Enrollment Test Cases](https://confluence.ascensus.com/display/GSSD/Prefill+Online+Enrollment+Test+Cases) and the **NVU** catalog from Unite Regression Automation (12 cases).

**NVU test names (from Confluence / Unite Regression Automation)**

| # | Test name |
|---|-----------|
| 1 | Validate CSR Pre-fill Enrollment Error Messages for Pre-fill Enrollment Participant Info Individual |
| 2 | Validate CSR Pre-fill Enrollment Error Messages for Pre-fill Enrollment Address Info |
| 3 | Validate CSR Pre-fill Enrollment Error Messages for Pre-fill Enrollment Successor Info |
| 4 | Validate CSR Pre-fill Enrollment Error Messages for Pre-fill Enrollment Beneficiary Info |
| 5 | CSR Pre-fill Enrollment with Pre-fill Enrollment UGMA/UTMA CHECK |
| 6 | CSR Pre-fill Enrollment with Pre-fill Enrollment Individual ROLLOVER |
| 7 | CSR Pre-fill Enrollment with Pre-fill Enrollment Individual AIP Monthly |
| 8 | CSR Pre-fill Enrollment with Pre-fill Enrollment UGMA/UTMA ROLLOVER |
| 9 | CSR Pre-fill Enrollment with Pre-fill Enrollment Individual AIP No Annual Increase |
| 10 | CSR Pre-fill Enrollment with Pre-fill Enrollment Individual EBT |
| 11 | CSR Pre-fill Enrollment with Pre-fill Enrollment Individual PAYROLL |
| 12 | CSR Pre-fill Enrollment with Pre-fill Enrollment Individual AIP Quarterly |

**Description (paste)**

```text
h2. Context
* Confluence: https://confluence.ascensus.com/display/GSSD/Prefill+Online+Enrollment+Test+Cases
* Existing automation baseline: PrefillEnrollmentPositive.feature under frontoffice/csr/prefillenroll (see QA-470 / Platform-support-jira-export.csv for path and Stage 1 defect narrative).

h2. Scope
* Map each Confluence row (NVU minimum; expand plans per MAY regression matrix) to automated or explicitly manual-only with sign-off.
* Cover error-message suite (Participant, Address, Successor, Beneficiary) and positive paths (UGMA/UTMA CHECK/ROLLOVER, Individual ROLLOVER, AIP variants, EBT, PAYROLL).

h2. Acceptance criteria
* [ ] Traceability matrix: Confluence case ID or name → feature method → @tags.
* [ ] Stage 1 green run for in-scope rows; attach report link.
* [ ] Regression suite includes prefill package without breaking unrelated CSR modules.
```

---

## Story 3 — `[V2][CSR][UgiftAble] UgiftAble automation coverage per GSSD test cases`

**Description (paste)**

```text
h2. Reference
https://confluence.ascensus.com/display/GSSD/UgiftAble+Test+Cases

h2. Scope
Automate (or stub + manual bridge where not automatable) UgiftAble CSR flows per Confluence; align with MAY 2026 regression PDF GSSD link family.

h2. Acceptance criteria
* [ ] Confluence rows mapped to tests or N/A.
* [ ] Data matrix for Able-specific accounts documented.
* [ ] Evidence: job URL + pass rate for first regression inclusion.
```

---

## Story 4 — `[V2][CSR][Management] Account search quick search and tracking cookie automation`

**Description (paste)**

```text
h2. Gaps
* CSR Account Search / Quick Search — not in regression.
* Tracking Cookie — not in regression.

h2. Scope
SME demo → locator strategy → scenarios for search result accuracy and cookie consent / persistence per app rules.

h2. Dependencies
CSR session baseline; test accounts with searchable attributes.

h2. Acceptance criteria
* [ ] At least one happy path + one negative per gap area (or documented SME waiver).
* [ ] Merged to regression suite with tags documented in Story comment.
```

---

## Story 5 — `[V2][CSR][Management] Advisor employer authorized individual automation`

**Description (paste)**

```text
h2. Gaps
* CSR Advisor Management
* CSR Employer Management
* Additional Authorized Individual
* Authorized Individual

h2. Scope
Matrix-driven automation; split Sub-tasks if >5 SP combined. Coordinate *P&E* traunch data for NYA/NYB/NYD with Story 10 as needed.

h2. Acceptance criteria
* [ ] Coverage matrix attached; each gap row Closed or linked follow-up.
* [ ] Stage 1 evidence for primary traunch per SME.
```

---

## Story 6 — `[V2][CSR][Management] Withdrawal aggregation case ops restriction freeze holding exception`

**Description (paste)**

```text
h2. Gaps
* CSR Withdrawal Management
* CSR Aggregation Management (CSR - Aggregation / OFAC history)
* CSR Case Administration
* CSR Case Management
* CSR Restriction / Freeze
* Withdrawal Holding
* Exception Check

h2. Related Confluence (MAY PDF link family)
CSR Withdrawal, Transfers, Exchanges GSSD pages — use for testcase IDs.

h2. Acceptance criteria
* [ ] OFAC / aggregation history navigation automated or manual script with evidence.
* [ ] Restriction/freeze and withdrawal holding: at least one scenario each proving UI + DB or UI-only per framework capability.
* [ ] Exception check path documented with defect escape if product blocker.
```

---

## Story 7 — `[V2][CSR][Management] Email username password security Q and A automation`

**Description (paste)**

```text
h2. Gap
CSR Email / Username / Password / Security Q&A — missing from regression.

h2. Security
Use vault-managed credentials only; rotate test passwords after recording; no credentials in Git or Jira body.

h2. Acceptance criteria
* [ ] Positive change + negative validation (wrong SQA, weak password) per SME.
* [ ] Audit log or post-condition check where available.
```

---

## Story 8 — `[V2][CSR][Fees] CSR fee transactions per GSSD test cases`

**Description (paste)**

```text
h2. Reference
https://confluence.ascensus.com/display/GSSD/CSR+fee+Test+Cases

h2. Scope
Fee assessment, waiver, reversal, inquiry — per Confluence matrix; DB assertion pattern aligned to existing CSR financial tests.

h2. Acceptance criteria
* [ ] Row-level mapping Confluence → automation.
* [ ] Stage 1 green subset linked.
```

---

## Story 9 — `[V2][Member][Flywire] CSR Flywire parity — member-only path`

**Description (paste)**

```text
h2. Context
Prior work automated Flywire for IND member distributions (QA-279–286 family): INDMODDistribution.feature, validate Flywire txn, DB type Flywire, currency summary, @regression @dailyrun (Platform-support-jira-export.csv).

h2. Ask
Implement *member-only* CSR-context Flywire scenarios (exact feature names Needs Validation) reusing assertion patterns from IND where possible.

h2. Acceptance criteria
* [ ] At least one end-to-end Flywire CSR-member scenario green on Stage 1.
* [ ] DB or API check documented for Flywire type / currency summary.
```

---

## Story 10 — `[V2][P and E][NYA NYB NYD] Pricing and expense update regression automation refresh`

**Description (paste)**

```text
h2. Context
May 2026 quarterly regression (see MAY 2026 - QA Regression.pdf): P&E (Pricing and Expense) updates affecting NYA, NYB, NYD traunches.

h2. Scope
* Refresh assertions or add scenarios for allocation / exchange / display rules impacted by P&E release.
* Align with existing exchange regression narratives (NYD, NYB, NYA, COD) in Platform-support-jira-export.csv where overlapping.

h2. Acceptance criteria
* [ ] SME change list attached (from product release notes or AHA).
* [ ] NYA, NYB, NYD each have at least one updated scenario passing on Stage 1.
* [ ] Linked defects for product gaps; automation Issues for test debt.
```

---

## Labels (all stories)

Suggested: `automation`, `v2`, `regression`, `qa-board-view`, `may-2026` plus story-specific labels from CSV.

---

## Changelog

| Date | Note |
|------|------|
| 2026-05-12 | Initial pack from MAY PDF URIs, Platform CSV, user Confluence links, NVU Prefill screenshot catalog. |
