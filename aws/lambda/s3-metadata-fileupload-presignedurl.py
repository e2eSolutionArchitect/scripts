import json
import boto3
from botocore.exceptions import ClientError
import base64
import requests
from datetime import datetime
import os
import logging
from botocore.config import Config

config = Config(signature_version='s3v4')


def lambda_handler(event, context):
    print("environment variable: " + os.environ['S3_BUCKET'])
    bucket = os.environ['S3_BUCKET']
    filename = event['params']['header']['filename']
    cardnumber = event['params']['header']['cardnumber']
    username = event['params']['header']['username']
    key = os.environ['UPLOAD_DIR'] + filename

    now = datetime.now()
    requestid = now.strftime("%m%d%Y%H%M%S")

    print(filename)
    
    s3 = boto3.client('s3', config=config)
    
    file_content = event['content']
    content_decoded=base64.b64decode(file_content)

    
    
    try:
        # Generating presigned url and adding metadata to the object
        metadata = {'Key': 'requestid', 'Value': requestid},{'Key': 'filename', 'Value': filename},{'Key': 'cardnumber', 'Value': cardnumber},{'Key': 'username', 'Value': username}
        presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=360  # 3600 = URL to expire in 1 hour
        )
        print(presigned_url)
        headers = {'Bucket': bucket, 'Key': key}
        response = requests.put(presigned_url, data=content_decoded, headers=headers)
        
        obj = s3.get_object(Bucket=bucket,Key=key)
        
        #response1 = s3.put_object_tagging(Bucket=bucket,Key=key,Tagging={'TagSet': [metadata,]})
        tags_response = s3.put_object_tagging(
            Bucket=bucket,
            Key=key,    
            Tagging={
                'TagSet': [
                    {'Key': requestid, 'Value': requestid},
                ]
            }
        )
        get_tags_response = s3.get_object_tagging(
            Bucket=bucket,
            Key=key, 
        )
        print(get_tags_response)
        print(response.status_code)
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
        'statusCode': response.status_code,
        'body': response.content
    }
