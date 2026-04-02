---
URL: https://bitwarden.com/help/database-options/
---

# Database Options

## Default database for server deployments

All Bitwarden self-hosted server deployments, except for [Lite](https://bitwarden.com/help/install-and-deploy-lite/), ship with an MSSQL Express image by default. This colocates your encrypted vault data with the application containers and simplifies deployments by ensuring that updates, maintenance, and backups are delivered concurrently with the rest of the code.

This default database does not require additional licensing and is pre-configured to Bitwarden standards to securely store and automatically backup vault data ([learn more](https://bitwarden.com/help/backup-on-premise/)). 

### Using an external database for server deployments

In those self-hosted server deployments that are shipped with an MSSQL Express image, use of that container is optional. For high-availability or to leverage existing infrastructure, customers may connect to an external MSSQL server or cluster ([learn more](https://bitwarden.com/help/external-db/)) of version 2022. 

Regardless of whether you use the included MSSQL Express image or your own external MSSQL server or cluster, standard Bitwarden deployments must currently use MSSQL.

## Databases for Lite deployments

Bitwarden Lite self-host deployments do not ship with a built-in database, but can connect to an existing MySQL/MariaDB, MSSQL, SQLite, or PosgreSQL database ([learn more](https://bitwarden.com/help/install-and-deploy-lite/)). **Only lite deployments** support these database options, standard deployments require MSSQL.

> [!NOTE] Lite database require your management.
> Because Bitwarden lite databases are not provided by or collocated with the application container, database maintenance, including updates, maintenance, and backups, must be fully managed by you.

## Optional database jobs

### Database preparation

In non-Lite self-host deployments, Bitwarden will check for the existence of the database specified in the constructed connection string and, if it doesn't exist, create it. This job requires the configured SQL user to have administrative privileges within the database server. Insufficient privileges will cause this job to fail.

If you are deploying your own external database, deactivate this deployment step by setting the following environment variable in `global.override.env`:

```plain text
globalSettings__sqlServer__skipDatabasePreparation=true
```

### Database maintenance

In all self-hosted deployments, including Lite, Bitwarden runs scheduled jobs on the database to perform routine maintenance, such as computing database statistics and building indices. These jobs require the configured SQL user to have administrative privileges within the database server. Insufficient privileges will cause this job to fail, which will be logged to `admin` container logs.

If you prefer to run these maintenance jobs as a separate user, deactivate this behavior by setting the following environment variable in `global.override.env`:

```plain text
globalSettings__sqlServer__disableDatabaseMaintenanceJobs=true
```

> [!NOTE] Skipping database maintenance jobs
> If you deactivate database maintenance jobs, manually review database clean-up and index creations regularly.
