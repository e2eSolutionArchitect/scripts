
Get policy list
```
vault policy list
```

Create policy [vault-policy-01.hcl](https://github.com/e2eSolutionArchitect/scripts/blob/main/hashicorp-vault/vault-policy-01.hcl)

```
vault policy write my-policy vault-policy-01.hcl
```

Check content of a policy
```
vault policy read <policy-name>
vault policy read my-policy
```

Delete policy
```
vault policy delete <policy-name>
```
## When using policy , it should be attached with a token before it is used

Attach a token with Policy

```
export VAULT_TOKEN="$(vault token create -field token -policy=my-policy)"
```

Policy to restrict a path access
```
path "secret/apps/confidential" {
     capabilities =["deny"]
}

or use + as wildcards instead of calling-out each segments of the path

path "secret/+/confi*" {
     capabilities =["deny"]
}
```
