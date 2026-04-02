---
URL: https://bitwarden.com/help/microsoft-sentinel-siem/
---

# Microsoft Sentinel SIEM

Microsoft Sentinel is a security information and event management (SIEM) platform that can be used to monitor Bitwarden organizations. Organizations can monitor [event](https://bitwarden.com/help/event-logs/) activity with the Bitwarden Event Logs app on Microsoft Sentinel.

## Setup

To setup the Bitwarden integration, an active Azure account with access to a Microsoft Sentinel Workspace is required. Additionally, a Bitwarden [API key](https://bitwarden.com/help/public-api/#authentication/), which can only be retrieved by [organization owners](https://bitwarden.com/help/user-types-access-control/).

## Install the Bitwarden app to your Microsoft Sentinel dashboard

The Bitwarden Event Logs application can be located in the [Microsoft Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/8bit-solutions-llc.bitwarden-sentinel-integration?tab=Overview). To add the new application to your Workspace:

1. Choose the Bitwarden Event Logs plan from the dropdown menu and select **Create**.

![Bitwarden Event Logs marketplace app](https://bitwarden.com/assets/7mrbZU5XylvwS9muqfXOM7/5f1216a644693655e970e66deb7dfbc2/2024-10-08_16-20-06.png)
2. Complete the required fields and select the Workspace that will be monitoring Bitwarden organization data.
3. Once complete, select **Review + create**.

## Connect your Bitwarden Organization

Once the Bitwarden Event Logs app has been added to your Microsoft Sentinel Workspace, you can connect your Bitwarden organization using your Bitwarden [API key](https://bitwarden.com/help/public-api/#authentication/).

1. Return to the **Data connectors** screen and select the Bitwarden Event Logs app. Select **Open connector page**. If the Bitwarden Event Logs app is not visible, you may be required to select [refresh] **Refresh.**

![Microsoft Sentinel Bitwarden Event Logs app](https://bitwarden.com/assets/7CoeRtrpz1i7JbbF6Tm91e/a6e46ad19099681aa4b93cfc6fb9ed69/2024-10-08_12-45-04.png)
2. Keep this screen open, on another tab, log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
3. Navigate to your organization's **Settings** → **Organization info** screen and select the **View API key**button. You will be asked to re-enter your master password in order to access your API key information. 

![Organization api info](https://bitwarden.com/assets/6gHjAyqgeqDj6UPT6agsBK/3a614e043cb3836a41bd68f226835e53/2024-12-04_09-51-07.png)
4. Return to the Microsoft Sentinel tab. On the **Configuration** page, complete the following fields:

| Field | Value |
|------|------|
| Bitwarden Identity URL | For Bitwarden cloud users, the default URL will be `https://identity.bitwarden.com `or `https://identity.bitwarden.eu`. For self-hosted Bitwarden users, input your self-hosted URL. For example, `https://<self-hosted-url>/identity`. Be sure that the URL does not include any trailing forward slashes at the end of the URL "`/`". |
| Bitwarden API URL | For Bitwarden cloud users, the default URL will be `https://api.bitwarden.com `or `https://api.bitwarden.eu`. For self-hosted Bitwarden users, input your self-hosted URL. For example, `https://<self-hosted-url>/api`. Be sure that the URL does not include any trailing forward slashes at the end of the URL "`/`". |
| Client ID | Input the value for `client_id` from the Bitwarden organization API key window. |
| Client Secret | Input the value for `client_secret` from the Bitwarden organization API key window. |

Select **Connect** once the required fields have been completed.

> [!NOTE] Org API information sensitive
> Your organization API key information is sensitive data. Do not share these values in nonsecure locations.

## Start monitoring event logs

> [!NOTE] Historic event data 
> Historic event data is not available for the Bitwarden Event Logs app on Microsoft Sentinel at this time. Additionally, it may take up to 1 hour for the first events to appear in Microsoft Sentinel.

Bitwarden organization event logs can be viewed in Microsoft Sentinel using the `BitwardenEventLogs` query function. 

1. From Microsoft Sentinel, select **Logs**. A New Query tab will be created. On the left hand navigation, select **Functions** → **Workspace functions**→**BitwardenEventLogs**.
2. Before running the query, you may select time frame and add specific parameters to the query. To being the query, select **Run**.

![Microsoft Sentinel query](https://bitwarden.com/assets/38MLy3Ieg9nf3YH4s50R1K/d4b9f6df7e1e5e42bbe84a2bbaf5afa5/image_480-1.png)

Queries can be saved for future use.

![Microsoft Sentinel query result](https://bitwarden.com/assets/B1P94UrwYOysKWh28oHJp/f6ab59d7f240b0519922fba9d0723598/image__1_.png)

### Monitor using Workbooks

Workbooks can be used to review event logs and visualize data. Additionally, templates are included in the Bitwarden Event Logs Workbook for a pre-configured overview of available data. 

To access Workbooks, select **Workbooks** from the navigation and then **Templates**.

![Workbook templates](https://bitwarden.com/assets/4eh5nlRZ1TCptqg8Q8Yz3T/55e09959de52e396a69f17f5509fdccd/workbooks.png)

The Bitwarden Event Logs app will have three templates included by default. Select one of the templates and choose **View Template** to begin monitoring data.

![Included templates](https://bitwarden.com/assets/2UfrEiMzlyVJcJ7P9Exaub/9e0664475aa6b357b5a3710e6ac268b8/included_templates.png)

The dashboards include visualized data:

![Microsoft Sentinel dashboard view](https://bitwarden.com/assets/3Wf1N2jRun1kROxJnjGrMy/ebe3cb8fddff817e8a00b1f2666a3f0e/BitwardenEventLogsAuthenticationWhite1.png)

Continue scrolling the overview page for additional event log data:

![Bitwarden even log view](https://bitwarden.com/assets/6wGNTITmTwvrzJXIJSZxJA/500b34ddb453cb63036a995e3c3db5d0/BitwardenEventLogsAuthenticationWhite2.png)

##
