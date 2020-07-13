from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

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
            pass
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", word=word, results_number=len(jobs))
