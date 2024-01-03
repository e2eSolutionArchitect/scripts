
## Git common issues

### remote: Repository Not found
```
git clone https://myusername:mypassword@github.com/path_to/myRepo.git
OR
git clone https://myusername@github.com/path_to/myRepo.git -- it will open a github login popup. you can enter password or use the option to login via browser.

C:\Som\workspace\terraform>git clone https://github.com/myusername/myrepo.git
Cloning into 'myrepo'... remote: Repository not found.
fatal: repository 'https://github.com/myusername/myrepo.git/' not found

C:\Som\workspace\terraform>git clone https://myusername@github.com/myusername/myrepo.git
Cloning into 'myrepo'... info: please complete authentication in your browser... remote: Enumerating objects: 18, done.
remote: Counting objects: 100% (18/18), done. remote: Compressing objects: 100% (15/15), done.
remote: Total 18 (delta 4), reused 0 (delta 0), pack-reused 0 Receiving objects: 100% (18/18), 4.99 KiB | 1.66 MiB/s, done.
Resolving deltas: 100% (4/4), done.

```

### fatal: unable to access <repo link> : could not load PEM client certificate, OpenSSL error error:02001002:system library:fopen:No such file or directory, ...

### check you git config and remove hhtp.sslcert record from there (if its there)

```
git config -l --show-origin
git config --global --unset http.sslCert
```

### configure username and email globally 
  
```
git config --global user.name=youname
git config --global user.email=your@email
```
### ignore ssl for git 

```
git config --global http.sslverify=false
```
  
  ```
  set no-proxy="abc.com"
  ```

## SSL certificate problem: self signed certificate in certificate chain

```
use http.sslVerify=false
instead
git config --global http.sslVerify false # Do NOT do this!
You should never globally disable TLS(/SSL) certificate verification

Run below command
git -c http.sslVerify=false clone https://github.com/e2eSolutionArchitect/academy.git
```
