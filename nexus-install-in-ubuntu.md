
## update packages

sudo apt-get update

## install openjdk 8

sudo apt install openjdk-8-jdk 

## change user to sudo

sudo su

## browse to /opt. where we will install nexus

## get nexus binary 

wget https://sonatype-download.global.ssl.fastly.net/nexus/3/nexus-3.24.0-02-unix.tar.gz

tar -zxvf  nexus-3.24.0-02-unix.tar.gz

mv /opt/nexus-3.24.0-02 /opt/nexus

## add user. (best practice to avoid root user. create new user)

sudo adduser nexus

## add priviledge to new user
 visudo 
 
 ###add  nexus   ALL=(ALL)       NOPASSWD: ALL

## change ownership to new user
sudo chown -R nexus:nexus /opt/nexus

sudo chown -R nexus:nexus /opt/sonatype-work

## update /opt/nexus/bin/nexus.rc file, just uncomment run_as_user

vi /opt/nexus/bin/nexus.rc

run_as_user="nexus"

## Add nexus as a service at boot time

sudo ln -s /opt/nexus/bin/nexus /etc/init.d/nexus

## start nexus

/etc/init.d/nexus start

## check the services running on ports

netstat -nlpt

it should show like below 

Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name

### tcp        0      0 0.0.0.0:8081            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:36665         0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -          


http://nexuxserver url:8081  (default 8081). Make sure you have 8081 port in your security group (for AWS) / network rule (for Azure) / ingress rule ( for GCP) 

Use below credentials to login

username : admin

get initial password from path /opt/sonatype-work/nexus3/admin.password 

run cat /opt/sonatype-work/nexus3/admin.password in your nexus server. 


# pull artifact from nexus to jenkins and deploy to tomcat 
## in JENKINS build job write below shell script to pull artifact 

wget --user=<nexux username> --password=<password> <nexus artifact url (war/ear)>

wget --user=admin --password=admin http://35.184.138.42:8081/repository/maven-snapshots/awstechguide/spring-webapp/1.0.0-SNAPSHOT/spring-webapp-1.0.0-20200703.145607-1.WAR



