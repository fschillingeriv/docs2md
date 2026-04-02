---
URL: https://bitwarden.com/help/self-host-bitwarden/
---

# Self-host Bitwarden

Before reviewing the deployment methods, it's important to align with the key stakeholders required for self-hosting Bitwarden. Review and complete the following document with your team before continuing:

- [Self-host Checklist](https://bitwarden.com/help/self-host-checklist/)

## Cloud deployment

Bitwarden provides Cloud-hosted services via a multi-tenant SaaS model to provide an easy-to-use and simple to maintain platform to increase security. When considering hosting options, the following table is provided to compare cloud-hosting Bitwarden to the self-hosting options described further in the document.

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| IT professionals, system administrators | Minimal | Minimal |

## Self-host deployment

For some customers, preference, regulatory and compliance needs, or security policies require that platforms like Bitwarden be deployed in-house instead of using a cloud-hosted model. 

Bitwarden publishes Docker containers built from [source code](https://bitwarden.com/help/is-bitwarden-audited/#open-source-codebase/) and hosted on GitHub Container Registry (GHCR) to allow for this deployment model. Docker containers can be deployed and managed on multiple different platforms. **This document outlines the supported options for self-hosting Bitwarden in your environment**.

> [!TIP] Self-hosting for Enterprise
> Bitwarden's Enterprise plan includes self-hosting for no additional cost.

Customers wanting to self-host a Bitwarden server for their organization or personal use have a variety of deployment options including:

- The server and infrastructure Bitwarden is deployed on.
- The database used by the server.
- The certificate used by the server.

### Linux deployment

#### Linux standard deployment

Deploy Bitwarden to a Linux server using a provided Bash setup script to automate Bitwarden container deployment and maintenance. Suitable for those with experience in Linux systems and command-line operations. Provides flexibility and control over the deployment environment. [Get started](https://bitwarden.com/help/install-on-premise-linux/).

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| IT professionals, system administrators | Intermediate to advanced | Linux command-line, server management, SQL Ops administration |

#### Linux manual deployment

Deploy Bitwarden to a Linux server by manually configuring and building containers and the runtime environment from downloadable installation artifacts. Suitable for integrating into existing Docker container management and processes, but requires additional manual steps for maintenance and upgrades. [Get started](https://bitwarden.com/help/install-on-premise-manual/).

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| System administrators with existing Docker management experience | Advanced | Linux command-line, server maintenance, container management using Docker |

#### Linux offline deployment

Deploy Bitwarden to an offline or air-gapped Linux server environment by configuring containers and the runtime environment from downloadable installation artifacts. Suitable for integrating into existing self-hosted Docker repositories, and requires additional manual steps for maintenance and upgrades. [Get started](https://bitwarden.com/help/install-and-deploy-offline/).

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| Network and system administrators with existing Docker management experience | Advanced | Linux command-line, server maintenance, container management using Docker, network design and setup |

### Windows deployment

#### Windows standard deployment

Deploy Bitwarden to a Windows server via Docker Desktop using a provided Powershell setup script. Suitable for users comfortable with Windows Server environments. Requires knowledge of Windows-specific installation and configuration processes. [Get started](https://bitwarden.com/help/install-on-premise-windows/).

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| IT professionals, system administrators | Intermediate | Windows Server management, PowerShell |

#### Windows offline deployment

Deploy Bitwarden to an offline or air-gapped Windows server environment by configuring containers and the runtime environment from downloadable installation artifacts. Suitable for integrating into existing self-hosted Docker repositories, and requires additional manual steps for maintenance and upgrades. [Get started](https://bitwarden.com/help/install-and-deploy-offline-windows/).

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| Network and system administrators with existing Docker management experience | Advanced | Windows server management, Powershell, network design and setup |

### Bitwarden Lite

Deploy Bitwarden as a single docker container. Suitable for personal users, home labs, or lightweight sharing. [Get started](https://bitwarden.com/help/install-and-deploy-lite/).

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| Prosumers | Intermediate | Linux command-line, container management using Docker |

> [!TIP] Transitioning from Unified to Lite.
> In December, 2025 Bitwarden Unified exited beta and was renamed Bitwarden lite. If you participated in the beta, make sure that you use the new image name (`ghcr.io/bitwarden/lite`) when updating to the latest version.

### Kubernetes & Helm deployments

Deploy Bitwarden in different Kubernetes environments using a Helm chart. Designed for highly-available and containerized deployments and suitable for cloud-native and large-scale deployments on shared or dedicated clusters. Compatible with, but requires setup knowledge of, many Kubernetes primitives like storage and Ingress configuration.

| Intended audience | Required skill level | Expected knowledge |
|------|------|------|
| DevOps engineers, cloud administrators | Advanced | Kubernetes orchestration, Helm charts |

Get started with:

- [Azure AKS Deployments](https://bitwarden.com/help/azure-aks-deployment/)
- [OpenShift Deployments](https://bitwarden.com/help/openshift-deployment/)
- [AWS EKS Deployments](https://bitwarden.com/help/aws-eks-deployment/)

## Further options

### Database options

All Bitwarden self-hosted server deployments, except for [unified](https://bitwarden.com/help/install-and-deploy-lite/), ship with an MSSQL Express image by default, however customers may connect to an external MSSQL server or cluster of version 2019 or higher. [Learn more](https://bitwarden.com/help/database-options/).

### Certificate options

Customers self-hosting Bitwarden may deploy Bitwarden with one of several different SSL certificate options. [Learn more](https://bitwarden.com/help/certificates/).

## Next steps

- Deploy Bitwarden using one of the **Install & Deploy Guides** linked above.
- If you're hosting Bitwarden for an organization, use [this guide](https://bitwarden.com/help/self-host-an-organization/) to get it ready for rollout to users.
- Complete the [Bitwarden Self-host Checklist](https://bitwarden.com/help/self-host-checklist/) with your team. This document will help ensure you have alignment across your stakeholders involved in the deployment, and can be downloaded as a PDF.
