
### Execute below commands in an Ubuntu VM to install and setup Apache. 

```
sudo apt update
sudo apt install apache2
sudo ufw app list
sudo ufw allow 'Apache'
sudo ufw status
sudo systemctl status apache2
hostname -I
```

Test 

```
http://your_server_ip
``
