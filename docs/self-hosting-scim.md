---
URL: https://bitwarden.com/help/self-hosting-scim/
---

# Self-hosting SCIM

> [!NOTE] Self-host SCIM deployment style support
> The steps described in this article are for Docker standard deployments, in Helm deployments you will instead need to set `scim: true` in the `values.yaml` file to enable SCIM.

In order to use [SCIM](https://bitwarden.com/help/about-scim/) to automatically provision and de-provision members and groups in your self-hosted Bitwarden organization, you will need to enable a flag in your `config.yml` file. To enable SCIM for your Bitwarden server:

1. Save a [backup](https://bitwarden.com/help/backup-on-premise/) of, at a minimum, `.bwdata/mssql`. Once SCIM is in use, it's recommended that you have access to a backup image in case of an issue.

> [!NOTE] Using external MSSQL
> If you are using an [external MSSQL database](https://bitwarden.com/help/external-db/), take a backup of your database in whatever way fits your implementation.
2. Update your self-hosted Bitwarden installation in order to retrieve the latest changes:

```
./bitwarden.sh update
```
3. Edit the `.bwdata/config.yml` file and enable SCIM by toggling `enable_scim` to `true`.

```
nano bwdata/config.yml
```
4. Rebuild your self-hosted Bitwarden installation:

```
./bitwarden.sh rebuild
```
5. Update your self-hosted Bitwarden installation again in order to apply the changes:

```
./bitwarden.sh update
```

Now that your server has SCIM enabled, use one of our SCIM integration guides to integrate your Bitwarden organization with:

- [Microsoft Entra ID](https://bitwarden.com/help/microsoft-entra-id-scim-integration/)
- [Okta](https://bitwarden.com/help/okta-scim-integration/)
- [OneLogin](https://bitwarden.com/help/onelogin-scim-integration/)
- [JumpCloud](https://bitwarden.com/help/jumpcloud-scim-integration/)
