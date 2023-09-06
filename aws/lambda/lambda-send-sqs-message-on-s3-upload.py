import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    try:
        print(event)
        print(event['Records'])
        for record in event['Records']:
            event_time = record['eventTime']
            source_bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            size = record['s3']['object']['size']
            source_ip_address = record['requestParameters']['sourceIPAddress']
            print(event_time)
            print(source_bucket)
            print(key)
            print(size)
            print(source_ip_address)
        
    except ClientError as e:
        response = {
            'statusCode': e.response['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps('Error uploading file: ' + e.response['Error']['Message'])
        }
    return {
        'statusCode': 200,
        'body': 'Message has been sent to SQS'
    }
