---
URL: https://bitwarden.com/help/configure-self-hosted-environment-with-forward-proxy/
---

# Configure Self-hosted environment with forward proxy

> [!NOTE] Proxy env setup required
> Configuration using a forward proxy should be completed by advanced users only. This guide does not address setup of the forward proxy itself.

This article demonstrates the necessary configurations required to route your Bitwarden self-hosted instance's traffic through a forward proxy. At this time, only Linux Docker Compose environments will support this proxy environment. 

> [!NOTE] Linux deployment setup required
> In order to configure the forward proxy, follow the deployment steps for your Bitwarden self-hosted instance <u>up to and including </u>create a [Bitwarden local users & directory.](https://bitwarden.com/help/install-on-premise-linux/#create-bitwarden-local-user-directory/)

- [Linux standard deployment](https://bitwarden.com/help/install-on-premise-linux/)
- [Linux manual deployment](https://bitwarden.com/help/install-on-premise-manual/)
- [Linux offline deployment](https://bitwarden.com/help/install-and-deploy-offline/)

Once your self-host environment has been configured through the **Create Bitwarden local user & directory** step, you may return to this guide and continue with the forward proxy configuration.

## Configure Docker to forward to your proxy

Configure Docker to route traffic through our your configured proxy:

1. Create and access `systemd` override file:

```bash
# Create directory for docker.service.d 
sudo mkdir -p /etc/systemd/system/docker.service.d

# create and edit http-proxy.conf in the new directory
sudo nano -w /etc/systemd/system/docker.service.d/http-proxy.conf
```
2. In the new file, we are going to add configuration to instruct the proxy to pull `HTTP` and `HTTPS` requests through the proxy environment, for example:

```bash
[Service]
Environment="HTTP_PROXY=http://10.138.0.3:3128"
Environment="HTTPS_PROXY=http://10.138.0.3:3128"
Environment="NO_PROXY=localhost,nginx,admin,mssql,sso,web,attachments,icons,notifications,identity,api,events"
```

> [!NOTE] retrieve docker.service.d information
> Retrieve the information for the `docker.service.d` file from your proxy configuration file.
3. Apply changes:

```bash
sudo systemctl daemon-reload
```

> [!NOTE] Proxy settings require sudo access
> Configuring the proxy and any build-specific firewall configurations will require root access and sudo permission. These steps should be done before installing Bitwarden. When installing and setting up a Bitwarden self-host instance, using a dedicated Bitwarden user is required.
4. Restart Docker:

```bash
systemctl restart docker
```

## Edit Bitwarden local user & directory

Now that you have configured Docker to send traffic through the forward proxy, additional client configurations will be required for the forward proxy setup:

1. Create a .config directory in the `/opt/bitwarden.docker` & `/home/bitwarden`.`docker` locations: 

```bash
mkdir /opt/bitwarden/.docker && mkdir /home/bitwarden/.docker
```
2. Create `config.json` file and add configurations for the Docker client:

```bash
sudo nano -w /opt/bitwarden/.docker/config.json

# add configurations to config.json 
{
 "proxies":
 {
 "default":
 {
 "httpProxy": "http://10.138.0.3:3128",
 "httpsProxy": "http://10.138.0.3:3128",
 "noProxy": "localhost,nginx,admin,mssql,sso,web,attachments,icons,notifications,identity,api,events"
 }
 }
}
```
3. Copy `config.json` to the `bitwarden` user's `/home/` directory:

```plain text
sudo cp /opt/bitwarden/.docker/config.json /home/bitwarden/.docker
```

## Next steps

Once the Docker configuration has been completed, we can continue with the Linux self-hosted install procedure. For each deployment guide ([Linux standard deployment](https://bitwarden.com/help/install-on-premise-linux/), [Linux manual deployment](https://bitwarden.com/help/install-on-premise-manual/), and [Linux offline deployment](https://bitwarden.com/help/install-and-deploy-offline/)) users will start **after**the **Create Bitwarden local user & directory**step to complete the self-hosted installation.
