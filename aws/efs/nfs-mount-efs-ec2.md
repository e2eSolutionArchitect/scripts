
# Create EFS
- Simply create an EFS filesystem and get the file-system id. e.g, fs-########
- Select the EFS filesystem and go to it's 'Network' tab. select the 'Security Group'
- The Security group must have type NSF for port 2049 open for either 0.0.0.0/0 or any specific source which connects the file-system (e,g the EC2s which creates mount with the this EFS)


# Mount EFS with RHEL instance via NFS
- Provision an EC2 with RHEL OS
- Refer userdata for the instalnce [here](https://github.com/e2eSolutionArchitect/scripts/blob/main/aws/ec2/userdata-nfs-mount-efs-RHEL.sh)
- The userdata script is supposed to make a directory for mount point 'efs'
- The command to mount efs with directory 'efs' in ec2 is as below
```
  e.g sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-######.efs.us-east-1.amazonaws.com:/ efs
```

# Important: 
- Make sure to configure security group to have access between EFS ( type NFS - port 2049) and EC2
