# By Brock Heinz (bch285@nau.edu) & Manu Hailame ()
import random


def main():
    board = initBoard()
    printBoard(initBoard())
    


def initBoard():
    line = []
    base = []
    for outer in range(5):
        for inner in range(5):
            if random.randint(0,1) == 0:
                line.append("#")
            else:
                line.append("O")
            # '#' is considered On, 'O' is considered Off
        base.append(line)
        line = []
    return base


def printBoard(board):
    line = ""
    for outer in range(5):
        for inner in range(5):
            line += board[outer][inner] + " "
        print(line)
        line = ""


def click(board, x, y):
    


def isDark(board):
    


main()
