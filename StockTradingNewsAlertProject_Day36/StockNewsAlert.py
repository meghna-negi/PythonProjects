import requests
import datetime as dt

STOCK = "TSLA" #Stock name
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = '' #API Key for stock

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

#Getting today's date
today = dt.date.today()
 
#Getting Yesterday and day before's date
yesterday = today - dt.timedelta(days = 3)
day_before_yesterday = yesterday - dt.timedelta(days = 1)

#Getting the data for the stocks
response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
response.raise_for_status()
data = response.json()