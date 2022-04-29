Update the packages on your instance

```
[ec2-user ~]$ sudo yum update -y
```

Install Docker

```
[ec2-user ~]$ sudo yum install docker -y
```

Start the Docker Service

```
[ec2-user ~]$ sudo service docker start
```

Add the ec2-user to the docker group so you can execute Docker commands without using sudo.

```
[ec2-user ~]$ sudo usermod -a -G docker ec2-user
```
