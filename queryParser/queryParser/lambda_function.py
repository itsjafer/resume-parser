import requests
import json
from base64 import b64decode

def lambda_handler(event, context):
    # TODO implement
    body = event['body']
    print(body)
    
    resume = body['resume']
    bytes = b64decode(resume, validate=True)
    
    # resume = request.files['file']
    response = requests.post('https://jobs.lever.co/parseResume', files=dict(resume=bytes))

    return response.json()
