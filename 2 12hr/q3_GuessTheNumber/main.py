from random import choice
from flask import Flask, render_template, request

app = Flask(__name__)
MAX, MIN = 1000000, 1
data = {}


def init():
    data["number"], data["guesses"] = choice(range(MIN, MAX + 1)), []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        guess = int(request.form["number_guess"])
        data["guesses"].append(check_number(guess))
        template = render_template(
            "index.html", guesses=data["guesses"], min=MIN, max=MAX
        )
        if guess == data["number"]:
            init()
        return template

    return render_template("index.html", guesses=data["guesses"], min=MIN, max=MAX)


def check_number(guess):
    """
    Given the guess, compare it with the computer's number.

    >>> data['number'] = 50

    >>> check_number(5)
    '5 is too low'

    >>> check_number(75)
    '75 is too high'

    >>> check_number(50)
    '50 is correct!'
    """
    if guess > data["number"]:
        return f"{guess:,} is too high"
    elif guess < data["number"]:
        return f"{guess:,} is too low"
    else:
        return f"{guess:,} is correct!"


init()
app.run(host="0.0.0.0", port=81)
