# QA Automation — Framework, Tools & Evaluation Summary

**Prepared for:** Rajib Akhter  
**Prepared by:** QA Automation  
**Date:** June 2026  
**Purpose:** Answer leadership questions on current automation stack, homegrown framework design, alternatives evaluated, and rationale for maintaining the current approach.

**Source documents (this repo — `docs/Leadership Docs/`):**

| Document | Content |
|----------|---------|
| `QA_Automation_Framework_Updated.docx` | Framework & tools overview (PRIME, JSONAPI, mobile, performance) |
| `API Automation Testing FrameworkTool Evaluation.pdf` | API tool/framework evaluation matrix |
| `NeoLoad Tricentis Performance testing Tool.pdf` | Performance tool comparison (NeoLoad vs JMeter/Taurus/BlazeMeter) |
| `Quality Tools List.pdf` | Enterprise quality tooling inventory and licensing |

**Related Confluence / GitLab references:** Prime V2/V3 master overview, JSONAPI documentation, API Automation KT, Quality Tools List, NeoLoad evaluation page (links in Section 6).

---

## Executive Summary

Ascensus Government Savings (AGS) QA Automation operates on **homegrown, Java-based frameworks** built for our domain (529, ABLE, enrollment, account maintenance, contributions, IDP, and related back-office flows). The stack is **not a single off-the-shelf product** — it is a **mature combination of PRIME (UI regression), JSONAPI (API automation), JMeter/Taurus/BlazeMeter (performance), and a separate mobile stack (WebdriverIO/BrowserStack)**, integrated with **Jenkins, GitLab CI, qTest, and Jira**.

We **have documented evaluations** for API automation tools and performance tooling. The **recommended and adopted direction** remains **REST Assured + Maven hybrid framework (JSONAPI)** for API and **PRIME v2/v3** for UI — because they align with existing coverage, team skills, CI/CD, and deep database validation requirements.

**Strategic conclusion:** Replacing the current stack with a market alternative (Playwright, Karate, Tosca, NeoLoad-as-primary, etc.) would require **multi-year migration**, **loss of regression depth**, **retraining/hiring**, and **high execution risk** — with limited benefit given how customized and stable our frameworks already are.

---

## 1. What Framework and Tools We Use for Automation

### 1.1 Front-End / UI Regression (Non-Mobile)

| Framework | Build | Core technologies | Role today |
|-----------|-------|-------------------|------------|
| **VESPA (Legacy)** | Ant | Groovy, Selenium, TestNG | Original framework; largely superseded |
| **PRIME v2** | Ant | Java 8, Selenium, Cucumber, TestNG, JDBC, BrowserStack | Active — legacy Unite/monolith regression (Jenkins, Stage1) |
| **PRIME v3 (Current direction)** | Maven | Java 17, Selenium, Cucumber, TestNG, JDBC, Nexus, BrowserStack | Active — modular UI automation (GitLab CI; UE, IDP, expanding modules) |

**Execution & CI/CD**

| Platform | Primary use |
|----------|-------------|
| **Jenkins** | PRIME v2 nightly/smoke/release regression |
| **GitLab CI/CD** | PRIME v3 pipelines, artifact publishing (Nexus) |
| **GitHub Actions** | Target direction for microservices/metadata flows |
| **BrowserStack** | Cross-browser / device compatibility (where applicable) |
| **Selenium Grid (internal)** | Hub-based regression reports (e.g., Stage1 hub) |

---

### 1.2 API Automation

| Framework | Build | Core technologies | Role today |
|-----------|-------|-------------------|------------|
| **JSONAPI (homegrown)** | Maven | Java 17, **REST Assured**, TestNG, JDBC, Nexus | **Primary** AGS API automation framework |
| **Legacy standalone API automations** | Maven (varies) | REST Assured, Gherkin patterns | Partner/project-specific; being consolidated |
| **Microservice co-located tests** | Maven | Java, Cucumber, service-local runners | In app repos; migration to JSONAPI in progress (e.g., UniteMSC) |

**Supporting tools:** Postman (manual/exploratory API), SoapUI (legacy manual), Boomerang (Chrome extension).

---

### 1.3 Mobile Automation

