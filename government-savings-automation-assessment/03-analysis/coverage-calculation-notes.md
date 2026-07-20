# Coverage Calculation Notes

**Assessment date:** 2026-07-20  
**Rebuild validated:** 2026-07-21  
**Single source of truth:** `verified-metrics-register.csv`

---

## 1. Metric separation (non-negotiable)

| # | Metric | Code | Measured in this assessment? |
|---|--------|------|------------------------------|
| 1 | Business automation coverage | B | Yes — domain-specific |
| 2 | API endpoint coverage | B-api | Yes — MSC + UP subsets |
| 3 | Execution coverage | C | Partial — live runs mostly TBD |
| 4 | CI integration coverage | D | Partial |
| 5 | Gate coverage | E | Partial — scheduled vs merge gate distinguished |
| 6 | Application source-code coverage | A | Partial — UniteMSC JaCoCo |
| 7 | Traceability completeness | T | Low — qTest/Jira blocked |

**Leadership rule:** Do not combine these into one GS percentage.

---

## 2. Verified percentages (defensible for leadership)

### Universal Platform — V3 UI (inventory share)

| Field | Value |
|-------|------:|
| Numerator | 379 scoped TestNG methods |
| Denominator | 436 nightly source population |
| **Result** | **86.9%** |
| Timestamp | 2026-07-01 SME sign-off |
| Status | **Verified** |
| Not | Requirement-level coverage |

### Universal Platform — V2 UI (inventory share)

| Field | Value |
|-------|------:|
| Numerator | 268 UP-scoped qTest cases |
| Denominator | 744 executed qTest population |
| **Result** | **36.0%** |
| Timestamp | 2026-06-29 qTest export (**Stale**) |
| Status | **Verified** within export scope |

### Mobile 2 — API endpoint automation (**leadership baseline**)

| Field | Value |
|-------|------:|
| Numerator | **22** automated business endpoints |
| Denominator | **25** documented business endpoints (Dinesh workbook) |
| **Result** | **88.0%** |
| Timestamp | **2026-07-14** @ `7ccaf46` |
| Evidence | `17-mobile2-api-automation-signoff.md` |
| Status | **Verified** — retain until sign-off path completes |
| Exclusions | `GET mobilemembers/{planId}/{username}` — acceptance helper, not automation target |

### Mobile 2 — projected (pending sign-off) — **not leadership-final**

| Field | Value |
|-------|------:|
| Numerator | **24** (adds YTD + `GET mobilebanks/{id}` in code @ `cee0de9`) |
| Denominator | **25** |
| **Result** | **96.0%** projected |
| Timestamp | 2026-07-20 code review |
| Status | **Pending verification** |
| Required | Matrix refresh; QC4 master rerun; Stage 1 master rerun; contribution fixture documented |

**Do not claim 100%** — `mobilemembers` remains excluded from automation numerator by approved sign-off scope.

### Mobile 1 — API endpoint automation

| Field | Value |
|-------|------:|
| **Verified baseline** | **1 / 27 = 3.7%** (`POST mobilemembersession`) @ 2026-07-09 |
| **Implemented pending evidence** | **5 additional endpoints** in code @ `cee0de9` (owner, owner menu, profile menu, beneficiary, bank by routing) |
| **Potential** | 6/27 = 22.2% — **not verified** until workbook mapping + suite/master wiring + execution evidence |
| Status | **Verified 3.7%** for leadership; sprint progress reported separately |

---

## 3. CI / execution metrics

| Metric | Value | Status |
|--------|-------|--------|
| Mobile 2 GitLab nightly (D) | 0% scheduled | **Verified gap** — QA-1405 |
| GHA Dashboard slice (D) | Externally validated | **Verified external** — workflow repo not in clone |
| V3 scheduled regression fail-on-error (E) | Yes on scheduled run | **Verified** — not MR gate |

---

## 4. Rejected / corrected prior claims

| Prior claim | Correction |
|-------------|------------|
| Mobile 2 **100% (24/24)** | **Rejected** — used manipulated denominator |
| Mobile 1 **22.2% verified** | **Rejected** — conflated code presence with verified metric |
| GitHub Actions **not implemented** | **Rejected** — Dashboard slice validated externally |
| V3 **hard merge gate** | **Rejected** — scheduled hard-fail only |

See `00-review/contradiction-resolution-ledger.md`.

---

## 5. Safe leadership statements

**Safe:**
- "Mobile 2 verified endpoint automation is **22 of 25 (88%)** per July 14 sign-off evidence."
- "Code on `main` may support **24 of 25 (96%)** — pending refreshed QC4/Stage 1 runs and formal approval."
- "Mobile 1 verified automation remains **1 of 27 (3.7%)** with additional endpoints in active sprint implementation."
- "V3 Universal Experience has a **verified GitLab scheduled regression** with **379 scoped TestNG methods** (86.9% inventory share)."

**Avoid:**
- "Government Savings has X% total coverage."
- "Mobile 2 is 100% complete."
- "GitHub Actions is not implemented."
- "GitLab nightly failures block merge requests" (without pipeline rule evidence).

---

*Regenerate DOCX/XLSX: `tools/generate_gs_assessment_deliverables.py`*
