Install Java
```
sudp apt update
sudo apt install default-jdk
java -version

```
Install Tomcat v10.0.20
```
mkdir tomcat
cd tomcat
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.20/bin/apache-tomcat-10.0.20.tar.gz
sudo tar xzvf apache-tomcat-10*tar.gz -C /opt/tomcat --strip-components=1
```

Configure Tomcat Service

```
# Reload the systemd daemon so that it becomes aware of the new service
sudo systemctl daemon-reload

# start the Tomcat service
sudo systemctl start tomcat

# status to confirm that it started successfully
sudo systemctl status tomcat

# To enable Tomcat starting up with the system, run the following command:
sudo systemctl enable tomcat

```
