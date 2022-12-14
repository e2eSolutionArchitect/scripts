referance : https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-a-specific-iam-role/
```
aws iam get-role --role-name <role-name>
```

copy the ROLE ID, suppose AROAEXAMPLEID or 111111111111.

add below policy in s3 bucket policy of bucket name "MyExampleBucket"

Run the command: aws iam get-user -–user-name USER-NAME

In the output, look for the userId string, which will begin with AIDAEXAMPLEID for userid and AROAEXAMPLEID for Roleid.

dont be confused with "aws:userId" you can add userId and RoleID with aws:userId. userid will be a string like "AIDA*" or roleid it will be "AROA*"

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::MyExampleBucket",
        "arn:aws:s3:::MyExampleBucket/*"
      ],
      "Condition": {
        "StringNotLike": {
          "aws:userId": [
            "AROAEXAMPLEID:*",
            "111111111111"
          ]
        }
      }
    }
  ]
}
```
