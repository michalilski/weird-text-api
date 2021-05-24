# Weird Text REST API

## Run locally:

1. Install requirements using
 - ### pip install -r requirements.txt
2.1 Run command (with default parameters)
 - ### python3 weirdtextapi/manage.py runserver
2.2 or using gunicorn
 - ### gunicorn --pythonpath weirdtextapi weirdtextapi.wsgi

## Heroku:

To use this API from cloud just make GET request:
 - https://weird-text-api.herokuapp.com/v1/encode/?data=\<sentence\>  
where \<sentence\> is your sentence to encode
 - https://weird-text-api.herokuapp.com/v1/decode/?data=\<encoded\>  
where \<encoded\> is your text to decode