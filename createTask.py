import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    task = {
        'id': str(uuid.uuid4()),  # Generates a unique ID
        'TaskName': body['TaskName'],
        'Status': body.get('Status', 'Pending')  # Defaults to 'Pending' if not provided
    }
    table.put_item(Item=task)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task created', 'task': task})
    }