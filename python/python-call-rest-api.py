# GET call

--------------------------
# Option 1

import requests
api_url = "https://lnvajpvyae.execute-api.us-east-1.amazonaws.com/prod/message"
response = requests.get(api_url)
response.json()

--------------------------

# Option 2

import requests
import json

responses = list() 

for i in range(10):
  print(i)
  api_url = "https://lnvajpvyae.execute-api.us-east-1.amazonaws.com/prod/message"
  responses = requests.get(api_url)
  data=json.loads(responses.text)
  print(data)
  
  --------------------------
