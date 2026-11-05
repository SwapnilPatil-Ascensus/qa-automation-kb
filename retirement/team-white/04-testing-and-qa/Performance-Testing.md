# Performance Testing

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Performance-Testing-310454775.aspx) | Created: 2025-03-14 | Last modified: 2025-03-27 | Author: Chris Reynolds | Last editor: Chris Reynolds

---

### Useful Links

- [Performance Testing Strategy](https://ascensus0.sharepoint.com/sites/QualityEngineeringCF/SitePages/QA-Performance-Testing-Strategy-238065787.aspx)
- [Performance Testing Videos](https://ascensus0.sharepoint.com/sites/QualityEngineeringCF/SitePages/QA-Performance-Testing-Videos-178520537.aspx) (local setup, testing strategies, and deployment info)
- [Blazemeter with Kubernetes & Helm](https://ascensus0.sharepoint.com/sites/QualityEngineeringCF/SitePages/QA-Blazemeter-with-Kubernetes--Helm-96221276.aspx)
  - Sample project: [Employee.Investing.Api.PerformanceTests](https://tfs.ascensus.com/tfs/PSG/Portfolio/_git/EmployeeDesktop?path=/Employee/Employee.Investing.Api/Test/Employee.Investing.Api.PerformanceTests)
  - Setup in TeamCity: [https://gettaurus.org/kb/TeamCity/](https://gettaurus.org/kb/TeamCity/)
- [Test Organization Recommendations](https://ascensus0.sharepoint.com/sites/QualityEngineeringCF/SitePages/QA-Test-Organization-162467099.aspx)
- Used Python 3.11.9 and Apache Jmeter 5.6.3
- How to Configure JMeter to bypass SSL verification for the plugin repository
  - In the file  apache-jmeter-5.6.3\apache-jmeter-5.6.3\bin\user.properties  , add this line **jpgc.repo.address=[http://jmeter-plugins.org/repo/](http://jmeter-plugins.org/repo/)** Adding the above line made the error  "Failed to download plugins repository. One of the possible reasons is that you have proxy requirement for Internet connection.   Please read the instructions on this page: [https://jmeter-plugins.org/wiki/PluginsManagerNetworkConfiguration/](https://jmeter-plugins.org/wiki/PluginsManagerNetworkConfiguration/) "   to go away
- Onboarding Demo Tests: [https://a.blazemeter.com/app/#/accounts/406482/workspaces/404690/projects/2493816/tests](https://a.blazemeter.com/app/#/accounts/406482/workspaces/404690/projects/2493816/tests)
