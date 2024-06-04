import sys
import settings
from api import get_historical_rate, read_api_key
from utils import get_valid_amount, load_currency_codes, get_valid_currency, save_conversion_to_json

if len(sys.argv) > 1:
    DATE = sys.argv[1]
    print(f"Provided date: {DATE}")
else:
    EXECUTABLE_FILENAME = sys.argv[0]
    print('You need to provide a date as an argument')
    print(f'Please run the app with the following command: "python {EXECUTABLE_FILENAME} {{YYYY-MM-DD}}"')
    sys.exit(1)

settings.CURRENCY_CODES = load_currency_codes()
settings.API_KEY = read_api_key(settings.CONFIG_JSON)


while True:
    amount = get_valid_amount()
    base_currency = get_valid_currency()
    target_currency = get_valid_currency()

    rate = get_historical_rate(DATE, base_currency, target_currency);

    converted_amount = amount * rate
    save_conversion_to_json(DATE, amount, base_currency, target_currency, converted_amount)
    print(f"{amount:.2f} {base_currency} is {converted_amount:.2f} {target_currency}")


