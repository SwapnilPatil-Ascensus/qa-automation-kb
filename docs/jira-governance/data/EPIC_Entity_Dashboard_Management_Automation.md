# Epic (draft): V3 — Entity Dashboard & Entity Management — Test design, automation, execution, regression & smoke

**Document:** `docs/jira-governance/data/EPIC_Entity_Dashboard_Management_Automation.md`  
**Purpose:** Single source for JIRA **Epic** creation, backlog decomposition, and **test-case inventory** for Entity-related work across **this sprint and next** (aligned to **AMSQUAD Sprint 26.04 – 26.05** and forward).  
**JIRA:** Create Epic in **QA** project, then paste **Epic key** into the metadata table below and link child stories.

---

## 1. Evidence from `docs/jira-governance/data` (inventory)

| Source | What it says about Entity / Unite |
|--------|-----------------------------------|
| **`Sprint Data/AMSQUAD Sprint 26.04 - 26.05.csv`** | **[QA-333](https://ascensuscollegesavings.atlassian.net/browse/QA-333)** — *`[V3] [Unite/Entity] Management - Create Regression GitLab pipeline for Unite Project in V3`* — Status **To Do**, **3** story points, Medium, Assignee **Swapnil Patil**, under parent theme **QA-3** (*Update regression test plan for Unite, Universal*). **[QA-635](https://ascensuscollegesavings.atlassian.net/browse/QA-635)** — *`[V3][IDP Login] Port IDP login coverage from Universal Enrollment module into Unite V3`* — **Validation**, **2** SP — adjacent Unite V3 login work. |
| **`Platform-support-jira-export.csv`** | **QA-333** row confirms title **V3 Unite/Entity Management - Create Regression GitLab pipeline for Unite Project in V3**, labels **QA-Board-View**, **Regression**, **WebRegAutomation**, parent **QA-3**. Regression narrative: *Each module (Login, Web Reg, Enrollment, Contributions, Withdrawals, Profile/Acct Maint., Balance, **Entity if present**)* is reviewed in TestNG/qTest results. **QA-98** (*Expand Web Registration Flows*): plans **NHB, ILB (Entity)** for registration coverage. **QA-97** (*Enhance Legacy Login Feature Testing*): **Entity Login: NHB, ILB**; negative: **missing profile link**, **incorrect entity mapping**. |
| **`README.md`** | Notes `jira-export.csv` as optional fresh export — use to reconcile keys after Epic is filed. |
| **`Env-Pipeline-Project/`** | No additional Entity/Unite strings found in meeting artifacts under this folder. |

**Program context (from exports):** QA Automation project description references [Confluence — QA Automation hub](https://confluence.ascensus.com/pages/viewpage.action?pageId=315559619) (*pageId=315559619*).

---

## 2. Epic metadata (fill after JIRA create)

| Field | Value |
|-------|--------|
| **Epic name (short)** | `V3 Entity Dashboard & Management — Automation` |
| **Epic key** | `QA-[CREATE_EPIC_PASTE_HERE]` |
| **Parent / program link** | Relate to **QA-3** — *Update regression test plan for Unite, Universal* (per export: QA-333 already rolls under this theme). |
| **Suggested labels** | `@Entity`, `@Unite`, `@V3`, `Regression`, `QA-Board-View`, `PrimeV3` *(adjust to team convention)* |
| **Owners** | QA Automation (functional lead per project: Swapnil Patil; JIRA admin: Timothy Kaufman — per export boilerplate). |

---

## 3. JIRA-ready Epic description (paste into Epic body)

### Summary / Epic Name

**V3 Entity Dashboard & Entity Management — automation, pipelines, regression & smoke**

### Problem statement

Entity-specific experiences (**Entity dashboard**, **entity management** flows, **entity-backed plans** such as **NHB / ILB**) are called out in historical stories (**QA-97**, **QA-98**) and in regression **module checklists** (**“Entity if present”**). **Unite V3** delivery needs the same **trusted CI signal** as other modules, but **QA-333** (*GitLab regression pipeline for Unite / Entity management in V3*) remains **To Do**. Without a bounded Epic, **test design**, **implementation**, **scheduled execution**, and **suite placement** (full regression vs smoke) risk being fragmented across sprints.

### Goals

1. **Design** a coherent **Entity** test strategy for V3: dashboard, management actions, navigation, permissions, and plan-specific rules for **entity** traunches.  
2. **Implement** automated scenarios in the **Unite V3** codebase with framework-aligned patterns (reuse IDP/UE patterns where **[QA-635](https://ascensuscollegesavings.atlassian.net/browse/QA-635)** applies).  
3. **Execute** in **GitLab CI** via a **V3 Unite regression pipeline** (deliverable of **QA-333**).  
4. **Classify** scenarios into **full regression** vs **smoke** (minimal path for post-deploy / nightly gate).  
5. **Prove** coverage in **TestNG / reporting** with **Entity** visible as its own slice in the same spirit as the *“Entity if present”* review line in platform narratives.

### In scope

- **Entity dashboard** — load, widgets/summary (as per product spec), empty vs populated states, error handling.  
- **Entity management** — CRUD or workflow steps **as delivered by product** (users/roles, entities, relationships — *refine titles when AHA/ODY links available*).  
- **Authentication & entry** — **Entity login** patterns for **NHB, ILB** (from **QA-97**); alignment with **IDP login ported to Unite V3** (**QA-635**).  
- **Web registration** — **Entity** plan registration paths (**QA-98**: NHB, ILB).  
- **Negative / edge** — **Missing profile link**, **incorrect entity mapping** (from **QA-97** acceptance themes).  
- **CI/CD** — **Regression GitLab pipeline** for Unite V3 (**QA-333**): stages, artifacts, env parameters, tagging of Entity jobs.  
- **Suite hygiene** — tags, groups, or TestNG suites so **smoke** can run subset without duplicating maintenance.

### Out of scope (unless product pulls in)

- Performance/load testing of Entity APIs.  
- Non-V3 legacy-only flows **unless** required for parity comparison (then document as *spike* story).  
- Product defects without automation frame — file bugs separately; Epic tracks **testability and coverage**.

### Success criteria (Epic DoD)

- [ ] **Epic** linked under **QA-3** (or agreed program parent).  
- [ ] **QA-333** **Done**: V3 Unite project runs **scheduled regression** in GitLab with Entity scenarios included or explicitly flagged “N/A” with sign-off.  
- [ ] **Test case matrix** (Section 6) mapped to **automated** or **deferred** with rationale.  
- [ ] **Smoke list** ≤ agreed time budget (define e.g. &lt; 15–20 min wall-clock or team SLA) documented in Confluence or README in repo.  
- [ ] **Regression report** checklist includes **Entity** (not only “if present” ad hoc).  
- [ ] **Cross-story**: **QA-635** either **Done** and consumed by Entity login paths, or **linked** with explicit dependency note.

---

## 4. Phased delivery (suggested)

| Phase | Focus | Typical outputs |
|-------|--------|-----------------|
| **P0 — Foundations** | Pipeline (**QA-333**), branch strategy, env secrets, baseline green without Entity | Pipeline YAML, first green job, doc link |
| **P1 — Entity smoke** | Minimum **Entity login** + **dashboard load** + one **management** happy path per agreed plan (e.g. **NHB** or **ILB**) | Smoke tag, CI job optional `SMOKE_ENTITY` |
| **P2 — Entity regression** | Full matrix Section 6 — negative mapping, registration overlap with **QA-98**, profile link | Regression suite, qTest/TestNG mapping |
| **P3 — Hardening** | Flake fixes, data strategy, DB assertions if required | Stability label, dashboards |

---

## 5. Child stories (existing + proposed)

**Link these under the new Epic in JIRA:**

| Key | Summary | Role in Epic |
|-----|---------|----------------|
| **[QA-333](https://ascensuscollegesavings.atlassian.net/browse/QA-333)** | `[V3] [Unite/Entity] Management - Create Regression GitLab pipeline for Unite Project in V3` | **Core** — CI enablement |
| **[QA-635](https://ascensuscollegesavings.atlassian.net/browse/QA-635)** | `[V3][IDP Login] Port IDP login coverage from Universal Enrollment module into Unite V3` | **Dependency / shared login** for Unite V3 |
| **QA-TBD** | *Entity dashboard — automated smoke (load + navigation)* | New story |
| **QA-TBD** | *Entity management — happy path workflow (per product spec)* | New story |
| **QA-TBD** | *Entity negative — profile link + mapping errors (QA-97 themes)* | New story |
| **QA-TBD** | *Entity web reg — NHB/ILB alignment with QA-98 patterns in V3* | New story *(if V3 differs from legacy)* |

---

## 6. Test case catalog (backlog for automation)

Use this table to spawn **BDD features**, **TestNG classes**, or **qTest** cases. Mark **Smoke** vs **Regression** when grooming.

### 6.1 Entity dashboard

| ID | Area | Scenario (high level) | Type | Notes from data |
|----|------|------------------------|------|-----------------|
| ED-01 | Access | Authenticated **entity** user reaches **Entity dashboard** landing URL | Smoke | Entry after **Entity login** |
| ED-02 | Access | Unauthorized / wrong role cannot open dashboard (403 or redirect) | Regression | Security |
| ED-03 | UI | Dashboard loads primary sections without JS fatal / 500 | Smoke | Align with “module present” checklist |
| ED-04 | Data | Populated entity shows summary metrics / lists per **product spec** | Regression | May need DB/API validation |
| ED-05 | Empty | New or edge entity shows guided empty state | Regression | UX |
| ED-06 | Resilience | Timeout / partial API failure — user-visible error, retry or support path | Regression | Optional P3 |

### 6.2 Entity management (workflows)

| ID | Area | Scenario | Type | Notes |
|----|------|----------|------|------|
| EM-01 | Lifecycle | Create or register **entity** (if applicable) — happy path | Smoke | Tie to product **E2E** |
| EM-02 | Lifecycle | Edit entity attributes (name, contact, metadata per spec) | Regression | |
| EM-03 | Lifecycle | Deactivate / archive (if applicable) | Regression | |
| EM-04 | Users | Add / invite / remove entity user | Regression | RBAC |
| EM-05 | Users | Role change reflects in UI within session / refresh | Regression | |
| EM-06 | Beneficiary / link | Actions that tie entity to **beneficiary/account** per domain rules | Regression | Cross-check UE if shared |

### 6.3 Authentication & plans (from QA-97 / QA-98)

| ID | Area | Scenario | Type | Notes |
|----|------|----------|------|------|
| AU-01 | Entity login | **NHB** — entity login happy path | Smoke | **QA-97** |
| AU-02 | Entity login | **ILB** — entity login happy path | Smoke | **QA-97** |
| AU-03 | Negative | Invalid credentials | Regression | |
| AU-04 | Negative | **Missing profile link** after login | Regression | **QA-97** |
| AU-05 | Negative | **Incorrect entity mapping** (wrong entity context) | Regression | **QA-97** |
| AU-06 | Web reg | **NHB** registration flow (subset of **QA-98**) | Regression | **QA-98** |
| AU-07 | Web reg | **ILB** registration flow | Regression | **QA-98** |

### 6.4 Integration with Unite / Universal themes

| ID | Area | Scenario | Type | Notes |
|----|------|----------|------|------|
| UN-01 | Port parity | Same critical path as UE **IDP** where shared — no duplicate brittle code | Regression | **QA-635** |
| UN-02 | Pipeline | Entity-tagged tests run in **Unite V3** GitLab pipeline | Smoke | **QA-333** |

### 6.5 Reporting & governance

| ID | Area | Scenario | Type | Notes |
|----|------|----------|------|------|
| RP-01 | Checklist | Nightly/regression report explicitly lists **Entity** pass/fail | Regression | Platform narrative: *Entity if present* |
| RP-02 | Traceability | Each automated case links to Epic + product story | Both | |

---

## 7. Risks & dependencies

| Risk | Mitigation |
|------|------------|
| Product **Entity dashboard** scope still moving | Timebox **P1 smoke** to login + shell only; gate **EM-*** on SME sign-off |
| **Test data** for NHB/ILB fragile after refresh | Document refresh playbook; parameterized accounts |
| **QA-333** blocked on infra | Escalate with DevOps; parallel **local** suite until CI unblocked |
| Overlap with **QA-635** | Daily sync; avoid duplicate login code — shared page objects |

---

## 8. Acceptance criteria (Epic-level)

1. Stakeholders can open **one JIRA Epic** and see **all** Entity automation scope, **phased** plan, and **test IDs** (Section 6).  
2. **GitLab** shows a **V3 Unite** job that includes **Entity** scenarios or documents exclusion with approval.  
3. **Smoke** set is **named**, **fast**, and **optional** on MR if team policy allows.  
4. **Regression** includes **Entity** alongside Login, Web Reg, Enrollment, … per existing **module review** convention.

---

## 9. Changelog

| Date | Author | Change |
|------|--------|--------|
| 2026-05-08 | KB / QA Automation | Initial Epic draft from `AMSQUAD Sprint 26.04 - 26.05.csv` + `Platform-support-jira-export.csv` |

---

**Next step:** Create the Epic in JIRA → paste description from **§3** → link **QA-333**, **QA-635** → split **§5** stories → map **§6** IDs to qTest/GitLab. Update **§2** Epic key when filed.
