---
URL: https://bitwarden.com/help/backup-on%2Dpremise/
---

# Backup Server Data

When self-hosting Bitwarden, you are responsible for implementing your own backup procedures in order to keep data safe. Though the steps required to do so will depend on your deployment method, in all cases it is recommended that you:

- Manually take regular backups of important data, including configuration data, certificate data, and more.
- Ensure that automatically-recurring database backups are being taken.

> [!TIP] Recurring backups, by deployment
> In **Docker**deployments using the built-in database, a nightly backup runs as long as the `mssql` container is running. In **Helm** deployments, you will need to either schedule a job outside the cluster or create a CronJob object within the cluster, and Bitwarden provides examples to help guide your approach.

### Docker

## Manual backups

Bitwarden will take automatic nightly backups of the `mssql` database container (see below), however for the most complete disaster recovery (DR) plan you should manually backup and keep safe the entire `./bwdata` directory.

Particularly important pieces of `./bwdata` to backup regularly include:

- `./bwdata/env` - Instance's environment variables, including database and certificate passwords.
- `./bwdata/core/attachments` - Instance's vault item attachments.
- `./bwdata/mssql/data` - Instance's database data.
- `./bwdata/core/aspnet-dataprotection` - Framework-level data protection, including authentication tokens and some database columns.

You can also manually trigger a backup of the `mssql` database container at any time using the following command:

```bash
docker exec -i bitwarden-mssql /backup-db.sh
```

## Automatic database backups

Bitwarden will automatically take nightly backups of the `mssql` database container, as long as the container running. These backups are stored in the `./bwdata/mssql/backups` directory for 30 days.

> [!NOTE] Lite doesn't do nightly backups.
> [Bitwarden lite](https://bitwarden.com/help/install-and-deploy-lite/) does not take nightly backups. Using lite, you are required to manage your own backup processes.

### Restore a database backup

In the event of data loss, you can use `./bwdata/mssql/backups` to restore a nightly backup. Complete the following steps to restore a nightly backup:

1. Retrieve your database password from the `globalSettings__sqlServer__connectionString=...Password=` value found in `global.override.env`.
2. Identify the Container ID of the `mssql` container using the `docker ps` command.
3. Run the following command to open a bash session for your `mssql` docker container:

```
docker exec -it bitwarden-mssql /bin/bash
```

Your command prompt should now match the identified Container ID of the `bitwarden-mssql` container.
4. In the container, locate the backup file you wish to restore.

> [!NOTE]
> The backup directory in the container is volume-mapped from the host directory. `./bwdata/mssql/backups` on the host machine maps to `etc/bitwarden/mssql/backups` in the container.

For example, a file `/etc/bitwarden/mssql/backups/vault_FULL_20201208_003243.BAK` is a backup taken on December 08, 2020 at 12:32am.
5. Start the `sqlcmd` utility with the following command:

```bash
/opt/mssql-tools18/bin/sqlcmd -S localhost -U <sa> -P <sa-password> -C
```

where `<sa>` and `<sa-password>` match the `User=` and `Password=` values found in `global.override.env`.
6. Once in the `sqlcmd` utility, you have two options for backup:

 1. **Offline restore** (Preferred)

Run the following SQL commands:

```
1> use master
2> GO
1> alter database vault set offline with rollback immediate
2> GO
1> restore database vault from disk='/etc/bitwarden/mssql/backups/vault_FULL_{Backup File Name}.BAK' with replace
2> GO
​1> alter database vault set online
2> GO
1> exit
```

Restart your Bitwarden instance to finish restoring.
 2. **Online restore**

Execute the following SQL commands:

```
1> RESTORE DATABASE vault FROM DISK = '/etc/bitwarden/mssql/backups/vault_FULL_20200302_235901.BAK' WITH REPLACE
2> GO
```

Restart your Bitwarden instance to finish restoring.

### Helm

## Manual backups

Bitwarden provides example jobs that can be used to regularly backup your database (see below), however for the most complete disaster recovery (DR) plan you should manually backup and keep safe a wider array of server data.

Particularly important pieces of data to backup regularly include:

- Your chart's `my-values.yaml` file.
- Your [Kubernetes Secrets object](https://bitwarden.com/help/self-host-with-helm/#create-a-secret-object/) (typically, as a `.yaml` file).
- Any persistent volumes (PVCs) set up for:

 - `dataprotection`
 - `attachments`
 - `licenses`

## Recurring database backups

There are a variety of ways to schedule recurring database backups for your Bitwarden deployment. The Bitwarden Helm Charts repository contains [one such example for backing up the pre-packaged SQL container](https://github.com/bitwarden/helm-charts/tree/main/examples), which includes:

- Creating a Kubernetes Job object (`backup-job.yaml`) that establishes a connection to the database through Kubernetes Secrets, executes a backup, and stores the resultant `vault.bak` file to a persistent volume (PVC) while preserving prior backups.
- Creating a Bash script (`db-backup.sh`), intended for use by a task scheduler outside of the cluster, that will run the Kubernetes Job and monitor it in real-time.

## Restoring backups

To restore a backup, deploy a new Helm installation of Bitwarden with your backed-up `my-values` file and Kubernetes Secret object `.yaml` file. Once the chart is re-installed, re-attach your manually backed-up persistent volumes (PVCs) and `vault.bak` database backup.
