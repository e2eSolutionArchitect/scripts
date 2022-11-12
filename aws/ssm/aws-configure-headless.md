aws configure set varname value [--profile profile-name]

https://docs.aws.amazon.com/cli/latest/reference/configure/set.html

```
$ aws configure set aws_access_key_id default_access_key  --profile testing
$ aws configure set aws_secret_access_key default_secret_key  --profile testing
$ aws configure set default.region us-west-2  --profile testing
$ aws configure set default.ca_bundle /path/to/ca-bundle.pem  --profile testing
$ aws configure set region us-west-1 --profile testing
```
