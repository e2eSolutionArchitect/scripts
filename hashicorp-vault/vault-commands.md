
Find the leader node of a cluster
```
curl http://127.0.0.1:8200/v1/sys/leader | jq
```

Command to use easily re-encrypt the original data with the new version of the key. This operation does not reveal the plaintext data. Vault will decrypt the value using the appropriate key in the keyring and then encrypt the resulting plaintext with the newest key in the keyring
```
vault write transit/rewrap/<key-name> ciphertext=<old-data>
```
