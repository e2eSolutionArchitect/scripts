ClamAV documentation [here](https://docs.clamav.net)
Docker Hub [here](https://hub.docker.com/r/clamav/clamav)

Recommended RAM for ClamAV (As of 2020/09/20): Minimum: 3 GiB, Preferred: 4 GiB

# On RHEL Install

# On Ubuntu Install

# On Docker Install

### All images come in two forms:

- clamav/clamav:<version>: A release preloaded with signature databases.

Using this container will save the ClamAV project some bandwidth. Use this if you will keep the image around so that you don't download the entire database set every time you start a new container. Updating with FreshClam from existing databases set does not use much data.

- clamav/clamav:<version>_base: A release with no signature databases.

Use this container only if you mount a volume in your container under /var/lib/clamav to persist your signature database databases. This method is the best option because it will reduce data costs for ClamAV and for the Docker registry, but it does require advanced familiarity with Linux and Docker.
