# Persistent Bi-Weekly Leadership Update – Template

**Use:** Every alternate week when Persistent meets with the client.  
**Input:** Brief update on what happened and what’s happening with the QA Automation team.  
**Output:** (1) Detailed Confluence page (with top-of-page block, velocity & key metrics, and main sections), (2) PSL page summary ("5. Automation Team" block), (3) **Key Summary** – standalone copy-paste for MAIN – Persistent Updates left column, emails, or slides.

**Prompt to run:** See `00_SYSTEM/PROMPTS.md` → **F2) "Persistent Bi-Weekly Leadership Update"**. Copy that prompt, paste your brief update at the end, and run in Cursor to generate all deliverables.

**Reference example:** `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/15. QA Automation Program – Leadership Working Update (As of 02182026).md`  
**Key summary example:** `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/MyUpdates/QA_Automation_Key_Summary_02182026.md`  
**PSL format reference:** `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/MAIN - PSL - Persistent Updates.pdf`

---

## Part 1: Detailed Confluence Page Structure

Fill or replace `[PLACEHOLDER]` sections; keep section headings. **Include the top-of-page block and the "QA Automation Team – Velocity & Key Metrics" section** so the page aligns with MAIN – Persistent Updates (left column = key activities/next steps; right column = velocity chart).

### 1a. Top-of-Page Block (MAIN – Persistent Updates)

Add at the very top so the page can be embedded as Section 5 of the main doc:

- **Document:** MAIN – Persistent Updates (As of [MM-DD-YYYY])
- **Section:** 5. Automation Team – Detailed Working Update
- **Period Covered / Purpose / Owner** (as below)

### 1b. Velocity & Key Metrics Section (Before §1 Executive Context)

Add a section **"QA Automation Team – Velocity & Key Metrics (As of [MMDDYYYY])"** containing:

- **Team Structure & Focus** – Table: Name | Role | Primary Focus | Key Contribution (this/last period). Populate from input (Project Lead, Tech Lead API, Perf Eng, Sr SDET V2, Sr SDET V3; test cases added, bugs found, docs, release support).
- **Key Summary** – 5–6 bullets: V2 (TCs added, bugs, flaky, release support), V3 (TCs, IDP/UE, release support), API (TCs, SME, QTest), Performance (TCs, platform-independent, nightly prep), Cross-cutting (release, nightly, bug docs), **Total test-case velocity** (e.g. 190+).
- **Key Metrics table** – Test cases added by stream, bugs found, regression suite size (V2/V3), release support, nightly & bug docs, pipeline readiness/blocker.
- **Velocity Chart – Test Cases Added by Stream** – Table (Stream | Test Cases Added | Owner) for bar chart; optional Mermaid barChart snippet.
- **Velocity Chart – Cumulative Regression Growth** – Table (Month | V2 Regression TCs | V3 Regression TCs) for horizontal stacked bar or line chart (Oct–current month). Replace with actuals when JIRA/dashboard available.
- **Observations** – Velocity, quality (bugs, nightly), delivery (release, nightly), blocker (pipeline). Match tone of other scrum teams (e.g. "On time delivery, 0 escape defects").

### 1c. Main Confluence Page (Sections 1–10)

```markdown
# QA Automation Program – Leadership Working Update (As of [MMDDYYYY])

**Document:** MAIN – Persistent Updates (As of [MM-DD-YYYY])
**Section:** 5. Automation Team – Detailed Working Update
**Period Covered:** [Start Date] – [End Date]
**Purpose:** Detailed working update since last leadership share-out ([Last Share Date])
**Owner:** QA Automation Team

---

## QA Automation Team – Velocity & Key Metrics (As of [MMDDYYYY])

[Team Structure table | Key Summary bullets | Key Metrics table | Velocity chart table(s) + optional Mermaid | Observations]

---

## 1. Executive Context (What Changed Since [Last Date])

[2–4 bullet points: high-level shifts this period – V2/V3, API/Perf, platform support, risks]

---

## 2. Prime Version 2 – [Theme e.g. Closure / Stabilization]

### Progress Since [Last Date]
- [Bullet: key achievement]
- [Bullet: new coverage / fixes]
- [Bullet: flakiness / docs]
### Execution Model
- [Offshore ownership, nightly regression, readiness – 1–2 lines]

---

## 3. Prime Version 3 – [Theme e.g. IDP, Universal Enrollment]

### Enhancements Since [Last Date]
- [IDP / UE / CSR / member update – bullets]
- [Flakiness / in-progress work]
### Coverage Summary
- [1–2 lines: primary surface, stability]

---

## 4. API Automation & Metadata Integration

### Current State
- [Auth server, metadata, CMS, Postman/Swagger – bullets]
### Next Focus
- [1–2 bullets]

---

## 5. Performance Testing

### Progress
- [IDP analysis, scripts, mid-Feb or similar – bullets]
### Next Focus
- [Repeatable suite, cadence – 1 bullet]

---

## 6. Cross-Team & Platform Support

[Bullets: SSS, Apache, Stage 5 CAT, dependency sync – what’s done, what’s pending]

---

## 7. Key Risk: Unplanned Support Load (if applicable)

### What’s Changing
[Default validation layer – bullets]
### Risk
[Sustain impact – bullets]
### Leadership Alignment Needed
[1–2 sentences]

---

## 8. Leadership Discussion Points (To Align On)

- [Support vs roadmap]
- [Intake expectations]
- [Capacity protection]
- [Environment readiness]
- [API/Performance timing – if needed]

---

## 9. Summary

[4–6 bullets: what the team did this period]
[1 sentence: program health + alignment need]

---

## 10. Detailed Reference Snapshot (One-Line Summary)

**QA Automation** [One sentence: transition/achievement + leadership call-out if needed]
```

