---
URL: https://bitwarden.com/help/server-logs/
---

# Server Logs

This article contains information about accessing and configuring the storage of server logs. The particulars will depend on your deployment method:

### Docker

## Logs in real time

If you've deployed Bitwarden with Docker, use the `docker compose logs -f` command to follow logging in real-time from the terminal or command-line. Note that this command should be run from the `/bwdata/docker` directory:

```bash
cd /opt/bitwarden/bwdata/docker
docker compose logs -f
```

## Logs in storage

Logs created by self-hosted Bitwarden servers are, by default, stored in `bwdata/logs/`. 

To change the default log storage location, access your `global.override.env` file and set the [environment variable](https://bitwarden.com/help/environment-variables/#optional-variables/) `globalSettings__logDirectory=` to the desired location. 

After changing environment variables, you will be required to restart your server to apply the new configuration:

- If you're using the standard deployment method, use the `bitwarden.sh` or `bitwarden.ps1 restart` command.
- If you're deploying Bitwarden manually or offline, use `docker compose down` and back `up`, for example:

```
docker compose -f ./docker/docker-compose.yml down && docker compose -f ./docker/docker-compose.yml up -d
```

## Download logs

If you've deployed Bitwarden with Docker using the `bitwarden.sh` or `bitwarden.ps1` installation script, you can additionally use the `compresslogs` command to download a tarball of all server logs, or all server logs in a specified date range:

```bash
./bitwarden.sh compresslogs 20240304 20240305
.\bitwarden.ps1 -compresslogs 20240304 20240305
```

### Helm

## Logs in real time

By default, logs for Helm deployments are ephemeral and aren't stored in a central location. While the server is running, logs can be accessed in real time through a container's stdout, for example by running the following command:

```bash
kubectl logs pod api
```

## Logs in storage

You can configure the server to save logs to a persistent volume (PVC) by setting the `volume.logs.enabled:` value in your `my-values.yaml` file to `true`. By default logs are saved to a new PVC, however you can use an existing PVC by configuring the `volume.logs.existingClaim:` value.
