# By Brock Heinz (bch285@nau.edu) & Manu Hailame (mvh36@nau.edu)
import random


def main():
    board = initBoard()
    printBoard(board)
    xInput = -1
    yInput = -1
    prevX = -2
    prevY = -2
    numMoves = 0
    while not isDark(board):
        print("Please choose a row number (1-5): ")
        yInput = input()
        print("Please choose a column number (1-5): ")
        xInput = input()
        board = click(board, int(xInput) - 1, int(yInput) - 1)
        printBoard(board)
        # Increment move count if unique move, decrement if undoing last
        # move
        if xInput == prevX and yInput == prevY:
            numMoves -= 1
            prevX = -2
            prevY = -2
        else:
            numMoves += 1
            prevX = xInput
            prevY = yInput
        print("Moves: " + str(numMoves))
    print("You won with " + str(numMoves) + " moves!")


def initBoard():
    line = []
    base = []
    for outer in range(5):
        for inner in range(5):
            if random.randint(0, 1) == 0:
                line.append("\N{WHITE SQUARE}")
            else:
                line.append("\N{BLACK SQUARE}")
        base.append(line)
        line = []
    return base


def printBoard(board):
    line = "      "
    for outer in range(5):
        for inner in range(5):
            line += board[outer][inner] + " "
        print(line)
        line = "      "


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
    if tile == "\N{WHITE SQUARE}":
        return "\N{BLACK SQUARE}"
    else:
        return "\N{WHITE SQUARE}"


def isDark(board):
    for outer in range(5):
        for inner in range(5):
            if board[outer][inner] == "\N{WHITE SQUARE}":
                return False
    return True


main()
