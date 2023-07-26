# production env config

storage "raft" {
  path = "./vault/data"
  node_id = "node1"
  }

listener "tcp" {
   address = "0.0.0.0:8200" # 0.0.0.0 is because of installing vault in a remote VM
   tls_disable = "true" # for actual production this value should be false
  }

api_addr = "http://127.0.0.1:8200"
cluster_addr = "https://127.0.0.1:8201"
ui = true
