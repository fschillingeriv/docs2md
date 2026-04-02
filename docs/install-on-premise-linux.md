---
URL: https://bitwarden.com/help/install-on-premise-linux/
---

# Linux Standard Deployment

This article will walk you through the procedure to install and deploy Bitwarden to your own Linux server. Bitwarden can also be installed and deployed on [Windows](https://bitwarden.com/help/install-on-premise-windows/) machines. Please review Bitwarden [software release support](https://bitwarden.com/help/bitwarden-software-release-support/#release-support-at-bitwarden/) documentation.

## System specifications

| | **Minimum** | **Recommended** |
|------|------|------|
| Processor | x64, 1.4GHz | x64, 2GHz dual core |
| Memory | 2GB RAM | 4GB RAM |
| Storage | 12GB | 25GB |
| Docker Version | Engine 26+ and Compose`ª` | Engine 26+ and Compose`ª` |

`ª` - Docker Compose is automatically installed as a plugin when you download Docker Engine.

Standard self-hosted server deployments ship with an **MSSQL Express** image by default, however you have the option to use an [external database](https://bitwarden.com/help/external-db/). The default database has a 10GB [maximum relational database size](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?view=sql-server-ver17#scale-limits) but does not require additional licensing.

> [!NOTE] Digital Ocean Link
> If you are looking for a quality provider with affordable prices, we recommend DigitalOcean. [Get started today](https://marketplace.digitalocean.com/apps/bitwarden) or read our [blog post about Bitwarden on DigitalOcean](https://bitwarden.com/blog/digitalocean-marketplace/).

## Overview

The following is a summary of the installation procedure in this article. Links in this section will jump to detailed **Installation procedure** sections:

1. [**Configure your domain**](https://bitwarden.com/help/install-on-premise-linux/#configure-your-domain/). Set DNS records for a domain name pointing to your machine, and open ports 80 and 443 on the machine.
2. [**Install Docker and Docker Compose**](https://bitwarden.com/help/install-on-premise-linux/#install-docker-and-docker-compose/) on your machine.
3. [**Create a Bitwarden user & directory**](https://bitwarden.com/help/install-on-premise-linux/#create-bitwarden-local-user-directory/) from which to complete installation.
4. Retrieve an installation id and key from [**https://bitwarden.com/host**](https://bitwarden.com/host/) for use in installation.

For more information, see [What are my installation id and installation key used for?](https://bitwarden.com/help/hosting-faqs/#q-what-are-my-installation-id-and-installation-key-used-for/)
5. [**Install Bitwarden**](https://bitwarden.com/help/install-on-premise-linux/#install-bitwarden/) on your machine.
6. [**Configure your environment**](https://bitwarden.com/help/install-on-premise-linux/#post-install-configuration/) by adjusting settings in `./bwdata/env/global.override.env`.

> [!NOTE]
> At a minimum, configure the `globalSettings__mail__smtp...` variables to setup an email server for inviting and verifying users.
7. [**Start your instance**](https://bitwarden.com/help/install-on-premise-linux/#start-bitwarden/).
8. Test your installation by opening your configured domain in a web browser.
9. Once deployed, we recommend regularly [backing up your server](https://bitwarden.com/help/backup-on-premise/) and [checking for system updates](https://bitwarden.com/help/updating-on-premise/).

## Installation procedure

> [!NOTE] Protocol consistency required
> Bitwarden requires consistent HTTP or HTTPS usage throughout your deployment. Mixing protocols (for example, HTTPS at proxy, HTTP internally) causes connection, authentication, and syncing errors. We reccomend using HTTPS for production; HTTP for testing only.

### Configure your domain

By default, Bitwarden will be served through ports 80 (`http`) and 443 (`https`) on the host machine. Open these ports so that Bitwarden can be accessed from within and/or outside of the network. You may opt to choose different ports during installation.

We recommend configuring a domain name with DNS records that point to your host machine (for example, `server.example.com`), especially if you are serving Bitwarden over the internet. We recommend not including Bitwarden in your hostname to keep the server identity or type concealed.

### Install Docker and Docker Compose

Bitwarden will be deployed and run on your machine using an array of [Docker containers](https://docs.docker.com/get-started/). Bitwarden can be run with any Docker edition or plan. Evaluate which edition is best for your installation. Deployment of containers is orchestrated using [Docker Compose](https://docs.docker.com/compose/). Docker Compose is automatically installed as a plugin when you download Docker Engine.

[Download Docker Engine for Linux](https://docs.docker.com/engine/install/#supported-platforms).

### Create Bitwarden local user & directory

Configure your Linux server with a dedicated `bitwarden` service account, from which to install and run Bitwarden. Doing so will isolate your Bitwarden instance from other applications running on your server. For more information, see Docker's [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/) documentation.

1. Create a bitwarden user:

```
sudo adduser bitwarden
```
2. Set password for bitwarden user (strong password):

```
sudo passwd bitwarden
```
3. Create a docker group (if it doesn’t already exist):

```
sudo groupadd docker
```
4. Add the bitwarden user to the docker group:

```
sudo usermod -aG docker bitwarden
```
5. Create a bitwarden directory:

```
sudo mkdir /opt/bitwarden
```
6. Set permissions for the `/opt/bitwarden` directory:

```
sudo chmod -R 700 /opt/bitwarden
```
7. Set the bitwarden user as owner of the `/opt/bitwarden` directory:

```
sudo chown -R bitwarden:bitwarden /opt/bitwarden
```

### Install Bitwarden

> [!TIP] If you've setup self-host local user and directory.
> Once you have [created a Bitwarden user & directory](https://bitwarden.com/help/install-on-premise-manual/#create-bitwarden-local-user--directory/), complete the following as the `bitwarden` user from the `/opt/bitwarden` directory. **Do not install Bitwarden as root**, as you will encounter issues during installation.

Bitwarden provides a shell script for easy installation on Linux and Windows (PowerShell). Complete the following steps to install Bitwarden using the shell script:

1. Download the Bitwarden installation script (`bitwarden.sh`) to your machine:

```
curl -Lso bitwarden.sh "https://func.bitwarden.com/api/dl/?app=self-host&platform=linux" && chmod 700 bitwarden.sh
```
2. Run the installer script. A `./bwdata` directory will be created relative to the location of `bitwarden.sh`.

```
./bitwarden.sh install
```
3. Complete the prompts in the installer:

 - **Enter the domain name for your Bitwarden instance:**

Typically, this value should be the configured DNS record.
 - **Do you want to use Let's Encrypt to generate a free SSL certificate? (y/n):**

Specify `y` to generate a trusted SSL certificate using Let's Encrypt. You will be prompted to enter an email address for expiration reminders from Let's Encrypt. For more information, see [Certificate Options](https://bitwarden.com/help/certificates/).

Alternatively, specify `n` and use the **Do you have a SSL certificate to use?** option.
 - **Enter your installation id:**

Retrieve an installation id using a valid email at [https://bitwarden.com/host](https://bitwarden.com/host/). For more information, see [what are my installation id and installation key used for?](https://bitwarden.com/help/hosting-faqs/#q-what-are-my-installation-id-and-installation-key-used-for/)
 - **Enter your installation key:**

Retrieve an installation key using a valid email at [https://bitwarden.com/host](https://bitwarden.com/host/). For more information, see [What are my installation id and installation key used for?](https://bitwarden.com/help/hosting-faqs/#q-what-are-my-installation-id-and-installation-key-used-for/)
 - **Enter your region (US/EU):**Enter US or EU depending on the [cloud server](https://bitwarden.com/help/server-geographies/) you will use to [license paid features](https://bitwarden.com/help/licensing-on-premise/), only applicable if you're connecting a self-hosted account or organization to a paid subscription.
 - **Do you have a SSL certificate to use? (y/n):**

(Only if `n` selected for **Do you want to use Let's Encrypt to generate a free SSL certificate?**) If you already have your own SSL certificate, specify `y` and place the necessary files in the `./bwdata/ssl/your.domain` directory. You will be asked whether it is a trusted SSL certificate (y/n). For more information, see [Certificate Options](https://bitwarden.com/help/certificates/).

Alternatively, specify `n` and use the **self-signed SSL certificate?** option, which is only recommended for testing purposes.
 - **Do you want to generate a self-signed SSL certificate? (y/n):**

(Only if `n` selected for **Do you have a SSL certificate to use?**) Specify `y` to have Bitwarden generate a self-signed certificate for you. This option is only recommended for testing. For more information, see [Certificate Options](https://bitwarden.com/help/certificates/).

If you specify `n`, your instance will not use an SSL certificate and you will be required to front your installation with a HTTPS proxy, or else Bitwarden applications will not function properly.

### Post-install configuration

Configuring your environment can involve making changes to two files; an environment variables file and an installation file:

#### Environment variables (*required*)

Some features of Bitwarden are not configured by the `bitwarden.sh` script. Configure these settings by editing the environment file, located at `./bwdata/env/global.override.env`. **At a minimum, you should replace the values for:**

```
...
globalSettings__mail__smtp__host=<placeholder>
globalSettings__mail__smtp__port=<placeholder>
globalSettings__mail__smtp__ssl=<placeholder>
globalSettings__mail__smtp__username=<placeholder>
globalSettings__mail__smtp__password=<placeholder>
...
adminSettings__admins=
...
```

Replace `globalSettings__mail__smtp...=` placeholders to connect to the SMTP mail server that will be used to send verification emails to new users and invitations to organizations. Adding an email address to `adminSettings__admins=` will provision access to the System Administrator Portal.

After editing `global.override.env`, run the following command to apply your changes:

```
./bitwarden.sh restart
```

#### Installation file

The Bitwarden installation script uses settings in `./bwdata/config.yml` to generate the necessary assets for installation. Some installation scenarios (such as installations behind a proxy with alternate ports) may require adjustments to `config.yml` that were not provided during standard installation.

Edit `config.yml` as necessary and apply your changes by running:

```
./bitwarden.sh rebuild
```

### Start Bitwarden

Once you have completed all previous steps, start your Bitwarden instance:

```
./bitwarden.sh start
```

> [!NOTE]
> The first time you start Bitwarden it may take some time as it downloads all of the images from GitHub Container Registry.

Verify that all containers are running correctly:

```
docker ps
```

![Docker healthy](https://bitwarden.com/assets/3Sq7MaJZ1jaEJUCW44wmwj/008be5ee5e43c20c8c840e71617e57eb/2025-05-05_15-34-44.png)

Congratulations! Bitwarden is now up and running at your specified domain (in the above example, `https://bitwarden.example.com)`. Visit the web vault in your web browser to confirm that it's working.

You may now register a new account and log in. You will need to have configured `smtp` environment variables (see [Environment Variables](https://bitwarden.com/help/environment-variables/)) in order to verify the email for your new account.

> [!TIP] Backup and Update your Server
> Once deployed, we recommend regularly [backing up your server](https://bitwarden.com/help/backup-on-premise/) and [checking for system updates](https://bitwarden.com/help/updating-on-premise/).

## Script commands reference

The Bitwarden installation script (`bitwarden.sh` or `bitwarden.ps1`) has the following commands available:

> [!NOTE]
> PowerShell users will run the commands with a prefixed `-` (switch). For example `.\bitwarden.ps1 -start`.

| **Command** | **Description** |
|------|------|
| install | Start the installer. |
| start | Start all containers. |
| restart | Restart all containers (same as start). |
| stop | Stop all containers. |
| update | Update all containers and the database. |
| updatedb | Update/initialize the database. |
| updaterun | Update the `run.sh `file. |
| updateself | Update this main script. |
| updateconf | Update all containers without restarting the running instance. |
| uninstall | Before this command executes, you will be prompted to save database files. `y `will create a tarfile of your database including the most recent backup. Stops containers, deletes the `bwdata `directory and all its contents, and removes ephemeral volumes. After executing, you will be asked whether you also want to purge all Bitwarden images. |
| compresslogs | Download a tarball of all server logs, or of server logs in a specified date range, to the current directory. For example, use `./bitwarden.sh compresslogs 20240304 20240305` to download logs from March 4th, 2024 to March 5th, 2024. |
| renewcert | Renew certificates. |
| rebuild | Rebuild generated installation assets from `config.yml`. |
| help | List all commands. |

## Next steps

- If you are planning to self-host a Bitwarden organization, see [self-host an organization](https://bitwarden.com/help/self-host-an-organization/) to get started.
- For additional information see [self hosting FAQs](https://bitwarden.com/help/hosting-faqs/).
