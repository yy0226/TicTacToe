from flask import Flask, redirect, render_template, request, url_for, session
from engine.cli import *
from engine.logic import *
import random

app = Flask(__name__)
app.secret_key = 'ttt'

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
    session.pop('first_player', None)
    session.pop('second_player', None)
    session.pop('board', None)
    if request.method == "POST":
        first_player = request.form.get("player1")
        second_player = request.form.get("player2")
        session['name'] = name

        return redirect(url_for('game'))
        #board = [[None, None, None], [None, None, None], [None, None, None]]

        #return render_template(
        #    "play.html", board=board, player1=first_player, player2=second_player
        #)
    else:
        if 'user' in session
         return redirect(url_for('game'))
        else:
            return render_template("index.html")


@app.route('/game', methods = ["POST", "GET"])
def game():
    if "board" not in session:
            person = random.choice(["X","0"])
            session["board"] = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
            ]
            session["turn"] = person
            session["winner"] = False
            session["draw"] = False
    
    winner = get_winner(session["board"])

        
    if "name" in session:
        name = session["name"]
        return render_template('game.html', name = name,  game = session["board"], turn = session["turn"], winner = winner)
    else:
        return redirect(url_for("get_game_mode"))


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == "X":
            return 1
        elif board[0][0] == "O":
            return 2
        else:
            return None

    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == "X":
            return 1
        elif board[1][0] == "O":
            return 2
        else:
            return None

    elif board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == "X":
            return 1
        elif board[2][0] == "O":
            return 2
        else:
            return None

    elif board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == "X":
            return 1
        elif board[0][0] == "O":
            return 2
        else:
            return None

    elif board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == "X":
            return 1
        elif board[0][1] == "O":
            return 2
        else:
            return None

    elif board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] == "X":
            return 1
        elif board[0][2] == "O":
            return 2
        else:
            return None

    elif board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 1
        elif board[0][0] == "O":
            return 2
        else:
            return None

    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 1
        elif board[0][2] == "O":
            return 2
        else:
            return None

    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 1
        elif board[0][2] == "O":
            return 2
        else:
            return None

def check_draw(self, board):
    # check if its a draw
    isDraw = True
    for row in board.board():
        # if there is space left in the board, it's not a draw
        if None in row:
            isDraw = False
    return isDraw


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "O":
        return "X"
    else:
        return "O"


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "0"
    else:
        session["turn"] = "X"
    return redirect(url_for('game'))


if __name__ == "__main__":
    app.run()
