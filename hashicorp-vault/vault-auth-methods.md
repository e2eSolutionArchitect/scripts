

```
vault auth list
vault auth enable <auth-method-name>
vault auth enable approle
```

After enabling auth method we have to assign it to the policy

## Associate auth method with policy

```
vault write auth/approle/role/my-role \
  secret_id_ttl=10m \
  token_num_uses=10 \
  token_ttl=20m \
  token_max_ttl=30m \
  secret_id_num_uses=40 \
  token_policies=my-policy
```
'my-policy' is already created policy and 'approle' is the auth method already created


```
export ROLE_ID="$(vault read -field=role_id auth/approle/role/my-role/role-id)"
export SECRET_ID="$(vault write -f -field=secret_id auth/approle/role/my-role/secret-id)"
```

Write config
```
vault write auth/approle/login role_id="$ROLE_ID" secret_id="$SECRET_ID"

```
