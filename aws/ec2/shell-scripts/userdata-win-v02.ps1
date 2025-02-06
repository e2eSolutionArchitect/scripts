<powershell>
$LogFile= "C:\log.txt"
New-Item -Path $LogFile -ItemType File -Value "User Data Script starting---------------"

"Input: secretname_app - $secretname_app"  >> $LogFile
"Input: secretname_users - $secretname_users"  >> $LogFile
"Input: region - $region"  >> $LogFile

$Region = "us-east-1"

# Updating metadata for IMDSv2
#Edit-EC2InstanceMetadataDefault -Region $Region -HttpToken "required" -HttpPutResponseHopLimit 2 -InstanceMetadataTags "enabled"

Get-EC2InstanceMetadataDefault -Region $Region | Format-List >> $LogFile

# Fetch metadata values
$InstanceId = Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/instance-id
$AZ = Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/placement/availability-zone

$Environment = "dev"
# SNS Topic ARN
$SNSTopicArn = "arn:aws:sns:us-east-1:00000000000:demo-app-dev-ec2-failure-alert-topic"

$SecretName = "development/app/infra"
$UserSecretName = "development/app/users"

"Param: InstanceId - $InstanceId"  >> $LogFile
"Param: AZ - $AZ"  >> $LogFile
"Param: Environment - $Environment"  >> $LogFile
"Param: Region - $Region"  >> $LogFile
"Param: LogFile - $LogFile"  >> $LogFile
"Param: SNSTopicArn - $SNSTopicArn"  >> $LogFile
"Param: SecretName - $SecretName"  >> $LogFile
"Param: UserSecretName - $UserSecretName"  >> $LogFile

# Generate a unique hostname
$NewHostname = "demo-app-$Environment-" + $InstanceId.Substring($InstanceId.Length - 4)

"Renaming host to $NewHostname------"  >> $LogFile

# Get the current hostname
$CurrentHostname = hostname

# Check if hostname is already set
if ($CurrentHostname -ne $NewHostname) {


    $CurrentHostname >> $LogFile
    Write-Host "Updating hostname to $NewHostname..."
    Rename-Computer -NewName $NewHostname -Force

    # Mark the instance as updated to prevent re-execution on reboot
    New-Item -Path "C:\Windows\Setup\Scripts\hostname_set.txt" -ItemType File

    # Update EC2 Name Tag to match the hostname
    Write-Host "Updating EC2 Name tag to $NewHostname..."
    aws ec2 create-tags --resources $InstanceId --tags Key=Name,Value=$NewHostname
    "EC2 Name tag updated successfully to $NewHostname..." >> $LogFile

    # Restart to apply the hostname change
    "Restarting to apply the hostname change------"  >> $LogFile
    Restart-Computer -Force
} else {
    Write-Host "Hostname is already set. No changes needed."
   "Hostname is already set. No changes needed." >> $LogFile
}
"End: Renaming host------"  >> $LogFile

# --------- Creating Route53 Rocord ------
$DomainName = "demo.internal.com"
$HostedZoneId = "GFH435DFG#$%"  # Replace with your Route 53 Hosted Zone ID
$Hostname = $NewHostname              

# Install AWS CLI (if not already installed)
if (-Not (Get-Command aws -ErrorAction SilentlyContinue)) {
    Write-Output "Installing AWS CLI..."
    $msiPath = "$env:TEMP\awscli.msi"
    Invoke-WebRequest -Uri "https://awscli.amazonaws.com/AWSCLIV2.msi" -OutFile $msiPath
    Start-Process -FilePath "msiexec.exe" -ArgumentList "/i $msiPath /quiet" -Wait
    Remove-Item -Path $msiPath -Force
}

# Configure AWS CLI with the instance's IAM role
Write-Output "Configuring AWS CLI..."
aws configure set default.region us-east-1  # Replace with your region

# Get the instance's private IP address
$PrivateIP = Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/local-ipv4

# Create the A record in Route 53
"Creating A record for $Hostname.$DomainName with IP $PrivateIP..."  >> $LogFile

# Construct the JSON for the change-batch
$ChangeBatch = @"
{
    "Changes": [
        {
            "Action": "UPSERT",
            "ResourceRecordSet": {
                "Name": "$Hostname.$DomainName",
                "Type": "A",
                "TTL": 300,
                "ResourceRecords": [
                    {
                        "Value": "$PrivateIP"
                    }
                ]
            }
        }
    ]
}
"@

# Save the JSON to a temporary file
$TempFile = "$env:TEMP\change-batch.json"
$ChangeBatch | Out-File -FilePath $TempFile -Encoding ASCII

# Update Route 53 with the new A record
aws route53 change-resource-record-sets --hosted-zone-id $HostedZoneId --change-batch file://$TempFile

# Clean up the temporary file
Remove-Item -Path $TempFile -Force

"A record created successfully for $Hostname.$DomainName."  >> $LogFile
# ----------Route53 record end ----------


try {
    $SecretValue = Get-SECSecretValue -SecretId $SecretName -Region $Region
    $SecretJson = ($SecretValue.SecretString | ConvertFrom-Json)
    
    ($SecretValue.SecretString | ConvertFrom-Json) >> $LogFile
       
    "Start: Bot script------"  >> $LogFile
    
    $bucketName = $SecretJson.s3BucketName
    $objectKey1 = $SecretJson.ObjectKeyName
    $localPath = "C:"
    $filePath1 = "C:\$objectKey1"
    aws s3 cp "s3://$bucketName/$objectKey1" $filePath1
} catch {
    Write-Host "Failed to fetch devices: $($_.Exception.Message)"
	"Failed to fetch devices at step 8: $($_.Exception.Message)" >> $LogFile

    # Capture the error message
    $ErrorMessage = "Environment: $Environment , Instance ID: $InstanceId failed in AZ: $AZ for Error: $($_.Exception.Message)"
    Write-Host "ERROR: $ErrorMessage"

    # Send error notification to SNS before termination
    Write-Host "Sending failure notification to SNS..."
    #aws sns publish --topic-arn $SNSTopicArn --message "$ErrorMessage" --subject "app bot failure alert in $Environment environment for instance $InstanceId"

    # Terminate the instance on failure
    Write-Host "Terminating instance due to failure..."
    #aws ec2 terminate-instances --instance-ids $InstanceId

    # Wait a bit before instance terminates
    #Start-Sleep -Seconds 30

    exit
}


$SecretValue = Get-SECSecretValue -SecretId $UserSecretName -Region $Region
$UserList = ($SecretValue.SecretString | ConvertFrom-Json).users

# Iterate through the list of users and create each one
foreach ($User in $UserList) {
    $Username = $User.username
    $Password = $User.password

    if (-not (Get-LocalUser -Name $Username -ErrorAction SilentlyContinue)) {
        
        New-LocalUser -Name $Username -Password (ConvertTo-SecureString $Password -AsPlainText -Force) -FullName "$Username Account" -Description "Created via User Data Script"

        Add-LocalGroupMember -Group "Administrators" -Member $Username
        Add-LocalGroupMember -Group "Remote Desktop Users" -Member $Username

        Set-LocalUser -Name $Username -PasswordNeverExpires $false

        Write-Output "User $Username created successfully and will reset password on first login."
    } else {
        Write-Output "User $Username already exists, skipping creation."
    }
}

Get-LocalUser >> $LogFile
Get-LocalGroupMember -Group "Remote Desktop Users" >> $LogFile

"Script completed ------------" >> $LogFile
</powershell>
<persist>true</persist>

