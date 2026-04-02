---
URL: https://bitwarden.com/help/onelogin-scim-integration/
---

# OneLogin SCIM Integration

System for cross-domain identity management (SCIM) can be used to automatically provision and de-provision members and groups in your Bitwarden organization. 

> [!NOTE] SCIM vs. BWDC
> SCIM integrations are available for **Teams and Enterprise organizations**. Customers not using a SCIM-compatible identity provider may consider using [Directory Connector](https://bitwarden.com/help/directory-sync/) as an alternative means of provisioning.

This article will help you configure a SCIM integration with OneLogin. Configuration involves working simultaneously with the Bitwarden web vault and OneLogin Admin Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented. 

## Enable SCIM

> [!NOTE] Self-hosting SCIM
> **Are you self-hosting Bitwarden?** If so, complete [these steps to enable SCIM for your server](https://bitwarden.com/help/self-hosting-scim/) before proceeding.

To start your SCIM integration, open the Admin Console and navigate to **Settings**→ **SCIM provisioning**: 

![SCIM provisioning](https://bitwarden.com/assets/6sw1kuK7GuZ3dfQkkbs6rV/a4f4e18e561733297338e4ed44c6ed8c/2024-12-03_15-25-46.png)

Select the **Enable SCIM**checkbox and take note of your **SCIM URL**and **SCIM API Key**. You will need to use both values in a later step.

## Create a OneLogin app

In the OneLogin Portal, navigate to the the **Applications** screen and select the **Add App** button:

![Add an Application ](https://bitwarden.com/assets/37OSt7e5j969j9ikvH8buI/3bf9fa6b57a45b357a9d2bc012d8a6af/ol-addapp.png)

In the search bar, type `SCIM` and select the **SCIM Provisioner with SAML (SCIM v2 Enterprise)** app:

![SCIM Provisioner App](https://bitwarden.com/assets/1nhhqAjka2eRfzl0cG00re/009afae8e9a056db414523aaf99392b2/remove-name-3.png)

Give your application a Bitwarden-specific **Display Name** and select the **Save** button.

### Configuration

Select **Configuration**from the left-hand navigation and configure the following information, some of which you will need to retrieve from the Single Sign-On and SCIM Provisioning screens in Bitwarden.

![SCIM App Configuration](https://bitwarden.com/assets/2AeNYZyjrTZSU8CHupIXjY/d8e0475924f924fceebc9a6e4a2331b7/remove-name-4.png)

#### Application details

OneLogin will require you to fill in the **SAML Audience URL**and **SAML Consumer URL** fields even if you aren't going to use single sign-on. [Learn what to enter in these fields](https://bitwarden.com/help/saml-onelogin/#configuration/).

#### API connection

Enter the following values in the **API Connection** section:

| **Application setting** | **Description** |
|------|------|
| SCIM base URL | Set this field to the SCIM URL ([learn more](https://bitwarden.com/help/onelogin-scim-integration/#enable-SCIM/)). |
| SCIM bearer token | Set this field to the SCIM API key ([learn more](https://bitwarden.com/help/onelogin-scim-integration/#enable-SCIM/)). |

Select **Save**once you have configured these fields.

### Access

Select **Access** from the left-hand navigation. In the **Roles**section, assign application access to all the roles you would like provision in Bitwarden. Each role is treated as a group in your Bitwarden organization, and users assigned to any role will be included in each group including if they are assigned multiple roles.

### Rules

Create a rule to map OneLogin Roles to Bitwarden groups:

1. Select **Rules**from the left-hand navigation.
2. Select the Add Rule button to open the **New mapping**dialog:

![Role/Group Mapping](https://bitwarden.com/assets/42I8sAk9GBypUCDFxWbb4V/3c34b07f12bc62fb85270bf91881f582/Screen_Shot_2022-07-21_at_12.14.25_PM.png)
3. Give the rule a **Name**like Create Groups from Rules.
4. Leave **Conditions**blank.
5. In the **Actions**section:

 1. Select **Set Groups in <application_name>** from the first dropdown.
 2. Select the **Map from OneLogin** option.
 3. Select **role**from the "For each" dropdown.
 4. Enter .* in the "with value that matches" field to map all roles to groups, or enter a specific role name.
6. Select the **Save**button to finish creating the rule.

### Test connection

Select **Configuration**from the left-hand navigation, and select the **Enable**button under **API Status:**

![Test API Connection](https://bitwarden.com/assets/6JJ9yBJshFhR7BgxXBg83K/74cc06192465100b109c6f94cc9ae680/remove-name-6.png)

This test **will not** start provisioning, but will make a GET request to Bitwarden and display **Enabled**if the application gets a response from Bitwarden successfully.

### Enable provisioning

Select **Provisioning**from the left-hand navigation:

![Provisioning Settings](https://bitwarden.com/assets/YMC1HjBpeKREdb3lJNHqb/1abdcbb216848efb62795c921edc05b5/image.png)

On this screen:

1. Select the **Enable Provisioning**checkbox.
2. In the **When users are deleted in OneLogin...**dropdown, select **Delete**.
3. In the **When user accounts are suspended in OneLogin...** dropdown, select **Suspend**.

When you are done, select **Save** to trigger provisioning.

### Designate groups to provision

Select **Parameters**from the left-hand navigation. Select **Groups**from the table, enable the **Include in User Provisioning**checkbox, and select the **Save**button:

![Include Groups in User Provisioning](https://bitwarden.com/assets/2h03FR4hdjbrxWuUojzzGb/c004d00d53e780b98429453f20591125/remove-name-5.png)

### Finish user onboarding

Now that your users have been provisioned, they will receive invitations to join the organization. Instruct your users to [accept the invitation](https://bitwarden.com/help/managing-users/#accept/) and, once they have, [confirm them to the organization](https://bitwarden.com/help/managing-users/#confirm/).

> [!NOTE] Invite/Accept/Confirm
> The Invite → Accept → Confirm workflow facilitates the decryption key handshake that allows users to securely access organization vault data.

## Appendix

### User attributes

Both Bitwarden and OneLogin's **SCIM Provisioner with SAML (SCIM v2 Enterprise)** application use standard SCIM v2 attribute names. Bitwarden will use the following attributes:

- `active`
- `emails`ª or `userName`
- `displayName`
- `externalId`

ª - Because SCIM allows users to have multiple email addresses expressed as an array of objects, Bitwarden will use the `value` of the object which contains `"primary": true`.
