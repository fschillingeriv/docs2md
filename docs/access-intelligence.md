---
URL: https://bitwarden.com/help/access-intelligence/
---

# Access Intelligence

Enterprise organizations can use **Access Intelligence** to identify and prioritize applications with [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/) credentials that are stored within your Bitwarden organization by its members. Using this report, select [critical applications](https://bitwarden.com/help/access-intelligence/#marking-critical-applications/) and notify organization members that they [need to take action on at-risk passwords](https://bitwarden.com/help/change-at-risk-passwords/).

Access Intelligence provides easy co-located visibility for admins into which credentials are [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/), it does not grant administrators direct access to passwords they don't otherwise have access to.

> [!NOTE] Access Intelligence & individual vaults
> Access Intelligence does not allow admin visibility into items for which the organization is not the owner. To ensure full visibility into all potential at-risk credentials, Bitwarden recommends activating the [Centralize organization ownership](https://bitwarden.com/help/policies/#centralize-organization-ownership/) policy so that all data is owned by the organization.

## Run the report

As the application landscape evolves and changes within your organization, the contents of this report will change. It is critically important that Access Intelligence be treated as a continuous exercise. To update the report, take note of the **Data last updated** timestamp and select the **Run report** button.

![Run the Access Intelligence report](https://bitwarden.com/assets/6ooDvXBHM0ehpTD2XWpQGK/88c0af7c5edd5b30b8037f49baf8ac88/2026-03-20_12-07-24.png)
*Run the Access Intelligence report*

## Activity

The **Activity** tab of the Access Intelligence report provides a summary of crucial datapoints and tasks. While the Activity tab provides this information at-a-glance, you should familiarize yourself with the **All applications** and **Critical applications** tab to best understand what's surfaced here:

![Access Intelligence, Activity tab](https://bitwarden.com/assets/4ors4hBI2rwbW0zvjb2W0U/fb9e9ce8a0c636ea114abe80e838d02d/2026-03-20_12-07-50.png)
*Access Intelligence, Activity tab*

- **Password change progress**: Percentage completion of [dispatched password change requests](https://bitwarden.com/help/access-intelligence/#requesting-password-changes/).
- **At-risk members**: Number of members with access to [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/) items for [critical](https://bitwarden.com/help/access-intelligence/#marking-critical-applications/) applications.
- **Critical applications**: Proportion of [critical](https://bitwarden.com/help/access-intelligence/#marking-critical-applications/) applications that are currently [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/).
- **Applications needing review**: Number of new applications added by members since the [report was last run](https://bitwarden.com/help/access-intelligence/#run-the-report/).

### Determining risk

A password is determined to be **at-risk** if it is weak, exposed, or re-used within the organization. This analysis is done with the same tools used in the [Weak passwords report](https://bitwarden.com/help/reports/#weak-passwords-report/), [Exposed passwords report](https://bitwarden.com/help/reports/#exposed-passwords-report/), and [Reused passwords report](https://bitwarden.com/help/reports/#reused-passwords-report/). As is the case for running reports manually, the analysis done by Access Intelligence is done locally to preserve zero-knowledge and protect your data integrity and anonymity.

## All applications

The Access Intelligence report lists all applications saved as items within your Bitwarden organization. Each application represents the set of all items with a URI that matches a given web service (for example, the "Atlassian" application may contain 26 "Total passwords", indicating there are 26 items that contain credentials for logging into Atlassian) and contains:

| Column | Description |
|------|------|
| **Application** | The name of the application that is [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/). |
| **At-risk passwords** | The number of passwords associated with the application that are [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/). |
| **Total passwords** | The total number of passwords associated with the application. |
| **At-risk members** | The number of members who have access to the [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/) passwords associated with the application. |
| **Total members** | The total number of members who have access to the application. |

> [!TIP] Access Intelligence for Shadow IT & SSO gap detection.
> By surfacing a list of all applications for which organization members have credentials, Access Intelligence can also help administrators detect the use of unsanctioned applications as well as those which could be migrated to single sign-on (SSO) authentication through an IdP.

### Marking critical applications

> [!TIP] Why mark applications critical?
> Marking an application **critical** is an important tool for ensuring organization members are encouraged to take quick action on the applications that matter most.
> 
> One important function of Access Intelligence is the ability to dispatch notifications to members informing them they need to take action on a critical [at-risk](https://bitwarden.com/help/access-intelligence/#determining-risk/) password. Dispatching these notifications in targeted waves will help prevent member alert fatigue and resultant delays in remediation.

Applications marked **critical** are those which will have notifications dispatched to organization members informing them that they [need to take action on at-risk passwords](https://bitwarden.com/help/change-at-risk-passwords/). To mark applications critical, toggle one or more checkboxes and select select the **Mark app as critical** button:

![Mark a critical application](https://bitwarden.com/assets/77hdEeJiKWpHd8BoHYbnCx/e691c69651cace09523a8655e31e3988/2026-03-20_12-09-56.png)
*Mark a critical application*

## Critical applications

Using Access Intelligence, administrators can preemptively assess which applications they want prioritized for members to take action on. The report can be narrowed down from **All applications** for which there are credentials stored within your organization to only those you select as the current **Critical applications** to take action on.

### Requesting password changes

Requesting password changes will dispatch notifications to organization members with access to critical applications informing them that they [need to take action on at-risk passwords](https://bitwarden.com/help/change-at-risk-passwords/). Members will receive notifications both in their email inbox and as a banner in a Bitwarden browser extensions they're logged in to.

> [!TIP] Best practices before sending Access Intelligence notifications.
> Before dispatching your first password change requests, or as part of employee Bitwarden training, we recommend:
> 
> - Informing members that these emails are legitimate and should not be ignored.
> - Providing members with instructions for [how to take action on password change requests](https://bitwarden.com/help/change-at-risk-passwords/).

To request password changes on all applications currently marked [critical](https://bitwarden.com/help/access-intelligence/#marking-critical-applications/), navigate to the **Critical applications** view and select **Request password changes**:

![Request a password change](https://bitwarden.com/assets/6wQ3EUzMFkzRIkA2FHgnlY/99836bd7d0bd053e1c2eb6878175685c/2026-03-20_12-07-242.png)
*Request a password change*
