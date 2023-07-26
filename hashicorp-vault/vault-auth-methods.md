

```
vault auth list
vault auth enable approle
```

After enabling auth method we have to assign it to the policy

```
vault write auth/approle/role/my-role \
  secret_id_ttl=10m \
  token_num_uses=10 \
  token_ttl=20m \
  token_max_ttl=30m \
  secret_id_num_uses=40 \
  token_policies=,y-policy
```
