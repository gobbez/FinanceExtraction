# FinanceExtraction
Do you ever wondered if there is a way to exctract EVERY Stock Market Price, from past years to these days?

# Short answer: Yes, you can!
This code exctracts every stock market price from Yahoo Finance, creates a Linear Regression ML model to calculate predictions.
This code can be further enhnaced to make future predictions, but for now it's mainly for exctractions.

# Modules:
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Extraction:
Set your start and end date and the game begins!
start_date = start
end_date = end 
count = 1
for symbol in all_tickers['Tickers']:
    try:
        # Fetch historical stock data (stock_data is a df of current extraction and it will be concatenated to the df_stocks)
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        stock_data['Stock'] = symbol
