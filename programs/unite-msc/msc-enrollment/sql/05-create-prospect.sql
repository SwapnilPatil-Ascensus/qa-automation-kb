-- Step 05: POST /enrollmentapi/v1/enrollments/prospects
-- Downstream:
--   unite-metadata  → plan validation (TU_TRAUNCH) — see 00-shared-plan-branding.sql
--   unite-account   → MemberService.validateProspect() — username + fraud checks
--   unite-auth      → ProspectSessionService — NO SQL (JWT from SHA512 hash)
-- Tables: TA_LOGIN, TA_APP_CONTEXT, TU_MEMBER, TU_FRAUD_BLOCK_INFO, TU_TRAUNCH

-- ---------------------------------------------------------------------------
-- 1) Check username availability (must return 0 rows for new enrollment)
-- Source: LoginTableDao.getMemberLogins
-- ---------------------------------------------------------------------------
SELECT l.username,
       l.traunch_id,
       m.uii_member_id
FROM ta_login l
INNER JOIN ta_app_context ac ON ac.login_id = l.login_id AND ac.active = 'Y'
INNER JOIN tu_member m ON m.uii_member_id = ac.app_member_id
WHERE l.ctl_rec_stat = 'A'
  AND m.web_registered = 'Y'
  AND l.traunch_id = (
      SELECT t.traunch_id
      FROM tu_traunch t
      WHERE t.ctl_rec_stat = 'A'
        AND UPPER(t.branding) = UPPER('hawaii')
  )
  AND UPPER(l.username) = UPPER('QAAUTOTEST_ENR_20260804_100830_427');  -- bind :username

-- ---------------------------------------------------------------------------
-- 2) Check email not fraud-blocked (must return 0 rows)
-- Source: FraudBlockInfoTableDao.findByEmail
-- ---------------------------------------------------------------------------
SELECT f.seq_fraud_block_info_id,
       f.email,
       f.permanent_flag,
       f.temp_block_flag
FROM tu_fraud_block_info f
WHERE f.ctl_rec_stat IN ('A', 'R')
  AND (f.permanent_flag = 'Y'
       OR (f.temp_block_flag = 'Y' AND f.temp_block_endtime > SYSDATE))
  AND UPPER(f.email) = UPPER('qaa.enr.20260804_100830_427@example.com');  -- bind :email

-- ---------------------------------------------------------------------------
-- 3) Traunch ID for prospect plan (maps to account.planId at submit)
-- ---------------------------------------------------------------------------
SELECT t.traunch_id AS plan_deprecated_id,
       t.branding   AS plan_id
FROM tu_traunch t
WHERE t.ctl_rec_stat = 'A'
  AND t.allow_enrollments = 'Y'
  AND UPPER(t.branding) = UPPER('hawaii');

-- NOTE: usernameHash = Base64(SHA-512(username)) — computed in test data builder, not from DB
