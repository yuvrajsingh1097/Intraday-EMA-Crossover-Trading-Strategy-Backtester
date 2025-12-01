# import yfinance as yf
# import matplotlib.pyplot as plt
# import pandas as pd

# # 1. Define the stock ticker and date range
# ticker = "AAPL"
# start_date = "2023-01-01"
# end_date = "2025-01-01"

# # 2. Fetch historical stock data
# stock_data = yf.download(ticker, start=start_date, end=end_date)

# # 3. Plot the closing price
# plt.figure(figsize=(12, 6))
# plt.plot(stock_data['Close'], label='AAPL Close Price')

# # 4. Add labels, title, and grid
# plt.title(f'AAPL Stock Price Chart ({start_date} to {end_date})')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend()
# plt.grid(True)

# plt.show()




# import pandas as pd
# import numpy as np
# import datetime as dt
# import yfinance as yf

# def get_intraday_data(symbol="RELIANCE.NS", period="30d", interval="5m"):
#     df = yf.download(symbol, period=period, interval=interval, prepost=False)
#     df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
#     df.dropna(inplace=True)
#     return df

# def ema_intraday_strategy(df, fast=9, slow=21):
#     df = df.copy()

#     # Indicators
#     df['EMA_fast'] = df['Close'].ewm(span=fast, adjust=False).mean()
#     df['EMA_slow'] = df['Close'].ewm(span=slow, adjust=False).mean()

#     # Raw signal: 1 = long, 0 = flat
#     df['Position'] = 0
#     df.loc[df['EMA_fast'] > df['EMA_slow'], 'Position'] = 1
#     df.loc[df['EMA_fast'] < df['EMA_slow'], 'Position'] = 0

#     # Convert index to India time (usually it already is, but just in case)
#     if df.index.tz is not None:
#         df = df.tz_convert("Asia/Kolkata")

#     # Trading window: 09:20 to 15:20
#     start_t = dt.time(9, 20)
#     end_t   = dt.time(15, 20)

#     times = df.index.time
#     trading_mask = (times >= start_t) & (times <= end_t)

#     # Outside trading window: must be flat
#     df.loc[~trading_mask, 'Position'] = 0

#     # Shift for next-bar execution (no look-ahead)
#     df['Position'] = df['Position'].shift(1).fillna(0)

#     # Returns
#     df['Return'] = df['Close'].pct_change().fillna(0)

#     # Strategy returns only when in position
#     df['Strategy_Return'] = df['Position'] * df['Return']

#     # Equity curve (starting with 1 unit of capital)
#     df['Equity'] = (1 + df['Strategy_Return']).cumprod()

#     # Per-day performance
#     df['Date'] = df.index.date
#     daily_equity = df.groupby('Date')['Equity'].last()
#     daily_return = daily_equity.pct_change().fillna(0)

#     stats = {
#         "Total Return %": (df['Equity'].iloc[-1] - 1) * 100,
#         "Max Drawdown %": ((df['Equity'].cummax() - df['Equity']) / df['Equity'].cummax()).max() * 100,
#         "Daily Sharpe (approx)": (daily_return.mean() / daily_return.std() * np.sqrt(252)) if daily_return.std() != 0 else np.nan
#     }

#     return df, stats

# if __name__ == "__main__":
#     symbol = "RELIANCE.NS"  # change to '^NSEI', '^NSEBANK', 'TCS.NS', etc.
#     df = get_intraday_data(symbol, period="30d", interval="5m")
#     result, stats = ema_intraday_strategy(df, fast=9, slow=21)

#     print("Backtest stats for", symbol)
#     for k, v in stats.items():
#         print(f"{k}: {v:.2f}")

#     print(result[['Close', 'EMA_fast', 'EMA_slow', 'Position', 'Equity']].tail())




import pandas as pd
import yfinance as yf

def get_intraday_data(symbol="TATAMOTORS.NS", period="30d", interval="5m"):
    """
    Fetch intraday data from Yahoo Finance.
    period: '1d','2d','3d','7d'
    interval: '1m','5m','15m','30m','60m'
    """
    df = yf.download(symbol, period=period, interval=interval, prepost=False)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)
    return df

df = get_intraday_data("TATAMOTORS.NS", period="30d", interval="5m")
print(df.head())
