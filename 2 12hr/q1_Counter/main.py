from flask import Flask, render_template_string

app = Flask(__name__)

db = {}
if "number" not in db:
    db["number"] = 0


@app.route("/")
def home():
    return render_template_string("index.html", number=db["number"])


@app.route("/increment")
def increment():
    db["number"] += 1
    return render_template_string("index.html", number=db["number"])


@app.route("/decrement")
def decrement():
    db["number"] -= 1
    return render_template_string("index.html", number=db["number"])


app.run(host="0.0.0.0", port=81)
