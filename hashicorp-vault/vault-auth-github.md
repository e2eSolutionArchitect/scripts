
Create Authentication method for GitHub
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
