## it is a lambda function in python to archive a file when it is dropped in an s3 bucket and read the file content. It is manly to read a small text file
import boto3
import urllib

def lambda_handler(event, context):
   s3_client =boto3.client('s3')
  
   s3_archive_bucket="arc_bucket"
   
   bucket_name = event['Records'][0]['s3']['bucket']['name']
   key=event['Records'][0]['s3']['object']['key']
   key=urllib.parse.unquote_plus(key,encoding='utf-8')
   message=key + ' file uploaded ' + ' to bucket ' + bucket_name
   print(message)
   
   response=s3_client.get_object(Bucket='s3fileupload',Key=key)
   contents= response["Body"].read().decode()
   print("file : \n",contents)
   
   s3_upload_archive =s3_client.put_object(Bucket=s3_archive_bucket, Key=key)
