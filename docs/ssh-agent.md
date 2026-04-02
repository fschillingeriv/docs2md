---
URL: https://bitwarden.com/help/ssh-agent/
---

# SSH Agent

Bitwarden Password Manager desktop app can act as an SSH Agent to securely encrypt and store your SSH (Secure Shell) keys for use with:

- Authenticating to servers
- Signing Git commits
- Interacting with SSH based services

The Bitwarden SSH Agent will organize and protect your keys in one secure location. SSH keys can be accessed with the desktop app, web app, browser extension, and mobile app. SSH keys can be generated using the desktop app, web app, and browser extension.

> [!NOTE] SSH agent availability
> The SSH Agent requires release version 2025.1.2 or newer.

## Storing an SSH key

New SSH keys can be created and saved in the Bitwarden desktop app. Bitwarden SSH keys will store:

| Field | Description |
|------|------|
| Key name | The name for your SSH key. |
| Private key | The private key is sensitive data that will be used by the server to facilitate secure connection. Private key data should be treated with care and kept secure. Users may use Bitwarden to generate a secure, unique private key. |
| Public key | Portion of the key shared with the server that you will be connecting to. |
| Fingerprint | A short unique string generated from the public key for identification. For example, SSH-signed git commits can be verified using the fingerprint. |

SSH keys stored in the Bitwarden Password Manager will have access to Bitwarden features such as [folders](https://bitwarden.com/help/folders/), [favorites](https://bitwarden.com/help/favorites/), [master password re-prompt](https://bitwarden.com/help/managing-items/#protect-individual-items/), notes, [cloning items](https://bitwarden.com/help/managing-items/#clone/), [attachments](https://bitwarden.com/help/attachments/), and [custom fields](https://bitwarden.com/help/custom-fields/).

## Create new SSH key

Create a new SSH key using the Bitwarden desktop app, web app, or browser extension. Once created, SSH keys stored in Bitwarden can be accessed from the desktop app, web app, browser extension, and mobile apps.

1. Select the **New** button and choose **SSH key** as the item type:

![Create new SSH key on desktop](https://bitwarden.com/assets/1XYC3HwXOTMAPvyW1GS3Mk/5c7833241844eded5fa119d44d6efebd/new-ssh.png)
*Create new SSH key on desktop*

> [!NOTE] Create SSH key only ED25519
> At this time, Bitwarden can only generate `ED25519` type SSH keys.
2. Fill in remaining details such as **Name**and select the [save-changes] Save icon once complete.

### Organization SSH keys

SSH keys can be created and stored in an organization collection. Organization members with appropriate permissions may create, manage and access SSH keys owned by an organization. Learn more about collection permissions [here](https://bitwarden.com/help/collection-permissions/).

To add a new shared SSH key to the organization vault:

1. On the Vault view of the desktop or web app, select the + **New button** and select **SSH key**.

> [!TIP] Can also be done from Admin Console
> Organization [owners, admins, and some custom users](https://bitwarden.com/help/user-types-access-control/) can also take this step directly from the **Admin Console** to skip some of the steps in this process.
2. Using the **Owner** dropdown, choose the organization you want this item to be owned by.
3. Using the **Collections** dropdown, choose the collection(s) to share this item with.

![Share an SSH key](https://bitwarden.com/assets/1YnrhzwCw78KuFsArEioOO/b7db01ff5dbd209ebe30f6454275ba41/Share-ssh.png)
*Share an SSH key*

> [!NOTE] SSH key sharing best practices
> In general, resources that use SSH keys can support per-user keys. We recommend reviewing SSH key best practices before sharing SSH keys to an organization.

### Edit existing keys

Once an SSH key has be saved in your Bitwarden vault, you may edit some of the key fields such as name, owner, folder and custom fields:

### Desktop

To edit SSH keys on the Bitwarden desktop app:

1. Open the Bitwarden desktop app and navigate to **SSH keys**.
2. Locate the SSH key you wish to edit and then select [pencil] **Edit**.
3. Once you have completed the desired changes, select [save-changes] **Save**.

### Web app

To edit SSH keys on the Bitwarden web app:

1. Open the Bitwarden web app and navigate to **SSH keys**.
2. Locate and select the SSH key you wish to edit. A dialogue will appear on screen, then select **Edit**.
3. Once you have completed the desired changes, select **Save**.

### Mobile

To edit SSH keys on the Bitwarden mobile app:

1. Open the Bitwarden mobile app and navigate to **SSH keys**.
2. Locate the SSH key you wish to edit and then select **Edit**.
3. Once you have completed the desired changes, select **Save**.

### Browser extension

To edit SSH keys on the Bitwarden browser extension:

1. Open the Bitwarden browser extension and navigate to **SSH keys**.
2. Locate and select the SSH key you wish to edit. A dialogue will appear on screen, then select **Edit**.
3. Once you have completed the desired changes, select **Save**.

## Import key to Bitwarden

The import function for SSH keys is available on the Bitwarden desktop app. Using the Bitwarden desktop app:

1. Select the **New** button and choose **SSH key** as the item type.
2. Copy the existing SSH key you wish to import into Bitwarden.
3. Use the **Import key from clipboard** icon. This will automatically paste the SSH key into Bitwarden.

 - At this time, imported keys must be in **OpenSSH** or **PKCS#8** format.

![Import an SSH key](https://bitwarden.com/assets/5QTvyu39h3o0azkjU26P3t/77e877af88307d167daf0f292a38dd03/import-ssh.png)
*Import an SSH key*

> [!NOTE] import SSH must be in OpenSSH format
> At this time, imported SSH keys from Putty are not compatible.

## Configure Bitwarden SSH agent

In order to use Bitwarden as your primary SSH Agent, you will be required to configure your SSH client to communicate with Bitwarden for authentication.

### Windows

To enable the Bitwarden SSH Agent on Windows, you must disable the OpenSSH service on your Windows machine. To disable OpenSSH:

1. On your Windows machine, navigate to **Services → OpenSSH Authentication Agent**. Services can be located with the Windows search bar.

![Windows Services panel](https://bitwarden.com/assets/77fTJpxIBH5ikJYQW1KFL7/0c6fa3b9f68f7a85569ad6ede489979e/openSSH_agent.png)
2. Once you have opened the OpenSSH Authentication Agent Properties window, set the **Startup type** setting to **Disabled**.

![Disable OpenSSH Windows](https://bitwarden.com/assets/6Ghl3WkroGhoyy4fUMDbCg/800780f201fff9d6dc2de3d6577587ac/Screenshot_2024-12-04_142322.png)
3. Once the settings have been adjusted, select **Apply** and then **OK**.

### macOS

#### macOS store

Enable the Bitwarden SSH Agent on macOS store download:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. The following example demonstrates how to do this after replacing `<user>` with your username:

```plain text
export SSH_AUTH_SOCK=/Users/<user>/Library/Containers/com.bitwarden.desktop/Data/.bitwarden-ssh-agent.sock
```

#### .dmg download

Enable the Bitwarden SSH Agent on macOS .dmg download:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. The following example demonstrates how to do this after replacing `<user>` with your username:

```bash
export SSH_AUTH_SOCK=/Users/<user>/.bitwarden-ssh-agent.sock
```
2. Alternatively, configure `SSH_AUTH_SOCKET`:

```plain text
launchctl setenv "SSH_AUTH_SOCKET" "/Users/<user>/.bitwarden-ssh-agent.sock"
```

> [!NOTE] launchctl require terminal restart
> You may need to restart the terminal after using the `launchctl` command.

#### Shell configuration

1. Access your `.bashrc` or `.zshrc` file:

```plain text
nano ~/.bashrc
nano ~/.zshrc
```
2. Set the environment variable in the `.bashrc` or `.zshrc` file:

```plain text
export SSH_AUTH_SOCK=/Users/<user>/.bitwarden-ssh-agent.sock
```

### Linux

Enable the Bitwarden SSH Agent on Linux:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. The following example demonstrates how to do this after replacing `<user>` with your username:

```plain text
export SSH_AUTH_SOCK=/home/<user>/.bitwarden-ssh-agent.sock
```

#### Shell configuration

1. Access your `.bashrc` or `.zshrc` file:

```plain text
nano ~/.bashrc
nano ~/.zshrc
```
2. Set the environment variable in the `.bashrc` or `.zshrc` file:

```plain text
export SSH_AUTH_SOCK=/home/<user>/.bitwarden-ssh-agent.sock
```

#### Snap and Flatpak

Enable the Bitwarden SSH Agent on snap or Flatpak installations:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. The following example demonstrates how to do this after replacing `<user>` with your username:

```plain text
# Snap
export SSH_AUTH_SOCK=/home/<user>/snap/bitwarden/current/.bitwarden-ssh-agent.sock

# Flatpak
export SSH_AUTH_SOCK=/home/<user>/.var/app/com.bitwarden.desktop/data/.bitwarden-ssh-agent.sock
```

## Enable SSH agent

To enable the SSH Agent on your Bitwarden desktop app, navigate to **Settings** and **Enable SSH agent**. 

[Embedded content]After enabling SSH agent, you may also adjust the **Ask for authorization when using SSH agent** setting. This setting will determine when Bitwarden will require you to authorize access to an SSH key:

[Embedded content]- Always
- Never
- Remember until vault is locked

**Always** will be selected by default.

## Testing SSH keys

Once the SSH Agent has been configured for Bitwarden, we can test the setup by requesting an SSH list:

```plain text
ssh-add -L
```

This will return a list of SSH keys saved in your Bitwarden desktop client.

> [!NOTE] SSH key lock vault behavior
> When accessing an SSH key, the behavior of Bitwarden will differ depending on the locked or unlocked status of the client.
> 
> - **Locked vault**: If your Bitwarden vault is locked, Bitwarden will automatically prompt you to unlock your vault in order to gain access to the SSH key.
> - **Unlocked vault**: If the desktop vault is unlocked, you will be prompted to confirm the SSH key usage.

### Use SSH key to authenticate with Git

SSH can be used to authenticate with Git. The Bitwarden SSH Agent can add security and ease of use to your Git workflows. In this example, the Bitwarden SSH Agent will authenticate to GitHub.

1. On your GitHub account, setup an SSH key by navigating to **Settings**,**SSH and GPG keys**, then select **New SSH Key**.
2. On the add new SSH key screen, add a **Name**, select a **Key type.** Choose `Authentication Key`. Copy & paste the**Public key** from your Bitwarden vault into the **Key** field on GitHub.

[Embedded content]
3. Once you have completed all of the fields, select **Add SSH key**to save the key. GitHub will request you verify your GitHub account before the key is saved.
4. Test the GitHub SSH key in your terminal, for example if you are using macOS:

```plain text
ssh -T git@github.com
```
5. If successful, Bitwarden will prompt you to verify the access request. Select **Authorize** to confirm. If successful, you will receive a message verifying the authentication attempt:

```plain text
Hi <USER>! You've successfully authenticated, but GitHub does not provide shell access.
```

## Authenticate with git repositories

Use the Bitwarden SSH Agent to sign SSH Git commits. Before using the Bitwarden SSH Agent to sign Git commits, your system will require:

- Git version 2.34 or newer. Check your Git version with:

```plain text
git --version
```
- OpenSSH version 8.8 or newer. Check version with:

```plain text
ssh -V
```
- Bitwarden desktop client with SSH Agent enabled.

### Configure Git for SSH signing

Configure your Git environment to point to your SSH key for signing. To complete this you may set global variables or establish the instructions in your `.gitconfig` file.

#### Set global variables

To configure Git settings using `--global` variables:

1. Set Git to use SSH for signing:

```plain text
git config --global gpg.format ssh
```
2. Specify the SSH key to use as the signing key. To use the Bitwarden SSH Agent, replace `<YOUR_PUBLIC_KEY> ` with the public key copied from the SSH key saved in your Bitwarden vault.

```plain text
git config --global user.signingkey "<YOUR_PUBLIC_KEY>"
```
3. Enable automatic commit signing.

```plain text
git config --global commit.gpgsign true
```

#### Set `.gitconfig` file

To configure Git using a `.gitconfig` file:

1. Access `.gitconfig` with your preferred text editor:

```plain text
nano ~/.gitconfig
```
2. Add the following configurations:

```bash
[gpg]
 format = ssh
[user]
 signingkey = "<YOUR_PUBLIC_KEY>"
 name = <USER_NAME>
 email = <USER_EMAIL>
[commit]
 gpgsign = true
```

> [!NOTE] windows git signing
> For Windows users:
> 
> 1. Add the `core.sshCommand` variable to your Git config to use Microsoft OpenSSH:
> 
> 
> 
> ```plain text
> git config --global core.sshCommand "C:/Windows/System32/OpenSSH/ssh.exe"
> ```
> 
> Alternatively, set variable in your `.gitconfig` file:
> 
> 
> ```plain text
> [core]
> sshCommand = C:/Windows/System32/OpenSSH/ssh.exe
> ```
> 2. Next, you may be required to set the `gpg.ssh.program` parameter:
> 
> 
> 
> ```plain text
> git config --global gpg.ssh.program "C:/Windows/System32/OpenSSH/ssh-keygen.exe"
> ```

### Sign Git commits

Using SSH to authenticate with Git can add security and ease of use to your workflow. Similarly, SSH keys stored in Bitwarden can be used to sign and verify Git commits using SSH protocol. In this example, the Bitwarden SSH Agent will be used to sign Git commits to GitHub.

1. On your GitHub account, setup an SSH signing key by navigating to **Settings**,**SSH and GPG keys**, then select **New SSH Key**.
2. On the add new SSH key screen, add a **Name** and select a **Key type**, Choose `Signing Key`. Copy & paste the**Public key** from your Bitwarden vault into the **Key** field on GitHub.
3. Configure git to use the `allowedSignersFile` with the following command:

```plain text
git config --global gpg.ssh.allowedSignersFile "$HOME/.ssh/allowed_signers"
```
4. Add your public key to the allowedSignersFile:

```bash
# Create allowed_signers file
touch ~/.ssh/allowed_signers

# Edit the allowed_signers file and add a line for your public key pair you wish to trust, for example:
 User1@Bitwarden.com ssh-ed25519 <Your_Public_Key>
```
5. Use the SSH key to clone your repository with SSH method:

[Embedded content]

```plain text
git clone git@github.com:<USER>/<repository>.git
```
6. Create the Git commit using terminal or your preferred text editor:

```plain text
git commit -m "This commit is signed using SSH"
```
7. Bitwarden will prompt you to authorize the key usage:

[Embedded content]
8. Once authorized, the SSH key will be initiated to approve the commit. You may now push the commit:

```plain text
git push
```
9. You may verify your commit on Github by navigating to GitHub commits:

[Embedded content]

## SSH Agent forwarding

SSH agent forwarding allows a remote server you are accessing to authenticate to other servers using your keys, without exposing your private keys outside of your vault. The server you are logged in to can request your local Bitwarden instance to authenticate to the remote server. In this example, we will demonstrate transferring files between servers:

1. To begin, make sure the SSH agent has been enabled on your Bitwarden desktop app by navigating to **Settings**  and **Enable SSH agent**:

[Embedded content]
2. Create a new SSH key or import and existing SSH key to your Bitwarden desktop app.
3. Activate agent forwarding by opening a connection with the server you wish to send files to:

```plain text
ssh -A <HostnameA>
```
4. Send a file to the server:

```plain text
rsync -avzP ./TEST.txt <USER>@<HostnameB>:/home/<USER>/test.txt
```
5. Bitwarden will prompt you to approve the SSH key access. This will show that the SSH key has been requested and used to complete the file transfer.

[Embedded content]
