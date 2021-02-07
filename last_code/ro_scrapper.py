import requests
from bs4 import BeautifulSoup

def ro_get_jobs(word):
    url = f"https://remoteok.io/remote-{word}-jobs"

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }

    jobs = []

    result = requests.get(url, headers=headers)

    soup = BeautifulSoup(result.text, "html.parser")

    results = soup.find_all("tr", {"class":"job"})

    for result in results:
        title = result.find("h2", {"itemprop":"title"}).get_text()
        company = result.find("h3", {"itemprop":"name"}).get_text()
        try:
            link = result.find("a", {"class":"no-border tooltip"}).get('href')
        except:
            link = 'Closed'        
        
        if link == 'Closed':
            apply_link = 'This job post is closed and the position is probably filled'
        elif 'email' in link:
            apply_link = 'email-protection'
        else:
            apply_link = f"https://remoteok.io{link}"    
        row = {'title': title, 'company': company, 'link': apply_link}
        jobs.append(row)
    
    return jobs






