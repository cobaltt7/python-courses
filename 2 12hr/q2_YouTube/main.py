from flask import Flask, render_template, request
from numerize.numerize import numerize as _numerize
import requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://youtube138.p.rapidapi.com/channel/videos/"

    channel = request.args.get("channel")

    if not channel:
        return render_template("index.html")

    querystring = {"id": channel, "hl": "en", "gl": "US"}

    headers = {
        "X-RapidAPI-Key": "42dfedfd8dmsh82009e0f92c8689p11eb81jsn475e8b00d698",
        "X-RapidAPI-Host": "youtube138.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    contents = data["contents"]
    videos = [
        video["video"] for video in contents if video["video"]["publishedTimeText"]
    ]

    return render_template("videos.html", videos=videos)


@app.template_filter()
def numerize(number):
    return _numerize(number, 1)


app.run(host="0.0.0.0", port=81)
