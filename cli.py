# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import *
import random

def print_board(board):
    for i in range(len(board)):
        print(board[i])

def pve(board, winner, Current_player):
    print('playing against computer')

    turn = 'player'

    while winner == None:
        # TODO: Show the board to the user.
        print_board(board) 
        
        # TODO: Input a move from the player.
        if turn == 'player':
            print('Player' + Current_player + 'your turn!')
            X = int(input ())
            Y = int(input ())

            if not 0 <= X <= 2:
                print('X does not fit inside 0 to 2')
                continue
            if not 0 <= Y <= 2:
                print('Y does not fit inside 0 to 2')
                continue
            # to think=> range / occupied

            # TODO: Update the board.
        else:
            X = random.randint(0,2)
            Y = random.randint(0,2)
            while board[X][Y] is not None:
                X = random.randint(0,2)
                Y = random.randint(0,2)
        
        board[X][Y] = Current_player
    
        # TODO: Update who's turn it is.
        Current_player = other_player(Current_player)
        
        if turn == 'player':
            turn = 'computer'
        else:
            turn = 'player'

        """winner = 'X'  # FIXME"""
        winner = get_winner(board)
        if winner == 1:
            print('X won')
        elif winner == 2:
            print('O won')
 

def pvp(board, winner, Current_player):

    turn = 'player'
    while winner == None:
        # TODO: Show the board to the user.
        print_board(board) 
        
        # TODO: Input a move from the player.
        if turn == 'player':
            print('Player' + Current_player + 'your turn!')
            X = int(input ())
            Y = int(input ())

        if not 0 <= X <= 2:
                print('X does not fit inside 0 to 2')
                continue
        if not 0 <= Y <= 2:
                print('Y does not fit inside 0 to 2')
                continue
            # to think=> range / occupied

            # TODO: Update the board.

        board[X][Y] = Current_player
    
        # TODO: Update who's turn it is.
        Current_player = other_player(Current_player)

        """winner = 'X'  # FIXME"""
        winner = get_winner(board)
        if winner == 1:
            print('X won')
        elif winner == 2:
            print('O won')
 
if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    Current_player = 'O'

    game_type = input('press 1 to play against computer or 2 to play against another player')

    if game_type == '1':
        pve(board, winner, Current_player)
    elif game_type == '2':
        pvp(board, winner, Current_player)
    else:
        print('invalid selection')
    # print players symbol
    # print board
