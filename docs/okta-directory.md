---
URL: https://bitwarden.com/help/okta-directory/
---

# Sync with Okta

This article will help you get starting using Directory Connector to sync users and groups from your Okta directory to your Bitwarden organization.

## Create an Okta API token

Directory Connector requires knowledge of an Okta-generated token to connect to your directory. Complete the following steps to create and obtain an Okta API token for use by Directory Connector:

1. From your Okta Developer Console (`https://yourdomain-admin.okta.com`) navigate to **Security** → **API** → **Tokens**.
2. Select the **Create token** button and give your token a Bitwarden-specific name (for example, `bitwarden-dc`).
3. Copy the generated **Token value** to the clipboard.

> [!NOTE] Okta api token value
> Your token value will not be shown again. Paste it somewhere safe to prevent it from being lost.

## Connect to your directory

Complete the following steps to configure Directory Connector to use your Okta Directory:

1. Open the Directory Connector [desktop app](https://bitwarden.com/help/directory-sync-desktop/).
2. Navigate to the **Settings** tab.
3. From the **Type** dropdown, select **Okta**.

The available fields in this section will change according to your selected type.
4. Enter your Okta Organization URL in the **Organization URL** field (for example, `https://yourdomain.okta.com`).
5. Paste the API Token Value in the **Token** field.

## Configure sync options

> [!NOTE] Clear sync cache
> When you're finished configuring, navigate to the **More** tab and select the **Clear Sync Cache** button to prevent potential conflicts with prior sync operations. For more information, see [Clear Sync Cache](https://bitwarden.com/help/clear-sync-cache/).

Complete the following steps to configure the settings used when syncing using Directory Connector:

1. Open the Directory Connector [desktop app](https://bitwarden.com/help/directory-sync-desktop/).
2. Navigate to the **Settings** tab.
3. In the **Sync** section, configure the following options as desired:

| **Option** | **Description** |
|------|------|
| Interval | Time between automatic sync checks (in minutes). |
| Remove disabled users during sync | Check this box to remove users from the Bitwarden organization that have been disabled in your directory. |
| Overwrite existing organization users based on current sync settings | Check this box to always perform a full sync and remove any users from the Bitwarden organization if they are not in the synced user set. |
| More than 2000 users or groups are expected to sync | Check this box if you expect to sync 2000+ users or groups. If you don't check this box, Directory Connector will limit a sync at 2000 users or groups. |
| Sync users | Check this box to sync users to your organization. Checking this box will allow you to specify **User Filters**. |
| User Filter | See [Specify sync filters](https://bitwarden.com/help/okta-directory/#specify-sync-filters/). |
| Sync groups | Check this box to sync groups to your organization. Checking this box will allow you to specify **Group Filters**. |
| Group Filter | See [Specify sync filters](https://bitwarden.com/help/okta-directory/#specify-sync-filters/). |

### Specify sync filters

Use comma-separated lists to include or exclude based on user email or group name. Additionally, Okta APIs provide limited filtering capabilities for users and groups that may be used in Directory Connector filter fields.

Consult Okta documentation for more information about using the `filter` parameter for [users](https://developer.okta.com/docs/api/resources/users#list-users-with-a-filter) and [groups](https://developer.okta.com/docs/api/resources/groups#filters).

#### User filters

##### Include/Exclude users by email

To include or exclude specific users based on email address:

```
include:joe@example.com,bill@example.com,tom@example.com
```

```
exclude:joe@example.com,bill@example.com,tom@example.com
```

##### Concatenate with `filter`

To concatenate a user filter with the `filter` parameter, use a pipe (`|`):

```
include:john@example.com,bill@example.com|profile.firstName eq "John"
```

```
exclude:john@example.com,bill@example.com|profile.firstName eq "John"
```

##### Use only `filter`

To use only the `filter` parameter, prefix the query with a pipe (`|`):

```
|profile.lastName eq "Smith"
```

#### Group filters

> [!NOTE] nested groups not supported okta
> Syncing nested groups is not supported by Okta.

##### Include/Exclude groups

To include or exclude groups by name:

```
include:Group A,Group B
```

```
exclude:Group A,Group B
```

##### Concatenate with `filter`

To concatenate a group filter with the `filter` parameter, use a pipe (`|`):

```
include:Group A|type eq "APP_GROUP"
```

```
exclude:Group A|type eq "APP_GROUP"
```

##### Use only `filter`

To use only the `filter` parameter, prefix the query with a pipe (`|`):

```
|type eq "BUILT_IN"
```

## Test connection

> [!TIP] BWDC connect to EU server.
> Before testing or executing a sync, check that Directory Connector is connected to the right cloud server (e.g. US or EU) or self-hosted server. Learn how to do so with the [desktop app](https://bitwarden.com/help/directory-sync-desktop/#getting-started/) or [CLI](https://bitwarden.com/help/directory-sync-cli/#config/).

To test whether Directory Connector will successfully connect to your directory and return the desired users and groups, navigate to the **Dashboard** tab and select the **Test Now** button. If successful, users and groups will be printed to the Directory Connector window according to specified [sync options](https://bitwarden.com/help/okta-directory/#configure-sync-options/) and [filters](https://bitwarden.com/help/okta-directory/#specify-sync-filters/):

![Test sync results](https://bitwarden.com/assets/6LbdKcCZucynwqW7eoOetT/331b88e5bc07cbe92f67a2a92f2d807d/dc-okta-test.png)

## Start automatic sync

Once [sync options](https://bitwarden.com/help/okta-directory/#configured-sync-options/) and [filters](https://bitwarden.com/help/okta-directory/#specify-sync-filters/) are configured as desired, you can begin syncing. Complete the following steps to start automatic sync with Directory Connector:

1. Open the Directory Connector [desktop app](https://bitwarden.com/help/directory-sync-desktop/).
2. Navigate to the **Dashboard** tab.
3. In the **Sync** section, select the **Start Sync** button.

You may alternatively select the **Sync Now** button to execute a one-time manual sync.

Directory Connector will begin polling your directory based on the configured [sync options](https://bitwarden.com/help/okta-directory/#configured-sync-options/) and [filters](https://bitwarden.com/help/okta-directory/#specify-sync-filters/).

If you exit or close the application, automatic sync will stop. To keep Directory Connector running in the background, minimize the application or hide it to the system tray.

> [!NOTE] Teams Starter + BWDC
> If you're on the [Teams Starter](https://bitwarden.com/help/password-manager-plans/#teams-starter-organizations/) plan, you are limited to 10 members. Directory Connector will display an error and stop syncing if you try to sync more than 10 members.
> 
> **This plan is no longer available for purchase**. This error does not apply to Teams plans.
