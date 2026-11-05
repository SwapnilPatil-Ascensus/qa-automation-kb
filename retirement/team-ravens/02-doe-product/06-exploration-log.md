# 06 - Exploration log (2026-11-05, QA only)

Scope respected: only `retsupport-qax`, `secure-qa`, `demo-merrilledge` QA links from Group 1 and Group 2. No PRO links opened. No shared test credentials were typed anywhere. No submit/e-sign actions.

## What worked
- All 10 Group 1 QA links load **without login** and render the right partner landing page.
- URL pattern: `eapp-1737642567136?style=<brand>#/display/<appId>?partner=<p>&product=<offeringKey>`; Unqork rewrites the hash to internal IDs after load.
- Advisor start -> **Firm Information** screen works with name + email.
- BAML IK and Group entries work end to end up to the landing screen (creates an `onboardingId`).
- ShareBuilder Purchase Site Simulator and Sales Portal QA load without login.

## Observations / possible defects (to confirm with Ravens)

| # | Observation | Where | Severity guess |
| - | --- | --- | --- |
| 1 | **CRD lookup did not prefill** advisor details after entering sample CRD `6249274` and tabbing out (doc says it should populate on blur) | Victory landing | Medium - maybe QA backend/VPN or CRD not in QA data |
| 2 | **Dealer information step did not advance** with dealer number `12345` on Continue (twice) | Victory, Firm Information | Medium - probably needs a valid dealer lookup; cannot tell without network trace |
| 3 | Sales Flow landing shows **blank fee values** ("$" with no number) | Sales Flow preview | Low - expected before product selection, but looks unfinished |
| 4 | Onboarding Portal interstitial contains an **"Error" heading** in the DOM while redirecting ("Hang tight...") | secure-qa BAML initialize | Low - hidden error container, but check it is not visible on slow networks |
| 5 | Dashboard shows skeleton + "Not found / Page 1 of 0" without a user | Dashboard | Info - needs signed-in partner |
| 6 | QA pages expose **debug fields** (Onboarding ID, planId) and a Preview bar ("Preview as", "Preview Style") | all eapp pages | Info - QA only, confirm absent in PRO |
| 7 | Page text still says **"(c) 2025 Ascensus, LLC"** in November 2026 | footer | Low - copyright year |
| 8 | `logRocketPanel` heading present on every page (LogRocket integration active in QA) | eapp | Info |

## Not explored (needs login/approval)
- Newport Test Boss and partner dashboard (login required).
- DEV2 and QA Sales Portal "Generate welcome email" (would send email).
- ShareBuilder real QA site (third party).
- Plan Details, Confirmation, sponsor-side screens, DocuSign.

## Next steps
1. Pair with Aashay/Ema for a real walkthrough (CRD, dealer, plan details).
2. Open network tab / LogRocket QA sessions to see the API calls behind CRD lookup and dealer validation.
3. Add the observations above as questions in the Ravens action items ([`../05-open-items/action-items.md`](../05-open-items/action-items.md)).
