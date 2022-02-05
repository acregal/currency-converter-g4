# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import requests to be able to make API call
import urllib3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
# extract values from the event object we got from the Lambda service and store in a variable
    inputSourceCurrency = event['sourceCurrency']
    inputTargetCurrency = event['targetCurrency']
    inputSourceAmount = event['sourceAmount']
    i = 0

    apiURL = "https://openexchangerates.org/api/latest.json?app_id=3422b9f728864e51ba72589e132bd889"

    http = urllib3.PoolManager()
    response = http.request('GET', apiURL)
    responseData = response.data
    dataResultData = json.loads(responseData)

    for i in dataResultData.keys():
        if i == "rates":
            for j in dataResultData[i].keys():
                if j == inputTargetCurrency:
                    targetRate = dataResultData[i].get(inputTargetCurrency)
                if j == inputSourceCurrency:
                    sourceRate = dataResultData[i].get(inputSourceCurrency)
# Source currency is 1 USD -> EUR
# Target currency is also 1 USD -> JPY
# So target / source = actual exchange rate

    actualRate = round((float(targetRate) / float(sourceRate) * int(inputSourceAmount)), 2)

# return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps(actualRate)
    }