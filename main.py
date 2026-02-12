""" A program for looking up a country's name from a country code. """

import country_api 

def main():
    while True:
        code = input('Enter country code or press enter to quit ')
        # Check if user pressed enter to quit
        if not code:
            break
        # TODO check code is 2 letters 
        found, name, capital, error = country_api.get_country_name(code)
        
        if found:
            print(f'{code} is the country code for {name}')
            if capital:
                print(f'Capital: {capital}')
        elif not found and not error:
            print('No country found for that code')
        else:
            print('Error fetching data')
        

main()
