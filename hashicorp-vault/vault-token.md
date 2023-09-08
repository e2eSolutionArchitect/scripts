
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
