
Create Authentication method for GitHub
```
vault auth list
vault auth enable github
```

Link GitHub Org to Vault
```
vault write auth/github/config organization=<github-org-name>
```
