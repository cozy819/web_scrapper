import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
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

print("Hello! Please choose select a country by number")
data_number = 0
while data_number < len(country):
    print(f"# {data_number} {country[data_number]}.")
    data_number = data_number + 1

def output():
    try:
        number_in = int(input("# "))
        if(0<= number_in <=267):
                print(f"You chose {country[number_in]}.")
                print(f"The currency code is {currency_code[number_in]}.")
        else:
            print("Choose a number from the list.")
            output()
    except:
        print("That wasn't a number.")
        output()        

output()