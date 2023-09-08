

- HashiCorp Vault [installation instruction](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-install) in short [check it](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/install-vault.md)
- Types and sources for Vault [installation](https://developer.hashicorp.com/vault/docs/install)
- Vault [tutorials](https://developer.hashicorp.com/vault/tutorials)



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

Set Root config for AWS
```
vault write aws/config/root access_key######## secret_key=######## region=us-east-1
```

Setup a role for which we need dynamic secrets
```
vault write aws/roles/myrole credential_type=iam_user policy_document=-<<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "ec2:*"
             ],
            "Resource": {
                "*"
            },
           
        }
    ]
}
EOF
```

Generate Dynamic secret access_ket, secret_key via the role created above
```
vault read aws/creds myrole
```


Create secrets
```
vault kv put -mount=secret creds password="my-super-secret-passwprd123"
```

- [Policy](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/vault-policy.md)

Regenerate vault token

```
vault token create
```

Login with Root Token. Use your root token as password
```
vault login
```

Revoke root token
```
vault token revoke <root-token>
vault token revoke hvs.hisdf776234kSDFSFhiendsfsdfjh
```

Login to Vault using GitHub token
```
vault login -method=github
```

- [Generate Dynamic Secrets for AWS](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/generating-dynamic-secrets-for-aws.md)
