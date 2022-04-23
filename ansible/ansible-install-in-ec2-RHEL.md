
##************INSTALL ANSIBLE STARTS****************

###update instance in ansible controller and all remote hosts

sudo yum update (Linux)
sudo apt-get update (Ubuntu)

###Install RPEL. get RPEL link from https://fedoraproject.org/wiki/EPEL
### for ansible installation is it good to use Redhat Image

sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

###install ansible with YUM

yum install ansible

### ansible version

ansible --version


### /etc/ansible -- main config directory
### /etc/ansible/ansible.cfg -- config file
### /etc/ansible/hosts -- all clients info saved. ansible inventory directory. client name , server names saved here

###change the user to sudo 

sudo su -

### create an user for ansible . make sure you are creating it as root. best practice to use user other than root. 

useradd -d /home/awstechguide -m awstechguide

### create password for this user. a non expiry password

passwd awstechguide
passwd -x -1 awstechguide

### browse to /ect/ansible and open hosts file to add remote host ips

vi /etc/ansible/hosts 

### create groups and mention remote host ips like below 

### if it doesn't edit as your user. change to sudo user, edit the file and back to your user. 

[webservers]
3.86.186.116

[dbservers]
3.80.198.8



###************INSTALL ANSIBLE ENDS****************
###************CONNECT REMOTE HOSTS WITH ANSIBLE CONTROLLER STARTS****************
###**********DO THIS FOR ALL REMOTE HOSTS THOSE NEED TO CONNECT TO ANSIBLE HOST/CONTROLLER **********

###update all remote hosts

sudo yum update (Linux)
sudo apt-get update (Ubuntu)

###change to sudo user 

sudo su -

### create an user in remotehost . make sure you are creating it as root. best practice to use user other than root. 

useradd -d /home/awstgremotedb -m awstgremotedb

### create password for this user. a non expiry password

passwd awstgremotedb
passwd -x -1 awstgremotedb

###change user to newly created user

su - awstgremotedb

### generate key in remote host

###browse to '.ssh' directory in your user profile. 
###If it doesnt exit create it

mkdir .ssh

### chnage directory permission

chmod 700 .ssh/

### browse into directory

cd .ssh

###run 

ssh-keygen

awstgremotedb@remotehost:~/.ssh$ ssh-keygen
Generating public/private rsa key pair. 
Enter file in which to save the key (/home/awstgremotedb/.ssh/id_rsa): ******* just press enter
Enter passphrase (empty for no passphrase): ******* just press enter
Enter same passphrase again:***** just press enter
Your identification has been saved in /home/awstgremotedb/.ssh/id_rsa.
Your public key has been saved in /home/awstgremotedb/.ssh/id_rsa.pub.

###create new file authorized_keys

touch authorized_keys

awstgremotedb@remotehost:~$ cd .ssh
awstgremotedb@remotehost:~/.ssh$ ll
-rw-rw-r-- 1 awstgremotedb awstgremotedb    0 May 20 10:39 authorized_keys
-rw------- 1 awstgremotedb awstgremotedb 1675 May 20 10:38 id_rsa
-rw-r--r-- 1 awstgremotedb awstgremotedb  410 May 20 10:38 id_rsa.pub


### MAKE SURE the permissions are -rw------- in remotehost /.ssh. if not change the permissions by chmod 600

[awstgremotedb@ip-172-31-90-177 .ssh]$ chmod 600 authorized_keys
[awstgremotedb@ip-172-31-90-177 .ssh]$ ll
total 12
-rw------- 1 awstgremotedb awstgremotedb  410 May 20 11:19 authorized_keys
-rw------- 1 awstgremotedb awstgremotedb 1679 May 20 11:18 id_rsa
-rw------- 1 awstgremotedb awstgremotedb  410 May 20 11:18 id_rsa.pub


### all three files above will be ownered by the new user created. like awstgremotedb. if its not showing like that. change the owner by below command
###set the file owner as awstechguide

chown awstgremotedb:awstgremotedb authorized_keys

### id_rsa.pub is public key. id_rsa is private key
### VERY IMPORTANT STEP: 
### [ remote host ]copy public key in authorized_keys
### copy private key of remotehost from id_rsa and in ansible host system under /etc/ansible  create a new file with any name. like remotehost.key. and past the private key which you copied 
### from remotehost

awstgremotedb@remotehost:~/.ssh$ cat id_rsa.pub

###copy the public key in authorized_keys file 

awstgremotedb@remotehost:~/.ssh$ vi authorized_keys

### open and copy private key id_rsa from remote host

awstgremotedb@remotehost:~/.ssh$ cat id_rsa

###***********************************go to ansible host/controller 
###change user to newly created user

su - awstechguide

###create a new file under /etc/ansible.  say remotehost1.key. and paste the private key copied from remotehost

###make owner of directory awstechguide

chown awstechguide:awstechguide /etc/ansible

[root@ip-172-31-83-158 ansible]### ll
total 28
-rw-r--r--. 1 root root 19985 May 13 04:01 ansible.cfg
-rw-r--r--. 1 root root  1221 May 19 13:58 hosts
drwxr-xr-x. 2 root root     6 May 13 04:01 roles

### create a new file with private key from remote host

vi remotehost1.key

### update file permission of the new key file 

chmod 600 remotehost1.key

###test ssh connection from ansible host/controller to remote hosts

ssh -p22 -i /etc/ansible/remotehost1.key <remotehost username>@<remote host ip>
ssh -p22 -i /etc/ansible/remotehost-web.key awstgremotedb@3.86.186.116
ssh -p22 ansadmin@40.112.208.131

###update vi etc/ansible/host

[webservers]
54.164.166.210 ansible_ssh_user=<hostname of remote system> ansible_ssh_private_key_file=<key file location in ansible host to connect the particular remote host>
54.164.166.210 ansible_ssh_user=ec2-user ansible_ssh_private_key_file=/etc/ansible/remotehost1.key
OR to pass the sudo password for remote host use below command
54.160.76.21 ansible_ssh_user=awstgremoteweb ansible_ssh_private_key_file=/etc/ansible/webserver1.key ansible_sudo_pass=awstgremoteweb

OR if you are not connecting using SSHkey. just ssh password then use below command in inventory file
<remote host ip> ansible_user=<remote host user name> ansible_password=<remote host password>
52.160.40.11 ansible_user=awstgremotehost ansible_password=awstgremotehost


###ping remote host by group name . dbservers

ansible webservers -m ping
ansible dbservers -m ping
ansible all -m ping ### will ping all hosts from /etc/ansible/hosts file

###************CONNECT REMOTE HOSTS WITH ANSIBLE CONTROLLER END****************


###************TEST REMOTE HOST CONNECTION WITH ANSIBLE CONTROLLER****************



###********************MISC*************************
### server details

uname -a

### list repos in server

yum repolist

### validate ansible installation

rpm -qa | grep ansible

###open ansible package 

rpm -ql <package name> | more
rpm -ql ansible-2.9.7-1.el8.noarch | more

