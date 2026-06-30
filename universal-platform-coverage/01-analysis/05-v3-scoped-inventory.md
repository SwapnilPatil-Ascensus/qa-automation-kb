# V3 Scoped Inventory

## Source populations

| Report | Source total |
|---|---:|
| Universal Enrollment | 303 |
| Unite (IDP Login + Contributions + Withdrawal + CSR + Web Reg) | 133 |
| **Combined V3 source** | **436** |

### Unite component check

56 + 36 + 20 + 15 + 6 = **133** ✓

## Scoped vs adjacent (nightly scheduled)

| Classification | Count |
|---|---:|
| IN_SCOPE_ENROLLMENT | 303 |
| IN_SCOPE_IDP | 56 |
| IN_SCOPE_WITHDRAWAL | 20 |
| ADJACENT_NOT_CONFIRMED | 57 |
| **Nightly source total** | **436** |

## Validated in-scope V3 UI subtotal (nightly)

**379** executed TestNG methods (UE 303 + IDP Login 56 + Member Withdrawal 20).

## Implemented but not in nightly master

- ABLE Entity Platform: 6 suite test definitions (MIB, NEB, VAB)
- Angular lib-ui: 22 component test definitions

436 is **not** published as Universal Platform scoped coverage without excluding adjacent suites (Contributions 36, CSR 15, Web Registration 6).
