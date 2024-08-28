"""
Rock Paper Scissors SOLUTION 🚀🔥
Concepts covered in this project:
    👉 Variables
    👉 Conditionals (if elif)
    👉 String Interpolation
    👉 Databases
    👉 Routing
    👉 Functions
    👉 Random
"""

from flask import Flask, render_template, request
from random import choice

db = {}

app = Flask(__name__)

if "game_start" not in db:
    db["game_start"] = False

if "player_score" not in db:
    db["player_score"] = 0

if "choices" not in db:
    db["choices"] = ""

if "result" not in db:
    db["result"] = ""


@app.route("/")
def index():
    # update the values to be dynamic and rely on the database
    return render_template(
        "index.html",
        game_start=db["game_start"],
        player_score=db["player_score"],
        choices=db["choices"],
        result=db["result"],
    )


# ** Calculate who won and show it on the screen **


@app.route("/play", methods=["POST"])
def play():
    # change the state of game_start in the database to True
    db["game_start"] = True
    # get human choice from url arguments & save humans choice in a variable
    # request.args['choice'] 👉 will get you the player choice as a string
    player_choice = request.args["choice"]
    # generate a choice on behalf of the computer then save it in a variable
    computer_choice = get_computer_choice()
    # calculate score of the player vs. computer choice
    score = calculate_result(player_choice, computer_choice)
    # update result, choices and player_score in the database
    db["result"] = get_result(score)
    db["choices"] = f"👨 {player_choice} 🤖 {computer_choice}"
    db["player_score"] += score
    # render the index.html file with dynamic values
    return render_template(
        "index.html",
        game_start=db["game_start"],
        player_score=db["player_score"],
        choices=db["choices"],
        result=db["result"],
    )


def get_computer_choice():
    """
    ** get_computer_choice randomly selects between `Rock` `Paper` `Scissors` and returns that string**
    get_computer_choice() 👉 'Rock'
    get_computer_choice() 👉 'Scissors'
    """
    return choice(["Rock", "Paper", "Scissors"])


def calculate_result(player_choice, computer_choice):
    """
    ** calculate_result compares player_move & computer_move and returns the score accordingly **
    human wins - calculate_result('Rock', 'Scissors') 👉 1
    human loses - calculate_result('Scissors', 'Rock') 👉 -1
    human draws - calculate_result('Rock', 'Rock') 👉 0
    """
    # Create a variable called `score` and set it's value to None

    # All situations where human draws, set `score` to 0
    if player_choice == computer_choice:
        return 0
    # All situations where human wins, set `score` to 1
    # make sure to use elifs here
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Scissors" and computer_choice == "Paper")
        or (player_choice == "Paper" and computer_choice == "Rock")
    ):
        return 1
    # Otherwise human loses (aka set score to -1)
    return -1
    # return score


def get_result(score):
    """
    get_result returns a string with a value of `You win!` or `I win!` or
    `It's a Draw!` based on the score.

    >>> get_result(1)
    "You win!"

    >>> get_result(-1)
    "I win!"

    >>> get_result(0)
    "It's a Draw!"
    """
    if score == 1:
        return "You win!"
    elif score == -1:
        return "I win!"
    else:
        return "It's a draw!"


@app.route("/end")
def end_game():
    # ** end_game resets every value to its initial value **
    db["game_start"] = False
    db["player_score"] = 0
    db["choices"] = ""
    db["result"] = ""
    return render_template(
        "index.html", game_start=False, player_score=0, choices="", result=""
    )


app.run(host="0.0.0.0", port=81)
