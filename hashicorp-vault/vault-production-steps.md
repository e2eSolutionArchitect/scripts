start vault server
```
vault server -config = config.hcl # for production/server model 
```
For production server please make vault as a service

Set environment variables
```
export VAULT_ADDR='http://<server-public-ip>:8200'
export VAULT_TOKEN="hvs.6j4cuewowBGit65rheNoceI7"
```



Insitialize Vault
```
vault operator init
```
