# Purpose: This feature file tests the Member Single Contribution process via CSR.
#         It includes scenarios for:
#         - Contributions using existing bank accounts.
#         - Contributions with new bank accounts.
#         - Contributions involving multiple funds or beneficiaries.
# Usage:
#     - Use the `Examples` table to specify test case names.
#     - Tags like `@regression`, `@smoke`, and `@functional` can be used to filter scenarios during execution.
#     - Ensure the required test data is loaded before running the tests.

Feature: Member Single Contribution via CSR

  Background:
    Given starting "login" URL for "csr"
    And load test cases
    And using browser
    And using unite database connection
    And set test case creator as swapnil.patil@ascensus.com

  @regression @smoke @functional
  Scenario Outline: Perform member single contribution for <test case name>
    When user logs in for <test case name>
    And user pulls account information for <test case name>
    And user jumps to member account with account number for <test case name>
    And user completes member contribution for <test case name>
    Then log and validate member contribution for <test case name>

    @dailyrun @smokerun
    Examples:
      | test case name               |
      | EBT - Existing Bank          |
      | EBT w/ New Bank - Savings    |
      | EBT - Multiple Beneficiaries |

    @functionalrun
    Examples:
      | test case name               |
      | EBT (3 Funds)                |
      | EBT - Multiple Beneficiaries |
