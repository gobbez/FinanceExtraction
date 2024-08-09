# FinanceExtraction
Do you ever wondered if there is a way to exctract EVERY Stock Market Price, from past years to these days?

# Short answer: Yes, you can!
This code exctracts every stock market price from Yahoo Finance, creates a Linear Regression ML model to calculate predictions. <br>
This code can be further enhnaced to make future predictions, but for now it's mainly for exctractions.

# Modules:
import yfinance as yf <br>
import pandas as pd <br>
from sklearn.linear_model import LinearRegression <br>
from sklearn.model_selection import train_test_split <br>
from sklearn.metrics import r2_score, mean_squared_error <br>

# Extraction:
Set your start and end date and the game begins! <br>
start_date = start <br>
end_date = end <br>
count = 1 <br>
for symbol in all_tickers['Tickers']: <br>
    stock_data = yf.download(symbol, start=start_date, end=end_date) <br>
    stock_data['Stock'] = symbol <br>
