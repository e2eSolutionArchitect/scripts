## Install mysql and phpadmin on docker

### Update ubuntu instance and install OpenJDK11

sudo apt-get update && sudo apt-get upgrade -y 

sudo apt-get install openjdk-11-jre -y 

### Refer docker documentation to install docker on ubuntu

### https://docs.docker.com/engine/install/ubuntu/

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common -y
	
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
   sudo apt-get update
   
   sudo apt-get install docker-ce docker-ce-cli containerd.io -y
   
   sudo usermod -aG docker ubuntu
   
   sudo systemctl status docker
   
### dont user root for docker setup

### login to your VM instance

### Change the user to sudo

sudo su -

### create an user

useradd -d /home/awstechguide -m awstechguide

### create password for this user. a non expiry password

passwd awstechguide

passwd -x -1 awstechguide

### add user to docker group after docker installation

### To create the docker group and add your user:

### Create the docker group.

sudo groupadd docker

### Add your user to the docker group.

sudo usermod -aG docker ${USER}

### You would need to loog out and log back in so that your group membership is re-evaluated or type the following command:

su -s ${USER}

### Verify that you can run docker commands without sudo.

docker run hello-world
   
### Install mysql
docker pull mysql:8
docker run -e MYSQL_ROOT_PASSWORD=pass123 -d mysql


docker exec "mysql container id" mysql --version

docker exec "mysql container id" mysql -uroot -p"root-passwd" -e 'show databases;'

docker exec -it "mysql container id"  mysql -uroot -p<root-passwd>

create database DEVTEST
   
use DEVTEST

CREATE USER 'testurs'@'localhost' IDENTIFIED BY 'test123'; 
   
### Install phpmyadmin
docker pull phpmyadmin/phpmyadmin:latest

### link phpmyadmin container with mysql and  run in backgroud 

docker run --name myadmin -d --link  "container id of mysql":db -p 8899:80 phpmyadmin/phpmyadmin

Note: we are using 8899 port for phpmyadmin. 

### use docker compose

### reference : https://docs.docker.com/compose/install/

### Install docker compose

### Run this command to download the current stable release of Docker Compose:

sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


### Apply executable permissions to the binary:

sudo chmod +x /usr/local/bin/docker-compose

### Test the installation

docker-compose --version

### write docket compose to manage mysql and phpmyadmin and then start docker compose

docker-compose up -d

docker ps
