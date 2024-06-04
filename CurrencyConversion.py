import sys
import settings

from api import get_historical_rate, read_api_key
from cache import get_rate_from_cache, save_cache
from utils import get_valid_amount, load_currency_codes, get_valid_currency, save_conversion_to_json

# Passing date as a command-line argument at startup
if len(sys.argv) > 1:
    DATE = sys.argv[1]
else:
    EXECUTABLE_FILENAME = sys.argv[0]
    print('You need to provide a date as an argument')
    print(f'Please run the app with the following command: "python {EXECUTABLE_FILENAME} {{YYYY-MM-DD}}"')
    sys.exit(1)

# Loading all ISO 4217 currency codes from CSV file at startup
settings.CURRENCY_CODES = load_currency_codes()
# Loading Fast Forex API_KEY from config.json file at startup
settings.API_KEY = read_api_key(settings.CONFIG_JSON)


while True:
    # Getting Amount, Base Currency and Target Currency validated input
    amount = get_valid_amount()
    base_currency = get_valid_currency()
    target_currency = get_valid_currency()

    # Getting Historical Rate from cache if existing
    rate = get_rate_from_cache(DATE, base_currency, target_currency)
    # Getting Historical Rate from API when not existing in cache
    if not rate:
        rate = get_historical_rate(DATE, base_currency, target_currency)

    # Amount conversion to Target Currency
    converted_amount = amount * rate

    # Saving rate to cache
    save_cache(DATE, base_currency, target_currency, rate)
    # Saving successful conversion to conversions.json file
    save_conversion_to_json(DATE, amount, base_currency, target_currency, converted_amount)

    # printing conversion result
    print(f"{amount:.2f} {base_currency} is {converted_amount:.2f} {target_currency}")


