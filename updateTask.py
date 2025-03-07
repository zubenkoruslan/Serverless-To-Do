import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Use event directly from mapping template
    table.update_item(
        Key={'id': event['id']},
        UpdateExpression="set TaskName = :n, #s = :s",
        ExpressionAttributeValues={
            ':n': event['TaskName'],
            ':s': event['Status']
        },
        ExpressionAttributeNames={'#s': 'Status'}
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Task updated'})
    }