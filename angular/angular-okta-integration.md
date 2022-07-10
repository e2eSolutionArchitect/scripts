Please refer https://d28m3l9ryqsunl.cloudfront.net/docs/guides/sign-into-spa-redirect/angular/main/
Very useful link for Angular and Okta integration. The content has been copied below as the above link is cloudfront link. Primarily use the above link for any updated content. 

Sign users in to your SPA using the redirect model
Add authentication with Okta's redirect model (opens new window)to your single-page app. This example uses Okta as the user store.

Learning outcomes

Create an integration that represents your app in your Okta org.
Add dependencies and configure your app to use Okta redirect authentication.
Add sign-in and sign-out actions.
Require authentication on protected routes.
Get authenticated user info.
Make an HTTP call with the access token.
Check the integration by signing in a user.
Sample code

Quickstart sample app(opens new window)

Note: For server-side web apps, see Sign users in to your web app using the redirect model instead. To protect the API your SPA calls, see Protect your API endpoints.

Set up Okta
Set up your Okta org. The CLI is the quickest way to work with your Okta org, so we recommend using it for the first few steps. If you don't want to install the CLI, you can manually sign up for an org (opens new window)instead. We provide non-CLI instructions along with the CLI steps below.

Install the Okta command-line interface: Okta CLI (opens new window).

If you don't already have a free Okta developer account, create one by entering okta register on the command line.

Make a note of the Okta Domain as you need that later.

IMPORTANT: Set the password for your Okta developer org by opening the link that's shown after your domain is registered. Look for output similar to this:

```
Your Okta Domain: https://dev-xxxxxxx.okta.com
To set your password open this link:
https://dev-xxxxxxx.okta.com/welcome/xrqyNKPCZcvxL1ouKUoh
```
Note: If you don't receive the confirmation email sent as part of the creation process, check your spam filters for an email from noreply@okta.com

Connect to your Okta developer org if you didn't create one in the last step (successfully creating an Okta org also signs you in) by running the following command. You need the URL of your org — which is your Okta domain with https:// prepended — and an API/access token:

okta login
Create an Okta integration for your app
An application integration represents your app in your Okta org. The integration configures how your app integrates with the Okta services including: which users and groups have access, authentication policies, token refresh requirements, redirect URLs, and more. The integration includes configuration information required by the app to access Okta.

To create your app integration in Okta using the CLI:

Create the app integration by running:

okta apps create spa
Enter Quickstart when prompted for the app name.

Specify the required redirect URI values:
Redirect URI: http://localhost:4200/login/callback
Post Logout Redirect URI(s): select the default option, http://localhost:4200

Make note of the application configuration printed to the terminal as you use the Client ID and Issuer to configure your SPA.

At this point, you can move to the next step: Creating your app. If you want to set up the integration manually, or find out what the CLI just did for you, read on.

Sign in to your Okta organization (opens new window)with your administrator account.
Click Admin in the upper-right corner of the page.
Open the Applications page by selecting Applications > Applications.
Click Create App Integration.
Select a Sign-in method of OIDC - OpenID Connect.
Select an Application type of Single-Page Application, then click Next.
Note: If you choose an inappropriate application type, it can break the sign-in or sign-out flows by requiring the verification of a client secret, which is something that public clients don't have.

Enter an App integration name.
Select Authorization Code and Refresh Token as the Grant type. This enables the Authorization Code flow with PKCE for your application and the ability to refresh the access token when it expires without prompting the user to re-authenticate.
Enter the Sign-in redirect URIs for both local development, such as http://localhost:xxxx/login/callback, and for production, such as https://app.example.com/login/callback.
Select the type of Controlled access for your app in the Assignments section. You can allow all users to have access or limit access to individuals and groups. See the Assign app integrations (opens new window)topic in the Okta product documentation.
Click Save to create the app integration and open its configuration page. Keep this page open as you need to copy some values in later steps when configuring your app.
On the General tab, scroll to General Settings and click Edit.
Verify that Refresh Token is selected as a Grant type. In the Refresh Token section, refresh token rotation is automatically set as the default refresh token behavior.
Note: The default number of seconds for the Grace period for token rotation is set to 30 seconds. You can change the value to any number between 0 and 60 seconds. After the refresh token is rotated, the previous token remains valid for this amount of time to allow clients to get the new token. Using a value of 0 indicates that there is no grace period. However, a grace period of 0 doesn't necessarily mean that the previous refresh token is immediately invalidated. That token is invalidated after the new one is generated and returned in the response.

