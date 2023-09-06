import boto3
from datetime import datetime
import json

def lambda_handler(event, context):
    now = datetime.now()
    current_time = now.strftime("%d %B %Y, %H:%M:%S %p")
    ts= datetime.timestamp(now)
    print(current_time)
    print(ts)
    
    # Set up SQS client
    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-1.amazonaws.com/306442480424/scanning-queue'
    message_body ={
        'fileName': 'test.txt',
        'fileKey': 'upload',
        'scanStatus': 'WAITING', # 'WAITING','SCANNING', 'SCANNED',
        'waitingStartTime': current_time,
        'scanningStartTime': current_time,
        'scanningEndTime': current_time
        }
    
    # Message to be sent to SQS queue
    #message_body = "Hello, this is a test message sent at current time "+current_time
    
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
    
    return {
        'statusCode': 200,
        'MessageId': response['MessageId'],
        'body': 'Message sent to SQS: '+json.dumps(message_body, indent = 4)
    }
