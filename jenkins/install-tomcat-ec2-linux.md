## Check java version in EC2 linux instance 

java -version

## Install openjdk 8

sudo yum install java-1.8.0-openjdk

## Remove old version

sudo yum remove java

## Tomcat website http://tomcat.apache.org/

## Copy download link from http://apache.forsale.plus/tomcat/tomcat-8/v8.5.54/bin/apache-tomcat-8.5.54.tar.gz

## login to EC2 instance and change user to sudo  

sudo su -

## download tar in ec2

wget <paste the tar.gz address copied in step1>

## extract 
tar -xvzf <tar file name>

## Browse to the bin folder under tomcat folder.  Two files, namely; startup.sh and shutdown.sh. 

## start tomcat service

./startup.sh

## /*Change port number from 8080 to 8090 (if your Jenkins on AWS is also listening to the port 8080)
Browse to conf sub-directory under Tomcat directory and open server.xml file for editing using ‘vi’ command */

vi server.xml

## Allow port no 8090 under security group in AWS


## Restart the tomcat service (browse to the bin folder)

./shutdown.sh
./startup.sh


### Go to Browser and type- 

http://<ip_address>:<port no>  defalut is 8080

### Configure for manager app access outside of tomcat server: find context file location

find / -name context.xml

## update context.xml by commenting context value eliment only. do the same in both context.xml files. 
### check tomcat manager link

## for user creation go to conf/tomcat-users.xml

### add role and user in conf/tomcat-users.xml

<role rolename="manager-gui"/>
<user username="tomcat" password="s3cret" roles="manager-gui"/>

# below role and user config is for deploying was from an external system 

<role rolename="manager-script"/>
<user username="deployer" password="deployer" roles="manager-script"/>

restart tomcat
