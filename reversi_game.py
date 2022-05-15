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

    def create_new_board(self):
        board = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                row.append(0)
            board.append(row)

