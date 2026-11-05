# How to create a new test

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-to-create-a-new-test-315558307.aspx) | Created: 2025-04-02 | Last modified: 2025-04-16 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

Every test requires the execution of one or more scenarios, so the first step to creating a new test is ensuring that the proper scenario(s) have been created.

#### Add a new scenario in OnboardingScenarios.yaml

1. All scenarios are stored in OnboardingScenarios.yaml, which can be found in the root of Onboarding.Api/Test/Onboarding.Api.PerformanceTests
2. Copy an existing scenario to get started based on the method type of the new endpoint
3. The first thing to set is the name of the new scenario, which is how it will be referred to later on.
4. If the endpoint being tested requires any input parameters, they can be provided via a csv file which is loaded into the scenario by defining a data-source.
  1. See "Adding a new input file" below for more information
5. Update the URL to hit the endpoint that will be tested and set the appropriate method type as needed.
  1. Provide parameters from the input file in either the URL or in the request body
6. Add assertions against the data within the response
  1. At a minimum we should assert on the status code coming back in the response
  2. Additionally, if able, we should assert that the response contains the record that we requested by matching upon the input value(s)

#### Adding a new input file

1. Drop the input file in Data
2. Update the files in Settings to include the new path to the input file under a new FILEPATH variable
  1. Note that SettingsQa.yaml and SettingsQaViaKong.yaml will be used within the pod in rancher and will expect them to existing in the current running directory due to how they are stored in the Config Map
  2. Note that SettingsQaLocal.yaml and SettingsQaViaKongLocal.yaml are used when kicking of the test locally, and as a result they expect the file paths to be explicit based on the root directory of the performance tests
3. Update line 3 of the following files within the Templates directory to include the new data file via the "--from-file [PATH_TO_DATA_FILE]" argument:
  1. run-rancher-{env}.bat
  2. run-rancher-{env}-via-kong.bat
4. Note that the path to the input file should be relative to the directory of the test being executed.  In general this should be up two levels and into the Data folder

#### Create a new directory for the test

1. Once the scenarios needed by the tests have been created along with their supporting data files, a new test can be created against the scenarios by copying an existing test directory under Tests.  Here is a brief description of the contents within a test directory:
  1. run-local-{env}.bat
    1. This script is used to kick the tests off from your local PC against the internal service URL in the applicable environment
    2. *Note: This script is identical in all test directories, and is simply used to execute the core "run-local.bat" script that is found in the Templates directory from within the context of the current test*
  2. run-local-{env}-via-kong.bat
    1. This script is used to kick the tests off from your local PC against the external service URL in the applicable environment (routed through Kong).
    2. *Note: This script is identical in all test directories, and is simply used to execute the core "run-local-via-kong.bat" script that is found in the Templates directory from within the context of the current test*
  3. run-rancher-{env}.bat
    1. This script is used to deploy a pod to rancher to kick off the tests against the internal service URL n the applicable environment, and will also export the results into Blazemeter
    2. *Note: This script is identical in all test directories, and is simply used to execute the core "run-rancher.bat" script that is found in the Templates directory from within the context of the current test*
  4. run-rancher-{env}-via-kong.bat
    1. This script is used to deploy a pod to rancher to kick off the tests against the external service URLn the applicable environment (routed through Kong), and will also export the results into Blazemeter
    2. *Note: This script is identical in all test directories, and is simply used to execute the core "run-rancher-via-kong.bat" script that is found in the Templates directory from within the context of the current test*
  5. Blazemeter{env}.json
    1. This file is used when running the tests in rancher and it contains information that is used to export the test results into the appropriate project and test in Blazemeter
  6. Blazemeter{env}ViaKong.json
    1. This serves the same purpose as Blazemeter.json but is specifically used by the tests routed through Kong so the results can be differentiated
  7. PerformanceTest.yaml
    1. This file declares the execution parameters around which scenarios are to be executed
  8. PerformanceTestViaKong.yaml
    1. This is essentially identical to PerformanceTest.yaml with an additional scenario prepended to the front to obtain the access token that will be used for the requests sent through Kong
2. Update Blazemeter{env}.json and Blazemeter{env}ViaKong.json to declare the test that is being executed
  1. Be sure to prepend the title of the test with the environment that it is being executed against
  2. For Blazemeter{env}ViaKong.json, we've been using the same title but with an included tag distinguishing the test as being routed through Kong
3. Update PerformanceTest.yaml
  1. Set the execution parameters around which scenario will be executed
4. Update PerformanceTestViaKong.yaml
  1. Update the name of the execution scenario and further define it in the "scenarios" section at the bottom of the file.
  2. In general, for a single endpoint this will first call the GetAccessToken scenario to obtain an authorization token, and will then call the scenario being tested in PerformanceTest.yaml
  3. *Note: The name of the scenario used in the execution step(s) should be the same name that is declared in the scenarios section below it.  You are really defining a new scenario here, which is just a combination of existing scenarios from OnboardingScenarios.yaml*

#### Example

Please see the following commit for an example of adding a new test, which includes everything mentioned above:

[https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding/commit/0e6676ac86a6776d5d9d4211621f164367781128?refName=refs%2Fheads%2F669565_OnboardingApi_PerformanceTesting_PoC](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/Onboarding/commit/0e6676ac86a6776d5d9d4211621f164367781128?refName=refs/heads/669565_OnboardingApi_PerformanceTesting_PoC)
