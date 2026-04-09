# ENVP automation alignment — Leadership · QA Leads · Tech Leads

**Date:** 9 Apr 2026  
**Duration:** 30 minutes  
**Type:** Kickoff + decision ownership (not a status readout)

**References:** [Aha ACS-5289](https://acscensus.aha.io/features/ACS-5289) · Jira Epic [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600) · KB drafts: `docs/jira-governance/upcoming-stories/Env-Pipeline_project/`

---

## 1. Purpose (why we are here)

- **Program:** Environment Pipeline (ENVP) needs **credible, maintainable automation** so promotion gates mean something — not ad hoc debate every release.
- **This quarter’s concrete wedge:** **Universal Enrollment (UE)** — package a **Stage 1 UI integration suite** (target **≤10 min**), wire **CI**, then **replicate the model** for other MFEs/services.
- **Why leadership + both lead types:** Gates touch **product risk** (who accepts flake vs real defects), **engineering** (build/deploy blocking), and **capacity** (grid, time budgets). Without named owners, execution stalls.

**Success for this 30 minutes:** Everyone leaves with **named owners**, **one agreed “definition of pass” direction**, and **3–5 written follow-ups** with due expectations — not full resolution of every open topic.

---

## 2. Kickoff framing (one sentence you can open with)

> “We’re kicking off ENVP automation alignment around Epic QA-600 and ACS-5289: we need the same clarity on **who decides**, **what blocks deploy**, and **what we can run in under ~10 minutes** for UE — then we’ll scale that playbook.”

---

## 3. Pointers — for live opinion, decisions, and notes

*Use this section during the meeting: tick decisions, fill names, capture dissent.*

### A. Scope and vocabulary

- [ ] **Smoke (3–5 min)** vs **integration (~10 min UE)** vs **nightly/full** — are these **different gates** or one bucket?
- [ ] **UI vs API:** What must UI prove that API cannot (wiring, auth, real MFE, schema in flow)?
- [ ] **“One UI scenario per URN/schema”** — sufficient for smoke or explicitly **not**?

### B. Ownership (RACI-style — fill in names)

| Topic | **Accountable** (decides) | **Responsible** (does) | **Consulted** | **Informed** |
|-------|---------------------------|------------------------|---------------|--------------|
| What goes in **Stage 1 UI smoke** | | | | |
| What goes in **UE integration suite** | | | | |
| **Pass/fail** / flake policy for gates | | | | |
| **Grid / parallelism** limits | | | | |
| **Test data / cleanup** strategy | | | | |
| **Confluence / taxonomy** (suite intent) | | | | |

### C. Collaboration commitments (yes/no + owner)

- [ ] Product / feature QA provides **cases + data** for UE suite — owner: _______
- [ ] Tech lead signs off **non-flaky bar** or **documented risk** if gate is soft — owner: _______
- [ ] Automation implements **suite + CI** — owner: _______
- [ ] Leadership **escalation path** when gate blocks deploy — owner: _______

### D. Limitations and reality checks

- [ ] **Grid capacity:** max parallel UI sessions; queue impact on duration — who confirms numbers? _______
- [ ] **Time ceiling:** 3–5 min smoke vs ≤10 min UE — both allowed? _______
- [ ] **Retries:** If test fails then passes on retry, does **build pass**? _______
- [ ] **Stage 1 stability:** known env noise — how do we separate flake from defect?

### E. Gaps in requirements (capture verbatim)

| Gap | Impact | Proposed next step | Owner |
|-----|--------|-------------------|-------|
| | | | |
| | | | |

### F. Resource asks (be explicit)

- [ ] **People:** FTE / hours per week for suite + CI + stabilization
- [ ] **Infra:** Grid slots, CI runner type, secrets/Vault if applicable
- [ ] **SME time:** Traunch rules, enrollment edge cases (e.g. foreign phone)
- [ ] **Tooling:** qTest / reporting / Confluence space

### G. Immediate decisions needed today (check when closed)

- [ ] **D1:** UE integration is **in scope this quarter** as first ENVP UI package — Y/N
- [ ] **D2:** **≤10 min** is the agreed **budget** for that UE suite (document variance if grid differs) — Y/N
- [ ] **D3:** **Flake policy** owner = QA Lead + Tech Lead joint — Y/N
- [ ] **D4:** **Confluence taxonomy page** will exist; owner + target date: _______
- [ ] **D5:** Next **30-min** follow-up date: _______

---

## 4. Agenda — 30 minutes (timed)

| Min | Block | Outcome |
|-----|--------|---------|
| 0–3 | Purpose + kickoff | Room aligned on “alignment + owners,” not deep technical debug |
| 3–10 | **Program + wedge** (ACS-5289 / QA-600, UE first) | Leadership nod on priority and sequencing |
| 10–18 | **UI vs API + gate types** | Clear vocabulary; who approves scope per gate |
| 18–25 | **Pass/fail, flake, grid, data** | Owner per area; explicit “we don’t know yet” list |
| 25–30 | **Actions + follow-up** | Names on 3–5 items; next meeting if needed |

---

## 5. Detailed script / talk track

*Read naturally; adjust names and examples to your org.*

### Opening (0–3 min)

“Thanks for making time — this is a **30-minute kickoff and alignment** for ENVP automation work tied to **ACS-5289** and Epic **QA-600**.

The **business goal** is deployment confidence: pipelines should only promote when we **mean** it. The **technical wedge** we’re executing first is **Universal Enrollment on Stage 1**: a **defined UI integration suite** we can run in about **ten minutes** in CI, with clear reporting.

What I need from this group today is **ownership** and **shared vocabulary** — smoke versus integration, UI versus API, and what **pass** means when UI is involved. I’m not asking us to solve every flake today; I’m asking **who decides** and **what we commit to** for the next few weeks.”

### Program context (3–10 min)

“Aha describes **team-owned** automation and **clear test intent** — UI versus service. The ENVP vision also includes broader CI/CD maturity; our **automation track** has to plug into that without pretending **UI integration** is the same as **unit tests**.

**First deliverable:** UE **Stage 1 integration** packaged in repo — TestNG suite, Maven profile, GitLab job, **artifact reports**, and **documented scenario intent**. We already have a **draft suite** and a **baseline run** around **nine and a half minutes** for thirty scenarios, but **stability** — for example a **foreign phone** enrollment path — still fails intermittently. That’s why we need **product and tech** alongside automation: some fixes are **test hardening**, some may be **real defects** or **env** issues.

**Ask to leadership:** Confirm UE is the right **first vertical** for this model, and that we’re allowed to treat **≤10 minute integration** as a **separate idea** from a stricter **3–5 minute smoke** bar we’ve also heard — or tell us to collapse them and we’ll rescope.”

### UI vs API + who decides scope (10–18 min)

“**API tests** catch contracts and services; **UI integration** catches **wiring**, **auth**, **front-end behavior**, and **end-user path** risks APIs don’t see. We can’t run **everything** in ten minutes, so **someone** must own **inclusion criteria**.

**Proposal:** **QA Lead** proposes scenario sets per gate; **Tech Lead** confirms **feasibility and stability bar**; **leadership** weighs **risk** if we ship with **narrower** UI coverage. If that split doesn’t work, tell us **who does decide** — we’ll document it.

**Concrete question:** Is **one UI scenario per URN or schema** enough for **smoke**, or do we need **more** for UE specifically? If we don’t know, that’s fine — I need an **owner** to **decide by** a named date.”

### Pass/fail, flake, grid, data (18–25 min)

“UI will **flake**. Pipelines want **binary** pass/fail. We’ve seen **retries** where a scenario **pass–fail–pass** and the **build still fails** — that’s confusing for everyone.

**We need a short policy:** Do **retries** clear a red build? When do we **quarantine** with **visible** risk acceptance? **Who can override** a blocking gate?

**Grid and parallelism** directly drive **duration and stability**. If we add more ENVP UI jobs, we need **capacity numbers** from the owners of the grid — not guesses.

**Test data and cleanup:** Nick raised that **pipelines don’t really have a cleanup story** today. For enrollments, we need either **idempotent data**, **isolation**, or a **cleanup** path — **someone** must own **discovery**; automation can implement once **rules** exist.

**Asks:** Name **one owner each** for **flake policy**, **grid limits**, and **data strategy** — even if the answer is ‘spike first.’”

### Close (25–30 min)

“To close: I’ll circulate **action items** with **one owner** and **target week** for each. **Artifacts:** we’ll add a **Confluence** page mapping **suite type**, **job**, **UI vs API**, and **time budget** so ACS-5289’s **clarity of intent** is real.

**Confirm:** next **check-in** on **\[date\]** — **15 minutes** on **progress** and **15** on **blockers** — or whatever the group prefers.

Thanks — I’ll send notes same day.”

---

## 6. Pre-filled context you can cite if asked (facts, not opinions)

- **Epic / Aha:** QA-600, ACS-5289 — ENVP automation and deployment gates.
- **UE integration draft:** Multi-traunch Stage 1 tests tagged `@integration` and `@intrun`; parallel execution in TestNG (draft `thread-count="4"`).
- **Observed duration:** ~**9m 28s** Maven / ~**9.2 min** suite for **30** scenarios (baseline; environment-dependent).
- **Known pain:** **Foreign phone** scenario — **30s** wait timeout on `#firstName`; intermittent under parallel runs.
- **Open from prior discussions:** **3–5 min** smoke expectation vs **parallel UI limits** (~10–15 typical, up to ~30 if grid is ideal).

---

## 7. Notes back page (empty — copy to Confluence or email after)

**Attendees:**

**Decisions:**

**Action items:**

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Parking lot / next meeting:**

---

*End of document.*
