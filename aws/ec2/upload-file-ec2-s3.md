`` considering a scenario where you want to zip a directory in your EC2 and then transfer to S3 bucket``

``Zip a directory in ubuntu EC2 instance``

apt install zip

zip -r temp.zip existing_folder

``Create an IAM role with S3 write access or admin access``

``Map the IAM role to an EC2 instance``

``Install CLI``

$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install

``Run the AWS s3 cp command to copy the files to the S3 bucket``

aws s3 cp copy.zip s3://<s3bucket_name>
