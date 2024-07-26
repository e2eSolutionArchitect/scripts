import json
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config
import logging

config = Config(signature_version='s3v4')
s3 = boto3.client('s3', config=config)

def lambda_handler(event, context):
    try:
        response =""
        bucket = 'e2esa-mybucket-us-east-1'
        key='upload/test.jpg'
        response = s3.put_object_tagging(
            Bucket=bucket,
            Key=key,    
            Tagging={
                "TagSet": [
                    {"Key": "requestid", "Value": "oldvalue"},{"Key": "newkey", "Value": "value2"}
                ]
            }
        )
        print(response)
        get_tags_response = s3.get_object_tagging(
            Bucket=bucket,
            Key=key, 
        )
        print(get_tags_response)
        # Add user-defined Metadata to S3 object
        s3_client = boto3.resource('s3')
        s3_object = s3_client.Object(bucket, key)
        s3_object.metadata.update({'myid':'myvalue'})
        s3_object.copy_from(CopySource={'Bucket':bucket, 'Key':key}, Metadata=s3_object.metadata, MetadataDirective='REPLACE')

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
        'body': response
    }
