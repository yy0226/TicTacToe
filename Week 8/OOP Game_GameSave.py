import random
from logic import get_winner


class Game:
    def __init__(self, playerX, playerO, board): #it is method; self should be adopted in every method
        self.board = board
        self.playerX = playerX
        self.playerO = playerO

    def print_board(self, board):
        for i in board:
            print(i)

    def run(self):
        game_not_over = True
        self.print_board(self.board)

        curr_player = self.playerX
        winner = None

        while winner == None:

            self.board = curr_player.get_move(self.board)

            self.print_board(self.board)
            winner = get_winner(board)

            if winner is not None:
                print("the winner is: " + str(winner))
            if curr_player == self.playerX:
                curr_player = self.playerO
            else:
                curr_player = self.playerX
            

    def test(self):
        print("test")

class Human:
    def __init__(self, type):
        self.type = type

    def get_move(self, board):
        print("player move")
        while True:
            x = int(input("choose column "))
            y = int(input("choose row"))

            if board[y][x] is None:
                break
            else:
                print('invalid move, please try again')
        board[y][x] = self.type
        return(board)


class Bot:
    def __init__(self, type):
        self.type = type

    def get_move(self, board):
        print("robot move")

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[y][x] is None:
                break
            else:
                print('invalid move, please try again')
        board[y][x] = self.type
        return(board)

### code starts here#####
playerX = None
playerO = None

x = input("robot or player: ")
if x.lower() == 'robot':
    playerX = Bot('X')
    playerO = Human('O')

elif x.lower() == "player":
    playerX = Human('X')
    playerO = Human('O')

else:
    print("Please select a valid choice")

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]
game = Game(playerX, playerO, board)
game.run()
#game.test()
