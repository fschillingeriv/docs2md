---
URL: https://bitwarden.com/help/okta-scim-integration/
---

# Okta SCIM Integration

System for cross-domain identity management (SCIM) can be used to automatically provision and de-provision members and groups in your Bitwarden organization. 

> [!NOTE] SCIM vs. BWDC
> SCIM integrations are available for **Teams and Enterprise organizations**. Customers not using a SCIM-compatible identity provider may consider using [Directory Connector](https://bitwarden.com/help/directory-sync/) as an alternative means of provisioning.

This article will help you configure a SCIM integration with Okta. Configuration involves working simultaneously with the Bitwarden web vault and Okta Admin Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

### Supported features

The following provisioning features are supported by this integration:

- **Push Users: **Users in Okta that are assigned to Bitwarden are added as users in Bitwarden.
- **Deactivate Users:**Users with the deactivated status will no longer have access to their assigned apps. Deactivating a user in Okta will change their Bitwarden status to revoked. 
- **Delete user**: Users deleted in Okta will be moved to revoked status in the Bitwarden organization.

> [!NOTE] Suspended users Okta
> Choosing the suspended status for a user in Okta will **not** result in a revoked status in Bitwarden.
- **Push Groups: **Groups and their users in Okta can be pushed to Bitwarden.

> [!NOTE] SCIM Okta Support for Email Stuff
> Please note, Bitwarden does not support changing a user's email address once provisioned. Bitwarden also does not support changing a user's email address type, or using a type other than `primary`. The values entered for email and username should be the same.[ Learn more](https://bitwarden.com/help/about-scim/#required-attributes/).

## Enable SCIM

> [!NOTE] Self-hosting SCIM
> **Are you self-hosting Bitwarden?** If so, complete [these steps to enable SCIM for your server](https://bitwarden.com/help/self-hosting-scim/) before proceeding.

To start your SCIM integration, open the Admin Console and navigate to **Settings**→ **SCIM provisioning**: 

![SCIM provisioning](https://bitwarden.com/assets/6sw1kuK7GuZ3dfQkkbs6rV/a4f4e18e561733297338e4ed44c6ed8c/2024-12-03_15-25-46.png)

Select the **Enable SCIM**checkbox and take note of your **SCIM URL**and **SCIM API Key**. You will need to use both values in a later step.

## Add the Bitwarden app

In the Okta Admin Portal, select **Applications** → **Applications**from the navigation. On the Application screen, select the **Browse App Catalog**button:

![Browse App Catalog](https://bitwarden.com/assets/nBs4O5osFzxI0QCfQLpxx/c8232cb95494901d8c04e38efc1b3662/Screen_Shot_2022-08-29_at_11.43.30_AM.png)

In the search bar, enter `Bitwarden` and select **Bitwarden**:

![Bitwarden Okta App](https://bitwarden.com/assets/4I8U9GJFm2w25scodW6aHu/cff940398de8ba4e363b706a2fe98d9f/today1.png)

Select the **Add Integration**button to proceed to configuration.

### General settings

On the **General Settings**tab, give the application a unique, Bitwarden-specific label. Check the **Do not display application icon to users**and **Do not display application icon in Okta Mobile App**options and select **Done**.

## Setup provisioning

To setup provisioning, the following steps must be completed in the order presented.

### Provisioning settings

Open the **Provisioning**tab and select the **Configure API Integration**button.

Once selected, Okta will list a few options for you to configure:

![Configure API Integration](https://bitwarden.com/assets/1vyUChnKJS2WM2V6u0gMGS/826c7a34f32cc9dc3b864a969d1b00c5/Screen_Shot_2023-02-06_at_1.39.09_PM.png)

1. Check the **Enable API Integration** checkbox.
2. In the **Base URL** field, enter your SCIM URL, which can be found on the SCIM Provisioning screen ([learn more](https://bitwarden.com/help/okta-scim-integration/#enable-scim/)).
3. In the **API Token** field, enter your SCIM API Key ([learn more](https://bitwarden.com/help/okta-scim-integration/#enable-scim/)).

Once you are finished, use the **Test API Credentials**button to test your configuration. If it passes the test, select the **Save** button.

### Set Provisioning actions

After the provisioning settings step has been completed, navigate to the **Provisioning**→ **To App** screen. Then, select the **Edit**button:

![Provisioning To App](https://bitwarden.com/assets/7HbSzaHxTZ8iddtJ3p0ATj/b24242f237309de4d51e1f7c943d7903/today3.png)

Enable, at a minimum, **Create Users** and **Deactivate Users**. Select **Save**when you are done.

## Assignments

Open the **Assignments**tab and use the Assign dropdown menu to assign people or groups to the application. Assigned users and groups will be automatically issued an invitation. Depending on your workflow, you may need to use the **Push Groups**tab to trigger group provisioning once they are assigned. 

## Finish user onboarding

Now that your users have been provisioned, they will receive invitations to join the organization. Instruct your users to [accept the invitation](https://bitwarden.com/help/managing-users/#accept/) and, once they have, [confirm them to the organization](https://bitwarden.com/help/managing-users/#confirm/).

> [!NOTE] Invite/Accept/Confirm
> The Invite → Accept → Confirm workflow facilitates the decryption key handshake that allows users to securely access organization vault data.
