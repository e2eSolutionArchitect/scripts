yum install epel-release

yum -y install clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd

freshclam

crontab -e
@hourly   /usr/local/bin/freshclam --quiet


groupadd clamav
useradd -g clamav -s /bin/false -c "Clam Antivirus" clamav
