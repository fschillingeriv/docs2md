---
URL: https://bitwarden.com/help/bitwarden-software-release-support/
---

# Software Release Support

Bitwarden maintains software versions for the Bitwarden server, Bitwarden clients, and other supported integrations and modules. This document describes software lifecycle policies followed by Bitwarden, this information will help you prepare for updates appropriate for your organization.

As a security company building a globally trusted product, Bitwarden maintains up-to-date and relevant software versions for all of our user base, making them widely available and easy to access.

At the same time, we recognize there needs to be a balance between frequent updates and release lifespan. We also recognize there needs to be a balance between pushing forward with new features on newer systems and relinquishing support for older systems. (“Systems” in this case represents devices, operating systems, and software applications and frameworks.)

## Bitwarden software support

> [!NOTE] Definition of "major version"
> A "major version", as described in this document, is indicated by the second number in the version format used for Bitwarden clients and servers (e.g. 2025.**`6`**.0 or 2025.**`7`**.1).

The following sections describe support policies for software developed by Bitwarden:

### Bitwarden cloud server

The Bitwarden cloud servers are operated and maintained directly by Bitwarden. We update the Bitwarden cloud servers regularly and post updates at [status.bitwarden.com](https://status.bitwarden.com/).

### Bitwarden self-hosted server

For self-hosted implementations with applicable subscription plans, Bitwarden servers receive ongoing updates:

- At a given time, Bitwarden maintains the current major server version and the previous 2 major server versions.
- Each server version is compatible with clients of the same major version, the previous 2 major client versions, and the subsequent 2 major client versions.

> [!NOTE] Client compatibility tip
> Self-hosted users are expected to keep their server up-to-date to stay current on Bitwarden features and support, and remain compatible with the latest released clients. Self-hosted instances that do not update client and server versions in accordance with the Bitwarden version support policy risk introducing a client change that is incompatible with their server.

### Bitwarden clients

For Bitwarden client applications:

- At a given time, Bitwarden maintains the current major client version and the previous 2 major client versions.
- Each client version is compatible with servers of the same major version, the previous 2 major server versions, and the subsequent 2 major server versions.

[Learn how to check your client version](https://bitwarden.com/help/versioning/#client-version/).

### Bitwarden API

The Bitwarden API release cycle and duration aligns with Bitwarden servers. As a practice, we aim to provide backwards compatibility to the API indefinitely through semantic versioning. However, if we add enhancements that make it difficult or impossible to maintain backwards compatibility to all prior versions, we will indicate that by incrementing the major version number.

## Platform software support

The following sections describe support policies for software on which Bitwarden is installed or used:

### Platforms for Bitwarden clients

For all underlying platforms on which Bitwarden clients applications are installed or used, for example desktop or mobile operating systems and web browser versions, Bitwarden aims to support those versions which are currently supported by the vendor.

### Platforms for self-hosted Bitwarden servers

Unless otherwise specified in the System Requirements, self-hosted installations should be maintained on up-to-date operating systems and compute platforms under active support from their vendor(s).
