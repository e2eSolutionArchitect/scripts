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
import time

responses = list() 

for i in range(50):
  time.sleep(5) # Sleep for 3 seconds
  print(i)
  api_url = "https://o9mhe0mj74.execute-api.us-east-1.amazonaws.com/prod/message"
  responses = requests.get(api_url)
  data=json.loads(responses.text)
  print(data)
  
  --------------------------
