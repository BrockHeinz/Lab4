# By Brock Heinz (bch285@nau.edu) & Manu Hailame (mvh36@nau.edu)
import random


def main():
    print("WARNING: Depending on the font of your command line, the black" +
          " squares may show up as white, and vice versa.")
    print("         (I say this only because such is the case on my end.)")
    print("         The goal of the game is still to change all to black.")
    board = initBoard(False)
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


def initBoard(test):
    line = []
    base = []
    for outer in range(5):
        for inner in range(5):
            line.append("\N{BLACK SQUARE}")
        base.append(line)
        line = []
    if test:
        base[1][2] = toggle(base[1][2])
        base[3][2] = toggle(base[3][2])
        base[2][1] = toggle(base[2][1])
        base[2][3] = toggle(base[2][3])
    else:
        for _ in range(15):
            base = click(base, random.randint(0, 4), random.randint(0, 4))
    return base


def printBoard(board):
    print("\n        1 2 3 4 5")
    for outer in range(5):
        line = "      " + str(outer + 1) + " "
        for inner in range(5):
            line += board[outer][inner] + " "
        print(line)
        line = "      "
    print("\n")


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
