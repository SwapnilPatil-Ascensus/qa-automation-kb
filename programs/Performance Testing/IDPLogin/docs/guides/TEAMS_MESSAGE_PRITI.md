# Copy/paste for Teams — Preeti

Hi Preeti — the **JMeter script is ready** with the 6 post-login banner/dashboard pages added. Here's what to do:

**Script location (in qa-automation-kb):**
`programs/Performance Testing/IDPLogin/scripts/jia-banner-post-login/idp-login-resources.jmx`

**Your steps:**
1. Copy the JMX to `performance-test-automation/.../jmeter/` (see DEPLOY.md in same folder)
2. Local smoke: 1 user, nyd — `QAPERFTEST_119527095` / `Newton@123`
3. Confirm all **15 steps** green (9 original + 6 new banner pages)
4. Run Jenkins on stage1 with current settings (25 users, 1h)
5. Then we'll do 50 users / 5 plans per Arun's request

**6 pages added** (after login, before logout):
- auth/customBannerMessage.cs, auth/sideBannerMessage.cs
- al/customBannerMessage.cs, ao/customBannerMessage.cs
- ao/overview.cs, al/list.cs

**YAML:** no change needed for Jenkins.

**Full handoff doc:** `PRITI_HANDOFF.md` in the IDPLogin folder.

Let me know when smoke passes!
