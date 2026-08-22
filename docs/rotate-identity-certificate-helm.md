---
URL: https://bitwarden.com/help/rotate-identity-certificate-helm/
---

# Rotate a Helm Identity Certificate Password

This article covers a **fixed vulnerability** for some [self-hosted Helm chart deployments](https://bitwarden.com/help/self-host-with-helm/) of the Bitwarden server. The issue was limited to specific installations meeting the criteria below:

> [!WARNING] Helm cert rotation, who's required.
> Rotation is **required** for deployments that meet **all of the following criteria:**
> 
> - You deployed with the `bitwarden/self-host` Helm chart.
> - Your deployment was **first installed**on a chart version **earlier than**`2.0.0`.
> - You use the default chart-generated certificate (`secrets.identityCertificate.generate: true`).

## Background

The Bitwarden Identity Server signs its access and refresh tokens with a PKCS#12 (`.pfx`) certificate. On the Helm chart, that certificate and its password are generated at install time and stored in two Kubernetes secrets.

Chart versions before `2.0.0` had a defect that set the `.pfx` password to the fixed value `map[]` on every install. Because that value is public and identical everywhere, anyone who obtains your `identity.pfx` (via a backup, snapshot, support bundle, or pod access) can decrypt it and recover your token-signing private key.

The defect is fixed in `2.0.0`+ (passwords are now per-install random values), but upgrading doesn't rotate an existing password — it's created once and preserved across upgrades. So if you first installed on a version earlier than `2.0.0`, your certificate keeps the `map[]` password **until you rotate it**, which when done re-encrypts the existing certificate with a new random password. 

This has been fixed in versions above `2.0.0`, wherein the default chart-generated certificate now generates random passwords per installation. If you first installed the Bitwarden server using an earlier version of the Helm chart with the default certificate, **you must manually rotate**your certificate password as rotation is not a function of the upgrade process.

Chart versions `2.3.0` and above include a detection check that will automatically halt an upgrade if your `.pfx` password is still the defective value.

## Rotate your certificate password

> [!NOTE] Helm Cert rotation, check for namespace
> In all of the following sections, replace `<release>` and `<namespace>` with your values. If you are unsure of your release name or namespace, run `helm list -A` to list all Helm releases and their namespaces. 
> 
> You will also need:
> 
> - `kubectl` access to the cluster and namespace, with permission to read, delete, and create secrets and to restart deployments.
> - `openssl` available locally.

### Check your certificate password

The criteria documented in the warning above can help you determine whether you are impacted, however if you'd like to confirm it yourself you can decode the stored certificate password:

```plain text
kubectl get secret <release>-identity-cert-password -n <namespace> -o jsonpath='{.data.globalSettings__identityServer__certificatePassword}' | base64 -d; echo
```

If the command returns `map[]`, you are affected and should begin this procedure as soon as possible. If the command returns a long, random alphanumeric string, your certificate already has a strong password and no action is needed.

### What happens after you rotate

Rotating the certificate password will involve a restart of the `identity` and `sso` pods, so expect a short interruption to sign-in and token refresh and plan to rotate during a specifically-flagged maintenance window or otherwise low-traffic window. Access tokens issued to your users will remain verifiable, meaning no unexpected sign-out should occur.

### Recommended procedure

The following procedure re-encrypts the existing certificate with a new password:

1. Export your certificate, specifically the -identity-cert secret, from the cluster:

```bash
kubectl get secret <release>-identity-cert -n bitwarden -o jsonpath='{.data.identity\.pfx}' | base64 -d > identity.pfx
```

Once exported, check that the file is not empty:

```bash
wc -c < identity.pfx
```

A returned size of `0` would indicate that the secret or `identity.pfx` was not found, typically due to a typo in the secret name.
2. Generate a new password and re-encrypt the certificate with your new password. The following three commands should be run **verbatim**, **independently**, and in the **same shell session**:

```bash
export NEW_PASSWORD=$(openssl rand -base64 24)
openssl pkcs12 -in identity.pfx -out identity.pem -nodes -passin pass:'map[]'
openssl pkcs12 -export -out identity-rotated.pfx -in identity.pem -passout env:NEW_PASSWORD
```

> [!NOTE] Warn: If step of helm cert password rotation fails
> If this step fails because the certificate cannot be read, generate a replacement certificate using the following commands and load it into the `-identity-cert` and `-identity-cert-password` secrets (**Step 3**):
> 
> 
> ```bash
> openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout identity.key -out identity.crt -subj "/CN=Bitwarden IdentityServer" -days 10950
> openssl pkcs12 -export -out ./identity/identity.pfx -inkey identity.key -in identity.crt -passout pass:<your-pfx-password>
> ```
> 
> Be aware that implementing a **new certificate will invalidate every issued token**, meaning all users will be signed out and will need to log in again. Only do this if re-encrypting is not possible.
3. Update the `-identity-cert` and `-identity-cert-password` secrets in-place:

```bash
kubectl create secret generic <release>-identity-cert -n bitwarden --from-file=identity.pfx=./identity-rotated.pfx --dry-run=client -o yaml | kubectl apply -f -
kubectl create secret generic <release>-identity-cert-password -n bitwarden --from-literal=globalSettings__identityServer__certificatePassword="$NEW_PASSWORD" --dry-run=client -o yaml | kubectl apply -f -
```

Both commands should be expected to return a `resource secrets/... is missing the kubectl.kubernetes.io/last-applied-configuration annotation` warning, which can be ignored.
4. Confirm that the new password secret now holds a new random value:

```bash
kubectl get secret <release>-identity-cert-password -n bitwarden -o jsonpath='{.data.globalSettings__identityServer__certificatePassword}' | base64 -d; echo
```
5. Restart the components that consume the certificate, meaning the `identity` and `sso` pods:

```bash
kubectl rollout restart deployment/<release>-identity -n bitwarden
kubectl rollout restart deployment/<release>-sso -n bitwarden

kubectl rollout status deployment/<release>-identity -n bitwarden
kubectl rollout status deployment/<release>-sso -n bitwarden
```
6. Once both rollouts have completed successfully, delete the local working files. In particular, `identity.pem` must be deleted as it contains the unencrypted private key:

```bash
rm identity.pfx identity.pem identity-rotated.pfx
```

Once all steps are complete, you may continue with a `helm upgrade` as normal.
