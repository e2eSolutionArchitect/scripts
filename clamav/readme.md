Contents referred from ClamAV documentation [here](https://docs.clamav.net)
Docker Hub [here](https://hub.docker.com/r/clamav/clamav)

 

Recommended RAM for ClamAV (As of 2020/09/20): Minimum: 3 GiB, Preferred: 4 GiB

# On RHEL Install

# On Ubuntu Install

# On Docker Install - check [here](https://docs.clamav.net/manual/Installing/Docker.html) 

### All images come in two forms: 

- clamav/clamav:<version>: A release preloaded with signature databases.

Using this container will save the ClamAV project some bandwidth. Use this if you will keep the image around so that you don't download the entire database set every time you start a new container. Updating with FreshClam from existing databases set does not use much data.

- clamav/clamav:<version>_base: A release with no signature databases.

Use this container only if you mount a volume in your container under /var/lib/clamav to persist your signature database databases. This method is the best option because it will reduce data costs for ClamAV and for the Docker registry, but it does require advanced familiarity with Linux and Docker.

### clamav/clamav:latest_base and clamav/clamav:latest: These are the same as clamav/clamav:stable_base and clamav/clamav:stable. They exist because many users expect all images to have a "latest".

### Persisting the virus database (volume)
The virus database in /var/lib/clamav is by default unique to each container and thus is normally not shared.

1. Create a Docker volume using the docker volume command.. Volumes are completely managed by Docker and are the best choice for creating a persistent database volume.
For example, create a "clam_db" volume:
```
docker volume create clam_db
```
2. Create a Bind Mount that maps a file system directory to a path within the container.
Run the container with these arguments to mount the a directory from your host environment as a volume in the container.
--mount type=bind,source=/path/to/databases,target=/var/lib/clamav

```
docker run -it --rm \
    --name "clam_container_01" \
    --mount type=bind,source=/path/to/databases,target=/var/lib/clamav \
    clamav/clamav:stable_base


```
