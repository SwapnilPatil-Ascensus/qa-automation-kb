# Government Savings Automation — Leadership Summary

**Assessment date:** July 20, 2026  
**Live validation:** July 20, 2026 (evening)  
**Metric authority:** `03-analysis/verified-metrics-register.csv`

---

## 1. Executive answer

Government Savings has **meaningful automation** across Universal Experience (V3), legacy Unite (V2), MSC Mobile APIs, metadata API, performance assets, and deployment-validation pipelines. **There is no single Government Savings-wide coverage percentage.** Current repository validation is the primary source of truth.

**Current platform-specific results:**

| Platform | What we can say today | Status |
|----------|----------------------|--------|
| **Mobile 2 API** | **96% implemented** (24 of 25 business endpoints) in code on `main` | **Verified (code)** |
| **Mobile 2 API** | Last **execution sign-off: 88%** (22/25) on July 14 — refresh pending | **Stale execution** |
| **Mobile 1 API** | **22% implemented** (6 of 27 endpoints) in current code | **Verified (code)** |
| **Mobile 1 API** | **3.7% execution-verified** (1 of 27) — session/auth | **Verified (historical run)** |
| **V3 / UE UI** | **87% inventory share** (379 of 436 nightly TestNG methods) | **Verified (SME)** |
| **V2 UI (UP-scoped)** | **36% inventory share** (268 of 744 qTest cases) | **Stale export** |
| **Metadata API** | Scheduled GitLab Stage 1 job | **Verified (YAML)** |
| **GitHub Actions** | Mobile 2 Dashboard vertical slice validated (deployment) | **Verified external** |

---

## 2. Current coverage by platform

Automation exists at different maturity levels. Use the **implementation status** labels below — not one blended percentage.

| Area | Implemented in code | Executed / verified | Scheduled in CI |
|------|-------------------:|--------------------:|:---------------:|
| Mobile 2 API | **96%** (24/25) | **88%** stale (22/25) | **No** |
| Mobile 1 API | **22%** (6/27) | **4%** (1/27) | **No** |
| V3 UI | Large nightly inventory | GitLab scheduled | **Yes** |
| V2 UI | Large legacy corpus | Jenkins — unverified live | **Unknown** |
| Universal APIs (beyond metadata) | Manual execution | Not scheduled | **No** |
| ASTRO / COPACS | ASTRO assets exist; COPACS unknown | Not verified | **No** |

---

## 3. Current CI/CD integration

| Channel | What runs today | Purpose |
|---------|-----------------|---------|
| **GitLab** | V3 UI nightly; metadataweb API nightly | Scheduled regression |
| **GitLab** | Stage 5 smoke (manual) | Lightweight smoke |
| **GitHub Actions** | Mobile 2 Dashboard + Nexus flow | **Deployment validation** (not full regression) |
| **Jenkins** | Performance (IDP weekdays); V2/Ant inferred | Perf + legacy |
| **Manual** | Mobile 1/2 API suites; most universal API modules | Local/QA execution |

Failures on GitLab **scheduled** jobs stop **that job** — they are **not verified merge or deployment gates**.

---

## 4. What is fully operational

- V3 Universal Experience **GitLab scheduled regression** (Stage 1)
- Universal **metadataweb API** GitLab scheduled job
- Mobile 2 **canonical TestNG** implementation for **24/25** business endpoints
- Mobile 2 **GitHub Actions Dashboard** deployment-validation slice (externally validated)
- Large **V2** automation corpus (manual/Jenkins execution model)
- **Python assessment tooling** in this knowledge base

---

## 5. What is implemented but not scheduled

- **Mobile 2** master regression (QC4/Stage 1) — **no GitLab nightly** (QA-1405)
- **Mobile 1** six endpoint tests — no CI job
- Most **universal API** modules beyond metadataweb
- **ASTRO** UI regression assets

---

## 6. What is intentionally smoke-only or targeted

- Mobile 2 **PUT/DELETE banks** — smoke suite; excluded from master (destructive)
- Mobile 2 **DELETE contribution** — module suite only
- Mobile 2 **`mobilemembers`** — harness/smoke; excluded from business coverage numerator
- Mobile 2 **YTD** — in master **and** smoke (implemented; execution refresh pending)

---

## 7. What remains unknown or needs scope confirmation

- Live GitLab **schedule cadence** and latest pass/fail (API token expired)
- Jenkins **V2 nightly** job name and schedule
- **COPACS** automation scope
- **qTest/Jira** live reconciliation (APIs blocked)
- Fresh **Mobile 2 master** run post-`cee0de9`

---

## 8. Automated coverage tooling available today

| Capability | Available? |
|------------|------------|
| Repository scanners / endpoint inventories | **Yes** |
| Assessment generators (DOCX/XLSX/PDF) | **Yes** |
| qTest / Jira live integration | **No** (blocked) |
| GitLab live pipeline API | **No** (expired token) |
| JaCoCo on microservices | **Yes** (services) |
| Central governed register | **No** — in progress |

---

## 9. Why tools are not yet harmonized

- Separate CI platforms (GitLab, GHA, Jenkins) with different purposes
- No stable qTest-to-code identifier mapping
- Jira scope not exported live
- Different denominators per platform (endpoints vs TestNG methods vs qTest cases)
- No automated freshness or contradiction detection across systems
- Smoke vs regression placement not modeled in qTest

---

## 10. Minimum recommended solution

Extend existing **Python utilities** with read-only API collectors → normalized JSON/CSV register → weekly reconciliation → leadership + technical workbooks. **No large new application** until the register proves insufficient.

---

## 11. 30 / 60 / 90-day plan

| Horizon | Focus |
|---------|-------|
| **30 days** | Mobile 2 GitLab nightly; refresh QC4/Stage1 master; valid GitLab token; distribute current metrics |
| **60 days** | qTest/Jira collectors; execution snapshot automation; Mobile 1 execution evidence |
| **90 days** | Traceability standards; selective gates; quarterly register cadence |

---

## 12. Leadership decisions and support required

1. Approve **separate metrics** — never one GS-wide %  
2. Accept **96% Mobile 2 implemented** vs **88% last execution sign-off** as different layers  
3. Prioritize **QA-1405** Mobile 2 GitLab nightly  
4. Sponsor **GitLab API token** refresh for live validation  
5. **30–40% BA capacity** for denominators and qTest hygiene  
6. Clarify **COPACS** and **ASTRO** recurring scope  

---

## 13. Appendix — metric definitions

| Metric | Definition |
|--------|------------|
| **Implemented automation** | Canonical automated test exists in merged code |
| **Executed verified** | Successful run evidence within agreed window |
| **Scheduled CI** | Included in active pipeline schedule |
| **Inventory share** | Subset ÷ source population — not requirement coverage |
| **Gate coverage** | Failure demonstrably blocks merge/deploy/promotion |

---

*Technical detail: `03-analysis/technical-assessment-live-validation.md` · Endpoint CSVs: `01-inventory/mobile*-endpoint-current-state.csv`*
