import requests
import sys
import json

def main():
    get_value()


def get_value():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()
    response = response.json()
    rate_float = response["bpi"]["USD"]["rate_float"]
    print(f"${(num*rate_float):,.4f}")


if __name__ == "__main__":
    main()
