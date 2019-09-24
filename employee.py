import boto3
from uuid import uuid4

NAME_KEY = 'name'
CLOUD_KEY = 'cloud'
PL_KEY = 'pl2'
PL2_KEY = 'pl'


TABLE_KEY = 'nfjs-example'
DYNAMODB_ENDPOINT_KEY = 'DYNAMODB_ENDPOINT_URL'


class DynamoDBException(Exception):
    def __init__(self, message, status=500):
        self.message = message
        self.status = status


class Employee(object):
    def __init__(self):
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url='http://localhost:4569')

        self.db = dynamodb.Table(TABLE_KEY)

        print(f'In init, db is {self.db}')

        if not self.db:
            raise DynamoDBException(f'Table {TABLE_KEY} not found!')

    def save_employee(self, context=None):
        if context == None:
            raise DynamoDBException('No context was provided!', 400)

        id = str(uuid4())
        employee = {
            'uuid': str(uuid4()),
            'name': context.json[NAME_KEY],
            'cloud': context.json[CLOUD_KEY],
            'programmingLanguage': context.json[PL2_KEY],
            'programmingLanguage2': context.json[PL_KEY]
        }
        print(f'Employee is {employee}')
        self.db.put_item(Item=employee)

        return employee

    def get_employee(self, uuid=None):
        if uuid == None:
            raise DynamoDBException(f'No uuid was provided!', 400)

        response = self.db.get_item(
            Key={
                'uuid': str(uuid)
            }
        )
        if 'Item' not in response:
            raise DynamoDBException(f'{uuid} has no context', 404)

        return response['Item']
