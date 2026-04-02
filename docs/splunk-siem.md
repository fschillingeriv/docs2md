---
URL: https://bitwarden.com/help/splunk-siem/
---

# Splunk SIEM

Splunk Enterprise is a security information and event management (SIEM) platform that can be used with Bitwarden organizations. Organizations can monitor [event](https://bitwarden.com/help/event-logs/) activity with the [Bitwarden Event Logs](https://splunkbase.splunk.com/app/6592) app on their Splunk dashboard.

## Setup

### Create a Splunk account

Installing the Bitwarden app on Splunk requires a Splunk Enterprise account. Bitwarden event monitoring is available on:

- Splunk Enterprise
- Spunk Cloud Classic
- Splunk Cloud Victoria

### Install Splunk

For on-premise Splunk users, the next step is to install Splunk Enterprise. Follow the [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/9.0.4/SearchTutorial/InstallSplunk) to complete an install of the Splunk Enterprise software. 

> [!NOTE] Splunk Enterprise supported versions
> Bitwarden is supported on Splunk Enterprise versions 9.3, 9.4, and 10.0. Splunk Enterprise versions 8.X are no longer supported.

### Create an index

Before connecting your Bitwarden organization to your Splunk Dashboard, create an index that will maintain Bitwarden data. 

1. Open the **Settings** menu located on the top navigation bar and select **Indexes**.
2. Once you are on the indexes screen, select **New Index**. A window will appear for you to create a new index for your Bitwarden app. 

### Splunk Cloud

![New Index](https://bitwarden.com/assets/j3k8D4EBEEFPv7le82mFS/7cae447085492faf80f61898b7c4f0cf/new_index.png)

### Splunk Enterprise

![New Index Enterprise](https://bitwarden.com/assets/3yYEP61PqzSEl9tOBuwWIl/c452955bbba510d972d1584c5416fe13/new_index_sh.png)
3. In the **Index Name** field, enter `bitwarden_events`.
4. Apply your required values for **Max raw data size** and **Searchable retention**.
5. When you are finished, select **Save**.` `

### Install the Splunk Bitwarden app

After your Bitwarden index has been created, navigate to your Splunk dashboard.

1. Open the **Apps** drop down menu and select **Find More Apps**.

![Splunk apps dashboard](https://bitwarden.com/assets/IsbH3oo9FYomh0InDjVwt/fc2aca538dedd4d56820e8da236d8278/more_apps.png)
2. Select **Browse more apps**.
3. Search **Bitwarden Event Logs** in the app catalogue. Select **Install** for the **Bitwarden Event Logs**app.

![Bitwarden event logs app](https://bitwarden.com/assets/5IzRtDgpykBPZ21AUJnxbJ/c70ffa253781789cbeb200932edc0554/Bitwarden_event_logs.png)
4. In order to complete the installation, you will need to enter your [Splunk ](https://splunkbase.splunk.com/)account. Your Splunk account may not be the same credentials used to access your Splunk portal. 

![Login and install Bitwarden app on Splunk](https://bitwarden.com/assets/1Ko0eUuBz2AYIo0kNuxDoQ/2bb4b832236780509e6667e3c325a72f/2024-04-16_11-04-51.png)
5. After you have entered your information, select **Agree and Install**.

> [!NOTE] Restart Splunk
> Following the Bitwarden Event Logs app download, you may be required to restart Splunk.

### Connect your Bitwarden organization

Once the Bitwarden Event Logs app has been installed in your Splunk Enterprise instance, you can connect your Bitwarden organization using your Bitwarden [API key](https://bitwarden.com/help/public-api/#authentication/). 

1. Go to the dashboard home and select the **Bitwarden Event Logs**app:

![Bitwarden on Splunk dashboard](https://bitwarden.com/assets/4XFuwwljpBglow8GsaYTcP/08af521d324c76fea00937617a7fe19d/2024-05-06_16-09-59.png)
2. Next, on the App configuration page, select **Continue to app setup page**. This is where you will add your Bitwarden organization's information.

![Setup Bitwarden menu](https://bitwarden.com/assets/4c0008B7jTVp0PQtp97p0h/e725995706475b44b8726db6fbf066c1/SplunkSetupFull_edited.png)
3. Keep this screen open, on another tab, log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
4. Navigate to your organization's **Settings** → **Organization info** screen and select the **View API key**button. You will be asked to re-enter your master password in order to access your API key information.

![Organization api info](https://bitwarden.com/assets/6gHjAyqgeqDj6UPT6agsBK/3a614e043cb3836a41bd68f226835e53/2024-12-04_09-51-07.png)
5. Copy and paste the `client_id` and `client_secret` values into their respective locations on the Splunk setup page.

Complete the following additional fields as well:

| Field | Value |
|------|------|
| Index | Select the index that was created previously in the guide: `bitwarden_events`. |
| Server URL | For self-hosted Bitwarden users, input your self-hosted URL.` `For cloud-hosted organizations, use the URL `https://vault.bitwarden.com` or `https://vault.bitwarden.eu`. |
| Start date (optional) | Set a start date for data monitoring. When not set, the default date will be set to 1 year. This is a one time configuration, once set, this setting **cannot** be changed. |

> [!NOTE] Org API information sensitive
> Your organization API key information is sensitive data. Do not share these values in nonsecure locations.

Once done, select **Submit**.

## Understanding Search Macro

The `bitwarden_event_logs_index `search macro will be created following the initial Bitwarden Event Logs install. To access the macro and adjust settings:

1. Open the **Settings** on to top navigation bar. Then, select **Advanced Search**.
2. Select **Search Macros** to open the list of search macros.

### Search macro permissions

Next, setup which user roles will have permission to use the macro:

1. View macros by selecting **Settings**→ **Advanced Search**→ **Search macros**.
2. Select **Permissions**on `bitwarden_events_logs_index`. Edit the following permissions and select Save once complete:

![Search Macro Permissions](https://bitwarden.com/assets/69xCHcmqFE8CLp7kGJJkdJ/4faffad91633090dd5709b32e4cb7bc0/2024-05-14_08-44-55.png)

| Field | Description |
|------|------|
| Object should appear in | In order to use the macro in event searching, select **This app only**. The macro will not apply if **Keep private** is selected. |
| Permissions | Select the desired permissions for user roles with **Read**and **Write** access. |

> [!NOTE] Splunk single macro
> Only one search macro will be functional on the app at a given time.

## Understanding the dashboards

The Dashboard will provide several options for monitoring and visualizing Bitwarden organizational data. The three primary categories of data monitoring include:

- Bitwarden authentication events
- Bitwarden vault item events
- Bitwarden organization events

The data displayed on the dashboards will provide information and visualization for a broad variety of searches. More complex queries can be completed by selecting the **Search** tab at the top of the dashboard.

> [!NOTE] Splunk Ingest all paramaters
> Search results will only populate data relevant to a specific event type that occurred. Attributes that are not in-scope for a specific event type will be displayed as `null` in the search results. For example, `collectionId=null` will be present when the event type is a user logging in.

### Timeframe

While searching from the **Search**page or **Dashboards**, searches can be designated to a specific timeframe.

![Splunk timeframe search](https://bitwarden.com/assets/zizTsxjCMKlD4TXLmi2UZ/86807e58f3de67b9b51c10924f594069/2024-03-06_16-56-03.png)

> [!NOTE] Splunk on-premises search
> For on-premises users, the following timeframes are supported for Bitwarden event logs searches:
> 
> - Month to date
> - Year to date
> - Previous week
> - Previous business week
> - Previous month
> - Previous year
> - Last 30 days
> - All time

## Query parameters

Set up specific searches by including search queries. Spunk utilizes its search processing language (SPL) method for searching. See [Splunk's documentation](https://docs.splunk.com/Documentation/Splunk/9.0.4/Search/GetstartedwithSearch) for additional details on searches. 

**Search structure:**

```
search | commands1 arguments1 | commands2 arguments2 | ...
```

An example of a standard search result object:

![Splunk search result object](https://bitwarden.com/assets/620J7a17eXWhkgkCOzpixU/a75acef6074ca30a014811363cb36c8a/query_data.png)

The fields shown in the standard search object can be included in any specific search. This includes all of the following values:

#### Bitwarden Fields

| Value | Description |
|------|------|
| `actingUserEmail` | The email of the user performing the action. |
| `actingUserId` | Unique id of user performing action. |
| `actingUserName` | Name of the user performing an action. |
| `collectionId` | Organization collection id. |
| `device` | Numerical number to identify the device that the action was performed on. |
| `deviceName` | Numerical id of device. Exact mapping can be located [here](https://github.com/bitwarden/splunk/blob/a9a6d6501c36d37ee7e95f88400c39f6ff2c926b/package/default/props.conf#L83). |
| `groupId` | Organization group id. |
| `groupName` | Organization group name. |
| `hash` | Splunk computed data hash. Learn more about Splunk's data integrity [here](https://docs.splunk.com/Documentation/Splunk/9.0.4/Security/Dataintegritycontrol). |
| `ipAddress` | The ip address that performed the event. |
| `itemId` | Vault item (cipher, secure note, etc..) of the organization vault. |
| `memberEmail` | Email of the organization member that the action was directed towards. |
| `memberId` | Unique id of the organization member that the action was directed towards. |
| `memberName` | Name of organization member that action was directed towards. |
| `policyId` | Organization policy update. See organization events [here](https://bitwarden.com/help/event-logs/#organization-events/). |
| `type` | The event type code that represents the organization event that occurred. See a complete list of event codes with descriptions [here](https://bitwarden.com/help/event-logs/). |
| `typeName` | Type numerical id. See mappings [here](https://github.com/bitwarden/splunk/blob/a9a6d6501c36d37ee7e95f88400c39f6ff2c926b/package/default/props.conf#L8). |

#### Spunk default fields

The following Splunk default fields will appear in queries. More information on the Splunk's default fields can be located in the [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/9.4.1/Knowledge/Usedefaultfields).

Fields:

- `source`
- `sourcetype`
- `date`

 - `date_hour
date_mday
date_minute
date_month
date_second
date_wday
date_year
date_zone`
- `index`
- `linecount`
- `punct`
- `splunk_server`
- `timestamp`

> [!NOTE] Null attribute in non-relevant event types
> Attributes that are not relevant to the event type will be reported as `null`.

**Search all:**

```
sourcetype="bitwarden:events" type=*
```

**Filter results by a specific field**

In the following example, the search is looking for `actingUserName `with a `* `wildcard which will display all results with `actingUserName`.

```
sourcetype="bitwarden:events" actingUserName=*
```

The **AND operator** is implied in Splunk searches. The following query will search for results containing a specific `type` AND * *`actingUserName.`

```
sourcetype="bitwarden:events" type=1000 actingUserName="John Doe"
```

Include multiple commands by separating with `|`. The following will show results with the top value being `ipAddress`.

```
sourcetype="bitwarden:events" type=1115 actingUserName="John Doe" | top ipAddress
```

## Additional resources

#### Set user roles

Manage users roles to allow individuals to perform specific tasks. To edit user roles:

1. Open the **Settings**menu on the top navigation bar. 

2. Select **Users** from the bottom right corner of the menu.

3. From the users screen, locate the user that you wish to edit permissions for and select **Edit**.

![Splunk edit user permissions](https://bitwarden.com/assets/5CnTzwphqVenaRu638uVoI/151e295ab1e06fad53698b648accf500/Screenshot_2023-04-13_at_9.48.48_AM__2_.png)

From this screen, details for the user can be filled out. Permission such as `admin`, `power`, and `can_delete` can be individually assigned here as well.

#### Delete data

Delete Bitwarden search data by clearing the index with SSH access. Data may need to be cleared in instances such as changing the organization being monitored. 

1. Access the Splunk directory and `stop` Splunk processes.
2. Clear the `bitwarden_events` index with `-index` flag. For example:

```plain text
splunk clean eventdata -index bitwaren_events
```
3. Restart Splunk processes.

## Troubleshooting

- Splunk Enterprise users, the app will log to: `/opt/splunk/var/log/splunk/bitwarden_event_logs.log

`If you are experiencing any errors, or the Bitwarden app is not functioning correctly, users can check the log file for errors or see [Spunk's documentation](https://docs.splunk.com/Documentation/Splunk/9.2.0/Indexer/RemovedatafromSplunk).
