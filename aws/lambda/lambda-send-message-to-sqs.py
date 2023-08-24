import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Set up SQS client
    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-1.amazonaws.com/306442480424/scanning-queue'
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    
    # Message to be sent to SQS queue
    message_body = "Hello, this is a test message sent at current time "+current_time
    
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
    
    return {
        'statusCode': 200,
        'body': 'Message sent to SQS'
    }
