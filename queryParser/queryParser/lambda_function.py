import requests
import json
from base64 import b64decode

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    print(body['content'])
    
    resume = b64decode(body['content'])
    print(resume)
    print(type(resume))
    
    # resume = request.files['file']
    parseResponse = requests.post('https://jobs.lever.co/parseResume', files=dict(resume=resume))
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Methods": "POST"
        },
        "body": json.dumps(parseResponse.json())
    };
    
    print(response)

    return response
