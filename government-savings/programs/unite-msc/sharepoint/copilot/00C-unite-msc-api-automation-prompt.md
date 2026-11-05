PART C of 4. Edit the existing SharePoint page "Unite MSC API Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## Start here
Render this set as a second Quick Links web part in tile or grid layout.

| I need to… | Open |
|---|---|
| Join or take over support | 01 KT and Onboarding |
| Understand components and ownership | 02 Architecture and Ownership |
| Get access and configure an environment | 03 Access, Setup and Environments |
| Run a suite today | 04 Daily Run Playbook |
| Check Mobile 1 | 05 Mobile 1 Automation |
| Check Mobile 2 | 06 Mobile 2 Automation |
| Check Enrollment | 07 Enrollment Automation |
| Review coverage or sign-off | 08 Coverage, Traceability and Sign-off |
| Diagnose a failure | 09 Reporting and Troubleshooting |
| Prepare data after a refresh | 10 Test Data, DB Refresh and Security |
| Add a scenario safely | 11 Extend the Automation |

## Who should use this hub
| Audience | Use this hub to |
|---|---|
| New engineer or receiving team | Complete KT, get access, run one safe suite |
| Day-to-day support | Run a suite, read a report, classify a failure |
| Module owner | Confirm Mobile 1, Mobile 2, or Enrollment scope and exclusions |
| Lead or reviewer | Find sign-off, coverage, and the L1-L4 completion bar |

## Program accomplishment
| Measure | Result |
|---|---:|
| Catalog rows reviewed | 79 |
| Automated business operations | 75 |
| Overall catalog coverage | 94.9% |
| Mobile 1 | 26/26 = 100% |
| Mobile 2 | 24/25 = 96.0% |
| Enrollment | 25/28 = 89.3% |
| Legacy traceability rows improved/new | 69 of 83 |

The result is a canonical, multi-plan TestNG platform—not a one-time script conversion. It includes IDP flows, encrypted Enrollment, dynamic Oracle fixtures, safe destructive-suite separation, Bruno manual collections, endpoint registers, formal sign-off packs, and a reusable reporting portal.

## Current scope
| Module | Current documented scope | Primary plants | Child page |
|---|---|---|---|
| Mobile 1 | 26/26 endpoint operations | Current XML: OK Direct, New York, NM Direct | 05 Mobile 1 Automation |
| Mobile 2 | 24/25 business operations; harness excluded | Current XML: OK Direct, New York, NM Direct | 06 Mobile 2 Automation |
| Enrollment | 25/28 catalog rows; 3 partner APIs deferred | Current XML: OK Direct, New York, NM Direct | 07 Enrollment Automation |

Enrollment deferred items are partner submit, Upromise account, and OAuth token. They are exclusions, not missing coding in the signed-off MSC happy path.

## Environments
| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost examples | Development templates only | Not CI evidence |

Caution callout: QC4 is not a substitute for Stage1 sign-off evidence. After any database refresh, use page 10 before classifying a product defect.

Republish the page when finished.
