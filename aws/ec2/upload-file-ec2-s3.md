### considering a scenario where you want to zip a directory in your EC2 and then transfer to S3 bucket``

### Zip a directory in ubuntu EC2 instance``

```
apt install zip

zip -r temp.zip existing_folder
```

Create an IAM role with S3 write access or admin access

### Map the IAM role to an EC2 instance``

### Install CLI

```
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install
```

### Run the AWS s3 cp command to copy the single file to the S3 bucket

```
aws s3 cp <source file with full path> s3://<s3bucket_name>
aws s3 cp /home/ec2-user/copy.zip s3://<s3bucket_name>
```

### Run the AWS s3 cp command to recursive file copy to the S3 bucket

```
aws s3 cp <source directory path> s3://<s3bucket_name> --recursive
aws s3 cp /home/ec2-user/mydir s3://<s3bucket_name> --recursive
```

### sync files to S3 bucket
sync will only upload the new or modified files. As it named sync

```
aws s3 sync <source directory path> s3://<s3bucket_name>
aws s3 sync /home/ec2-user/mydir s3://<s3bucket_name>
```


### if upload fails showing "Warning: Skipping file /home/ec2-user/copy.zip"

```
check file permission
ls -l /home/ec2-user/copy.zip

you may have -rw-------- on this file . So change the file permission

chmod 644 /home/ec2-user/copy.zip

Now the permission should show -rw-r--r--

Now run the copy command again
aws s3 cp /home/ec2-user/copy.zip s3://<s3bucket_name>
```
### Copy from S3 to EC2
```
aws s3 cp s3://<s3bucket_name>/copy.zip .  (dont miss the '.' It will copy to your corrent directry. Or provide a directory path like /home/ec2-user/)
```
you can also use s3 presigned url (incase your s3 bucket is private) to download
1. select the object in s3 bucket > Click Action > Create Pre-signed url by adding time validity 
2. go to your EC2. run below command to download the object to ec2. NOTE: add your pre-signed url into ""

```
curl "https://......"
```

### If you want to a diff AWS account suppose Account A to account B. everything remains same. just make sure you have your account B's credential configuied in account A
go to home/ec2-user/.aws and update the credential of account B in 'credential' file of account A

### Upload from local system to ec2
```
scp -i ~/Downloads/file.pem local_image_file user@ec2_elastic_ip:/home/user/
```
