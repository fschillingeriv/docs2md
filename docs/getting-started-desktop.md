---
URL: https://bitwarden.com/help/getting-started-desktop/
---

# Password Manager Desktop Apps

The Bitwarden desktop app brings a full vault experience straight out of your browser and into your desktop. The desktop app supports up to five logged-in accounts at a time, making it easy to switch between personal and work accounts at any moment ([learn more](https://bitwarden.com/help/account-switching/)).

In the 🔒 **My** **Vault** view, you can browse all your items, including items owned by an organization that you are a member of. Use the Vaults dropdown to filter for items in **All Vaults**, **My Vault,**and any organization vaults.

![Password Manager on desktop](https://bitwarden.com/assets/79qrrbQ4Oi7ZGUnSrE3VpZ/9e8a86298c65c028e9280a36d0bcb99f/2026-01-28_09-42-19.png)
*Password Manager on desktop*

## First steps

Let's start your desktop app journey by adding a new login item to your vault and making sure it's secure and easy to find: 

### Create a folder

[Folders](https://bitwarden.com/help/folders/) are a great way to make sure you can always find vault items when you need to use them. To create a folder:

1. In the first column of the desktop app, select + **Add** next to **Folders**.
2. Give your folder a name (for example `Social Media`) and select [save] **Save.**

### Add a login

Now, let's add a login to your new folder. To create a new login item:

1. In the middle column, select + **Add**. An Add Item panel will be displayed in the third column.
2. Choose which type of item to create (in this case, select **Login**).
3. Enter the basic information for this login. For now, give the item:

 1. A **Name** to help you easily recognize it (for example, `X.com Account`).
 2. Your **Username**.
 3. Your current **Password** (we'll replace this with a strong one soon).
4. Select the + **New URI**button and enter the URL where you log in to the account (for example, `https://x.com/i/flow/login`).

![X.com Login URI](https://bitwarden.com/assets/5jf74Y0xH5LXouxuBLfER0/02aca3fb33feb85d0a05ecbd06e00ba5/x.comlogin_close_up.png)
5. Select a folder from the Folder dropdown. If you are following our example, choose the Social Media folder we just created!
6. Nice work! Select [save] **Save**to finish.

> [!TIP] Import from desktop app
> You can also import data directly to Bitwarden from your desktop app. [Learn how](https://bitwarden.com/help/import-data/#tab-desktop-app-5ALQx9afSqWXX9jfXsY5sb/).

### Generate a strong password

Now that you have saved a new login, let's improve its security by replacing your password with a strong one:

1. Open a web browser and login to the account with your existing username and password. In that account, find where you can **Change your password**.
2. On the **Change your password** form, enter your **Current password**, which you can copy and paste from Bitwarden using the [clone] **Copy** icon.
3. In Bitwarden, select [pencil] **Edit**on your item.
4. In the Password box, select [generate] **Generate** and confirm **Yes**to overwrite your old password.

This will replace your password with a randomly-generated strong password. Moving from `Fido1234` to `X@Ln@x9J@&u@5n##B` can stop a would-be hacker in their tracks.
5. Select [save] **Save.**
6. Copy your new password with the [clone] **Copy** icon you used earlier, and paste your new password in the **New Password**and **Confirm New Password**fields back in your web browser.
7. Once you are done, select **Save**in the web browser.

Congratulations! Your login is now saved in Bitwarden for secure and easy use!

### Add a second account

Do you have multiple Bitwarden accounts, perhaps one for personal use and one for work? The desktop app can be logged in to five accounts at once! 

To login to an additional account, select the currently logged-in account from the top-right of the desktop app and select + **Add Account:**

![Switch accounts on desktop](https://bitwarden.com/assets/7fpUmakpNIByzoWQa1cU8L/1062adaaed12e43a9c53e8e182453c96/2026-01-28_09-08-28.png)
*Switch accounts on desktop*

Once you log in to your second account, you can quickly swap between them from the same menu, which will also show the current status of each account's vault (*locked *or *unlocked*). If you log out of one of these accounts, it will be removed from this list.

## Next steps

Now that you have mastered the basics, you can customize your desktop app to work exactly the way you want it to:

### 🪟 Windows

### Set your preferences

To set your preferences, select **File** → **Settings**from the menu bar. You'll notice three sections; **Security**, **Preferences**, and **App Settings**.

> [!TIP] Desktop Preferences
> **Security** and **Preferences** apply to the [active account](https://bitwarden.com/help/getting-started-desktop/#add-a-second-account/) and should be set separately for each account, but **App Settings** apply to all accounts.

#### Unlock with biometrics

One of the most popular desktop app settings is [unlock with biometrics](https://bitwarden.com/help/biometrics/), which allows for seamless access using [Windows Hello](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello) with PIN, facial recognition, or [other hardware that meets Windows Hello biometric requirements](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello-biometric-requirements). To setup biometric unlock:

> [!TIP] Biometrics C++ Redistributable
> Windows users may need to install the [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) before Windows Hello can be turned on in desktop preferences.

1. Enable Windows Hello on your computer.
2. In the Security section, an **Unlock with Windows Hello** option will appear if Windows Hello is supported and enabled on your computer:

![Windows unlock options ](https://bitwarden.com/assets/HQYTF4l5WyPbeTMHhhDnN/fe4ddb713557443e7836f3737534ca1e/windows.png)

Check the **Unlock with Windows Hello** option to proceed. Your computer will prompt you to input your biometric.
3. Once enabled, use the **Unlock with Windows Hello**button on the unlock screen to unlock your vault.

![Unlock desktop with biometric](https://bitwarden.com/assets/JSmueUxWjUGxQK0bA716O/f6bcfa6ec4523b8080a77e418e1eae8e/2025-08-13_11-20-59.png)

**Security**settings are set per-account, so if you want to enable biometric unlock for another account you'll need to go through these steps again!

#### Start Bitwarden automatically

Another helpful feature is to always start Bitwarden when you boot up your computer. To enable this, navigate to the **App Settings** section and check the **Start automatically on login** checkbox.

Unlike biometrics, this setting applies globally to all logged-in accounts!

### 🍎 macOS

### Set your preferences

To set your preferences, select **Bitwarden** → **Settings**from the menu bar. You'll notice three sections, **Security**, **Preferences**, and **App Settings**.

> [!TIP] Desktop Preferences
> **Security** and **Preferences** apply to the [active account](https://bitwarden.com/help/getting-started-desktop/#add-a-second-account/) and should be set separately for each account, but **App Settings** apply to all accounts.

#### Unlock with biometrics

One of the most popular desktop app settings is [unlock with biometrics](https://bitwarden.com/help/biometrics/), which allows seamless access to your desktop app using [Touch ID](https://support.apple.com/en-us/HT207054) technology. To setup biometric unlock:

1. Enable Touch ID on your computer. See Apple's [Touch ID Documentation](https://support.apple.com/en-us/HT207054) for help.
2. In the Security section, an **Unlock with Touch ID** option will appear if Touch ID is supported and enabled on your computer:

![macOS unlock options](https://bitwarden.com/assets/3O1If6IchE83Qb8ee0mYqx/9c61afb380d8479eb4e55e97c2e628c6/macos-bio1.png)

Check the **Unlock with Touch ID** checkbox to proceed. Your computer will prompt you to input your fingerprint to confirm.
3. Once enabled, use the **Unlock with Touch ID**button on the Unlock screen to unlock your vault.

![Unlock with Touch ID ](https://bitwarden.com/assets/MPQwBfgcoTZJvan99sZCZ/e7a2305ffdc24af1fc08adf466463841/mac_unlock_with_touch_id.png)

**Security**settings are set per-account, so if you want to enable biometric unlock for another account you'll need to go through these steps again!

#### Start Bitwarden Automatically

Another helpful feature is to always start Bitwarden when you boot up your computer. To enable this, navigate to the **App Settings** section and check the **Start automatically on login** checkbox.

Unlike biometrics, this setting applies globally to all logged-in accounts!

### 🐧 Linux

### Snap post-installation instructions

The Bitwarden Password Manager desktop app uses secure storage for persisting authentication tokens while you are logged in to the application. **If you use Snap to install the desktop app**, you will need to allow the app to access secure storage by:

1. On all distributions, run the command `sudo snap connect bitwarden:password-manager-service`.
2. If you've already logged in to the Password Manager desktop app, log out of all accounts and log back in.

### Set your preferences

To set your preferences, select File → Settings from the menu bar. You'll notice three sections; **Security**, **Preferences**, and **App Settings**.

> [!TIP] Desktop Preferences
> **Security** and **Preferences** apply to the [active account](https://bitwarden.com/help/getting-started-desktop/#add-a-second-account/) and should be set separately for each account, but **App Settings** apply to all accounts.

#### Unlock with biometrics

One of the most popular desktop app settings is [unlock with biometrics](https://bitwarden.com/help/biometrics/), which allows seamless access to your desktop app. Bitwarden desktop apps from `AppImage`, `Deb`, and `.rpm` package types are supported`.` Additionally, confirm that your system has a polkit agent and secret service (such as GNOME-Keyring). To enable biometric unlock:

1. Enable System Authentication on your machine.
2. In the Security section of your Bitwarden desktop app, an enable **Unlock with system authentication** option will appear if system authentication is supported and enabled on your machine:

![Unlock with system authentication](https://bitwarden.com/assets/2AMdLd9zqVZwkDMfS1ZW00/bfe0b4bd4b93541fed04563e55722358/Aug_15_Screenshot_from_Bitwarden.png)

Check the **Unlock with system authentication**checkbox to proceed. You machine will prompt you to input your verification to confirm.
3. Once enabled, use **Unlock with system authentication** button on the unlock screen to unlock your vault.

![Unlock vault system authentication](https://bitwarden.com/assets/6UIFh90LrxZzgrbacuMw3o/ef9b39a24775d098f1ad9825094206f0/Aug_15_Screenshot_from_Bitwarden__1_.png)

Security settings are set per-account, so if you want to enable biometric unlock for another account you'll need to go through these steps again!

### Start Bitwarden automatically

One helpful feature is to always start Bitwarden when you boot up your computer. To enable this, navigate to the **App Settings** section and check the **Start automatically on login** checkbox.

Remember that this setting applies globally to all logged-in accounts!
