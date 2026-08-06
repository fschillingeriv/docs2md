---
URL: https://bitwarden.com/help/ssh-agent/
---

# SSH Agent

Bitwarden Password Manager desktop app can act as an SSH Agent to securely encrypt and store your SSH (Secure Shell) keys for use with:

- Authenticating to servers
- Signing Git commits
- Interacting with SSH-based services

See [About SSH](https://bitwarden.com/help/about-ssh/) for additional information on how the agent works, supported key types, known limitations, and vault behavior.

## Enable SSH Agent

To enable the SSH Agent on your Bitwarden desktop app, navigate to **Settings** and **Enable SSH agent**. Then, adjust the **Ask for authorization when using SSH agent** setting. This setting will determine when Bitwarden will require you to authorize access to an SSH key:

![Enable SSH storage on desktop client](https://bitwarden.com/assets/7Fx7AnfIPXmiJpHq1lFhTx/d151287d040a69dcb52d36fc6a4593b9/Enable_SSH_agent_updated.png)
*Enable SSH storage on desktop client*

#### Behavior by vault state

The SSH agent behaves differently depending on the current state of your vault. The following describes single-account behavior with the agent enabled.

| Vault state | Agent running | List requests | Sign requests |
|------|------|------|------|
| Logged out | No | | |
| Locked (before initial unlock) | Yes | Supported | Prompts to unlock vault. |
| Locked (after initial unlock) | Yes | Supported | Prompts to unlock vault, then prompts to authorize. |
| Unlocked | Yes | Supported | Supported |

## Configure your system to use Bitwarden SSH agent

In order to use Bitwarden as your primary SSH Agent, you will be required to configure your SSH client to communicate with Bitwarden for authentication. Once you have enabled the agent in the desktop app, configure your operating system to route SSH requests to Bitwarden:

### Windows

To enable the Bitwarden SSH Agent on Windows, you must disable the OpenSSH service on your Windows machine:

1. Navigate to **Services → OpenSSH Authentication Agent**. 

![Windows Services panel](https://bitwarden.com/assets/77fTJpxIBH5ikJYQW1KFL7/0c6fa3b9f68f7a85569ad6ede489979e/openSSH_agent.png)
*Windows Services panel*
2. Once you have opened the OpenSSH Authentication Agent Properties window, set the **Startup type** setting to **Disabled**.

![Windows Services panel](https://bitwarden.com/assets/77fTJpxIBH5ikJYQW1KFL7/0c6fa3b9f68f7a85569ad6ede489979e/openSSH_agent.png)
*Windows Services panel*
3. Once the settings have been adjusted, select **Apply** and then **OK**.

### macOS App store

Enable the Bitwarden SSH Agent on macOS store download:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. In the following example, replace `<user>` with your username:

```plain text
export SSH_AUTH_SOCK=/Users/<user>/Library/Containers/com.bitwarden.desktop/Data/.bitwarden-ssh-agent.sock
```
2. To make this persistent, add the `export` command to your `~/.zshrc` or `~/.bashrc` file.

### macOS .dmg

Enable the Bitwarden SSH Agent on macOS .dmg download:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. In the following example, replace `<user>` with your username:

```bash
export SSH_AUTH_SOCK=/Users/<user>/.bitwarden-ssh-agent.sock
```
2. Alternatively, configure `SSH_AUTH_SOCKET`:

```plain text
launchctl setenv "SSH_AUTH_SOCKET" "/Users/<user>/.bitwarden-ssh-agent.sock"
```
3. To make this persistent, add the `export` command to your `~/.zshrc` or `~/.bashrc` file.

> [!NOTE] launchctl require terminal restart
> You may need to restart the terminal after using the `launchctl` command.

### Linux

Enable the Bitwarden SSH Agent on Linux:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. In the following example, replace `<user>` with your username:

```plain text
export SSH_AUTH_SOCK=/home/<user>/.bitwarden-ssh-agent.sock
```
2. To make this persistent, add the `export` command to your `~/.zshrc` or `~/.bashrc` file.

### Snap and Flatpak

Enable the Bitwarden SSH Agent on snap or Flatpak installations:

1. Configure the `SSH_AUTH_SOCK` variable to point to the Bitwarden SSH Agent socket. The following example demonstrates how to do this after replacing `<user>` with your username:

```plain text
# Snap
export SSH_AUTH_SOCK=/home/<user>/snap/bitwarden/current/.bitwarden-ssh-agent.sock

# Flatpak
export SSH_AUTH_SOCK=/home/<user>/.var/app/com.bitwarden.desktop/data/.bitwarden-ssh-agent.sock
```

## Test SSH agent

Once the SSH Agent has been configured for Bitwarden, you may test the setup by requesting an SSH list:

```plain text
ssh-add -L
```

# Scenarios and workflows

Once the agent has been enabled and your OS has been configured, you can use Bitwarden SSH keys in a range of tools and workflows. The following scenarios will provide step-by-step setup for a range of common setups and use cases.

### Use SSH to authenticate with Git

SSH can be used to authenticate with Git. The Bitwarden SSH Agent can add security and ease of use to your Git workflows. In this example, the Bitwarden SSH Agent will authenticate to GitHub.

1. On your GitHub account, setup an SSH key by navigating to **Settings**,**SSH and GPG keys**, then select **New SSH Key**.
2. On the add new SSH key screen, add a **Name**, select a **Key type.** Choose `Authentication Key`. Copy & paste the**Public key** from your Bitwarden vault into the **Key** field on GitHub.

![Create new GitHub key](https://bitwarden.com/assets/1bZWyhzPtdpdhoDM6GNYdz/3c326b32d15d134ff7532a57041ceff4/2025-02-12_11-26-35.png)
*Create new GitHub key*
3. Once you have completed all of the fields, select **Add SSH key**to save the key. GitHub will request that you verify your GitHub account before the key is saved.
4. Test the GitHub SSH key in your terminal, for example if you are using macOS:

```plain text
ssh -T git@github.com
```
5. If successful, Bitwarden will prompt you to verify the access request. Select **Authorize** to confirm. If successful, you will receive a message verifying the authentication attempt:

```plain text
Hi <USER>! You've successfully authenticated, but GitHub does not provide shell access.
```

### Authenticate with Git repositories

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

### 

### Sign Git commits

Using SSH to authenticate with Git can add security and ease of use to your workflow. Similarly, SSH keys stored in Bitwarden can be used to sign and verify Git commits using SSH protocol. In this example, the Bitwarden SSH Agent will be used to sign Git commits to GitHub.

1. On your GitHub account, setup an SSH signing key by navigating to **Settings**,**SSH and GPG keys**, then select **New SSH Key**.
2. On the add new SSH key screen, add a **Name** and select a **Key type**. Choose `Signing Key`. Copy & paste the**Public key** from your Bitwarden vault into the **Key** field on GitHub.
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

![SSH clone](https://bitwarden.com/assets/76Snkd9TQMrVMmegeJRqK/21836de7c7500b9ebdabaeb1d17b9659/2025-02-12_17-16-13.png)
*SSH clone*

```plain text
git clone git@github.com:<USER>/<repository>.git
```
6. Create the Git commit using terminal or your preferred text editor:

```plain text
git commit -m "This commit is signed using SSH"
```
7. Bitwarden will prompt you to authorize the key usage based on user settings:

![Authorize SSH with client](https://bitwarden.com/assets/0aGz4U3YpB63EHRWVU2YY/d7e7883eb93065205226df80ffebde7c/github_auth_key.png)
*Authorize SSH with client*
8. Once authorized, the SSH key will be initiated to approve the commit. You may now push the commit:

```plain text
git push
```
9. You may verify your commit on Github by navigating to GitHub commits:

![Verify your commit in GitHub](https://bitwarden.com/assets/1PR4Sss3Pvf3anlau5AlgC/ecfdb02b50fb83f59a21ebc7ed550042/2025-02-12_14-51-41.png)
*Verify your commit in GitHub*

### SSH agent forwarding

SSH agent forwarding allows a remote server you are accessing to authenticate to other servers using your keys, without exposing your private keys outside of your vault. The server you are logged in to can request your local Bitwarden instance to authenticate to the remote server. In this example, we will demonstrate transferring files between servers:

1. Create a new SSH key or import an existing SSH key to your Bitwarden desktop app.
2. Activate agent forwarding by opening a connection with the server you wish to send files to:

```plain text
ssh -A <HostnameA>
```
3. Send a file to the server:

```plain text
rsync -avzP ./TEST.txt <USER>@<HostnameB>:/home/<USER>/test.txt
```
4. Bitwarden will prompt you to approve the SSH key access. This will show that the SSH key has been requested and used to complete the file transfer.

![Confirm SSH Agent Forwarding](https://bitwarden.com/assets/4TPhGUdynuGBHj1l4zmUcS/04aae27ee063080afc5fbd6183a354b3/Confirm_SSH_key_usage.webp)
*Confirm SSH Agent Forwarding*

## **Troubleshooting**

The following section includes common issues users may encounter when using the SSH agent.

`Error connecting to agent: Connection refused`

- The agent is not running; confirm it has been properly enabled and check the app logs.

`ssh <action> `fails

- Try to run the command with `-vvv` and capture the output to share in a bug report.
