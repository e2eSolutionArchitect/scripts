// Example talks about using pandas in Lambda. 
// Please refer the steps https://www.youtube.com/watch?v=lrEAu75zhNI
import json
import pandas as pd

def lambda_handler(event, context):
    a  = [5,6,7,8,9]
    srs = pd.Series(a)
    print(srs)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
