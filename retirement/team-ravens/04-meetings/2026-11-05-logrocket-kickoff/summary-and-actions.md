# LogRocket kickoff — summary and actions

**Date:** 2026-11-05  
**Attendees:** Aashay Bhargava, Emanuel (Ema) Pedraza, Swapnil Patil  
**Full transcript:** [transcript.md](transcript.md)

## What LogRocket is doing for Team Ravens

| Topic | Summary |
|-------|---------|
| Scope | LogRocket is enabled for Unqork **DEV and QA**. Every user session in Unqork is reported and recorded. |
| Retention | Recordings are kept for roughly **30 days** before they are posted to the LogRocket app for review. |
| Code base | Unqork flows share one common code base. Testing one flow is representative of others. |
| Goal | Measure experience in the SBR DOE: time on task, drop-offs, issues. Ticket context is in [access-request-justification.md](../../01-logrocket/access-request-justification.md). |

## First-day plan (agreed on the call)

1. Understand how the LogRocket recordings and sessions map to screens.
2. Play with the **QA links** that Aashay shared. Nothing is harmful to change there; the goal is to see which screens are captured and which options exist.
3. Pick **random** flows on different days, not only one, because the common code path should behave the same.
4. Later: automate or script repeated checks across several flows once the business flow is clear.
5. Aashay will follow with four more sessions like this one.

## Actions

| # | Owner | Action | Status |
|---|-------|--------|--------|
| 1 | Swapnil | Submit LogRocket access request (use justification file) | Open |
| 2 | Swapnil | Explore QA Unqork links and note screen → LogRocket recording mapping | Open |
| 3 | Swapnil | Confirm with Ema who approves tool access | Open |
| 4 | Aashay | Four follow-up sessions | Planned |
| 5 | Team | Confirm DOM and network sanitization for SBR before PRO use | Open |

## Open questions

- Who approves DEV/QA vs PRO LogRocket access for Team Ravens?
- Are the four follow-up sessions scheduled?
- Which LogRocket custom events will we agree on for drop-off and time-on-task?
