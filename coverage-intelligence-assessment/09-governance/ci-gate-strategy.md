# CI Gate Strategy — Government Savings

**Assessment date:** 2026-07-20  
**Principle:** Risk-based distinct gates — not one crude enterprise coverage threshold

## Gate categories

### 1. Unit / source-code coverage gate (A)

| Attribute | Recommendation |
|-----------|----------------|
| **Where** | UniteMSC microservice repos (application code) |
| **Trigger** | Push/MR to service repo |
| **Threshold** | No unacceptable regression per service; minimum by app team — **not one GS-wide %** |
| **Blocking** | Informational first; blocking after Sonar enabled |
| **Owner** | Service team + DevOps |
| **Exception** | Waiver with owner, reason, expiry |
| **Rollout** | Enable Sonar (`RUN_SONARQUBE`) → set team thresholds → MR gate |
| **Tooling** | JaCoCo + SonarQube |

**Status today:** JaCoCo **Verified**; Sonar **disabled**; no blocking code-coverage gate **Verified**

### 2. Test-result gate (B/C)

| Attribute | Recommendation |
|-----------|----------------|
| **Where** | Service CI + QA automation repos |
| **Trigger** | Push/MR / schedule |
| **Threshold** | Required unit/integration tests pass |
| **Blocking** | **Yes** on service repos; scheduled QA jobs exit non-zero |
| **Owner** | Dev + QA |
| **Exception** | Emergency bypass via release manager |
| **Rollout** | Already on UniteMSC; extend to Mobile2 nightly |
| **Tooling** | Maven Surefire, GitLab JUnit reports |

**Status:** V3 + metadataweb scheduled — **Verified hard fail**

### 3. Critical smoke gate (E)

| Attribute | Recommendation |
|-----------|----------------|
| **Where** | Deployment validation (Stage5 smoke, Mobile2 Nexus when built) |
| **Trigger** | Pre/post deploy manual or workflow |
| **Threshold** | Critical journeys pass (approved list) |
| **Blocking** | **Yes** for promotion to target env |
| **Owner** | QA + Release |
| **Exception** | Documented risk acceptance |
| **Rollout** | Stage5 smoke exists — formalize critical list |
| **Tooling** | GitLab manual job; future GitHub Actions |

### 4. Traceability gate

| Attribute | Recommendation |
|-----------|----------------|
| **Where** | New automation MRs |
| **Trigger** | MR to `api-test-automation`, `prime-test-automation` |
| **Threshold** | Stable `automation_id` or Jira/qTest reference in PR |
| **Blocking** | Soft → hard over 60 days |
| **Owner** | QA Automation |
| **Tooling** | MR template + optional CI lint script |

**Status:** **Planned**

### 5. Regression-registration gate

| Attribute | Recommendation |
|-----------|----------------|
| **Where** | Maintained tests |
| **Trigger** | New test merge |
| **Threshold** | Assigned to approved suite XML / Maven profile |
| **Blocking** | CI check that suite file updated |
| **Owner** | QA Automation |

**Status:** **Planned**

### 6. Evidence-publication gate

| Attribute | Recommendation |
|-----------|----------------|
| **Where** | All scheduled regression |
| **Trigger** | Pipeline complete |
| **Threshold** | JUnit/Surefire archived ≥30 days |
| **Blocking** | Informational → required for audit |
| **Owner** | DevOps |
| **Tooling** | GitLab artifacts |

**Status:** **Partial** — V3 publishes JUnit **Verified**

### 7. Quality gate exception process

| Field | Required |
|-------|----------|
| Waiver ID | Yes |
| Owner | Named approver |
| Reason | Business or technical |
| Expiration | Max 30 days (recommended) |
| Affected metric | A–E specified |

## What NOT to do

- Block every environment deployment on **full GS regression** (5,000+ scenarios across frameworks)  
- Use QA pass % as JaCoCo replacement  
- Single **80%** enterprise threshold without domain split  

## Rollout sequence

1. **Now:** Document existing gates (this assessment)  
2. **30d:** Mobile2 scheduled gate (QA-1405)  
3. **60d:** Traceability soft gate on new MSC API tests  
4. **90d:** Sonar pilot on 2 services; critical smoke list approved  

---

*See `coverage-governance-model.md`, `05-pipelines/ci-gate-audit.md`*
