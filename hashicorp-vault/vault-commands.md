
HashiCorp Vault [installation instruction](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install)

Set environment variables
```
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN="hvs.6j4cuewowBGit65rheNoceI7"
```
Vault & version status

```
vault -version
vault status
```
Get the list of secret engine paths
```
vault secrets list
```

Enable AWS secret engine path
```
vault secrets enable -path=<path> <name-of-secret-engine>
vault secrets enable -path=myaws aws
```

Disable secret engine path
```
vault secrets disable <path-name>
vault secrets disable myaws
```
