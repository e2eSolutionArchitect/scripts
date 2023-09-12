#!/bin/bash -xe
echo 'Starting Update'
sudo yum install -y update yum-utils nfs-utils
echo 'Create efs mount' 
sudo mkdir efs
sudo chmod -R 777 efs
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-050d6dbc42c12259e.efs.us-east-1.amazonaws.com:/ efs
df -h