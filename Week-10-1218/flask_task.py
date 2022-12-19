from flask import Flask, redirect, render_template, request, url_for, session
#from engine.app import cli, logic

app = Flask(__name__)

""" app.config['session_file_dir'] = mkdtemp
app.config['session_permanent'] = False
app.config['session_type'] = 'filesystem'

@app.route('/')
def index():
    if 'board' not in session:
        session['board'] = [[None, None, None], [None, None, None], [None, None, None]]
        session['turn'] = Current_player
        session(app) """

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        first_player = request.form.get("player1")
        second_player = request.form.get("player2")

        board = [[None, None, None], [None, None, None], [None, None, None]]

        return render_template(
            "play.html", board=board, player1=first_player, player2=second_player
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
