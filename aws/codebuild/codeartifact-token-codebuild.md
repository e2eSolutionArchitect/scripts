
## Pass an auth token using an environment variable refer https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html
### macOS or Linux:

export CODEARTIFACT_TOKEN=`aws codeartifact get-authorization-token --domain my-domain --domain-owner domain-owner-id --query authorizationToken --output text`

### Windows (using default command shell):

for /f %i in ('aws codeartifact get-authorization-token --domain my-domain --domain-owner domain-owner-id --query authorizationToken --output text') do set CODEARTIFACT_TOKEN=%i

### Windows PowerShell:

$env:CODEARTIFACT_TOKEN = aws codeartifact get-authorization-token --domain my-domain --domain-owner domain-owner-id --query authorizationToken --output text

