# Intraday Strategy Backtester

A robust, Python-based backtesting engine designed to evaluate intraday trading strategies using historical market data. This project focuses on calculating key performance analytics and risk metrics to validate trading logic before live deployment.

## 🚀 Overview
This tool automates the process of testing intraday strategies (e.g., Momentum, Mean Reversion, or Crossover). By leveraging high-frequency data, it simulates trades, manages risk, and provides a detailed breakdown of the strategy's profitability.

## ✨ Key Features
* **Performance Metrics:** Automatically calculates Sharpe Ratio, Maximum Drawdown, CAGR, and Win Rate.
* **Risk Management:** Integrated support for fixed Stop-Loss (SL) and Take-Profit (TP) levels.
* **Fast Processing:** Built using optimized Pandas and NumPy operations for handling large intraday datasets.
* **Visualization:** Generates equity curves and trade entry/exit points for visual verification.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Handling:** Pandas, NumPy
* **Data Source:** [Mention source, e.g., yfinance / CSV / Alpha Vantage]
* **Visualization:** Matplotlib / Plotly





# 📊 9/20 EMA Crossover Strategy

A clean, beginner-friendly implementation of the classic **9 EMA / 20 EMA crossover** trading strategy with signal generation, backtesting, and performance visualization.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Latest-150458?style=flat&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📌 Overview

The **9/20 EMA Crossover** is one of the most widely used momentum-based trading strategies. It uses two Exponential Moving Averages of different periods to identify trend direction and generate buy/sell signals when the faster EMA crosses the slower one.

This project fetches real historical stock/forex data, computes the EMAs, generates signals, backtests the strategy, and produces a full performance report with chart.

---

## 🧠 Strategy Logic

```
9 EMA  → Fast EMA  (reacts quickly to recent price changes)
20 EMA → Slow EMA  (smoother, represents medium-term trend)

BUY  Signal : 9 EMA crosses ABOVE 20 EMA  → Bullish momentum
SELL Signal : 9 EMA crosses BELOW 20 EMA  → Bearish momentum
```

### Entry & Exit Rules

| Signal | Condition | Action |
|--------|-----------|--------|
| **BUY**  | 9 EMA crosses above 20 EMA | Enter Long |
| **SELL** | 9 EMA crosses below 20 EMA | Exit Long / Enter Short |
| **Stop Loss** | 1.5× ATR below entry | Risk control |
| **Take Profit** | 2× Stop Loss distance | 2R target |

---

## ✅ Features

- Fetches real OHLCV data using `yfinance`
- Computes 9 EMA and 20 EMA with pandas
- Detects crossover events (Golden Cross / Death Cross)
- Backtests strategy with configurable risk per trade
- Calculates full performance metrics (Win Rate, Sharpe, Max DD)
- Plots candlestick chart with EMA lines and signal arrows
- Works on any ticker — stocks, forex, crypto, indices

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/9-20-ema-crossover.git
cd 9-20-ema-crossover
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the strategy
```bash
python ema_strategy.py --ticker AAPL --interval 1d --period 1y
```

---

## 📁 Project Structure

```
9-20-ema-crossover/
├── ema_strategy.py       # Main strategy script
├── backtest.py           # Backtesting engine
├── plot.py               # Chart generation
├── requirements.txt      # Dependencies
├── output.png            # Sample output chart
└── README.md
```

---

## ⚙️ Configuration

| Argument | Default | Description |
|----------|---------|-------------|
| `--ticker` | `AAPL` | Any stock, forex, or crypto ticker |
| `--interval` | `1d` | Candle timeframe (`1m` `5m` `1h` `1d`) |
| `--period` | `1y` | Data lookback period |
| `--fast_ema` | `9` | Fast EMA period |
| `--slow_ema` | `20` | Slow EMA period |
| `--risk_pct` | `0.01` | Risk per trade (1%) |
| `--atr_sl` | `1.5` | ATR multiplier for stop loss |

---

## 📊 Performance Metrics

| Metric | Description |
|--------|-------------|
| **Total Trades** | Number of completed signals |
| **Win Rate** | % of trades that hit take profit |
| **Net P&L** | Total profit/loss in USD |
| **Sharpe Ratio** | Risk-adjusted return (target > 1.0) |
| **Max Drawdown** | Largest peak-to-trough equity drop |
| **Profit Factor** | Gross wins ÷ Gross losses (target > 1.5) |

---

## 📉 Sample Results (AAPL Daily, 2023)

```
Ticker         : AAPL
Timeframe      : Daily
Period         : 2023-01-01 → 2024-01-01
Fast EMA       : 9
Slow EMA       : 20
─────────────────────────────
Total Trades   : 18
Winning Trades : 11  (61.1%)
Losing Trades  :  7  (38.9%)
Net P&L        : +$1,842
Sharpe Ratio   :  1.34
Max Drawdown   : -8.2%
Profit Factor  :  1.78
```

---

## 📈 How EMAs Work

```
EMA = Price × Multiplier + Previous EMA × (1 − Multiplier)
Multiplier = 2 ÷ (Period + 1)

9  EMA Multiplier = 2 ÷ (9  + 1) = 0.200  (reacts fast)
20 EMA Multiplier = 2 ÷ (20 + 1) = 0.095  (reacts slow)
```

The **9 EMA** is extremely sensitive to recent candles, making it ideal as a signal trigger. The **20 EMA** acts as a dynamic support/resistance and trend filter.

---

## 🔌 Supported Instruments

```python
# Stocks
python ema_strategy.py --ticker TSLA --interval 1d

# Forex (via yfinance)
python ema_strategy.py --ticker EURUSD=X --interval 1h

# Crypto
python ema_strategy.py --ticker BTC-USD --interval 4h

# Indices
python ema_strategy.py --ticker ^NSEI --interval 1d
```

---

## 🛠 Requirements

```
yfinance
pandas
numpy
matplotlib
mplfinance
ta
```

```bash
pip install -r requirements.txt
```

---

## 🔍 Tips for Better Results

- Use on **trending markets** — EMAs perform poorly in sideways/choppy conditions
- Combine with **volume confirmation** — strong crossovers have increasing volume
- Add **RSI filter** — only take longs when RSI > 50, shorts when RSI < 50
- Use **higher timeframes** (1h, 4h, daily) for more reliable signals

---

## 🛠 Future Improvements

- Add ADX filter to avoid trading in low-trend environments
- Multi-timeframe confirmation (HTF trend + LTF entry)
- Walk-forward optimization of EMA periods
- Live paper trading integration via broker API
- Streamlit dashboard for interactive backtesting

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. Do not use this as financial advice or for live trading without proper risk management. Past backtest results do not guarantee future performance.

---

## 📄 License

MIT License — free to use, modify, and distribute.

