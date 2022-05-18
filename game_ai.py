import numpy as np

from reversi_game import get_possible_moves

corners = [(0,0),(0,7),(7,0),(7,7)]

def get_board_weights(board):

    score = 0

    boardWeights = [
        [500, -150, 30, 10, 10, 30, -150, 500], \
        [-150, -250, 1, 1, 1, 1, -250, -150], \
        [30, 0, 1, 2, 2, 1, 0, 30], \
        [10, 0, 2, 16, 16, 2, 0, 10], \
        [10, 0, 2, 16, 16, 2, 0, 10], \
        [30, 0, 1, 2, 2, 1, 0, 30], \
        [-150, -250, 1, 1, 1, 1, -250, -150], \
        [500, -150, 30, 10, 10, 30, -150, 500]]

    white_score = 0
    black_score = 0
    blank_spaces = 0
    white_weighted = 0
    black_weighted = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                blank_spaces += 1
            elif board[i][j] == 1:
                black_score += 1
                black_weighted += boardWeights[i][j]
            elif board[i][j] == 2:
                white_score += 1
                white_weighted += boardWeights[i][j]

            if blank_spaces > 0:
                return black_weighted, white_weighted
            else:
                return black_score, white_score

# Using the minimax algorithm (pseudocode from lectures)
def minimax_1(depth, board):
    possible_moves = get_possible_moves(board)
    if depth == 0 or possible_moves == []:
        score = get_board_weights(board)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    return score[1] - score[0]
                else:
                    return score[0] - score[1]
        best_min_score = 99999


def minimax_2(depth, board, color):
    possible_moves = get_possible_moves(board, color)
    if depth == 0 or possible_moves == []:
        score = get_board_weights(board)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    return score[0] - score[1]
                else:
                    return score[1] - score[0]
        best_max_score = -99999
