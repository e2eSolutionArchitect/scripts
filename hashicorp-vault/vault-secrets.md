

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
vault kv metadata delete - permanently deletes the secret
vault kv delete - soft delete current version
vault kv destroy - permanently deletes current version of the secret
```
