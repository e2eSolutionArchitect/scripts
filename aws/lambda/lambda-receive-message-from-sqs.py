import boto3
import json

def lambda_handler(event, context):
    # Set up SQS client
    sqs = boto3.client('sqs')
    queue_url='https://sqs.us-east-1.amazonaws.com/306442480424/scanning-queue'
    
    # Receive messages from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=60,  
        WaitTimeSeconds=10     
    )
    
    # Check if messages were received
    if 'Messages' in response:
        #print(response['Messages'])
        for message in response['Messages']:
            message_body = message['Body']
            receipt_handle = message['ReceiptHandle']
            message_id= message['MessageId']
            
            #print(f"Received message: {message_body}")
            print(json.loads(message_body))
            
            # Add processing logic here
            
            # Delete the message from the queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            
            print(f"Deleted message:"+message_id)
    else:
        print("No messages received from the queue.")
    
    return {
        'statusCode': 200,
        'body': 'Message processing complete for messageId: '+message_id
    }
