from flask import Flask, render_template, request, redirect
from extractors.remoteok import extract_rto_job
from extractors.weworkremote import extract_wwr_job

app = Flask("Webscrapper")


db={}

@app.route("/")
def home():
    return render_template("home.html", name="Search")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        remoteok = extract_rto_job(keyword)
        weworkremote = extract_wwr_job(keyword)
        jobs = remoteok + weworkremote
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("127.0.0.1")