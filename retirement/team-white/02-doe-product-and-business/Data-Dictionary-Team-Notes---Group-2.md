# Data Dictionary: Team Notes - Group 2

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Data-Dictionary-Team-Notes---Group-2-336401374.aspx) | Created: 2025-08-04 | Last modified: 2025-08-04 | Author: Max Shakirov | Last editor: Max Shakirov

---

### Additional fields

Here is a list of additional data dictionary fields that you may not find in original data dictionary for Group 2 - some of thee fields are having functional purpose within Onboarding it-self rather than being data value associated with plan or sponsor:

| **Field** | **Value** | **Description** |
| --- | --- | --- |
| _collectionItemId | Random GUID | <br>This field is auto-assigned to any JSON collection that contain a secure field such as "participantSSN" in "participants" collection. It's used primarily to precisely identify secure record in order to interact with it editing and delete wise.<br> |
| preOnboardingComplete | Boolean (true/false) | <br>false -  Sponsor is not finished uploading prior rk info<br>true - Sponsor is completed uploading prior rk info<br> |
| internalTransferWorkflowComplete | Boolean (true/false) | <br>false - sponsor sits back and waits<br>true - sponsor gest started to review / sign<br> |
