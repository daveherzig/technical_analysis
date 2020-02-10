import requests
from configparser import ConfigParser

# read the api key from the config file
def read_api_key(filename):
    parser = ConfigParser()

    parser = ConfigParser()
    parser.read(filename)

    return parser.get('keys', 'api-key')

def get_stock_data(symbol, start_date, end_date):
    base_url = "https://api.tiingo.com/tiingo/daily/" + symbol + "/prices"
    api_key = read_api_key("api-key.ini")
    print(api_key)
    payload = {
        'token': api_key,
        'startDate': start_date,
        'endDate': end_date
    }
    response = requests.get(base_url, params=payload)
    return response

if __name__ == "__main__":
    print("data_retriever.py")
    res = get_stock_data("PFE", '2018-03-25', '2019-04-25')
    print(res.json())
