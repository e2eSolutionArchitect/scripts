Install Java
```
sudo apt update
sudo apt install default-jdk
# or for java 11
sudo apt install openjdk-11-jdk

java -version

```
Install Tomcat v10.0.20
```
mkdir tomcat
cd tomcat
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.20/bin/apache-tomcat-10.0.20.tar.gz
sudo tar xzvf apache-tomcat-10*tar.gz -C /opt/tomcat --strip-components=1
```

# create a user
```
sudo useradd -m -d /opt/tomcat -U -s /bin/false tomcat

# grant ownership the to the new user
sudo chown -R tomcat:tomcat /opt/tomcat/
sudo chmod -R u+x /opt/tomcat/bin
```
Configure Admin user
```
sudo nano /opt/tomcat/conf/tomcat-users.xml
```
Update passwords 'manager_password' and 'admin_password'
```
<role rolename="manager-gui" />
<user username="manager" password="manager_password" roles="manager-gui" />

<role rolename="admin-gui" />
<user username="admin" password="admin_password" roles="manager-gui,admin-gui" />
```
Remove the restriction for the Manager page, open its config file for editing
```
sudo nano /opt/tomcat/webapps/manager/META-INF/context.xml
```
Comment out the Valve definition, as shown
```
...
<Context antiResourceLocking="false" privileged="true" >
  <CookieProcessor className="org.apache.tomcat.util.http.Rfc6265CookieProcessor"
                   sameSiteCookies="strict" />
<!--  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" /> -->
  <Manager sessionAttributeValueClassNameFilter="java\.lang\.(?:Boolean|Integer|Long|Number|String)|org\.apache\.catalina\.filters\.Csr>
</Context>
```

Do the same for host manager
```
sudo nano /opt/tomcat/webapps/host-manager/META-INF/context.xml
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
