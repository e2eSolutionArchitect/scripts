

## Error: cli_loaddbdir: No supported database files found in /var/lib/clamav ERROR: Can't open file or directory
While running below command
```
sudo docker run --rm \
  --name "clamav_container_01" \
  --mount source=clam_db,target=/var/lib/clamav \
  --mount type=bind,source=/opt/scandir,target=/scandir \
  --env 'CLAMAV_NO_FRESHCLAMD=false' \
  --env 'FRESHCLAM_CHECKS=24' \
  clamav/clamav:1.0.2_base \
  clamscan /scandir
```

Fix: remove clamscan /scandir part and run
```
sudo docker run --rm \
  --name "clamav_container_01" \
  --mount source=clam_db,target=/var/lib/clamav \
  --mount type=bind,source=/opt/scandir,target=/scandir \
  --env 'CLAMAV_NO_FRESHCLAMD=false' \
  --env 'FRESHCLAM_CHECKS=24' \
  clamav/clamav:1.0.2_base 
```

## Could not connect to clamd on LocalSocket /tmp/clamd.sock: No such file or directory

Fix:


---------------------------------------

## ERROR: Can't open /var/log/clamav/freshclam.log in append mode (check permissions!)
```
sudo chmod -R 777 /var/log/clamav
which freshclam
```

## ERROR: /var/log/clamav/freshclam.log is locked by another process
## freshclam run automatically, If you want to stop the daemon and run it manually:
```
sudo systemctl stop clamav-freshclam.service
sudo freshclam
```

## Error: Could not connect to clamd on LocalSocket /var/run/clamav/clamd.ctl: No such file or directory LibClamAV Error: File tree walk aborted.
If clamd didn't run properly it will generate below error. clamd creates clamd.ctl file in /var/run/clamav/

Fix:
```
mkdir /var/run/clamav
sudo chmod -R 777 /var/run/clamav
sudo clamd
```
