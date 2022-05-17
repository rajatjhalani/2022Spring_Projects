# This code is refereed from https://medium.com/@gregoryg323/building-the-classic-othello-board-game-for-ai-8a42ba2d7f13
# and modified based on the requirements.


from tkinter import *


class Gui(object):
    def __init__(self, game_manager, player1, player2):

        self.game = game_manager
        self.players = player1, player2
        self.height = self.game.dimension
        self.width = self.game.dimension
        self.offset = 1
        self.cell_size = 20


        root = Tk()
        root.wm_title("Reversi")
        self.canvas = Canvas(root, height=self.cell_size * self.height,
                             width=self.cell_size * self.width)
        self.move_label = Label(root)
        self.score_label = Label(root)
        self.draw_board()

    def draw_board(self):
        self.draw_grid()
        self.draw_disks()
        player = "Black" if self.game.current_player == 1 else "White"
        self.move_label["text"] = player

    def draw_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                self.canvas.create_rectangle(i * self.cell_size + self.offset, j * self.cell_size + self.offset)

