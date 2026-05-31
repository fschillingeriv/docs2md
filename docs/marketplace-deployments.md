---
URL: https://bitwarden.com/help/marketplace-deployments/
---

# Marketplace Deployments

This article will walk you through deploying a self-hosted Bitwarden server using a pre-built virtual machine image from the AWS or Azure marketplace. These deployment options are a good fit for organizations that already operate in AWS or Azure and want to keep their Bitwarden server inside the same environment as the rest of their stack:

- [Self-host Bitwarden via the AWS marketplace](https://aws.amazon.com/marketplace/pp/prodview-tuo4cqgcd3f5w)
- [Self-host Bitwarden via the Azure marketplace](https://marketplace.microsoft.com/en-us/product/saas/bitwardeninc.bitwarden-self-host)

These marketplace deployments launch a virtual machine (VM) with the core software requirements for self-hosting Bitwarden and the installation script pre-loaded. Once launched, you can SSH into the VM and start the installation script to complete the setup procedure.

## Before you begin

### Included in the image

Both the AWS AMI and and Azure VM image are pre-loaded with:

- Ubuntu 24.04 LTS
- Docker Engine
- Docker Compose
- Bitwarden installation script

> [!WARNING] OS support for marketplace deployments
> The Bitwarden marketplace images are pre-loaded Ubuntu 24.04 LTS, however **operating system maintenance, patching, and OS-level troubleshooting are not in-scope for Bitwarden customer support**. You are responsible for maintaining the underlying OS, including applying security updates, monitoring, and backups as you would be for any other VM in your environment.

### Prerequisites

Have the following ready:

- An AWS or Azure account with permission to launch a VM from the marketplace.
- An installation ID and key, retrieved from [bitwarden.com/host](https://bitwarden.com/host/).
- A registered domain name with a DNS record pointing to the public IP your VM instance will use.
- An SMTP server or cloud SMTP provider that the VM can reach.
- An SSH key pair that can be used to access the VM.
- (**Optional**) An SSL certificate to apply to the VM. Let's Encrypt can be used once you SSH into the VM to generate and issue a certificate for free.

## Deployment

### AWS

1. Subscribe to the product from the [Bitwarden self-hosted server listing on the AWS marketplace](https://aws.amazon.com/marketplace/pp/prodview-tuo4cqgcd3f5w).
2. Open the launch wizard for the AMI through the AWS console.
3. Configure the AMI. The launch wizard will allow you to specify VPC, subnet, security group and a few other attributes, but make sure to take note of the following:

 - The designated **security group** must open ports 80 and 443.
 - There are many **instance types** to choose from, but a recommendation is provided.
 - A **key pair** can be generated for accessing the VM once it's launched.
4. Launch the instance. Once it reaches a running state, SSH into the VM. The `./bitwarden.sh install` command will automatically be launched to [begin the installation wizard](https://bitwarden.com/help/install-on-premise-linux/#install-bitwarden/).

> [!TIP] Skip some steps for marketplace deployments.
> Because marketplace deployments are pre-packaged with the installation script, you can skip directly to **Step 3** ("Complete the prompts in the installer") in the linked instructions.

### Azure

1. Select **Get it now** from the [Bitwarden self-hosted server listing on the Azure marketplace](https://marketplace.microsoft.com/en-us/product/saas/bitwardeninc.bitwarden-self-host). Azure will require you to enter information about your Azure account, like first and last name, before proceeding.
2. Choose which subscription to associate the VM with and select **Create** to launch the VM creation wizard.
3. Configure the AMI. The creation wizard will allow you to specify a wide variety of attributes, but make sure to take note of the following:

 - The designated **Network** **Security Group** must open ports 80 and 443.
 - There are many VM**sizes** to choose from, but a recommendation is provided.
 - A **key pair** can be generated for accessing the VM once it's launched.
4. Review and create the VM. Once it reaches a running state, SSH into the VM.he `./bitwarden.sh install` command will automatically be launched to [begin the installation wizard](https://bitwarden.com/help/install-on-premise-linux/#install-bitwarden/).

> [!TIP] Skip some steps for marketplace deployments.
> Because marketplace deployments are pre-packaged with the installation script, you can skip directly to **Step 3** ("Complete the prompts in the installer") in the linked instructions.

## Additional information

### Support

Bitwarden customer support covers the Bitwarden server and its configuration. For operating system support, including system maintenance, patching, and OS-level troubleshooting refer to your OS vendor's support infrastructure. For cloud account and platform support, refer to AWS or Azure's support infrastructure.

### Costs

The Bitwarden marketplace images are available at no extra charge through Bitwarden or the AWS and Azure marketplaces. You will be billed:

- By Bitwarden, as normal, for your subscription based on plan and seat count.
- By AWS or Azure, as for any other application, for compute and storage costs.

### Automatic updates

Marketplace deployments are setup by default with a cronjob that automatically applies updates to keep your Bitwarden server current. Updates to the Bitwarden server are applied in place using the [installation script's pre-packaged update commands](https://bitwarden.com/help/updating-on-premise/). 

To prevent downtime in the case of an unexpected update failure, Bitwarden **strongly recommends** that you put in place systems for regularly [backing up server data](https://bitwarden.com/help/backup-on-premise/) and for monitoring server availability.
