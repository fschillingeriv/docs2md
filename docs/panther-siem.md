---
URL: https://bitwarden.com/help/panther-siem/
---

# Panther SIEM 

Panther is a security information and event management (SIEM) platform that can be used with Bitwarden organizations. Organization users can monitor [event ](https://bitwarden.com/help/event-logs/)activity with the Bitwarden app on their Panther monitoring system. 

## Setup

### Create a Panther account

To start you will need a Panther account and dashboard. Create a Panther account on their [website](https://panther.com/). 

### Initialize Panther Bitwarden Log Source

1. Access the Panther dashboard.
2. On the menu, open the **Configure** dropdown and select **Log Sources**.

![Panther Log Sources](https://bitwarden.com/assets/2ZE57tHcy87V0qBKbUykRO/c0bf68f1da74c896562f87a85950138c/Panther_Log_sources.png)
3. Select **Onboard your logs**.

![Panther Onboard logs](https://bitwarden.com/assets/4mefTa7wGIZ6Kc62Mf9oNu/ab043ca54203609664765bcc0132158d/Panther_integration_marketplace.png)
4. Search **Bitwarden** in the catalogue. 

![Elastic Bitwarden integration](https://bitwarden.com/assets/3sSNvUFqgN8dwEWrfe0UFM/f9c1473e113c9851c506720992dfef2a/bitwarden_app.png)
5. Click on the **Bitwarden** integration and select **Start Setup**.

### Connect your Bitwarden organization

After you select **Start Setup** you will be brought to the configuration screen. 

> [!NOTE] Panther cloud organizations
> Panther SIEM services are only available for Bitwarden cloud hosted organizations.

1. Enter a name for the integration and then select **Setup.**
2. Next, you will have to access to your Bitwarden organization's **Client ID** and **Client Secret**. Keeping this screen open, on another tab, log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
3. Navigate to your organization's **Settings** → Organization info screen and select the **View API key**button. You will be asked to re-enter your master password in order to access your API key information.

![Organization api info](https://bitwarden.com/assets/6gHjAyqgeqDj6UPT6agsBK/3a614e043cb3836a41bd68f226835e53/2024-12-04_09-51-07.png)
4. Copy and paste the `client_id` and `client_secret` values into their respective locations on the Bitwarden App setup page. Once you have entered the information, continue by selecting **Setup**again.
5. Panther will run a test on the integration. Once a successful test has been completed, You will be given to option to adjust preferences. Complete the setup by pressing **View Log Source**.

> [!NOTE] Panther data ingestion
> Panther may take up to 10 minutes to ingest data following the Bitwarden App setup.

### Start monitoring data

1. To begin monitoring data, head over to the primary dashboard and select 🔍 **Investigate** and **Data Explorer**.
2. On the Data Explorer page, select the `panther_logs.public` database from the drop down menu. Make sure that `bitwarden_events `is being viewed as well.

![Panther Data Explorer](https://bitwarden.com/assets/3mrpsXxhYXiPHr5bAt2Dfk/9316f68edd7191180174869d37264752/data_explorer.png)
3. Once you have made all of your required selections, select **Run Query**.
You may also **Save as** to use the query at another time.
4. A list of Bitwarden events will be produced at the bottom of the screen.

![Panther Event Logs](https://bitwarden.com/assets/3iyy9chBYenrpJ5hCwVKOd/385e7d5348621b7c58649f0632f198b2/Panther_event_logs.png)
5. Events can be expanded and viewed in JSON by selecting **View JSON**. [arrow-circle-right].

![Panther JSON Object](https://bitwarden.com/assets/1wHDe1snFJ4NB1G13VBUBC/71def83a275e8bf25e25488b872a02f0/Header_object.png)

For additional information regarding Bitwarden organization events, see [here](https://bitwarden.com/help/event-logs/#organization-events/). Additional options for specific queries are available, see the [Panther Data Explorer](https://docs.panther.com/search/data-explorer) documentation for more information.

### 

###
