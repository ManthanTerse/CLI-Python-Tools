# Currency Converter
import argparse

exchange_rates = {
    "usd": 1.0,
    "inr": 83.0,
    "eur": 0.92,
    "jpy": 157.4
}

parser = argparse.ArgumentParser(description="Simple Currency Converter")

parser.add_argument("amount", type=float, help="Amount of money to convert")
parser.add_argument("from_currency", type=str, help="Currency to convert from (e.g., usd, inr, eur, jpy)")
parser.add_argument("to_currency", type=str, help="Currency to convert to (e.g., usd, inr, eur, jpy)")

args = parser.parse_args()

from_curr = args.from_currency.lower()
to_curr = args.to_currency.lower()

if from_curr not in exchange_rates or to_curr not in exchange_rates:
    print("Error: Supported currencies are:", ", ".join(exchange_rates.keys()))
else:
    usd_amount = args.amount / exchange_rates[from_curr]
    converted = usd_amount * exchange_rates[to_curr]
    print(f"{args.amount} {from_curr.upper()} = {converted:.2f} {to_curr.upper()}")
