from flask import Flask, render_template

app = Flask("Webscrapper")

@app.route("/")
def home():
    return render_template("home.html", name="kim")

@app.route("/hello")
def hello():
    return 'hello you!'

app.run("127.0.0.1")