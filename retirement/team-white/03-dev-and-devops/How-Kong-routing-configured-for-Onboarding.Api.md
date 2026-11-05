# How Kong routing configured for Onboarding.Api

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-Kong-routing--configured-for-Onboarding.Api-294996152.aspx) | Created: 2024-12-27 | Last modified: 2025-05-09 | Author: Eddie Hooper | Last editor: Eddie Hooper

---

#### Existing Kong configuration and routing for developer.qa.ascensus.com/onboarding/api/exception end point

*🚧 Gliffy diagram 'Kong for onboarding setup' replaced by image:*

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-How-Kong-routing--configured-for-Onboarding.Api-294996152/route%20request%20for%20service%20to%20kong.png)

#### How the  end point developer.ascensus.com/onboarding/api/exception page request gets propagated from   onboarding service via Kong service

1.Request comes from internet end up on F5

2. from F5 goes to K8 into Kong service

3. Kong service has applied plugin configs to internal implementation of plugins.

4. Kong see the  route it came from (developer.ascensus.com/onboarding/api/exception) and engage consumer and route.

5. Kong check if consumer has jwt  plugin and if route(onboarding/api/excerption in this case) has it.

6. Due to pre0function and http-log plugin  rule configuration kong will send information about request to ELK.

7. Kong check  jwt credentials with secureauth  and if allows  pass to upstream(service)

8. Upstream service if it response fine will return  exception page

Note: **for now whitelisting plugin exist ,but not applies and configured for any route!**

#### How to add new  end point to existing Kong configuration CONSIDERED THAT NEW END POINT HAS SAME WHITELISTING AND RATELIMIT

Granted all the same plugins used in new entry point page. If other plugins needed (whitelisting or/and rate limit) need to create separate kongroutes.yaml file - talk to your devops

All configurations are stored in Onboarding.Api/Deploy/helm/templates yaml files  .

In order to add new routing end point for service you need :

1.Add  in values.yaml  new row for new routing path as following

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-How-Kong-routing--configured-for-Onboarding.Api-294996152/image-2025-1-2_16-24-21.png)

2.Create new build in TC

3. Redeploy
