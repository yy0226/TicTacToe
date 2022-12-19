# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


#it's a 3*3 board
def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == 'X':
            return 1
        elif board[0][0] == 'O':
            return 2
        else:
            return None

    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == 'X':
            return 1
        elif board[1][0] == 'O':
            return 2
        else:
            return None 

    elif board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == 'X':
            return 1
        elif board[2][0] == 'O':
            return 2
        else:
            return None

    elif board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == 'X':
            return 1
        elif board[0][0] == 'O':
            return 2
        else:
            return None

    elif board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == 'X':
            return 1
        elif board[0][1] == 'O':
            return 2
        else:
            return None

    elif board[0][2] == board[1][2] ==  board[2][2]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return 2
        else:
            return None

    elif board[0][0] == board[1][1] == board[2][2] :
        if board[0][0] == 'X':
            return 1
        elif board[0][0] == 'O':
            return 2
        else:
            return None   

    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return 2
        else:
            return None

    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return 2
        else:
            return None
    
    #My thought: no 'None' on the board but there is no winner
    #elif board[0][0]!= None and  board[0][1]!= None and board[0][2]!= None
    #I tried using loop to code
    """for i in board:
        if i != None"""
def check_draw(self, board):
    #check if its a draw
    isDraw = True
    for row in board.board():
        #if there is space left in the board, it's not a draw
        if None in row:
            isDraw = False
    return isDraw


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == 'O':
        return 'X'
    else: 
        return 'O'

# Week Week 8 - Lab Submission from here
import pandas as pd

# to define new class: GameSave
# to define the record table


# to insert data
#games = pd.Dataframe{
#    "Game ID": , # I don't know how can I generate a Game ID
 #   "Player 1": player
  #  "Player 2": other_player,
   # "Winner": get_winner,
#}


#to append data
def add_info(games, player1, player2, winner):
    games.loc[len(games)] = {
        "Game_ID": len(games),
        "Player_1": player1,
        "Player_2": player2,
        "Winner": winner,
    }

# to load the game
games_database = '/Users/yvonne/VSCO_509/TicTacToe/database.csv'
def read_games(games_database):
    try:
        return pd.read_csv(games_database)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
             "Game_ID",
             "Player_1",
             "Player_2",
             "Winner",
        ])


games = read_games()
games.to_csv(games_database)

