from flask import Flask, render_template, request, redirect, send_file
from extractors.remoteok import extract_rto_job
from extractors.weworkremote import extract_wwr_job
from file import save_to_file

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



@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword==None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("127.0.0.1")