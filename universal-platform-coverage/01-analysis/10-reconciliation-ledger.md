# Reconciliation Ledger

All leadership numbers must trace to this ledger.

## V2 qTest source population = 744

| Classification | Count | Counting unit |
|---|---:|---|
| IN_SCOPE_ENROLLMENT | 151 | executed qTest cases (provisional module map) |
| IN_SCOPE_IDP | 27 | executed qTest cases |
| IN_SCOPE_ABLE | 17 | executed qTest cases |
| IN_SCOPE_WITHDRAWAL | 73 | executed qTest cases |
| ADJACENT_NOT_CONFIRMED | 196 | executed qTest cases |
| OUT_OF_SCOPE | 80 | executed qTest cases |
| UNMAPPED_NEEDS_SME_CONFIRMATION | 200 | executed qTest cases |
| **Total** | **744** | |

**Validated V2 in-scope UI subtotal:** 268 (Enrollment, IDP, ABLE dedicated suite, Withdrawal — four workstreams on V2; excludes adjacent, out-of-scope, unmapped)

## V3 UE source = 303

| Classification | Count |
|---|---:|
| IN_SCOPE_ENROLLMENT | 303 |
| **Total** | **303** |

## V3 Unite source = 133

| Suite | Count | Classification |
|---|---:|---|
| IDP Login | 56 | IN_SCOPE_IDP |
| Member Withdrawal | 20 | IN_SCOPE_WITHDRAWAL |
| IDP Web Registration | 6 | ADJACENT_NOT_CONFIRMED |
| Contributions | 36 | ADJACENT_NOT_CONFIRMED |
| CSR Account Maintenance | 15 | ADJACENT_NOT_CONFIRMED |
| **Total** | **133** | |

**Validated V3 in-scope UI subtotal (nightly):** 379 (303 + 56 + 20)

## V3 combined source = 436

303 + 133 = 436 ✓

## API source inventory

| Metric | Source total | In-scope subtotal |
|---|---:|---:|
| Test methods | ~269 | ~207 (enrollment + IDP + withdrawal; **inventory estimate**, method-level export not attached) |
| Unique operations | 27 (all modules) | 11 (enrollment + IDP + withdrawal) |
| Test classes | 38 | 30 |

## Performance source inventory

| Metric | Source total | In-scope subtotal |
|---|---:|---:|
| JMX scripts | 36 | 15 assets mapped to in-scope workstreams (counting unit: JMX file per journey asset; deduplication not fully verified) |
| Taurus configs | 53 | ~15 (deduplicated) |

## Limitations

- V2 row-level qTest IDs unavailable — module provisional mapping
- V2/V3 overlap not reconciled to unique business requirements
- Adjacent suites excluded from leadership scoped totals pending SME
