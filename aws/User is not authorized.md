I was actually getting this issue while trying to provision any resources from AWS CLI (using terraform) and having MFA enabled. 
It use to show an encrypted message so first decode the message to read it. 

User: xxx is not authorized to perform: xxx with an explicit deny in an indentity-based policy 

Ensure you have 'aws configure' done with valid access credentials.

Step 1:
Decode the error message by below sts command

aws sts decode-authorization-message --encoded-message <copy-the encoded-message-here>

It will show detail decoded message. 


Step 2: In Decoded message if you find BlockMostAccessUnlessSignedInWithMFA, it means you have your MFA enabled and while using CLI commands you have to use your MFA to generate sessio token

to generate session token run below command 

aws sts get-session-token --serial-number <enter-arn-of-your-mfa> --token-code <enter-code-from-your-authenticator-device>

aws sts get-session-token --serial-number arn:aws:iam::<aws-account-id>:mfa/<username> --token-code 000000

It will give an output with credentials AccessKeyId, SecretAccessKey, SessionToken

Step 3:
  
If you are using windows, browse to you user directory > .aws then open the 'credentials' in notepad. 
replace the existing values of AccessKeyId, SecretAccessKey with Step 2 output. and add one more line as below 

aws_session_token= <token from step 2 output>

save the file. and executing your aws command in cli 

Remember that Step 2 token is valid for a finite time only. Once it expires you have to generate it same way. 


****After the token expires when regenerating the token ***********
Step A: Reset the AccessKeyId, SecretAccessKey values with your original values (the actual values from your IAM record)
Step B: start  from Step 1 above. 

Note: If you miss Step A aws sts get-session-token  .. command will show error saying invalid credentials , That's why you have to add oroginal credentials back. 
