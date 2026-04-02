---
URL: https://bitwarden.com/help/provider-events/
---

# Provider Event Logs

## What are event logs?

Event logs are timestamped records of events that occur within your Provider. Event logs for the Provider are accessible only to [Provider admins](https://bitwarden.com/help/provider-users/) from the **Manage** → **Event logs** view of the Provider Portal:

![Provider event logs ](https://bitwarden.com/assets/78qTc5NI4nFDbpxWMDjwJz/e17201d717128c15e9fb55e55be6b57c/2024-12-05_09-44-47.png)

Selecting the **Export** button will create a `.csv` of all events within the specified date range:

![Export Provider event logs ](https://bitwarden.com/assets/1BYgVWThvhR5CWpNKBTuOT/862268581c453d9f3a0aa25df477f9ef/2024-12-05_09-44-47.png)

### Events

Event logs record several different types of events for Providers. The event logs screen captures a **Timestamp** for the event, client app information including the application type and IP (accessed by hovering over the [globe] globe icon), the **User** connected to the event, and an **Event** description. Provider events include:

- Invited user *user-identifier*
- Confirmed user *user-identifier*
- Edited user *user-identifier*
- Removed user *user-identifier*
- Accessed *organization-identifier* organization vault.
- Created organization *organization-identifier* (triggered when [a new organization is created within provider](https://bitwarden.com/help/client-org-setup/#create-a-client-organization/))
- Added organization *organization-identifier* (triggered when [an existing organization is added to provider](https://bitwarden.com/help/providers-faqs/#q-can-i-add-an-existing-organizations-to-my-provider/))
- Removed organization *organization-identifier*

> [!NOTE] Provider events not in event log
> Provider events do not currently roll up the events logged for each [client organization](https://bitwarden.com/help/providers/#client-organizations/). Provider users can access organization event logs from the client organization's vault. [Learn more](https://bitwarden.com/help/event-logs/).
