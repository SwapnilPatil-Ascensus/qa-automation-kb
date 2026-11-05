# Open Telemetry - In Service Use

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Open-Telemetry---In-Service-Use-315561243.aspx) | Created: 2025-04-07 | Last modified: 2025-04-08 | Author: Max Shakirov | Last editor: Max Shakirov

---

### Shared Onboarding Instrumentation Set

- Http Client Instrumentation - for more details go to [GitHub link here](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/tree/main/src/OpenTelemetry.Instrumentation.Http).
- Entity Framework Core - for more details go to [GitHub link here](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/tree/main/src/OpenTelemetry.Instrumentation.EntityFrameworkCore).
- Asp .Net Core - for more details go to [GitHub link here](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/tree/main/src/OpenTelemetry.Instrumentation.AspNetCore).
- Mass Transit - this instrumentation comes in as part of main MassTransit nuget package.

Each instrumentation is enriched with error details, client IP address, db command and text where applicable/possible. Also, we are having few filters in-place to remove open telemetry for certain endpoints, such as /swagger and /healthcheck.

### Configuration

Open telemetry is configured and used with the help of several critical components within Onboarding project:

- Shared
  - Open Telemetry service configuration  - it could be located here, \Onboarding\Shared\Source\Onboarding.Api.Shared\Configuration\OpenTelemetryConfiguration.cs. Its main purpose is to add Open Telemetry, as a configuration, to any service that needs to be traced within Onboarding project. In order to use this shared configuration, just add a following code to your Program.cs:   *🚧 Nested Code Block macro 1️⃣ moved below*
  - Open Telemetry dispatch proxy decorator - it could be located here, \Onboarding\Shared\Source\Onboarding.Api.Shared\Tracing\TraceWithOpenTelemetryDecoratorDispatchProxy.cs. This proxy allows Open Telemetry activity injection without a need to change original code. It should be used and applied to every interface that you'd like to trace activity wise as its own span in order to get very detailed trace report. In order to use this decorator, just follow a similar approach depicted in a sample below:   *🚧 Nested Code Block macro 2️⃣ moved below*
  - [TraceParameterWithOpenTelemetry] attribute - new method parameter attribute that allows developers to explicitly denote whether method attribute is traced or not via Open Telemetry. Here is an example of usage:   *🚧 Nested Code Block macro 3️⃣ moved below* | **❗ Method parameter tracing guidelines** | | --- | | <br>While tracing parameters for a certain call, be mindful that some of them could contain PII information and should not be exposed for tracing. Hence, as a rule, you should not expose parameters (explicitly) for tracing that contain JSON object, any personal information etc. Implicitly there is a check in the code to hide these by default, but with use of **[TraceParameterWithOpenTelemetry]**  attribute you might expose these values by accident. You should use **[TraceParameterWithOpenTelemetry] attribute** as "IsEnabled = true" in cases when you have a scalar value parameter that's safe to expose, or as "IsEnabled = false" in case if certain parameter might contain PII related value and you want to hide its value in tracing.<br> |
- Service specific
  - appsettings.json - each service where Open Telemetry is required should have a following configuration in-place, where "Endpoint" is an address for a collector that gathers Open Telemetry (i.e. Jaeger sidecar - typically, for Jaeger specifically, address depicted below should be same across all Ascensus environments, consult your DevOps team on this if needed) and "Enabled" is a flag that controls whether Open Telemetry should be gathered or not in case if you don't have collector installed, or you want to disable Open Telemetry for any other reason   *🚧 Nested Code Block macro 4️⃣ moved below*

*🚧 Nested Code Block macro 1️⃣ moved here:*

builder.Services.AddOpenTelemetryConfiguration(builder.Configuration,builder.Environment.ApplicationName);

*🚧 Nested Code Block macro 2️⃣ moved here:*

services.AddScoped<IOnboardingsManager, OnboardingsManager>();services.DecorateWithDispatchProxy<IOnboardingsManager, TraceWithOpenTelemetryDecoratorDispatchProxy<IOnboardingsManager>>();

*🚧 Nested Code Block macro 3️⃣ moved here:*

/* 🚧 Macro Title: %5B;TraceParameterWithOpenTelemetry%5D; attribute usage */ public async Task<PlanAdvisor?> GetPlanAdvisor(%5B;TraceParameterWithOpenTelemetry(IsEnabled = true)%5D; string crd)

*🚧 Nested Code Block macro 4️⃣ moved here:*

/* 🚧 Macro Title: Open Telemetry config in appsettings.json */ "OpenTelemetrySettings": {     "Endpoint": "http://localhost:4317",     "Enabled": false }
