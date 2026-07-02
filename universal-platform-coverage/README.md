# Universal Platform Automation Coverage Assessment

Scoped reconciliation of automation inventory against five Aha workstreams (ACS-I-2679 through ACS-I-2690).

## Structure

- `00-input-evidence/` — Aha PDFs, qTest/Jenkins, TestNG reports (read-only copies)
- `01-analysis/` — Scope, methodology, inventories, reconciliation ledger, CSV mappings
- `02-deliverables/` — Final leadership assessment (DOCX/PDF), email update
- `03-tools/` — Master rebuild prompt and scripts
- `99-archive/` — Pre-rebuild snapshot (2026-06-29)

## Key scoped totals (see 01-analysis/10-reconciliation-ledger.md)

| Source | Population | UP-scoped subtotal | Inventory share |
|---|---:|---:|---:|
| V2 qTest | 744 | 268 | 36.0% |
| V3 TestNG | 436 | 379 | 86.9% |
| API (unique operations) | — | 11 | — |
| Performance (journeys) | — | 15 | — |

**Final deliverables:** `02-deliverables/Universal-Platform-Test-Automation-Coverage-Assessment-Final.docx` and `.pdf`

**Do not** sum V2 and V3 totals or present inventory-share percentages as requirement-level coverage.
