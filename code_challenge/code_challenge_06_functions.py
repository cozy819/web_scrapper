import csv
import requests
from bs4 import BeautifulSoup

def get_link(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    super_brand = soup.find("div", {"id":"MainSuperBrand"})
    brand_link = super_brand.find_all("a", {"class":"goodsBox-info"})
    links = []
    for link in brand_link:
        links.append([link.find("span", {"class":"company"}).get_text(), link.get('href')])
    return links 

def get_info(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("div", {"id":"NormalInfo"})
    infos = table.find_all("tr", {"class":""})

    rows = []
    info_cnt = 1
    while info_cnt < len(infos):
        try:
            global place, title, time, pay, date
            place = infos[info_cnt].find("td", {"class":"local first"}).get_text().replace('\xa0', ' ')
            title = infos[info_cnt].find("span", {"class":"company"}).get_text()
            time = infos[info_cnt].find("td", {"class":"data"}).get_text()
            pay = infos[info_cnt].find("td", {"class":"pay"}).get_text()
            date = infos[info_cnt].find("td", {"class":"regDate last"}).get_text()
        except:
            pass    
        row = {'place':place, 'title':title, 'time':time, 'pay':pay, 'date':date}
        rows.append(row)
        info_cnt = info_cnt + 1
    return rows

def save_to_file(link_name, employments):
    file = open(f"{link_name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for employment in employments:
        writer.writerow(list(employment.values()))
    
    print(employments)
    return    

