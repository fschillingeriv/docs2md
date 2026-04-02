---
URL: https://bitwarden.com/help/projects/
---

# Projects

Projects are collections of [secrets](https://bitwarden.com/help/secrets/) logically grouped together for management access by your DevOps and cybersecurity teams. Projects that your user account has access to are listed in the primary Secrets Manager view as well as by selecting **Projects** from the navigation:

![Projects](https://bitwarden.com/assets/71lYVBOdFFIcautbuha9k1/65abe5b658360c4dc3402d8d4f1c815c/2024-12-03_11-34-34.png)

Opening a project will list the **Secrets**, **People**, and **Machine accounts**associated with it:

![Inside a project](https://bitwarden.com/assets/7IlJQx9yhxuO5ffABmKyqd/bef389322630e365c40e3dfa386bae4d/2024-12-03_11-35-19.png)

## Create a project

To create a new project:

[![Vimeo Video](https://vumbnail.com/846445432.jpg)](https://vimeo.com/846445432)
*[Watch on Vimeo](https://vimeo.com/846445432)*

**Video Chapters:**
Learn more about projects [here](https://bitwarden.com/help/projects/).

1. Use the **New**dropdown to select **Project**:

![Create a project](https://bitwarden.com/assets/3gGgCYT0CgS3MKAngKDooL/03bd6080e1f8c695c46fd23918f56951/2024-12-03_11-25-44.png)
2. Enter a **Project name**. You can change the project's name at any time using the (⋮ ) options menu on the Projects page.
3. Select the **Save**button.

## Add secrets to a project

You can add both new and existing [secrets](https://bitwarden.com/help/secrets/) to your project:

### Add existing secrets

To add existing secrets to your project:

1. Navigate to the **Secrets**view and select the secret to add.
2. In the Edit Secret window, in the **Project**section, type or select the project to associate the secret with. Each secret can only be associated with a single project at a time.
3. When you're finished, select the **Save**button.

### Add new secrets

To create new secrets for your project:

1. Use the **New** dropdown to select **Secret**:

![Create a secret](https://bitwarden.com/assets/3uEcZ7G5L2TJM4QgMmFZ4H/24d73aa7121de9c77383f51de618db02/2024-12-03_11-29-17.png)
2. On the New Secret window's Name/Value pair tab, enter a **Name**and **Value**. Adding **Notes**is optional.
3. In the **Project** section, type or select the project to associate the secret with. A few key points.

 - Only organization members with access to the project will be able to see or manipulate this secret.
 - Only [machine accounts](https://bitwarden.com/help/machine-accounts/) with access to the project will be able to create a pathway for injecting or editing this secret.
 - Each secret can only be associated with a single project at a time.
4. When you're finished, select the **Save**button.

## Add people to a project

Adding organization members to your project will allow those people to interact with the project's secrets. To add people to your project:

1. In the project, select the **People**tab.
2. From the People dropdown, type or select the members or [groups](https://bitwarden.com/help/about-groups/) to add to the project. Once you've selected the right people, select the **Add**button:

![Add people to a project](https://bitwarden.com/assets/4Vu9wuBd8ceEz7ji7V2kHZ/2f11a06f3ed09a1cd64190ad8197e914/2024-12-03_11-27-19.png)
3. Once members or groups are added to the project, set a level of **Permissions**for those members or groups. Members and groups can have one of the following levels of permission:

 - **Can read**: Members/groups will be able to view existing secrets in this project.
 - **Can read, write**: Members/groups will be able to view existing secrets and create new secrets in this project.

## Add machine accounts to a project

You can add both new and existing [machine accounts](https://bitwarden.com/help/machine-accounts/) to the project:

### Add existing machine accounts

To add existing machine accounts to your project:

1. In the project, select the **Machine accounts**tab.
2. From the Machine accounts dropdown, type or select the machine account(s) to add to the project. Once you've selected the right machine accounts, select the **Add**button:

![Add a machine account](https://bitwarden.com/assets/1IJNE4LCOMqQsAMBYKN5pe/187a4d47245bfbd750e13aa052dc6fb3/2024-12-03_11-36-39.png)
3. For each added project, select a level of **Permissions:**

 - **Can read**: Machine account can retrieve secrets from assigned projects.
 - **Can read, write**: Machine account can retrieve and edit secrets from assigned projects, create new secrets in assigned projects, or create new projects altogether.

> [!TIP] SM 07/25 dependency
> Fully utilizing write access for machine accounts is dependent on a forthcoming [CLI](https://bitwarden.com/help/secrets-manager-cli/) release. For now, this simply makes the option available in the UI. Stay tuned to the [Release Notes](https://bitwarden.com/help/releasenotes/) for more information.

### Add new machine accounts

To add a machine account for this project:

1. Use the **New**dropdown to select **Machine account**:

![New machine account](https://bitwarden.com/assets/LaVwicbqhvbliXPm6loOU/5559a5caf8ad70a95be3ea89f1b760ad/2024-12-03_11-29-17.png)
2. Enter a **Machine account name** and select **Save**.
3. Open the machine account and, in the **Projects** tab, type or select the name of the project(s) that this service account should be able to access. For each added project, select a level of **Permissions:**

 - **Can read**: Machine account can retrieve secrets from assigned projects.
 - **Can read, write**: Machine account can retrieve and edit secrets from assigned projects, as well as create new secrets in assigned projects or create new projects.

> [!TIP] SM 07/25 dependency
> Fully utilizing write access for machine accounts is dependent on a forthcoming [CLI](https://bitwarden.com/help/secrets-manager-cli/) release. For now, this simply makes the option available in the UI. Stay tuned to the [Release Notes](https://bitwarden.com/help/releasenotes/) for more information.

## Delete a project

To delete a project, use the (⋮ ) options menu for the project to delete to select **Delete project**. Deleting a project **will not**delete the secrets associated with it. Projects are fully removed once deleted and **do not** get [sent to the trash like secrets do](https://bitwarden.com/help/secrets/#delete-a-secret/). Enter the name of the project into the Delete project dialogue and select **Delete project**.
