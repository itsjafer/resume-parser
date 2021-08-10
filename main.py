import requests
import json
from base64 import b64decode

def handler(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    responseHeaders = {
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Origin': '*'
    }

    # Get the request body
    request_json = request.get_json()

    # decode the resume from base64
    resume = b64decode(request_json['content'])

    # ask Lever to parse our resume
    headers = {
        'Referer': 'https://jobs.lever.co/',
        'Origin': 'https://jobs.lever.co/'
    }
    parseResponse = requests.post(
        'https://jobs.lever.co/parseResume', 
        files=dict(resume=resume),
        headers=headers
    )

    response = {
        "body": json.dumps(parseResponse.json()) 
    }

    return (json.dumps(response, default=str), 200, responseHeaders)
