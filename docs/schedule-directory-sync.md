---
URL: https://bitwarden.com/help/schedule-directory-sync/
---

# Schedule a Sync

For organizations using the [Directory Connector CLI](https://bitwarden.com/help/directory-sync-cli/), automatic syncs can be scheduled on defined intervals as an alternative to using the desktop app's **Interval** setting. This is particularly useful in headless environments, or in circumstances where a desktop app cannot be left running in the background.

To schedule syncs, use **Cron** in Unix-like environments including Linux and MacOS, and use **Task Scheduler** in Windows environments:

### Cron

### Cron permissions

When running a cron job, we recommend doing so as a dedicated Directory Connector user. Create a `bwdc` user if you haven't already, and add that user to the `etc/cron.allow` list. This will allow a non-Root user to set up and run cron jobs.

In order to continue, you will also need your organization's [API key](https://bitwarden.com/help/public-api/#authentication/) `client_id` and `client_secret`, which can be obtained by an organization **owner** from the Web Vault by navigating to organization **Settings** → **My Organization**.

### Setup a sync script

In order avoid session timeouts, we recommend creating a shell script to run through cron. This script should securely read your `client_secret` to complete the login, and run a `bwdc sync` command that writes output to `bwdc.log`.

> [!TIP] (BWDC) Sync from multiple directories
> Need to sync from multiple directories? In your sync script, you can specify multiple folders, each of which must contain a `data.json` file with your directory sync settings. 
> 
> You can then specify each directory to sync by performing multiple `bwdc sync` operations, for example:
> 
> 
> ```bash
> # Linux
> BITWARDENCLI_CONNECTOR_APPDATA_DIR="./instance-1" bwdc sync
> BITWARDENCLI_CONNECTOR_APPDATA_DIR="./instance-2" bwdc sync
> 
> # Windows
> set BITWARDENCLI_CONNECTOR_APPDATA_DIR=./instance-1
> bwdc sync
> set BITWARDENCLI_CONNECTOR_APPDATA_DIR=./instance-2
> bwdc sync
> ```

### Setup the cron job

As the permitted `bwdc` user:

1. Edit the user's crontab file by entering `crontab -e` in the terminal, or as edit the crontab file as any user by entering `crontab -u <bwdc_username> -e`.
2. Add a line to the crontab that includes:

 - A scheduling expression that will determine the time/recurrence interval on which to execute the desired command (for example, `0 0 * * 2` to run every Tuesday at midnight).
 - The command to execute at the specified time/recurrence interval. In this case, execute the previously created sync script (for example, `bwdcSyncService.sh`):

For example, to run the sync script every Monday at 12:00:

```
# 0 12 * * 1 bwdcSyncService.sh
```

#### Cron job scheduling expressions

Use the following reference when scheduling syncs via cron to ensure you're scheduling them for the desired time:

```
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │ 7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * <command to execute>
```

> [!NOTE]
> If you're not yet comfortable with cron job scheduling expressions, check out [https://crontab.guru/](https://crontab.guru/) for help.
> 
> Please note, this is a third-party resource that is not operated or maintained by Bitwarden.

### Task Scheduler

### Task Scheduler permissions

When running a task, we recommend doing so as a dedicated Directory Connector user. Create a `bwdc` user if you haven't already.

In order to continue, you will also need your organization's [API key](https://bitwarden.com/help/public-api/#authentication/) `client_id` and `client_secret`, which can be obtained by an organization **owner** from the web app by navigating to organization **Settings** → **My Organization**.

### Setup a sync script

In order to avoid session timeouts, you will need to create a script to run as the Task Scheduler action. This script should securely read your `client_secret` to complete the login, and run a `bwdc sync` command that writes output to `bwdc.log`.

> [!TIP] (BWDC) Sync from multiple directories
> Need to sync from multiple directories? In your sync script, you can specify multiple folders, each of which must contain a `data.json` file with your directory sync settings. 
> 
> You can then specify each directory to sync by performing multiple `bwdc sync` operations, for example:
> 
> 
> ```bash
> # Linux
> BITWARDENCLI_CONNECTOR_APPDATA_DIR="./instance-1" bwdc sync
> BITWARDENCLI_CONNECTOR_APPDATA_DIR="./instance-2" bwdc sync
> 
> # Windows
> set BITWARDENCLI_CONNECTOR_APPDATA_DIR=./instance-1
> bwdc sync
> set BITWARDENCLI_CONNECTOR_APPDATA_DIR=./instance-2
> bwdc sync
> ```

### Create a task

As the dedicated `bwdc` user:

1. Open Task Scheduler and select **Create Task** from the Actions menu.
2. Configure the task with the following security options:

 - Set the task to use the created `bwdc` user.
 - Set the task to **Run whether user is logged on or not**.
3. Select the **Triggers** tab and select the **New...** button to create a trigger that fits your directory sync needs.

> [!NOTE] Create weekly trigger
> For example, you could create a weekly trigger that runs at 8:00 PM every Sunday or every week:
> 
> ![Using Task Scheduler](https://bitwarden.com/assets/6GPFmp4DqONQyQ89jqq5mp/6d17bf8f050ee905b35b43c4061693ee/taskscheduler-trigger.png)
4. Select the **Actions** tab and select the **New...** button to create an action that runs the created sync script.
5. Select **OK** to finish creating the scheduled task.
