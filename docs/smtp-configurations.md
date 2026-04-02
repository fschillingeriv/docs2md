---
URL: https://bitwarden.com/help/smtp-configurations/
---

# SMTP Configurations

This guide covers SMTP (simple mail transfer protocol) setup and common configuration issues for Bitwarden self-hosted servers. SMTP is handled across the `api`, `identity`, `admin`, and `notifications` containers. All settings are configured in `global.override.env`.

> [!NOTE] SMTP required in self-host deployments
> SMTP is required in self-hosted deployments, as it is necessary for sending [emails from Bitwarden](https://bitwarden.com/help/list-of-emails/) and facilitating [system administrator portal](https://bitwarden.com/help/system-administrator-portal/) access.

## Configuration location

Manage and update your SMTP settings by accessing the `global.override.env` file.

## SMTP setup best practices

### Use port 587 for email submission

Port 587 is the default mail submission port. This port is the industry standard for mail submission, works with TLS encryption and follows IETF guidelines.

> [!NOTE] Bitwarden port configuation 
> Always configure Bitwarden to use port 587 unless you have specific technical requirements and explicit approval from your hosting provider.

### Avoid port 25 for application email

Port 25 should not be used for Bitwarden email configuration and is not suitable for application level email submission. This port is intended for server-to-server SMTP relaying only, and commonly blocked by residential ISPs and cloud hosting providers. 

## Security configuration best practices

### Enable TLS encryption

Always use TLS encryption to protect email contents and credentials:

```bash
globalSettings__mail__smtp__port=587
globalSettings__mail__smtp__ssl=false
globalSettings__mail__smtp__startTls=true
```

Port 587 uses TLS by default through `startTls`. Set `ssl=false` when using `startTls`.

### Certificate handling

For production environments, ensure your SMTP server has a valid and trusted SSL/TLS certificate. For troubleshooting, development, or testing environments with self-signed certificates, you can use:

```bash
globalSettings__mail__smtp__trustServer=true
```

> [!NOTE] In production always use validated certificates
> Only use `trustServer=true` in controlled development environments. For production systems, always use properly validated certificates to prevent man-in-the-middle attacks.

### Validate a server certificate

To configure Bitwarden to validate your server certificate:

### Docker

1. Copy your root CA certificate into `./bwdata/ca-certificates`.
2. Run the `./bitwarden.sh restart` command to apply the certificate to your containers and restart your server.

### Helm

1. In your `my-values.yaml` configuration file, set the value `caCertificate.enabled: true`.
2. Create a ConfigMap object that contains your certificate file. The simplest way is to add a `preInstall` [RawManifest](https://bitwarden.com/help/add-rawmanifest-files/) to your `my-values.yaml` file, as in the following example:

```bash
rawManifests:
 preInstall:
 - kind: ConfigMap
 apiVersion: v1
 metadata:
 name: cacert
 data:
 rootca.crt: |
 -----BEGIN CERTIFICATE-----
 ...
 -----END CERTIFICATE-----
 postInstall:
```

## Recommended configurations

The section demonstrates common SMTP configurations to reference when setting up a self-hosted environment.

### Standard enterprise SMTP configuration

The following is an example of a standard SMTP configuration:

```bash
globalSettings__mail__replyToEmail=no-reply@yourdomain.com
globalSettings__mail__smtp__host=mail.yourdomain.com
globalSettings__mail__smtp__port=587
globalSettings__mail__smtp__ssl=false
globalSettings__mail__smtp__startTls=true
globalSettings__mail__smtp__username=bitwarden@yourdomain.com
globalSettings__mail__smtp__password=your-secure-password
```

### Example Office 365 configuration

For organizations using Microsoft Office 365:

```bash
globalSettings__mail__replyToEmail=bitwarden@yourdomain.com
globalSettings__mail__smtp__host=smtp.office365.com
globalSettings__mail__smtp__port=587
globalSettings__mail__smtp__ssl=false
globalSettings__mail__smtp__username=bitwarden@yourdomain.com
globalSettings__mail__smtp__password=your-secure-password
```

Microsoft recommends using a dedicated service account rather than a personal mailbox. Refer to Microsoft's documentation for [configuring multifunction devices](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365) or applications for detailed setup guidance.

### Apply configuration changes

Configuration changes require a full server restart to take effect. Apply your configuration changes to `global.override.env` and then perform a restart to apply your changes:

```bash
./bitwarden.sh restart
```

> [!NOTE] Always compelte stop and start cycle
> Only restarting individual containers will not apply configuration changes.

### Verify container health

Before deploying to production, always verify that all containers are healthy:

```plain text
docker ps
```

### Test SMTP connectivity

Before going live, test SMTP connectivity from within the API container to ensure network paths are clear and authentication works correctly.

1. Access the API container:

```plain text
sudo docker ps
sudo docker exec -it <CONTAINER_ID> sh
```
2. Install testing tools:

```bash
apk update
apk add busybox-extras
```
3. Test connectivity:

```bash
telnet <smtp_server> 587
```

A successful connection confirms that network connectivity and firewall rules are properly configured.

### Monitor email logs

Regularly review email-related logs in these locations to catch issues early:

- `./bwdata/logs/admin/`
- `./bwdata/logs/api/`
- `./bwdata/logs/identity/`
- `./bwdata/logs/notifications/`

Implement log monitoring or alerting for email delivery failures in production environments.

## Additional configuration options

Bitwarden supports additional [SMTP environment](https://bitwarden.com/help/environment-variables/#optional-variables/) variables. Review these options to customize email behavior according to your organization's requirements.

## Summary checklist

Before deploying your Bitwarden SMTP configuration, check for the following best practices:

- A Port configured for email submission (such as port 587)
- TLS encryption enabled
- Strong, unique SMTP credentials configured
- Professional reply-to address set
- Connectivity tested from API container
- All containers show as healthy
- Configuration applied via full server restart
- Log monitoring implemented
- Valid SSL/TLS certificates in use (production)
- Documentation updated with configuration details