| Track | Stack | Notes |
|-------|-------|-------|
| **Mobile UI (separate workstream)** | Node.js, TypeScript, **WebdriverIO**, BrowserStack | Architecture-team aligned; not part of PRIME core |
| **Mobile microservices API (current program)** | Java, Cucumber, REST Assured, Maven | Migrating into **JSONAPI / mobile-microservices** structure — API only, not Appium |

---

### 1.4 Performance Testing

| Tool | Role |
|------|------|
| **Apache JMeter** | Script-based load/stress testing (open source) |
| **Taurus** | YAML-driven CI-friendly execution wrapper |
| **BlazeMeter** | Cloud load generation, dashboards, reporting (~$4k license per Quality Tools List) |

---

### 1.5 QA Tooling Ecosystem (Governance & Support)

From **Quality Tools List** and practice-wide usage:

| Category | Tools |
|----------|-------|
| Test management | **qTest** (Tricentis), Jira |
| Issue tracking | **Jira** |
| IDE | IntelliJ, Eclipse, WebStorm (mobile) |
| Source control | GitLab (migration from Perforce) |
| Monitoring / logs | Splunk, New Relic |
| Accessibility | JAWS, WAVE, UsableNet AQA |
| Security (manual) | Burp Suite |
| Browsers / devices | Selenium, BrowserStack, physical devices where required |

---

## 2. What Our Homegrown Framework Is Made Of — and How It Differs

### 2.1 Core homegrown platforms

Our automation is centered on two **internally maintained** platforms:

1. **PRIME** — UI and end-to-end regression (member, CSR, enrollment UI, IDP flows, etc.)
2. **JSONAPI** — API and back-office service validation (REST Assured hybrid framework)

Both share design goals: **Java**, **TestNG execution**, **environment-driven configuration**, **Oracle/JDBC validation**, and **CI/CD integration**.

---

### 2.2 PRIME — architecture components

| Layer | What it does | Why it matters |
|-------|--------------|----------------|
| **Execution** | TestNG runners, Cucumber features, step definitions, tags/suites | BDD-readable scenarios + pipeline-friendly suite selection |
| **Resource / configuration** | Environment properties (Stage1, QC4, etc.), plan/traunch configs | Same tests across environments without code forks |
| **Business logic** | Page objects, action classes, API clients (where shared) | Maintainable UI flows across many plans |
| **Data validation** | SQL scripts, DB assertions, back-office validation steps | **Key differentiator** — validates data layer, not just UI |
| **Reporting** | TestNG reports, Jenkins/GitLab artifacts, hub HTML | Leadership and dev triage visibility |
| **Shared libraries (v3)** | Nexus-published modules, modular repo layout | Reduces duplication vs monolithic v2 Ant layout |

**PRIME v2 vs v3 distinction**

| Aspect | PRIME v2 | PRIME v3 |
|--------|----------|----------|
| Build | Ant | Maven |
| Java | 8 | 17 |
| Structure | Monolith-oriented | Modular, shared libraries |
| CI | Jenkins (primary) | GitLab CI (primary) |
| Status | Active legacy gate | Forward-looking standard |

---

### 2.3 JSONAPI — architecture components

| Layer | What it does | Why it matters |
|-------|--------------|----------------|
| **REST Assured core** | HTTP calls, auth, JSON/XML validation | Industry-standard API library on Java |
| **Hybrid framework** | Custom clients, encryption, plan-specific logic | Supports AGS auth schemes, encryption, complex payloads |
| **TestNG + (optional) Cucumber** | Suite execution, tagging | Aligns with PRIME skills and CI patterns |
| **JDBC / database-loader** | DB setup and assertions | Same enterprise validation model as UI |
| **jsonapi-parent / modules** | `json-api`, `universal/`, extending to `mobile-microservices/` | Reuse across 529, ABLE, microservices |
| **Nexus artifacts** | Versioned dependencies | Controlled promotion across teams |

---

### 2.4 What sets our homegrown approach apart from market tools

| Differentiator | Description |
|----------------|-------------|
| **Domain-specific** | Built for AGS plans, traunches, enrollment, CSR, IDP — not generic SaaS templates |
| **Deep DB validation** | Oracle/SQL integrated into pass/fail — uncommon in low-code or scriptless tools |
| **Cross-plan reuse** | Configuration-driven execution across many business lines |
| **Pipeline-native** | Nightly regression, Stage1 gates, multi-environment property model |
| **Extensibility** | Custom encryption, feeds, file manipulation, semantic/DBPR-aware patterns |
| **Investment already made** | Thousands of scenarios, years of CI history, trained staff |

