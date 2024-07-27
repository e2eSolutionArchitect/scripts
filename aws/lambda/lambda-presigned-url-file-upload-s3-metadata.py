import json
import boto3
from botocore.exceptions import ClientError
import base64
import requests # Make sure the Lambda layer is added for 'requests'. It is not readily available unless custom layer is added. please refer https://github.com/e2eSolutionArchitect/troubleshoot/blob/main/aws/lambda%20function%20requests%20module%20not%20found.md
from datetime import datetime
import os
import logging
from botocore.config import Config

config = Config(signature_version='s3v4')
s3 = boto3.client('s3', config=config)

def lambda_handler(event, context):
    #print("environment variable: " + os.environ['S3_BUCKET'])
    bucket = os.environ['S3_BUCKET']
    filename = event['params']['header']['filename']
    cardnumber = event['params']['header']['cardnumber']
    username = event['params']['header']['username']
    key = os.environ['UPLOAD_DIR'] + filename

    now = datetime.now()
    requestid = now.strftime("%m%d%Y%H%M%S")

    #print(filename)
    
    file_content = event['content']
    content_decoded=base64.b64decode(file_content)

    
    
    try:
        # Generating presigned url and adding metadata to the object
        metadata = {'requestid': requestid, 'filename': filename,'cardnumber': cardnumber,'username': username}
        presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=360  # 3600 = URL to expire in 1 hour
        )
        headers = {'Bucket': bucket, 'Key': key}
        response = requests.put(presigned_url, data=content_decoded, headers=headers)
        tag_metadata(bucket,key,metadata)
        s3_object_copy(bucket,bucket,key,'process/'+ filename)
        
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

def tag_metadata(bucket,key,metadata):
    try:
        tags_response = s3.put_object_tagging(
                    Bucket=bucket,
                    Key=key,    
                    Tagging={
                        "TagSet": [
                            {"Key": "pii", "Value": "true"}
                        ]
                    }
                )
        print(tags_response)
        # Add user-defined Metadata to S3 object
        s3_resource = boto3.resource('s3')
        s3_object = s3_resource.Object(bucket, key)
        s3_object.metadata.update(metadata)
        s3_object.copy_from(CopySource={'Bucket':bucket, 'Key':key}, Metadata=s3_object.metadata, MetadataDirective='REPLACE')
    except ClientError as e:
        logging.error(e)
        return {
            'statusCode': e.args[0],
            'body': json.dumps({'ClientError during Metadata tagging': str(e)})
        }    
    except Exception as e:
        logging.error(e)
        return {
            'statusCode': e.args[0],
            'body': json.dumps({'error during Metadata tagging': str(e)})
        }
        
def s3_object_copy(src_bucket,dest_bucket,src_key,dest_key):
    try:
        s3.copy_object(Bucket=dest_bucket, 
                       CopySource={'Bucket': src_bucket, 'Key': src_key}, 
                       Key=dest_key)
    except ClientError as e:
        response = {
            'statusCode': e.response['ResponseMetadata']['HTTPStatusCode'],
            'body': json.dumps('Error copying file: ' + e.response['Error']['Message'])
        }
    return {
        'statusCode': 200,
        'body': 'File moved successfully'
    }
