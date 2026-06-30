Subject: Universal Platform Automation Coverage Assessment — Scoped to Five Aha Workstreams

Kevin and Rajib,

Please find attached the Universal Platform Automation Coverage Assessment, scoped exclusively to the five Aha workstreams you requested: Universal Enrollment (ACS-I-2679), IDP/Authentication (ACS-I-2680), ABLE (ACS-I-2681), Angular (ACS-I-2682), and Withdrawal (ACS-I-2690).

This assessment reports validated automation inventory and business-flow coverage — not requirement-level percentages, as the Aha ideas do not yet provide an enumerated requirements baseline.

**V2 (qTest daily regression)** — source population 744 executed test cases. After scoped classification, **268** map directly to the five workstreams (enrollment, IDP login, withdrawal, and dedicated LA ABLE). An additional **196** cases require scope confirmation (web registration, CSR maintenance, contributions, transfers). **280** are out-of-scope or unmapped pending SME review (80 out-of-scope + 200 unmapped including per-plan expansion).

**V3 (GitLab nightly TestNG)** — source population 436 methods (Universal Enrollment 303 + Unite 133). **379** map to enrollment, IDP login, and member withdrawal. **57** Unite methods (contributions, CSR maintenance, web registration) are adjacent pending Angular/IDP scope confirmation. ABLE Entity Platform (6 scenarios) and Angular lib-ui (22 component tests) are implemented but not yet in the nightly pipeline.

**API and performance** — scoped separately. Eleven unique API operations and fifteen performance journeys align to the five workstreams. No ABLE-specific API automation was identified.

Pending SME validation with Nick on adjacent suite mappings, V2 per-plan expansion allocation, and pipeline enablement for implemented-but-unscheduled assets.

Happy to walk through the dashboard on request.

Best regards,
QA Automation
