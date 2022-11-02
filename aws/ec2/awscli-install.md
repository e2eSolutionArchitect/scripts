Zip a directory in ubuntu EC2 instance``

```
sudo apt install zip -y

zip -r temp.zip existing_folder

```
Create an IAM role with S3 write access or admin access

Map the IAM role to an EC2 instance
Install CLI

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install

```
