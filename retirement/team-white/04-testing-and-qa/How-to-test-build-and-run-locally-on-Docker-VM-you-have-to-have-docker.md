# How to test build and run locally on Docker VM you have to have docker on your machine to be able to run it

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-to-test--build--and-run-locally-on-Docker-VM--you-have-to-have-docker-on-your-machine-to-be-able-to-run-it-299384531.aspx) | Created: 2025-01-15 | Last modified: 2025-02-19 | Author: Eddie Hooper | Last editor: Shankar Satijani

---

- Test this with DockerVM( you can use [Connect to Docker VM](https://ascensus0.sharepoint.com/sites/dcdevops/SitePages/DC-Connect-to-Docker-VM-221039818.aspx) doc to build and run your image)
  - Team White Docker VM is RWTDTEAMWHITE01
  - on powershell  need to do initial set up your port and connection to this machine
    - $remote_docker_server = "RWTDTEAMWHITE01"
    - `$remote_docker_port = "``2376"`
    - `docker context create $remote_docker_server -``-docker` `host=``"tcp://$($remote_docker_server):$($remote_docker_port)"`
    - `docker context``ls`
    - `docker context use $remote_docker_server`
  - to build image run the following after you cd to Onboarding root directory of Onboarding project
    - docker build -t onboarding-api --build-arg  APPLICATION=Onboarding.Api  -f ./Onboarding.Api/Build/Dockerfile .
  - to run image on  RWTDTEAMWHITE01    :
    - docker run  – it onboarding api
  - to   remove context
    - docker context rm `$remote_docker_server`
