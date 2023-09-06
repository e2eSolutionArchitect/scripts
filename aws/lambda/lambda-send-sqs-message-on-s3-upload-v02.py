import boto3
import json
from botocore.exceptions import ClientError
from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    current_time = now.strftime("%d %B %Y, %H:%M:%S %p")
    try:
        for record in event['Records']:
            event_time = record['eventTime']
            source_bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            size = record['s3']['object']['size']
            source_ip_address = record['requestParameters']['sourceIPAddress']
            message_body ={
                'fileName': key,
                'fileSize': size,
                'sourceBucket': source_bucket,
                'sourceIPAddress': source_ip_address,
                'scanStatus': 'WAITING', # 'WAITING','SCANNING', 'SCANNED',
                'uploadEventTime': event_time,
                'waitingStartTime': current_time,
                'scanningStartTime': current_time,
                'scanningEndTime': current_time
                }
            
        # Set up SQS client
        sqs = boto3.client('sqs')
        queue_url = 'https://sqs.us-east-1.amazonaws.com/306442480424/scanning-queue'
        
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
        'body': 'Message has been created in SQS'
    }
