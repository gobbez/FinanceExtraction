import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

all_tickers = pd.read_csv(r"C:\Users\user\PycharmProjects\LearningToolbox\pythonProject\Finances\All_Finance_Tickers.csv")
df_stocks = pd.DataFrame({'Date': [], 'Open': [], 'High': [], 'Low': [], 'Close': [], 'Adj Close': [], 'Volume': [], 'Stock': [], 'LinReg_Pred': [], 'R2_Score': [], 'MSE': [], 'Avg7': [], 'Avg42': []})
#df = pd.read_csv(r'C:\Users\user\PycharmProjects\LearningToolbox\pythonProject\Finances\all_tickers_extractions_1950_01_01_2024_08_08.csv')
#print(df.columns)

def extract_all_tickers(start, end):
    global all_tickers, df_stocks
    # Set start date and end date
    start_date = start
    end_date = end
    count = 1
    for symbol in all_tickers['Tickers']:
        try:
            # Fetch historical stock data (stock_data is a df of current extraction and it will be concatenated to the df_stocks)
            stock_data = yf.download(symbol, start=start_date, end=end_date)
            stock_data['Stock'] = symbol
            # Converts index (Date) as a regular columns (Date)
            stock_data = stock_data.reset_index()
            print(f'Eseguita estrazione di {symbol}')

            # ML Linear Regression
            # Setting Parameters for Models
            SEED = 42
            # Convert 'Date' to a numerical format (timestamp)
            stock_data['Date'] = stock_data['Date'].apply(lambda x: x.timestamp())
            X = stock_data[['Date', 'Close']].values
            y = stock_data['Close'].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)
            lr = LinearRegression()
            lr.fit(X_train, y_train)
            # Predict y_pred
            y_pred = lr.predict(X_test)
            # Calculate metrics
            r2 = r2_score(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)

            print(f'R2 Score for {symbol}: {r2}')
            print(f'MSE for {symbol}: {mse}')

            # Assign predictions and metrics to the entire dataset
            stock_data['LinReg_Pred'] = lr.predict(X)
            stock_data['R2_Score'] = r2
            stock_data['MSE'] = mse

            # Calculate Mobile Average of 7 and 42 days
            stock_data['Avg7'] = stock_data['Close'].rolling(window=7).mean()
            stock_data['Avg42'] = stock_data['Close'].rolling(window=42).mean()
            print('Calculated mobile avgs.. ')

            # Concats the stock_data df with the full df_stocks df
            df_stocks = pd.concat([df_stocks, stock_data])
            df_stocks.to_csv('all_tickers_extractions_1900_01_01_2024_08_08.csv')
            count += 1
            if count < 4:
                print(df_stocks)
                print(df_stocks['LinReg_Pred'])
        except Exception as e:
            print(f'Error processing {symbol}: {e}')
            continue


    # Display the stock data
    print(df_stocks)
    df_stocks.to_csv('all_tickers_extractions_1900_01_01_2024_08_08.csv')


extract_all_tickers("1900-01-01", "2024-08-08")