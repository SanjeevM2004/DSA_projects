
import copy
from sudokuGenerator import *

Board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

solvedBoard = copy.deepcopy(Board)

def solve(board):
    # end condition:- getting to the end of the board - the function findEmpty return NONE
    find = findEmpty(board)
    if find is None:  # if find != False
        return True
    else:
        row, col = find
    for number in range(1, 10):
        if validCheck(board, number, (row, col)):
            board[row][col] = number
            if solve(board):
                return True
            board[row][col] = 0
    return False


def mainSolver(level):
    sudokuGenerate(Board, level)
    solvedBoard = copy.deepcopy(Board)
    solve(solvedBoard)
    return solvedBoard
   #Done