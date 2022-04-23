# Follow the instruction to add layers in aws lambda to import pandas lib
# Watch this tutorial https://youtu.be/lrEAu75zhNI
# Pundas lib is not available in aws lambda by default. 

import pandas as pd
import json

def lambda_handler(event, context):
    a = [5, 7, 4, 9]
    srs = pd.Series(a)
    
    print(srs)
    
    return {
        'statusCode': 200,
        'body': json.dumps('imported pandas')
    }
