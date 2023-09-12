
## Install docker in Ubuntu. 
## for the docker documentation for updated info. the instructions below are from https://docs.docker.com/engine/install/ubuntu/

## Update the apt package index and install packages to allow apt to use a repository over HTTPS:

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### -------------Optional----------------
### To install a specific version of Docker Engine, list the available versions in the repo, then select and install:

### a. List the versions available in your repo:
```
 apt-cache madison docker-ce

  docker-ce | 5:18.09.1~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 5:18.09.0~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 18.06.1~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  docker-ce | 18.06.0~ce~3-0~ubuntu       | https://download.docker.com/linux/ubuntu  xenial/stable amd64 Packages
  ...
```
### b. Install a specific version using the version string from the second column, for example, 5:18.09.1~3-0~ubuntu-xenial.

```
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```
-----------------------------

## Verify that Docker Engine is installed correctly by running the hello-world image.
```
sudo docker run hello-world
```

### *********dont user root for docker setup***********
## login to your VM instance
## Change the user to sudo 
```
sudo su -
```
## create an user 
```
useradd -d /home/awstechguide -m awstechguide
```
## create password for this user. a non expiry password
```
passwd awstechguide
passwd -x -1 awstechguide
```
## change to the new user
```
su -s awstechguide
```
### *********add user to docker group after docker installation***********

## To create the docker group and add your user:

## Create the docker group.
 ```
 sudo groupadd docker
```
## Add your user to the docker group.
 ```
 sudo usermod -aG docker ${USER}
```
## You would need to loog out and log back in so that your group membership is re-evaluated or type the following command:
 ```
 su -s ${USER}
```

## Verify that you can run docker commands without sudo.
 ```
 docker run hello-world
```
