
# Install in Ubuntu 

```
sudo apt-get install -y clamav clamav-base clamav-daemon clamav-freshclam clamav-testfiles
```

# ERROR: Can't open /var/log/clamav/freshclam.log in append mode (check permissions!)
```
sudo chmod -R 777 /var/log/clamav
which freshclam
```

# ERROR: /var/log/clamav/freshclam.log is locked by another process
# freshclam run automatically, If you want to stop the daemon and run it manually:
```
sudo systemctl stop clamav-freshclam.service
sudo freshclam
```

crontab -e
@hourly   /usr/bin/freshclam --quiet

# Configure clamd 
cd /etc/clamav
vi clamd.conf
vi  freshclam.conf

# Start clamav service

```
sudo systemctl start clamav-freshclam.service
sudo systemctl status clamav-freshclam.service
```
# Install htop to check momory consumption
```
sudo apt-get install htop -y 
htop
```

# run clamd. check LocalSocket path in clamd.conf
```
mkdir /var/run/clamav
sudo chmod -R 777 /var/run/clamav
sudo clamd
```

# Run scan 

```
clamdscan --fdpass <scan directory>
clamdscan --fdpass /home/ubuntu/scantest
```


# Generate example config
```
clamconf -g freshclam.conf > freshclam.conf
clamconf -g clamd.conf > clamd.conf
```


# Enable On Access Scanning 
Update clamd.conf with below attributes
```
OnAccessIncludePath /home/ubuntu/scandir
OnAccessPrevention yes
OnAccessExcludeUname clamav
```
### If getting permission issue to update clamd.conf. change the permission

```
sudo chmod -R 777 /etc/clamav/clamd.conf
```

