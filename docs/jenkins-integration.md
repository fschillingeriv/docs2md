---
URL: https://bitwarden.com/help/jenkins-integration/
---

# Jenkins Integration

Jenkins is an open source automation server that automates building, testing, and deploying software. Use the Bitwarden Secrets Manager CLI to inject secrets into Jenkins CI/CD Pipelines.

## Save an access token

To get started, create a token that will be used to authenticate with the Bitwarden Secrets Manager and retrieve [secrets](https://bitwarden.com/help/secrets/). To save an [access token](https://bitwarden.com/help/access-tokens/) as a Jenkins credential:

1. In Jenkins, navigate to the **Settings  → Credentials** page.

![Setting credentials](https://bitwarden.com/assets/7BNSdUFjmu3LaVcywyKaOd/be6b83e5d2648bc3a26cabe7febbd90c/Setting_credentials.png)
*Setting credentials*
2. Select the desired credential store.
3. Select **Add Credentials**.
4. Click the **Kind** drop down menu and select **Secret text**.
5. Give the credential an appropriate name. Next, we will prepare the `bitwarden-access-token`.
6. In a new tab, open the Secrets Manager web app and [create an access token](https://bitwarden.com/help/access-tokens/).

![Create access token](https://bitwarden.com/assets/0X3dgYBEQpW9EOGWIHiUV/22aef7ea682198c0f42630cf7637bf63/new_access_token.png)
*Create access token*
7. Return to Jenkins and paste the newly-created access token into the **Secret** field.
8. Once complete, select **Create**.

![Jenkins credential](https://bitwarden.com/assets/4HjU45wJZMlhuyhTLWEwpB/0bfb7ee75ed53c427927b5c99e45a6e4/2026-02-06_18-10-34.png)
*Jenkins credential*

## Add to your Jenkins Pipeline

Next, a Jenkins Pipeline needs to be created. The following section features an example Pipeline. 

1. Create a new Jenkins Pipeline by selecting **New Item** on the left-hand navigation.
2. Enter a name for the new item. Next, select the **Pipeline** item type and then **OK** when complete. 

![New Pipeline](https://bitwarden.com/assets/6FP4AFLnuLT7pamWPhhF56/034dc91dfb4632155f74f0daf7575074/2026-02-09_17-16-10.png)
*New Pipeline*
3. On the following screen, configure your desired settings and triggers. In the Pipeline section, include the following contents:

```java
pipeline {
 agent any

 stages {
 stage('Build Rust Project with Secrets from Bitwarden') {
 steps {
 withCredentials([string(credentialsId: 'bitwarden-access-token',
 variable: 'BWS_ACCESS_TOKEN')]) {
 sh '''
 export PATH=$PATH:/usr/local/bin # ensure bws is in PATH
 bws run -- <command needing secrets here>
 '''
 }
 }
 }
 }
}
```

> [!NOTE] Replace command in Jenkins Pipeline
> Replace `<command_needing_secrets_here>` with the command that requires access to secrets manager.

## Run the CI/CD Pipeline

On the left, select **Build Now → Pipelines** and select **Run Pipeline** located on the top-right of the page. Select **Run Pipeline**on the page to run the newly-created Pipeline.
