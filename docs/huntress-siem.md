---
URL: https://bitwarden.com/help/huntress-siem/
---

# Huntress SIEM

Huntress is a managed security platform that provides threat detection, investigation, and response capabilities. Huntress Managed SIEM centralizes log data from across your environment and can be integrated with Bitwarden, giving security teams unified visibility into password management activity alongside the rest of their security environment. 

## Requirements

To setup Bitwarden as a log source in Huntress, you must:

- Have a Bitwarden Teams or Enterprise organization.
- Have a Huntress organization that includes Managed SIEM.
- Have administrative access to both Bitwarden and Huntress.

> [!NOTE] Bitwarden organizations vs. Huntress organizations
> Both Bitwarden and Huntress use the term "organization" to describe the entity that ties together users and data. Since you'll need to access both during setup, this document will disambiguate Bitwarden organizations and Huntress organizations where applicable.

## Add Bitwarden as a source

To add Bitwarden as a log source to the Huntress Managed SIEM platform:

1. In Huntress, navigate to **SIEM** → **Source Management**.

![Source Management](https://bitwarden.com/assets/30FE7CyWJrv4aztO5zNLXV/b5f85e14faaeb34f5023afe16ba7d54a/2026-02-18_13-12-18.png)
*Source Management*
2. Select **Add Source** and, from the dropdown, select **Bitwarden**.

![Add source](https://bitwarden.com/assets/33tJYy7Wg9swFU36TmSfsp/4a4d8198c5ee47f52f003c93d147623e/2026-02-18_13-13-34.png)
*Add source*
3. Select **Add**. If you have other pre-existing Bitwarden log sources, they'll also be listed on this page.
4. Select a configuration method. The method you choose will depend on whether your Bitwarden organization is on a Bitwarden cloud server or a self-hosted server:

### Cloud hosted

If your Bitwarden organization is on a Bitwarden cloud server (US or EU):

1. Choose **I am using Bitwarden's Cloud Hosting** and select **Next**.
2. From the **Organization** dropdown, select a Huntress organization that includes Managed SIEM.
3. Provide a **Name** that can be used to identify the integration and, optionally, a **Description**.
4. Select **Save**.
5. On the following page, take note of the **HTTP Event Collector URL**and **HTTP Event Collector Token**. You will need these values in a subsequent step.

> [!NOTE] Getting back to Huntress configuration details.
> If you click out of this view, you can re-retrieve these values by navigating back to the list of Bitwarden log sources, choosing the source, and selecting the [pencil] **Configure** button.
6. In Bitwarden, open the Admin Console and navigate to the **Integrations**page and **Event management** tab.
7. Scroll down to the Huntress card and select the **Connect Huntress** button:

![Integrations page](https://bitwarden.com/assets/1eVEp2giglyZSo8X4tBQ0E/59730bd09ab12bfee9d9a607a971eca0/huntress.png)
*Integrations page*
8. Copy your **HTTP Event Collector URL**and **HTTP Event Collector Token** from Huntress and paste them into the **Connect Huntress** panel in Bitwarden.
9. Select **Save**.

### Self-hosted

If your Bitwarden organization is on a self-hosted Bitwarden server:

1. Choose **I have a Self-Hosted Domain for Bitwarden**and select **Next**.
2. From the **Organization** dropdown, select a Huntress organization that includes Managed SIEM.
3. Provide a **Name** that can be used to identify the integration and, optionally, a **Description**.
4. Enter the **Base URL** of the API on your self-hosted server.
5. Enter your Bitwarden organization's [client ID and client secret](https://bitwarden.com/help/public-api/#authentication/), which will be used for authentication.
6. Select **Save**.
