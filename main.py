""" A program for looking up a country's name from a country code. """

import country_api 

def main():
    while True:
        code = input('Enter country code or press enter to quit ')
        # TODO check code is 2 letters 
        # TODO end the loop if user presses enter
        result = country_api.get_country_info(code)
        
        if result['found']:
            print(f'{code} is the country code for {result["name"]}.')
            print(f'{result["capital"]} is the capital of {code}.')
        elif not result['found'] and not result['error']:
            print('No country found for that code')
        else:
            print('Error fetching data')
        

main()
