# Use Python 3.7 or 3.8
import json
import boto3
from botocore.exceptions import ClientError
import base64
import requests

def lambda_handler(event, context):
    bucket_name = 'e2esa-demo'
    filename = event['params']['header']['filename']
    object_key = 'uploads/' + filename
    
    s3_client = boto3.client('s3')
    
    file_content = event['body-json']
    content_decoded=base64.b64decode(file_content)
    
    # Generate a pre-signed URL for the S3 object
    try:
        presigned_url = s3_client.generate_presigned_url(
            'put_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=3600  # URL to expire in 1 hour
        )
        print(presigned_url)
        
        response = requests.put(presigned_url, data=file_content)
        print(response.status_code)
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps({'presignedUrl': presigned_url})
    }
