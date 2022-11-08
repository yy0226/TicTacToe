# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import *

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    Current_player = 'O'

    while winner == None:
        # TODO: Show the board to the user.
        print(board) 
        
        # TODO: Input a move from the player.
 
        X = int(input ())
        Y = int(input ())

        if not 0 <= X <= 2:
            print("X does not fit inside 0 to 2")
            continue
        if not 0 <= Y <= 2:
            print("Y does not fit inside 0 to 2")
            continue
        # to think=> range / occupied

        # TODO: Update the board.
        board[X][Y] = Current_player
    
        # TODO: Update who's turn it is.
        Current_player = other_player(Current_player)
        

        """winner = 'X'  # FIXME"""
        Winner = get_winner(board)
        if Winner == 1:
            print('X won')
        elif Winner == 2:
            print('O won')
 
        