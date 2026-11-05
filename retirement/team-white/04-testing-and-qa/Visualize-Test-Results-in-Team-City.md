# Visualize Test Results in Team City

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Visualize-Test-Results-in-Team-City-305971939.aspx) | Created: 2025-02-20 | Last modified: 2025-02-20 | Author: Federico Pizzaro | Last editor: Federico Pizzaro

---

In order to properly visualize the results of a test run that is executed as part of a build in Team City you need to add some additional configuration:

#### **Add TeamCity.VSTest.TestAdapter Package**

This package provides the TeamCity integration with test frameworks via the Visual Studio Test Platform or VSTest IDE tools.

This package should be added to the test projects ONLY.

You can find the Package Official Page [here](https://github.com/jetbrains/TeamCity.VSTest.TestAdapter).

You can find the Nuget Package Info [here](https://www.nuget.org/packages/TeamCity.VSTest.TestAdapter).

dotnet add package TeamCity.VSTest.TestAdapter --version 1.0.41

#### **Docker Container Support: Add Team City Environment Variable**

To run tests from within a Docker container that is hosted on a machine running the TeamCity agent, the container must have a `TEAMCITY_PROJECT_NAME` or `TEAMCITY_VERSION` environment variable set.

Update the docker file to include an environment variable named "TEAMCITY_PROJECT_NAME" and whose value matches the application name.

Example:

ENV TEAMCITY_PROJECT_NAME=$APPLICATION

You can find example docker files in [this folder](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Api/Build).

#### **Configure the dotnet test command in the Docker file**

The `dotnet test` command is used to execute unit tests in a given solution. The `dotnet test` command builds the solution and runs a test host application for each test project in the solution using `VSTest`.
If all tests are successful, the test runner returns 0 as an exit code; otherwise if any test fails, it returns 1.

The key part of this command execution is to properly configure the command arguments, other configurations different from the ones provided next as example are not guaranteed to successfully display the test results in TeamCity.

Basically, the "logger" argument should not be provided and the verbosity argument must be kept as "normal"

To run test from multiple test projects that belong to the same solution use a command like this:

RUN find $APPLICATION/Test -name  *UnitTest.csproj | xargs -I '{}'  dotnet test --configuration=$BUILD_CONFIGURATION  --verbosity=normal  --no-build  /p:Version=$BUILD_NUMBER  /p:CollectCoverage=true  /p:CoverletOutputFormat=teamcity   '{}'

To run tests from a single test project use a command like this:

RUN dotnet test $APPLICATION/Test/$APPLICATION.AutomationTest/$APPLICATION.AutomationTest.csproj --configuration=Release  --verbosity=normal  --no-build  /p:Version=$BUILD_NUMBER

You can find examples in [this folder](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding?path=/Onboarding.Api/Build).

You can find the dot net test cmd documentation [here](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test?tabs=dotnet-test-with-vstest).

#### **Visualize Test Results in Team City**

If everything works as expected you should see a test execution summary next to the build number and branch name:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Visualize-Test-Results-in-Team-City-305971939/image-2025-2-20_10-25-57.png)

In addition to that you should see a Test tab in the build details page:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Visualize-Test-Results-in-Team-City-305971939/image-2025-2-20_10-33-9.png)
