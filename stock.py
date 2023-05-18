# Correlation Analysis: Determine the correlation between different stocks to understand the relationship between their price movements. Correlation analysis helps identify diversification opportunities and assess portfolio risk.

# Volatility Analysis: Calculate the volatility of stock prices using metrics such as standard deviation, average true range (ATR), or Bollinger Bands. Volatility analysis provides insights into the potential risk and price fluctuations associated with the stocks.

# Financial Ratios: Use the stock data to calculate financial ratios such as price-to-earnings ratio (P/E ratio), earnings per share (EPS), and dividend yield. These ratios provide insights into the valuation and financial health of the company.

# Candlestick Chart Analysis: Visualize the stock data using candlestick charts, which display the open, high, low, and close prices for each day. Candlestick patterns can provide insights into price trends, market sentiment, and potential reversal points.

# Moving Averages: Calculate and plot moving averages of different time periods to identify trends and potential support/resistance levels. Moving averages smooth out price fluctuations and can help in determining entry and exit points.

# Volume Analysis: Analyze the trading volume associated with the stock data to understand the level of market interest and liquidity. Volume analysis can provide insights into price movements and potential market trends.

# Risk Analysis: Calculate risk metrics such as Value at Risk (VaR) or drawdowns to assess the potential downside risk associated with the stocks. Risk analysis helps in portfolio optimization and risk management.

# Time Series Forecasting: Use time series forecasting techniques, such as ARIMA, exponential smoothing, or machine learning algorithms, to predict future stock prices based on historical data. Forecasting can assist in making investment decisions and managing portfolios.


import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_dummy_stock_data():
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    dummy_stocks = []

    for symbol in symbols:
        num_days = 100  # Number of days for which historical data will be generated
        start_date = datetime.now() - timedelta(days=num_days)

        # Generate a range of dates
        dates = pd.date_range(start=start_date, periods=num_days, freq='D')

        # Generate random price values for Open, High, Low, and Close
        open_prices = np.random.uniform(50, 200, num_days)
        high_prices = np.random.uniform(open_prices, 200, num_days)
        low_prices = np.random.uniform(50, open_prices, num_days)
        close_prices = np.random.uniform(low_prices, high_prices, num_days)

        # Generate random volume values
        volumes = np.random.randint(100000, 1000000, num_days)

        # Create a list of dictionaries with the generated data
        stock_data = [
            {
                'Symbol': symbol,
                'Date': date,
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price,
                'Volume': volume
            }
            for date, open_price, high_price, low_price, close_price, volume
            in zip(dates, open_prices, high_prices, low_prices, close_prices, volumes)
        ]

        dummy_stocks.append(stock_data)

    return dummy_stocks


# Historical Price Analysis: Analyze the historical price data to identify trends, patterns, and fluctuations in the stock prices over time. You can calculate metrics such as moving averages, standard deviation, and rate of return to assess the volatility and stability of the stock.
def perform_historical_price_analysis(stock_data):
    for stock in stock_data:
        df = pd.DataFrame(stock)
        df.set_index('Date', inplace=True)
        symbol = df['Symbol'].iloc[0]  # Get the symbol from the DataFrame

        # Calculate moving averages (e.g., 10-day and 50-day)
        df['MA10'] = df['Close'].rolling(window=10).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()

        # Plot closing prices and moving averages
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, df['Close'], label='Close')
        plt.plot(df.index, df['MA10'], label='MA10')
        plt.plot(df.index, df['MA50'], label='MA50')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f"Stock Analysis: {symbol}")  # Use the symbol variable
        plt.legend()
        plt.show()


# # Generate dummy stock data
stock_data = generate_dummy_stock_data()

# # Perform historical price analysis and visualize the results
# perform_historical_price_analysis(stock_data)


# Performance Comparison: Compare the performance of different stocks or the same stock over different time periods. Calculate metrics like cumulative return, annualized return, and relative performance to evaluate the performance of stocks relative to benchmarks or other stocks.
def calculate_performance_metrics(stock_data):
    for stock in stock_data:
        df = pd.DataFrame(stock)
        symbol = df['Symbol'].iloc[0]

        # Convert the 'Date' column to datetime type
        df['Date'] = pd.to_datetime(df['Date'])

        # Calculate additional performance metrics
        df['Return'] = df['Close'].pct_change()
        df['Cumulative Return'] = (1 + df['Return']).cumprod()

        # Calculate annualized return
        df['Annualized Return'] = (
            df['Cumulative Return'].iloc[-1]) ** (252 / len(df)) - 1

        # Calculate relative performance
        df['Relative Performance'] = (
            df['Cumulative Return'] / df['Cumulative Return'].iloc[1] - 1) * 100

        # Plotting cumulative return
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Cumulative Return'])
        plt.xlabel('Date')
        plt.ylabel('Cumulative Return')
        plt.title(f'Cumulative Return for {symbol}')
        plt.show()

        # Plotting annualized return
        plt.figure(figsize=(10, 6))
        plt.bar(symbol, df['Annualized Return'])
        plt.ylabel('Annualized Return')
        plt.title(f'Annualized Return for {symbol}')
        plt.show()

        # Plotting relative performance
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Relative Performance'])
        plt.xlabel('Date')
        plt.ylabel('Relative Performance')
        plt.title(f'Relative Performance for {symbol}')
        plt.show()


# Calculate performance metrics and visualize
calculate_performance_metrics(stock_data)
