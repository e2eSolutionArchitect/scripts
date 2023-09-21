

Secrets list in detail
```
vault secrets list -detailed
```

enable versioning
```
vault kv enable-versioning
```

Delete secret engine
```
vault kv metadata delete - permanently deletes the secret with all versions and metadata
vault kv delete - soft delete current version
vault kv destroy - permanently deletes current version of the secret
```

revoke all leases associated with the secret engine mounted at /aws
```
vault lease revoke -prefix aws/
```

Transit secret engine

```
curl \
--header "X-Vault-Token: hvs.########" \
--request POST \
--data @data.json \
https://prod-vault.abc.com:8200/v1/transit/encrypt/customer-data
```
data.json will contain plaintext customer data to be encrypted


Force to remove the secret
```
vault lease revoke -force -prefix <lease-path>
```
