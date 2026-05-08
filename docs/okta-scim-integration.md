---
URL: https://bitwarden.com/help/okta-scim-integration/
---

# Okta SCIM

System for cross-domain identity management (SCIM) can be used to automatically provision and de-provision members and groups in your Bitwarden organization. 

> [!NOTE] SCIM vs. BWDC
> SCIM integrations are available for **Teams and Enterprise organizations**. Customers not using a SCIM-compatible identity provider may consider using [Directory Connector](https://bitwarden.com/help/directory-sync/) as an alternative means of provisioning.

This article will help you configure a SCIM integration with Okta. Configuration involves working simultaneously with the Bitwarden web vault and Okta Admin Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

## Supported features

The following provisioning features are supported by this integration:

- **Push users: **Users in Okta that are assigned to Bitwarden are added as users in Bitwarden.
- **Deactivate users:**Users with the deactivated status will no longer have access to their assigned apps. Deactivating a user in Okta will change their Bitwarden status to revoked. 
- **Delete user**: Users deleted in Okta will be moved to revoked status in the Bitwarden organization.

> [!NOTE] Suspended users Okta
> Choosing the suspended status for a user in Okta will **not** result in a [revoked status in Bitwarden](https://bitwarden.com/help/revoke-users/).
- **Push groups: **Groups and their users in Okta can be pushed to Bitwarden.

> [!NOTE] SCIM Okta Support for Email Stuff
> Bitwarden does not support changing a user's email address once provisioned. Bitwarden also does not support changing a user's email address type or using a type other than `primary`. The values entered for email and username should be the same. [Learn more](https://bitwarden.com/help/about-scim/#required-attributes/).

## Enable SCIM in Bitwarden

> [!NOTE] Self-hosting SCIM
> **Are you self-hosting Bitwarden?** If so, complete these steps to [set up SCIM for your server](https://bitwarden.com/help/self-hosting-scim/) before proceeding.

To start your SCIM integration:

1. From the Admin Console, go to **Settings**→ **SCIM provisioning**.
2. Check **Enable SCIM**.
3. Select **Save**.
4. Your **SCIM URL**and **SCIM API key** will appear, which you will later [enter in Okta](https://bitwarden.com/help/okta-scim-integration/#connect-your-bitwarden-organization/):

![SCIM provisioning](https://bitwarden.com/assets/6sw1kuK7GuZ3dfQkkbs6rV/e665df6992fb880114fcef82e4e4c07c/SCIM_provisioning_URL_and_API_key.png)
*SCIM provisioning*

## Add the Bitwarden app to Okta

To add Bitwarden within Okta:

1. From the Okta Admin Portal, go to **Applications** → **Applications**.
2. Select **Browse App Catalog**.
3. In the search bar, enter `Bitwarden` and select **Bitwarden**:

![Browse app catalog for Bitwarden](https://bitwarden.com/assets/7DjlcFofhaHLVKyy2TId7c/86dc82876b88ba717ecfb107b192e7c7/Browse_app_catalog_for_Bitwarden_.png)
*Browse app catalog for Bitwarden*
4. Select **Add Integration**, which will open the Bitwarden app's general settings.
5. Enter a unique, Bitwarden-specific name in **Application label**.
6. Check **Do not display application icon to users.**
7. Select **Done**.

## Set up provisioning in Okta

To set up provisioning, the following steps must be completed in the same order that's presented here.

### Connect your Bitwarden organization

To connect Okta with Bitwarden:

1. While still on the Bitwarden app configuration page in Okta, select **Provisioning**.
2. Select **Configure API Integration**.
3. Check **Enable API Integration**.
4. Enter details you found earlier in the Bitwarden Admin Console, from **Settings**→ **SCIM provisioning**:

 - In the **Base URL** field, enter your **SCIM URL** from Bitwarden.
 - In the **API Token** field, enter your **SCIM API key** from Bitwarden.

![Enter Bitwarden SCIM URL and API key](https://bitwarden.com/assets/5GMQfUOLdpOaKhNxDf88D6/86617a7ee28f2fc5d2e6d646652406a1/Enter_Bitwarden_SCIM_URL_and_API_key.png)
*Enter Bitwarden SCIM URL and API key*
5. Select **Test API Credentials**. If you see a confirmation message like "Bitwarden was verified successfully!" then your connection works.
6. Select **Save**.

### Set provisioning actions

To allow specific provisioning actions:

1. While still on the **Provisioning** tab, select **To App**.
2. Select **Edit**:

![Provisioning to app](https://bitwarden.com/assets/2xFykuY8l8QtAp8ZfvrwQB/f7e98ede27e13479d54aa04f1a8fec18/Provisioning_to_app.png)
*Provisioning to app*
3. Check **Create Users** and **Deactivate Users**.
4. Select **Save**.
5. (Optional) Customize the **Bitwarden Attribute Mappings**.

### Set Assignments

Open the **Assignments**tab and use the **Assign** dropdown menu to assign people or groups to the application. Assigned users and groups will be automatically issued an invitation. Depending on your workflow, you may need to use the **Push Groups**tab to trigger group provisioning once they are assigned. 

## Finish user onboarding

Now that your users have been provisioned, they will receive invitations to join the organization. Instruct your users to [accept the invitation](https://bitwarden.com/help/managing-users/#accept/) and, once they have, [confirm them to the organization](https://bitwarden.com/help/managing-users/#confirm/).

> [!NOTE] Invite/Accept/Confirm
> The Invite → Accept → Confirm workflow facilitates the decryption key handshake that allows users to securely access organization vault data.
