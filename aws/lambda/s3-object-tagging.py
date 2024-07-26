import json
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
import logging

config = Config(signature_version='s3v4')
s3 = boto3.client('s3', config=config)

def lambda_handler(event, context):
    try:
        bucket = 'e2esa-facepay-registration-us-east-1'
        key='upload/test.jpg'
        tags_response = s3.put_object_tagging(
            Bucket=bucket,
            Key=key,    
            Tagging={
                "TagSet": [
                    {"Key": "requestid", "Value": "oldvalue"},{"Key": "newkey", "Value": "value2"}
                ]
            }
        )
        print(tags_response)
        get_tags_response = s3.get_object_tagging(
            Bucket=bucket,
            Key=key, 
        )
        print(get_tags_response)
    except ClientError as e:
        logging.error(e)
        return {
            'statusCode': e.args[0],
            'body': json.dumps({'ClientError': str(e)})
        }    
    except Exception as e:
        logging.error(e)
        return {
            'statusCode': e.args[0],
            'body': json.dumps({'error': str(e)})
        }
    
    return {
        'body': tags_response
    }
