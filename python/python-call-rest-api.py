
# GET call
import requests
api_url = "https://lnvajpvyae.execute-api.us-east-1.amazonaws.com/prod/message"
response = requests.get(api_url)
response.json()
