## Angular Error and Fix

Error: An unhandled exception occurred: Cannot find module '@angular-devkit/build-angular/package.json'
Fix: Run this , 
```
npm install --save-dev @angular-devkit/build-angular
```

Error: 'ng' is not recognized as an internal or external command
Fix: 
```
npm install -g @angular/cli
```

If error still exists, Go to environment variable > click PATH valiable > add below to values un der PATH then restart terminal
```
%USERPROFILE%\AppData\Roaming\npm
%USERPROFILE%\AppData\Roaming\npm\node_modules\angular-cli\bin
```

Error: Cannot find module '@angular/compiler-cli'
```
rm -r node_modules
npm cache clean --force
install npm
```

### set proxy for git config global
```
git config --global http.proxy "http://abc.com:8080"
```

## set ssl false
```
npm config set strict-ssl false -g
```

## Run npm install with proxy 
```
npm install -g angular/cli --proxy "http://abc.com:8080"
```
