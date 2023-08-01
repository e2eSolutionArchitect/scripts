- AWS KMS to automatically unseal Vault on private EC2 instances. The subnet where Vault is deployed into doesn't have internet access
  Ans: Add a VPC endpoint to enable private connectivity to the KMS service
