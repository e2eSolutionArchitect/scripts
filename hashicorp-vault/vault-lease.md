

Revoke lease

```
vault lease revoke -prefix <path> -- leases from a secrets engine using the -prefix
vault lease revoke -prefix aws/mycreds

vault lease revoke aws/mycred/<lease_id> -- revoke particular lease

```
