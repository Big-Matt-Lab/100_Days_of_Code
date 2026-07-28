"""Udemy - 100 Days of Code:
The Complete Python Pro Bootcamp

*** Stock News Alert Project ***
This script fetches daily stock prices, calculates the percentage change between
the last two trading days, and if the stock price changed by more than 5%,
it retrieves the latest news articles related to the company.

Python Concepts Highlighted:
- Environment Variables for security (`os.environ.get()`)
- API Requests for retrieving JSON data (`requests.get()`)
- Date and Time manipulation (`datetime`, `timedelta`)
- List comprehensions for data processing (`[value for (key, value) in ...]`)
- Function modularity and clean code architecture
"""

import os
from datetime import datetime, timedelta

import requests

# Use the `os` module to safely retrieve API keys from environment variables
STOCK_API = os.environ.get("Stock_Data_API")
NEWS_API = os.environ.get("News_Data_API")

# Global variables defining the target stock and company names
STOCK_NAME = "SHW"
COMPANY_NAME = "Sherwin_Williams"

# Endpoint URLs for our external APIs
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Constants for displaying trend direction
UP_ARROW = "🔺 "
DOWN_ARROW = "🔻 "


def get_prices():
    """
    Fetches daily stock prices and checks for significant changes.
    Calculates the percentage difference between the last two trading days.
    Calls `get_news` if the price variation is greater than 5%.

    Args:
        None

    Returns:
        None
    """
    # Dictionary of query parameters sent with the HTTP request
    stock_search_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API,
        "outputsize": "compact"
    }
    
    # Python concept: Using the `requests` library to fetch data from an API
    response = requests.get(STOCK_ENDPOINT, params=stock_search_parameters, timeout=5)
    
    # Raise an exception if the HTTP request returned an unsuccessful status code
    response.raise_for_status()
    
    # Parse the response data into a Python dictionary
    data = response.json()

    stock_price_data = data["Time Series (Daily)"]

    # Python concept: Using a list comprehension to convert a dictionary into a list of its values
    data_list = [value for (key, value) in stock_price_data.items()]

    # Extract the closing price from the most recent trading day
    yesterday_closing_price = float(data_list[0]["4. close"])

    # Extract the closing price from the previous trading day
    day_before_closing_price = float(data_list[1]["4. close"])

    # Determine the trend direction to display
    if yesterday_closing_price > day_before_closing_price:
        arrow = UP_ARROW
    else:
        arrow = DOWN_ARROW

    # Python concept: Using `abs()` to get the absolute difference regardless of trend direction
    diff = (abs(day_before_closing_price - yesterday_closing_price)) / day_before_closing_price
    percent = diff * 100

    # Only fetch news if the stock price fluctuated significantly
    if percent <= 5:
        print("No news")
    else:
        get_news(STOCK_NAME, COMPANY_NAME, arrow, percent)


def get_news(ticker, company_name, arrow, percent):
    """
    Fetches the top news articles related to the company for the last day.

    Args:
        ticker (str): The stock ticker symbol.
        company_name (str): The name of the company to search news for.
        arrow (str): The trend direction arrow icon to display.
        percent (float): The percentage change in stock price.

    Returns:
        None
    """
    news_search_parameters = {
        "q": company_name,
        "from": date,
        "sortBy": "popularity",
        "apiKey": NEWS_API,
        "pageSize": 3,
    }
    
    response = requests.get(NEWS_ENDPOINT, params=news_search_parameters, timeout=5)
    response.raise_for_status()
    news_data = response.json()
    
    # Extract the list of articles from the JSON response
    news_articles = news_data["articles"]

    # Python concept: Iterating through a list of dictionaries to format and print specific fields
    for article in news_articles:
        # Python concept: Using f-strings and format specifiers (`.2f`) to round floating point numbers
        print(f"{ticker}: {arrow}{percent:.2f}%")
        
        # Use `.get()` to safely retrieve dictionary values, falling back to a default if the key is missing
        print("Headline:", article.get("title", "No Title"))
        print("Brief:   ", article.get("description", "No Description"))
        print("-" * 40)


if __name__ == "__main__":
    # Python concept: Using the `datetime` module to calculate yesterday's date
    dt = datetime.now() - timedelta(days=1)
    
    # Python concept: Formatting a datetime object into a specific string format using `strftime()`
    date = dt.strftime("%Y-%m-%d")

    get_prices()
