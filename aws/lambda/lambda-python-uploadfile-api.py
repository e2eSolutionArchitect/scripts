# it is a lambda function in python. Used for triggering through an API gateway to upload the file into a s3 bucket. 

import json
import boto3
import base64

def lambda_handler(event, context):
    
   s3_client =boto3.client('s3')
   s3_bucket="s3fileupload"
   
   file_content=event["content"]
   content_decoded=base64.b64decode(file_content)
   s3_upload =s3_client.put_object(Bucket=s3_bucket, Key='uploaded-file.csv', Body=content_decoded)

   return {
       'statusCode': 200,
       'body': json.dumps('Hello from Lambda!')
   }
