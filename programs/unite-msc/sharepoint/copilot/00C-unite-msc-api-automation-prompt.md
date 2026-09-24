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

## Who should use this hub
| Audience | Use this hub to |
|---|---|
| New engineer or receiving team | Complete KT, get access, run one safe suite |
| Day-to-day support | Run a suite, read a report, classify a failure |
| Module owner | Confirm Mobile 1, Mobile 2, or Enrollment scope and exclusions |
| Lead or reviewer | Find sign-off, coverage, and the L1-L4 completion bar |

## Current scope
| Module | Current documented scope | Primary plants | Child page |
|---|---|---|---|
| Mobile 1 | 26 coded endpoint operations | OK Direct; NM Direct on applicable auth/IDP flows | 05 Mobile 1 Automation |
| Mobile 2 | 24 in-scope business APIs; harness excluded | OK Direct, New York; selected NM Direct smoke | 06 Mobile 2 Automation |
| Enrollment | 25 automated of 28 catalog rows; 3 partner APIs deferred | OK Direct, New York | 07 Enrollment Automation |

Enrollment deferred items are partner submit, Upromise account, and OAuth token. They are exclusions, not missing coding in the signed-off MSC happy path.

## Environments
| Environment | Use | Caveat |
|---|---|---|
| Stage1 | Primary regression and sign-off evidence | Refresh can invalidate users and data |
| QC4 | Integration and environment proof | Stability, IDP/reverse proxy, and refresh dependencies can block runs |
| Localhost examples | Development templates only | Not CI evidence |

Caution callout: QC4 is not a substitute for Stage1 sign-off evidence. After any database refresh, use page 10 before classifying a product defect.

## Validation and sign-off bar
| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Optional enhancement; not the completion gate |

Leadership directed that L5 SQL field reconciliation is not the completion gate. Do not claim L5 is implemented.

Republish the page when finished.
