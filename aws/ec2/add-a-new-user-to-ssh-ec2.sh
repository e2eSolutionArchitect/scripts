# This is to add multiple users to SSH an EC2
# The primary user (who has the ssh key pair ) loginto the instance and run below commands to add another user for ssh access to that EC2.
# The new user need to share private-key of his/her key <ssh-private-key-of-the-new-user>

sudo bash
useradd -m --group sudo <username>
mkdir -p /home/<username>/.ssh
echo ssh-rsa <ssh-private-key-of-the-new-user> >> /home/<username>/.ssh/authorized_keys
chmod 700 /home/<username>/.ssh
chmod 600 /home/<username>/.ssh/authorized_keys
chown <username>:<username> -R /home/<username>/.ssh
