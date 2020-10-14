# By Brock Heinz (bch285@nau.edu) & Manu Hailame (mvh36@nau.edu)
import random


def main():
    board = initBoard()
    printBoard(board)
    xInput = -1
    yInput = -1
    numMoves = 0
    while not isDark(board):
        print("Please choose a row number (0-4): ")
        yInput = input()
        print("Please choose a column number (0-4): ")
        xInput = input()
        board = click(board, int(xInput), int(yInput))
        printBoard(board)
        numMoves += 1
        print("Moves: " + str(numMoves))
    print("You win!")


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
    board[y][x] = toggle(board[y][x])
    if (x > 0):
        board[y][x - 1] = toggle(board[y][x - 1])
    if (x < 4):
        board[y][x + 1] = toggle(board[y][x + 1])
    if (y > 0):
        board[y - 1][x] = toggle(board[y - 1][x])
    if (y < 4):
        board[y + 1][x] = toggle(board[y + 1][x])
    return board


def toggle(tile):
    if tile == "#":
        return "O"
    else:
        return "#"


def isDark(board):
    for outer in range(5):
        for inner in range(5):
            if board[outer][inner] == "#":
                return False
    return True


main()
