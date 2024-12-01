from flask import Flask, render_template, request, session
import requests

USERS = []

app = Flask(__name__)
app.secret_key = "fake_secret_key_for_dummy_app"


def get_user(user_name):
    # new user
    filtered = [user for user in USERS if user["user_name"] == user_name]
    if filtered:
        user = filtered[0]
        user["logins"] += 1
    else:
        user = {"user_name": user_name, "logins": 1, "dogs_generated": 0}
        USERS.append(user)
    return user


def get_leaderboard():
    return enumerate(
        sorted(USERS, key=lambda user: user["dogs_generated"], reverse=True)
    )


def get_total_dogs():
    count = 0
    for user in USERS:
        count += user["dogs_generated"]
    return count


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form["user_name"]
        session["user"] = user_name

        # new user
        user = get_user(user_name)
    else:
        user = None

    return render_template(
        "index.html",
        dogs_generated=get_total_dogs(),
        user=user,
        leaderboard=get_leaderboard(),
    )


@app.route("/get_dog")
def get_dog():
    if not session["user"]:
        return render_template("index.html")
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    dog_image = data["message"]
    user = get_user(session["user"])
    user["dogs_generated"] += 1
    return render_template(
        "index.html",
        dog_image=dog_image,
        dogs_generated=get_total_dogs(),
        user=user,
        leaderboard=get_leaderboard(),
    )


@app.route("/logout")
def logout():
    session["user"] = None
    return render_template("index.html", leaderboard=get_leaderboard())


@app.template_filter()
def trophy(index):
    return "1 🏆" if index == 0 else index + 1


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=81)
