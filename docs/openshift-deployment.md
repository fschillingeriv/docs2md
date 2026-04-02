---
URL: https://bitwarden.com/help/openshift-deployment/
---

# OpenShift Deployment

This article dives into how you might alter your [Bitwarden self-hosted Helm Chart](https://bitwarden.com/help/self-host-with-helm/) deployment based on the specific offerings of OpenShift.

## Requirements

Before proceeding with the installation, ensure the following requirements are met:

- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) is installed.
- [Helm 3](https://helm.sh/docs/intro/install/) is installed.
- You have an SSL certificate and key or access to creating one via a certificate provider.
- You have a SMTP server or access to a cloud SMTP provider.
- A [storage class](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) that supports ReadWriteMany.
- You have an installation id and key retrieved from [https://bitwarden.com/host](https://bitwarden.com/host/).

### Rootless requirements

Bitwarden will detect whether your environment restricts what user containers can be run as during startup and will automatically initiate deployment in rootless mode if restriction is detected. Successfully deploying in rootless mode requires one of the following two options:

- Deploying an [external MSSQL database](https://bitwarden.com/help/external-db/) instead of the SQL container included by default in the Helm chart.
- Assigning elevated privileges to the included SQL container [using a service account](https://bitwarden.com/help/kubernetes-service-accounts/), [pod security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod), or other method.

> [!TIP] SQL pod as root to non-root
> While Microsoft requires that SQL containers be run as root, container startup will step down to a non-root user before executing application code.

## OpenShift routes

This example will demonstrate [OpenShift Routes](https://docs.openshift.com/container-platform/3.11/architecture/networking/routes.html#overview) instead of the default ingress controllers.

#### Disable default ingress

1. Access `my-values.yaml`.
2. Disable the default ingress by specifying `ingress.enabled: false`:

```bash
general:
 domain: "replaceme.com"
 ingress:
 enabled: false
```

The remaining ingress values do not require modification, as setting `ingress.enabled: false` will prompt the chart to ignore them.

#### Add raw manifest for routes

Locate the `rawManifests` section in `my-values.yaml`. This section is where the OpenShift Route manifests will be assigned.

An example file for a `rawManifests` section that uses OpenShift Routes can be downloaded ⬇️ [here](https://bitwarden.com/assets/330r6BrWsFLL9FLZbPSLIc/badadefadd43ce575fd5f42221155786/rawManifests.yaml). 

> [!NOTE] Rawmanifest example
> In the example provided above, `destinationCACertificate` has been set to an empty string. This will use the default certificate setup in OpenShift. Alternatively, specify a certificate name here, or you can use Let's Encrypt by following [this guide](https://developer.ibm.com/tutorials/secure-red-hat-openshift-routes-with-lets-encrypt/). If you do, you will be required to add `kubernetes.io/tls-acme: "true"` to the annotations for each route.

## Shared storage class

A shared storage class is required for most OpenShift deployments. `ReadWriteMany` storage must be enabled. This can be done through the method of your choice, one option is to use the [NFS Subdir External Provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner/blob/master/charts/nfs-subdir-external-provisioner/README.md).

## Secrets

The `oc` command can be used to deploy secrets. A valid installation id and key can be retrieved from [bitwarden.com/host/](https://bitwarden.com/host/). For more information, see [What are my installation id and installation key used for?](https://bitwarden.com/help/hosting-faqs/#q-what-are-my-installation-id-and-installation-key-used-for/)

The following command is an example:

> [!WARNING] Insecure way of setting a secret
> This example will record commands to your shell history. Other methods may be considered to securely set a secret.

```bash
oc create secret generic custom-secret -n bitwarden \
 --from-literal=globalSettings__installation__id="REPLACE" \
 --from-literal=globalSettings__installation__key="REPLACE" \
 --from-literal=globalSettings__mail__smtp__username="REPLACE" \
 --from-literal=globalSettings__mail__smtp__password="REPLACE" \
 --from-literal=globalSettings__yubico__clientId="REPLACE" \
 --from-literal=globalSettings__yubico__key="REPLACE" \
 --from-literal=globalSettings__hibpApiKey="REPLACE" \
 --from-literal=SA_PASSWORD="REPLACE" # If using SQL pod 
 # --from-literal=globalSettings__sqlServer__connectionString="REPLACE" # If using your own SQL server
```
