## Install and Run jenkins in docker container 

## Using Ubuntu system
## Install Docker
### follow instruction to install docker in ubuntu platform https://docs.docker.com/engine/install/ubuntu/

# pull docker image
docker pull jenkins

# create docker volume
docker volume create jenkins

# list docker volumes
docker volumn ls

# run jenkins image and map to docker volume
docker run -p 8080:8080 -p 50000:50000 -v jenkins:/var/jenkins_home jenkins
