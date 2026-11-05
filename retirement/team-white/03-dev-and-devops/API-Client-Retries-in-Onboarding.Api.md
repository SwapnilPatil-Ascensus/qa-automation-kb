# API Client Retries in Onboarding.Api

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-API-Client-Retries-in-Onboarding.Api-346550804.aspx) | Created: 2025-10-29 | Last modified: 2025-10-29 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

### Overview

API client retry behavior is centrally configured via the ApiClients section in Onboarding.Api/appsettings.json and consumed when named/typed HttpClients are registered. Retry logic is enforced through Polly policies.

#### Configuration Structure (appsettings.json)

##### ApiClients:

DefaultTimeoutInSeconds: (global fallback)
  EnableLogging: (global default)
  EnableRetryPolicy: (global default)
  Clients: [
    {
      "Name": "ChorusAPI",
      "TimeoutInSeconds": 90,
      "EnableRetryPolicy": true,
      "RetryOnTimeout": true,
      "RetryAttempts": 3,
      "RetryBackoffType": "Exponential",
      "RetryInitialDelay": 1,
      "RetryOnlyOnStatusCodes": [403]
    },
    {
      "Name": "OnboardingAPI",
      "EnableRetryPolicy": true,
      "RetryOnTimeout": true,
      "TimeoutInSeconds": 90,
      "RetryAttempts": 3,
      "RetryBackoffType": "Exponential",
      "RetryInitialDelay": 1
    }
    // (Additional clients similar shape)
  ]

Add a new client by inserting a new object into Clients with required retry parameters.  It will also need to be added to the [Onboarding library set in Octopus](https://octopus.ascensus.com/app#/Spaces-1/projects/onboarding-api/variables/library) and copied into appsettings.json for Onboarding.Api, Onboarding.Messaging.Api, and Onboarding.Workflow.Api.

##### Per-Client Option Properties (ApiClientOptions)

**Name:**

unique identifier for lookup.

**TimeoutInSeconds:**

base request timeout (seconds).

**EnableLogging:**

enable/disable logging override.

**LogOnlyHttpMethods:**

restrict logged verbs.

**EnableRetryPolicy:**

turn retries on/off for this client.

**RetryAttempts:**

max retry attempts (after the initial try).

**RetryBackoffType:**

Constant | Linear | Exponential (controls delay progression between attempts).

**RetryInitialDelay:**

starting delay (seconds) before first retry.

**RetryOnTimeout:**

include timeout failures in retry evaluation.