---

### 2.5 Known limitations (transparent)

| Limitation | Mitigation in progress |
|------------|------------------------|
| Some API tests still **co-located in application repos** | UniteMSC → centralized JSONAPI migration program |
| **PRIME v2 + v3** run in parallel | v3 phased rollout; v2 remains gate until modules migrate |
| **Mobile UI** not fully unified with PRIME | Separate WebdriverIO track; API mobile work uses JSONAPI |
| API **CI pipelines** still maturing in places | Pipeline integration stories in backlog; GitHub migration alignment |
| Documentation spread across GitLab/Confluence | Consolidation via QA KB + leadership briefs (this document) |

---

## 3. Alternatives We Have Evaluated — and Market Landscape

### 3.1 API automation — formal evaluation on file

**Source:** `API Automation Testing FrameworkTool Evaluation.pdf`  
**Goal stated in doc:** Build a lightweight API framework for legacy APIs and microservices.

| Option | Summary assessment | Outcome |
|--------|-------------------|---------|
| **Karate** | Gherkin API tool; easy start; weak IDE support; TestNG support deprecated; limited custom auth | Not selected as primary |
| **Tosca (Tricentis)** | Scriptless, model-based; existing Tricentis relationship (qTest); licensing limits | Not selected for API framework |
| **ACCELQ** | Cloud BDD; no scripting; trial-only commercial | Not selected |
| **Katalon** | Record/playback; Groovy-only; performance concerns | Not selected |
| **ReadyAPI** | Scriptless + Groovy; licensing cost | Not selected |
| **Legacy standalone automations** | Partner-specific; duplicate code; not a reusable framework | Consolidate into JSONAPI |
| **Microservice in-repo automation** | Good for new services; weak for legacy API; dev-coupled | Selective use; migrate shared scenarios to JSONAPI |
| **PRIME ASTROAPI/UNITEAPI** | Reuses PRIME DB/reporting; heavy for API-only; limited CI | Superseded by JSONAPI direction for API |
| **REST Assured + hybrid framework** | Java team fit; CI-friendly; customizable auth/encryption/JSON | **Recommended and adopted (JSONAPI)** |

**Evaluation conclusion (from source doc):**

- Ready-made tools address **general** API testing; they limit customization for AGS-specific auth, encryption, and DB validation.
- A **custom Java hybrid framework** provides freedom to match project needs, reporting standards, and test data management.
- Team has **Java expertise**; REST Assured has strong community support.
- Cucumber at API layer adds complexity — use where BDD value exceeds maintenance cost (JSONAPI uses it selectively).

---

### 3.2 Performance testing — formal evaluation on file

**Source:** `NeoLoad Tricentis Performance testing Tool.pdf`

| Tool | Assessment |
|------|------------|
| **NeoLoad (Tricentis)** | Enterprise GUI, SLA dashboards, smart correlation, wide protocols; **expensive**; less script flexibility vs JMeter |
| **JMeter + Taurus + BlazeMeter (current)** | Open source + SaaS; YAML/CI friendly; team already invested; cost-efficient |

**Recommendation documented in evaluation:**

> **Stick with JMeter + Taurus + BlazeMeter** as primary tooling.  
> **Consider NeoLoad selectively** for pilot/POC on high-visibility flows or teams needing GUI-driven perf — not as a wholesale replacement.

---

### 3.3 UI automation — market alternatives (context)

**Note:** No single enterprise doc lists a full UI tool bake-off (Playwright vs Cypress vs Selenium). Below is **market context** plus **internal direction**.

| Market option | Typical use | Relative to our stack |
|---------------|-------------|------------------------|
| **Selenium + Java (current)** | Enterprise UI regression | **In production** — PRIME v2/v3 |
| **Playwright** | Modern browser automation | Would require rewrite of massive Cucumber/TestNG corpus |
| **Cypress** | JS-centric UI tests | Different language; no JDBC/enterprise layer fit |
| **Tosca / Katalon / ACCELQ** | Low-code E2E | Evaluated for API; licensing and customization limits for AGS DB validation |
| **BrowserStack** | Execution layer | **Already integrated** — complements Selenium, not a framework replacement |

