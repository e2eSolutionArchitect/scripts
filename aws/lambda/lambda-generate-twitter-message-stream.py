import boto3
import json
from datetime import date
import random
import calendar
import time
from datetime import datetime

def lambda_handler(event, context):

    usr_id = random.randint(10000000, 100000000)
    id_str = random.randint(9999999999, 99999999999)
    
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    print("Current timestamp:", time_stamp)
    
    country=["US", "Canada", "Mexico", "India", "Japan" , "Dubai" , "China", "Kenya", "Australia" , "Srilanka"]
    hash_tags=create_hashtags(event)
    
    data_dict = {
      "created_at": datetime.fromtimestamp(time_stamp),
      "id_str": id_str,
      "text": "1\/ Today we\u2019re sharing our vision for the future of the Twitter API platform!\nhttps:\/\/t.co\/XweGngmxlP",
      "user": [
      {
        "id": usr_id,
        "name": "Twitter Dev",
        "screen_name": "TwitterDev",
        "location": "Internet",
        "url": "https:\/\/dev.twitter.com\/",
        "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"
      }],
      "place": [country[random.randint(0, 9)]],
      "entities": {
        "hashtags": hash_tags,
        "urls": [
          {
            "url": "https:\/\/t.co\/XweGngmxlP",
            "unwound": {
              "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",
              "title": "Building the Future of the Twitter API Platform"
            }
          }
        ],
        "user_mentions": [     
        ]
      }
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


def create_hashtags(event):
    hashtags_list=["Ucal", "Data608", "Calgary", "Canada", "Alberta" ]
    return [
         hashtags_list[random.randint(1,4)] , hashtags_list[random.randint(1,4)] 
    ]
