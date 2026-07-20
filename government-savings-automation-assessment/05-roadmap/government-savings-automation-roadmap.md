# Government Savings Automation Roadmap

**Assessment date:** 2026-07-20  
**Horizons:** Immediate (0–30d) · Near-term (30–90d) · Strategic (90+d)

---

## Immediate — 0 to 30 days

| # | Outcome | Business value | Owner | Dependency | Priority | Evidence for closure |
|---|---------|----------------|-------|------------|----------|----------------------|
| I-1 | Refresh Mobile 2 QC4 + Stage 1 master evidence | Defensible MSC API sign-off | QA Automation | DB tunnel; contribution SQL fixtures | P1 | 40/40 Surefire + HTML report @ commit |
| I-2 | Wire GitLab nightly Mobile 2 regression (QA-1405) | Recurring API gate | DevOps + QA | Secure files; runner network QC4 | P1 | Green scheduled pipeline URL |
| I-3 | Update MSC sign-off docs (`16`, `17`) | Leadership-ready MSC status | QA Automation | I-1 complete | P1 | Approved sign-off package |
| I-4 | Confirm Mobile 1 sprint scope (6→N endpoints) | MSC member API progress | QA + Program | Jira backlog; test data | P1 | Endpoint matrix refresh |
| I-5 | Publish GS CI gate inventory (this assessment) | Single source of truth | QA Automation | None | P1 | Leadership distribution of assessment folder |
| I-6 | Live-verify GitLab schedule cadence (V3 + metadataweb) | Accurate "what runs nightly" | DevOps | GitLab access | P2 | Schedule screenshot + last pipeline |
| I-7 | Retire stale metrics (M2 88%, M1 3.7%) | Prevent misleading leadership numbers | QA Automation | Code review complete | P2 | Updated leadership slides |

---

## Near-term — 30 to 90 days

| # | Outcome | Business value | Owner | Dependency | Priority | Evidence for closure |
|---|---------|----------------|-------|------------|----------|----------------------|
| N-1 | Mobile 1 non-IDP endpoint expansion | MSC API coverage growth | QA Automation | Sprint capacity | P1 | Endpoint % with execution evidence |
| N-2 | Mobile 1 IDP hardening | NMD parity | QA Automation | IDP test accounts | P1 | Stage1 nmdirect module passes |
| N-3 | Implement GitHub Actions Mobile 2 Nexus slice (if approved) | Deployment validation path | DevOps | Nexus secrets; workflow PR | P2 | Green workflow run |
| N-4 | Schedule MSC functional performance | Perf regression visibility | Performance QA | Clean non-IDP + IDP JMX runs | P2 | Jenkins periodic trigger |
| N-5 | ASTRO/SFRP scope + recurring execution decision | Close GS UI gap | Program + QA | Business priority | P2 | Documented scope + schedule |
| N-6 | COPACS automation scope intake | Unknown area resolution | Program + SME | Platform owner | P2 | Scope doc or explicit out-of-scope |
| N-7 | V2 backoffice vs V3 nightly mapping | Batch coverage clarity | QA + DevOps | Jenkins/GitLab inventory | P2 | Suite-to-pipeline matrix |
| N-8 | qTest ↔ automation traceability (GS) | Audit-ready metrics | QA + BA | qTest export | P2 | Mapped case IDs |
| N-9 | Universal API modules on CI (accountweb auth) | UP API gate expansion | DevOps + QA | Pipeline design | P3 | Scheduled jobs |

---

## Strategic — 90+ days

| # | Outcome | Business value | Owner | Dependency | Priority | Evidence for closure |
|---|---------|----------------|-------|------------|----------|----------------------|
| S-1 | Enrollment API automation program | UP enrollment API gate | QA + DevOps | api-test-automation enrollment module growth | P1 | Endpoint matrix + nightly job |
| S-2 | Dynamic API-driven test-data capability | Reduced fixture fragility | QA + Data | SQL/utility design | P2 | KB + implementation |
| S-3 | Broader microservice CI integration | Service-level GS quality | DevOps | UniteMSC template alignment | P2 | Per-service gate doc |
| S-4 | Standardized CI quality gates (GS playbook) | Consistent release confidence | DevOps + QA | Leadership approval | P2 | Published playbook |
| S-5 | Quarterly GS automation roadmap | Predictable planning | Program + BA | 30–40% reporting capacity | P1 | Quarterly published roadmap |
| S-6 | Definition of Done — API + perf validation | Clear completion criteria | Program | SME sign-off | P2 | Updated DoD in Jira/confluence |
| S-7 | V2 → V3 consolidation strategy execution | Reduce dual-framework cost | Program + QA | Jenkins sunset plan | P2 | Migration milestones |
| S-8 | SQL L5 API–DB reconciliation (MSC) | Deeper validation | QA Enhancement | mobile2-api-db-validation backlog | P3 | L5 framework pilot |

---

## Ownership model (recommended)

| Track | Primary owner | Supporting |
|-------|---------------|------------|
| MSC Mobile API | QA Automation (AMSQUAD) | DevOps, Persistent |
| V3 UI nightly | QA Automation + DevOps | UE/Unite dev |
| V2 legacy UI | QA Automation (legacy) | Jenkins admin |
| Performance | Performance QA | DevOps load servers |
| Metrics / reporting | QA Lead + BA (~30–40%) | Program management |
| Scope / priority | Program lead (Rajiv/Rajib chain) | Kevin, Henry, Michael |

---

## Reporting cadence (recommended)

| Artifact | Frequency | Audience |
|----------|-----------|----------|
| GS coverage matrix refresh | Quarterly | Leadership |
| CI gate status | Monthly | DevOps + QA leads |
| MSC API endpoint matrix | Per sprint | Program team |
| UP inventory share | Semi-annual or on major release | UP stakeholders |

---

*Linked deliverables: `government-savings-coverage-matrix.xlsx`, `leadership-summary.md`*
