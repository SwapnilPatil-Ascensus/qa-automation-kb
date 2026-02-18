✅ MASTER CURSOR PROMPT
(Save as: /knowledge-base/prompts/bi_weekly_leadership_update_prompt.md)
CONTEXT
You are generating a Bi-Weekly QA Automation Leadership Update.
This update is for:
Rajiv Akhter
Henry Dittmer
Senior stakeholders
The output must generate:
Confluence Leadership Page (using existing template structure)
PSL Update Summary (concise)
Executive Email Summary (short, direct)
Leadership Decision Section (clear and actionable)
Tone:
Executive
Outcome-focused
No fluff
No repetition
Clear risks and clear asks
Structured
Confident but not aggressive
CURRENT PROGRAM STATUS INPUT
Use the following updates as the source of truth.
PRIME V2 – CURRENT STATUS
V2 used heavily for release testing.
Added edge case coverage (e.g., subsequent weekly requirements).
Flaky cases resolved.
All 7 core modules closed.
Documentation and sign-off artifacts completed.
Offshore owns nightly regression, RCA, release readiness.
Regression suite expanded across environments:
Previously Stage1 only
Now expanding to CAT + QC regions
Multi-environment support in progress
C5 moved to CAT; lighter CSR-only regression suite planned.
Migration support:
Legacy → IDP transitions supported (KSD, NYD).
Test cases moved from legacy to V3 IDP when required.
Gap analysis ongoing for:
Reversal transfers
Exchanges
Funds-related flows (recent release gaps)
Goal:
Multi-environment adaptability
Maintain release readiness
Identify high-demand module gaps
PRIME V3 – CURRENT STATUS
Added test cases for:
Web registration
CSR account maintenance
Profile updates
IDP login (positive, negative, forgot password, links)
IDP coverage stable; minimal flaky locator issue under investigation.
UE coverage significantly expanded.
Unite V3 coverage growing.
Working with Dom on pipeline enablement.
Entity planned for later nightly onboarding.
Next planned expansion:
IDP transaction flows (member side)
API AUTOMATION – CURRENT STATUS
Auth + Metadata API suites created.
Running in QC4.
Environment dependency issue:
Data-centric validation prevents direct Stage1 portability.
Strategy in progress to make API tests environment-independent.
SME collaboration completed.
Ready for regression onboarding once pipeline finalized.
PERFORMANCE TESTING – CURRENT STATUS
Ownership under QA.
Auth flows stabilized.
Priti working on:
Enrollment
Withdrawal
Account creation
Login performance
Blazemeter dashboard being configured.
Manual test case documentation in progress.
Plan:
Add baseline performance cases to nightly pipeline
Expand incrementally
CROSS-TEAM SUPPORT
Stage 5 → CAT support
Docker automation integration validation
Scrum-of-Scrum pipeline coordination
Release failure investigations
Bug identification and resolution
Ad-hoc team support ongoing
REQUIRED OUTPUT FORMAT
Generate the following sections.
1️⃣ CONFLUENCE PAGE (Leadership View)
Structure:
Executive Summary
5–7 concise bullets
What improved
What is stable
What is blocked
Where leadership matters
Prime v2
Status
Improvements
Environment expansion
Gaps being evaluated
Risk assessment
Prime v3
Growth summary
Technical constraints (Shadow DOM / refactor)
Stability
Expansion roadmap
API Automation
Readiness
Environment limitation
Pipeline dependency
Performance Testing
Stabilization progress
Dashboard initiative
Baseline creation
Cross-Team Support
Support areas
Capacity implication
Risks & Constraints
Pipeline dependency
Environment coupling (API)
Growing regression volume
Capacity pressure
Leadership Decisions Required
(Explicit, numbered)
Migration ownership model
Prime v3 charter scope
Pipeline finalization
Capacity support (BA / admin)
Intake enforcement
Next 2–4 Week Outlook
What will be added
What will be stabilized
What depends on leadership decision
2️⃣ PSL SUMMARY (Concise)
Format:
8–10 bullets
No paragraphs
Director-readable in < 60 seconds
3️⃣ EXECUTIVE EMAIL SUMMARY
Short.
One paragraph summary.
Then numbered leadership asks.
Then “What’s coming next.”
No fluff.
STYLE RULES
No motivational language.
No repetition.
No internal team-level details.
No deep technical explanation.
Do not exceed necessary length.
Highlight ownership clearly.
Make risks visible but controlled.
Frame decisions as enablers.
IMPORTANT
Assume prior leadership email already referenced:
Migration accountability
Prime v3 scope decision
Pipeline direction (GitLab vs GitHub)
BA/Admin capacity
Intake discipline enforcement
Ensure alignment with those themes.