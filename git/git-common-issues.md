
## Git common issues

### fatal: unable to access <repo link> : could not load PEM client certificate, OpenSSL error error:02001002:system library:fopen:No such file or directory, ...

### check you git config and remove hhtp.sslcert record from there (if its there)

got config -l --show-origin
git config --global --unset http.sslCert


### configure username and email globally 

git config --global user.name=youname
git config --global user.email=your@email

### ignore ssl for git 

git config --global http.sslverify=false
