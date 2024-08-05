*******Angular Notes *******
// start angular app
npm start // or you can do ng serve

// run below command if you get ".ps1 cannot be loaded because the execution of scripts is disabled on this system"
powershell Set-ExecutionPolicy RemoteSigned
powershell Set-ExecutionPolicy Restricted
powershell Get-ExecutionPolicy -List

The @angular/material package provides the components of the Material Design, @angular/cdk is a component development kit that is needed for the Material components to work and hammerjs is a library that provides smooth animations for the component. @angular/flex-layout provides a flexible and responsive grid. It is independent of the Material components but is often used together with it.

ng add @angular/material
npm i @angular/flex-layout
npm i hammerjs

Angular-cli from css to scss

//https://stackoverflow.com/questions/40726081/angular-cli-from-css-to-scss/45255290

Change the default style extension to scss
Manually change in .angular-cli.json (Angular 5.x and older) or angular.json (Angular 6+) or run:

ng config defaults.styleExt=scss
if you get an error: Value cannot be found. use the command:

ng config schematics.@schematics/angular:component.styleext scss

Experimental support for decorators is a feature that is subject to change in a future release. Set the 'experimentalDecorators' option in your 'tsconfig' or 'jsconfig' to remove this warning.ts(1219)
Soluntion: in VS Code 
File -> Preferences -> Settings
find experimentalDecorators and enable experimentalDecorators 

// mat icons https://klarsys.github.io/angular-material-icons/

Error: Angular JIT compilation failed: '@angular/compiler' not loaded!
  - JIT compilation is discouraged for production use-cases! Consider AOT mode instead.
  Solution:
  Turn off the AOT by changing "aot": true to "aot: false in angular.json file. I would not recommend this as this improves the performance of the Angular app and improves the catching of error codes in development mode.
  
## for Angular Firebase installation

npm install -g firebase-tools
npm install firebase @angular/fire
firebase login --reauth

Build Production mode:
You can build your application in production mode by running command:
ng build --prod

When application is built for production mode then environments/environment.ts file gets replaced with environments/environment.prod.ts file. Hence if you are referring to settings from environment.ts file in your code, you don’t have to put any if condition or hard code production URL.

