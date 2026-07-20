# Draft Response — Michael Blake

**Subject:** Government Savings test automation coverage — feasibility assessment  
**Assessment date:** 2026-07-20  
**Status:** Draft for review — politically neutral

---

Michael,

Following your questions on Government Savings test automation coverage and whether we can calculate and trust a figure such as "80% covered," we completed a **read-only feasibility assessment** across qTest, Jira, automation repositories, and CI/CD pipelines. Below is a concise summary. Full evidence is in the `coverage-intelligence-assessment` artifact pack.

## Do we have an automated coverage tool?

**Partially.** We have Python-based assessment utilities and SME-reviewed Universal Platform coverage work (June–July 2026). We do **not** yet have a continuously running enterprise tool that automatically reconciles Jira scope, qTest inventory, repository tests, and live pipeline results. That capability is **feasible** with a small extension of existing Python collectors — not a new web application — once read-only API access is provisioned.

## What automation exists today?

Verified capabilities include:

- **Unite V3 / Universal Experience:** GitLab nightly regression on Stage 1 (**379 scoped TestNG methods**; **86.9%** of the nightly inventory population — inventory share, not requirement coverage).
- **Universal metadata API:** Scheduled GitLab Stage 1 job.
- **Mobile 2 MSC APIs:** **100%** of **24 in-scope documented endpoints** automated in code (`api-test-automation`); **nightly GitLab scheduling is pending** (QA-1405).
- **Mobile 1 MSC APIs:** **6 of 27** documented endpoints (**22.2%**).
- **V2 Unite UI:** Large automation asset base (~2,176 scenarios) with qTest PRIME history (**744** executed cases in last available export); recurring Jenkins gate **not verified** in this pass.
- **ASTRO, performance, MSC service tests:** Assets exist; CI integration and scope vary by area.

## Can we trust "80% covered"?

**Not as a single Government Savings number today.** Source-code coverage (JaCoCo), business scenario coverage, execution coverage, CI integration, and gate coverage are **different metrics** and must not be combined without an explicit formula and approved denominator.

Within **documented scope**, defensible figures include the V3 inventory share, V2 UP-scoped qTest inventory share (36%), and Mobile 2 endpoint automation (100% in-scope). Each has a documented numerator, denominator, timestamp, and evidence source.

## CI quality gates

**Some are integrated; coverage is uneven.**

- **Verified hard gates (scheduled):** V3 UI GitLab nightly; metadataweb API nightly.
- **Service repos:** Build/test gates with JaCoCo; SonarQube currently disabled on reviewed UniteMSC pipelines.
- **Gaps:** Mobile 2 API nightly, most universal API modules, V2 full nightly, ASTRO recurring regression, GitHub Actions Mobile 2 workflow (documented but not in repository).

We recommend **risk-based smoke/deployment gates** and **scheduled full regression** — not blocking every deployment on the complete GS regression suite.

## Recommended next step

Establish an automated **Government Savings quality coverage register** that reconciles approved scope (Jira + catalogs), test inventory (qTest), implementation (repositories), and execution (GitLab/Jenkins) — reporting **separate metrics** for source-code, business automation, execution, CI integration, and gates. Begin with **read-only reporting** and data-quality remediation before introducing additional blocking gates.

**30 days:** Credentials, weekly register, QA-1405 Mobile 2 nightly.  
**60 days:** Live qTest/Jira reconciliation, execution snapshots.  
**90 days:** Traceability standards, selective gate pilots, quarterly cadence.

## Leadership support requested

1. Approve domain-specific denominators (not one enterprise %).  
2. Provision read-only qTest, Jira, and GitLab API access.  
3. Sponsor QA-1405 DevOps work.  

Happy to walk through the assessment pack or the executive summary on a call.

Regards,  
QA Automation

---

*Evidence pack: `coverage-intelligence-assessment/10-leadership/executive-summary.md`*
