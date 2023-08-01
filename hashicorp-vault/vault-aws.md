- AWS KMS to automatically unseal Vault on private EC2 instances. The subnet where Vault is deployed doesn't have internet access
  Ans: Add a VPC endpoint to enable private connectivity to the KMS service. The other way is to permit outbound access to the Internet simply, but the VPC endpoint is more secure since the traffic never leaves the AWS network