---

### 3.4 Documentation gap (acknowledged)

| Topic | Status |
|-------|--------|
| Framework inventory (PRIME, JSONAPI, tools) | **Documented** — GitLab docs, Confluence, Quality Tools List, this brief |
| API tool evaluation matrix | **Documented** — PDF in Leadership Docs |
| Performance tool evaluation | **Documented** — NeoLoad PDF |
| **Single consolidated “UI tool bake-off” (Playwright/Cypress)** | **Not found** as formal decision record — recommend future 1-pager if leadership requires |
| **Strategic multi-year roadmap (v2 sunset, GitHub CI)** | Partially in Confluence/CICD KB — link from program hubs |

---

## 4. Why We Maintain the Current Setup

The current stack is the **rational choice** given where we are today — not because alternatives are unknown, but because **migration cost and risk outweigh benefit**.

### 4.1 Scale of existing automation investment

| Factor | Reality |
|--------|---------|
| **Coverage depth** | PRIME v2/v3 runs **hundreds of scenarios** nightly across Stage1 (enrollment, CSR, contributions, transfers, IDP, web login/reg, etc.) |
| **API corpus** | JSONAPI and legacy API suites cover **multiple plans and services** with DB-backed validation |
| **Performance scripts** | JMeter/Taurus assets tied to IDP, enrollment, and platform perf programs |
| **Historical CI signal** | Jenkins/GitLab pipelines, hub reports, and leadership regression visibility built around current tools |

Replacing the stack means **rebuilding or porting** this coverage — not swapping a license.

---

### 4.2 Migration is not a simple tool change

| Barrier | Impact |
|---------|--------|
| **Language & patterns** | Java, TestNG, Cucumber, REST Assured, JDBC — embedded in thousands of files |
| **Custom layers** | Resource managers, SQL validation, plan configs, encryption — no off-the-shelf equivalent |
| **Parallel frameworks** | v2 + v3 + JSONAPI + mobile tracks — migration already in flight **within** Java ecosystem |
| **CI/CD rewiring** | Jenkins, GitLab, Nexus, secrets, env properties — all coupled to current runners |
| **Flakiness re-baseline** | New tools would require months of stabilization before trust matches today’s baselines |

Industry migrations of this size typically run **12–24+ months** with **dual maintenance** — we are already executing a **controlled internal migration** (v2 → v3, app-repo API → JSONAPI) without throwing away the language or validation model.

---

### 4.3 Team and hiring alignment

| Factor | Reality |
|--------|---------|
| **Current skills** | QA and SDET hires are aligned to **Java, Selenium, Cucumber, TestNG, REST Assured, Maven** |
| **Training cost** | Moving to Tosca, Karate-only, or Playwright-first would require **broad retraining or new hiring profile** |
| **Dev collaboration** | Devs already understand Java/Maven test repos and PRIME/JSONAPI layout |
| **Bus factor mitigation** | Documentation, KB, and modular v3/jsonapi structure reduce key-person risk **within** current stack |

---

### 4.4 Framework is actively updated — not frozen legacy

| Evolution | Status |
|-----------|--------|
| **PRIME v3** | Java 17, Maven, Nexus, GitLab CI — modern modular standard |
| **JSONAPI** | Ongoing extension (universal modules, mobile-microservices migration) |
| **Pipeline strategy** | GitHub/GitLab alignment for UniteMSC and microservices |
| **Tooling** | BrowserStack, BlazeMeter, qTest, Jira — integrated ecosystem |
| **Evaluations** | API and perf alternatives **documented**; decisions favor extend-not-replace |

The strategy is **evolve the homegrown frameworks**, not abandon them for a market substitute that would discard DB validation and plan-specific logic.

---

### 4.5 Cost, stability, and risk

| Dimension | Current stack | Wholesale replacement |
|-----------|---------------|------------------------|
| **License cost** | JMeter/Taurus open source; BlazeMeter/qTest/Jira known spend | Tosca/NeoLoad/ACCELQ add **six-figure** enterprise licensing |
| **Stability** | Known flakes and env issues — **understood** and triaged | New tool = **new unknown failure modes** |
| **Time to value** | Incremental stories (v3 module, JSONAPI migration) deliver weekly | Big-bang rewrite delays regression protection |
| **Leadership reporting** | Existing hub reports, JIRA, nightly status | Re-establish all gates from zero |

