         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 
 
# Resume Parser

This repo hosts the AWS Lambda function for querying Lever's resume parsing API (as a bonus, it was written using AWS Cloud9). The REST API to query the function was set up using AWS API Gateway

While the Lever API is (probably unintentionally) public, it implements strict CORS. This lambda function is used as a proxy to facilitate server-to-server communication.

You can view a live demo [here](https://itsjafer.com/#/parser).

## How does this work?

Lever.co is a popular recruiting platform used by many companies. As job applicants, we often encounter Lever when applying for jobs. When applying to a job posting powered by Lever, if you pay attention to the network requests being made, you'll notice that a call to an internal Lever API is made. In particular, a post request is made to `https://jobs.lever.co/parseResume` which parses the resume through Lever's backend. My website is simply a front-end that displays the results of the parse in an easy-to-digest manner.

![diagram](overview.jpg)

