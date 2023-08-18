
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

------

yum install epel-release

yum -y install clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd

freshclam

crontab -e
@hourly   /usr/local/bin/freshclam --quiet


groupadd clamav
useradd -g clamav -s /bin/false -c "Clam Antivirus" clamav
