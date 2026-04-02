---
URL: https://bitwarden.com/help/add-rawmanifest-files/
---

# Add rawManifest Files

The Bitwarden self-host Helm Chart allows you to include other Kubernetes manifest files either pre- or post-install. To do this, update the `rawManifests` section of the chart. The article contains some examples of how you might use rawManifests:

## Validate server certificate

For example, to configure Bitwarden to validate your MSSQL database server's certificate:

> [!NOTE] my-values.yaml value required
> In this example, you would also need to set the value `caCertificate.enabled: true` in your `my-values.yaml` file.

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

## Traefik IngressRoute

For example, to install Traefik's IngressRoute as an alternative to Kubernetes' Ingress controller, add the following:

> [!NOTE] Add manifest example
> In this example, you would also need to disable the ingress controller at `general.ingress.enabled`: within your `my-values.yaml` file.

```bash
rawManifests:
 preInstall: []
 postInstall:
 - apiVersion: traefik.containo.us/v1alpha1
 kind: Middleware
 metadata:
 name: "bitwarden-self-host-middleware-stripprefix"
 spec:
 stripPrefix:
 prefixes:
 - /api
 - /attachments
 - /icons
 - /notifications
 - /events
 - /scim
 ##### NOTE: Admin, Identity, and SSO will not function correctly with path strip middleware
 - apiVersion: traefik.containo.us/v1alpha1
 kind: IngressRoute
 metadata:
 name: "bitwarden-self-host-ingress"
 spec:
 entryPoints:
 - websecure
 routes:
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/`)
 services:
 - kind: Service
 name: bitwarden-self-host-web
 passHostHeader: true
 port: 5000
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/api/`)
 services:
 - kind: Service
 name: bitwarden-self-host-api
 port: 5000
 middlewares:
 - name: "bitwarden-self-host-middleware-stripprefix"
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/attachments/`)
 services:
 - kind: Service
 name: bitwarden-self-host-attachments
 port: 5000
 middlewares:
 - name: "bitwarden-self-host-middleware-stripprefix"
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/icons/`)
 services:
 - kind: Service
 name: bitwarden-self-host-icons
 port: 5000
 middlewares:
 - name: "bitwarden-self-host-middleware-stripprefix"
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/notifications/`)
 services:
 - kind: Service
 name: bitwarden-self-host-notifications
 port: 5000
 middlewares:
 - name: "bitwarden-self-host-middleware-stripprefix"
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/events/`)
 services:
 - kind: Service
 name: bitwarden-self-host-events
 port: 5000
 middlewares:
 - name: "bitwarden-self-host-middleware-stripprefix"
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/scim/`)
 services:
 - kind: Service
 name: bitwarden-self-host-scim
 port: 5000
 middlewares:
 - name: "bitwarden-self-host-middleware-stripprefix"
 ##### NOTE: SSO will not function correctly with path strip middleware
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/sso/`)
 services:
 - kind: Service
 name: bitwarden-self-host-sso
 port: 5000
 ##### NOTE: Identity will not function correctly with path strip middleware
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/identity/`)
 services:
 - kind: Service
 name: bitwarden-self-host-identity
 port: 5000
 ##### NOTE: Admin will not function correctly with path strip middleware
 - kind: Rule
 match: Host(`REPLACEME.COM`) && PathPrefix(`/admin`)
 services:
 - kind: Service
 name: bitwarden-self-host-admin
 port: 5000
 tls:
 certResolver: letsencrypt
```

##
