---
URL: https://bitwarden.com/help/migrate-from-default-to-external-mssql/
---

# Migrate from Default to External MSSQL

This guide will walk you through migrating your self-hosted Bitwarden instance from the default MSSQL Express database to an [external MSSQL database](https://bitwarden.com/help/external-db/). This process:

- Requires downtime for your Bitwarden server.
- Requires administrative access to the Bitwarden server and both databases.
- Requires that the external database you're migrating to is MSSQL Server 2022.
- Requires that the external database you're migrating to is accessible from the Bitwarden host.

## Migrate in Docker deployments

Complete the following processes to migrate from the default MSSQL Express database to an external one in Docker deployment scenarios:

1. Create a [manual backup](https://bitwarden.com/help/backup-on-premise/) of your database:

```bash
docker exec -i bitwarden-mssql /backup-db.sh
```

The backup directory in the container is volume-mapped to the host, so your backup will be available as a `.BAK` file in `./bwdata/mssql/backups`.
2. Stop all Bitwarden containers in order to ensure data consistency during migration:

```bash
# Bash
./bitwarden.sh stop

# PowerShell
.\bitwarden.ps1 -stop
```
3. Upload the `.BAK` file to a place where it can be ingested into the new external MSSQL database. Methods will vary depending on your environment, but common methods include SCP or copying the file to a network share mounted on the new database server.
4. Restore the `.BAK` file to the new external MSSQL database. Methods will vary depending on your environment, but common methods include SMSS, T-SQL, or sqlcmd.
5. Verify that the `sa` account is active and on your new external MSSQL database at that you can access its password, as this will be used in your connection string for application access to the restored database and to avoid any user mapping issues.
6. In your [environment variables](https://bitwarden.com/help/environment-variables/) file (`global.override.env`), update at a minimum the database connection string used by the Bitwarden server:

```bash
globalSettings__sqlServer__connectionString="Data Source=your-sql-server.example.com,1433;Initial Catalog=database_name;User ID=sa;Password=sa_user_password;Encrypt=True;TrustServerCertificate=False;"
```

Check the other SQL [environment variables](https://bitwarden.com/help/environment-variables/) and adjust them as needed.
7. Restart your Bitwarden containers:

```bash
# Bash
./bitwarden.sh start

# PowerShell
.\bitwarden.ps1 -start
```

Once started:

 - Verify that the server is functioning by logging in and creating a test item.
 - Verify that the expected vault items and users accounts were successfully migrated.
