import os
from babel.numbers import format_currency
from code_challenge_05_functions import get_currency_code, input_countryNum, input_money, convert_currency

os.system("clear")

print("Welcome to Currency Convert Pro 2000")
#--------------------------------------------------
currency_code = []
currency_code = get_currency_code()
data_length = len(currency_code)

number = 0
while number < data_length:
    print(f"#{number}: {currency_code[number][0]}" )
    number = number + 1
#--------------------------------------------------

def select_country():
    global first_country_num
    print("Where are you from? Choose a country by number.")
    first_country_num = input_countryNum(data_length)
    print(currency_code[first_country_num][0])

    global second_country_num
    print("Now choose another country")
    second_country_num = input_countryNum(data_length)
    print(currency_code[second_country_num][0])

    if first_country_num == second_country_num:
        print("Your choices are same.")
        select_country() 
    
    output = [first_country_num, second_country_num]    
    
    return output

order = []
order = select_country()

selected_from = currency_code[order[0]]
selected_to = currency_code[order[1]]

print(f"How many {selected_from[1]} do you want to convert to {selected_to[1]}?")
money_in = input_money()

money_out = convert_currency(selected_from[1], selected_to[1], money_in)

output_money_in = format_currency(money_in, selected_from[1], locale="ko_KR")
output_money_out = format_currency(money_out, selected_to[1], locale="ko_KR")

print(f"{selected_from[1]} {output_money_in} is {output_money_out}")