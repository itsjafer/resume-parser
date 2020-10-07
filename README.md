         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

# Resume Parser

This repo hosts the AWS Lambda function for querying Lever's resume parsing API (as a bonus, it was written using AWS Cloud9). 

While the Lever API is (probably unintentionally) public, it implements strict CORS. This lambda function is used as a proxy to facilitate server-to-server communication.

You can view a live demo [here](https://itsjafer.com/#/parser).

