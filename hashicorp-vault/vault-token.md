
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

Revoke root token
```
vault token revoke <root-token>
vault token revoke hvs.hisdf776234kSDFSFhiendsfsdfjh
```

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
