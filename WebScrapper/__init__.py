from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", word=word)
