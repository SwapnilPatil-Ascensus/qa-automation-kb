-- Step 07: POST /enrollments/enrollment/owner-address-entered
-- Downstream: unite-profile → CloudOwnerService.verifyOwnerAddress()
-- Tables: TU_USPS_ADDRESS_INFO (zip → state cross-check)

-- ---------------------------------------------------------------------------
-- 1) Validate zip maps to expected state (owner mailing address)
-- Source: UspsAddressInfoTable ORM findByCriteria on TU_USPS_ADDRESS_INFO
-- ---------------------------------------------------------------------------
SELECT u.zipcode,
       u.city,
       u.state,
       u.county
FROM tu_usps_address_info u
WHERE u.ctl_rec_stat = 'A'
  AND u.zipcode = '02459';   -- bind :zipcode (first 5 digits)

-- ---------------------------------------------------------------------------
-- 2) Find valid zip/state pairs for test data (pick any active row)
-- ---------------------------------------------------------------------------
SELECT u.zipcode,
       u.city,
       u.state
FROM tu_usps_address_info u
WHERE u.ctl_rec_stat = 'A'
  AND u.state = 'MA'
  AND ROWNUM <= 10
ORDER BY u.zipcode;

-- Default test data (matches Postman env):
--   mlAddline1 / permAddline1 = '95 Wells Ave'
--   mlCity / permCity         = 'Newton'
--   mlZipcode / permZipcode   = '02459'
--   mlStatelabel / permStatelabel = 'MA'
--   isForeignAddress / isForeignPermaddr = 'N'
