import os
import json
import boto3
from botocore.exceptions import ClientError
import base64
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        file_content = event['body-json']
        content_decoded=base64.b64decode(file_content)
        
        filename = event['params']['header']['filename']
        print(f"filename: {filename}")
        bucket_name = 'e2esa-demo'  
        file_key = 'upload/' + filename  
        
        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_key, Body=content_decoded)
        # send message to SQS
        send_msg = send_sqs_message(filename)
        if send_msg.statusCode==200:
            print(f"sqs message status: {send_msg.statusCode}")
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

def send_sqs_message(data):
    try:
        # Set up SQS client
        sqs = boto3.client('sqs')
        queue_url = 'https://sqs.us-east-1.amazonaws.com/306442480424/scanning-queue'
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S %p")
        
        # Message to be sent to SQS queue
        message_body = "File "+data+" has been sent for scanning at "+current_time
        
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageAttributes={
                'Service': {
                    'DataType': 'String',
                    'StringValue': 'ClamAV scanning'
                },
                'Author': {
                    'DataType': 'String',
                    'StringValue': 'John Doe'
                },
                'CreatedOn': {
                    'DataType': 'String',
                    'StringValue': current_time
                }
            },
            MessageBody=message_body
        )
        
        print(f"MessageId: {response['MessageId']}")
    except ClientError as e:
        response = {
            'statusCode': e.response['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps('Error uploading file: ' + e.response['Error']['Message'])
        }
    
    return response