
# Create EFS
- Simply create an EFS filesystem and get the file-system id. e.g, fs-########
- Select the EFS filesystem and go to it's 'Network' tab. select the 'Security Group'
- The Security group must have type NSF for port 2049 open for either 0.0.0.0/0 or any specific source which connects the file-system (e,g the EC2s which creates mount with the this EFS)


# Mount EFS with RHEL instance via NFS
