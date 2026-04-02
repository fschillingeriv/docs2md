---
URL: https://bitwarden.com/help/ping-identity-scim-integration/
---

# Ping Identity SCIM Integration

System for cross-domain identity management (SCIM) can be used to automatically provision and de-provision members and groups in your Bitwarden organization.

> [!NOTE] SCIM vs. BWDC
> SCIM integrations are available for **Teams and Enterprise organizations**. Customers not using a SCIM-compatible identity provider may consider using [Directory Connector](https://bitwarden.com/help/directory-sync/) as an alternative means of provisioning.

This article will help you configure a SCIM integration with Ping Identity. Configuration involves working simultaneously with the Bitwarden web vault and Ping Identity Administrator dashboard. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

## Enable SCIM

> [!NOTE] Self-hosting SCIM
> **Are you self-hosting Bitwarden?** If so, complete [these steps to enable SCIM for your server](https://bitwarden.com/help/self-hosting-scim/) before proceeding.

To start your SCIM integration, open the Admin Console and navigate to **Settings**→ **SCIM provisioning**: 

![SCIM provisioning](https://bitwarden.com/assets/6sw1kuK7GuZ3dfQkkbs6rV/a4f4e18e561733297338e4ed44c6ed8c/2024-12-03_15-25-46.png)

Select the **Enable SCIM**checkbox and take note of your **SCIM URL**and **SCIM API Key**. You will need to use both values in a later step.

## Create a SCIM app

1. Navigate to provisioning + **New Connection**.

![Ping Identity new Connection](https://bitwarden.com/assets/7rehLEEEAvNwsBHGKqDwln/babec3f81595ead3253285229fe0e653/2024-10-09_11-29-32.png)
2. In the Create a New Connection window, choose the **Select** option for **Identity Store**.
3. In the Identity Store, enter SCIM into the search box and select **SCIM Outbound**. Once this step is complete, select **Next**.

![SCIM Connection ](https://bitwarden.com/assets/1FYhcQpQbuh78ypyLxi2Jn/9081de91a419870aad37dded7c5db080/2024-10-09_11-35-23.png)
4. Input a Name and Description for the SCIM connection.
5. Next, you will be required to input the **SCIM BASE URL**. Copy the **SCIM URL** value located on the Enable SCIM page in the Bitwarden Admin Console and paste it into this field.
6. Using the **Authentication Method** dropdown menu, select **OAuth 2 Bearer Token**. A field will appear named **Oauth Access Token**, paste the **SCIM API key** value from the Bitwarden Admin Console into this field.

![Ping Identity SCIM connection test](https://bitwarden.com/assets/7uGtHe2xM6QxJnqs5LNycl/6408a86d4332001ab1dac5f99c222887/2024-10-09_12-06-25.png)
7. Once setup is complete, you may select **Test Connection**. If successful, select **Next**.
8. On the **Configure Preferences** page, select desired preferences and actions.

> [!NOTE] Remove action Ping Identity SCIM
> Setting the Remove Action setting to `Disable` will result in Bitwarden users being moved to `Revoked` status rather if the user fails to meet the filter criteria set on Ping Identity. Restoring the criteria will return the user to their `previous state`.
> 
> If the Remove Action is set to `Delete`, the same action will [deprovision the user](https://bitwarden.com/help/managing-users/#deprovision-users/).
9. Select **Save** once complete. Select the newly created Connection and enable the Connection using the toggle.

![Enable Ping Identity Connection](https://bitwarden.com/assets/1GpO1UTspVLzLh0SwRgKuf/4669f4225cca00108f4f0a8700c38e2e/2024-10-09_14-13-24.png)

## Create a Rule

Before syncing user groups and directories, a Rule is required to sync the user groups to Bitwarden SCIM.

1. Return to the Provisioning Screen.
2. Select the **Rules**tab and then + **New Rule**.
3. Enter an app specific name for the Rule and select **Create Rule**.
4. Edit the new Rule in the Configuration tab. Select **Bitwarden SCIM connection** and then **Save**.

![Ping Identity Rule](https://bitwarden.com/assets/3eKZXwtiFdQqhlUNRSm6jr/167c28c624cf7f9ceb7dc563d58c64f4/2024-10-09_14-11-35.png)
5. Select the Configuration tab and add a [pencil] **User Filter**. For more information, see the [Ping Identity documentation](https://docs.pingidentity.com/pingone/integrations/p1_add_provisioning_filter.html). Select **Save** once complete.

![Ping Identity User Filter](https://bitwarden.com/assets/1dgfaEYambvyHm7J4WBASe/9b2245b92629e61341856c8cb197be2f/2024-10-09_14-32-31.png)
6. Enable the Rule using the toggle.

![Ping Identity new Rule](https://bitwarden.com/assets/73Y4cHkTeLtxtuqB3xIrOR/6faf11b60a278eab11f5c83d52035b57/2024-10-09_14-37-44.png)

## Provision groups

1. To assign groups, return to the Provisioning screen and select the rule ⋮ **Edit Group Provisioning**.

![Edit group provisioning](https://bitwarden.com/assets/10ztwQpTzsxZoi0vh83no6/f976a4f57d1fbe60b1f616f6114ce635/2024-10-09_15-11-57.png)
2. Choose the group or groups to provision and select **Save**. Once saved, the directory will trigger a sync.

## Appendix

### Required attributes

Both the Bitwarden and Ping Identity **SCIM Provisioner with SAML (SCIM v2 Enterprise)** applications use standard SCIM v2 attribute names. Bitwarden will use the following attributes:

#### User attributes

- `active`
- `emails`ª or `userName`
- `displayName`
- `externalId`

ª - Because SCIM allows users to have multiple email addresses expressed as an array of objects, Bitwarden will use the `value` of the object which contains `"primary": true`.

#### Group attributes

For each group, Bitwarden will use the following attributes:

- `displayName` (**required**)
- `members`ª
- `externalId`

ª - `members` is an array of objects, each object representing a user in that group.
