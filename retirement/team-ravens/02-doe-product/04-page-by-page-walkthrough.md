# 04 - Page-by-page walkthrough (QA, 2026-11-05)

All screenshots are in [`assets/screenshots/`](assets/screenshots/). Synthetic data only (`qa.advisor@example.com`, fake business). Nothing was submitted to sign/e-sign steps.

## A. Advisor flow - Group 1 Individual(k) (Victory example)

| # | Screen | What it shows | Fields / controls | Screenshot |
| - | --- | --- | --- | --- |
| A1 | **Landing / Get started** | Partner logo, "Get started with <Partner>", plan name, 3 FAQ accordions (what info, how long, how notified), **Employer fees** (setup, 1st participant, each extra) and **Participant fees** (Victory only), "Let's get started" card | Advisor CRD (optional) - "saves time by pulling in Advisor information"; OR first name, last name, email; **Get started** | ![landing](assets/screenshots/g1-victory-01-landing.png) |
| A2 | **Firm Information - Review your business information** (stepper: Firm Information > Plan Details > Confirmation) | Advisor business info | Business name, advisor first/last, branch number, rep ID, CRD, address 1/2, city, state (searchable select), zip, email, phone `(XXX) XXX-XXXX`; **Back / Continue**; debug fields "Onboarding ID" and `planId` exist in DOM (QA only) | ![business info](assets/screenshots/g1-victory-02-advisor-business-info.png) |
| A3 | **Dealer information** | Broker-dealer link | Dealer number; Back / Continue | ![dealer](assets/screenshots/g1-victory-04-dealer-info.png) |
| A4 | Plan Details (not reached) **[Doc/Guess]** | Client (sponsor) info, "does the client have an existing plan?" (yes: date + sequence number; no: fund list), fund list with default fund, eligibility, bank/payment method for fees | | |
| A5 | Confirmation (not reached) **[Doc]** | Advisor part done; emails: advisor completed, sponsor completed + signed, setup complete | | |

State dropdown behaviour: hidden 1x1 "Select box focus" button + visible custom select; a coordinate click opens a searchable list of all US states, DC, Guam, Puerto Rico, US Virgin Islands. ![state](assets/screenshots/g1-victory-03-state-dropdown.png)

### Partner variations on the landing page

| Partner | Screenshot |
| --- | --- |
| Ameriprise ($375 first participant) | ![](assets/screenshots/g1-ameriprise-landing.png) |
| Pershing | ![](assets/screenshots/g1-pershing-landing.png) |
| J.P. Morgan ($345) | ![](assets/screenshots/g1-jpmorgan-landing.png) |
| Ascensus Balance Forward | ![](assets/screenshots/g1-ascensus-balfwd-landing.png) |
| Ascensus Daily Level Comp (5 days **assuming a Common Remitter Agreement is in place**) | ![](assets/screenshots/g1-ascensus-dailylc-landing.png) |
| Ascensus Direct Fee Based | ![](assets/screenshots/g1-ascensus-dailyfb-landing.png) |
| State Farm - "Agent" wording, no CRD | ![](assets/screenshots/g1-statefarm-landing.png) |

Best-guess business logic **[Guess]**:
- **First-participant fee** is the partner price lever ($150 Victory, $235 State Farm, $345 JPM, $375 Ameriprise/Pershing, $425 Ascensus); setup ($125) and each extra participant ($150) are constant.
- **Participant asset fee** (0% for Victory, 0.07% for Ascensus Daily products) appears only on "Daily" offerings; "Balance Forward" offerings show none.
- Landing text and fees are driven by `product=` (offering key) and branding by `style=` (logo/colors), which is why one Unqork app serves 8 partners.
- State Farm omits CRD because its agents are captive (no FINRA CRD).

## B. Sales flow (Group 1, `preview=true`)

"Let us help you find the right Individual(k) plan" with FAQs ("Is an Individual(k) right for my client?", "Are nonprofits eligible?", "Why choose an Individual(k)?"). Same start form as the eapp, but fees render **blank ($ with no number)** because no product is selected yet. ![sales flow](assets/screenshots/g1-sales-flow.png)

## C. Dashboard (Group 1 and DCA partner dashboard)

"Onboarding Plans": chart tiles + tabs **Follow up** and **Individual(k)**; table columns PLAN, START DATE, TIME, SPONSOR, DUPLICATE EIN. Without a signed-in partner user it shows skeleton loaders then "Not found - Page 1 of 0". ![dashboard](assets/screenshots/g1-dashboard.png)
Related releases **[Doc]**: Resolve Hardstop, Sponsor History, Cancel/Extend/Reactivate, CSV export for analytics, partner filter, DCA partner dashboard for external users.

## D. Group 2 - BAML / Merrill Edge

| Screen | Details | Screenshot |
| --- | --- | --- |
| Individual(k) landing | "Complete your Solo(k) setup in just a few minutes!", "Things to know" accordions (info needed, setup process, **can I save my progress and complete later?**, who is this plan for), fees ($0 setup, $67.50 quarterly; participant $15 quarterly + 0.70%), start form: first name, last name, business email, **phone number for secure log in** | ![](assets/screenshots/g2-baml-ik-onboarding-portal-redirect.png) |
| Group landing | "A simple, affordable 401(k) plan tailored to fit your business." Fees: $0 setup, $285 quarterly; participant $15 quarterly + 0.70% | ![](assets/screenshots/g2-baml-group-landing.png) |

The 0.70% breakdown shown on the page: fiduciary services 0.08% + call-center servicing 0.20% + account services/trading/custody/financial wellness 0.42%.

## E. Group 2 - ShareBuilder purchase-site simulator

Internal QA-only form that posts a purchase to Onboarding so testers do not need the real ShareBuilder site. ![simulator](assets/screenshots/g2-sharebuilder-partner-site-simulator.png)
Key inputs: contact + business + address, EIN, **group vs Individual(k)**, **existing plan to transfer?**, **allow safe harbor contribution?**, default contribution %, routing / account / checking-savings, default model portfolio (Conservative, Balanced, Moderate, Growth), profit-sharing formula (Social Security Integrated, Salary Proportionate/ProRata, Age Weighted, New Comparability), partner admin and setup fee discounts (amount and percent), readonly partner redirect URL.

## F. Group 2.2 - Sales Portal

Internal staff page: choose Individual(k) or Group, partner, installation type **Startup / Transfer**, then **Generate welcome email**. ![sales portal](assets/screenshots/g22-sales-portal-qa.png)

Next: [05 Test strategy and coverage](05-test-strategy-and-coverage.md)
