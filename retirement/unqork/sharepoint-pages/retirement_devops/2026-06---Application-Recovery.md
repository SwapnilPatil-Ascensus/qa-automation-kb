# 2026-06 - Application Recovery

> Source: [SharePoint](https://ascensus0.sharepoint.com/sites/retirement_devops/SitePages/2026-06---Application-Recovery.aspx) | Created: 2026-05-26 | Last modified: 2026-06-04 | Author:  | Last editor: 

---

##### Helpful Notes:

- **VPN Instructions\F5 Connection\vCenter Link ->** [**Disaster Recovery**](https://ascensus0.sharepoint.com/sites/retirement_devops/SitePages/DC-Disaster-Recovery-100960907.aspx)
- **Microservice services**  - Instructions for starting a service with a conflicting port
  - That port number should show in the app event log for the service that is failing to start. Run the following command with that port number to find the service that is using it.
  - netstat -aof | findstr :PORTNUMBER
  - The PID will show as the last value in the return
  - Stop the conflicting service, start the service that was down and then restart the conflicting service.
    - Example:
      - C:\WINDOWS\system32>netstat -aof | findstr 56759    TCP    192.168.212.108:56759  services.ascensus.com:http  ESTABLISHED     4004
      - C:\WINDOWS\system32>tasklist /FI "PID eq 4004
      - Image Name                     PID Session Name        Session#    Mem Usage   ========================= ======== ================ =========== ============   Integration.PDFReactor.ex     4004 Services                   0    151,844 K

##### Priority One Validation Summary:

| **Application** | **DevOp** | **Start** | **End** | **Status** | **Issue** | **Resolution** |
| --- | --- | --- | --- | --- | --- | --- |
| [Rancher](https://rancher.ascensus.com/login) | @aspitzer |  | <br> | <br>can login to legacy rancher, but DMZ (and thus nodes) are inaccessable<br> |  | <br> |
| Rancher-NEW | @aspitzer | <br> | 1:30 | new RANCHER is currently inaccessable |  |  |
| <br>RabbitMQ VM Cluster<br> | @aspitzer |  | 1:30 | all nodes in cluster up and running | <br> |  |
| <br>Redis - New VM Cluster<br> | @aspitzer | 12:47-12:56 | 12:56 | all clusters up and working now | RWTPREDFB01-3 are inaccessable - DMZ issue | <br>there are actually 4 clusters that need to be checked<br>RDRE1-PREDFA0x (up)<br>RDRE1-PREDBA0x (up)<br>RWTPREDFB0x (up)<br>RWTPREDBB0x (up)<br> |
| <br>Redis - Legacy VM Cluster<br> | @aspitzer |  | 1:34p | up | nodes rdre1-predisa initially. redis did not start automatically |  |
| <br>Legacy Windows Microservices<br> | @gtierney | 2:00 | 2:25 | Up | <br> |  |
| <br>Mongo VM Cluster<br> | @aspitzer | 11:45-11:47 | 11:47 | all nodes in cluster up and running |  |  |
| <br>Content Delivery (Umbraco)<br> | @gflynn |  |  | up and running |  |  |
| [Proget](https://proget.ascensus.com/) | @aspitzer | <br> | 1:30 | can access and login |  |  |
| <br>DCA Web Services<br> | <br> |  |  |  |  |  |
| <br>BPMCOREs<br> | <br> |  |  |  |  |  |
| ARK\EE\ER\FP\IT\IT2\INT Middle Tier | @gflynn | <br> | <br> | all up |  |  |
| RPS Core services | <br> |  |  |  |  |  |
| RPS Middle Tier | <br> |  |  |  |  |  |
| [ELK](https://logging.ascensus.com/s/employee-pro/app/home#/) | @aspitzer |  | 1:30 | Elk is working now | RWTPLOGSA01-7 was inaccessable - network issue. |  |

##### Priority Two Validation Summary:

| <br>**Application**<br> | <br>**DevOp**<br> | <br>**Start**<br> | <br>**End**<br> | <br>**Status**<br> | <br>**Issue**<br> | <br>**Resolution**<br> |
| --- | --- | --- | --- | --- | --- | --- |
| [Sponsor Website](https://www.sponsorinsight.com/Ascensus/SignIn?returnUrl=/Ascensus) | <br> |  |  |  |  |  |
| [Employee Website](https://myaccount.ascensus.com/rplink/account/login) (myaccount) |  |  |  |  |  |  |
| [FP Website](https://mybusiness.ascensus.com/) (MyBusiness) |  |  |  |  |  |  |
| [DCA](https://secure.ascensus.com/login/participant) (Participant SSO) |  |  |  |  |  |  |
| [DCA](https://secure.ascensus.com/login/Sponsor) (Sponsor SSO) |  |  |  |  |  |  |
| [IRADirect](https://signon.ascensus.com/) |  |  |  |  |  |  |
| [taxreporting.ascensus.com](http://taxreporting.ascensus.com) |  |  |  |  |  |  |
| [PAS-Cycle3](https://pas.ascensus.com/c3) |  |  |  |  |  |  |
| <br>[ARK](http://ark.ascensus.com/)<br> | @plohe | 2:30 | 2:40 | Up | <br> |  |
| <br>Newport CRM<br> |  |  |  |  |  |  |
| <br>[Impact](http://impact10g.ascensus.com/)<br> | @plohe | 2:30 |  |  |  |  |
| <br>CLIFF Application/Xtender<br> | @gtierney | 2:25 | 2:35 | Up |  |  |
| <br>Newport BOBJ<br> | <br> |  |  |  |  |  |
| [BOSS](http://boss.newportgroup.com/) | @gflynn | 2:45 | 2:45 | Up |  |  |
| Web admin |  |  |  | <br> |  |  |
| [Pronto](http://pronto.secure.newportgroup.com/) |  |  |  | <br> |  |  |
| <br>CRM - PRO<br> |  |  |  |  |  |  |
| <br>Windows Cluster Services<br> | @gtierney | 1:30 | 1:40 | Up |  |  |
| <br>TPS Trade Services ([VMS – DR testing for Trade Processing](https://ascensus0.sharepoint.com/sites/retirement_devops/SitePages/DC-VMS-–-DR-testing-for-Trade-Processing-100962522.aspx))<br> | <br> | <br> | <br> | <br> |  |  |
| <br>Payroll Services<br> | <br> |  |  |  |  |  |
| <br>Compliance Services<br> | <br> |  |  |  |  |  |
| <br>Ascensus Trust website<br> |  |  |  |  |  |  |
| <br>Trust Plan Onboarding website<br> |  |  |  |  |  |  |
| <br>Trust SSRS/Services<br> |  |  |  |  |  |  |
| <br>Trust TrackerPro<br> |  |  |  |  |  |  |
| <br>SSRS - Data warehouse (fee disclosures), PSG 2008, RK Helpdesk, Client Reports, IRA Direct, Newport SSRS<br> |  |  |  |  |  |  |
| <br>ReadySave<br> |  |  |  |  |  |  |
| <br>Retirement Kofax<br> |  |  |  |  |  |  |
| [TeamCity](https://teamcity.ascensus.com/) | @aspitzer |  | 1:30 | can login and see all projects and history | <br> |  |
| [TFS](https://tfs.ascensus.com/tfs/psg) | @aspitzer |  | 1:30 | can login, access boards and repos | <br> |  |
| [Octopus](https://octopus.ascensus.com/app#/Spaces-1) | @aspitzer | <br> | 1:30 | <br>can login and see all deployments<br> |  |  |
| <br>UIPath Bots<br> |  |  |  |  |  |  |
| [Confluence](https://confluence.ascensus.com/) | @aspitzer | <br> | 1:30 | can login and browse around | <br> |  |
| <br>TrakIT<br> | @aspitzer | <br> | <br> | up - unfortunatlyf trakit seems to work fine. |  |  |
| <br>Source Code Manager (SCM)<br> |  |  |  |  |  |  |
| <br>[pronto.secure.newportgroup.com](http://pronto.secure.newportgroup.com/)<br> |  |  |  |  |  |  |
| <br>EIM Servers RWTPEIMRS01/02<br> |  |  |  |  |  |  |

##### Issues:

| <br>**Product**<br> | <br>**DevOps**<br> | <br>**Notes**<br> |
| --- | --- | --- |
| Onboarding | @schaggar | Onboarding works/connects with [https://retsupport.unqork.io/](https://retsupport.unqork.io/) - an external site. Does this need to be included in DR validation and if so any impact if site is opened up to live Production. |
| Cloud VDM | @alunger | <br>There were a few issues within the cloud desktop environment, some with temporary fixes, others that are outstanding:<br>- Teams spinning for 10+ minutes on the splash screen. I sent Aatiff Teams logs and he said it looked like it was updating. Restarting Teams multiple times, and the desktop once, didn't resolve the issue. Aatiff said to just use Teams in the browser for now.<br>- RDP access to Windows microservice servers (i.e. RDRE1-PMSVC01) wasn't working from the cloud desktop, or the CyberArk web UI. Karthik Veluchamy provided a workaround to RDP into 172.18.7.197 (Solarwinds box?), and then to the microservice boxes. The long-term solution is being worked on.<br>- App install permissions don't seem consistent with the regular environment desktop. I couldn't open a PowerShell terminal as an administrator, so I couldn't install Chocolatey. I was able to install Cursor directly downloaded from the Cursor website.<br>- Attempts to access [vcenterlas.internal.ascensus.com](https://vcenterlas.internal.ascensus.com/) time out.<br> |

**App\Dependency Breakdown:**

| App | Dependencies |
| --- | --- |
| [ark.ascensus.com](http://ark.ascensus.com/) | Active Directory |
|  | Sybase |
|  | Kubernetes |
|  | Redis |
|  | [services.ascensus.com](http://services.ascensus.com/) |
|  | Web Comments |
|  | Ark middle tier |
|  | Ark front end |
| <br>[Impact](http://impact10g.ascensus.com/)<br> | Sybase |
|  | SQL |
|  | BPMCore |
|  | int middle tier |
|  | IT2 middle tier |
|  | CLIFF Application Xtender |
|  | Impact Search |
|  | Impact Engines |
|  | Impact Portlets |
| [Employee Website](https://myaccount.ascensus.com/rplink/account/login) | Active Directory |
|  | LDS/LDAP |
|  | Sybase |
|  | SQL |
|  | BPM Core |
|  | Kubernetes |
|  | Redis |
|  | [services.ascensus.com](http://services.ascensus.com/) |
|  | MFE |
|  | EE Middle Tier |
|  | Secure Auth |
|  | Cold Fusion |
|  | Umbraco |
|  | Akamai |
| [FP Website](https://mybusiness.ascensus.com/) (MyBusiness) | Active Directory |
|  | LDS/LDAP |
|  | SQL |
|  | Kubernetes |
|  | Redis |
|  | [services.ascensus.com](http://services.ascensus.com/) |
|  | FP Middle Tier |
|  | Cirrus CMS |
| [Sponsor Website](https://www.sponsorinsight.com/Ascensus/SignIn?returnUrl=/Ascensus) | Active Directory |
|  | LDS/LDAP |
|  | Sybase |
|  | SQL |
|  | BPM Core |
|  | Kubernetes |
|  | Redis |
|  | PDF Reactor |
|  | [services.ascensus.com](http://services.ascensus.com/) |
|  | ER Middle Tier |
|  | Secure Auth |
|  | Cold Fusion |
|  | Sponsor MVC/IIS |
|  | Fusion Reactor (monitoring tool) |
|  | Umbraco |
|  | Akamai |
| [IRADirect](https://signon.ascensus.com/) | Active Directory |
|  | LDS/LDAP |
|  | Oracle |
|  | Kubernetes |
|  | Redis |
|  | MFE |
|  | UCM |
|  | RPS Core |
|  | RPS Middle Tier |
|  | Reverse Proxy IIS |
|  | Clusters App Servers |
|  | WebLogic/JAVA |
| SSRS Report | Sybase |
|  | SQL |
|  | Data warehouse (fee disclosures) |
|  | PSG 2008 |
|  | RK Helpdesk |
|  | Client Reports |
|  | IRA Direct |
|  | Newport SSRS |
| CLIFF Application Xtender | Active Directory |
|  | SQL |
| Statement Processing | Sybase |
|  | SQL |
|  | Extream Cluster |
|  | ARK |
|  | Snowbatch |
|  | Kubernetes |
| [DCA](https://secure.ascensus.com/login/participant) (Participant SSO)\[DCA](https://secure.ascensus.com/login/Sponsor) (Sponsor SSO) | LDS/LDAP |
|  | SQL Server |
|  | DCA Web Services |
|  | Kubernetes |
|  | Redis |
|  | BOBJ |
|  | Pronto |
|  | Meta Defender |
|  | NG Release |
|  | Unified Login |
|  | EUM API |
|  | JAMS |
|  | Dynamics CRM |
| Trade (TPS) | Sybase |
|  | Windows Cluster |
| Compliance apps | Sybase |
|  | Kubernetes |
|  | Redis |
|  | Windows Cluster |
| Payroll apps | Sybase |
|  | Kubernetes |
|  | Redis |
|  | Windows Cluster |
| [BOSS](http://boss.newportgroup.com/) | Active Directory |
|  | SQL |
| Web Admin | Active Directory |
|  | SQL |
| Chorus |  |
| AMP-Alerting app |  |
| Mailgun |  |
| Onboarding |  |
