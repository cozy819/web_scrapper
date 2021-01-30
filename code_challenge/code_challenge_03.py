import os
import requests

#data length
const = None 
def set_data_length(n)
    const = n


def is_valid_url ():
    print('Welcome to IsItDown.py!')
    print('Please write a URLs you want to check.(seperated by comma)')
    typed_in = input().split(',')

    urls = []   
    url_list = []
    url_error = []

    for i in typed_in:
        urls.append(i.strip().lower())

    for url in urls:
        if "." not in url:
            url_error.append(url)
        elif url.startswith('http://') is True:
            url_list.append(url)
        elif url.startswith('https://') is True:
            url_list.append(url)
        else:
            url_list.append('http://'+url)

    for url in url_list:
        print(examine_url(url))
        
    for error in url_error:
        print(f"{error} is not a valid url.")

    restart()        



    

def examine_url(url):
    try: 
        result = requests.get(url).status_code
    except:
        result = 0
    
    message = ''

    if result == 200:
        message = f"{url} is up!"
    else:
        message = f"{url} is down!"

    return message        


def restart():
    answer = input('Do you want start over? (y/n)')

    if answer is 'n':
        print('ok, bye!')
    elif answer is 'y':
        os.system('clear')
        is_valid_url()
    else:
        print("It's not a valid answer.")
        restart()    


is_valid_url()    