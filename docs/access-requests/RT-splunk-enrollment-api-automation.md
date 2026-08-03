# RT Request — Splunk Access for API Automation (Enrollment)

**Request type:** Access / Tooling  
**System:** Splunk (Enterprise)  
**Requester:** Swapnil Patil — SSDET, Government Savings, IT Development  
**Manager:** `[TBD — your manager]`  
**Priority:** Normal  
**Duration:** Ongoing (role-based; review annually)  
**Created:** 2026-07-31

---

## RT title (Subject)

```
Splunk read access — QA Automation API triage (Enrollment / Universal Platform, non-prod)
```

---

## Business justification (copy into RT)

### Summary

QA Automation requires **read-only Splunk access** to investigate **enrollment and Universal Platform API** test failures in **non-production** environments (QC4, Stage 1). Without application and gateway logs, automation failures cannot be triaged efficiently — we cannot distinguish **environment issues**, **application defects**, and **test-data/automation problems**, which delays releases and increases repeat failures.

### Business need

| Driver | Detail |
|--------|--------|
| **Program** | Government Savings API automation — Universal Enrollment, Mobile Enrollment API, and related BFF/microservice flows (`api-test-automation`) |
| **Operational impact** | Enrollment API automation is a **priority expansion** (multi-sprint). Nightly/universal enrollment regression includes **300+ TestNG methods**; failures are increasing as coverage grows |
| **Current gap** | When API tests fail (4xx/5xx, timeouts, ECONNRESET, assertion mismatches), QA has **HTTP response only** — no server-side correlation ID, stack trace, or downstream service visibility |
| **Cost of delay** | Each untriaged failure requires **Dev/DevOps round-trips** (hours–days). Recent QC4 mobile auth incident (RT **514351**) required Splunk/pod logs to resolve — same pattern expected for enrollment APIs |
| **Risk if denied** | Slower defect identification, false-positive automation bugs, blocked enrollment automation rollout, repeated escalation to Synergy/DevOps for log pulls |

### What this enables

1. **Faster root-cause analysis** when enrollment API automation fails in CI or manual runs  
2. **Environment vs defect classification** (planned maintenance, cert/auth, DB, vs code bug)  
3. **Reduced dependency** on DevOps for ad-hoc log exports during regression triage  
4. **Support for leadership commitments** on Universal Platform nightly regression and enrollment API automation program (P1 roadmap item)

### What we will NOT use Splunk for

- Production customer PII mining or bulk data export  
- Unauthorized log sharing outside Ascensus  
- Write/admin changes to Splunk indexes or configurations  

---

## Technical justification

### Systems / APIs in scope

| Area | Examples | Environments |
|------|----------|--------------|
| Universal Enrollment API | Enrollment submission, plans, account creation flows | Stage 1, QC4 |
| BFF / gateway | `unite-bff`, API gateway routing, auth headers | Stage 1, QC4 |
| Mobile enrollment (bootstrap) | Mobile enrollment API pilot (`api-test-automation/mobile/enrollment`) | QC4, Stage 1 |
| Supporting services | IDP token exchange, metadata, account services (when enrollment flow fails downstream) | Stage 1, QC4 |

### Typical failure scenarios requiring Splunk

| Symptom | Why Splunk is needed |
|---------|----------------------|
| HTTP 500 / 502 / 503 on enrollment POST | Identify failing microservice, DB timeout, or gateway error |
| HTTP 401 / 403 | Cert, token, or partner-auth path — correlate with JBoss/gateway logs |
| ECONNRESET / connection timeout | Infra/LB/pod health (precedent: RT 514351 mobile login) |
| HTTP 200 with wrong payload | Trace orchestration across services; compare request ID in logs |
| Intermittent / flaky failures | Time-correlate with deploys, batch jobs, or env refresh (e.g. RT 511448 Stage 1 refresh) |

### Repositories / automation context

| Repo | Relevance |
|------|-----------|
| `api-test-automation` | Universal + mobile enrollment API TestNG/RestAssured |
| `qa-automation-kb` | Triage standards, evidence folders, bug lifecycle |
| GitLab nightly | Universal Enrollment (303 methods), IDP, Withdrawals |

### Access level requested

| Item | Request |
|------|---------|
| **Permission** | **Read-only** search and dashboard view |
| **Environments** | **Non-production only** — QC4, Stage 1 (and Dev if enrollment tests run there) |
| **Production** | **Not requested** at this time — escalate via DevOps if prod incident |
| **Indexes / sourcetypes** | `[TBD — confirm with DevOps: unite*, enrollment*, bff*, kofax*, jboss*, api-gateway*]` |
| **Correlation** | Ability to search by timestamp, `traceId`/`correlationId`, HTTP path, plan ID (non-PII), test window |

---

## RT form fields (copy-paste)

| Field | Value |
|-------|-------|
| **Category** | Access Request — Application / Monitoring Tool |
| **Application / System** | Splunk Enterprise |
| **Business unit** | Government Savings — QA Automation |
| **Justification** | See **Business justification** section above |
| **Access type** | Read-only search |
| **Environment** | Non-production (QC4, Stage 1) |
| **Duration** | Ongoing (annual review) |
| **Data sensitivity** | May encounter regulated data in logs — access used only for triage; no export of PII; follow Ascensus data handling policy |
| **Approver** | Direct manager + `[TBD — DevOps / Platform owner if required]` |

---

## Supporting statement (short version for RT description box)

> QA Automation is expanding **enrollment API** test coverage under the Universal Platform program. When automated tests fail in QC4/Stage 1, we currently lack visibility into server-side logs and must open separate DevOps requests for each incident. **Read-only Splunk access** will allow us to triage failures in minutes (env vs defect vs test data), reduce repeat escalations, and support enrollment automation delivery. Precedent: RT **514351** (QC4 mobile login) required pod/Splunk logs for resolution. Requesting **non-prod, read-only** access only.

---

## Acceptance / completion criteria (for RT closure)

- [ ] Splunk SSO/login works for requester
- [ ] Can run basic search against Stage 1 / QC4 enrollment-related indexes
- [ ] Access confirmed read-only (no admin)
- [ ] Index/sourcetype list documented in team runbook (`qa-automation-kb`)

---

## Follow-up actions (after access granted)

1. Document Splunk search patterns for enrollment API triage in `qa-automation-kb`  
2. Add “check Splunk” step to automation bug lifecycle / triage rules  
3. Share index names and sample queries with Priti / enrollment automation owners  
4. Do **not** store log excerpts with PII in git — use JIRA/evidence folders per `CONSTRAINTS.md`

---

## References

| Item | Link / path |
|------|-------------|
| Prior RT (Splunk/logs precedent) | https://rt.acs529.com/Ticket/Display.html?id=514351 |
| Stage 1 refresh RT (env vs defect) | https://rt.acs529.com/Ticket/Display.html?id=511448 |
| Enrollment API program | `programs/unite-msc/leadership/2026-07-17-leadership-update/` |
| Automation bug lifecycle | `automation-bug-lifecycle/` |
| GS automation roadmap (Enrollment P1) | `programs/government-savings-assessment/05-roadmap/` |

---

## Manager approval text (optional — forward to manager)

> Swapnil requires read-only Splunk access (non-prod) to support QA Automation triage of enrollment API test failures. This reduces DevOps dependency, speeds defect identification, and supports the Universal Platform / enrollment automation program. Access is read-only; no production access requested.

---

**Submit to:** https://rt.acs529.com (or internal Service Desk — confirm current Splunk access workflow with DevOps)
