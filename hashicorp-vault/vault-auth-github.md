
Create an Authentication method for GitHub
```
vault auth list
vault auth enable github
```

Link GitHub Org to Vault
Write Config for Org
```
vault write auth/github/config organization=<github-org-name>
```

Write config for Teams. web-team, app-team assumed created in github org already
```
vault write auth/github/map/teams/my-team values = web-team, app-team
```

Now login using Github method. Use Github Token as password
```
vault login -method=github

```

Create Github Token from Github
- Github > Profile > Developer Settings > Personal Access Token
- Make sure to add 'read-org' permission to the PAT (Personal Access Token)


How to remove the authentication method? such as Github

```
vault token revoke -mode path auth/github
# Also disable the auth method
vault auth disable github
```
