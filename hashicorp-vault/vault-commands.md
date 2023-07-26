
- HashiCorp Vault [installation instruction](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install)
- Types and sources for Vault [installation](https://developer.hashicorp.com/vault/docs/install)
- Vault [tutorials](https://developer.hashicorp.com/vault/tutorials)

- 
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

start vault server
```
vault server -dev
vault server -server
```


Get the list of secret engine paths
```
vault secrets list
```
Enable a new secret engine path
``
vault enable mypath
``

Write Key Value
```
vault kv put <path> <key>=<value>
vault kv put mypath/hello1 key1=value1
```

Get key value from path
```
vault kv get <path>
vault kv get mypath/hello1
```

Delete
```
vault kv delete <path>
vault kv delete mypath/hello1
```


Enable AWS secret engine path
```
vault secrets enable -path=<path> <name-of-secret-engine>
vault secrets enable -path=mypath2 aws
```

Disable secret engine path
```
vault secrets disable <path-name>
vault secrets disable mypath/hello1
```

Create secrets
```
vault kv put -mount=secret creds password="my-super-secret-passwprd123"
```

- [Policy](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/vault-policy.md)
- [Generate Dynamic Secrets for AWS](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/generating-dynamic-secrets-for-aws.md)
