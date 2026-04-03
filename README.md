\ BINANCE FUTURES TRADING BOT



\ OVERVIEW

This is a Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.



\ FEATURES

\- Market and Limit order support

\- Buy and Sell functionality

\- CLI input using argparse

\- Logging of API requests and responses

\- Error handling



\ SETUP

1\. Install dependencies:

pip install -r requirements.txt



2\. Add your API keys in cli.py



\ USAGE



\### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002



\### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000



\ LOGS

All logs are stored in bot.log

