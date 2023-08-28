

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

## Fix:
