import requests
from typing import NamedTuple


class CountryResult(NamedTuple):
    found: bool
    name: str | None
    capital: str | None
    error: str | None

def get_country_info(country_code):
    """ Returns a CountryResult with found status, country name, capital, and error.
    If country is found: CountryResult(found=True, name=..., capital=..., error=None)
    If country is not found: CountryResult(found=False, name=None, capital=None, error=None)
    If there is an error: CountryResult(found=False, name=None, capital=None, error=...)"""

    try:
        url = create_url(country_code)
        json_response = make_api_request(url)
        if not json_response:
             return CountryResult(found=False, name=None, capital=None, error=None)
        name, capital = get_country_info_from_response(json_response)
        return CountryResult(found=True, name=name, capital=capital, error=None)
    except Exception as e:
        return CountryResult(found=False, name=None, capital=None, error='Error connecting to API')

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


def get_country_info_from_response(json_response):
    name = json_response[0]['name']['official']
    capital = json_response[0]['capital'][0] if json_response[0].get('capital') else 'N/A'
    return name, capital
