## login to your VM instance
## Change the user to sudo 

sudo su -

## create an user 

useradd -d /home/awstechguide -m awstechguide

## create password for this user. a non expiry password

passwd awstechguide
passwd -x -1 awstechguide
