PART A of 3. Create a polished SharePoint Site Page titled "08 Coverage, Traceability and Sign-off".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 07 Enrollment Automation | Next: 09 Reporting and Troubleshooting

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 08 Coverage, Traceability and Sign-off
Purpose: Executive coverage story and reviewer drill-down: what was automated, how much improved over legacy, where every endpoint maps, and what COMPLETE means.

## 1. Coverage at a glance
| Module | Catalog | Automated business operations | Coverage | Sign-off |
|---|---:|---:|---:|---|
| Mobile 1 | 26 | 26 | 100% | COMPLETE |
| Mobile 2 | 25 | 24 | 96.0% | COMPLETE; one harness excluded |
| Enrollment | 28 | 25 | 89.3% | COMPLETE for MSC scope; 3 partner APIs deferred |
| Total | 79 | 75 | 94.9% | L1-L4 completion boundary |

This is 75 canonical business API operations across Mobile 1, Mobile 2, and Enrollment—not merely converted scripts. The work adds multi-plan suites, SQL-driven data, IDP paths, mobile encryption, subsequent enrollment, lean assertions, and reusable reporting.

## 2. Legacy-to-canonical scorecard
| Delta in the 83-row traceability matrix | Rows |
|---|---:|
| Improved | 47 |
| Newly added | 22 |
| Unchanged | 6 |
| Explicitly excluded | 6 |
| Missing/backlog | 2 |

69 of 83 traced rows are improved or newly added. Improvements include IDP token flows absent from legacy Cucumber, encrypted Enrollment requests, dynamic Oracle fixtures, multi-plan execution, dashboard consolidation from eight scenarios to one lean test, and subsequent Enrollment APIs missing from the early spreadsheet.

## 3. What COMPLETE means
- Every in-scope operation has a canonical Java class/method and stable endpoint ID.
- The class is wired into an intended TestNG suite/profile and branding block.
- L1 HTTP, L2 contract, L3 typed/schema where supported, and L4 business assertions are present.
- Coverage registers and formal sign-off packs record exclusions and enhancement scope.
- Code presence is not a current green run; execution evidence remains run-specific.
- L5 universal API-to-DB reconciliation is documented analysis, not the approved completion gate.

Publish under "Unite MSC API Automation", then continue with Part B.
