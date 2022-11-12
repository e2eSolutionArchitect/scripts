
# check if instance IAM profile enough to run below

```
aws secretsmanager describe-secrets --secret-id <secret-name>
aws secretsmanager get-secret-value --secret-id <secret-name> --version-stage AWSCURRENT 
 ```
 https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html
 
```
 export AWS_REGION=your_aws_region
 export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
```


aws configure set varname value [--profile profile-name]

https://docs.aws.amazon.com/cli/latest/reference/configure/set.html

```
$ aws configure set aws_access_key_id default_access_key  --profile testing
$ aws configure set aws_secret_access_key default_secret_key  --profile testing
$ aws configure set default.region us-west-2  --profile testing
$ aws configure set default.ca_bundle /path/to/ca-bundle.pem  --profile testing
$ aws configure set region us-west-1 --profile testing
```
 
 ```
aws ssm put-parameter --name mysecret --type SecureString --value 'secret value' --profile <aws-cli-profile-name>
aws ssm get-parameter --name mysecret --profile <aws-cli-profile-name>
aws ssm get-parameter --name mysecret --with-decryption --profile <aws-cli-profile-name>
```
https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-ps-secretsmanager.html

```
aws ssm get-parameter \
    --name /aws/reference/secretsmanager/s1-secret:AWSCURRENT \
    --with-decryption
```
