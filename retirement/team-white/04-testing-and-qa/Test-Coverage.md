# Test Coverage

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Test-Coverage-294993400.aspx) | Created: 2024-12-20 | Last modified: 2024-12-20 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

Projects within the Onboarding solution will require at least 80% code coverage to pass in the build.  The following extension can be installed to track code coverage ahead of time (before completing a PR).

[https://marketplace.visualstudio.com/items?itemName=FortuneNgwenya.FineCodeCoverage2022](https://marketplace.visualstudio.com/items?itemName=FortuneNgwenya.FineCodeCoverage2022)

After installing this tool, the "Fine Code Coverage" results window can be viewed and pinned to the UI:

- View => Other Windows => Fine Code Coverage.

This will show the coverage for each file within the solution.  Additionally, VS2022 will indicate which lines have proper code coverage in the left side of the frame (left of the line numbers, if visible).

- Green lines are fully covered
- Yellow lines are covered in some branches, but not all
- Red lines have zero coverage

For example, in the following screenshot, line 27 is showing as yellow because at least one test exists where the Exception *ex*  is NOT NULL (which in this case bypasses lines 28-29).  Lines 28-29 are red because there are currently no tests which have Exception *ex*  = NULL.  All of these lines would turn green only after one or more tests satisfy this missing condition, resulting in that *branch*  of logic being traversed.

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Test-Coverage-294993400/image-2024-12-20_13-31-17.png)
