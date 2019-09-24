import boto3
import os
from uuid import UUID, uuid4

TABLE_KEY = 'nfjs-example'
DYNAMODB_ENDPOINT_KEY = 'DYNAMODB_ENDPOINT_URL'


class DynamoDBException(Exception):
    def __init__(self, message, status=500):
        self.message = message
        self.status = status


class DynamoDB:
    def __init__(self):
        if DYNAMODB_ENDPOINT_KEY in os.environ:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url='http://localhost:4569')
        else:
            dynamodb = boto3.resource('dynamodb')

        self.db = dynamodb.Table(TABLE_KEY)

        if not self.db:
            raise DynamoDBException(f'Table {TABLE_KEY} not found!')

    def create_employee(self, context=None):
        if context == None:
            raise DynamoDBException('No context was provided!', 400)

        id = str(uuid4())
        employee = {
            'id': str(uuid4()),
            'Name': context.json['Name'],
            'Cloud': context.json['Cloud'],
            'ProgrammingLanguage': context.json['pl'],
            'ProgrammingLanguage2': context.json['pl2']
        }

        self.db.put_item(Item=employee)

        return employee