---

## Part 2: PSL Page Summary Structure ("5. Automation Team")

Use this block on the **main PSL page** (MAIN - PSL - Persistent Updates). Keep structure; replace content.

```markdown
## 5. Automation Team

**Detailed Reference:** QA Automation Leadership Update – [MMDD]

**One-Line Summary**
[One sentence: what changed this cycle + leadership call-out if needed]

**Key Highlights**

- **Prime V2 – [Subtitle]:** [2–3 sentences: closure/stability, new coverage, flakiness, docs]
- **Prime V3 – IDP & Universal Enrollment [or theme]:** [2–3 sentences: IDP, UE, CSR, flakiness, in-progress]
- **Regression Growth & Stability:** [1–2 sentences: coverage, nightly, offshore]
- **Platform-Independent Automation Enablement:** [1–2 sentences: SSS, Stage 5 CAT, regions]
- **API & Performance Foundations:** [1–2 sentences: auth, metadata, CMS, performance baseline]
- **Critical Release & War-Room Support:** [1–2 sentences: default layer, urgent/valid, capacity]

**In Progress / Next Focus**

- **Prime V2:** [One line]
- **Prime V3:** [One line]
- **API Automation:** [One line]
- **Performance Testing:** [One line]

**Initiatives & Execution Highlights**

- **[Initiative 1 name]:** [1 sentence]
- **Offshore Ownership at Scale:** [1 sentence – keep or adapt]
- **[Initiative 2 name]:** [1 sentence]
- **[Initiative 3 name]:** [1 sentence]
- **Program Maturity:** [1 sentence – keep or adapt]

**Call-Out for Leadership**

[2–3 sentences: dependency, risk of unplanned support, need for intake alignment – decision point]
```

---

## Part 3: Key Summary (Standalone Copy-Paste)

Generate a **separate key summary** for the MAIN – Persistent Updates left column, emails, or slides. Save as:  
`10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/MyUpdates/QA_Automation_Key_Summary_[MMDDYYYY].md`

**Structure:**

```markdown
# QA Automation – Key Summary (Standalone Copy-Paste)
**As of:** [MMDDYYYY]  **Period:** [Start]–[End]

## Key Activities / Achievements
- **Prime V2:** [Closure of flaky cases; new coverage areas; TCs added; bugs found; suite size; owner/release support.]
- **Prime V3:** [IDP & UE expansion; TCs added; coverage areas; flaky fixes; suite size; owner/release support.]
- **API & Performance Foundations:** [API: TCs, suites, SME, QTest, pipeline readiness. Performance: TCs, areas, platform-independent, nightly prep, owner/collaborators.]

## Next Steps
- **Prime V3:** [Pipeline enablement; regression expansion; IDP transaction workflows.]
- **API Automation:** [Pipeline direction; lightweight regression; CI/CD.]
- **Performance Testing:** [Repeatable suite; baseline to nightly; cadence.]

## One-Line Key Summary
[One sentence: V2/V3/API/Perf highlights + velocity (e.g. 190+ TCs) + blocker if any.]
```

Use **only** facts from the brief update; no invented metrics. Match the format of other scrum teams’ left-column blocks (achievements + next steps).

---

## Checklist Before Publishing

- [ ] Period dates and “since last” date correct
- [ ] All [PLACEHOLDER] and [MMDD] replaced
- [ ] **Top-of-page block** present (Document, Section, Period, Purpose, Owner)
- [ ] **Velocity & Key Metrics** section present (team structure, key summary, key metrics table, velocity chart table(s), observations)
- [ ] Confluence page saved (e.g. `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/NN. QA Automation Program – Leadership Working Update (As of MMDDYYYY).md`)
- [ ] **Key Summary** saved (e.g. `MyUpdates/QA_Automation_Key_Summary_MMDDYYYY.md`)
- [ ] PSL block copy-pasted into MAIN - PSL - Persistent Updates page
- [ ] One-line summary and call-out consistent between Confluence, PSL, and Key Summary
