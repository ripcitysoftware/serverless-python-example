import boto3
import os
from uuid import UUID, uuid4
from simplejson import dumps, loads

TABLE_KEY = 'nfjs-example'
DYNAMODB_ENDPOINT_KEY = 'DYNAMODB_ENDPOINT_URL'


class DynamoDBException(Exception):
    def __init__(self, message, status=500):
        self.message = message
        self.status = status


class Employee(object):
    def __init__(self):
        if DYNAMODB_ENDPOINT_KEY in os.environ:
            dynamodb = boto3.resource(
                'dynamodb', endpoint_url='http://localhost:4569')
        else:
            dynamodb = boto3.resource('dynamodb')

        self.db = dynamodb.Table(TABLE_KEY)

        print(f'In init, db is {self.db}')

        if not self.db:
            raise DynamoDBException(f'Table {TABLE_KEY} not found!')

    def save_employee(self, context=None):
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
        print(f'Employee is {employee}')
        self.db.put_item(Item=employee)

        return employee

    def get_employee(self, uuid=None):
        if uuid == None:
            raise DynamoDBException(f'No uuid was provided!', 400)

        response = self.db.get_item(
            Key={
                'Uuid': str(uuid)
            }
        )
        if 'Item' not in response:
            raise DynamoDBException(f'{uuid} has no context', 404)

        item = response['Item']
        item = loads(item, use_decimal=True)
        return item

