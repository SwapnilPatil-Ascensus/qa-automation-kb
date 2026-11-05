# DocuSign Business Requirements

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/Team.Summit/SitePages/DocuSign-Business-Requirements.aspx) | Created: 2026-09-15 | Last modified: 2026-09-24 | Author:  | Last editor: 

---

![image](https://cdn.hubblecontent.osi.office.net/m365content/publish/2de80906-d5be-4982-ad75-eb05deedc15a/645958734_super.jpg)

MVP Requirements:

- SITES
  - PSG - need a branded site for Vanguard and another one for Ascensus, and Non-Branded. Each will have their own "from" email address. Rules for Non Branded templates TBD. Nikki Reichert is a contact for Non-Branded. Return emails required for Vanguard and Ascensus which are monitored. - Melinda to confirm.
  - RPS - they need a co-branded Stiffel site, and others will be Ascensus branded with a distinct from email and contact for each fin org. Every fin org has their own return email which are monitored.
  - From email addresses should be reused and only setup new if there is not a supported branded site.
- Communication
  - RPS - reminders for package signing events with X no. of days included in content including cc rules, reminders to vary by signature event process/rules
  - PSG - reminders for package signing events with X no. of days included in content including cc rules, reminders to vary by signature event process/rules
  - Should assess communication/email templates (400+) to determine if dynamic template content can be supported to reduce template counts.
- Esign Roles
  - PSG - want to add more Role types (meeting set up with Katie Bachman, Monica Stehr, Lynn L. and Kelly in early July to get this on Monica's list to add)
    - Currently have 9 role types of:
      - Broker (ESignRole Type 0)
      - Sponsor (1)
      - Limited Trustee (ESignRole Type 2/EmailAddress Type 4)
      - Limited Trustee Plus (ESignRole Type 3/EmailAddress Type 4)
      - TPA ((ESignRole Type 4/EmailAddress Type 5)
      - Related Employer ((ESignRole Type 5/EmailAddress Type 6)
      - Trustee (6)
      - Trustee Plus (7)
      - Insurance Company ((ESignRole Type 8/EmailAddress Type 3)
      - Custodian ((ESignRole Type 9/EmailAddress Type 2)
    - Will also ask about moving current roles to SalesForce - Need to confirm with Lori this requirement as emails are available in ARK email manager now where they were not previously
      - CC (Broker)
      - Custodian
      - Insurance Company
      - Limited Trustee
      - Other Plan Administrator
      - Related Employer
        - Table location: ProcessTrack..ESignEmailAddresses
    - Need to confirm signors/role types. @kelly to provide existing and group to review proposed list of added signors with email mapping as needed. Signor source should match what is leveraged by Sertifi today.
- Will we require a password for clients to access DocuSign?
  - Lori checking with other groups who have a DocuSign solution
    - Digital Onboarding: Only available to the user when in the "Unqork" experience, no password required
    - FuturePlan: Client is sent link, no password required. They do have the option at the end to create an account but they recommend to clients to not do so.
    - Confirmed with Eddie Hooper that no password is required to access their signature transaction
    - Need to confirm if requiring PW access can flex by partner/product. PSG PW for Sertifi is plan #. RPS would need to assess this requirement. Confirm what actions the recipient can take if no password is required (i.e. fwd, delegate signature, etc.)
    - Need to assess any terms and conditions offered through DocuSign and determine if any additional conditions should be added. No conditions required through Sertifi today.
- Signing order is not required. Technical assessment needed to determine if this can be removed without breaking existing processes.
  - Partner/Product level signor rules will need to be applied (maybe by template?)
- Deliver email to only those roles that are required and cc those that are non-signers (5MB is the limit for document size, anything larger will pass as weblink) If limits are exceeded by the external partner then the pkg will fail. Custom even logging/subscription required to track this.
- Would prefer if a user has more than one role (for example, sponsor and limited trustee), that they can sign in one experience.
- Certification document with signing details should be stored with the plan documents with associated meta data.

**Technical Considerations**

- Sertifi and DocuSign will need to be supported in tandem
- DocuSign needs to accommodate reprocessing (for corrections, expired links/transactions, etc). Will require workflow changes to listen to/complete events.
- Signor types and rules may need to be expanded, Signor order is not required for PAS events (need to confirm for onboarding)
- Signors are determined by email address (with opportunity assessment for in session links)
- Need to accommodate branding for signing experience, and communication templates
- Systematic reminders to sign needed
- Solution architecture should include framework which can be reused for “other” signature events outside of PAS
- Admin users should have access to events/status
- Separate PSG and RPS accounts will be required as the “from address” and other items varies
- Asynchronous signature events will be required

| <br> |  |  | <br> |
| --- | --- | --- | --- |
|  | <br> | <br> |  |
|  |  | <br> |  |
|  | <br> |  | <br> |
|  |  |  |  |
