# Coverage Governance Model

**Assessment date:** 2026-07-20

## Governance bodies

| Role | Responsibility |
|------|----------------|
| **Program sponsor** | Approves denominators and critical gate lists |
| **QA Automation lead** | Owns register, formulas, collector health |
| **BA / product** | Maintains approved scope catalogs |
| **DevOps** | CI gate implementation, artifact retention |
| **qTest admin** | Schema, custom fields, automation flags |
| **Jira admin** | Scope fields, linkage conventions |

## Policy statements

1. **No unsupported enterprise-wide percentage** shall be quoted externally.  
2. Every metric publication includes: formula ID (A–E), numerator, denominator, timestamp, evidence source, confidence.  
3. **Inventory share ≠ requirement coverage** — mandatory disclaimer for UI metrics.  
4. V2 and V3 UI metrics **shall not be summed**.  
5. Service-level Cucumber coverage **shall not** substitute for BFF acceptance coverage.  
6. Fuzzy reconciliation matches **shall not** enter leadership numerators.  
7. Exceptions to gates require documented waiver (see `ci-gate-strategy.md`).

## Register lifecycle

| Stage | Activity | Frequency |
|-------|----------|-----------|
| **Collect** | Automated snapshots | Daily (CI) / Weekly (ALM) |
| **Reconcile** | Cross-system matching | Weekly |
| **Review** | QA lead validates conflicts | Weekly |
| **Publish** | Leadership summary | Monthly |
| **Approve** | Denominator changes | Quarterly or on major release |

## Metric ownership

| Metric | Owner | Approver |
|--------|-------|----------|
| A — Source-code | Service team | Dev lead |
| B — Business automation | QA Automation | Program + BA |
| C — Execution | QA Automation | QA lead |
| D — CI integration | DevOps | DevOps lead |
| E — Gate | DevOps + QA | Program sponsor |

## Change control

| Change type | Approval |
|-------------|----------|
| New denominator for a domain | Program + BA |
| Inclusion rule change | QA lead + BA |
| New blocking gate | Program sponsor |
| Collector schema v2 | QA Automation |

## Audit readiness

Maintain in git-excluded assessment folder:

- Versioned JSON snapshots  
- Reconciliation CSV with match confidence  
- Evidence register cross-references  
- Decision log for denominator changes  

---

*Freshness SLAs: `data-freshness-and-ownership.md`*
