#!/bin/bash -xe
echo 'Starting Update'
sudo apt-get update -y
echo 'Starting clamav install'
sudo apt-get install -y clamav clamav-base clamav-daemon clamav-freshclam
sudo chmod -R 777 /var/log/clamav
echo 'Check status'
sudo systemctl status clamav-freshclam.service
which freshclam
sudo mkdir /var/run/clamav
echo 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > /home/ubuntu/scandir/bad.txt
echo 'I am good file' > /home/ubuntu/scandir/good.txt
sudo chmod -R 777 /var/run/clamav
sudo clamd
sudo clamdscan --fdpass --move=/home/ubuntu/quarantined /home/ubuntu/scandir