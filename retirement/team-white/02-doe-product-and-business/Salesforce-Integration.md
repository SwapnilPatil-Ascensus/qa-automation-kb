# Salesforce Integration

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-Salesforce-Integration-321343253.aspx) | Created: 2025-05-26 | Last modified: 2026-03-20 | Author: Federico Pizzaro | Last editor: Chris Reynolds

---

### Intro

#### The Connected App

The recommended approach to authorize a client application that needs to access the Salesforce REST API is to create a *Connected App*  that requests access using one the different *OAuth 2.0 Authorization Flows* .

- OAuth 2.0 is an open protocol that authorizes secure data sharing between applications through the exchange of tokens.
- A connected app is a framework that enables an third-party application to integrate with Salesforce by using APIs and standard protocols, such as SAML, OAuth, and OpenID Connect.
- Connected apps use these protocols to authenticate, authorize, and provide single sign-on (SSO) for third-party applications.

#### The Authorization Flow

There are some scenarios where you want to directly share information between two applications without a user getting in the way. For these scenarios, you can use the OAuth 2.0 client credentials flow.

- In this flow, the client app exchanges its client credentials defined in the connected app for an access token.
- This flow eliminates the need for explicit user interaction.
- This flow is a more secure alternative to the OAuth 2.0 username-password flow.

#### The Authorization Process

When a Connected App is created a set of client credentials (Client Id and Client Secret) are assigned to it.

- These credentials cannot be used to directly access a REST API, instead they must be exchanged for an *Access Token*  (Bearer Token)
- There is a /token endpoint where these credentials are posted and a token is returned as a response
- The auth token usually has a short expiration. In case the token expires a new one must be requested using the same approach.
- The auth token must be presented in each request to the REST API in the *Authorization*  header indicating that it is a *Bearer*  token.

### Hands On

#### Configure a Connected App

A connected app is used to request access to REST API resources on behalf of the client application using the OAuth 2.0 protocol.

**Steps to Create a Connected App**

1. Login in Salesforce and Navigate to the *Setup* page

2. In the *Quick Find* search box type "*Client App* " and click on "*External client App Manager* "

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2025-5-26_12-2-17.png)

3. Click on the "*New External Client App* " button and complete the required fields:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2025-5-26_12-6-17.png)

4. Expand the*API (Enable OAuth Settings)*  section and check the "*Enable OAuth* " checkbox.

In the*Callback URL*  field enter any valid URL. This value will not be used in our authorization flow but is still required, so any value will work.

In the *OAuth Scopes*  field select "*Full* " and "Manage user data via APIs". By selecting the *Full scope* this doesn't mean that our client app will have full access to all the Salesforce REST API.
Instead, this means that our client app will have access to all the resources that were granted to the Salesforce user that is impersonating the app. (We will see more about this later).

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2025-9-9_15-44-22.png)

5. For the*Flow*  Enablement, check the option to *Enable Client Credentials Flow* , and in *Security* sections you can uncheck the checked options since they do not apply to our flow.

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2026-3-20_12-5-51.png)

6. Click on create. You will see the created app in the External Client App Manager list:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2025-5-26_12-18-36.png)

7. Click on the name of the API so you can navigate to the details page. Then click on the Edit button:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2025-5-26_12-20-31.png)

8. Expand the *OAuth Policies*  section and check the *Enable Client Credentials Flow*  checkbox.
   Last populate the*Run As*  field with the username of the user that will be impersonating this client app.
   Is worth to mention here that the permissions to the different API resources are granted to this user and not to the Connected App. That's why the connected app needs a user in which it can run as.

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2025-5-26_12-32-12.png)

*9. Click on Save.*

#### Getting the *Client Secret*  and *Client Key*

Once the Connected App is created the client credentials will be available in the settings page. Navigate to the *Connected App*  details page and select the Settings tab.

You will see a button that let you access to the client and secret keys:

![image](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SiteAssets/SitePages/MTP-Salesforce-Integration-321343253/image-2025-5-26_12-35-50.png)
