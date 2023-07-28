
Generating dynamic secrets for AWS
- You need to have ACCESS_KEY, SECRET_KEY as prerequisite
- Enable AWS secret engine
```
vault secrets enable -path=aws aws
```
- Set root config
```
vault write aws/config/root \
access_key = #### \
secret_key = #### \
region = us-east-1
```
- Setup role 'my-ec2-role'
```
vault write aws/roles/my-ec2-role \
      credential_type=iam_user \
      policy_document=-<<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt18712309772343400"
      "Effect": "Allow",
      "Action": [
        "ec2:*"
      ],
      "Resource": ["*"]
    }
  ]
}
```
- Vault to generate ACCESS_KEY, SECRET_KEY for role  'my-ec2-role'

```
vault read aws/creds/my-ec2-role

```

How to revoke the dynamic key?
```
vault lease revoke aws/creds/my-ec2-role/JJASD534dfg5df67789dfgJASDASD
```
