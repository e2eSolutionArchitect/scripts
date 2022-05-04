## Context: We are discussing here about the installation of jmeter and executing distributed load test in plain EC2 instance with redhat AMI (NON docker environment). 

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

### Step 3: RMI keystore JKS file in Jmeter controller
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
  
### Step 4: Configure jmeter.properties
- 
- 
- Log into controller node and generate rmi keystore jks. copy the jsk file to <jmeter-home>/bin  in controller node
- Download the rmi keystore jks file from controller node and upload to <jmeter-home>/bin in worker(s) nodes
- start jmeter server in worker node
- Run test in controller node
  

