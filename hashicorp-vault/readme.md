

- HashiCorp Vault [installation instruction](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install) in short [check it](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/install-vault.md)
- Types and sources for Vault [installation](https://developer.hashicorp.com/vault/docs/install)
- Vault [tutorials](https://developer.hashicorp.com/vault/tutorials)

- Vault [API docs](https://developer.hashicorp.com/vault/api-docs/system/leader)

Set environment variables
```
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN="hvs.6j4cuewowBGit65rheNoceI7" # root token
```
Vault version & status

```
vault -version
vault status
```

start vault server
```
vault server -dev
vault server -config = config.hcl # for production/server mode 
```
For the production server please make Vault as a service

Enable a new secret engine path
``
vault enable mypath
``

Write Key Value
```
vault kv put <path> <key>=<value>
vault kv put mypath/hello1 key1=value1
```

Note: Once a new 'path' is mentioned the 'path' should be enabled for a secret engine. please check how to enable in the section "Enable AWS secret engine path" below. 

Get key value from path
```
vault kv get <path>
vault kv get mypath/hello1

Read in JSON format
vault kv get -format=json my/path
```

Delete
```
vault kv delete <path>
vault kv delete mypath/hello1
```

Get the list of secret engine paths
```
vault secrets list
```

Enable AWS secret engine path
```
vault secrets enable -path=<path> <name-of-secret-engine>
vault secrets enable -path=aws aws
```

Disable secret engine path
```
vault secrets disable <path-name>
vault secrets disable mypath/hello1
```

Command to instruct the active node to gracefully stand down
```
vault operator step-down
```

- [Generate Dynamic Secrets for AWS](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/generating-dynamic-secrets-for-aws.md)
- [Policy](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/vault-policy.md)

Apply policy to write secrets
```
vault kv put -mount=secret creds password="my-super-secret-passwprd123"
```

Notes:
- After initializing Vault or restarting the Vault service, each individual node in the cluster needs to be unsealed.

Rekey operation using the vault operator rekey command creates new unseal/recovery keys as well as a new master key
```
vault operator rekey
```
