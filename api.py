import json
import requests
import settings


# Reading API key from config.json
def read_api_key(json_file):
    filename = json_file
    with open(filename, 'r') as json_file:
        loaded_file = json.load(json_file)
        return loaded_file['API_KEY']


# Getting Historical Rate from the API
def get_historical_rate(date, base_currency, target_currency):
    url = f"https://api.fastforex.io/historical?date={date}&from={base_currency}&to={target_currency}&api_key={settings.API_KEY}"
    headers = {"accept": "application/json"}

    # Verify option is set to False due to security limitations on my work computer
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    return data['results'][target_currency]

