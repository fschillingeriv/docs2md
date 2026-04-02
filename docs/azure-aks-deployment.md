---
URL: https://bitwarden.com/help/azure-aks-deployment/
---

# Azure AKS Deployment

This article dives into how you might alter your [Bitwarden self-hosted Helm Chart](https://bitwarden.com/help/self-host-with-helm/) deployment based on the specific offerings of Azure and AKS.

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

## Ingress controllers

This section documents 2 options for ingress controllers that can be used in your Azure AKS deployment:

- Using the **Azure nginx** ingress controller to optionally integrate with Azure DNS for zone management and Azure Key Vault for certificate issuance.
- Using the **Azure Application Gateway** ingress controller (AGIC) to deploy Bitwarden behind an application load balancer.

### Azure nginx

Azure provides an nginx ingress controller option that supports an application routing add-on and optionally integrates with Azure DNS for zone management and Azure Key Vault for certificate issuance. If you use this option:

1. [Create a "managed" nginx ingress controller.](https://learn.microsoft.com/en-us/azure/aks/app-routing#create-the-ingress-object)
2. In your `my-values.yaml` file, set `general.ingress.className:`to `webapprouting.kubernetes.azure.com`.
3. In your `my-values.yaml` file, uncomment the following values:

```yaml
nginx.ingress.kubernetes.io/use-regex: "true"
nginx.ingress.kubernetes.io/rewrite-target: /$1
```

Once complete, you can retrieve the IP address assigned to your Azure nginx ingress controller using the command `kubectl get ingress -n bitwarden`. It may take a few minutes after deployment for your IP address to populate.

### Azure Application Gateway

Azure customers may, however, prefer to use an Azure Application Gateway as the ingress controller for their AKS cluster in order to deploy Bitwarden behind an application load balancer. 

#### Before installing the chart

If you prefer this option, **before** [installing the chart](https://bitwarden.com/help/self-host-with-helm/#install-the-chart/) you must:

1. [Enable the Azure Application Gateway ingress controller for your cluster](https://learn.microsoft.com/en-us/azure/application-gateway/tutorial-ingress-controller-add-on-existing).
2. Update your my-values.yaml file, specifically `general.ingress.className:`, `general.ingress.annotations:`, and `general.ingress.paths:`:

```bash
general:
 domain: "replaceme.com"
 ingress:
 enabled: true
 className: "azure-application-gateway" # This value might be different depending on how you created your ingress controller. Use "kubectl get ingressclasses -A" to find the name if unsure.
 ## - Annotations to add to the Ingress resource.
 annotations:
 appgw.ingress.kubernetes.io/ssl-redirect: "true"
 appgw.ingress.kubernetes.io/use-private-ip: "false" # This might be true depending on your setup.
 appgw.ingress.kubernetes.io/rewrite-rule-set: "bitwarden-ingress" # Make note of whatever you set this value to. It will be used later.
 appgw.ingress.kubernetes.io/connection-draining: "true" # Update as necessary.
 appgw.ingress.kubernetes.io/connection-draining-timeout: "30" # Update as necessary.
 ## - Labels to add to the Ingress resource.
 labels: {}
 # Certificate options.
 tls:
 # TLS certificate secret name.
 name: tls-secret
 # Cluster cert issuer (e.g. Let's Encrypt) name if one exists.
 clusterIssuer: letsencrypt-staging
 paths:
 web:
 path: /(.*)
 pathType: ImplementationSpecific
 attachments:
 path: /attachments/(.*)
 pathType: ImplementationSpecific
 api:
 path: /api/(.*)
 pathType: ImplementationSpecific
 icons:
 path: /icons/(.*)
 pathType: ImplementationSpecific
 notifications:
 path: /notifications/(.*)
 pathType: ImplementationSpecific
 events:
 path: /events/(.*)
 pathType: ImplementationSpecific
 scim:
 path: /scim/(.*)
 pathType: ImplementationSpecific
 sso:
 path: /(sso/.*)
 pathType: ImplementationSpecific
 identity:
 path: /(identity/.*)
 pathType: ImplementationSpecific
 admin:
 path: /(admin/?.*)
 pathType: ImplementationSpecific
```
3. If you're going to use the provided Let's Encrypt example for your TLS certificate, update `spec.acme.solvers.ingress.class:` in the script linked [here](https://bitwarden.com/help/self-host-with-helm/#example-certificate-setup/) to `"azure/application-gateway"`.
4. In the Azure Portal, create an empty rewrite set for Application Gateway:

 1. Navigate to the **Load balancing** > **Application Gateway** in the Azure Portal and select your Application Gateway.
 2. Select the **Rewrites**blade.
 3. Select the + **Rewrite set** button.
 4. Set the **Name**to the value specified for `appgw.ingress.kubernetes.io/rewrite-rule-set:` in `my-values.yaml`, in this example `bitwarden-ingress`.
 5. Select **Next**and **Create**.

#### After installing the chart

**After** [installing the chart](https://bitwarden.com/help/self-host-with-helm/#install-the-chart/), you will also be required to create rules for your rewrite set:

1. Re-open the empty rewrite set you created before installing the chart.
2. Select all routing paths that begin with `pr-bitwarden-self-host-ingress...`, de-select any that do not begin with that prefix, and select **Next**.
3. Select the + **Add Rewrite rule** button. You can give your rewrite rule any name and any sequence.
4. Add the following condition:

 - **Type of variable to check**: Server variable
 - **Server variable**: uri_path
 - **Case-sensitive**: No
 - **Operator**: equal (=)
 - **Pattern to match**: `^(\/(?!admin)(?!identity)(?!sso)[^\/]*)\/(.*)`
5. Add the following action:

 - **Rewrite type**: URL
 - **Action type**: Set
 - **Components**: URL path
 - **URL path value**: `/{var_uri_path_2}`
 - **Re-evaluate path map**: Unchecked
6. Select **Create**.

## Creating a storage class

Deployment requires a shared storage class that you provide, which must support [ReadWriteMany](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes). The following example is a script you can run in the Azure Cloud Shell to create an Azure File Storage class that meets the requirement:

> [!WARNING] It's just an example
> The following is an illustrative example, be sure to assign permissions according to your own security requirements.

```bash
cat <<EOF | kubectl apply -n bitwarden -f -
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
 name: azure-file
 namespace: bitwarden
provisioner: file.csi.azure.com
allowVolumeExpansion: true
mountOptions:
 - dir_mode=0777
 - file_mode=0777
 - uid=0
 - gid=0
 - mfsymlinks
 - cache=strict
 - actimeo=30
parameters:
 skuName: Standard_LRS
EOF
```

You must set the `sharedStorageClassName` value in `my-values.yaml` to whatever name you give the class, in this example:

```bash
sharedStorageClassName: "azure-file"
```

## Using Azure Key Vault CSI Driver

Deployment requires Kubernetes secrets objects to set sensitive values for your deployment. While the `kubectl create secret` command can be used to set secrets, Azure customers may prefer to use Azure Key Vault and the Secrets Store CSI Driver for AKS:

> [!TIP] Key Vault existing is assumed
> These instructions assume you already an have Azure Key Vault setup. If not, [create one now](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver#create-or-use-an-existing-azure-key-vault).

1. Add Secrets Store CSI Driver support to your cluster with the following command:

```bash
az aks enable-addons --addons azure-keyvault-secrets-provider --name myAKSCluster --resource-group myResourceGroup
```

The add-on creates a user-assigned managed identity you can use to authenticate to your key vault, however you have other [options for identity access control](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-identity-access). If you use the created user-assigned managed identity, you will need to explicitly assign **Secret** > **Get** access to it ([learn how](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy?tabs=azure-portal)).
2. Create a SecretProviderClass, as in the following example.

The `parameters` section of the following YAML file is accurate for most environments. However, depending on your setup, you may need to change some values; for example, `cloudName` should be set to `AzureUSGovernmentCloud` for Azure US Government Cloud. Consult [Microsoft's documentation](https://azure.github.io/secrets-store-csi-driver-provider-azure/docs/getting-started/usage/#create-your-own-secretproviderclass-object) for full details.

The `parameters` section also contains `<REPLACE>` placeholders that you must replace, and will be slightly different depending on if you are using the included SQL pod or using your own SQL server.

```bash
cat <<EOF | kubectl apply -n bitwarden -f -
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
 name: bitwarden-azure-keyvault-csi
 labels:
 app.kubernetes.io/component: secrets
 annotations:
spec:
 provider: azure
 parameters:
 useVMManagedIdentity: "true" # Set to false for workload identity
 userAssignedIdentityID: "<REPLACE>" # Set the clientID of the user-assigned managed identity to use
 # clientID: "<REPLACE>" # Setting this to use workload identity
 keyvaultName: "<REPLACE>"
 cloudName: "AzurePublicCloud"
 objects: |
 array:
 - |
 objectName: installationid
 objectAlias: installationid
 objectType: secret
 objectVersion: ""
 - |
 objectName: installationkey
 objectAlias: installationkey
 objectType: secret
 objectVersion: ""
 - |
 objectName: smtpusername
 objectAlias: smtpusername
 objectType: secret
 objectVersion: ""
 - |
 objectName: smtppassword
 objectAlias: smtppassword
 objectType: secret
 objectVersion: ""
 - |
 objectName: yubicoclientid
 objectAlias: yubicoclientid
 objectType: secret
 objectVersion: ""
 - | 
 objectName: yubicokey
 objectAlias: yubicokey
 objectType: secret
 objectVersion: ""
 - |
 objectName: hibpapikey
 objectAlias: hibpapikey
 objectType: secret
 objectVersion: ""
 - | 
 objectName: sapassword #-OR- dbconnectionstring if external SQL
 objectAlias: sapassword #-OR- dbconnectionstring if external SQL
 objectType: secret
 objectVersion: ""
 tenantId: "<REPLACE>"
 secretObjects:
 - secretName: "bitwarden-secret"
 type: Opaque
 data:
 - objectName: installationid
 key: globalSettings__installation__id
 - objectName: installationkey
 key: globalSettings__installation__key
 key: globalSettings__mail__smtp__username
 - objectName: smtppassword
 key: globalSettings__mail__smtp__password
 - objectName: yubicoclientid
 key: globalSettings__yubico__clientId
 - objectName: yubicokey
 key: globalSettings__yubico__key
 - objectName: hibpapikey
 key: globalSettings__hibpApiKey
 - objectName: sapassword #-OR- dbconnectionstring if external SQL
 key: SA_PASSWORD #-OR- globalSettings__sqlServer__connectionString if external SQL
EOF
```
3. Use the following commands to set the required secrets values in Key Vault:

> [!WARNING] Insecure way of setting a secret
> This example will record commands to your shell history. Other methods may be considered to securely set a secret.

```bash
kvname=<REPLACE>
az keyvault secret set --name installationid --vault-name $kvname --value <REPLACE>
az keyvault secret set --name installationkey --vault-name $kvname --value <REPLACE>
az keyvault secret set --name smtpusername --vault-name $kvname --value <REPLACE>
az keyvault secret set --name smtppassword --vault-name $kvname --value <REPLACE>
az keyvault secret set --name yubicoclientid --vault-name $kvname --value <REPLACE>
az keyvault secret set --name yubicokey --vault-name $kvname --value <REPLACE>
az keyvault secret set --name hibpapikey --vault-name $kvname --value <REPLACE>
az keyvault secret set --name sapassword --vault-name $kvname --value <REPLACE>
# - OR -
# az keyvault secret set --name dbconnectionstring --vault-name $kvname --value <REPLACE>
```
4. In your `my-values.yaml` file, set the following values:

 - `secrets.secretName`: Set this value to the `secretName` defined in your SecretProviderClass.
 - `secrets.secretProviderClass`: Set this value to the `metadata.name` defined in your SecretProviderClass.
