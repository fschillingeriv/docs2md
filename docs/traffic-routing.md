---
URL: https://bitwarden.com/help/traffic-routing/
---

# Traffic Routing

> [!NOTE]
> NGINX Ingress has reached EOL and will no longer receive support. Bitwarden has included configurations for Gateway API in `my-values.yaml`. Please see Kubernetes' [official statement](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/) on the deprecation of NGINX Ingress.

This article provides sample traffic routing configurations for Kubernetes based Bitwarden deployments, and should be used alongside [Self-host with Helm](https://bitwarden.com/help/self-host-with-helm/). This article covers a standard Gateway API setup, as well as migration steps if you are running the deprecated NGINX Ingress configuration.

## Prerequisites

Before proceeding with the Gateway API setup, ensure the following requirements and initial setup have been completed in [Self-host with Helm](https://bitwarden.com/help/self-host-with-helm/#requirements/):

1. [Bitwarden namespace created](https://bitwarden.com/help/self-host-with-helm/#prepare-the-chart/)
2. [Create Secrets](https://bitwarden.com/help/self-host-with-helm/#create-a-secret-object/)
3. [Create and install certificates](https://bitwarden.com/help/self-host-with-helm/#example-certificate-setup/)

## NGINX Gateway Fabric

The following sections include instructions to [setup](https://bitwarden.com/help/helm-traffic-routing/#install-the-gateway-api-custom-resource-definition/) or [migrate](https://bitwarden.com/help/helm-traffic-routing/#migrating-from-nginx-ingress-to-gateway-api/) from NGINX Ingress to NGINX Gateway Fabric. Configure Gateway API for your Bitwarden Helm deployment using the steps below:

- **New Deployment**: Follow the steps in order.
- **Migrating from NGINX Ingress:**Complete the steps up to Create the Gateway resource, then skip to [Migrating from NGINX Ingres](https://bitwarden.com/help/helm-traffic-routing/#migrating-from-nginx-ingress-to-gateway-api/) to [NGINX Gateway Fabric](https://bitwarden.com/help/helm-traffic-routing/#migrating-from-nginx-ingress-to-gateway-api/).

### Install the Gateway API custom resource definition

Install the Gateway API custom resource definitions before deploying a Gateway controller. The following example is using NGINX Gateway Fabric v2.4.2:

```bash
kubectl kustomize "https://github.com/nginx/nginx-gateway-fabric/config/crd/gateway-api/standard?ref=v2.4.2" | kubectl apply -f -
```

> [!NOTE] CRD versions are tied to the Gateway controller version
> CRD versions are tied to the Gateway controller version. Check your controller's documentation to confirm the compatible CRD version before running this command. In this example, the CRD version is tied to NGINX Gateway Fabric.

Additional implementation options can be found in Gateway API's documentation.

### Install a Gateway controller

A Gateway controller handles the traffic routing. To install NGINX Gateway Fabric using Helm:

```bash
helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric \
 --create-namespace \
 -n nginx-gateway \
 --set nginx.service.type=LoadBalancer
```

### Create the Gateway resource

Create a `Gateway` resource in the `bitwarden` namespace. The Gateway terminates TLS using the `self-signed-cert` secret created during the [prerequisite setup](https://bitwarden.com/help/self-host-with-helm/), and restricts attached routes to the same namespace.

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
 name: bw-gateway
 namespace: bitwarden
spec:
 # Change this if your controller uses a different GatewayClass.
 # For example, many environments will NOT use "nginx" here.
 gatewayClassName: nginx
 listeners:
 - name: http
 hostname: bw.localtest.me # change this value
 port: 80
 protocol: HTTP
 allowedRoutes:
 namespaces:
 from: Same
 - name: https
 hostname: bw.localtest.me # change this value
 port: 443
 protocol: HTTPS
 tls:
 mode: Terminate
 certificateRefs:
 - kind: Secret
 name: self-signed-cert
 allowedRoutes:
 namespaces:
 from: Same
```

If your setup requires HTTP to HTTPS redirect, you can use the following additional route to a `redirect.yaml` file:

[Embedded content]To apply HTTP to HTTPS:

[Embedded content]Apply the manifest:

```bash
kubectl apply -f gateway.yaml
```

To list the `GatewayClass` resources installed by your controller, run:

[Embedded content]The `gatewayClassName` value above must match one of these.

> [!NOTE] Continue to Migrate
> At this point, if you are migrating from an NGINX Ingress setup, continue to [Migrating from NGINX Ingress to Gateway API](https://bitwarden.com/help/helm-traffic-routing/#migrating-from-nginx-ingress-to-gateway-api/).

### Configure the Helm chart for Gateway API

Update the `my-values.yaml` file to disable the deprecated Ingress, and enable the Gateway API HTTPRoute. Set `parentRefs` to point to the Gateway:

```yaml
general:
 ingress:
 # Ingress is deprecated. Disable it when using Gateway API.
 enabled: false
 gateway:
 # Set to true to create an HTTPRoute resource managed by the Helm chart.
 enabled: true
 # parentRefs attach the HTTPRoute to the Gateway.
 parentRefs:
 - name: bw-gateway # Must match the Gateway metadata.name
 namespace: bitwarden # Must match the Gateway metadata.namespace
 sectionName: https # Must match the listener name in the Gateway spec
```

Apply the changes:

```bash
helm upgrade bitwarden bitwarden/self-host \
 --install \
 --namespace bitwarden \
 --values my-values.yaml
```

> [!NOTE] ingress & Gateway API parallel use
> The provided `my-values.yaml` file includes configurations for both Ingress and Gateway API setups. Both of these methods can be utilized at the same time depending on your specific infrastructure needs.

### HTTPRoute functionality

When `general.gateway.enabled` is `true`, the Helm chart creates an `HTTPRoute` resource in the `bitwarden` namespace. The `HTTPRoute` attaches to the Gateway defined in `parentRefs` and routes traffic to each Bitwarden service by path prefix. The HTTPRoute chart produced by the configuration can be reviewed [here](https://bitwarden.com/assets/2BFMWDWYdIOkE0AwvxN5Jr/357fdcbfcdbde5fe76c6a02659c5e10b/HTTPRoute.yaml).

> [!NOTE] TLS handled on gateway level
> TLS is handled at the Gateway level, not the HTTPRoute. Do not add TLS configuration to the HTTPRoute resource.

## Migrating from NGINX Ingress to Gateway API

If you have an existing Bitwarden Helm deployment using the deprecated `general.ingress` configuration, you may migrate to Gateway API. If you have not completed [Install NGINX Gateway Fabric](https://bitwarden.com/help/helm-traffic-routing/#install-a-gateway-controller/), and [Create Gateway resource](https://bitwarden.com/help/helm-traffic-routing/#create-the-gateway-resource/) from the steps above, please do so before returning to this section.

1. Next, update your values file to disable Ingress and enable the Gateway:

```yaml
general:
 ingress:
 enabled: false
 gateway:
 enabled: true
 parentRefs:
 - name: bw-gateway
 namespace: bitwarden
 sectionName: https
```
2. Apply the changes:

```bash
helm upgrade bitwarden bitwarden/self-host \
 --namespace bitwarden \
 --values my-values.yaml
```

The chart will delete the old `Ingress` resource and create the `HTTPRoute` in its place.
