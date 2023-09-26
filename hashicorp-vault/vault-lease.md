

Revoke lease

```
vault lease revoke -prefix <path> -- rekove all from this path
vault lease revoke -prefix aws/mycreds

vault lease revoke aws/mycred/<lease_id> -- revoke particular lease

```
