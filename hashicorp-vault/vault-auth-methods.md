
'token' is the default auth method in the vault.

Auth methods offers the cababilities to use external authentication service in vault. 

Examples of machine auth methods include AppRole, Cloud-based auth methods, tokens, TLS, Kubernetes, and Radius. Examples of human auth methods include Okta, LDAP, GitHub, OIDC, and userpass.

```
vault auth list
vault auth enable <auth-method-name>
vault auth enable approle
```
Check what version the KV store is using
```
vault secrets list -detailed
```
After enabling auth method we have to assign it to the policy

## Associate auth method with policy

```
vault write auth/approle/role/my-role \
  secret_id_ttl=10m \
  token_num_uses=10 \
  token_ttl=20m \
  token_max_ttl=30m \
  secret_id_num_uses=40 \
  token_policies=my-policy
```
'my-policy' is already created policy and 'approle' is the auth method already created


```
export ROLE_ID="$(vault read -field=role_id auth/approle/role/my-role/role-id)"
export SECRET_ID="$(vault write -f -field=secret_id auth/approle/role/my-role/secret-id)"
```

Write config
```
vault write auth/approle/login role_id="$ROLE_ID" secret_id="$SECRET_ID"

```

Vault ERROR http: server gave HTTP response to HTTPS client
```
If you're running Vault in a demo or non-production environment, you can configure Vault to disable TLS. In this case, TLS has been disabled, but the default value for VAULT_ADDR is https://127.0.0.1:8200. Therefore Vault is sending the request over HTTPS, but Vault is responding using HTTP since TLS is disabled. In this case, you should set the VAULT_ADDR environment variable to "http://127.0.0.1:8200". This is true if you're running Vault Dev server as well.
```
