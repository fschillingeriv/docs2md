---
URL: https://bitwarden.com/help/clear-sync-cache/
---

# Clear Sync Cache

Directory Connector keeps a local cache while syncing changes to your Bitwarden organization. This cache helps Directory Connector to **only send the deltas between the two directories** (before / after).

If you encounter sync errors, or if a particular directory change is not being synced as expected, you should clear this cache. Clearing the cache will trigger a full sync to occur during the next sync operation. To clear the local cache:

### Desktop

From the Directory Connector [desktop app](https://bitwarden.com/help/directory-sync-desktop/):

1. Select the **More** tab.
2. In the Other section, select the **Clear Sync Cache** button.

### CLI

Use the following command:

```
bwdc clear-cache
```
