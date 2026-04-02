---
URL: https://bitwarden.com/help/import-secrets-data/
---

# Import Data

Import data to Secrets Manager for easy migration from another organization or secrets management solution. Secrets Manager supports direct import of both [secrets](https://bitwarden.com/help/secrets/) and [projects](https://bitwarden.com/help/projects/). [Machine accounts](https://bitwarden.com/help/machine-accounts/) and [access tokens](https://bitwarden.com/help/access-tokens/) cannot be imported. 

[![Vimeo Video](https://vumbnail.com/854758635.jpg)](https://vimeo.com/854758635)
*[Watch on Vimeo](https://vimeo.com/854758635)*

**Video Chapters:**
Learn more about secrets [here](https://bitwarden.com/help/secrets/).

## Condition an import file

Secrets Manager currently supports direct import of secrets and project as a `.json` file. Your import file should be conditioned according to the following schema and rules:

- Even if you're only importing secrets, you must include a `"projects" :` object containing an empty array, for example:

```
{
 "projects": [],
 "secrets": [
 {
 "key": "Secret for Import 1",
 "value": "this-is-my-value",
 "note": "These are some notes.",
 "id": "00000000-0000-0000-0000-000000000001",
 "projectIds": []
 },
 {
 "key": "Secret for Import 2",
 "value": "this-is-my-value",
 "note": "These are some notes.",
 "id": "00000000-0000-0000-0000-000000000002",
 "projectIds": []
 }
 ]
}
```
- For now, each secret can only be associated with a single project.
- All objects must have a non-empty `"id": ""` attribute that matches an expected format. We recommend using `"00000000-0000-0000-0000-000000000001"` for the first object and incrementing with each subsequent object. On import, new randomly generated identifiers will be generated for each object:

```
{
 "projects": [
 {
 "id": "00000000-0000-0000-0000-000000000001",
 "name": "New Project"
 },
 {
 "id": "00000000-0000-0000-0000-000000000002",
 "name": "Second New Project"
 }
 ],
 "secrets": [
 {
 "key": "Secret for Import",
 "value": "this-is-my-value",
 "note": "These are some notes.",
 "id": "00000000-0000-0000-0000-000000000003",
 "projectIds": []
 },
 {
 "key": "Second Secret for Import 2",
 "value": "this-is-my-value",
 "note": "These are some notes.",
 "id": "00000000-0000-0000-0000-000000000004",
 "projectIds": []
 }
 ]
}
```
- You can use the `"projectIds": ""` attributes to associate imported secrets with a newly imported project:

```
{
 "projects": [
 {
 "id": "00000000-0000-0000-0000-000000000001",
 "name": "New Project"
 }
 ],
 "secrets": [
 {
 "key": "New Secret",
 "value": "this-is-my-value",
 "note": "This secret will go in the new project.",
 "id": "00000000-0000-0000-0000-000000000003",
 "projectIds": [
 "00000000-0000-0000-0000-000000000001"
 ]
 }
 ]
}
```

## Import to Secrets Manager

To import your `.json` file to Secrets Manager:

> [!NOTE] Secrets Import Role
> To import to Secrets Manager, your user account must be an owner or admin within the organization.

1. Select **Settings**→ **Import data** from the left-hand navigation:

![Import data](https://bitwarden.com/assets/1YQuiYqXIuYYG1TpXoSJoU/f76b3ee08dda7b470f96da9ebbe4f9b1/2024-12-03_11-28-29.png)
2. Select **Choose File**and choose a `.json` file for import, or **Copy & paste import contents** into the input box.
3. Select the **Import data** button. When prompted, enter your master password.

> [!WARNING] Secrets import duplicates
> Importing does not check whether objects in the file to import already exist in Secrets Manager. If you import multiple files or import files with objects already in Secrets Manager, **this will create duplicates**.
