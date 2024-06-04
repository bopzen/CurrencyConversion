import csv
import json
import os
import sys
import settings


# Loading all ISO 4217 currency codes from CSV file
def load_currency_codes():
    currency_codes = set()
    filename = settings.CURRENCY_CODES_CSV

    with open(filename, 'r') as file:
        csvfile = csv.reader(file)
        for line in csvfile:
            currency_codes.add(line[0])

    return currency_codes


# Validation of Amount input
def get_valid_amount():
    while True:
        amount = input()
        check_exit(amount)

        try:
            amount = float(amount)
            if round(amount, 2) == amount:
                return amount
            else:
                print("Please enter a valid amount")
        except ValueError:
            print("Invalid input. Please enter a valid float with two decimal places.")


# Validation of Base Currency and Target Currency input
def get_valid_currency():
    while True:
        currency = input()
        check_exit(currency)

        try:
            if currency.upper() in settings.CURRENCY_CODES:
                return currency.upper()
            else:
                print('Please enter a valid currency code')
        except ValueError:
            print("Invalid currency code. Currencies must be in ISO 4217 three letter currency code format")


# Saving successful conversion to conversions.json file
def save_conversion_to_json(date, amount, base_currency, target_currency, converted_amount):
    conversion = {
        "date": date,
        "amount": round(amount, 2),
        "base_currency": base_currency,
        "target_currency": target_currency,
        "converted_amount": round(converted_amount, 2)
    }

    if os.path.exists(settings.CONVERSIONS_JSON):
        with open(settings.CONVERSIONS_JSON, 'r') as json_file:
            conversions = json.load(json_file)
    else:
        conversions = []

    conversions.append(conversion)

    with open(settings.CONVERSIONS_JSON, 'w') as json_file:
        json.dump(conversions, json_file, indent=4)


# Checking for exit command
def check_exit(command):
    if command.lower() == 'end':
        sys.exit(0)
