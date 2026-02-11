import requests 

def get_country_info(country_code):
    """ Returns a dictionary with country information.
    If country is found: {'found': True, 'name': country_name, 'capital': capital_city, 'error': None}
    If country is not found: {'found': False, 'name': None, 'capital': None, 'error': None}
    If there is an API error: {'found': False, 'name': None, 'capital': None, 'error': error_message}"""

    try:
        url = create_url(country_code)
        json_response = make_api_request(url)
        if not json_response:
             return {'found': False, 'name': None, 'capital': None, 'error': None}
        name = get_name_from_response(json_response)
        capital = get_capital_from_response(json_response)
        return {'found': True, 'name': name, 'capital': capital, 'error': None}
    except Exception as e:
        return {'found': False, 'name': None, 'capital': None, 'error': 'Error connecting to API'}

def create_url(country_code):
    url = f'https://restcountries.com/v3.1/alpha/{country_code}'
    return url


def make_api_request(url):
    response = requests.get(url)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    json = response.json()  
    return json


def get_name_from_response(json_response):
    name = json_response[0]['name']['official']
    return name


def get_capital_from_response(json_response):
    capital = json_response[0]['capital'][0] if 'capital' in json_response[0] else None
    return capital
