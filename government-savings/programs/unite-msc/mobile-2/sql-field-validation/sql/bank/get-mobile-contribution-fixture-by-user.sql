-- ============================================================================
-- Query: get-mobile-contribution-fixture-by-user
-- Feature: mobilecontribution
-- BFF Endpoints (path params on GET / PUT / DELETE only; POST has no {id}):
--   GET    /mobile2api/v1/mobilecontribution/{ext}/{id}
--   PUT    /mobile2api/v1/mobilecontribution/{ext}/{id}
--   DELETE /mobile2api/v1/mobilecontribution/{ext}/{id}
-- Downstream: GET bankapi/v1/bankInstructions/{ext}/{id}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\
--   unite-mobile2/.../MobileContributionService.getMobileRecurringContributionByExtAndId
--   unite-mobile2/.../BankGateway.getBankInstructionsByExtAndId
--   unite-bank/.../BankInstructionService.getBankInstructionsById
--   unite-bank/.../BankInstruction.java (@BeanPropertyMapper id ← seqPayId)
-- DB tables: tu_acct, tu_member, ta_app_context, ta_login, tu_traunch,
--            tu_bank, tu_bnk_instruction
-- Parameters: ? = rowNumber (same index as get.mobile.auth.user / setTestUser),
--             $$branding$$ = test branding shortcode
-- Returns: accountExt, apiContributionId
--
-- ID SEMANTICS (read before using results):
--   API path {id}  = JSON RecurringContribution.id
--                  = BankInstruction.id (domain)
--                  = tu_bnk_instruction.seq_pay_id
--   NOT path {id}: tu_bank.seq_bnk_id (JSON bnkId), tu_acct.seq_acct_id,
--                  transaction YTD / contribution-summary totals
--   Product docs call this "contribution id"; persistence is bank instruction pay id.
--   Legacy Cucumber: bankWorld.getBankInstructions()[0].getId() → same value.
--
-- {ext} = tu_acct.uii_acct_ext for an account the member owns; instruction must
--         be on that account (bi.seq_acct_id = a.seq_acct_id).
--
-- PREFERRED automation order:
--   1. Authenticate (get.mobile.auth.user → setTestUser)
--   2. API discovery: GET mobileactivity/{ext} → recurringContribution[].id
--      OR GET mobilecontribution/{ext}/{candidateId} until 200
--   3. DB query below to validate / seed-check ext + id for same member
-- ============================================================================

SELECT
    account_ext        AS accountExt,
    api_contribution_id AS apiContributionId
FROM (
    SELECT
        a.uii_acct_ext                 AS account_ext,
        TO_CHAR(bi.seq_pay_id)         AS api_contribution_id,
        bi.seq_bnk_id                  AS seq_bnk_id,
        bi.seq_acct_id                 AS seq_acct_id,
        bi.payment_type                AS payment_type,
        ROW_NUMBER() OVER (
            ORDER BY
                CASE WHEN a.seq_acct_id = auth_user.seq_acct_id THEN 0 ELSE 1 END,
                bi.seq_pay_id DESC
        ) AS pick_rank
    FROM (
        SELECT
            a.seq_acct_id,
            a.uii_member_id,
            a.uii_acct_ext,
            ROW_NUMBER() OVER (
                ORDER BY
                    a.ctl_ins_dttm DESC,
                    l.username ASC,
                    a.uii_acct_id DESC
            ) AS row_number
        FROM tu_acct a
        INNER JOIN tu_member m
            ON a.uii_member_id = m.uii_member_id
        INNER JOIN ta_app_context ac
            ON m.uii_member_id = ac.app_member_id
        INNER JOIN ta_login l
            ON ac.login_id = l.login_id
        INNER JOIN tu_traunch t
            ON t.traunch_id = a.traunch_id
        WHERE UPPER(l.username) LIKE 'QAAUTOTEST%'
          AND m.twofactor_optin = 'S'
          AND t.branding = '$$branding$$'
          AND a.ctl_rec_stat = 'A'
    ) auth_user
    INNER JOIN tu_acct a
        ON a.uii_member_id = auth_user.uii_member_id
       AND a.ctl_rec_stat = 'A'
    INNER JOIN tu_bnk_instruction bi
        ON bi.seq_acct_id = a.seq_acct_id
    INNER JOIN tu_bank b
        ON b.seq_bnk_id = bi.seq_bnk_id
       AND b.uii_member_id = auth_user.uii_member_id
    WHERE auth_user.row_number = ?
      AND bi.status = 'A'
      AND bi.ctl_rec_stat = 'A'
      AND bi.payment_type = 'P'
      AND b.status = 'G'
      AND b.ctl_rec_stat = 'A'
)
WHERE pick_rank = 1;

-- ============================================================================
-- Verification: confirm a candidate path id matches DB + member (manual)
-- Replace literals: branding, username, path id, ext
-- ============================================================================
/*
SELECT
    l.username,
    t.branding,
    a.uii_acct_ext          AS account_ext,
    bi.seq_pay_id           AS api_contribution_id,
    bi.seq_bnk_id           AS bnk_id_not_path_id,
    bi.seq_acct_id,
    bi.payment_type,
    bi.status               AS instr_status,
    b.status                AS bank_status
FROM tu_bnk_instruction bi
JOIN tu_acct a       ON a.seq_acct_id = bi.seq_acct_id
JOIN tu_bank b       ON b.seq_bnk_id = bi.seq_bnk_id
JOIN tu_member m     ON m.uii_member_id = a.uii_member_id
JOIN ta_app_context ac ON ac.app_member_id = m.uii_member_id
JOIN ta_login l      ON l.login_id = ac.login_id
JOIN tu_traunch t    ON t.traunch_id = a.traunch_id
WHERE t.branding = 'okdirect'
  AND l.username = 'QAAUTOTEST...'
  AND a.uii_acct_ext = '01'
  AND bi.seq_pay_id = 472560;
*/
