# E2E — Cross-feature index

**Status:** Not Started | **Scenarios:** 1 in `e2e.feature`

The e2e feature exercises multiple BFF endpoints in one flow. Do not duplicate SQL here — link to feature-specific validation docs.

## Feature doc index

| Feature file | KB path | Endpoints used in e2e |
|--------------|---------|----------------------|
| mobiledashboard | [mobiledashboard/overview.md](../mobiledashboard/overview.md) | mobiledashboard, mobilemembers |
| mobilebank | [mobilebank/overview.md](../mobilebank/overview.md) | mobilebanks |
| mobilecontribution | [mobilecontribution/overview.md](../mobilecontribution/overview.md) | mobilecontribution |
| mobileactivity | [mobileactivity/overview.md](../mobileactivity/overview.md) | mobileactivity |
| mobileTransactionHistory | [mobileTransactionHistory/overview.md](../mobileTransactionHistory/overview.md) | mobiletransactionhistory |
| mobilePerformance | [mobilePerformance/overview.md](../mobilePerformance/overview.md) | mobileperformance |
| mobileBalanceTrend | [mobileBalanceTrend/overview.md](../mobileBalanceTrend/overview.md) | mobilebalancetrend |
| mobileStackup | [mobileStackup/overview.md](../mobileStackup/overview.md) | mobilestackup |
| mobileugift | [mobileugift/overview.md](../mobileugift/overview.md) | mobileugift |
| investment | [investment/overview.md](../investment/overview.md) | investments |
| planselection | [planselection/overview.md](../planselection/overview.md) | plans |
| contentservice | [contentservice/overview.md](../contentservice/overview.md) | content (no DB) |

## Validation strategy for e2e

1. Decompose e2e scenario into constitutent API calls.
2. Run per-feature SQL validation at each step.
3. Document cross-step data dependencies in a scenario file under `scenarios/` when e2e is expanded.

## Registry

Full endpoint list: `mappings/endpoint-registry.yaml`
