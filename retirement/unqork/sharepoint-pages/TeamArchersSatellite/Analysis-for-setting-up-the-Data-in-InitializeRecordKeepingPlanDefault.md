# Analysis for setting up the Data in InitializeRecordKeepingPlanDefaults (Step3) For Drawdowns and Moneytypes

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/TeamArchersSatellite/SitePages/TARC-Analysis-for-setting-up-the-Data-in-InitializeRecordKeepingPlanDefaults-(Step3)-For-Drawdowns-and-Moneytypes-367362673.aspx) | Created: 2026-01-27 | Last modified: 2026-02-24 | Author:  | Last editor: 

---

##### Overview

This page provides detailed information about **Money Types**  and **Drawdowns**  that are typically **defaulted in Step 3 (`InitializeRecordKeepingPlanDefaults` endpoint)** . Developers should refer to this documentation when configuring Step 3 default data for any **new offering key** . Doing so will help **prevent duplicate entries**  in Step 4.

The Money Types and Drawdowns listed here represent the **current default set**  for the existing offering key.

Please note:

- Any Money Type or Drawdown derived from **Unqork properties**  will **not**  be configured in Step 3.

#####

##### SQL Scripts Location

The default data for Step 3 is stored in SQL scripts located at:
`Onboarding.Setup.Plan/Source/Onboarding.Setup.Plan/SQL Script/Plan Defaults Data Setup/`

##### Group Plan (Plan4Most)

Money Types -

| Money Type Number | Money Type Name |
| --- | --- |
| 1 | EMPLOYER PROFIT SHARING |
| 3 | EMPLOYEE 401(K) |
| 4 | EMPLOYEE ROLLOVER |
| 33 | EMPLOYEE RELATED ROLLOVER |
| 11 | QUALIFIED NON-ELECTIVE CONTRIB |
| 44 | EE ROLVER QP AT |
| 54 | EMPLOYEE ROLLOVER IRA |
| 64 | EMPLOYEE ROLLOVER 403(B) |
| 74 | EMPLOYEE ROLLOVER 457(B) |
| 84 | EMPLOYEE ROLLOVER 403(A) P/T |
| 94 | EMPLOYEE ROLLOVER 403(A) A/T |

Drawdowns -

| Drawdown Number | DrawdownName |
| --- | --- |
| 1 | TOTAL PAYOUT |
| 3 | PARTIAL PAYOUT |
| 6 | RMD W/ ROTH |
| 17 | DISABILITY |
| 19 | QUAL RESERVIST |
| 28 | DEEMED SEVERANC |
| 35 | DISTRI FEE |
| <br> | <br> |
| <br> | <br> |
| <br> | <br> |
| 66 | RMD NON-ROTH |
| <br>71<br>72<br> | <br>MISC EXPED FEE<br>HS EXPED FEE<br> |
| 73 | TERM EXPED FEE |
| 75 | PARTIAL EXP FEE |

##### IK(Plan4One)

Money Types -

| Money Type Number | Money Type Name |
| --- | --- |
| 1 | EMPLOYER PROFIT SHARING |
| 3 | EMPLOYEE 401(K) |
| 4 | EMPLOYEE ROLLOVER |
| 20 | EMPLOYEE ROTH 401(K) DEFERRAL |
| 34 | EMPLOYEE ROTH 401(K) ROLLOVER |

Drawdowns-

| Drawdown Number | DrawdownName |
| --- | --- |
| 1 | TOTAL PAYOUT |
| 2 | HARDSHIP |
| 3 | PARTIAL PAYOUT |
| 4 | LOAN |
| 5 | 59.5 DISTRIB |
| 6 | 70.5 DISTRIB |
| 7 | IN-SERVICE WITH |
| 12 | LOAN MODULE |
| 13 | NRA |
| 17 | DISABILITY |
| 19 | QUAL RESERVIST |
| 28 | DEEMED SEVERANC |
| 35 | DISTRIB FEE |
| 66 | RMD NON-ROTH |
| 71 | MISC EXPED FEE |
| 72 | HS EXPED FEE |
| 73 | TERM EXPED FEE |
| 74 | INSVC EXPED FEE |
