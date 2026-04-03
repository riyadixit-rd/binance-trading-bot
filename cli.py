import argparse
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

# ==============================
# 🔐 ADD YOUR FUTURES TESTNET KEYS HERE
# ==============================
API_KEY = "BiXaTo0g7HKXzAcxc9WAze8GcoAFGJsRfHcbRkAtNCd0sMmDOafWwEyJaUEhJriY"
API_SECRET = "9MCFQQKtPZiGyr04Uby38F357lcUV2uAeOjVvqu1lrGzBrVZHRMILDegUvyvcTbl"

# ==============================
# 🔧 LOGGING CONFIGURATION
# ==============================
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==============================
# 🔗 BINANCE CLIENT SETUP
# ==============================
client = Client(API_KEY, API_SECRET)

# ✅ IMPORTANT: Futures Testnet URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"


# ==============================
# 📌 ORDER FUNCTION
# ==============================
def place_order(symbol, side, order_type, quantity, price=None):
    try:
        print("\n📤 ORDER REQUEST")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        logging.info(f"Order Request → {symbol} {side} {order_type} {quantity} {price}")

        # ==============================
        # MARKET ORDER
        # ==============================
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        # ==============================
        # LIMIT ORDER
        # ==============================
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        # ==============================
        # RESPONSE OUTPUT
        # ==============================
        logging.info(f"API Response → {order}")

        print("\n✅ ORDER SUCCESS")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Quantity:", order.get("executedQty"))
        print("Average Price:", order.get("avgPrice", "N/A"))

    except BinanceAPIException as e:
        logging.error(f"Binance API Error → {e}")
        print("\n❌ Binance API Error:", e)

    except Exception as e:
        logging.error(f"General Error → {e}")
        print("\n❌ Error:", e)


# ==============================
# 🎯 CLI INPUT HANDLING
# ==============================
def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    # ==============================
    # INPUT VALIDATION
    # ==============================
    if args.type == "LIMIT" and args.price is None:
        print("❌ ERROR: LIMIT order requires --price")
        return

    if args.quantity <= 0:
        print("❌ ERROR: Quantity must be greater than 0")
        return

    # ==============================
    # PLACE ORDER
    # ==============================
    place_order(args.symbol, args.side, args.type, args.quantity, args.price)


# ==============================
# 🚀 ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()