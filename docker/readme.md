```
docker run <image name> (run a docker image)
docker ps 
docker ps -a

```

```
docker image ls (list available docker images)
docker container ls (list running containers)
```

```

docker -v  # check version
docker stop <container name>
docker ps -a # check stopped containers 
docker volume --help # to get docker volume commands
```

```
docker image rm -f db2b37ec6181 # delete images forcibly 
```

```
docker volume create <volume name>
```

```
docker volume inspect <volume name> // describe a volume and find the mount path 
```

```
docker volume ls # list volume
```

```
docker volume prune // will remove all unused volumes, which are not used by any containers 
```

```
docker volume rm 
```
