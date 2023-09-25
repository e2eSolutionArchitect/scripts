

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

Invalidate a credential
```
vault lease revoke aws/creds/....
```

Steps to encrypt
```
vendor secrets enable transit
vault write -f transit/keys/myencrpkey
base64 <<< "my confidential text"

vault write transit/encrypt/myencrpkey plaintext="dfgdJJDfg#$%#FDgaGFzaGljbZFDgd#$%#$DFGmllZA=="
```

perform API call to read secrets for a particular namespace 'integration'
```
curl \
--header "X-Vault-Token:s.lzrmRe5Y3LMcDRmOttEjWoag" \
--header "X-Vault-Namespace: integration" \
--request GET \
https://vault.example.com:8200/v1/secret/data/my-secret

```
