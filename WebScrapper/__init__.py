from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask(__name__)

db = {}

@app.route('/')
def hello_world():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromdb = db.get(word)
        if fromdb:
            jobs = fromdb
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html",
                           word=word,
                           results_number=len(jobs),
                           jobs=jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            print("jobs doesn't exist")
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv",
                         mimetype='text/csv',
                         attachment_filename="jobs.xlsx",
                         as_attachment=True)
    except:
        return redirect("/")
