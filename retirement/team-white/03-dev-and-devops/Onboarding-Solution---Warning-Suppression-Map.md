# Onboarding Solution - Warning Suppression Map

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Onboarding-Solution---Warning-Suppression-Map-310455226.aspx) | Created: 2025-03-15 | Last modified: 2025-03-15 | Author: Max Shakirov | Last editor: Max Shakirov

---

#### Finding warning code description

To find and understand C# compiler warnings by their index (e.g., CS1658), you can refer to the [Microsoft Learn documentation](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-messages/) or use the Visual Studio IDE's built-in features to navigate to the relevant documentation for a specific warning code.

#### I still see suppressed warnings in my Visual Studio IDE

Although suppression capabilities exist at various levels of solution (i.e. solution vs project vs in-code suppression), please note that some particular warnings may not be explicitly suppressed. You could also occasionally see warnings that should be suppressed, but they aren't - there seems to be a consistency issue with this when it comes to Visual Studio and compiling project in general. The best way to tackle this is to remove a source for warning in a first place.

Please note that compilers do evolve too, hence you'd most likely to see a lot of warnings when copying code from old project to new one. In this case, try to resolve such warnings as much as possible before your first PR. This is especially dangerous when old and new projects don't share the same framework behind the scenes.

#### Current Map

| **Namespace** | **Project** | **Suppressed Warnings** |
| --- | --- | --- |
| Onboarding | Onboarding.Data | 1701;1702 |
| Onbarding.Api | Onbarding.Api | 1701;1702 |
| <br> | Onboarding.Api.Contract | 1701;1702 |
| <br> | Onboarding.Api.Domain | 1701;1702;8601;8602;8603;8604; |
| <br> | Onboarding.Api.Domain.Contract | 1701;1702 |
| <br> | Onboarding.Api.ServiceClient | 1701;1702 |
| Onboarding.Setup.Plan | Onboarding.Setup.Plan | 1701;1702;1591;0169; |
| Onboarding.Workflow.Api | Onboarding.Workflow.Api | 1701;1702 |
| <br> | Onboarding.Workflow.Api.Contract | 1701;1702 |
| <br> | Onboarding.Workflow.Api.Domain | 1701;1702 |
| <br> | Onboarding.Workflow.Api.Domain.Contract | 1701;1702 |
| <br> | Onboarding.Workflow.Api.ServiceClient | 1701;1702 |
| Sales.Api | Sales.Api | 1701;1702 |
| <br> | Sales.Api.Contract | 1701;1702 |
| <br> | Sales.Api.Domain | 1701;1702 |
| <br> | Sales.Api.Domain.Contract | 1701;1702 |
| Shared | Infrastructure.Framework.Exceptions | 1701;1702 |
| <br> | Onboarding.Api.Shared | 1701;1702 |
| <br> | Onboarding.Features | 1701;1702 |
| Onboarding.Api.Tests | Onboarding.Api.AutomationTest | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
| <br> | Onboarding.Api.Domain.UnitTest | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
| <br> | Onboarding.Api.UnitTest | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
| Onboarding.Setup.Plan.Test | Onboarding.Setup.Plan.AutomationTests | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
| <br> | Onboarding.Setup.Plan.IntegrationTest | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
| <br> | Onboarding.Setup.Plan.UnitTest | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
| Onboarding.UI.Tests | Onboarding.UI.AutomationTests | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
| Onboarding.Workflow.Api.Tests | Onboarding.Workflow.Api.AutomationTest | 1701;1702 |
| <br> | Onboarding.Workflow.Api.Domain.UnitTest | 1701;1702 |
| Shared.Tests | Infrastructure.Framework.Exceptions.UnitTest | 1701;1702;0108;0114;1998;0649;4014;8601;8602;8603;8604;8618;8625; |
