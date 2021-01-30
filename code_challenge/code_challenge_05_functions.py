import requests
from bs4 import BeautifulSoup

def get_currency_code():
    url = "https://www.iban.com/currency-codes"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    soup_table = soup.find("table", {"class":"table table-bordered downloads tablesorter"})
    soup_td = soup_table.find_all('td')
    td_data_all = []
    for td in soup_td:
        td_data_all.append(td.string)
    td_data_all__count = len(td_data_all)

    country = []
    currency_code = []

    country_count = 0
    while country_count < td_data_all__count:
        country.append(td_data_all[country_count])
        country_count = country_count + 4

    currency_count = 2
    while currency_count < td_data_all__count:
        currency_code.append(td_data_all[currency_count])
        currency_count = currency_count + 4

    result = []

    result_count = 0
    while result_count < len(country):
        result.append([country[result_count], currency_code[result_count]])
        result_count = result_count + 1

    return result


def input_countryNum(data_length):
    try:
        global choice
        choice = int(input("#:"))
        if 0 <= choice < data_length:
            pass
        else:
            print("Choose a number from the list.")
            input_countryNum(data_length)        
    except:
        print("That wasn't a number.")
        input_countryNum(data_length)
    output = choice        
    return output    

def input_money():
    try:
        money = float(input("#:"))
    except:
        print("That wasn't number")
        input_money()
    return money






def convert_currency(currency_code_from, currency_code_to, money_in):
    url = f"https://transferwise.com/gb/currency-converter/{currency_code_from}-to-{currency_code_to}-rate?amount={money_in}"    
    
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    exchange_ratio_string = soup.find("span", {"class":"text-success"}).string
    money_out = money_in*float(exchange_ratio_string)
    
    return money_out