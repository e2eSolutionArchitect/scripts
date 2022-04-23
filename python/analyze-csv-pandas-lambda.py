import json
import boto3
import base64
import pandas as pd

def lambda_handler(event, context):
    
   s3_client =boto3.client('s3')
   s3_bucket="s3fileupload"
   # print the event to find the variables to consider for body or other attributes. 
   print(json.dumps(event))
   file_content=event["body-json"]
   content_decoded=base64.b64decode(file_content)
   # through your client POST request if you are sending an attribute for holding filename 'filename' then it will be under 'params' section.
   # Note: you have to send a custom attribute to send file name like 'filename'. file name is not available by default. 
   # secondly note that, API gateway > API > Integration request > Mapping request > select method request passthrough 
   filename=event["params"]["header"]["filename"]
   s3_upload =s3_client.put_object(Bucket=s3_bucket, Key=filename, Body=content_decoded)
   
   
   
   #bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
   #s3_file_name = event["content"][0]["s3"]["object"]["key"]
   #print(s3_file_name)
   resp = s3_client.get_object(Bucket=s3_bucket, Key=filename)
       
   df = pd.read_csv(resp['Body'], sep=',')
   #print(df.info())

   return {
       'statusCode': 200,
       'body': json.dumps('worked')
   }
