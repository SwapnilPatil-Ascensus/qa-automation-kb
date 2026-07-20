# Action Item Proposal — Rebuilt Assessment

**Date:** 2026-07-21  
**For:** Program leadership, DevOps, QA Automation

## Primary recommendation

Establish an automated Government Savings quality coverage register reconciling Jira scope, qTest inventory, repository implementation, and CI execution — with **separate metrics** for business automation, execution, CI integration, gates, and source-code coverage. Begin **read-only reporting** before expanding blocking gates.

## P0 — Before leadership quotes new numbers

| ID | Action | Owner | Evidence of done |
|----|--------|-------|------------------|
| P0-1 | Distribute rebuilt assessment + Review Findings DOCX | QA Lead | Email + shared path |
| P0-2 | Retire **100% M2** and **22% M1 verified** slides | QA + PMO | Updated decks |
| P0-3 | Align talking points to **88% M2 verified** / **3.7% M1 verified** | QA Lead | Signed talking-points doc |

## P1 — 0–30 days

| ID | Action | Owner |
|----|--------|-------|
| P1-1 | Mobile 2 GitLab nightly (QA-1405) | DevOps + QA |
| P1-2 | Mobile 2 sign-off rerun QC4 + Stage 1 @ `cee0de9` | QA Automation |
| P1-3 | Refresh endpoint matrix (`16-mobile2-coverage-matrix.md`) | QA Automation |
| P1-4 | Mobile 1 sprint — evidence for 5 implemented endpoints | QA Automation |
| P1-5 | Live-verify GitLab schedule cadence (V3 + metadataweb) | DevOps |
| P1-6 | Locate GHA workflow repository for audit record | DevOps (Chaitanya) |

## P2 — 30–90 days

| ID | Action | Owner |
|----|--------|-------|
| P2-1 | qTest/Jira read-only API credentials | IT Admin |
| P2-2 | Weekly coverage register (Python collector) | QA Automation |
| P2-3 | GHA module suite expansion aligned to Nexus | DevOps |
| P2-4 | ASTRO / COPACS scope decisions | Program + SME |
| P2-5 | V2 Jenkins job inventory | QA + Jenkins admin |

## Leadership support required

- DevOps priority for QA-1405  
- Mobile 2 sign-off path sponsorship  
- Mobile 1 sprint priority  
- Test-data/environment readiness (Stage 1 contribution)  
- Structured intake + CI ownership  
- qTest/Jira traceability cleanup  
- 30–40% BA/Scrum reporting capacity  
- Quarterly roadmap visibility  
