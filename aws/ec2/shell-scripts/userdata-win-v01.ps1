<powershell>
$LogFile= "C:\log.txt"
New-Item -Path $LogFile -ItemType File -Value "User Data Script starting---------------"

# For IMDS V2 - use token for metadata access
# Get the session token
$token = Invoke-RestMethod -Uri "http://169.254.169.254/latest/api/token" -Method Put -Headers @{ "X-aws-ec2-metadata-token-ttl-seconds" = "21600" } 
# Access metadata using the session token
$InstanceId = Invoke-RestMethod -Uri "http://169.254.169.254/latest/meta-data/instance-id" -Headers @{ "X-aws-ec2-metadata-token" = $token } 
$AZ = Invoke-RestMethod -Uri "http://169.254.169.254/latest/meta-data/placement/availability-zone" -Headers @{ "X-aws-ec2-metadata-token" = $token }

# Get the instance's private IP address
$PrivateIP = Invoke-RestMethod -Uri "http://169.254.169.254/latest/meta-data/local-ipv4" -Headers @{ "X-aws-ec2-metadata-token" = $token } 
$PublicIP = Invoke-RestMethod -Uri "http://169.254.169.254/latest/meta-data/public-ipv4" -Headers @{ "X-aws-ec2-metadata-token" = $token }

$Environment = "dev"

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
$HostedZoneId = "ASD34234DFSDF"  # Replace with your Route 53 Hosted Zone ID
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



# Create the A record in Route 53
"Creating A record for $Hostname.$DomainName with IP $PublicIP..."  >> $LogFile

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

# "Updating domain name $Env:USERDOMAIN to " >> $LogFile
# $Env:USERDOMAIN =$Hostname.$DomainName
# echo $Env:USERDOMAIN >> $LogFile 

Get-LocalUser >> $LogFile
Get-LocalGroupMember -Group "Remote Desktop Users" >> $LogFile

"Script completed ------------" >> $LogFile
</powershell>
<persist>true</persist>

