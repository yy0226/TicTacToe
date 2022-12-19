from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <link rel="stylesheet" href="/static/style.css">
    <div class="myclass"> this is red </div> 
    """


@app.route("/goodbye")
def goodbye():
    return "cya!"


@app.route("/user/<name>")
def profile(name):
    return render_template("profile.html", name=name)


@app.route("/game/<game_id>")
def show_game(game_id):
    return "Hello " + game_id
