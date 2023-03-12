import boto3
import json
from datetime import date
import random
import calendar
import time
from datetime import datetime

def lambda_handler(event, context):
    usr_id = random.randint(10000000, 100000000)
    
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    print("Current timestamp:", time_stamp)
    
    data_dict = {
        "id": usr_id,
        "name": "Twitter Dev",
        "screen_name": "TwitterDev",
        "location": "Internet",
        "url": "https:\/\/dev.twitter.com\/",
        "description": "Your official source for Twitter Platform news, updates & events. Need technical help?"
      }
    

    # Convert Dictionary to JSON String
    data_string = json.dumps(data_dict, indent=2, default=str)
    
    
    # Upload JSON String to an S3 Object
    s3_resource = boto3.resource('s3')
    
    s3_bucket = s3_resource.Bucket(name='ucal-datalake')
    
    s3_bucket.put_object(
        Key='raw-zone/streaming-data/message-'+str(time_stamp)+'.json',
        Body=data_string
    )

    return {
        'statusCode': 200,
        'body': data_string
    }
