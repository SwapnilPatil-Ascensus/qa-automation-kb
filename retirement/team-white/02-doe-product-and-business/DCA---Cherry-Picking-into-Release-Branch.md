# DCA - Cherry Picking into Release Branch

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/DCA---Cherry-Picking-into-Release-Branch.aspx) | Created: 2026-08-11 | Last modified: 2026-08-11 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

![image](https://ascensus0.sharepoint.com/_layouts/15/images/sleektemplateimagetile.jpg)

### Prerequisites

•    Git access to the DCA repo
•    Commit IDs from **master** that need to go into the release

## Step 1: Create a New Branch off Release

```
git fetch origin
git checkout release
git pull origin release
git checkout -b white/<description> release
```

*Replace <description> with a short name for the change (e.g., white/123456-cherry-pick-onboarding-menu-item-visibility).*

## Step 2: Find Commit IDs on Master

Use the Git log to identify the commit(s) you need:

```
git log origin/master --oneline
```

Copy the commit hash(es) for the changes you need to cherry-pick.

*Tip: In Visual Studio, you can also use Git > View Branch History on master to browse commits visually and copy their IDs.*

## Step 3: Cherry-Pick the Changes

For a single commit:

```
git cherry-pick <commit-id>
```

For **multiple commits**  (in order, oldest first):

```
 git cherry-pick <oldest-commit-id> <next-commit-id> <newest-commit-id>
```

If you hit a **merge conflict** :
1.    Resolve the conflicts in the affected files.
2.    Stage the resolved files: **git add .**
3.    Continue the cherry-pick: **git cherry-pick --continue**
*To abort a cherry-pick gone wrong: **git cherry-pick --abort***

## Step 4: Push & Create a PR

```
git push -u origin white/<description>
```

Then create a Pull Request in Azure DevOps:
•    Source: **white/<description>**
•    Target: **release**
•    Add appropriate reviewers.
•    Fill in PR description

## Step 5: Update DCA Implementation Plan

Go to the [DCA Implementations page](https://ascensus0.sharepoint.com/sites/DCADevelopmentCollaboration/SitePages/DCA-Deployments.aspx?TeamsCID=60d7f68a-0986-43e7-a0fd-b59d3915c00e&linkOpenTime=1786124394373) and update the implementation plan with your change details.

## Step 6: Add Details to the Release Spreadsheet

In the DCA Implementation Plan release spreadsheet, add:
•    Team
•    Detail of item being released
•    Item & Version number (these come after the PR has been merged)
•    Link to Story

•    Pre-Implementation Tasks (all sections)
•    Database Changes (if applicable)
•    Octopus (release products/versions)

## Step 7: Complete the PR

Once approved, complete (merge) the PR into release in Azure DevOps.

## Step 8: Track the Release Version

After the PR merges, monitor the build in [TeamCity](https://teamcity.ascensus.com/buildConfiguration/Newport_Pdx_DcaSuite20_NpmBuild?mode=builds) and note the generated [release](https://octopus.ascensus.com/app#/Spaces-1/projects/dca/deployments/releases) version number.

## Step 9: Update Spreadsheet with Release Version

Go back to the DCA Implementation Plan release spreadsheet and record the release version from Octopus.

**NOTE:**  DCA.Foundation.API is deployed separately through Octopus following normal procedures.  No cherry picking needed there, but the release version should still be captured and tracked in the Octopus tab of the spreadsheet.

*Quick Reference — Common Issues:*
*•    Wrong commit picked? Run git revert <commit-id> on your branch before the PR is merged.*
*•    Need to start over? Delete the branch and re-create from Step 1.*
