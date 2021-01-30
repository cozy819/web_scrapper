import requests
from bs4 import BeautifulSoup

url = "https://transferwise.com/gb/currency-converter/CAD-to-USD-rate?amount=1000"    
    
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
exchange_ratio = soup.find("span", {"class":"text-success"}).string

print(exchange_ratio)
print(float(exchange_ratio))