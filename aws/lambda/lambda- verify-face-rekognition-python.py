import json
import boto3
from botocore.exceptions import ClientError

rekognition = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')

bucket='e2esa-mybucket-image'
collectionId='faceprintClnId'
fileName='test.jpg'
threshold = 80
maxFaces=2
        
def lambda_handler(event, context):
    found = False
    try:
        response=rekognition.search_faces_by_image(CollectionId=collectionId,
                                        Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                        FaceMatchThreshold=threshold,
                                        MaxFaces=maxFaces)
        for match in response['FaceMatches']:
          print(match['Face']['FaceId'],match['Face']['Confidence'])
          print ('FaceId:' + match['Face']['FaceId'])
          print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
          face = dynamodb.get_item(TableName = 'face_recognition', Key= {'RekognitionId':{'S':match['Face']['FaceId']}})
          print(json.dumps(face))
          if 'Item' in face:
            print ("Found Person: ", face['Item']['Metadata']['S'])
            found = True
        
          if not found:
            print("Person can not be recognized")
            
    except ClientError as e:
        print(e)
        return {
            'statusCode': e.args[0],
            'body': json.dumps({'ClientError': str(e)})
        }    
    except Exception as e:
        print(e)
        return {
            'statusCode': e.args[0],
            'body': json.dumps({'error': str(e)})
        }
    
    return {
        'body': found
    }
