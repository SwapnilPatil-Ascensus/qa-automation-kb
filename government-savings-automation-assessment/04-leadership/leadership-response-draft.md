# Draft Response — Michael Blake

**Subject:** Government Savings automation coverage — live validation  
**Date:** July 21, 2026

---

Michael,

We completed a **fresh validation** using the current `api-test-automation` repository (`main` @ `cee0de9`), pipeline YAML, and available tooling. **Meaningful automation exists across Government Savings.** Metrics are **platform-specific** — we do not publish one enterprise-wide percentage.

**Current repository truth (July 20, 2026):**

- **Mobile 2 API:** **24 of 25** documented business endpoints (**96%**) have canonical automated tests in merged code. One endpoint (`mobilemembers`) is an intentional harness exclusion. Destructive operations (banks PUT/DELETE, contribution DELETE) are automated but run in **smoke/targeted suites**, not the full master regression. **Last formal execution sign-off was 22/25 (88%) on July 14** — a refresh run is needed to align execution evidence with current code.
- **Mobile 1 API:** **6 of 27** endpoints (**22%**) are implemented in current code (up from the early one-endpoint baseline). **One endpoint** has historical execution-verified evidence (session/auth). None are on a GitLab schedule yet.
- **V3 / Universal Experience:** GitLab **scheduled** Stage 1 regression — **379 scoped TestNG methods (87% inventory share)**.
- **GitHub Actions:** Mobile 2 **Dashboard deployment-validation slice** is **validated** (Nexus archive pattern) — separate from GitLab nightly regression.
- **Metadata API:** GitLab scheduled Stage 1 job.

**Automated tools today:** Python repository scanners, assessment generators (DOCX/Excel/PDF), and prior Universal Platform reconciliation utilities. **qTest, Jira, and GitLab live APIs were not available** in this session (credentials expired/blocked).

**Why not one harmonized system yet:** fragmented ownership, inconsistent identifiers, separate CI platforms, different denominators, and no centralized normalized register with freshness rules.

**Minimum recommendation:** Extend the **existing Python utilities** with read-only API collectors to produce a **governed coverage register** — not a large new platform initially.

**Next actions:** (1) Mobile 2 GitLab nightly (QA-1405), (2) refresh Mobile 2 master execution evidence, (3) provision read-only GitLab/qTest/Jira access, (4) agree denominators and ownership.

Full pack: `qa-automation-kb/government-savings-automation-assessment/`

---

*~320 words*
