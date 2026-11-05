# 04-01-2026 Salesforce requirements for Group 1 and 2.2 review

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-04-01-2026--Salesforce-requirements-for-Group-1-and-2.2-review-378705893.aspx) | Created: 2026-04-01 | Last modified: 2026-04-07 | Author: Palak Bhatt | Last editor: Enes Ulukaya

---

#### Date

2026-03-31

#### Attendees

- Christopher McCoy
- [@Enes Ulukaya](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Enes.Ulukaya%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37c68bed0017cbcd4e3480022)
- [@Palak Bhatt](https://ascensus0.sharepoint.com/_layouts/15/sharepoint.aspx?q=Palak.Bhatt%40ascensus.com&v=/search/people&wtmri=user%3akey%3aatlassian%3a%7conprem%7c2c9286a37f5da6e3017f8dccba35001f)

#### Goals

- Walkthrough of Group 1 requirements from the email shared by Christopher McCoy; additional discussion on opportunity stages (Group 2.2 / dashboard vs. Salesforce for sales reps).
- Link to the recording -

#### Purpose

- Align on Group 1 DOE-related asks (opportunity naming, Daily Value fund entry, plan name/start date flexibility, sold date, advisor completion of sponsor portion, plan docs to advisors, pre-onboarding wording).
- Clarify ownership (Team White vs. business / Jodi & Ian).
- Capture follow-up on “Waiting for signature” vs In progress / Closed Won and current Group 1 behavior when documents are generated.

#### Discussion items

##### Discussion summary and decisions / alignment

| **#** | **Topic** | **Discussion / outcome** |
| --- | --- | --- |
| 1 | Opportunity name: company vs. plan ID | <br>Use company / plan name as the Salesforce Opportunity name when the opp is created (not plan ID), so advisors and automated emails are meaningful. Plan name is expected to be available from the sponsor flow.<br>**Already in Team White product backlog; to be taken with other Group 1 work.**<br>**[Product Backlog Item 763870](http://tfs.ascensus.com:8080/tfs/PSG/Portfolio/_workitems/edit/763870): [Salesforce Integration] - Replace the Plan ID in the Opportunity name with the Business Name**<br> |
| 2 | Daily Value: bulk ticker upload | <br>Today advisors search/add each fund one-by-one (Daily Value level comp / fee-based). Request: upload Excel (e.g., template with ticker column) to populate lineup—helps FAs with repeating lineups.<br>Chris noted larger lift than item 1.<br>2026-04-06 - Future enhancement opportunity per meeting with Ian and Jodi.<br>**Enes: business decision—escalate to Jodi and Ian, not solely Team White.**<br>**Chris offered demo/screenshot in chat.**<br> |
| 3 | Editable plan business name on either the UI or the data blob that gets fed into the forms | <br>Default remains sensible (e.g., adopting employer name + “IK plan” suffix). Allow sponsor to edit the plan name field so clients who want “401(k) plan,” “retirement plan,” etc. don’t need amendments.<br>Chris: reduces IK service amendment volume.<br>2026-04-06 - Nice to have and will not be prioritized.<br>**Take to Jodi and Ian (Enes: aligned with past requirements discussions).**<br> |
| 4 | Editable plan start date (default) | <br>Same pattern: default from answers, but allow a later (not earlier) date—e.g. completing DOE in Dec 2025 with start Jan 2026 when overlapping IRA/plan rules matter. Chris: Ian had suggested “don’t fund in 2025”; group noted compliance drivers for actual start date.<br>2026-04-06 - Nice to have and will not be prioritized.<br>**Take to Jodi and Ian.**<br> |
| 5 | Sold date on Opportunity | <br>Do not set sold date on creation; set only when Opportunity is Closed Won (or equivalent final stage).<br>**Team White scope. Aligns with keeping “in progress” accurate.**<br> |
| 6 | Advisor completes employer/sponsor portion (Group 1) | <br>Intent: advisor can enter sponsor details (or skip if unknown); sponsor still gets link to review—similar to CoPilot / Group 2.2 patterns.<br>For Group 1 advisor-sold BF and Daily Value, still desired;<br>2026-04-06 - Future enhancement opportunity per meeting with Ian and Jodi.<br>**Palak to confirm whether any Group 1 build exists—check with Jodi/Ian if unclear.**<br>Chris: important for advisor value and reducing sponsor confusion.<br> |
| 7 | Send copy of plan docs to advisor (Balance Forward) | <br>High manual volume today. Chris: Ian may already be driving an update since the original email—confirm status.<br>**Palak to follow up with Ian on Group 1 / advisor copy.**<br>**[Product Backlog Item 766843](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/766843): Email Signed Plan Sponsor Documents to Advisor for Balance Forward Group 1 Product**<br> |
| 8 | Pre-onboarding question wording | <br>Change “Does the client have an existing qualified retirement plan they are *transferring* ?” to remove “transferring” → “Does the client have an existing qualified retirement plan?” Reduces confusion for document-only → recordkeeping moves (not a “transfer” in client’s mind).<br>2026-04-06 -  Potential new requirements for a new helper text. Need to confirm with Ian.<br>**Jodi and Ian for approval/wording.**<br> |
| 9 | Existing plan + Ascensus + optional Plan ID (new related ask) | <br>If “yes” to existing plan, consider flow: Is it with Ascensus? If yes, optional field for current plan ID (skippable)—aimed at document-only cases where EIN hard-stop may not apply, to improve linkage and possible downstream trigger (e.g., notify document services when new BF/DV plan is set up). Enes noted EIN validation / hard stop for plans in system; Chris clarified gap for doc-only. Ian / Jodi decision on product flow.<br>[Product Backlog Item 778282](https://tfs.ascensus.com/tfs/PSG/Portfolio/_workitems/edit/778282): Creating an "Allow Duplicate EIN" button in the Internal Dashboard in order to facilitate Internal Conversion Plans<br> |

##### Additional discussion: Opportunity stages — “Waiting for signature” vs dashboard

- Team had been refining Group 2.2 stories/dashboard with two opportunity stages: In progress and Closed Won (for consistency across groups).
- Chris (sales support): Sales reps do not use the internal dashboard; they live in Salesforce. They need to see docs generated but unsigned vs truly complete.
- Issue: For Group 1, opportunities are reportedly marked Closed Won when documents are generated, not when signed—causing manual rework (reopen, move to waiting for signature, advisor emails). Group 2 behavior may already differ (closed after signature)—Palak to verify with engineering.
- Desired: (1) Stop moving to Closed Won until documents are signed (priority fix). (2) “Waiting for signature” (or equivalent) in Salesforce to support automation (e.g., alert advisor if still unsigned after ~30 minutes).
- Palak to take back to Team White and respond to Chris on Waiting for signature and Group 1 vs 2.2 behavior.

Testing note: Chris continues coordination with Chris Reynolds on Balance Forward testing.
