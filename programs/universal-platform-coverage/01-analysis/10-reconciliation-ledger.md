# Reconciliation Ledger

All leadership numbers trace to this ledger. **Final SME review complete (July 1, 2026).**

## V2 qTest source population = 744

| Classification | Count | Counting unit |
|---|---:|---|
| IN_SCOPE_ENROLLMENT | 151 | executed qTest cases |
| IN_SCOPE_IDP | 27 | executed qTest cases |
| IN_SCOPE_ABLE | 17 | executed qTest cases |
| IN_SCOPE_WITHDRAWAL | 73 | executed qTest cases |
| Legacy / non-UP / out-of-scope | 476 | executed qTest cases |
| **Total** | **744** | |

**UP-scoped V2 UI subtotal:** 268 (151 + 27 + 17 + 73)

**Inventory share:** 268 ÷ 744 = **36.0%**

## V3 source population = 436

| Suite / component | Count | In scoped subtotal? |
|---|---:|---|
| Universal Enrollment | 303 | Yes |
| IDP Login | 56 | Yes |
| Member Withdrawal | 20 | Yes |
| IDP Web Registration | 6 | No (adjacent) |
| Contributions | 36 | No (adjacent) |
| CSR Account Maintenance | 15 | No (adjacent) |
| **Total nightly source** | **436** | |

**Directly scoped V3 UI subtotal:** 379 (303 + 56 + 20)

**Other / adjacent V3 inventory:** 57 (6 + 36 + 15)

**Inventory share:** 379 ÷ 436 = **86.9%**

## Reported separately (not in V3 scoped subtotal of 379)

| Component | Count | Notes |
|---|---:|---|
| ABLE Entity Platform | 6 scenarios | MIB, NEB, VAB — implemented V3 |
| Angular lib-ui | 22 component tests | Not E2E business-flow coverage |

## API (in-scope)

| Workstream | Unique operations |
|---|---:|
| Enrollment | 5 |
| IDP | 4 |
| Withdrawal | 2 |
| **Total** | **11** |

## Performance (in-scope business journeys)

| Workstream | Journeys |
|---|---:|
| Enrollment | 7 |
| IDP | 6 |
| Withdrawal | 1 |
| ABLE Entity | 1 |
| **Total** | **15** |

## Measurement boundaries

- V2 and V3 are not summed (different frameworks; functional overlap may exist).
- Inventory-share percentages are not requirement-level coverage.
- No ABLE-specific API automation identified in reviewed repositories.
