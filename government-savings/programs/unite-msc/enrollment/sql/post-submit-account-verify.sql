-- Post-submit: verify account was created (ONLY SQL check during enrollment test)
-- Downstream: unite-account → CreateAccountService (INSERT at review-confirm)
-- Tables: TU_ACCT, TU_MEMBER, TA_LOGIN, TA_APP_CONTEXT, TU_TRAUNCH
-- Pattern: mobile/mobile1/sql/mobile.sql → get.mobile.auth.user (QAAUTOTEST%)

-- ---------------------------------------------------------------------------
-- 1) Find account by enrollment username (primary post-submit check)
-- ---------------------------------------------------------------------------
SELECT l.username,
       t.branding,
       a.uii_acct_id || a.uii_acct_ext AS account_id,
       m.uii_member_id,
       m.email,
       a.ctl_ins_dttm AS account_created
FROM tu_acct a
INNER JOIN tu_member m ON a.uii_member_id = m.uii_member_id
INNER JOIN ta_app_context ac ON m.uii_member_id = ac.app_member_id
INNER JOIN ta_login l ON ac.login_id = l.login_id
INNER JOIN tu_traunch t ON t.traunch_id = a.traunch_id
WHERE l.ctl_rec_stat = 'A'
  AND ac.active = 'Y'
  AND UPPER(l.username) = UPPER('QAAUTOTEST_ENR_20260804_100830_427')  -- bind :username
  AND UPPER(t.branding) = UPPER('hawaii');                               -- bind :branding

-- Assert: exactly 1 row returned after successful review-confirm-entered

-- ---------------------------------------------------------------------------
-- 2) Find any QAAUTOTEST enrollment account by branding (mobile1 pattern)
-- ---------------------------------------------------------------------------
SELECT l.username,
       'Test@123' AS password,
       a.uii_acct_id || a.uii_acct_ext AS account_id,
       m.uii_member_id,
       m.email AS user_email
FROM tu_acct a
INNER JOIN tu_member m ON a.uii_member_id = m.uii_member_id
INNER JOIN ta_app_context ac ON m.uii_member_id = ac.app_member_id
INNER JOIN ta_login l ON ac.login_id = l.login_id
INNER JOIN tu_traunch t ON t.traunch_id = a.traunch_id
WHERE UPPER(l.username) LIKE 'QAAUTOTEST_ENR%'
  AND UPPER(t.branding) = UPPER('hawaii')
ORDER BY a.ctl_ins_dttm DESC
FETCH FIRST 10 ROWS ONLY;

-- ---------------------------------------------------------------------------
-- 3) Verify login exists for created account
-- ---------------------------------------------------------------------------
SELECT l.username,
       l.traunch_id,
       l.ctl_ins_dttm
FROM ta_login l
WHERE l.ctl_rec_stat = 'A'
  AND UPPER(l.username) = UPPER('QAAUTOTEST_ENR_20260804_100830_427');
