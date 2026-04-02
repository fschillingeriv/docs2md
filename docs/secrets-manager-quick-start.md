---
URL: https://bitwarden.com/help/secrets-manager-quick-start/
---

# Secrets Manager Quick Start

> [!TIP] Switch the developer guide
> If you're a developer, you may prefer [Developer Quick Start](https://bitwarden.com/help/developer-quick-start/). The article you're currently on will cover Secrets Manager from an administrative and setup point of view.

Bitwarden Secrets Manager enables developers, DevOps, and cybersecurity teams to centrally store, manage, and deploy secrets at scale. Use the **Secrets Manager web app** to add and organize [secrets](https://bitwarden.com/help/secrets-manager-quick-start/#add-secrets/), create [systems of permissions](https://bitwarden.com/help/secrets-manager-quick-start/#assign-members-to-your-project/) to fit your needs, and [generate access tokens](https://bitwarden.com/help/secrets-manager-quick-start/#create-an-access-token/) for your applications.

Once Secrets Manager is set up, learn how to inject secrets into your machines and applications with the [Developer Quick Start](https://bitwarden.com/help/developer-quick-start/) guide.

## Access Secrets Manager

Log in to the Bitwarden web app and select **Secrets Manager**from the product switcher in the navigation menu:

[![Vimeo Video](https://vumbnail.com/840459200.jpg)](https://vimeo.com/840459200)
*[Watch on Vimeo](https://vimeo.com/840459200)*

If you or your organization are not active Secrets Manager users yet, click **Try it now**:

![Secrets Manager Homepage](https://bitwarden.com/assets/7iZGZNg39Z2l0OnoMIeFK9/30dd28c94db3bd1094c5258cfb60eeab/2024-08-05_09-18-08.png)

- **Owners** are taken to their organization's **Subscription** page for Secrets Manager.
- **Users** are asked if they want to send their organization owner an email requesting Bitwarden Secrets Manager access. They can edit the email before sending.

![Request access to Secrets Manager](https://bitwarden.com/assets/1yTEdQGVkLtkvZjRErjBkO/e68e6dafe143a5166ccddfdc4d61fc0e/2024-07-30_15-14-33.png)

## Set up Secrets Manager

### Add Secrets Manager to your organization

Only owners can add Secrets Manager to their organization. To start using Secrets Manager: 

1. In Admin Console for your organization, go to **Billing **→ **Subscription**.
2. In the **More from Bitwarden** section, check **Subscribe to Secrets Manager**:

![Add Secrets Manager](https://bitwarden.com/assets/eYPz7jQRhG0PvU7gclzXk/04bbea42872c078a1aa3d38e755ae2bc/Screenshot_2024-04-09_at_10.21.39_AM.png)
3. Depending on your organization's plan:

 - If you are on the Free plan, select **Submit**.
 - If you are on an upgraded plan, enter the desired number of **Subscription seats** (up to your Password Manager subscription's total) and **Additional machine accounts** beyond your plan's included amount (20 for Teams and 50 for Enterprise). Select **Save**.

> [!NOTE] User seat and service account scaling info
> Secrets Manager will automatically scale your user seats and machine accounts when new users or machine accounts are added. At any time, you can go to **Billing **→ **Subscription** to change the total allowed user seats and machine accounts. To set a scaling limit, select **Limit subscription** and **Limit machine accounts**:
> 
> ![Limit subscription seats and machine accounts](https://bitwarden.com/assets/6tcOx1PSHT54CQGPkbBZZ2/33a91dde38fdad0fd921403c2de77e00/Limit_subscription_seats_and_machine_accounts.png)

Once activated, you can open Secrets Manager from the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

### Give members access

> [!NOTE] Create SM Groups
> Before proceeding, we recommend [creating groups](https://bitwarden.com/help/about-groups/#create-a-group/) for Secrets Manager users. Groups let you to quickly assign access to secrets once users have Secrets Manager access.

Organization owners and admins can grant access to Secrets Manager. To give members access:

1. In Admin Console for your organization, go to **Members**.
2. Select which users you want to add to the Secrets Manager.
3. Click the ⋮ **icon** and select **Activate Secrets Manager**:

![Add Secrets Manager users](https://bitwarden.com/assets/3IBNL6FdndgPeuXa7m3rlP/fd04ec9951123e5a0ccd5fe4f04fa4de/2024-12-03_11-18-52.png)

Alternatively, go to **Members** → **Member role**and select **This user can access Secrets Manager**:

![Edit member role to grant Secrets Manager access](https://bitwarden.com/assets/3xGmMTCDMgY5V3tYSdA6O7/49200a3fab891c0aa65008dda65f80e0/Edit_member_role_to_grant_Secrets_Manager_access.png)

> [!NOTE] Refresh after SM access granted
> Once Secrets Manager access is granted to a user (or yourself), you may need to refresh your browser for Secrets Manager to appear.

## First steps

### Your secrets vault

Use the product switcher to open the Secrets Manager web app. If this is your first time opening the app you'll have an empty vault, but eventually it'll be full of your projects and secrets:

![Secrets vault](https://bitwarden.com/assets/644qYsogVg0ztLkZ90cKPi/a68037e16818da6ac3b335ab4a7d3a90/2024-12-03_11-24-23.png)

Let's start filling your vault.

### Add a project

**Projects**are collections of secrets logically grouped together for management access by your DevOps, cybersecurity, or other internal teams. It's important to take into account, when creating your projects, that projects will be **the primary structures through which you assign members access to secrets**. To create a project:

1. Use the **New**dropdown to select **Project**:

![Create a project](https://bitwarden.com/assets/3gGgCYT0CgS3MKAngKDooL/03bd6080e1f8c695c46fd23918f56951/2024-12-03_11-25-44.png)
2. Enter a **Project name**.
3. Select the **Save**button.

### Assign members to your project

Adding organization members to your project will allow those users to interact with the project's secrets. To add people to your project:

1. In the new project, select the **People**tab.
2. From the People dropdown, type or select the member(s) or group(s) to add to the project. Once you've selected the right people, use the **Add**button:

![Add people to a project](https://bitwarden.com/assets/4Vu9wuBd8ceEz7ji7V2kHZ/2f11a06f3ed09a1cd64190ad8197e914/2024-12-03_11-27-19.png)
3. Once members or groups are added to the project, set a level of **Permissions**for those members or groups. Members and groups can have one of the following levels of permission:

 - **Can read**: Members/groups will be able to view existing secrets in this project.
 - **Can read, write**: Members/groups will be able to view existing secrets and create new secrets in this project.

### Add secrets

Now that you have a project with a handful of members who can help you manage it, let's add some **secrets** to the project. Secrets are sensitive key-value pairs stored in your vault, typically things that should never be exposed in plain code or transmitted over unencrypted channels, for example:

- API Keys
- Application Configurations
- Database Connection Strings
- Environment Variables

You can import secrets directly to your vault as a `.json` file or add secrets manually:

### Import secrets

To import your secrets:

1. Review [this document](https://bitwarden.com/help/import-secrets-data/) for help properly formatting an import file.
2. Select **Settings**→ **Import data** from the left-hand navigation:

![Import data](https://bitwarden.com/assets/1YQuiYqXIuYYG1TpXoSJoU/f76b3ee08dda7b470f96da9ebbe4f9b1/2024-12-03_11-28-29.png)
3. Select **Choose File**and choose a `.json` file for import.

### Add secrets manually

To add secrets manually:

1. Use the **New** dropdown to select **Secret**:

![Create a secret](https://bitwarden.com/assets/3uEcZ7G5L2TJM4QgMmFZ4H/24d73aa7121de9c77383f51de618db02/2024-12-03_11-29-17.png)
2. In the New Secret window's top-most section, enter a **Name**and **Value**. Adding **Notes**is optional.
3. In the Project section, type or select the project to associate the secret with. A few key points:

 - Each secret can only be associated with a single project at a time.
 - Only organization members with access to the project will be able to see or manipulate this secret.
 - Only machine accounts with access to the project will be able to create a pathway for injecting this secret ([more on that soon](https://bitwarden.com/help/secrets-manager-quick-start/#add-a-service-account/)).
4. When you're finished, select the **Save**button.

Repeat this process for as many secrets as you want to add to your vault.

### Add a machine account

Now that you've got a project full of secrets, it's time to start constructing machine access to those secrets. **Machine accounts**represent non-human machine users, or groups of machine users, that require programmatic access to some of the secrets stored in your vault. Machine accounts are used to:

- Appropriately scope the selection of secrets a machine user has access to.
- Issue access tokens to facilitate programmatic access to, and the ability to decrypt, edit, and create secrets.

To add a machine account for this project:

1. Use the **New**dropdown to select **Machine account**:

![New machine account](https://bitwarden.com/assets/LaVwicbqhvbliXPm6loOU/5559a5caf8ad70a95be3ea89f1b760ad/2024-12-03_11-29-17.png)
2. Enter a **Machine account name** and select **Save**.
3. Open the machine account and, in the **Projects** tab, type or select the name of the project(s) that this machine account should be able to access. For each added project, select a level of **Permissions:**

 - **Can read**: Machine account can retrieve secrets from assigned projects.
 - **Can read, write**: Machine account can retrieve and edit secrets from assigned projects, as well as create new secrets in assigned projects or create new projects.

### Create an access token

**Access tokens** facilitate programmatic access to, and the ability to decrypt and edit, secrets stored in your vault. Access tokens are issued to a particular machine account, and will give any machine that they're applied to the ability to access **only the secrets associated with that machine account**. To create an access token:

1. Select **Machine accounts**from the navigation.
2. Select the machine account to create an access token for, and open the **Access tokens**tab:

![Create access token](https://bitwarden.com/assets/6EINDaXiPQp9qQcO6q1zt5/259e6c2c6e91e0df63c83d03a89ac4a2/2024-12-03_11-31-26.png)
3. Select the **Create access token**button.
4. On the Create Access Token panel, provide:

 - A **Name**for the token.
 - When the token **Expires**. By default, Never.
5. Select the **Create access token**button when you're finished configuring the token.
6. A window will appear printing your access token to the screen. Copy your token to somewhere safe before closing this window, as your token**cannot be retrieved later**:

![Access token example](https://bitwarden.com/assets/3QfpdSQai2hFrWGdGSlQRN/a5a5483cfbbbf690a8436043be58cea7/2024-12-03_11-32-26.png)

This access token is the authentication vehicle through which you'll be able to script secret injection to your machines and applications. 

## Next steps

Now that you've got the hang of creating the infrastructure for securely managing secrets, and of creating pathways for machine access to secrets, let's continue on to the [Developer Quick Start](https://bitwarden.com/help/developer-quick-start/) guide.

Or, for more information about Secrets Manager:

- [Bitwarden brings open source security and zero knowledge encryption to secrets management](https://bitwarden.com/blog/bitwarden-brings-open-source-security-to-secrets-management/)
- [Why does my development team need a secrets manager?](https://bitwarden.com/blog/why-does-my-development-team-need-a-secrets-manager/)
- [Why end-to-end encryption is crucial for developer secrets management](https://bitwarden.com/blog/why-end-to-end-encryption-is-crucial-for-developer-secrets-management/)
