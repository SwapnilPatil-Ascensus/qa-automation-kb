# Executive Summary — Rajib / Henry Biweekly (Sep 25, 2026)

**Presenter:** Swapnil Patil · **Deck:** `deliverables/AM-Squad-Biweekly-Status-Rajib-Henry-Sep25-2026.pptx`  
**Sprint scope:** 26.15 + **26.16 (current, 9/16–9/29)**  
**Board:** [QA AMSQUAD](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515)

---

## 30-second opener

> **MSC API coding is 100% done.** M1, M2, Enrollment on main — Bruno collections merged. This sprint we finish **SharePoint KT, qTest, QC4 proof**. Only **Enrollment performance** remains after that. **Preeti:** M2 perf done, **M1 done by tomorrow**, Enrollment next; Jenkins jobs ready — need nightly schedule. **Venkatesh:** V2 enroll/login/reg almost done; **member cases migrating to V3** (Direct→universal). **He:** back on V3 IDP profile gaps. **Ask:** do you want **Dinesh** to package remaining universal APIs into **regression + integration + nightly** suites (**QA-892**)?

---

## Pulse

| Metric | Value |
|--------|-------|
| MSC coding | **100%** (MR !268 merged Sep 11) |
| Bruno migration | **Merged** (MR !271 Sep 21) |
| Stage1 / V2 / V3 health | **Recovered** after DB refresh |
| Perf | M2 done · M1 by Sep 26 · Enrollment remaining |
| Wrap-up target | **End Sprint 26.16** |

---

## Team by owner

| Owner | Focus | Status |
|-------|--------|--------|
| **Preeti** | MSC performance | M2 done; M1 done tomorrow; Enrollment next; Jenkins jobs ready (not nightly yet) |
| **Venkatesh** | V2 → V3 | Enroll/login/reg almost done; member IDP → V3; CSR daily wiring |
| **He** | V3 IDP profile | Back after illness; fixed profile issues; adding missing IDP profile cases |
| **Dinesh + Swapnil** | MSC wrap-up | Bruno done; SharePoint + qTest + QC4 by end of sprint |

---

## Leadership asks (need answers on call)

1. **QA-892:** Assign Dinesh to wire remaining universal APIs into master regression / integration / nightly?  
2. **Post-MSC queue:** Atlas (Oct) vs API suite packaging vs continue V2/V3 gaps?  
3. **Approve** retiring V2 member IDP for Direct plans now on universal (V3 source of truth)?  
4. **Approve** scheduling API/MSC perf Jenkins jobs for nightly?  
5. **Name** ACM / SharePoint sustaining owner for MSC handoff?

---

## If they ask “what’s left on MSC?”

| Done | This sprint | After wrap-up |
|------|-------------|---------------|
| Coding M1/M2/Enrollment | SharePoint, qTest, QC4 | Enrollment **performance** |
| Bruno collections | KT docs for QAs | Optional: **QA-892** suite packaging |
| MR !268 | | |

---

## References

- Board: https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515  
- [Previous biweekly Sep 11](../2026-09-11-rajib-henry-biweekly/README.md)  
- QA-892 suite packaging · QA-2084 SharePoint · QA-2101–2108 qTest · QA-2159–2163 M1 perf
