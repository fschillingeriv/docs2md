# Self-host with Helm

This article will walk you through the procedure to install and deploy Bitwarden in different Kubernetes deployments using a Helm chart.

This article will describe the generic steps for hosting Bitwarden on Kubernetes. Provider-specific guides are available to dive into how you might alter a deployment based on each provider's specific offerings:

- [Azure AKS Deployment](https://bitwarden.com/help/azure-aks-deployment/)
- [OpenShift Deployment](https://bitwarden.com/help/openshift-deployment/)
- [AWS EKS Deployment](https://bitwarden.com/help/aws-eks-deployment/)

> [!NOTE] NGINX Ingress deprecation
> The community-maintained NGINX Ingress Controller (`kubernetes/ingress-nginx`) reached end-of-life in March 2026 and will no longer receive security patches or bug fixes. Bitwarden's Helm chart now includes native support for the Kubernetes Gateway API as the recommended replacement. See Kubernetes' [official statement](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/) for details. If you are currently running Bitwarden with NGINX Ingress, see [Migrating from NGINX Ingress Controller](https://bitwarden.com/help/self-host-with-helm/#migrating-from-nginx-ingress-controller/).

## Requirements

Before proceeding with the installation, ensure the following requirements are met:

- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) is installed.
- [Helm 3](https://helm.sh/docs/intro/install/) is installed.
- You have an SSL certificate and key or access to creating one via a certificate provider.
- You have an SMTP server or access to a cloud SMTP provider.
- A [storage class](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) that supports ReadWriteMany.
- You have an installation id and key retrieved from [https://bitwarden.com/host](https://bitwarden.com/host/).

### Rootless requirements

Bitwarden will detect whether your environment restricts what user containers can be run as during startup and will automatically initiate deployment in rootless mode if restrictions are detected. Successfully deploying in rootless mode requires one of the following two options:

- Deploying an [external MSSQL database](https://bitwarden.com/help/external-db/) instead of the SQL container included by default in the Helm chart.
- Assigning elevated privileges to the included SQL container [using a service account](https://bitwarden.com/help/kubernetes-service-accounts/), [pod security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod), or other method.

> [!TIP] SQL pod as root to non-root
> While Microsoft requires that SQL containers be run as root, container startup will step down to a non-root user before executing application code.

## Prepare the chart

### Add the repo to Helm

Add the repo to Helm using the following commands:

```bash
helm repo add bitwarden https://charts.bitwarden.com/
helm repo update
```

### Create a namespace

Create a namespace to deploy Bitwarden to. Our documentation assumes a namespace called `bitwarden`, so be sure to modify commands if you choose a different name.

```bash
kubectl create namespace bitwarden
```

### Create a configuration

Create a `my-values.yaml` configuration file, which you will use to customize your deployment, using the following command:

```bash
helm show values bitwarden/self-host > my-values.yaml
```

At a minimum, you must configure your `my-values.yaml` file with the values in the following table, however a comprehensive list of values can be found [here](https://github.com/bitwarden/helm-charts/blob/main/charts/self-host/values.yaml).

#### Required variables

| Value | Description |
|------|------|
| `general.domain:` | The domain that will point to your cluster's public IP address. Required for both ingress and Gateway API deployments. |
| `general.admins:` | A comma-separated list of email addresses that will be permitted to access the [System Admin Portal](https://bitwarden.com/help/system-administrator-portal/). |
| `general.email.replyToEmail:` | Email address used for invitations, typically `no_reply@smtp_host`. |
| `general.email.smtpHost:` | Your SMTP server hostname or IP address. |
| `general.email.smtpPort:` | The SMTP port used by the SMTP server. |
| `general.email.smtpSsl:` | Whether your SMTP server uses an encryption protocol (`true` = SSL, `false` = TLS). |
| `enableCloudCommunication:` | Set to `true` to allow communication between your server and our cloud system. Doing so [enables billing and license sync](https://bitwarden.com/help/self-host-an-organization/#step-4-setup-billing-and-license-sync/). |
| `cloudRegion:` | By default, `US`. Set to `EU` if your organization was started via the [EU cloud server](https://bitwarden.com/help/server-geographies/). |
| `sharedStorageClassName:` | The name of the shared storage class, which you will need to provide and must support [ReadWriteMany](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) ([see an example using Azure File Storage](https://bitwarden.com/help/azure-aks-deployment/#creating-a-storage-class/)) unless it's a single-node cluster. |
| `secrets.secretName:` | The name of your [Kubernetes secret object](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data). You will create this object in the next step, so decide on a name now or circle back to this value. |
| `database.enabled:` | Whether to use the SQL pod included in the chart. Only set to `false` if you're using an external SQL server. |
| `component.scim.enabled` | The SCIM pod is disabled by default. To enable the SCIM pod, set value `= true`. |
| `volume.logs.enabled:` | While not required, we recommend setting to `true` for troubleshooting purposes. |

#### Traffic routing options

The following sections describe the methods and values for configuring external traffic to your Bitwarden deployment. `my-values.yaml` includes configurations for both ingress and Gateway API. Enabling both `general.ingress.enabled` and `general.gateway.enabled` simultaneously is not recommended.

##### Ingress

The Kubernetes [Ingress API](https://kubernetes.io/docs/concepts/services-networking/ingress/) remains supported for deployments that use a maintained third-party ingress controller, such as [Azure Application Gateway](https://bitwarden.com/help/azure-aks-deployment/#azure-application-gateway/). Set `general.ingress.enabled: false` and use the `rawManifests` section to configure controllers not defined in the chart ([see an example](https://bitwarden.com/help/add-rawmanifest-files/)).

> [!WARNING] NGINX Ingress Controller is no longer supported
> The community-maintained NGINX Ingress Controller (`kubernetes/ingress-nginx`) reached end-of-life in March 2026 and must not be used for new deployments. If you are currently using it, see [Migrating from NGINX Ingress Controller](https://bitwarden.com/help/self-host-with-helm/#migrating-from-nginx-ingress-controller/).

| Value | Description |
|------|------|
| `general.ingress.enabled:` | Whether to use an ingress controller defined in the chart. |
| `general.ingress.className:` | The ingress class to use, for example `"azure-application-gateway"` ([see an example](https://bitwarden.com/help/azure-aks-deployment/#azure-application-gateway/)). Set `general.ingress.enabled: false` to use other ingress controllers. |
| `general.ingress.annotations:` | Annotations to add to the ingress resource. |
| `general.ingress.paths:` | Defaults are provided that you can customize as needed. |
| `general.ingress.tls.name:` | The name of your TLS certificate. We will walk through [an example](https://bitwarden.com/help/self-host-with-helm/#example-certificate-setup/) later, so enter it now if you have it or circle back later. |
| `general.ingress.tls.clusterIssuer:` | The name of your TLS certificate issuer. We will walk through [an example](https://bitwarden.com/help/self-host-with-helm/#example-certificate-setup/) later, so enter it now if you have it or circle back later. |

##### Gateway API

Bitwarden supports routing traffic using an `HTTPRoute` resource as an alternative to an ingress controller. Gateway API is the recommended approach for new deployments. For additional information, refer to:

- Gateway API [core documentation](https://gateway-api.sigs.k8s.io/guides/getting-started/)
- Gateway API [controller implementations](https://gateway-api.sigs.k8s.io/implementations/)

Configure the following values in `my-values.yaml` to enable Gateway API support:

| Value | Description |
|------|------|
| `general.gateway.enabled:` | Set to `true` to create an `HTTPRoute` resource for Gateway API-based routing. |
| `general.gateway.parentRefs:` | A list of `Gateway` resource references that your `HTTPRoute` attaches to. Each entry should specify the `name` and `namespace` of an externally managed `Gateway` resource. |
| `general.gateway.annotations:` | Annotations to add to the `HTTPRoute` resource. Accepts a map of `key: value` pairs. Leave empty `{}` if no annotations are needed. |
| `general.gateway.labels:` | Labels to add to the `HTTPRoute` resource. Accepts a map of `key: value` pairs. Leave empty `{}` if no labels are needed. |
| `general.gateway.paths:` | Path prefix configuration for each Bitwarden service exposed via `HTTPRoute`. Each entry maps a service to a URL path using `PathPrefix` matching. Do not change the default paths, as they match the required Bitwarden routing. Available path keys are: `web`, `attachments`, `api`, `icons`, `notifications`, `events`, `scim`, `sso`, `identity`, `admin`. |

> [!NOTE] TLS is handled at the Gateway resource level
> TLS termination is configured on the `Gateway` resource, not on the `HTTPRoute`. See [Example Gateway API setup](https://bitwarden.com/help/self-host-with-helm/#example-gateway-api-setup/) for a complete example including TLS configuration.

### Create a secret object

Create a [Kubernetes secret object](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data) to set, at a minimum, the following values:

| Value | Description |
|------|------|
| `globalSettings__installation__id` | A valid installation id retrieved from [https://bitwarden.com/host](https://bitwarden.com/host/). For more information, see [what are my installation id and installation key used for?](https://bitwarden.com/help/hosting-faqs/#general/) |
| `globalSettings__installation__key` | A valid installation key retrieved from [https://bitwarden.com/host](https://bitwarden.com/host/). For more information, see [what are my installation id and installation key used for?](https://bitwarden.com/help/hosting-faqs/#general/) |
| `globalSettings__mail__smtp__username` | A valid username for your SMTP server. |
| `globalSettings__mail__smtp__password` | A valid password for the entered SMTP server username. |
| `globalSettings__yubico__clientId` | Client ID for YubiCloud Validation Service or self-hosted Yubico Validation Server. If YubiCloud, get your client ID and secret key [here](https://upgrade.yubico.com/getapikey/). |
| `globalSettings__yubico__key` | Secret key for YubiCloud Validation Service or self-hosted Yubico Validation Server. If YubiCloud, get your client ID and secret key [here](https://upgrade.yubico.com/getapikey/). |
| `globalSettings__hibpApiKey` | Your HaveIBeenPwned (HIBP) API Key, available [here](https://haveibeenpwned.com/API/Key). This key allows users to run the [Data Breach report](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/) and to check their master password for presence in breaches when they create an account. |
| If you're using the Bitwarden SQL pod, `SA_PASSWORD`. If you're using your own SQL server, `globalSettings__sqlServer__connectionString`. | Credentials for the database connected to your Bitwarden instance. What is required will depend on whether you're using the included SQL pod or an external SQL server. |

For example, using the `kubectl create secret` command to set these values would look like the following:

> [!WARNING] Insecure way of setting a secret
> This example will record commands to your shell history. Other methods may be considered to securely set a secret.

```bash
kubectl create secret generic custom-secret -n bitwarden \
  --from-literal=globalSettings__installation__id="REPLACE" \
  --from-literal=globalSettings__installation__key="REPLACE" \
  --from-literal=globalSettings__mail__smtp__username="REPLACE" \
  --from-literal=globalSettings__mail__smtp__password="REPLACE" \
  --from-literal=globalSettings__yubico__clientId="REPLACE" \
  --from-literal=globalSettings__yubico__key="REPLACE" \
  --from-literal=globalSettings__hibpApiKey="REPLACE" \
  --from-literal=SA_PASSWORD="REPLACE"
```

Don't forget to set the `secrets.secretName:` value in `my-values.yaml` to the name of the created secret, in this case `custom-secret`.

### Example certificate setup

Deployment requires a TLS certificate and key, or access to creating one via a certificate provider. The following example will walk you through using [cert-manager](https://cert-manager.io/docs/) to generate a certificate with Let's Encrypt.

> [!NOTE] cert-manager version
> The commands below reference a specific cert-manager version. Check the [cert-manager releases page](https://github.com/cert-manager/cert-manager/releases) for the latest stable version before running.

1. Install cert-manager on the cluster using the following command:

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.16.3/cert-manager.yaml
```

2. Define a certificate issuer. Bitwarden recommends using the **Staging** configuration until your DNS records have been pointed to your cluster. Be sure to replace the `email:` placeholder with a valid value.

    The correct solver configuration depends on whether you are using an ingress controller or Gateway API:

    **For ingress deployments:**

    ##### Staging

    ```bash
    cat <<EOF | kubectl apply -n bitwarden -f -
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
      name: letsencrypt-staging
    spec:
      acme:
        server: https://acme-staging-v02.api.letsencrypt.org/directory
        email: me@example.com
        privateKeySecretRef:
          name: tls-secret
        solvers:
          - http01:
              ingress:
                class: azure/application-gateway  # update to match your ingress class
    EOF
    ```

    ##### Production

    ```bash
    cat <<EOF | kubectl apply -n bitwarden -f -
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
      name: letsencrypt-production
    spec:
      acme:
        server: https://acme-v02.api.letsencrypt.org/directory
        email: me@example.com
        privateKeySecretRef:
          name: tls-secret
        solvers:
          - http01:
              ingress:
                class: azure/application-gateway  # update to match your ingress class
    EOF
    ```

    **For Gateway API deployments:**

    ##### Staging

    ```bash
    cat <<EOF | kubectl apply -n bitwarden -f -
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
      name: letsencrypt-staging
    spec:
      acme:
        server: https://acme-staging-v02.api.letsencrypt.org/directory
        email: me@example.com
        privateKeySecretRef:
          name: tls-secret
        solvers:
          - http01:
              gatewayAPI:
                gatewayClassName: nginx  # update to match your GatewayClass name
    EOF
    ```

    ##### Production

    ```bash
    cat <<EOF | kubectl apply -n bitwarden -f -
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
      name: letsencrypt-production
    spec:
      acme:
        server: https://acme-v02.api.letsencrypt.org/directory
        email: me@example.com
        privateKeySecretRef:
          name: tls-secret
        solvers:
          - http01:
              gatewayAPI:
                gatewayClassName: nginx  # update to match your GatewayClass name
    EOF
    ```

3. If you haven't already, set the TLS values in `my-values.yaml` to match your chosen routing method:

    - For ingress, set `general.ingress.tls.name:` and `general.ingress.tls.clusterIssuer:`. In this example:

        - `general.ingress.tls.name: tls-secret`
        - `general.ingress.tls.clusterIssuer: letsencrypt-staging`

    - For Gateway API, TLS is configured on the `Gateway` resource directly. Set `general.gateway.parentRefs:` to point to the `Gateway` resource where your TLS listener is defined. See [Example Gateway API setup](https://bitwarden.com/help/self-host-with-helm/#example-gateway-api-setup/) for a complete example.

### Example Gateway API setup

This section walks through a complete Gateway API configuration for Bitwarden using [NGINX Gateway Fabric (NGF)](https://docs.nginx.com/nginx-gateway-fabric/) as the Gateway controller. NGF is an actively maintained open-source implementation from F5/NGINX and is a natural migration path for users coming from the community NGINX Ingress Controller.

Other Gateway API implementations, including [Contour](https://projectcontour.io/), [Envoy Gateway](https://gateway.envoyproxy.io/), and cloud-provider-native options, follow the same general pattern with different `GatewayClass` names. Refer to the [Gateway API implementations list](https://gateway-api.sigs.k8s.io/implementations/) for options.

> [!NOTE] Version compatibility
> The commands below reference specific versions of the Gateway API CRDs and NGINX Gateway Fabric. Check the [NGF releases page](https://github.com/nginx/nginx-gateway-fabric/releases) and the [Gateway API releases page](https://github.com/kubernetes-sigs/gateway-api/releases) for the latest compatible versions before running.

#### 1. Install the Gateway API CRDs

Gateway API CRDs must be installed in the cluster before deploying a Gateway controller. This is a separate step from installing the controller itself.

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.1/standard-install.yaml
```

#### 2. Install NGINX Gateway Fabric

Add the NGINX Gateway Fabric Helm repository and install NGF into a dedicated namespace:

```bash
helm repo add nginx-stable https://helm.nginx.com/stable
helm repo update

helm install ngf nginx-stable/nginx-gateway-fabric \
  --namespace nginx-gateway \
  --create-namespace
```

#### 3. Define a GatewayClass and Gateway

Create a `GatewayClass` that references the NGF controller, and a `Gateway` resource in the `bitwarden` namespace with a TLS listener. Replace `your.domain.com` with your actual domain and `tls-secret` if you are using a different certificate secret name.

```bash
cat <<EOF | kubectl apply -f -
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: nginx
spec:
  controllerName: gateway.nginx.org/nginx-gateway-controller
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: bitwarden-gateway
  namespace: bitwarden
spec:
  gatewayClassName: nginx
  listeners:
    - name: https
      protocol: HTTPS
      port: 443
      hostname: "your.domain.com"
      tls:
        mode: Terminate
        certificateRefs:
          - kind: Secret
            name: tls-secret
            namespace: bitwarden
    - name: http
      protocol: HTTP
      port: 80
      hostname: "your.domain.com"
EOF
```

> [!TIP] Redirect HTTP to HTTPS
> To enforce HTTPS, add an `HTTPRoute` that issues a permanent redirect for HTTP traffic. Refer to the [Gateway API documentation](https://gateway-api.sigs.k8s.io/guides/http-redirect-rewrite/) for an example.

#### 4. Configure my-values.yaml

In your `my-values.yaml`, disable the ingress controller and enable Gateway API, referencing the `Gateway` resource created above:

```yaml
general:
  domain: "your.domain.com"
  ingress:
    enabled: false
  gateway:
    enabled: true
    parentRefs:
      - name: bitwarden-gateway
        namespace: bitwarden
    annotations: {}
    labels: {}
```

#### 5. Install the chart and verify DNS

With your Gateway resources in place, install the chart as described in [Install the chart](https://bitwarden.com/help/self-host-with-helm/#install-the-chart/). The Bitwarden Helm chart will create `HTTPRoute` resources that attach to your `bitwarden-gateway` and route traffic to the appropriate Bitwarden services.

Retrieve the external IP address assigned to your NGF service and point your domain's DNS record to it:

```bash
kubectl get service ngf-nginx-gateway-fabric -n nginx-gateway
```

### Adding rawManifest files

The Bitwarden self-host Helm Chart allows you to include other Kubernetes manifest files either pre- or post-install. To do this, update the `rawManifests` section of the chart ([learn more](https://bitwarden.com/help/add-rawmanifest-files/)). This is useful, for example, in scenarios where you want to use an ingress controller not defined in `my-values.yaml` by default.

> [!NOTE] Traefik CRD API group change
> The Traefik IngressRoute example in the rawManifest documentation uses the `traefik.containo.us/v1alpha1` API group, which was replaced by `traefik.io/v1alpha1` in Traefik v3. If you are running Traefik v3 or later, update the `apiVersion` fields in that example accordingly before applying.

## Install the chart

To install Bitwarden with the configuration setup in `my-values.yaml`, run the following command:

```bash
helm upgrade bitwarden bitwarden/self-host --install --namespace bitwarden --values my-values.yaml
```

Congratulations! Bitwarden is now up and running at `https://your.domain.com`, as defined in `my-values.yaml`. Visit the web vault in your web browser to confirm that it's working. You may now register a new account and log in.

You will need to have set up an SMTP configuration and related secrets in order to verify the email for your new account.

## Next steps

### Migrating from NGINX Ingress Controller

> [!NOTE] New deployments
> This section is for users who are currently running Bitwarden with the community NGINX Ingress Controller (`kubernetes/ingress-nginx`). If you are setting up a new deployment, follow the [Example Gateway API setup](https://bitwarden.com/help/self-host-with-helm/#example-gateway-api-setup/) section above instead.

The community-maintained NGINX Ingress Controller reached end-of-life in March 2026 and no longer receives security patches. Follow the steps below to migrate your existing Bitwarden deployment to a supported Gateway API implementation.

#### Before you begin

- Review your current `my-values.yaml`, particularly any custom annotations or path overrides under `general.ingress`, as these will not carry over directly to a Gateway API configuration.
- Confirm that your cert-manager version is v1.15 or later, as earlier versions do not include the Gateway API HTTP-01 solver. You can check the installed version with:

```bash
kubectl get deployment cert-manager -n cert-manager \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

#### Step 1: Install the Gateway API CRDs

Install the Gateway API CRDs if they are not already present in your cluster:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.1/standard-install.yaml
```

#### Step 2: Install a Gateway API controller

Install NGINX Gateway Fabric (or your preferred Gateway API implementation) alongside your existing NGINX Ingress Controller. Running both during the transition allows you to verify the new setup before cutting over. Refer to steps 2 and 3 of [Example Gateway API setup](https://bitwarden.com/help/self-host-with-helm/#example-gateway-api-setup/) for installation commands and the `GatewayClass` and `Gateway` resource definitions. Use the same domain and `bitwarden` namespace as your existing deployment.

#### Step 3: Update my-values.yaml

Disable the ingress configuration and enable Gateway API:

```yaml
general:
  ingress:
    enabled: false
  gateway:
    enabled: true
    parentRefs:
      - name: bitwarden-gateway
        namespace: bitwarden
    annotations: {}
    labels: {}
```

#### Step 4: Update cert-manager (if applicable)

If you are using cert-manager with Let's Encrypt, update your `ClusterIssuer` to use the Gateway API HTTP-01 solver. Replace the `email:` placeholder and `gatewayClassName` as appropriate:

```bash
cat <<EOF | kubectl apply -n bitwarden -f -
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-production
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: me@example.com
    privateKeySecretRef:
      name: tls-secret
    solvers:
      - http01:
          gatewayAPI:
            gatewayClassName: nginx
EOF
```

#### Step 5: Upgrade the chart

Apply the updated configuration:

```bash
helm upgrade bitwarden bitwarden/self-host --namespace bitwarden --values my-values.yaml
```

Verify that Bitwarden is reachable at your domain and that TLS is functioning correctly before proceeding.

#### Step 6: Uninstall ingress-nginx

Once you have confirmed the Gateway API setup is working, remove the old NGINX Ingress Controller. Replace `<namespace>` with the namespace where ingress-nginx was installed (commonly `ingress-nginx` or `kube-system`):

```bash
helm uninstall ingress-nginx --namespace <namespace>
```

### Database backup and restore

In [this repository](https://github.com/bitwarden/helm-charts/tree/main/examples), we have provided two illustrative example jobs for backing up and restoring the database in the Bitwarden database pod. If you are using your own SQL Server instance that is not deployed as part of this Helm chart, please follow your corporate backup and restore policies.

Database backups and backup policies are ultimately up to the implementor. The backup could be scheduled outside of the cluster to run at a regular interval, or it could be modified to create a CronJob object within Kubernetes for scheduling purposes.

The backup job will create timestamped versions of the previous backups. The current backup is simply called `vault.bak`. These files are placed in the MS SQL backups persistent volume. The restore job will look for `vault.bak` in the same persistent volume.
