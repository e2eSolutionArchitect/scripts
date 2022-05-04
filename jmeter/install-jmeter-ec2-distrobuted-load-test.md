## Context: We are discussing here about the installation of jmeter and executing distributed load test in NON docker environment. 

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
sudo yum update -y
curl -L silent
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

- 
- 
- Log into controller node and generate rmi keystore jks. copy the jsk file to <jmeter-home>/bin  in controller node
- Download the rmi keystore jks file from controller node and upload to <jmeter-home>/bin in worker(s) nodes
- start jmeter server in worker node
- Run test in controller node
  

