from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from operator import itemgetter


def get_data(url, headers, selection):
    datas = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    divs = soup.find_all("div", {"class": "_1oQyIsiPHYt6nx7VOmd1sz"})
    for div in divs:
        try:
            count = int(
                div.find("div", {
                    "class": "_1rZYMD_4xY3gRcSS3p8ODO"
                }).get_text())
            title = div.find("h3", {
                "class": "_eYtD2XCVieq6emjKBH3m"
            }).get_text()
            link = div.find("a").get('href')
            data = {
                'theme': selection,
                'title': title,
                'count': count,
                'link': link
            }
            datas.append(data)
        except:
            pass
    return datas


"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}
"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript", "reactjs", "reactnative", "programming", "css", "golang",
    "flutter", "rust", "django"
]

app = Flask("DayEleven")


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/read")
def output():
    selections = []
    selections = request.args.getlist('check')
    total_result = []

    for selection in selections:
        url = f"https://www.reddit.com/r/{selection}/top/?t=month"
        results = []
        results = get_data(url, headers, selection)
        for result in results:
            data_part = result
            total_result.append(data_part)

            datas = sorted(total_result, key=itemgetter('count'), reverse=True)
    return render_template('read.html', selections=selections, datas=datas)


app.run(host="0.0.0.0")
