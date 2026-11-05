# Nick SME Validation Checklist — Factual Questions Only

## V2 in-scope mappings

1. Does the enrollments module (151 cases) fully map to ACS-I-2679, or should ABLE enrollment scenarios be reclassified to ACS-I-2681?
2. How should the 179-case PRIME per-plan expansion (744 minus documented modules) be allocated across workstreams?
3. Are web registration (46) and web login (27) both in-scope for ACS-I-2680?

## V3 suite-to-workstream mapping

4. Do all 303 Universal Enrollment methods belong to ACS-I-2679?
5. Should IDP Web Registration (6 methods) count under ACS-I-2680?
6. Should Contributions (36 methods) count under ACS-I-2682 (Angular)?
7. Should CSR Account Maintenance (15 methods) count under ACS-I-2682 or ACS-I-2681?

## Angular scope

8. Are the 22 lib-ui dynamic-forms component tests the intended ACS-I-2682 artifact?
9. Should Blazemeter Selenium UE/login flows count as Angular coverage?

## ABLE plan split

10. Confirm V2 ABLE plan set (AKB, COB, ILB, MIB, NHB, NYB, PAB, RIB, TNB) and dedicated LA ABLE suite (17 cases).
11. Confirm V3 Entity plans (MIB, NEB, VAB) and pipeline enablement target.
12. Is MIB correctly treated as separate V2 vs V3 implementations (no double-count)?

## API scope and scheduling

13. Confirm API modules in scope: auth, account/enrollment, financial/withdrawal only?
14. Which API gates are scheduled vs implemented-only?

## Performance scope and scheduling

15. Which of the 15 scoped performance journeys are scheduled with SLA governance?
16. Should database prototype scripts ever count as business-flow coverage?

## Unresolved adjacent tests

17. Should V2 transfers (12) map to ACS-I-2690?
18. Should empower-plan (21) and csr-actions (9) map to enrollment, ABLE, or remain out of scope?
