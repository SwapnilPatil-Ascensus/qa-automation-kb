# EF inside of base container

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-EF--inside-of-base-container-299381875.aspx) | Created: 2025-01-13 | Last modified: 2025-01-15 | Author: Eddie Hooper | Last editor: Eddie Hooper

---

#### Objective:

This will allow base container to run EF  deployment to DB first and then start base application.

#### Assumptions:

EF is version 8.0.0

applications.json refers to  ef version 8

for DDL user needs dbowner

Description:

- in base Dockerfile place the following:

1. Install toolset itself and build the app
![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-EF--inside-of-base-container-299381875/image-2025-1-13_10-27-40.png)

2. Create EF bundle. Make sure  your .csproj refer to correct version of EF

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-EF--inside-of-base-container-299381875/image-2025-1-13_10-28-40.png)

Please note that target for migration should be a main project that contains a connection string to the database and a reference to your "Data" project in case of mono repo.

3.  Dynamically create entrypoint.sh and give it execute privs  as :1 run efbundle ; 2. Startup app

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-EF--inside-of-base-container-299381875/image-2025-1-13_10-31-15.png)

- In C#
  - Make sure that resource access methods are configured as Scoped one in a DI container for your application
  - Ensure that your connection string for database doesn't have integrated security enabled prior to any migration - you should obtain a new database user account for it. You also must establish all connection strings (for all environments) in your Octopus project instance.
- Test this with DockerVM( you can use [Connect to Docker VM](https://ascensus0.sharepoint.com/sites/dcdevops/SitePages/DC-Connect-to-Docker-VM-221039818.aspx) doc to build and run your image)
  - Team White Docker VM is RWTDTEAMWHITE01
  - on powershell  need to do initial set up your port and connection to this machine
    - $remote_docker_server = "RWTDTEAMWHITE01"
    - `$remote_docker_port = "``2379"`
    - `docker context create $remote_docker_server -``-docker` `host=``"tcp://$($remote_docker_server):$($remote_docker_port)"`
    - `docker context``ls`
    - `docker context use $remote_docker_server`
  - to build image run the following after you cd to Onboarding.Api directory of Onboarding project
    - docker build -t onboarding-api --build-arg  APPLICATION=Onboarding.Api  -f ./Onboarding.Api/Build/Dockerfile .
  - to run image on  RWTDTEAMWHITE01    :
    - docker run  – it onboarding api
