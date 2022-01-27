import requests
import json
import random
from base64 import b64decode
from lxml import html

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
        print(request.method)
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': 'https://itsjafer.com',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type'
        }

        return ('', 204, headers)

    # Set CORS headers for the main request
    responseHeaders = {
        'Access-Control-Allow-Methods': 'POST,GET',
        'Access-Control-Allow-Origin': 'https://itsjafer.com'
    }

    # Get the request body
    request_json = request.get_json()

    # decode the resume from base64
    resume = b64decode(request_json['content'])

    # pick a random job posting
    # (lever's demo API has ~350 postings)
    postingSkip = random.randint(1,350)

    # get information about this posting
    postingInfo = requests.get(
        f'https://api.lever.co/v0/postings/leverdemo?skip={postingSkip}&limit=1&mode=json'
    )

    # get the URL for this posting
    postingURL = postingInfo.json()[0]['applyUrl']

    # get CSRF token and posting ID from the posting
    posting = requests.get(postingURL)
    root = html.fromstring(posting.text)
    csrf = root.get_element_by_id("csrf-token").get('value')
    postingID = root.get_element_by_id("posting-id").get('value')

    # ask Lever to parse our resume
    headers = {
        'Referer': 'https://jobs.lever.co/',
        'Origin': 'https://jobs.lever.co/'
    }

    parseResponse = requests.post(
        'https://jobs.lever.co/parseResume', 
        files=dict(
            resume=('resume.pdf', resume),
            csrf=(None,csrf),
            postingId=(None,postingID)
            ),
        headers=headers
    )

    response = {
        "body": json.dumps(parseResponse.json()) 
    }

    return (json.dumps(response, default=str), 200, responseHeaders)
