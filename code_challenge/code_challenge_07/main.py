from flask import Flask, render_template, redirect, url_for, request
from scrapper import get_json, get_repl

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api

app = Flask("Day Nine")


@app.route("/")
def home():
    articles = []
    order_by = request.args.get('order_by')
    if order_by == 'popular':
        articles = get_json(popular)
        return render_template("index.html", articles=articles, title='Popular')
    elif order_by == 'new':
        articles = get_json(new)
        return render_template("index.html", articles=articles, title='New')
    else:
        order_by = 'popular'
        articles = get_json(popular)
        return render_template("index.html", articles=articles, title='Popular')


def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}


@app.route("/<id>")
def detailed_by_id(id):
    detail_url = make_detail_url(id)
    print(detail_url)
    if id in db.keys():
        comment_head = db[id][0]
        comments = db[id][1]
    else:
        new_db = get_repl(detail_url)
        comment_head = new_db[0]
        comments = new_db[1]
        db[id] = new_db

    return render_template("detail.html",
                           comment_head=comment_head,
                           comments=comments)


app.run(host="0.0.0.0")
