# ABLE Two-Part Analysis

## Part A — Unite ABLE / CSR (V2)

- **ABLE plan codes (ending B):** AKB, COB, ILB, MIB, NHB, NYB, PAB, RIB, TNB (9 plans)
- **Parameterized blocks:** 43 plan-specific test blocks embedded in scheduled V2 modules
- **Dedicated LA ABLE suite:** 17 executed test cases (`stage1-laable.xml`) — **in-scope ABLE count for V2 dedicated suite**
- **Status:** Maintained in V2 framework; dedicated suite implemented, scheduling confirmation pending
- **Reuse:** Many flows reuse common scenarios with plan parameterization

## Part B — ABLE Entity Platform (V3)

- **Repository:** prime-test-automation/unite-entity
- **Suite definitions:** Entity registration (3 blocks) + Entity dashboard IDP login (3 blocks)
- **Plans:** MIB, NEB, VAB
- **Scheduled nightly:** No — not wired in `stage1-unite-regression-master.xml`
- **Counting unit:** 6 suite test definitions (expands to scenarios at execution)

## Separation

MIB appears in both Part A (V2 CSR/member) and Part B (V3 entity). **Different implementations — not merged or double-counted.**

## API

No ABLE-specific API automation was identified in the reviewed repositories.
