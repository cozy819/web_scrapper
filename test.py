import requests
from bs4 import BeautifulSoup
from operator import itemgetter

url = 'https://www.reddit.com/r/css/top/?t=month'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

selection = 'css'

datas = []
result = requests.get(url, headers= headers)
soup = BeautifulSoup(result.text, "html.parser")
divs = soup.find_all("div", {"class":"_1oQyIsiPHYt6nx7VOmd1sz"})

for div in divs:
    try:
        count = int(div.find("div", {"class":"_1rZYMD_4xY3gRcSS3p8ODO"}).get_text())
        print(count)
        title = div.find("h3", {"class":"_eYtD2XCVieq6emjKBH3m"}).get_text()
        link = div.find("a").get('href')
        data = {'theme': selection, 'title': title, 'count': count, 'link': link}
        datas.append(data)
    except:
        pass


print(datas)