import requests
import smtplib

STOCK = 'TSLA' #Stock name
STOCK_ENDPOINT = 'https://www.alphavantage.co/query' #Stock API endpoint
STOCK_API_KEY = '' #API Key for stock

#Parameters for the stock API
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}

#Getting the data for the stocks
response = requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']
#Getting the list of daily stock details 
stock_list = [value for (key,value) in stock_data.items()]

#Getting the data for closing stock value for previous day and day before yesterday
prev_day = float(stock_list[0]['4. close'])
day_before = float(stock_list[1]['4. close'])
#Calculating the percentage change in the stock value of the two previous days
change = ((prev_day-day_before)/day_before) * 100

#Deciding the direction of arrow based on if change is positive or negative
if change > 0 :
    arrow = '🔺'
elif change < 0:
    arrow = '🔻'

COMPANY_NAME = 'Tesla Inc' #Company name
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything' #News API endpoint
NEWS_API_KEY = '' #API key for news

#email and password to send the mail
email = ''
password = ''

#Parameters for the news API
news_parameters = {
    'q': COMPANY_NAME,
    'language': 'en',
    'sortBy':'popularity',
    'apiKey': NEWS_API_KEY,
}

#Check the percentage change in stock values 
#If it is more than 5% the retrieve the top 3 articles for that company
#Send the article title and description as a mail
if(abs(change) > 5.0):
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()['articles']
    send_articles = news[:3]
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs='',
            msg=f"Subject:Stock news Alert \n\n TESLA {arrow} {round(abs(change))} \n\nHeadline: {send_articles[0]['title']}\nBrief: {send_articles[0]['description']}\n\n"
                f"Headline: {send_articles[1]['title']}\nBrief: {send_articles[1]['description']}\n\n"
                f"Headline: {send_articles[2]['title']}\nBrief: {send_articles[2]['description']}".encode("utf-8")
        )
    