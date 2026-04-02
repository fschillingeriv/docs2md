---
URL: https://bitwarden.com/help/user-group-filters/
---

# Sync Options and Filters

When configuring the Directory Connector application, you can use a variety of sync options and filters to customize your sync operation and limit the users and/or groups that are processed to your Bitwarden organization.

Available sync options and filter syntaxes are different for each directory server type. Refer to the **Configure sync options** and **Specify sync filters** sections of one of the following articles for help:

- [Sync with Active Directory or LDAP](https://bitwarden.com/help/ldap-directory/)
- [Sync with G Suite (Google)](https://bitwarden.com/help/workspace-directory/)
- [Sync with Microsoft Entra ID](https://bitwarden.com/help/microsoft-entra-id/)
- [Sync with Okta](https://bitwarden.com/help/okta-directory/)
- [Sync with OneLogin](https://bitwarden.com/help/onelogin-directory/)

> [!NOTE] CLI json storage configuration 
> If you are using the Directory Connector CLI, see [Directory Connector File Storage](https://bitwarden.com/help/directory-sync-shared/) for help editing your `data.json` configuration file.

## Large syncs

Regardless of which directory you are syncing from, use the **More than 2000 users or groups are expected to sync** option to signal to Directory Connector that you are expecting a large number of users or groups:

![Signal a Large Sync](https://bitwarden.com/assets/2vEokum2rZLMpp59jsAjKz/6b5566af0acb05215be6756ac11d5fa8/Screen_Shot_2022-05-24_at_10.37.15_AM.png)

You may also activate this option directly in the Directory Connector [configuration file](https://bitwarden.com/help/directory-sync-shared/#config-file/) (`data.json`) by setting `"largeImport": true`:

```
"syncConfig": {
 ...,
 ...,
 ...,
 "largeImport": true
 },"
```

> [!NOTE]
> If you don't enable this option, Directory Connector will limit a sync to 2000 users or groups.

## Overwriting syncs

> [!WARNING] BWDC Overwrite
> This option is for very specific use-cases or debugging purposes and is disabled by default.

By activating the **Remove and re-add organization users during the next sync** option, every user except one owner user and every group will be removed and re-added by a sync, replacing them with the user list and/or group list that is fetched from the source directory.

![Remove and re-add users during next sync](https://bitwarden.com/assets/sM0wG9htsgHvpsXx1E1t9/929c1601a0f6d6c55a576e6154d89d31/2024-12-12_10-58-15.png)

You may also enable this option directly in the Directory Connector [configuration file](https://bitwarden.com/help/directory-sync-shared/#config-file/) (`data.json`) by setting `"overwriteExisting": true`:

```
"syncConfig": {
 ...,
 ...,
 ...,
 "overwriteExisting": true
 },"
```
