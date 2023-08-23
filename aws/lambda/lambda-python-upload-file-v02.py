import os
import json
import boto3
from botocore.exceptions import ClientError
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        file_content = event['body-json']
        content_decoded=base64.b64decode(file_content)
        
        filename = event['params']['header']['filename']
        print(f"filename: {filename}")
        bucket_name = 'e2esa-demo'  
        #file_key = 'upload/' + event['filename'] 
        file_key = 'upload/' + filename  
        
        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_key, Body=content_decoded)
        
        response = {
            'statusCode': 200,
            'body': json.dumps('File uploaded successfully')
        }
        
    except ClientError as e:
        response = {
            'statusCode': e.response['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps('Error uploading file: ' + e.response['Error']['Message'])
        }
    
    return response
