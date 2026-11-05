# DOE - QA Testing

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-DOE---QA-Testing-305981535.aspx) | Created: 2025-02-26 | Last modified: 2025-02-26 | Author: Franklin Zabala | Last editor: Franklin Zabala

---

**From:**  Eric Ma <[eric.ma](http://eric.ma)@[auxosolutions.io](http://auxosolutions.io)>
**Sent:**  Tuesday, February 25, 2025 5:03 PM
**To:**  Franklin Zabala <Franklin.Zabala@[ascensus.com](http://ascensus.com)>; Liam Cranley <liam@[auxosolutions.io](http://auxosolutions.io)>; Yashica Prabhakar <yashica.prabhakar@[auxosolutions.io](http://auxosolutions.io)>; Christopher Bauer <Chris.Bauer@[ascensus.com](http://ascensus.com)>
**Subject:**  [EXTERNAL] Re: App testing in QA

**WARNING:** **External Sender! Exercise caution with links, attachments and requests for login information. When in doubt, report it by clicking the Phish Alert Report button at the top of this email.**

Ok, I have the start of a product flow on QA. I will list here the happy path and known bugs.

1. Go to [https://retsupport-qax.unqork.io/app/eapp-1737642567136#/display/6792535b44a8367b0f7ebb20](https://url.us.m.mimecastprotect.com/s/ydRdC5ygRWhNZGOJSzf2TkOnOU?domain=retsupport-qax.unqork.io)
2. Enter a CRD, example: 6249274
3.
  1. The information retrieved is populated when the CRD field is unfocussed.
4. Click Get Started
5. Select “Ascensus”
6.
  1. Click Next
7. Select “Include Amundi funds only”
8.
  1. Click Next
9. Click “Let’s do it”
10. You now enter the Advisor flow
11.
  1. Onboarding ID debug field is here for illustration purposes
12. Enter Advisor Info
13.
  1. Click next
14. Enter Adivsor business info
15.
  1. Click next
16. Enter client information
17.
  1. Click next
18. Does the client have plan?
19.
  1. Either Yes or No work here
  2.
    1. Yes
    2.
      1. Enter date and sequence number
    3. No - goes to fund list
20. Fund List
21.
  1. Add some funds, select a default.
  2. Click next
22. Done
23.
  1. Does not update Ascensus record yet.

Known Issues:

- Navigation/Status on left nav  in both sales and advisor flow are broken
- No address verification yet
- Required fields still firing on page refresh
- Funds list, delete from list not functional yet

Still a work in progress but I wanted to make sure you had something to start automation with.
Sponsor portion as well as some of the bugs will be taken care of the rest of this week and the rest of the flows will follow shortly after.

Thanks,
Eric

*Oleksandr Klysheiko wrote on Friday, July 18, 2025 9:08:40 PM UTC (1)*

The test results for the complete DOE process, including **Cliff**  and **Chorus**  outputs for each partner in QA, have been finalized. This testing was conducted on **July 18, 2025** , as part of our preparation for the return to **PRO** .

**Important Note:**  Due to the file size limitations in TFS (4MB per document), the test result files exceeded the allowed upload size for historical documentation. Therefore, I have saved the complete results in an alternate location for reference.[Onboarding project test in QA DOE tests result 07182025.zip](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-DOE---QA-Testing-305981535/Onboarding%20project%20test%20in%20QA%20DOE%20tests%20result%2007182025.zip?wtAid=331396526)⠀
