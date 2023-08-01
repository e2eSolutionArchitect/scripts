
- Find the leader node of a cluster
```
curl http://127.0.0.1:8200/v1/sys/leader | jq
```

- Command to use easily re-encrypt the original data with the new version of the key. This operation does not reveal the plaintext data. Vault will decrypt the value using the appropriate key in the keyring and then encrypt the resulting plaintext with the newest key in the keyring
```
vault write transit/rewrap/<key-name> ciphertext=<old-data>
```

- Delete all versions and metadata for the key permanently. Command would permanently delete the path from Vault
```
vault kv metadata delete kv/applications/app01
```

- Permanently delete the current version of the secret. Not all version
```
vault kv destroy kv/applications/app01
```

- Soft delete the current version of the secret.
```
vault kv delete kv/applications/app01
```

Admin never sees all unseal  keys and can not unseal the vault by themselves. each individual user can only decrypt their own unseal key using their PGP keys
```
vault operator init -key-shares=3 -key-threshold=2 -pgp-keys="keybase:user1,keybase:user2,keybase:user3"
```
