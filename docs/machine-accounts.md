---
URL: https://bitwarden.com/help/machine-accounts/
---

# Machine Accounts

> [!NOTE] Service accounts now Machine account
> As of the 2024.4.1 release, service accounts are now referred to as machine accounts in Bitwarden Secrets Manager. All of the feature functionality will remain the same.

Machine accounts represent non-human machine users, like applications or deployment pipelines, that require programmatic access to a discrete set of [secrets](https://bitwarden.com/help/secrets/). Machine accounts are used to:

- Appropriately scope the selection of secrets a machine user has access to.
- Issue [access tokens](https://bitwarden.com/help/access-tokens/) to facilitate programmatic access to, and the ability to decrypt, edit, and create secrets.

Machine accounts that your user account has access to can be viewed by selecting **Machine accounts** from the navigation:

![Machine accounts](https://bitwarden.com/assets/3IQzFGc9f4OAoqvJSgrEBn/601542ce696652aac733e63b18cdffb0/2024-12-03_13-25-13.png)

Opening a machine account will list the **Secrets** and **People** the service account has access to, as well as any generated **Access tokens** and **Event logs**:

![Inside a machine account](https://bitwarden.com/assets/3L9EGMDn7gGAMi3uwD1MIP/74dd29c2c80c1d67ee3b27bd5160e8b7/2024-12-03_13-26-04.png)

## Create a machine account

On the Admin Console **Billing** → **Subscription** page you are able to assign the number of machine accounts available for use in your organization. For additional information regarding your available machine accounts and machine account scaling, see [here](https://bitwarden.com/help/secrets-manager-quick-start/#user-seats-and-service-account-scaling/).

To create a new machine account:

[![Vimeo Video](https://vumbnail.com/845933062.jpg)](https://vimeo.com/845933062)
*[Watch on Vimeo](https://vimeo.com/845933062)*

**Video Chapters:**
Learn more about machine accounts [here](https://bitwarden.com/help/machine-accounts/).

1. Use the **New**dropdown to select **Machine account**:

![New machine account](https://bitwarden.com/assets/LaVwicbqhvbliXPm6loOU/5559a5caf8ad70a95be3ea89f1b760ad/2024-12-03_11-29-17.png)
2. Enter a **Machine account name** and select **Save**.
3. Open the machine account and, in the **Projects** tab, type or select the name of the project(s) that this machine account should be able to access. For each added project, select a level of **Permissions:**

 - **Can read**: Machine account can retrieve secrets from assigned projects.
 - **Can read, write**: Machine account can retrieve and edit secrets from assigned projects, create new secrets in assigned projects, or create new projects altogether.

> [!TIP] SM 07/25 dependency
> Fully utilizing write access for machine accounts is dependent on a forthcoming [CLI](https://bitwarden.com/help/secrets-manager-cli/) release. For now, this simply makes the option available in the UI. Stay tuned to the [Release Notes](https://bitwarden.com/help/releasenotes/) for more information.

## Add people to a machine account

Adding organization members to a machine account will allow those people to generate access tokens for the machine account and interact with all secrets the machine account has access to. To add people to your machine account:

1. In the machine account, select the **People**tab.
2. From the people dropdown, type or select the members or groups to add to the machine account. Once you've selected the right people, select the **Add**button:

![Add people to a machine account](https://bitwarden.com/assets/3TrklnCquoynDHFX6nJ8w/2482453bf759525ccb6d23f8e9731a7d/2024-12-03_13-27-11.png)

## Add projects to a machine account

Adding projects to a machine account will allow programmatic access to included secrets using access tokens. To add projects to a machine account:

1. Open the machine account and select the **Projects**tab.
2. From the Projects dropdown, type or select the project(s) to add to the machine account. Once you've chosen the right projects, select the **Add** button:

![Add a project](https://bitwarden.com/assets/3XGkQt3MdNHmAoKLXXXMGh/2c68b9ea5a47885f35360a94d26f0442/2024-12-03_13-28-00.png)
3. For each added project, select a level of **Permissions:**

 - **Can read**: Machine account can retrieve secrets from assigned projects.
 - **Can read, write**: Machine account can retrieve and edit secrets from assigned projects, as well as create new secrets in assigned projects or create new projects.

## Delete a machine account

To delete a machine account, use the (⋮ ) options menu for the machine account to delete to select **Delete machine account**. Deleting a machine account **will not**delete the secrets associated with it. Machine accounts are fully removed once deleted and **do not** get [sent to the trash like secrets do](https://bitwarden.com/help/secrets/#delete-a-secret/).

## Machine account events

Timestamped records of actions taken with each service account are available from the machine account's **Event logs** tab.

Any user that has access to a given machine account will be able to view events for that machine account. Events that are captured include:

- Accessed secret *secret-identifier*. (`2100`)
- Added user: *user-identifier* to machine account with identifier: *machine-account-identifier* (`2300`)
- Removed user: *user-identifier* from machine account with identifier: *machine-account-identifier* (`2301`)
- Added group: *group-identifier* to machine account with identifier: *machine-account-identifier* (`2302`)
- Removed group: *group-identifier* from machine account with identifier: *machine-account-identifier *(`2303`)
- Created machine account with identifier: *machine-account-identifier* (`2304`)
- Deleted machine account with identifier: *machine-account-identifier* (`2305`)

> [!NOTE] Event capture
> Each **Event** is associated with a type code (`1000`, `1001`, etc.) that identifies the action captured by the event. Type codes are used by the [Bitwarden Public API](https://bitwarden.com/help/public-api/) to identify the action documented by an event.

Event logs are exportable and are retained indefinitely. Exporting events will create a `.csv` of all events within the specified date range, which should not exceed 367 days.

## Configuration information

The **Config**tab provides a quick view of information that might be required when configuring an application to use a machine account. **Identity server URL**, **API server URL**, **Organization ID**, and **Project IDs** are displayed and can be copied by selecting each field's respective [clone] icon. For more information on Secrets Manager environments, see the Secrets Manager [SDK documentation](https://bitwarden.com/help/secrets-manager-sdk/) and [CLI documentation](https://bitwarden.com/help/secrets-manager-cli/).

![Machine account config view](https://bitwarden.com/assets/4XRItVAnKy1iVtOM2DbDLg/97e60d73e9bf18823c98fa46c588f99e/2024-12-03_13-38-10.png)
