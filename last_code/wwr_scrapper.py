import requests
from bs4 import BeautifulSoup

def wwr_get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = []

    result = requests.get(url, allow_redirects=False)

    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("li", {"class":"feature"})

    for result in results:
        title = result.find("span", {"class":"title"}).get_text()
        company = result.find("span", {"class":"company"}).get_text()
        
        detail_link = []
        detail_link = result.find_all("a")
        for link in detail_link:
            if 'remote-jobs' not in link.get('href'):
                pass
            elif 'remote-jobs' in link.get('href'):
                add_link = link.get('href')
                new_link = f"https://weworkremotely.com{add_link}"  
        link_result = requests.get(new_link)
        link_soup = BeautifulSoup(link_result.text, "html.parser")
        apply_link = link_soup.find("a", {"id":"job-cta-alt"}).get('href')
        
        row = {'title': title, 'company': company, 'link': apply_link}
        
        jobs.append(row)
        
    return jobs







