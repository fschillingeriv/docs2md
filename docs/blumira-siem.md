---
URL: https://bitwarden.com/help/blumira-siem/
---

# Blumira SIEM

Blumira is a security information and event management (SIEM) and extended detection and response (XDR) platform that centralizes log data from across your environment. Bitwarden integrates with Blumira by forwarding organization event log data, giving security teams unified visibility into password management activity alongside the rest of their security data.

Bitwarden sends events to Blumira using HTTP ingestion. After generating a unique endpoint and token in Blumira, you'll add those values to the Blumira integration in the Bitwarden Admin Console.

## Requirements

To set up Bitwarden as a log source in Blumira, you must:

- Have a Bitwarden Teams or Enterprise organization.
- Have a Blumira account with the ability to add HTTP ingestion instances.
- Have administrative access to both Bitwarden and Blumira.

## Setup

Integrating Bitwarden with Blumira will require short setup procedures in both platforms.

### Set up HTTP ingestion in Blumira

Before connecting from Bitwarden, generate the credentials that Bitwarden will use to send events to Blumira:

1. Log in to the Blumira app and go to **Ingestion** → **HTTP Ingestion**.
2. Select **Add Ingestion Instance**:

![Add an instance in Blumira](https://bitwarden.com/assets/1MI8gE0thIwBSXgvgkBUxX/82efcf3cf23be0862ff8efa06e001087/2026-05-20_09-42-37.png)
*Add an instance in Blumira*
3. In the setup window:

 - From the **Vendor**dropdown, select **Bitwarden**.
 - (Optional) Edit the pre-populated **Ingestion Instance Name**.
 - (Optional) Enter a **Description** for any additional context.
 - Select **Save**.
4. Your **Credentials** will be displayed, showing an **HTTP Event Collector URL** and **HTTP Event Collector Token**. Both are needed to complete the next section.

> [!NOTE] Blumira credentials
> The **HTTP Event Collector Token** will only be displayed once. Either copy and save this value to a secure location now, or keep the window open in a separate browser tab while you complete the Bitwarden side of setup.

### Connect to Blumira from Bitwarden

Once you have your **HTTP Event Collector URL** and **HTTP Event Collector Token**, provide that information in your Bitwarden organization to complete setup:

1. Log in to the Bitwarden web app and open the **Admin Console**.
2. In the Admin Console, go to **Integrations** → **Event management.**
3. Find the **Blumira** card and select **Connect**:

![Connect to Blumira from Bitwarden](https://bitwarden.com/assets/21ppzLWsQU55qNt44Hf2sN/8630153cae92e04e5c15babb1c2e010d/2026-05-20_10-14-45.png)
*Connect to Blumira from Bitwarden*
4. Enter your **HTTP Event Collector URL** and **HTTP Event Collector Token**.
5. Select **Save**.

## Additional resources

- Learn more about [what events are surfaced by Bitwarden](https://bitwarden.com/help/event-logs/).
- Learn more about [managing HTTP Ingestion in Blumira](https://blumirabeta.zendesk.com/hc/en-us/articles/51420656192147-Using-Blumira-HTTP-Ingestion).
