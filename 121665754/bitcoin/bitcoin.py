import requests
import sys
import json

try:
    amount=None
    if str(sys.argv[1]).isalpha():
        sys.exit("Command-line argument is not a number")
    else:
        amount = float(sys.argv[1])


    responce = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data=responce.json()
    price = data['bpi']['USD']['rate_float']
    x=amount*price
    print(f"${x:,.4f}")

except requests.RequestException:
    ...
except IndexError:
    sys.exit("Missing command-line argument")