---

### 4.6 Leadership conclusion (recommended wording)

> **We use PRIME and JSONAPI because they are purpose-built for AGS**, already carry the majority of our regression coverage, integrate with our DB and CI/CD model, and match our team’s skills. Alternatives **have been evaluated** where formal analysis exists (API tools, NeoLoad for performance). Market tools excel at generic scenarios but **do not replace** our SQL validation, plan configuration, and pipeline investment without a multi-year migration. The right path is to **continue modernizing within the current stack** (PRIME v3, JSONAPI consolidation, pipeline hardening) — not to adopt a parallel framework that would duplicate cost and delay protection of Stage1/production releases.

---

## 5. Quick Reference — Answers to Rajib’s Three Questions

| Question | Short answer |
|----------|--------------|
| **What framework and tools do we use?** | **UI:** PRIME v2/v3 (Selenium, Cucumber, TestNG, Java). **API:** JSONAPI (REST Assured, Maven, TestNG). **Perf:** JMeter, Taurus, BlazeMeter. **Mobile UI:** WebdriverIO/BrowserStack. **CI:** Jenkins, GitLab, GitHub (target). **Governance:** Jira, qTest. |
| **What is our homegrown framework made of — and distinction?** | Modular Java frameworks (PRIME + JSONAPI) with TestNG/Cucumber execution, environment config, **integrated Oracle DB validation**, Nexus/Maven (v3/API), and pipeline-native regression — customized for AGS plans, not generic SaaS. |
| **What alternatives have we looked at?** | **API:** Karate, Tosca, ACCELQ, Katalon, ReadyAPI, legacy standalones — **REST Assured hybrid (JSONAPI) selected.** **Perf:** NeoLoad evaluated — **stay on JMeter/Taurus/BlazeMeter.** **UI:** Selenium-based PRIME remains standard; Playwright/Cypress not formally bake-off documented. |

---

## 6. References & Links

### Internal documents (this folder)

- `QA_Automation_Framework_Updated.docx`
- `API Automation Testing FrameworkTool Evaluation.pdf`
- `NeoLoad Tricentis Performance testing Tool.pdf`
- `Quality Tools List.pdf`

### Confluence (from framework overview doc)

| Topic | Link |
|-------|------|
| UI automation tech stack | Confluence pageId **315570801** |
| API tool evaluation | Confluence pageId **193361022** |
| API Automation KT | GSSD — API Automation space |
| IDP performance tool evaluation | GSSD — IDP Login Performance Testing |
| NeoLoad evaluation | GSSD — NeoLoad: Tricentis Performance testing Tool |
| Quality Tools List | GSSD — Quality Tools List |
| BI Dashboard tool evaluation | Confluence pageId **326742259** |

### GitLab documentation

| Framework | Documentation path (GitLab) |
|-----------|----------------------------|
| PRIME v2 | `automation` repo — `prime/docs/general-documentation.docx` |
| PRIME v3 | `prime-test-automation` — `prime/prime-core/docs/Prime Documentation.docx` |
| JSONAPI | `api-test-automation` — `jsonapi/jsonapi-core/docs/JsonAPI Documentation.docx` |

### QA Automation KB (this repository)

| Topic | Path |
|-------|------|
| Program hub — mobile MSC API migration | `docs/mobile-automation-program-hub/` |
| CI/CD landscape | `10_IMPORTS_RAW/AM_Regression_Reports/docs/CICD/` |
| Agent / team bootstrap | `docs/agent-context/` |

---

## 7. Optional Follow-Up Actions (if leadership wants)

| Action | Owner | Benefit |
|--------|-------|---------|
| Publish this brief to Confluence under GSSD leadership folder | QA Lead | Single link for Rajib/Henry reviews |
| Add 1-page **UI tool landscape** (Playwright/Cypress vs Selenium) decision memo | QA + Architecture | Closes documented gap |
| Annual **tool evaluation refresh** (API + perf + CI) | QA Automation | Keeps Rajib’s question answer current without ad-hoc searches |

---

**Document version:** 1.0  
**Classification:** Internal — leadership briefing  
**Next review:** Q3 2026 or after major framework change (e.g., PRIME v2 sunset date)
