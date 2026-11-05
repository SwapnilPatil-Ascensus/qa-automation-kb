# Teamwork Agreement

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Teamwork-Agreement-294989557.aspx) | Created: 2024-12-16 | Last modified: 2026-05-27 | Author: Pete Bretz | Last editor: Pete Bretz

---

**T** **eam White Logo**

#### Daily Scrum - Let's determine our PLAN FOR THE DAY!

- **Before the meeting**
  - Prepare answers to these questions so that we can focus on progress towards the Sprint Goal and not the technical details:
    - What's your plan for the day?
    - What are your impediments?
  - Update the board tasks
  - Remember that Production Issues should not derail the Daily Scrum. If an issue is a "drop everything" issue, it should have its own meeting. Otherwise, these items can be discussed as any other item on the board, including explicitly taking to the 17th minute or to a separate discussion.
- **During the meeting:**
  - Focus on progress towards the Sprint Goal
    - Includes swarming and limiting Work In Progress in order to achieve the Sprint Goal
  - Review In Progress Tasks count: [Current Sprint dashboard - Overview](https://tfs.ascensus.com/tfs/PSG/Portfolio/_dashboards/dashboard/aedf427c-13a2-4c90-9dd0-247675f7086e)
  - Review the board, top-down
  - Call out items that need to be added to the Scrum of Scrums agenda (blockers, dependencies, etc): [Scrum of Scrums](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Scrum-of-Scrums-326732448.aspx?web=1)
  - Check in with updates from Archers
  - **END OF DAILY SCRUM - 15 MINUTE LIMIT**
  - 16th Minute - Quick hitters (ex: "I'm off tomorrow")
  - 17th Minute - For topics that need a longer discussion. The goal of a 17th minute is to make sure everyone knows about it. If it needs a deep dive, it should be a separate discussion

#### Refinement

- Use this pointing tool: [https://play-game.scrumpypoker.com/#/room/dbwqlzrpjezc](https://play-game.scrumpypoker.com/#/room/dbwqlzrpjezc)
- Any team member can write a story, but do not place new stories in current sprint
- For Refinement, avoid getting too far into the technical details.
- When working on a new platform (ie, Salesforce, Chorus, etc), decide in Refinement if we need a spike story before building.
- Call out Spike stories early
- Review story tagging so we know how to properly call out and not lose track of new stories that have not been prioritized
- Use these Tags to indicate story status:
  1. Draft - Story Title with at least one acceptance criteria
  2. Shaped - As a/I want/So that summary, plus more fleshed out acceptance criteria. It should meet our [Definition of Ready](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Definition-of-Ready-17434865.aspx).
  3. Refined - Story is Pointed

#### Sprint Planning

- Potential template for facilitating: [Sprint Planning - Template - Team White - Ascensus - Confluence](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Sprint-Planning---Template-368322924.aspx)
- Add PTO to ADO calendar BEFORE Sprint Planning
- After we've set our goals and pulled our prioritized stories in, developers task out the stories
- Create all relevant tasks that we know about at the start of the sprint
- For stories with dependencies, ask, is the story ready relative to these dependencies (Chorus, PAS, Salesforce, etc)

#### Story creation process

- Anyone on the team can create stories, but do not place new stories in current sprint
- Keep the story up-to-date with ongoing work, but limit new requirements
- Attach a pairing task to each story. Decide who is story champion and who is pairing, including SME (testing/DevOps).
- If acceptance criteria needs to be modified, the team will either:
  - Create a new future story with that AC (or the new AC) if still applicable towards the goals and we can work on it in the future
  - If the AC ends up not being applicable towards our goal, then strike it out
  - These changes need to shared with the whole team

#### Issue tracking

- Bring up the issue immediately so we can determine if it's all hands-on deck
- We will create a new story for each production issue so that they are not thrown into larger buckets. We want to address and prioritize each issue individually.
- At the top of each sprint we'll have a Production Support story where we'll track issues.
  - Naming convention: "Sprint ## Production Issues - Group #". This helps with production deployments.
  - If we're using these stories, we're not going to point them; we'll use the Remaining Hours field on Tasks to estimate effort on items as they come in.
  - Tag the tasks for clarity (API, Unqork, etc).
  - The goal is that we don't need these granular production support buckets for the long term.
- When the rush of Production support issues slows down, we can stop tracking production issues as tasks within stories and, rather, create a story for each production issue.

#### Other

- For Production rolls, as part of the implementation plan, determine strategy for rollback
- Two developers required for code review
- Considerations for using Spare Capacity: [Teams Guiding Principle: Using Spare Capacity - Team White - Ascensus - Confluence](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Teams-Guiding-Principle-Using-Spare-Capacity-368324227.aspx)
