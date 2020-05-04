import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('CalendarTest')

    CalenderEntry = 1

    # try:
    #     response = table.get_item(
    #         Key={
    #             'CalenderEntry': CalenderEntry,
    #         }
    #     )
    # except ClientError as e:
    #     print(e.response['Error']['Message'])
    # else:
    #     item = response['Item']

    response = table.get_item(
        Key={
            'CalenderEntry': CalenderEntry,
        }
    )
    item = response['Item']
    date = item['Date']
    print(date)

    return {
        "statusCode": 287,
        "body": {"Date": date}
    }
