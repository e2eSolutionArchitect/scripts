### reference : https://docs.docker.com/compose/install/
 
## Install docker compose
### Run this command to download the current stable release of Docker Compose:
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

### Apply executable permissions to the binary:
 sudo chmod +x /usr/local/bin/docker-compose


### Test the installation
docker-compose --version
