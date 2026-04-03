# 🚀 Binance Futures Trading Bot

## 📌 Overview
A Python-based CLI trading bot that places **MARKET** and **LIMIT** orders on Binance Futures Testnet.

---

## ⚡ Features
- Market and Limit order support  
- Buy and Sell functionality  
- CLI input using argparse  
- Logging of API requests and responses  
- Error handling  

---

## 🛠️ Setup

1. Install dependencies:
```bash
pip install -r requirements.txt


```

 ## ▶️ Usage



🔹 Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002



🔹 Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000



 ## 📝 Logs

All logs are stored in bot.log

