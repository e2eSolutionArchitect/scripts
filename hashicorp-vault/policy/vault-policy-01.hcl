path "secret/data/*" {
capabilities = ["create","update"]
}

path "secret/data/foo" {
capabilities = ["read"]
}
