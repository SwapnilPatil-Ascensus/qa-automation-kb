# Counting Methodology

## Separate metrics (never mixed)

| Layer | Primary unit | Secondary units |
|---|---|---|
| V2 UI | qTest executed test cases (744 source population) | Jenkins module methods (508 subset), suite `<test>` blocks |
| V3 UI | TestNG executed methods (436 source) | Suite `<test>` definitions (59), feature files |
| API | Unique HTTP operation (method + path) | Test methods, test classes |
| Performance | Unique business journey | JMX scripts, Taurus configs |
| Angular | Component/library test definitions | E2E business-flow tests (reported separately) |

## Leadership metrics

- **Validated in-scope inventory** — only items with IN_SCOPE_* classification
- **Adjacent inventory** — reported separately, excluded from scoped totals
- **Scheduled vs implemented** — noted per workstream

## V2 vs V3

Reported separately. Overlap between frameworks is not presented as unique combined coverage.
