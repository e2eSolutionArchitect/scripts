
```
vault token create -policy=dev -use-limit=5
```

Regenerate vault token

```
vault token create
```

Login with Root Token. Use your root token as password
```
vault login
```

Generate Root Token

```
vault token create - when using a valid root token
vault operator init - when first time initializing vault

3rdly when generating a root token using a quorum of recovery keys when using vault auto seal

```

Revoke root token
```
vault token revoke <root-token>
vault token revoke hvs.hisdf776234kSDFSFhiendsfsdfjh
```

After authenticating, a client is issued a service token which is associated with a policy. That token is used to make all subsequent requests to Vault.

Login to Vault using GitHub token
```
vault login -method=github
```

Token renew [refer](https://developer.hashicorp.com/vault/docs/commands/token/renew#token-renew)
```
# Renew a token (this uses the /auth/token/renew endpoint and permission):
vault token renew <token_id>
vault token renew 96ddf4bc-d217-f3ba-f9bd-017055595017

vault token renew -increment=30m <token_id>
vault token renew -increment=30m 96ddf4bc-d217-f3ba-f9bd-017055595017

```

Use the token to access vault
```
vault token create -policy=mypolicy

Key                  Value
---                  -----
token                hvs.###########
token_accessor       #############
token_duration       24h
token_renewable      true
token_policies       ["e2esa" "default"]
identity_policies    []
policies             ["e2esa" "default"]


vault login hvc.########
or
vault login -method=token hvc.########

```

Revoke all leases associated with a role 'myrole'

```
vault lease revoke -prefix database/creds/myrole
```

Vault token look up shows associated policy with vault
```
vault token lookup s.DjWW0########
You can also use -accessor flag if you only know the accessor and not the token.
```

vault operator diagnose  is a new command in Vault 1.8 that allows you to troubleshoot a Vault node where the Vault service will not start
vault token capabilities will list the capabilities on a certain path 
vault policy list will list the current policies on the Vault node/cluster
