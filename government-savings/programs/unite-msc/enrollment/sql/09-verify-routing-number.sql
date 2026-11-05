-- Step 09: POST /enrollmentapi/v1/verify/routingnumber
-- Downstream: unite-bank → BankInfoService.postBankInfoVerify()
-- Source: BankInfoTableDao.getBankInfo
-- Table: TU_BNK_INFO

-- ---------------------------------------------------------------------------
-- 1) Verify routing number exists (returns bank name for test data)
-- ---------------------------------------------------------------------------
SELECT b.routing_num  AS routing_number,
       b.bnk_name     AS bank_name,
       b.city,
       b.state,
       b.zipcode
FROM tu_bnk_info b
WHERE b.ctl_rec_stat = 'A'
  AND b.routing_num = '071000013';   -- bind :routing_number

-- ---------------------------------------------------------------------------
-- 2) Pick any valid routing number for test data
-- ---------------------------------------------------------------------------
SELECT b.routing_num,
       b.bnk_name
FROM tu_bnk_info b
WHERE b.ctl_rec_stat = 'A'
  AND ROWNUM <= 20
ORDER BY b.routing_num;

-- Default test data (Postman env):
--   enrollment.bank.routing = '071000013'  (Chase)
--   enrollment.bank.name    = 'Chase'
--   enrollment.bank.account = '654321'
--   enrollment.bank.accountType = 'S' (savings) or 'C' (checking)
