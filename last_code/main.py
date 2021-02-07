from flask import Flask, render_template, request, redirect, send_file
from so_scrapper import so_get_jobs
from ro_scrapper import ro_get_jobs
from wwr_scrapper import wwr_get_jobs
from exporter import save_to_file
"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python



Good luck!main
"""
app = Flask("last_code")

@app.route("/")
def main():
    return render_template(
        'search.html'
    )

db = {}

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = so_get_jobs(word) + ro_get_jobs(word) + wwr_get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", 
        searchingBy=word, 
        resultsNumber=len(jobs),
        jobs = jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        filename = f"{word}.csv"
        save_to_file(jobs, filename)
        return send_file(filename)    
    except:
        return redirect("/")

app.run(host="0.0.0.0")