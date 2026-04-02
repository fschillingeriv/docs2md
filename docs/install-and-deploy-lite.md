---
URL: https://bitwarden.com/help/install-and-deploy-lite/
---

# Lite Deployment

> [!TIP] Who is Lite for?
> Bitwarden lite is intended for personal use and home-labs, not for use in business contexts. Businesses should use one of the [standard deployment options](https://bitwarden.com/help/self-host-bitwarden/).

This article will walk you through installing and launching [Bitwarden lite](https://github.com/bitwarden/self-host/tree/main/bitwarden-lite). Use this deployment method to:

- Simplify configuration and optimize resource usage (CPU, memory) by deploying Bitwarden with a single Docker image.
- Utilize different database solutions such as MSSQL, PostgreSQL, SQLite, and MySQL/MariaDB. **Only** lite deployments can currently leverage these databases, standard deployments require MSSQL.
- Run on ARM architecture for alternative systems such as Raspberry Pi and NAS servers.

> [!TIP] Transitioning from Unified to Lite.
> In December, 2025 Bitwarden Unified exited beta and was renamed Bitwarden lite. If you participated in the beta, make sure that you use the new image name (`ghcr.io/bitwarden/lite`) when updating to the latest version.

## System requirements

Bitwarden lite requires:

- RAM: At least 200 MB
- Storage: At least 1GB
- Docker Engine: Version 26+

## Setup

Before running a Bitwarden lite server, install Docker, setup your `settings.env` file, and decide on your database configuration:

### Install Docker 

Bitwarden lite will run on your machine using a [Docker container](https://docs.docker.com/get-started/). Lite can be run with any Docker edition or plan, but you must **install Docker on your machine before proceeding with installation.** Refer to the following Docker documentation for help:

- [Install Docker Engine](https://docs.docker.com/engine/installation/)

### Required environment variables

Environment variables can be specified by creating a `settings.env` file, which you can find an example of in our [GitHub](https://github.com/bitwarden/self-host/blob/main/bitwarden-lite/settings.env) repository, or by using the `--env` flag if you're using the `docker run` method. At a minimum, set values for the variables that fall under the `# Required Settings #` section of the example `.env` file:

> [!TIP] More Lite environment variables.
> More optional environment variables are available than those listed in this table.

| Variable | Description |
|------|------|
| BW_DOMAIN | Replace `bitwarden.yourdomain.com` with the domain where Bitwarden will be accessed. |
| BW_DB_PROVIDER | The database provider you will be using for your Bitwarden server. Available options are `sqlserver`, `postgresql`, `sqlite`, or `mysql`/`mariadb`. |
| BW_DB_SERVER | The name of the server on which your database is running. |
| BW_DB_DATABASE | The name of your Bitwarden database. |
| BW_DB_USERNAME | The username for accessing the Bitwarden database. |
| BW_DB_PASSWORD | The password for accessing the Bitwarden database. |
| BW_DB_FILE | Only required for `sqlite` if you would like to specify the path to your database file. If not specified, `sqlite` will automatically create a `vault.db` file under the `/etc/bitwarden` volume. |
| BW_INSTALLATION_ID | A valid installation ID generated from [https://bitwarden.com/host/](https://bitwarden.com/host/). |
| BW_INSTALLATION_KEY | A valid installation key generated from [https://bitwarden.com/host/](https://bitwarden.com/host/). |

### Database examples

Unlike standard Bitwarden deployments, lite does not come out-of-the-box with a database. You can use an existing database, or create a new one. Which `# Required Settings #` you'll be required to include in your `settings.env` file or `--env` flags will depend on which supported database provider you're using:

> [!NOTE] Lite database require your management.
> Because Bitwarden lite databases are not provided by or collocated with the application container, database maintenance, including updates, maintenance, and backups, must be fully managed by you.

### MySQL/MariaDB

The following variables are required for a MySQL or MariaDB database:

```
# Database
BW_DB_PROVIDER=mysql
BW_DB_SERVER=db
BW_DB_DATABASE=bitwarden_vault
BW_DB_USERNAME=bitwarden
BW_DB_PASSWORD=super_strong_password
```

### MSSQL

The following variables are required for an MSSQL database:

```
# Database
BW_DB_PROVIDER=sqlserver
BW_DB_SERVER=db
BW_DB_DATABASE=bitwarden_vault
BW_DB_USERNAME=bitwarden
BW_DB_PASSWORD=super_strong_password
```

### SQLite

The following variables are required for an SQLite database:

```
# Database
BW_DB_PROVIDER=sqlite
BW_DB_FILE=/path/to/.db
```

Assigning the `sqlite `value will create a `vault.db `file in the `/etc/bitwarden` volume automatically. `BW_DB_FILE` is only required if you would like to specify the path to a different database file.

### PostgreSQL

The following variables are required for an PostgreSQL database:

```
# Database
BW_DB_PROVIDER=postgresql
BW_DB_SERVER=db
BW_DB_DATABASE=bitwarden_vault
BW_DB_USERNAME=bitwarden
BW_DB_PASSWORD=super_strong_password
```

## Run the server

The lite deployment can be run using the `docker run` command or using Docker Compose. In either case, make sure that you've set your environment variables and made your database available before proceeding.

### Docker run

The lite deployment can be run with the `docker run` command, as in the following example:

```
docker run -d --name bitwarden -v /$(pwd)/bwdata/:/etc/bitwarden -p 80:8080 --env-file settings.env ghcr.io/bitwarden/lite
```

Running the server with the `docker run` command has several **required** options, including:

| **Name, shorthand** | **Description** |
|------|------|
| --detach , -d | Run the container in the background and print container ID. |
| --name | Provide a name for the container. `bitwarden` is used in the example. |
| --volume , -v | Bind mount a volume. At a minimum, mount `/etc/bitwarden`. |
| --publish , -p | Map container ports to the host. The example shows the port `80:8080` mapped. Port 8443 is required when configuring SSL. |
| --env-file | Path of the [file to read environment variables from](https://bitwarden.com/help/install-and-deploy-unified-beta/#specify-environment-variables/). Alternatively, use the `--env `flag to declare environment variables inline ([learn more](https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file)). |

Once you run the command, verify that the container is running and healthy with:

```
docker ps
```

Congratulations! Bitwarden lite is now up and running at `https://your.domain.com`. Visit the web vault in your browser to confirm that it's working. You may now register a new account and log in.

### Docker Compose

Running the lite deployment with Docker Compose will require Docker Compose version 1.24+. To run the lite deployment with Docker compose, create a `docker-compose.yml` file, for example:

```
---
version: "3.8"

services:
 bitwarden:
 depends_on:
 - db
 env_file:
 - settings.env
 image: ghcr.io/bitwarden/lite
 restart: always
 ports:
 - "80:8080"
 volumes:
 - bitwarden:/etc/bitwarden

 db:
 environment:
 MARIADB_USER: "bitwarden"
 MARIADB_PASSWORD: "super_strong_password"
 MARIADB_DATABASE: "bitwarden_vault"
 MARIADB_RANDOM_ROOT_PASSWORD: "true"
 image: mariadb:10
 restart: always
 volumes:
 - data:/var/lib/mysql

volumes:
 bitwarden:
 data:
```

In the `docker-compose.yml` file, make any desired configurations including:

- Mapping volumes for logs and Bitwarden data.
- Mapping ports.
- Configuring a database image.`ª`

`ª`Only setup a database in `docker-compose.yml`, as in the above example, if you want to **create a new database server** to use with Bitwarden. Sample configurations for MySQL, MSSQL, and PostgreSQL are included in our [example file](https://github.com/bitwarden/self-host/blob/main/bitwarden-lite/docker-compose.yml).

Once your `docker-compose.yml` and `settings.env` file are created, start your lite server by running:

```
docker compose up -d
```

Verify that all containers are running correctly: 

```
docker ps
```

Congratulations! Your lite deployment is now up and running at `https://your.domain.com`. Visit the web vault in your browser to confirm that it's working. You may now register a new account and log in.

### Update or restart the server

It's important to keep your Bitwarden lite server up to date. Like running the server, you can update it using either `docker run` commands or Docker Compose:

### Docker run

> [!TIP] Lite, if you're restarting instead of updating
> If you're restarting instead of updating the server, for example after making environment variable changes, skip the step that requires you to pull the most recent Bitwarden lite image.

To update the server:

1. Stop the running Docker container:

```
docker stop bitwarden
```
2. Remove the Docker container:

```
docker rm bitwarden
```
3. Pull the most recent Bitwarden lite image:

```
docker pull ghcr.io/bitwarden/lite
```
4. Restart the server:

```
docker run -d --name bitwarden -v /$(pwd)/bwdata/:/etc/bitwarden -p 80:8080 --env-file settings.env ghcr.io/bitwarden/lite
```

### Docker Compose

> [!TIP] Lite, if you're restarting instead of updating
> If you're restarting instead of updating the server, for example after making environment variable changes, skip the step that requires you to pull the most recent Bitwarden lite image.

To update the server:

1. Stop the running Docker container:

```
docker compose down
```
2. Pull the most recent Bitwarden lite image:

```
docker compose pull
```
3. Restart the server:

```
docker compose up -d
```

## Optional environment variables

Bitwarden lite works, by default, with some available services deactivated. These services, and many other server characteristics, can optionally be activated and customized with your `settings.env` file or `--env` flags:

> [!WARNING] When editing Lite environment variables
> Whenever you change an environment variable, you will need to restart your server in order for changes to take effect.

#### Services

Additional services can be activated or deactivated using the following variables:

| Variable | Description |
|------|------|
| BW_ENABLE_ADMIN | **Do not disable this service.** Learn more about Admin panel capabilities [here](https://bitwarden.com/help/system-administrator-portal/). Default `true`. |
| BW_ENABLE_API | **Do not disable this service.** Default `true`. |
| BW_ENABLE_EVENTS | Enable or disable Bitwarden events logs for teams and enterprise event monitoring. Default `false`. |
| BW_ENABLE_ICONS | Enable or disable Bitwarden brand icons that are set with the login item URI's. Learn more [here](https://bitwarden.com/help/website-icons/). Default `true`. |
| BW_ENABLE_IDENTITY | **Do not disable this service.** Default `true`. |
| BW_ENABLE_NOTIFICATIONS | Enable or disable notification services for receiving push notifications to mobile devices, using login with device, mobile vault sync, and more. Default `true`. |
| BW_ENABLE_SCIM | Enable or disable SCIM for Enterprise organizations. Default `false`. |
| BW_ENABLE_SSO | Enable or disable SSO services for Enterprise organizations. Default `false`. |
| BW_ICONS_PROXY_TO_CLOUD | Enabling this service will proxy icon service requests to operate through cloud services in order to lower system memory load. If choosing to use this setting, `BW_ENABLE_ICONS` should be set to `false` in order to reduce container load. Default `false`. |

#### Certificates

Use these variables to change certificate settings:

| **Variable** | **Description** |
|------|------|
| BW_ENABLE_SSL | Use SSL/TLS. `true`/`false`. Default `false`. SSL is required for Bitwarden to function properly. If you are not using SSL configured in the Bitwarden container you should front Bitwarden with a SSL proxy. |
| BW_SSL_CERT | The name of your SSL certificate file. The file must be located in the `/etc/bitwarden `directory within the container. Default `ssl.crt`. |
| BW_SSL_KEY | The name of your SSL key file. The file must be located in the `/etc/bitwarden `directory within the container. Default `ssl.key`. |
| BW_ENABLE_SSL_CA | Use SSL with certificate authority(CA) backed service. `true`/`false`. Default `false`. |
| BW_SSL_CA_CERT | The name of your SSL CA certificate. The file must be located in the `/etc/bitwarden `directory within the container. Default `ca.crt`. |
| BW_ENABLE_SSL_DH | Use SSL with Diffie-Hellman key exchange. `true`/`false`. Default `false`. |
| BW_SSL_DH_CERT | The name of your Diffie-Hellman parameters file. The file must be located in the `/etc/bitwarden `directory within the container. Default `dh.pem`. |
| BW_SSL_PROTOCOLS | SSL version used by NGINX. Leave empty for recommended default. [Learn more](https://wiki.mozilla.org/Security/Server_Side_TLS). |
| BW_SSL_CIPHERS | SSL ciphersuites used by NGINX. Leave empty for recommended default. [Learn more](https://wiki.mozilla.org/Security/Server_Side_TLS). |

> [!NOTE] Using existing SSL with Lite.
> If you are using an existing SSL certificate, you will have to enable the appropriate SSL options in `settings.env`. SSL files must be stored in `/etc/bitwarden`, which can be referenced in the the `docker-compose.yml` file. These files must match the names configured in `settings.env`.
> 
> The default behavior is to generate a self-signed certificate if SSL is enabled and no existing certificate files are in the expected location (`/etc/bitwarden`).

#### SMTP

Use these variables to setup or change an SMTP provider for your server:

| **Variable** | **Description** |
|------|------|
| globalSettings__mail__replyToEmail | Enter the reply email for your server. |
| globalSettings__mail__smtp__host | Enter host domain for your SMTP server. |
| globalSettings__mail__smtp__port | Enter the port number from the SMTP host. |
| globalSettings__mail__smtp__ssl | If your SMTP host uses SSL enter `true`. Set value to `false` if your host uses TLS service. |
| globalSettings__mail__smtp__username | Enter the SMTP username. |
| globalSettings__mail__smtp__password | Enter the SMTP password. |

#### Ports

Use these variables to configure the ports used for traffic:

| **Variable** | **Description** |
|------|------|
| BW_PORT_HTTP | Change the port used for HTTP traffic. By default, `8080`. |
| BW_PORT_HTTPS | Change the port used for HTTPS traffic. By default, `8443`. |

#### Yubico API

Use these variables to connect with Yubico Web Services:

| **Variable** | **Description** |
|------|------|
| globalSettings__yubico__clientId | Replace value with ID received from your Yubico Key. Sign up for Yubico Key [here](https://upgrade.yubico.com/getapikey/). |
| globalSettings__yubico__key | Input the key value received from Yubico. |

#### Miscellaneous

Use these variables to configure other characteristics of your Bitwarden lite server:

| **Variable** | **Description** |
|------|------|
| globalSettings__disableUserRegistration | Enable or disable user account registration capabilities. |
| globalSettings__hibpApiKey | Enter the API key provided by Have I Been Pwnd. Register to receive the API key [here](https://haveibeenpwned.com/API/Key). |
| adminSettings__admins | Enter admin email addresses. |
| BW_REAL_IPS | Define real IPs in `nginx.conf `in a comma seperated list. Useful for defining proxy servers that forward the client IP address. [Learn more](https://nginx.org/en/docs/http/ngx_http_realip_module.html). |
| BW_CSP | Content-Security-Policy parameter. Reconfiguring this parameter may break features. By changing this parameter, you become responsible for maintaining this value. |
| BW_DB_PORT | Specify a custom port for database traffic. If unspecified, the default will depend on your chosen database provider. |

## Troubleshooting

### Memory usage

By default, the Bitwarden container will consume memory that is available to it, often being more than the minimum needed to run. For memory conscious environments, you can use docker `-m` or `--memory= `to limit the Bitwarden container's memory usage.

| **Name, shorthand** | **Description** |
|------|------|
| --memory=, -m | The maximum amount of memory the container can use. Bitwarden requires at least 200m. See the [Docker documentation](https://docs.docker.com/config/containers/resource_constraints/#limit-a-containers-access-to-memory) to learn more. |

To control memory usage with Docker Compose, use the `mem_limit` key:

```
services:
 bitwarden:
 env_file:
 - settings.env
 image: ghcr.io/bitwarden/lite
 restart: always
 mem_limit: 200m
```
