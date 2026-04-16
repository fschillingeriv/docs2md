---
URL: https://bitwarden.com/help/attachments/
---

# File Attachments

> [!NOTE] Attachments only available if you're paying
> File attachments are available for Premium users and members of paid [organizations](https://bitwarden.com/help/about-organizations/). These upgraded plans include 5GB of encrypted storage for file attachments per user. [More storage](https://bitwarden.com/help/attachments/#add-storage-space/) can be purchased in 1GB increments.

Files can be attached to any vault item, including [shared](https://bitwarden.com/help/sharing/) vault items, from any Bitwarden app. A file of any type that's 500 MB or smaller (100 MB or smaller, if uploading from mobile) can be attached to an item and up to 5 GB of total attachments (unless more storage is added) can be uploaded per account. Attachments are encrypted and decrypted locally, meaning no unencrypted attachment data is transported over the internet or stored by the server.

> [!NOTE] Sends and Attachments utilize storage space
> Attachments on individual vault items and all Sends use the individual storage space granted by premium subscriptions or organizations. Attachments on organization owned items use shared organizational storage space. Learn how to [add storage space](https://bitwarden.com/help/attachments/#add-storage-space/).

## Upload an attachment

To attach an attachment to a vault item:

### Web app

To attach a file from the web app:

1. Open the item and select **Edit**.
2. Scroll to the bottom of the **Edit** view and select **Attachments**.
3. Select **Choose File** and browse for your file.
4. Select **Upload**.
5. Select **Save**.

Once saved, the **Attachments** section will list all files attached to that item.

### Browser extension

To attach a file from the browser extension:

1. Open the item and select **Edit**.
2. Scroll to the bottom of the **Edit** view and select **Attachments**. The extension will pop out.
3. Select **Choose File** and browse for your file.
4. Select **Upload**.
5. Select **Save**.

Once saved, the **Attachments** section will list all files attached to that item.

### Mobile

To attach a file from the mobile app:

1. Open the item and select the ⋮ **Menu icon**.
2. Select **Attachments**.
3. Select **Choose file** and browse for your file.
4. Select **Save** in Android or the ✓ **Save icon** in iOS.

Once saved, the **Attachments** section will list all files attached to that item.

### Desktop

To attach a file from the desktop app:

1. Open the item and select **Edit**.
2. Scroll to the bottom of the **Edit** view and select **Attachments**.
3. Select **Choose File** and browse for your file.
4. Select **Upload**.
5. Select **Save**.

Once saved, the **Attachments** section will list all files attached to that item.

### CLI

Use `bw create attachment` to attach a file to an existing vault item, for example:

```
bw create attachment --file /path/to/myfile.ext --itemid <itemid>
```

For more information, please refer to the Bitwarden [CLI documentation](https://bitwarden.com/help/cli/).

## View an attachment

On **Android** devices, image files (`.jpeg`, `.png`, `.gif`, `.WebP`, `.heic`) can be previewed from directly within Bitwarden, without downloading them to your device, by tapping the attachment on the **View item** screen:

![View an attachment](https://bitwarden.com/assets/8CANFNTEL2gsoDy0zvQPG/65b328d7d01be571b66596c51f78d07d/2026-04-10_09-10-55.png)
*View an attachment*

## Download an attachment

To download an attachment from most Bitwarden apps, open the item. Within the **Attachments** section, select the ⬇️ **Download icon** next to the file.

For the **CLI**, use `bw get attachment` to download a file, for example:

```
bw get attachment photo.png --itemid 99ee88d2-6046-4ea7-92c2-acac464b1412 --output /Users/myaccount/Pictures/
```

For more information, please refer to the [CLI documentation](https://bitwarden.com/help/cli/#get-attachment/).

## Export all attachments

To create an export that includes attachments:

### Web app

To export your attachments from the web app:

1. Select **Tools** → **Export**from the navigation:

![Export items](https://bitwarden.com/assets/5PUGzasNsQnABG9gtso4o3/4e4880193ff45c22f0474c129e68e4e3/2025-12-17_11-43-59.png)
*Export items*
2. From the **File format** dropdown, select `.zip (with attachments)`. Currently, attachments can only be exported from your individual vault.
3. Select **Export**. You will need to confirm your permission to do this using your master password or an email verification code.

Your export file will be sent to your Downloads folder or wherever your web browser is set to download files to.

### Browser extension

To export your attachments from the browser extension:

1. Open the **Settings** tab.
2. Select **Vault options** and then **Export vault**.
3. From the **File format** dropdown, select `.zip (with attachments)`. Currently, attachments can only be exported from your individual vault.
4. Select **Export vault** button to finish. You will need to confirm your permission to do this using your master password or an email verification code.

Your export file will be sent to your Downloads folder or wherever your web browser is set to download files to.

### Desktop app

To export your attachments from the desktop app:

1. From the menu bar, navigate to **File** → **Export vault**.
2. From the **File Format** dropdown, select `.zip (with attachments)`. Currently, attachments can only be exported from your individual vault.
3. Select **Export vault**. You will need to confirm your permission to do this using your master password or an email verification code.

Your export file will be sent to your Downloads folder or wherever your web browser is set to download files to.

### CLI

To export your attachments from the CLI, use the command:

```bash
bw export --format zip
```

## Delete an attachment

To delete an attachment:

### Web app

To delete an attachment from the web app:

1. Open the item and select **Edit**.
2. Scroll to the bottom of the **Edit** view and select **Attachments**.
3. Select the 🗑️ **Delete** **icon** next to the attachment.
4. Select **Yes** to confirm.
5. Select **Save**.

### Browser extension

To delete an attachment from the browser extension:

1. Open the item and select **Edit**.
2. Scroll to the bottom of the **Edit** view and select **Attachments**. The extension will pop out.
3. Select the 🗑️ **Delete** **icon** next to the attachment.
4. Select **Yes** to confirm.
5. Select the [angle-left] **Back icon**.
6. Select **Save**.

### Mobile

To delete an attachment from the mobile app:

1. Open the item and select the ⋮ **Menu icon**.
2. Select **Attachments**.
3. Select the 🗑️ **Delete** **icon** next to the attachment.
4. Depending on your mobile device:

 - In Android, select **Delete** to confirm and then **Save**.
 - In iOS, select **Yes** to confirm and then the ✓ **Save icon**.

### Desktop

To delete an attachment from the desktop app:

1. Open the item and select **Edit**.
2. Scroll to the bottom of the **Edit** view and select **Attachments**.
3. Select the 🗑️ **Delete** **icon** next to the attachment.
4. Select **Yes** to confirm.
5. Select **Save**.

### CLI

Use bw delete attachment to delete a file attachment, for example:

```
bw delete attachment 7063feab-4b10-472e-b64c-785e2b870b92
```

For more information, please refer to the Bitwarden [CLI documentation](https://bitwarden.com/help/cli/).

## Add storage space

Paid users and members of paid [organizations](https://bitwarden.com/help/about-organizations/) have 5GB of encrypted storage for file attachments. Individuals and organizations can purchase additional storage space by completing the following steps:

> [!NOTE] Adding Storage Billing Impact
> Adding storage space will adjust your billing totals and immediately charge your payment method. The first charge will be prorated for the remainder of the current billing cycle.

### Individual

To add storage space in your individual vault:

1. In the Bitwarden web app, navigate to**Settings**→ **Subscription.**
2. In the Storage section, select the **Add Storage** button:

![Add storage to individual vault](https://bitwarden.com/assets/113yhHwt2fIgkjWjmPgCa4/f3df4d33206d35873c92266a546a9ed6/Add_storage_to_individual_vault.png)
*Add storage to individual vault*
3. Using the counter, choose the number of **GB of Storage to Add** and select **Submit**.

### Organization

To add storage space in your organization vault:

1. In the Bitwarden web app, Open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*
2. From the navigation, select **Billing**→ **Subscription**.
3. In the Manage subscription section, select the **Add Storage** button:

![Add storage to organization vault](https://bitwarden.com/assets/6tMMQEzEKXIRSa9fIUXuoh/3d9f81b717d3cee9681f1feda97d1b91/2024-12-02_15-28-55.png)
*Add storage to organization vault*
4. Using the counter, choose the number of **GB of Storage to Add** and select **Submit**.

### Self-hosted

While attachment storage is still tied to being a paid user or member of an organization when self-hosted, the **amount of storage** space is only limited by how much space is available on the volume that contains your attachments directory, with an upward limit of 10 TB (10240 GB). Users and admins **do not** need to change any values to increase that limit.

## Fixing old attachments

Prior to December 2018, file attachments used a different method of encrypting their data. We have since moved to a newer, better way of encrypting attachments. Any attachments that use the older encryption method will be labeled with an alert icon in your vault listing. You should upgrade these old attachments to the newer method of encryption so that other account-related features can function properly:

1. Open the vault item containing the old attachment and select **Edit**.
2. Scroll to the bottom of the Edit form and select **Attachments**.
3. Click the **Fix**button next to the old attachment. This process will download the attachment, re-encrypt it using the new encryption method, re-upload the attachment back to your vault, and delete the old version of the attachment.

Once an attachment has successfully been upgraded, the alert icon and fix button should disappear.
