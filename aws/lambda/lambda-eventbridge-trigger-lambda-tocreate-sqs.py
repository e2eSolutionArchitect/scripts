import boto3
import json
from botocore.exceptions import ClientError
from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    current_time = now.strftime("%d %B %Y, %H:%M:%S %p")
    print(event)
    try:
        event_time = event['time']
        print(event_time)
        print(event['detail'])
        source_bucket = event['detail']['bucket']['name']
        print(source_bucket)
        file_name = event['detail']['object']['key']
        print(file_name)
        size = event['detail']['object']['size']
        print(size)
        source_ip_address = event['detail']['source-ip-address']
        message_body ={
            'fileName': file_name,
            'fileSize': size,
            'sourceBucket': source_bucket,
            'sourceIPAddress': source_ip_address,
            'uploadTime': event_time,
            'timeStamp': current_time
            }
            
        # Set up SQS client
        sqs = boto3.client('sqs')
        queue_url = 'https://sqs.us-east-1.amazonaws.com/306442480424/clamav-waiting-queue'
        
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
            MessageBody=json.dumps(message_body, indent = 4) 
        )
        
        print(f"MessageId: {response['MessageId']}")
        
    except ClientError as e:
        response = {
            'statusCode': e.response['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps('Error uploading file: ' + e.response['Error']['Message'])
        }
    return {
        'statusCode': 200,
        'MessageId': response['MessageId'],
        'body': 'Message has been created in SQS queue'
    }
