
```
sudo bash
useradd -m --group sudo <username>
mkdir -p /home/<username>/.ssh
echo ssh-rsa <ssh-private-key-of-the-new-user> >> /home/<username>/.ssh/authorized_keys
chmod 700 /home/<username>/.ssh
chmod 600 /home/<username>/.ssh/authorized_keys
chown <username>:<username> -R /home/<username>/.ssh

```
