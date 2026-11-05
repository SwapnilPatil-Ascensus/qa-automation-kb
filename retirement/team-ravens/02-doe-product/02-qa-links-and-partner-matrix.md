# 02 - QA links and partner matrix (QA only - never PRO)

> **Rule from the team lead:** only QA (Group 1 and Group 2). **Do not open PRO links.** PRO links are intentionally not repeated in this file; they exist only in the raw source page.
> Shared test-account passwords are **not** stored in this repo. Ask the team (they are on the Useful Links page) or use the team password vault.

## Environment map

| Env | Unqork host | Used for |
| --- | --- | --- |
| DEV | `retsupport-devx.unqork.io` | developer testing |
| DEV2 ("QA") | `retsupport-dev2x.unqork.io` | Sales Portal dev copy |
| **QA** | `retsupport-qax.unqork.io` | **our test target** |
| PRO | `retsupport.unqork.io` | do not touch |

Unqork builder/designer sign-in is separate (`retsupport-qa.unqork.io`, SSO via `mfaqa.ascensus.com/secureauth21`).

## Group 1 (Individual(k)) - QA links

All use one Unqork app `eapp-1737642567136`; the partner is selected by URL parameters, then the app rewrites the URL to internal IDs. **[Seen]**

| # | Partner | `style=` | `product=` | Landing page seen | Employer fees seen (setup / 1st ppt / each extra) | Participant fee seen |
| - | --- | --- | --- | --- | --- | --- |
| 1 | Victory | `amundi` (rewrites to `victory`) | `AmundiDailyIk` | "Get started with Victory - Individual(k)" | $125 / $150 / $150 | 0% asset based |
| 2 | Ameriprise | `ascensus` | `AmeripriseBalFwdIk` | "Get started with an Ameriprise - Individual(k)" | $125 / $375 / $150 | none shown |
| 3 | Pershing | `bny-pershing` | `PershingBalFwdIk` | "Get started with Pershing" (BNY Pershing logo) | $125 / $375 / $150 | none shown |
| 4 | J.P. Morgan | `jpm` | `JPMorganBalFwdIk` | "Get started with JP Morgan" | $125 / $345 / $150 | none shown |
| 5 | Ascensus Balance Forward | `ascensus` | `AscensusBalFwdIk` | "Balance Forward Individual(k)" | $125 / $425 / $150 | none shown |
| 6 | Ascensus Daily LC | `ascensus` | `AscensusDailyLCIk` | "Daily Level Comp 50 Individual(k)" (+ Common Remitter Agreement note) | $125 / $425 / $150 | 0.07% |
| 7 | Ascensus Daily Fee Based | `ascensus` | `AscensusDailyFBIk` | "Direct Fee Based Individual(k)" | $125 / $425 / $150 | 0.07% |
| 8 | State Farm | `statefarm` | `StateFarmDailyIk` | "Get started with State Farm" - **Agent** first/last/email, **no CRD field** | $125 / $235 / $150 | none shown |
| 9 | Sales Flow | `ascensus` (+ `preview=true`) | n/a | "Let us help you find the right Individual(k) plan" (questionnaire entry); fee values render blank | blank | blank |
| 10 | Dashboard | `ascensus` | n/a | "Onboarding Plans" with Follow up / Individual(k) tabs; shows loading skeleton, "Not found / Page 1 of 0" without a signed-in user | n/a | n/a |

Screenshots: [`assets/screenshots/`](assets/screenshots/) (`g1-*.png`).

## Group 2 - QA links

| Partner | Link purpose | What happens **[Seen]** | Not tested here |
| --- | --- | --- | --- |
| ShareBuilder | **Purchase Site Simulator** `.../app/partner-site` | Loads an Unqork form that imitates ShareBuilder's "purchase submitted" call: name, email, phone, business, address, EIN, group vs IK, transfer (Y/N), safe harbor, bank routing/account, model portfolio, profit sharing, partner discount fields, **Submit Purchase**, redirect URL | Submit (would create a QA onboarding + emails) |
| ShareBuilder | Real ShareBuilder QA site (third party) | not opened (third-party site) | pick **SoloK Plus** (loans or multiple owners); a credit-card prompt means wrong product; test bank acct 333555222, any routing |
| BAML | Merrill Edge demo (IK + Group) | Redirects through `secure-qa.ascensus.com/onboarding/portal/baml/initialize?plandesigntype=ik` (or `=group`) (brief "Hang tight" + an "Error" heading in markup), creates an `onboardingId`, then lands on Unqork `sign-in/landingpagebaml` with Merrill branding | Phone OTP step, rest of flow |
| BAML | Fees shown | IK: $0 setup, $67.50 billed quarterly; Group: $0 setup, $285 billed quarterly; participant $15 quarterly + 0.70% asset costs | |
| Newport Group | Test Boss (`testboss.newportgroup.com`) -> Test Sponsor Access -> swap URL to partner dashboard | requires login | everything |
| Sales Portal (2.2) | QA Sales Portal | Loads without login: Plan type (IK/Group), Partner dropdown (default Ascensus), Installation type (Startup/Transfer), **Generate welcome email** | Generating an email |

## Related internal QA systems (access by service ticket)

Cliff QA (`cliff.qa.internal.ascensus.com`), Chorus QA (SS&C beta), ARK QA (`ark-qa.ascensus.com`), Sybase QA (`bps_test`), SQL `Msvc_Onboarding` (QA server listed on the Access page), TeamCity/Octopus "Onboarding" projects, TFS repos `Onboarding` and `DCA`. Details: [`../../team-white/04-testing-and-qa/Onboarding-Project-Access-and-Application-Testing-References.md`](../../team-white/04-testing-and-qa/Onboarding-Project-Access-and-Application-Testing-References.md).

Next: [03 Workflows and diagrams](03-workflows-and-diagrams.md)
