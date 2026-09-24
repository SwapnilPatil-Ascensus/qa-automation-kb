# V2 Regression Suite — Gap Analysis (Venkatesh Mallela)

**Source:** Email to Swapnil · **Sprint:** 26.15 · **Jira epic area:** QA-1943–QA-2010

---

## Summary

Daily regression **already covers** contrib (member + greenscreen), fees (529 + ABLE LA), uGift contrib, withdrawals, transfers, investments, G100 open account, balance overview, and much profile maintenance.

**It does NOT run:** reversal, plan transfer/rollover, share adjust/conversion, P&E on core NYD/NYA; no YTD bucket or CSR history-screen tests. Several profile/uGift/overview items need new scenarios or new `@dailyrun` rows in existing features.

---

## P0 — Add to daily regression (automation exists, not scheduled)

| Gap | What's missing | What to add |
|-----|----------------|-------------|
| **Reversal** | `Reversal.feature` exists; not in active regression XML | New tests in `stage1-csr-actions.xml` or `stage1-csr-reversal.xml`: `@regression` + `@dailyrun` on Direct (and Advisor if applicable). Start with 1–2 scenarios. |
| **Plan transfer / rollover** | Rollover In, Plan Transfer from Partner, 529/ABLE rollover — only `@functionalrun` | Add `@dailyrun` examples in `stage1-csr-actions.xml` (same pattern as Contribution Check/AIP/EBT). |
| **Inter-plan transfer** | `CsrInterPlanTransfer.feature` only in Archive | Restore one daily test (e.g. NYD) — confirm traunch still valid in Stage1. |
| **Share adjustment / Conversion** | Daily only on `stage1-laable` / empower / Archive | Add Direct and Advisor to `CSR_ShareAdjustment.feature` with `@dailyrun`. |
| **Principal update (P&E)** | `CSR_PandE.feature` not on main V2 daily | Add one "Update Principal and Earning" daily row for Direct (and NYA if allowed). |
| **Advisor fee** | `AdvisorFeeEntry.feature` not in csr-actions daily | If NYA needs advisor-specific fee UI, add Advisor daily row. |
| **Upromise contribution** | Only `@functionalrun` on greenscreen | If V2 menu requires Link with Upromise: one `@dailyrun` on NYD. |
| **Rollover from another 529** | CSR Rollover in G100 is `@functional` | One `@dailyrun` on Advisor if Stage1 data supports enrollment rollover path. |

---

## P1 — Partial coverage: extend regression

| Module | Today | Add for V2 CSR regression |
|--------|-------|---------------------------|
| stage1-acct-overview | CSR balance on NYD, NYA | Optional: ABLE (NYB) balance row |
| stage1-contributions | Contrib + AIP on NYD, NYA, NYB | Optional: ABLE contribution negatives |
| stage1-csr-acct-maintenance | Profile, docs, bank, beneficiary, delivery agent | Invalid contact (may move V3), authorized individual, bank negatives, trusted contact |
| stage1-csr-actions | Greenscreen contrib + fees on COD, NYD, NYA | Advisor greenscreen fees; optional ABLE contrib/fees |
| stage1-enrollments | G100 enrollment + prefill + member enrollment | Expand Advisor CSR enrollment if needed |
| stage1-transfers | Transfer to beneficiary on NYD, OHD, MID | Same flow on Advisor (and ABLE if supported) |
| stage1-ugift | CSR uGift on NYD, NYB | Optional: Advisor CSR uGift |

---

## P2 — Not in framework (build automation, then add to regression)

| Gap | Action |
|-----|--------|
| YTD bucket adjustment | New feature + step defs + Stage1 data → daily test |
| Financial history | New UI scenario: open screen, assert row/filter |
| Failed transactions | Same as financial history |
| Bank instruction history | Separate from BankInformation maintenance |
| Aggregation / OFAC history | New CSR screen test — or defer to compliance |
| CSR Information | New scenario if distinct screen |
| Change beneficiary's image | Implement commented step in SharedStepDefs |
| Tell a friend | New automation if still in CSR UI — else defer |

---

## Leadership decision needed

1. **Approve P0 wiring first** — low effort, high coverage gain (existing automation).  
2. **Do not retire failing tests** without migration verification (QA-1963).  
3. **Classify retain/migrate/replace/retire** per plan migration (QA-1962) before suite changes.  
4. **Capacity:** Venkatesh/Wence can execute P0 while main squad finishes MSC sign-off.

---

## Related Jira (Sprint 26.15)

- QA-1943 — Inventory bin regression and daily suites  
- QA-1944 — Freeze coverage for retiring legacy direct plans  
- QA-1945 — Extract CSR enrollment for V3 migration  
- QA-1946 — Add missing valid coverage to scheduled regression  
- QA-1961–1964 — Migration verification + classification + suite removal  
- QA-2008–2010 — Coverage design, documentation, suite membership  
