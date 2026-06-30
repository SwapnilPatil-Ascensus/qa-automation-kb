# Universal Platform Automation Coverage Assessment

Scoped reconciliation of automation inventory against five Aha workstreams (ACS-I-2679 through ACS-I-2690).

## Structure

- `00-input-evidence/` — Aha PDFs, qTest/Jenkins, TestNG reports (read-only copies)
- `01-analysis/` — Scope, methodology, inventories, reconciliation ledger, CSV mappings
- `02-deliverables/` — Leadership assessment (DOCX/PDF), email draft, SME checklist
- `03-tools/` — Master rebuild prompt and scripts
- `99-archive/` — Pre-rebuild snapshot (2026-06-29)

## Key scoped totals (see 01-analysis/10-reconciliation-ledger.md)

| Source | Population | Validated in-scope subtotal |
|---|---:|---:|
| V2 qTest | 744 | 268 |
| V3 TestNG (nightly) | 436 | 379 |
| API (universal modules) | ~269 methods | ~207 methods / 11 operations |
| Performance JMX | 36 | 15 journeys |

**Do not** present 744, 436, 1,180, 269, or 36 as Universal Platform scoped totals without classification.
