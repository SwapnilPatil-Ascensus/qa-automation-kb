# How to see the information on Postman for unquork

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-to-see-the-information-on-Postman-for-unquork-326734858.aspx) | Created: 2025-06-09 | Last modified: 2025-06-09 | Author: Eddie Hooper | Last editor: Eddie Hooper

---

Variables for postman

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-How-to-see-the-information-on-Postman-for-unquork-326734858/image-2025-6-9_12-34-3.png)

Documentation  [https://developers.unqork.io](https://developers.unqork.io/)  does not shows correct devx url

Sample how to get  auth  key

curl --location "[https://retsupport-dev.unqork.io/api/1.0/oauth2/access_token](https://retsupport-dev.unqork.io/api/1.0/oauth2/access_token)" \
--header "Content-Type: application/x-www-form-urlencoded" \
--header "Authorization: ••••••" \
--data-urlencode "grant_type=client_credentials" \
--data-urlencode "clientId=[REDACTED]" \
--data-urlencode "clientSecret=[REDACTED]"

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-How-to-see-the-information-on-Postman-for-unquork-326734858/image-2025-6-9_12-45-23.png)

and respond you will get bearer token

Use that bearer token in other queries

Sample query how to retreive in our dev env the list of global  variables?

curl --location "[https://retsupport-devx.unqork.io/fbu/uapi//globalvars](https://retsupport-devx.unqork.io/fbu/uapi//globalvars)" --header "Content-Type: application/json" --header "Authorization: ••••••"  --data ""

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-How-to-see-the-information-on-Postman-for-unquork-326734858/image-2025-6-9_12-47-26.png)

Attached the export provided for list of end points to look but not use it as is since it is not our env url  [Unqork Customer API.postman_collection.json](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-How-to-see-the-information-on-Postman-for-unquork-326734858/Unqork%20Customer%20API.postman_collection.json?wtAid=326734886)⠀

It was suggested that release is not build via REST and not deploy via REST ,but manually

Concentrate on CSS and on global variables
