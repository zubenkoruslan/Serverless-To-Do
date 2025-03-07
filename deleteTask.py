import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    table.delete_item(Key={'id': event['id']})
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task deleted'})
    }