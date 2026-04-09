---
URL: https://bitwarden.com/help/clear-sync-cache/
---

# Clear Sync Cache

Directory Connector keeps a local cache while syncing changes to your Bitwarden organization. This cache helps Directory Connector to **only send the deltas between the two directories** (before and after).

If a particular directory change is not syncing as expected or you encounter a sync error, like "An unhandled server error has occurred," try clearing this cache. Clearing the cache will trigger a full sync to occur during the next sync operation. To clear the local cache:

### Desktop

From the Directory Connector [desktop app](https://bitwarden.com/help/directory-sync-desktop/):

1. Select the **More** tab.
2. In the Other section, select the **Clear Sync Cache** button.

### CLI

Use the following command:

```
bwdc clear-cache
```
