# ags-automation - taurus

## Description
Run HTML based load testing for IDP Login with blazemeter reporting

## Coverage
9/3/25 - Created flow for local and grid executions

## Script Creation
1a. General lighthouse script creation can be done through the Blazemeter chrome extension (save as YAML or PYTHON file)
1b. Recommended to use python scripts as it provides more control of data (especially generation) and browser interaction
1c. NOTE: Running a YAML file with embedded Ariritif script will create a python script in the test directory
2. Blazemeter demo: https://www.blazemeter.com/media/1652

## Installation
1. Follow installation instructions for Taurus on: https://gettaurus.org/install/Installation/
2. Download the necessary chrome driver for your installed browser version
2a. Execute with chrome browser version to find latest driver: https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_<major version>
2b. Download driver by adding version into: https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/<driver version>/win64/chromedriver-win64.zip

## Documentation
Scripts are currently written in Apiritif - https://gettaurus.org/docs/Apiritif/

## Execution
Note: Do not use cygwin (use command prompt)
1. Run: bzt <script>
2. Example: bzt Blazemeter-Login-Local.yaml

##Local File Settings
1. SSL-CERT has been turned off due to issues during execution
2. [Local] Chromedriver path/version is set in order to guarantee correct driver to browser versioning
3. [Grid] REMOTE controls the URL to the selenium grid
4. CONCURRENCY controls the number of users
5. ITERATIONS controls the number of times scenario should be run
6. DATA-SOURCES controls the loading of the data CSV file
