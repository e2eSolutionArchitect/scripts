import json

print('Loading function .... Lambda emi calculator using API gateway')

def lambda_handler(event, context):
	#1. Parse out query string params
	principal = event['queryStringParameters']['p']
	rate = event['queryStringParameters']['r']
	time = event['queryStringParameters']['t']
	
	principal = int(principal)
	rate = float(rate)
	time = int(time)
	
	emi = emi_calculator(principal, rate, time);
	
	#2. Construct the body of the response object
	transactionResponse = {}
	transactionResponse['p'] = principal
	transactionResponse['r'] = rate
	transactionResponse['t'] = time
	transactionResponse['emi'] = emi

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	#4. Return the response object
	return responseObject

def emi_calculator(p, r, t):
	r = r / (12 * 100) # one month interest 
	t = t * 12 # one month period 
	emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1) 
	return emi 
