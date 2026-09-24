# Enrollment — AI-assisted scenario guide

**QA-893 / QA-2046**

Use Cursor (or another approved AI) to add a **new Enrollment TestNG case from an existing wizard step**. Human review is mandatory. Secrets never go in prompts or Git.

## Pattern to copy

1. Pick a neighbor class (example: `OwnerEnteredTests` → new `OwnerAddressEnteredRequestTest`).
2. Same package, extend `EnrollmentBaseTest`.
3. Same groups as siblings (`integration`, `regression` unless smoke-only `functional`).
4. Encrypted POST if the API requires it.
5. Wire the class in **all three** suite XMLs if it belongs on CI (smoke / regression / integration). nmdirect only in localhost example until CI story lands.

## Prompt skeleton (paste in Cursor on `api-test-automation`)

```
Add a TestNG class for POST {path} in mobile/enrollment.
Clone the structure of {ExistingClass}. Do not change jsonapi-core.
Do not log JWT, SSN, or passwords. Do not commit host properties.
Add the class to enrollment-regression-testng.xml and enrollment-integration-testng.xml
for okdirect and newyork only.
```

Attach the Postman request **with secrets stripped**, or the payload from `msc-enrollment/postman/payloads/plain/` (plain JSON, not production data).

## Human review (required)

- [ ] Request matches Postman/Excel path and method
- [ ] Assertions are lean (status + key fields), not a full dump of PII
- [ ] No SkipException hiding a real 500
- [ ] Local run once on Stage1 or QC4
- [ ] MR reviewed by someone other than the prompt author (QA-2047 spirit)

## Forbidden in AI output

Credentials, `.properties` with passwords, raw `Authorization` headers, production SSNs, `git add .`, pushes without asking.
