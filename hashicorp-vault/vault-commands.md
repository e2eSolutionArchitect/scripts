
Get list of secret engine paths
```
vault secrets list
```

Enable AWS secret engine path
```
vault secrets enable -path=<path> <name-of-secret-engine>
vault secrets enable -path=myaws aws
```

Disable secret engine path
```
vault secrets disable <path-name>
vault secrets disable myaws
```
