## Problem statement: Install jmeter and execute distributed load test in plain EC2 instance with redhat AMI (NON docker environment). 

### Specification used:
- AWS EC2 instance with redhat image
- instance size t2.medium. (note: t2.micro is not recommended. consider atleast t2.small)
- 2 instances. one for jmeter controller and another for worker

### High Level Steps (Non Docker, in plain EC2 with redhat)
- Download and setup JDK and jmeter in jmeter controller and worker nodes
- Generate rmi keystore jks and upload to workers
- start jmeter server in worker node
- Run test in controller node

## Detail steps

### Step 1: Download and setup JDK and jmeter in jmeter controller and worker nodes (using two ec2 instance separate for controller and worker nodes)
1.1 Use the terraform code for above step (terraform code link will be posted soon)
1.2 jmeter manual installation

```
# Install JDK
sudo yum update -y
curl -L --silent <java_download_url> > /user/ec2-user/openjdk-<version>.tgz
tar -xzf user/ec2-user/openjdk-<version>.tgz -C /user/ec2-user
rm -f user/ec2-user/openjdk-<version>.tgz

export JAVA_HOME=/user/ec2-user/jdk-version
export PATH=$JAVA_HOME/bin:$PATH

# Install Jmeter
curl -L --silent <jmeter_download_url> > /user/ec2-user/apache-jmeter-<version>.tgz
tar -xzf user/ec2-user/apache-jmeter-<version>.tgz -C /user/ec2-user
rm -f user/ec2-user/apache-jmeter-<version>.tgz

export JMETER_HOME=/user/ec2-user/apache-jmeter-version
export PATH=$JMETER_HOME/bin:$PATH

```

### Step 2: Connect to controller instance using putty
verify jmeter installation
```
jmeter --version
```
if it doesn't show jmeter logo then check the path settings

```
echo $JAVA_HOME
echo $JMETER_HOME
echo $PATH  (PATH must have jmeter home and java home included)
```

### Step 3: Generate RMI keystore JKS file in Jmeter controller
- browse to <jmeter-home>/bin
- run below command to generate jks
  ```
  ./create-rmi-keystore.sh
  ```
  enter 'rmi' as name and keep pressing enter for all other question. Type "Yes" when it asks for review and enter to generate the jks file. 
NOTE: If the above step fails to generate jks then run below
  ```
  sudo chown -R $USER:$USER /home/ec2-user/apache-jmeter-5.4.3
  ```
  and then run 
    ```
  ./create-rmi-keystore.sh
  ```

### Step 4: Copy and Move RMI keystore JKS file in Jmeter controller and worker(s) nodes
- First copy/move the jks file to <jmeter-home>/bin in controller
  
  ```
  cp rmi_keystore.jsk /home/ec2-user/
  ```
- Secondly download the jks file in your system (local system). this file needs to be trasferred to EVERY worker nodes
  
  To Download from controller EC2
  ```
  pscp -i sample.ppk ec2-user@<dns-url-of-controller-instance>:/home/ec2-user/apache-jmeter-5.4.3/bin/rmi_keystore.jks .  (dont miss the '.' it will copy the file in your local directory)
  ```
  To Upload to worker EC2
  ```
  pscp -i sample.ppk rmi_keystore.jks ec2-user@<dns-url-of-worker-instance>:/home/ec2-user/apache-jmeter-5.4.3/bin/
  ```
  
### Step 5: Configure jmeter.properties in both controller and worker one after another
browse to /home/ec2-user/apache-jmeter-5.4.3/bin/ and open jmeter.properties
  
  ```
  sudo vi jmeter.properties
  ```
  search for port 4000. uncomment the line
  
### Step 6: Start worker server
  connect to your worker instance(s), browse to /home/ec2-user/apache-jmeter-5.4.3/bin/ and run below
  ```
  ./jmeter-server -Djava.rmi.server.hostname=<private ip of worker node> -Dserver.rmi.ssl.disable=true
  
  If you get rmi error then run below
  
   ./jmeter-server -Djava.rmi.server.hostname=<private ip of worker node> -Dserver.rmi.ssl.disable=true -Dserver.rmi.create=false
  ```
  
 ### Step 7: Run test from jmeter controller node
 ```
  jmeter -n -t /home/ec2-user/apache-jmeter-5.4.3/bin/examples/CSVSample.jmx -R=<comma separated private ips of your worker nodes> -l result.log -Dserver.rmi.ssl.disable=true
  
  jmeter -n -t /home/ec2-user/apache-jmeter-5.4.3/bin/examples/CSVSample.jmx -R10.1.1.2,10.1.1.5 -l result.log -Dserver.rmi.ssl.disable=true
```
  

