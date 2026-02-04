# Persistent Bi-Weekly Leadership Update – Template

**Use:** Every alternate week when Persistent meets with the client.  
**Input:** Brief update on what happened and what’s happening with the QA Automation team.  
**Output:** (1) Detailed Confluence page, (2) PSL page summary ("5. Automation Team" block).

**Prompt to run:** See `00_SYSTEM/PROMPTS.md` → **F2) "Persistent Bi-Weekly Leadership Update"**. Copy that prompt, paste your brief update at the end, and run in Cursor to generate both deliverables.

**Reference example:** `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/14. QA Automation Program – Leadership Working Update (As of 02042026).md`  
**PSL format reference:** `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/MAIN - PSL - Persistent Updates.pdf`

---

## Part 1: Detailed Confluence Page Structure

Fill or replace `[PLACEHOLDER]` sections; keep section headings.

```markdown
# QA Automation Program – Leadership Working Update (As of [MMDDYYYY])

**Period Covered:** [Start Date] – [End Date]
**Purpose:** Detailed working update since last leadership share-out ([Last Share Date])
**Owner:** QA Automation Team

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

## Checklist Before Publishing

- [ ] Period dates and “since last” date correct
- [ ] All [PLACEHOLDER] and [MMDD] replaced
- [ ] Confluence page saved (e.g. `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/NN. QA Automation Program – Leadership Working Update (As of MMDDYYYY).md`)
- [ ] PSL block copy-pasted into MAIN - PSL - Persistent Updates page
- [ ] One-line summary and call-out consistent between Confluence and PSL
