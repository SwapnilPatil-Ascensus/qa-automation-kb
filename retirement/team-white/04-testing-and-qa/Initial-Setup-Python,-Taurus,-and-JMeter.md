# Initial Setup: Python, Taurus, and JMeter

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396.aspx) | Created: 2025-03-20 | Last modified: 2025-04-04 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

Installation instructions as described in the following videos: [Performance Testing Videos](https://ascensus0.sharepoint.com/sites/QualityEngineeringCF/SitePages/QA-Performance-Testing-Videos-178520537.aspx).

Installation instructions from 2023 can also be found here: [Installing Taurus Locally](https://ascensus0.sharepoint.com/sites/QualityEngineeringCF/SitePages/QA-Installing-Taurus-Locally-97880756.aspx)

**Python Setup**

1. Download and install a version of Python before v3.12 (for example, [v3.11.9](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe))
  1. Note that if you are using Python v3.12+ you may encounter issues with *distutils*
2. During installation, check the option to "Add python.exe to PATH"
3. After installation has completed, open CMD and execute the following command to verify that the version that was just installed is the version that appears.  If you see a different version here, you will need to check your environment variables to remove any references to prior Python versions > python --version

**PIP Configuration**

1. Navigate to the following directory, and ensure that a folder named "pip" exists.  If it does not exist, create it.  > %appdata%\..\Roaming
2. Create/modify a file named "pip.ini" within the "pip" directory so that it contains the following contents: > [global]   > index-url = [http://devpi.ascensus.com/buildservice/ascensus](http://devpi.ascensus.com/buildservice/ascensus)   > trusted-host = [devpi.ascensus.com](http://devpi.ascensus.com)

**Setup Visual Studio Build Tools**

1. Open Visual Studio Installer
2. Verify that Visual Studio Build tools are installed.  If they are not installed, the continue below.
3. Click Modify on the version of Visual Studio that is installed
4. Check the option to include "Desktop development with C++" and click Modify to begin the download/installation process, then wait for it to complete.

**Taurus Setup**

1. Open CMD and enter the following command (Note that this may take some time to complete): > pip install bzt
2. Heads-up: Possible error: ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='[files.pythonhosted.org](http://files.pythonhosted.org)', port=443): Max retries exceeded with url: /packages/12/8c/7d47cfc0d04fd4e3639ec7e1c96c2561d5e890eb900de8f76eea75e0964a/lxml-5.3.1-cp311-cp311-win_amd64.whl.metadata (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1006)')))

Solution:

2.1 Try running CMD: pip install bzt --trusted-host [pypi.org](http://pypi.org) --trusted-host [pypi.python.org](http://pypi.python.org) --trusted-host [files.pythonhosted.org](http://files.pythonhosted.org)

2.2 pip install --upgrade certifi

2.3  if there are no errors, then repeat the command: pip install bzt

**JMeter Setup**

1. Download the latest version of JMeter (currently [v5.6.3](https://dlcdn.apache.org/jmeter/binaries/apache-jmeter-5.6.3.zip))
2. Extract the contents of the zip file into a known location, such as "C:\Tools"
3. Navigate to the following directory:  > %userprofile%
4. Create/modify a file named ".bzt-rc" so that it contains the following contents at a minimum (referencing the path used above): > modules:*jmeter:* *path: C:\Tools\apache-jmeter-5.6.3* Note that a base version of the file contents for the ".bzt-rc" file can be found [here](https://github.com/Blazemeter/taurus/blob/master/bzt/resources/base-bzt-rc.yml).  When using this base file, uncomment the lines above and modify them to match your jmeter path).
5. There are a set of plugins needed to properly run assertions against the responses from the API.  Extract these jar files into the "/lib/ext" within your jmeter path above: [jmeter-plugins.zip](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396/jmeter-plugins.zip?wtAid=315559969)
  1. Please see step 8 in the following confluence page for more information: [Installing Taurus Locally](https://ascensus0.sharepoint.com/sites/QualityEngineeringCF/SitePages/QA-Installing-Taurus-Locally-97880756.aspx)

**Validate Setup**

1. Save this file into a new directory, which contains the basic setup for a test against the GET Onboarding endpoint in DEV: > [get-onboarding.yaml](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Initial-Setup-Python,-Taurus,-and-JMeter-310459396/get-onboarding.yaml?wtAid=310459401)
2. Open CMD in the directory containing the yaml file above, and execute the following command to begin the test: > bzt get-onboarding.yaml

### [Initial Setup: Running Tests in Rancher](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Initial-Setup-Running-Tests-in-Rancher-315557114.aspx)
