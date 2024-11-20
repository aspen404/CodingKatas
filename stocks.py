import requests
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import json

# Alpha Vantage or other financial API key
ALPHA_VANTAGE_API_KEY = 'VQW1I0PVBW65A8LF'

def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    print(f"HTTP Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.text}")
        return None
    try:
        data = response.json()
        if "Time Series (1min)" not in data:
            print(f"Error: Invalid data structure: {data}")
            return None
        
        # Extract the latest timestamp and stock prices
        time_series = data["Time Series (1min)"]
        latest_timestamp = list(time_series.keys())[0]
        latest_data = time_series[latest_timestamp]
        
        print(f"Latest Stock Price for {symbol}:")
        print(f"Time: {latest_timestamp}")
        print(f"Open: {latest_data['1. open']}")
        print(f"High: {latest_data['2. high']}")
        print(f"Low: {latest_data['3. low']}")
        print(f"Close: {latest_data['4. close']}")
        print(f"Volume: {latest_data['5. volume']}")
    except Exception as e:
        print(f"Error processing stock data: {e}")
        return None


def get_yahoo_earnings(symbol):
    try:
        ticker = yf.Ticker(symbol)
        earnings = ticker.calendar
        print("Earnings Calendar from Yahoo Finance:")
        print(earnings)
        return earnings
    except Exception as e:
        print(f"Error fetching earnings data from Yahoo Finance: {e}")
        return None

def get_after_hours_data(symbol):
    ticker = yf.Ticker(symbol)
    after_hours_data = ticker.history(period="1d", interval="1m")
    return after_hours_data

def calculate_momentum(data):
    data['Price Change (%)'] = (data['Close'] - data['Open']) / data['Open'] * 100
    data['Volume Spike'] = data['Volume'] / data['Volume'].mean()
    return data

def get_yahoo_news(symbol):
    ticker = yf.Ticker(symbol)
    try:
        news = ticker.news
        print("News from Yahoo Finance:")
        return pd.DataFrame(news)
    except Exception as e:
        print(f"Error fetching Yahoo Finance news: {e}")
        return pd.DataFrame()

def analyze_earnings(earnings_data):
    try:
        earnings_avg = earnings_data["Earnings Average"]
        earnings_high = earnings_data["Earnings High"]
        earnings_low = earnings_data["Earnings Low"]

        if earnings_avg > earnings_high:
            print(f"*** Earnings BEAT Expectations by {earnings_avg - earnings_high:.2f} ***")
        elif earnings_avg < earnings_low:
            print(f"*** Earnings MISSED Expectations by {earnings_low - earnings_avg:.2f} ***")
        else:
            print("*** Earnings Met Expectations ***")
    except Exception as e:
        print(f"Error analyzing earnings data: {e}")

def generate_recommendation(price_change, volume_spike, earnings_data):
    try:
        earnings_avg = earnings_data["Earnings Average"]
        earnings_high = earnings_data["Earnings High"]
        earnings_low = earnings_data["Earnings Low"]

        earnings_factor = 1 if earnings_avg > earnings_high else (-1 if earnings_avg < earnings_low else 0)
        momentum_factor = 1 if price_change > 2 else (-1 if price_change < -2 else 0)
        volume_factor = 1 if volume_spike > 2 else 0

        score = earnings_factor + momentum_factor + volume_factor

        if score >= 3:
            return "EXTREME_BUY"
        elif score == 2:
            return "BUY"
        elif score == -1:
            return "SELL"
        elif score <= -2:
            return "EXTREME_SELL"
        else:
            return "HOLD"
    except Exception as e:
        print(f"Error generating recommendation: {e}")
        return "HOLD"

def main(symbol):
    print(f"Fetching data for {symbol}...")

    # Fetch stock price data
    get_stock_price(symbol)
    
    # Fetch earnings data
    earnings_data = get_yahoo_earnings(symbol)
    if earnings_data is not None:
        print("\nEarnings Data:")
        earnings_df = pd.DataFrame([earnings_data])  # Convert dictionary to DataFrame
        print(earnings_df.T)  # Transpose for better readability
        analyze_earnings(earnings_data)

    # Fetch after-hours trading data
    after_hours_data = get_after_hours_data(symbol)
    if not after_hours_data.empty:
        after_hours_data = calculate_momentum(after_hours_data)
        print("\nMomentum Metrics:")
        print(after_hours_data[['Price Change (%)', 'Volume Spike']].tail())

        # Calculate buy recommendation
        latest_data = after_hours_data.iloc[-1]
        price_change = latest_data['Price Change (%)']
        volume_spike = latest_data['Volume Spike']

        recommendation = generate_recommendation(price_change, volume_spike, earnings_data)
        print(f"\n*** RECOMMENDATION: {recommendation} ***")

        # Plot after-hours price changes
        plt.figure(figsize=(10, 5))
        plt.plot(after_hours_data.index, after_hours_data['Close'], label='Price')
        plt.title(f"After-Hours Trading for {symbol}")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.legend()
        plt.show()

    # Fetch news data
    news_data = get_yahoo_news(symbol)
    if not news_data.empty:
        print("\nRelated News Headlines:")
        print(news_data[['title', 'publisher', 'link']])

# Run the script
if __name__ == "__main__":
    stock_symbol = input("Enter stock symbol: ").upper()
    main(stock_symbol)
