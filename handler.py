import json


def hello(event, context):
    print("Hiiiiiiii from lambda logs")
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
