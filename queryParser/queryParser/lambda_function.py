import requests
import json
from base64 import b64decode

def lambda_handler(event, context):
    # get the request body from API gateway
    body = json.loads(event['body'])
    
    # decode the resume from base64
    resume = b64decode(body['content'])
    
    # ask Lever to parse our resume
    parseResponse = requests.post('https://jobs.lever.co/parseResume', files=dict(resume=resume))
    
    # return a response for API gateway
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://itsjafer.com",
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Methods": "POST"
        },
        "body": json.dumps(parseResponse.json())
    };
    return response
