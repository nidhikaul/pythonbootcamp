import requests
import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
FROM_PH = os.environ.get('FROM_PH')
TO_PH = os.environ.get('TO_PH')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "apikey" : os.environ.get("STOCK_APIKEY"),
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK
    }

news_parameters = {
    "apiKey" : os.environ.get("NEWS_APIKEY"),
    "q" : COMPANY_NAME,
    "from" : "2022-12-21",
    "sortBy": "publishedAt"
    }

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
# response.raise_for_status()
print(response.status_code)
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in stock_data.items()]
yest_data = data_list[0]
yest_closing = yest_data["4. close"]

daybefore_data = data_list[1]
daybefore_closing = daybefore_data["4. close"]

# yest_closing = float(stock_data["Time Series (Daily)"]["2022-12-13"]["4. close"])
# daybefore_closing = float(stock_data["Time Series (Daily)"]["2022-12-12"]["4. close"])
diff_closing = abs(float(yest_closing) - float(daybefore_closing))
up_down = None
if diff_closing > -10:
    up_down = "🔺"
else:
    up_down = "🔻"
# print("yest_closing:", yest_closing)
# print("daybefore_closing:",daybefore_closing)
# print("diff_closing:" , diff_closing)

cal_percentage = round((diff_closing/float(yest_closing)) * 100)

print("cal_percentage:",cal_percentage)

# if diff_closing < cal_percentage or cal_percentage < diff_closing:
    # print("Get News")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

if cal_percentage > -10:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    print("news_api:",response.status_code)
    news_data = response.json()
    news_slice = news_data["articles"][:3]

#If the stock price has increased or decreased by 5% print the 3 articles
# if cal_percentage > 5:
    # print(news_slice)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.
    formatted_articles = [f"{STOCK}: {up_down}{cal_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_slice]
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(  
                                    from_=FROM_PH, 
                                    body=article,      
                                    to=TO_PH
                                ) 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

