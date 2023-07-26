
Generating dynamic secrets for AWS
- You need to have ACCESS_KEY, SECRET_KEY as prerequisite
- Enable AWS secret engine
```
vault secrets enable -path=myaws aws
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
