start vault server
```
vault server -config = config.hcl # for production/server model 
```
For the production server please make Vault a service in Linux system

Set environment variables
```
export VAULT_ADDR='http://<server-public-ip>:8200'
```

Initialize Vault
```
vault operator init
```
