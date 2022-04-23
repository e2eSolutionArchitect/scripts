

## update packages
``` 
sudo apt-get update
``` 
## install openjdk 11

```
sudo apt-get update && sudo apt-get upgrade -y 

sudo apt-get install openjdk-11-jdk
``` 
### Alternatively, if you need JRE only then 

sudo apt-get install openjdk-11-jre

## browser to local directory and download tomcat binary

``` 
cd /usr/local/
wget https://mirror.csclub.uwaterloo.ca/apache/tomcat/tomcat-8/v8.5.56/bin/apache-tomcat-8.5.56.tar.gz
tar xvzf apache-tomcat-8.5.56.tar.gz 
``` 

## rename installation directory
``` 
mv apache-tomcat-8.5.56.tar.gz tomcat 
``` 
## start tomcat
``` 
cd /usr/local/tomcat/bin/
./startup.sh 
```

## check process 
 ``` 
 ps -ef | grep tomcat
``` 
## stop tomcat 
``` 
./shutdown.sh
``` 
 
## kill process 
``` 
sudo kill -9 <processid> 
``` 

