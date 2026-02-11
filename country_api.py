import requests 

def get_country_name(country_code):
    """Return structured country data for `country_code`.

    Returns a dict with the following keys:
      - found (bool): whether the country was found
      - name (str|None): official or common country name
      - capital (str|None): primary capital (if available)
      - region (str|None): region string from the API
      - population (int|None): population number from the API
      - error (str|None): error message if an error occurred

    Examples:
      If found: {'found': True, 'name': 'United States', 'capital': 'Washington, D.C.',
                 'region': 'Americas', 'population': 331002647, 'error': None}
      If not found (404): {'found': False, 'name': None, 'capital': None,
                           'region': None, 'population': None, 'error': None}
      On error: {'found': False, 'name': None, 'capital': None,
                 'region': None, 'population': None, 'error': '...'}
    """

    try:
        url = create_url(country_code)
        json_response = make_api_request(url)
        if not json_response:
            return {
                'found': False,
                'name': None,
                'capital': None,
                'region': None,
                'population': None,
                'error': None,
            }
        data = get_country_data_from_response(json_response)
        result = {'found': True, 'error': None}
        result.update(data)
        return result
    except Exception:
        return {
            'found': False,
            'name': None,
            'capital': None,
            'region': None,
            'population': None,
            'error': 'Error connecting to API',
        }

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


def get_country_data_from_response(json_response):
    country = json_response[0]
    name = None
    name_info = country.get('name', {})
    name = name_info.get('official') or name_info.get('common')

    capital = None
    caps = country.get('capital')
    if isinstance(caps, (list, tuple)) and caps:
        capital = caps[0]
    elif isinstance(caps, str):
        capital = caps

    region = country.get('region')
    population = country.get('population')

    return {
        'name': name,
        'capital': capital,
        'region': region,
        'population': population,
    }
