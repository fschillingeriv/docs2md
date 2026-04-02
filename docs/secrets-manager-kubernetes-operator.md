---
URL: https://bitwarden.com/help/secrets-manager-kubernetes-operator/
---

# Secrets Manager Kubernetes Operator

The Bitwarden Secrets Manager Kubernetes Operator will allow teams to integrate Secrets Manager into Kubernetes workflows securely and efficiently. Using the operator, which is deployed using [Helm](https://helm.sh/) package manager, secrets can be stored and retrieved from Secrets Manager.

#### Bitwarden Secrets Manager Kubernetes Operator

The `sm-operator` uses a controller to synchronize Bitwarden secrets into Kubernetes secrets. The operator registers the Custom Resource Definition: `BitwardenSecret` into the Kubernetes cluster. The cluster will listen for the newly registered `BitwardenSecret`, and synchronize on a configurable interval.

## Requirements

To get started, an active Bitwarden organization with [Secrets Manager](https://bitwarden.com/help/secrets-manager-overview/) is required. Additionally, one or more [access tokens](https://bitwarden.com/help/access-tokens/) associated with a [machine account](https://bitwarden.com/help/machine-accounts/) are required.

#### Additional dependencies

- [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [Helm 3](https://v3.helm.sh/docs/intro/install/)

## Add the repository to Helm

Add the Bitwarden Secrets Manager chart repository:

```plain text
helm repo add bitwarden https://charts.bitwarden.com/
```

Update information of locally available charts:

```plain text
helm repo update
```

## Installation

#### Create a configuration file

Create a custom values file used for deployment:

```plain text
helm show values bitwarden/sm-operator --devel > my-values.yaml
```

#### Update configuration file

Locate `my-values.yaml` and fill out required values. An example can be located in the [Bitwarden repository](https://github.com/bitwarden/helm-charts/blob/535ad726cfc9dd5c9cd18531c15008d0d939ed74/charts/sm-operator/values.yaml). We recommend that the following values be adjusted for your setup:

| Value | Description |
|------|------|
| `settings.bwSecretsManagerRefreshInterval` | How often the secrets synchronize (in seconds). Minimum value is 180. |
| `settings.cloudRegion` | Self-hosted users set to `US` or `EU` cloud region for sync. See [enable cloud communication](https://bitwarden.com/help/families-for-enterprise-self-hosted/#step-1-enable-cloud-communication/) for additional information. |
| `settings.bwApiUrlOverride` | For self-hosted users only. This is the URL for your instance API, for example `https://your.domain.com/api`. |
| `settings.bwIdentityUrlOverride` | For self-hosted users only. This is the URL for your instance's identity service, for example `https://your.domain.com/identity`. |
| `containers.enableSeccompProfileRuntimeDefault` | Set to `false` to work on older Kubernetes versions (< 1.19) or on vendor versions that do not support this field by default (such as OpenShift < 4.11). This setting is recommended for most common cases that do not require escalating privileges to make containers restrictive. See [Kubernetes documentation](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted) for more information. |

> [!NOTE] Using non-default char image
> To use a different operate image version than the one included with the chart, update:
> `containers.manager.image.tag`.

## Upgrade Helm chart

Once your `values.yaml` file has been configured, upgrade the release to a new chart by running:

```plain text
helm upgrade sm-operator bitwarden/sm-operator -i --debug -n sm-operator-system --create-namespace --values my-values.yaml --devel
```

This command installs or upgrades a release with the name `sm-operator`, in the namespace `sm-operator-system`, with the values from `my-values.yaml`.

> [!NOTE] Informatino for helm install/upgrade
> To see information for the `helm install` or `helm upgrade` commands, run `helm install --help` or `helm upgrade --help`.

## Create Bitwarden secrets

To synchronize secrets stored in Bitwarden Secrets Manager into Kubernetes secrets, we must create a BitwardenSecret object.

1. Create a Kubernetes secret to authenticate with Secrets Manager:

```plain text
kubectl create secret generic bw-auth-token -n <YOUR_NAMESPACE> --from-literal=token="<TOKEN_HERE>"
```

> [!NOTE] Command recorded in shell hsitory
> This command is recorded in your shell history. To avoid exposing access token data, consider deploying with an ephemeral pipeline agent.

## Deploy BitwardenSecret

The `BitwardenSecret` object is the synchronization setting that will be used by the operator to create and synchronize a Kubernetes secret. The Kubernetes secret belongs to a namespace and will be injected with the data that the Secrets Manager [machine account](https://bitwarden.com/help/machine-accounts/) has access to.

Example BitwardenSecret deployment with custom mapping:

```plain text
cat <<EOF | kubectl apply -n <YOUR_NAMESPACE> -f -
apiVersion: k8s.bitwarden.com/v1
kind: BitwardenSecret
metadata:
 labels:
 app.kubernetes.io/name: bitwardensecret
 app.kubernetes.io/instance: bitwardensecret-sample
 app.kubernetes.io/part-of: sm-operator
 app.kubernetes.io/managed-by: kustomize
 app.kubernetes.io/created-by: sm-operator
 name: bitwardensecret-sample
spec:
 organizationId: "a08a8157-129e-4002-bab4-b118014ca9c7"
 secretName: bw-sample-secret
 onlyMappedSecrets: true # default is true
 map:
 - bwSecretId: 6c230265-d472-45f7-b763-b11b01023ca6
 secretKeyName: container__registry__secret
# - bwSecretId: d132a5ed-12bd-49af-9b74-b11b01025d58
# secretKeyName: test__secret__2
 authToken:
 secretName: bw-auth-token
 secretKey: token
EOF
```

By default, the Kubernetes operator will only sync the secrets specified in the `map` section unless you set `onlyMappedSecrets: false`.

| **Setting** | **Description** |
|------|------|
| `metadata.name` | The name of the BitwardenSecret object you are deploying. |
| `spec.organizationId` | The Bitwarden organization ID you are pulling Secrets Manager data from. |
| `spec.secretName` | The name of the Kubernetes secret that will be created and injected with Secrets Manager data. |
| `spec.authToken` | The name of a secret inside of the Kubernetes namespace that the BitwardenSecrets object is being deployed into that contains the Secrets Manager machine account authorization token being used across secrets. |

> [!NOTE] Secrets Manager not guarentee unique secret names
> Secrets Manager does not guarantee unique secret names across projects. By default, secrets will be created with the Secrets Manager secret UUID used as the Key.

To use secrets, create a map of Bitwarden secret IDs to Kubernetes secret keys. The generated secret will replace the Bitwarden Secret IDs with the mapped name you provide. By default, the Kubernetes operator will only sync the secrets specified in the `map` section unless you set `onlyMappedSecrets: false`.

Available map settings:

| Setting | Description |
|------|------|
| `bwSecretId` | This is the UUID (universally unique identifier) of the secret in Secrets Manager. This can be found under the secret name in the Secrets Manager web portal or by using the Bitwarden [Secrets Manager CLI](https://bitwarden.com/help/secrets-manager-cli/). |
| `secretKeyName` | The resulting key inside the Kubernetes secret that replaced the UUID. |

## Example usage chart

```plain text
apiVersion: apps/v1
kind: Deployment
metadata:
 name: my-deployment
 labels:
 app: my-deployment
spec:
 selector:
 matchLabels:
 app: my-deployment
 template:
 metadata:
 labels:
 app: my-deployment
 spec:
 containers:
 - name: my-deployment
 image: <some-image>
 imagePullSecrets:
 - name: container__registry__secret
 envFrom:
 - secretRef:
 name: bw-sample-secret
```
