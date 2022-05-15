# Importing package
import sys


# Creating a class named Player
class Player(object):
    def __init__(self, color, name):
        self.name = name
        self.color = color


# Creating a class for the AI player
class AIPlayer(Player):

    def __init__(self,  color):
        self.color = color


class GameManager(object):

    def __init__(self, dimension=8):

        self.dimension = dimension
        self.board = self.create_new_board()
        self.current_player = 1

    def create_new_board(self, n):
        board = []

        if n < 4:
            print('The size of the board must be more than 3')
            return board

        if n % 2 != 0:
            print('The size of the board must be an even number.')
            return board

        if n > 15:
            print('The size of the board must not be greater than 15.')
            return board

        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            board.append(row)
            board[i][j] = 1
            board[i + 1][j + 1] = 1
            board[i + 1][j] = -1
            board[i][j + 1] = -1
            final = []
            for row in board:
                final.append(tuple(row))
            return board


        def print_board(self):
            for row in self.board:
                print(" ".join([str(x) for x in row]))