In the Login section, specify an Initiate login URI to have Okta initiate the sign-in flow. When Okta redirects to this URI (for example, https://example.com:xxxx/login), the client is triggered to send an authorize request. This URI is also used when users reset their passwords while signing in to the app. Okta redirects the user back to this URI after the password is reset so that the user can continue to sign in.
Click Save.
Enable Trusted Origins
Reduce possible attack vectors by defining Trusted Origins, which are the websites allowed to access the Okta API for your app integration. Cross-Origin Resource Sharing (CORS) enables JavaScript requests using XMLHttpRequest with the Okta session cookie. For information on enabling CORS, see Grant cross-origin access to websites.

Note: To reduce risk, only grant access to the Okta API to specific websites (origins) that you both control and trust.

To set trusted origins manually, add the Base URIs for local development, such as http://localhost:xxxx, and for production, such as https://app.example.com. These URIs are added as trusted origins in your Okta org and you can manage them by navigating to Security > API and selecting the Trusted Origins tab. See Enable Trusted Origins.

Create app
In this section you create a sample SPA and add redirect authentication using your new Okta app integration.

Create a new project
You need recent versions of Node (opens new window)and npm (opens new window). We also recommend installing the Angular CLI (opens new window).

Create an Angular application named okta-angular-quickstart with routing in your current directory using the following command. Choose CSS when it asks you what stylesheet format you want to use.

```
npx @angular/cli@13 new okta-angular-quickstart --routing
```
This creates an Angular application using version 13 regardless of the version of the Angular CLI installed on your system.

Note: This guide uses Angular CLI v13, ``` okta-angular v5.1.1, and okta-auth-js v6.0.0. ```

Note: You can also install the Okta CLI and run okta start angular to download and configure an Angular app with Okta integrated. This quickstart uses the basic Angular CLI output instead, as it's easier to understand the Okta-specific additions if you work through them yourself.

Add packages
Add the required dependencies for using the Okta SDK to your SPA.

Use Okta's Angular SDK and Okta's JavaScript SDK in your Angular application. Add the npm packages by running the following commands.
```
cd okta-angular-quickstart
npm install @okta/okta-angular@5.1 @okta/okta-auth-js@6.0
```
Configure your app
Our app uses information from the app integration that we created earlier to configure communication with the API: Client ID and Issuer.

The Okta Angular SDK requires an instance of an OktaAuth object with configuration properties. You should set the clientID and issuer properties with the values you got from the CLI earlier. This can happen by directly setting the properties, with variable replacement that happens as part of the build process, or during application load time.

Make the following changes to src/app/app.module.ts:

Add the following import lines to the code to pull in the dependencies:
```
import { OktaAuthModule, OKTA_CONFIG } from '@okta/okta-angular';
import { OktaAuth } from '@okta/okta-auth-js';
```
Add OktaAuthModule to the @NgModule imports array.

Add a new OktaAuth object like the one below, replacing the placeholder values with your own values:
```
const oktaAuth = new OktaAuth({
  issuer: 'https://${yourOktaDomain}/oauth2/default',
  clientId: '${yourClientID}',
  redirectUri: window.location.origin + '/login/callback'
});
```
Add ```{ provide: OKTA_CONFIG, useValue: { oktaAuth } } ``` to the providers array to add the Okta services to the dependency injection system. The Okta Angular SDK provides the OKTA_CONFIG injection token.

Find your config values
If you don't have your configuration values handy, you can find them in the Admin Console (choose Applications > Applications and find your app integration that you created earlier):

Client ID: Found on the General tab in the Client Credentials section.
Issuer: Found in the Issuer URI field for the authorization server that appears by selecting Security > API from the left navigation pane.
Redirect to the sign-in page
To sign a user in, your web app redirects the browser to the Okta-hosted sign-in page. This usually happens from a sign-in action, such as clicking a button or when a user visits a protected page.

Note: The sign-out action requires your app to be listed as a trusted origin. The Okta CLI sets this up for you, but if you used the Okta dashboard, follow the steps to add your app as a trusted origin.

The OktaAuthStateService and OktaAuth services are used together to support sign-in and sign-out actions. The OktaAuthStateService contains authState$, an RxJS Observable (opens new window)that you can use to get the current authenticated state.

The OktaAuth service has methods for sign-in and sign-outactions.

Add buttons, to support sign-in and sign-out actions, to the component template (app.component.html), just inside the top of <div class="toolbar" role="banner"></div> so that they are visible. Display either the sign-in or sign-out button based on the current authenticated state.

```
<ng-container *ngIf="(isAuthenticated$ | async) === false; else signout">
  <button (click)="signIn()"> Sign in </button>
</ng-container>

<ng-template #signout>
  <button (click)="signOut()">Sign out</button>
</ng-template>
```
Update the component TypeScript file (app.component.ts) with the following imports and updated export to get authenticated state and support sign-in and sign-out actions.

```
import { Component, Inject, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { OktaAuthStateService, OKTA_AUTH } from '@okta/okta-angular';
import { AuthState, OktaAuth } from '@okta/okta-auth-js';
import { filter, map, Observable } from 'rxjs';

export class AppComponent implements OnInit {
  title = 'okta-angular-quickstart';
  public isAuthenticated$!: Observable<boolean>;

  constructor(private _router: Router, private _oktaStateService: OktaAuthStateService, @Inject(OKTA_AUTH) private _oktaAuth: OktaAuth) { }

  public ngOnInit(): void {
    this.isAuthenticated$ = this._oktaStateService.authState$.pipe(
      filter((s: AuthState) => !!s),
      map((s: AuthState) => s.isAuthenticated ?? false)
    );
  }

  public async signIn() : Promise<void> {
    await this._oktaAuth.signInWithRedirect().then(
      _ => this._router.navigate(['/profile'])
    );
  }

  public async signOut(): Promise<void> {
    await this._oktaAuth.signOut();
  }
}
```
During the sign-in flow, the user is redirected to the hosted sign-in page where they authenticate. After successful authentication, the browser is redirected back to your application along with information about the user.

Note: To customize the hosted sign-in page, see Style the Okta-hosted Sign-In Widget.

Handle the callback from Okta
After Okta authenticates a user, they're redirected back to your application through the callback route that you define. When Okta redirects back, the URL query string contains a short-lived code that is exchanged for a token. The SDK does this for you with its callback component.

The Okta Angular SDK has a callback component that handles the token exchange. We use this inside app-routing.module.ts to handle the callback routing.

Import the component with the following line:

```
import { OktaCallbackComponent } from '@okta/okta-angular';
```
Add a new route for the callback to the routes array. The path should match the path provided in the redirectUri property when you configure the OktaAuth instance in app.module.ts.

```
{ path: 'login/callback', component: OktaCallbackComponent }
```
Get info about the user
After the user signs in, Okta returns some of their profile information to your app (see /userinfo response example). You can use this information to update your UI, for example to show the customer's name.

The default profile items (called claims) returned by Okta include the user's email address, name, and preferred username. The claims that you see may differ depending on what scopes your app has requested. See Configure packages.

The authState$ subject in OktaAuthStateService contains an idToken that contains the user profile claims. You can access it to display a welcome message as shown in the ProfileComponent.

Create a new component called profile using the CLI command ng generate component profile.

Update profile.component.ts as follows:

```
import { Component, OnInit } from '@angular/core';
import { OktaAuthStateService } from '@okta/okta-angular';
import { filter, map, Observable } from 'rxjs';
import { AuthState } from '@okta/okta-auth-js';

@Component({
  selector: 'app-profile',
  template: `
  <div class="profile-card">
    <div class="shield"></div>
    <p *ngIf="name$ | async as name">
        Hello {{name}}!
    </p>
  </div>
  `,
  styleUrls: ['./profile.component.css']
})

export class ProfileComponent implements OnInit {

  public name$!: Observable<string>;

  constructor(private _oktaAuthStateService: OktaAuthStateService) { }

  public ngOnInit(): void {
    this.name$ = this._oktaAuthStateService.authState$.pipe(
      filter((authState: AuthState) => !!authState && !!authState.isAuthenticated),
      map((authState: AuthState) => authState.idToken?.claims.name ?? '')
    );

  }
}
```
Add an instance of the <app-profile></app-profile> component into app.component.html, again inside the toolbar. This displays a message with your name after you are signed in.

Note: To get user information beyond the default profile claims, you can call the /userinfo endpoint, or call the getUser() method in OktaAuth.

Sign in a user
Test your integration by starting your server and signing in a user.

Start the Angular app by serving locally.

ng serve
You should be able to sign-in, view your name, and sign-out.

Configure required authentication
Your app can require authentication for everything or just for specific routes. Routes that don't require authentication are accessible without signing in, which is also called anonymous access.

Require authentication for everything
Some apps requires that the user be authenticated for all routes, for example a company intranet.

The Okta Angular SDK has a guard to check for the authenticated state that you can add to protected routes. It's common in Angular to use feature modules and protect the route to the feature so that all child routes are also guarded.

In app-routing.module.ts, add the OktaAuthGuard to protect the route accessing a feature module using the canActivate property.

Update the Okta import statement to:

```
import { OktaAuthGuard, OktaCallbackComponent } from '@okta/okta-angular';
Add the following route to the routes array:

{
  path: 'protected',
  loadChildren: () => import('./protected/protected.module').then(m => m.ProtectedModule),
  canActivate: [OktaAuthGuard]
},
```
Create a new protected module with the CLI command ng generate module protected.

Make sure that you are signed out, and then try navigating to /protected. You are automatically redirected to the Okta sign-in page. Any child routes are also protected.

Require authentication for a specific route
Your website may enable users to find some initial information but require a user to sign in or take some action for more information. For example, an ecommerce site can allow a user to browse anonymously and even to add items to a cart. However, checking out requires the user to sign in.

The OktaAuthGuard can protect a route to a single component as well.

```
Import the ProfileComponent component into app-routing.module.ts:

import { ProfileComponent } from './profile/profile.component';
Add the following to the routes array:

{ path: 'profile', component: ProfileComponent, canActivate: [OktaAuthGuard] }
```
This single /profile route is now protected.

Use the access token
SPAs need to send requests to one or more APIs to perform actions and retrieve information.

After a user signs in, your application stores an access token issued by Okta. By attaching this token to outgoing requests, your APIs can authenticate them (ensure that the user is signed in to perform an action) and authorize them (ensure that the user is allowed to do an action).

On your front-end (this SPA), make sure that you place the access token in the HTTP Authorization header of outgoing requests using this format:

Authorization: Bearer ${token}
On your back-end (the API), make sure that you check for valid tokens in incoming requests. See Protect your API endpoints.

The recommended way to add your access token to HTTP calls in Angular is to use an interceptor. To follow security best practices, the access token should only be added on calls to allowed origins.

Create an Angular interceptor (opens new window)called auth.interceptor, using the CLI command ng generate interceptor auth.

Add the following imports into app.module.ts:
```

import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AuthInterceptor } from './auth.interceptor';
Register the interceptor in app.module.ts by adding the following into the providers array:

{ provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
Update auth.interceptor.ts to add the access code when calling a trusted origin:

import { Inject, Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { OKTA_AUTH } from '@okta/okta-angular';
import { OktaAuth } from '@okta/okta-auth-js';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(@Inject(OKTA_AUTH) private _oktaAuth: OktaAuth) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    return next.handle(this.addAuthHeaderToAllowedOrigins(request));
  }

  private addAuthHeaderToAllowedOrigins(request: HttpRequest<unknown>): HttpRequest<unknown> {
    let req = request;
    const allowedOrigins = ['http://localhost'];
    if (!!allowedOrigins.find(origin => request.url.includes(origin))) {
      const authToken = this._oktaAuth.getAccessToken();
      req = request.clone({ setHeaders: { 'Authorization': `Bearer ${authToken}` } });
    }

    return req;
  }
}
```
When making HTTP calls within allowed origins, you should now see the Authorization header.

To enable access token renewal you must obtain a refresh token. See Get a refresh token with the code flow.

Alternatively, you can renew tokens by hitting the /authorize endpoint. See Get a new access token/ID token silently for your SPA .

Next steps
Learn more about session management, securing your APIs, and ways that you can integrate with Okta.

To protect the API that your SPA calls, see Protect your API endpoints
To customize your Okta org domain name, see Customize the Okta URL and email notification domains(opens new window)
To customize the hosted sign-in page, see Style the Okta-hosted Sign-In Widget
For resources to create a fully customized sign-in experience, see Languages & SDKs Overview(opens new window)
To secure your mobile app, see Sign users in to your mobile app using the redirect model
To support multi-tenancy, see Multi-tenant solutions(opens new window)
Angular documentation:

See Get started with Angular (opens new window)to learn about the framework from Angular's official documentation.

Okta Developer Blog:

Build a Beautiful App + Login with Angular Material(opens new window)
How to Customize Your Angular Build with Webpack(opens new window)
Use the Okta CLI to Quickly Build Secure Angular Apps(opens new window)
Loading Components Dynamically in an Angular App
