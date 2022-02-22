# Currency Converter Utility Functions
# CMSC 495 6380: Current Trends and Projects in Computer Science
# Group 4: Anand Kumar, Leslie Hawkins, Andrew Regal, and Deidra Colquitt  
# Version History
# Version 0.1 - February 21, 2022 - Initial Commit by Anand Kumar
# Version 0.2 - February 22, 2022 - Add checkAPIStatus to API class by Anand Kumar

import time
import requests

class CurrencyConverter:
    def __init__(self, currencyFrom, currencyTo):
        self.currencyFrom = currencyFrom
        self.currencyTo = currencyTo

    def convert(self):
        convertedAmount = self.currencyFrom.conversionAmount * ( ( 1.0 / self.currencyFrom.exchangeRate ) * self.currencyTo.exchangeRate )
        print ( "Converted Amount: " + str(convertedAmount) )

    def whoAmI(self):
        print("Currency Converter - " + "Currency From: " + self.currencyFrom.threeLetterAcronym + " | Currency To: " + self.currencyTo.threeLetterAcronym + " | Currency From Amount: " + str(self.currencyFrom.conversionAmount))

class Currency:
    def __init__(self, threeLetterAcronym, name):
        self.baseCurrency = "USD"
        self.exchangeRate = 0.0
        self.threeLetterAcronym = threeLetterAcronym
        self.name = name
        self.lastUpdated = time.time()
        self.conversionAmount = 1.0

    def whoAmI(self):
        print("Currency - " + "TLA: " + self.threeLetterAcronym + " | Name: " + self.name + " | Exchange Rate: " + str(self.exchangeRate) + " | Last Updated: " + str(self.lastUpdated) )

    def setExchangeRate(self, exchangeRate):
        self.exchangeRate = exchangeRate

    def setConversionAmount(self, conversionAmount):
        self.conversionAmount = conversionAmount

class API:
    def __init__(self):
        self.openExchangeRatesAppId = "5e4482f3ff5f4d5f881b83c5e29e3733"
        self.baseCurrency = "USD"
                
    def checkAPIStatus(self):
        url = "https://openexchangerates.org/api/usage.json?app_id=" + self.openExchangeRatesAppId
        apiResponse = requests.get(url) 
        return requests.get(url)

    def getLatestRates(self):
        url = "https://openexchangerates.org/api/latest.json?app_id=" + self.openExchangeRatesAppId + "&base=" + self.baseCurrency + "&symbols=USD,EUR,JPY,GBP,AUD,CAD,CHF,CNY,SEK,NZD"
        return requests.get(url) 

# Driver code starts here
api = API()
apiResponse = api.checkAPIStatus()
apiStatus = (apiResponse.json())['status']
if apiStatus != 200:
    print("Status " + str(apiStatus) + ": API is not available")
else:
    print("Status " +  str(apiStatus) + ": API is available.  All systems go!")
    

apiResponse = api.getLatestRates()
dictionaryOfCurrencies = { }

def loadTop10Currencies():
    for key,value in (apiResponse.json())['rates'].items():
        dictionaryOfCurrencies[key] = Currency(key,"We need a switch case")
        dictionaryOfCurrencies[key].setExchangeRate(value)
    
    for key,value in dictionaryOfCurrencies.items():
        print(key, str(value.exchangeRate))

loadTop10Currencies()
dictionaryOfCurrencies['EUR'].conversionAmount = 5
currencyConverter = CurrencyConverter(dictionaryOfCurrencies['EUR'], dictionaryOfCurrencies['JPY'])
currencyConverter.whoAmI()
currencyConverter.convert()


