# Team contribution summary — Unite MSC (2026-07-17)

**Purpose:** Leadership visibility — not individual performance ranking.  
**Evidence window:** Primarily Sprint 26.10–26.11; git log on `api-test-automation` where available.  
**Gap:** GitLab MR export not run this session — several items marked “commit evidence; MR verification pending.”

---

## Swapnil Patil

| | |
|--|--|
| **Primary focus** | Program architecture, Mobile 2 master suite, dynamic auth SQL, audit/sign-off packs, KB leadership reporting |
| **Completed** | Master integration/regression suite wiring (`835757a`); dynamic auth test data on `main` (`9655ff7`); Mobile 2 Dashboard GHA vertical slice (`bda1af5`); stackup/contribution suite enhancements (`9500947`); local-mobile-api-audit + sign-off docs; DevOps integration pipeline guide (`15-devops-...`) |
| **In progress** | Sign-off evidence refresh; contribution dynamic fixture (KB SQL); leadership reporting module; sprint coordination |
| **Evidence** | `git log` — Swapnil Patil; `project-documents/local-mobile-api-audit/*` |

---

## Dinesh Kumar

| | |
|--|--|
| **Primary focus** | Mobile 2 dashboard, plans, content, ugift, YTD |
| **Completed** | Mobile plans GET + GET-by-id (`ee87536` — merged MR QA-1069); Ugift GET/PATCH (`8ba7cda` QA-1066/1218); Content (`6d041c3` QA-1061); YTD summary on dashboard (`6735159` QA-1071, 2026-07-16) |
| **In progress** | YTD master-suite verification; any open MRs for dashboard module |
| **Evidence** | `git log` — Dinesh Kumar; Jira refs in commit messages |

---

## Venkatesh Mallela

| | |
|--|--|
| **Primary focus** | Mobile 2 contribution, balance trend, performance, stackup |
| **Completed** | Contribution module baseline (`6252fe7`); POST/PUT (`394af49`); DELETE (`269fad5` QA-1365); Balance trend, stackup, mobile performance (`b6cc154`) |
| **In progress** | Contribution Stage 1 stability (test-data dependency) |
| **Evidence** | `git log` — Venkatesh Mallela |

---

## Sunil Godiyal

| | |
|--|--|
| **Primary focus** | Mobile 2 banks, stackup, transaction history, investments |
| **Completed** | Banks GET/DELETE baseline (`7ccaf46` QA-1310 — sign-off anchor); Banks POST (`bfba1c7`); Stackup (`6dffa9a` QA-1067); Transaction history (`cabc7eb` QA-1068); Investments (`327fc23` — merged MR QA-1070); Banks GET-by-id (`a032ec6` QA-1386, 2026-07-15) |
| **In progress** | Banks module regression stability; sign-off gap closure verification |
| **Evidence** | `git log` — Sunil Godiyal |

---

## Priti Choudhary

| | |
|--|--|
| **Primary focus** | Unite MSC + Universal Platform performance regression |
| **Completed** | Jenkins `AGSUP_UNITE_MSC_ENDURANCE` + non-IDP login→Dashboard YAML deployed (**QA-1229**, Done 2026-07-02); load-server script deployment |
| **In progress** | IDP MSC login performance (**QA-1228**); test-data setup via automation framework (**QA-1230** refinement); expanding perf to Dashboard, Contribution, Banks, Mobile 1 flows |
| **Evidence** | `unite-msc-performance-testing-tracker.md` §8–9; **no commits** in `api-test-automation` (perf repo separate) |

**Kudos note:** Ramped quickly in complex authentication/performance area with limited initial domain context.

---

## Sunil Godiyal vs program roles

*Note: Two “Sunil” contexts — Sunil Godiyal = MSC API modules above.*

---

## Chaitanya (DevOps — referenced, not core team row)

| | |
|--|--|
| **Primary focus** | GitHub Actions pipeline, Nexus consume/run |
| **Completed** | Mobile 2 Dashboard integration vertical slice validated in GHA; env variable / access fixes |
| **In progress** | Expand to full Mobile 2 module integration suites |
| **Evidence** | Business context + `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md`; **TBD** — pipeline run URL |

---

## GitLab data required (if deeper attribution needed)

- [ ] MR list filtered by assignee (Sprint 26.11)
- [ ] Jira sprint board export (AMSQUAD 26.11)
- [ ] qTest execution summary for V2/V3 (UI track)

See `metrics-verification-checklist.md`.
