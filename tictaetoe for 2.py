# Primitive tic tae toe for 2 players
import numpy as np
gameboard = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]


def printboard():
    print("   \033[4m a b c\033[0m")
    for count, row in enumerate(gameboard):
        print(count, "|", row[0], row[1], row[2])


def player1turn():
    r1 = input("Player 1, it is your turn. Enter row -> ")
    while r1 not in ["0", "1", "2"]:
        r1 = input("You have entered invalid row. Please try again -> ")
    else:
        row1 = int(r1)
    c1 = input("Now enter column -> ")
    while c1.lower() not in ["a", "b", "c"]:
        c1 = input("You have entered invalid column. Please try again -> ")
    else:
        col = c1.lower()
    if col == 'a':
        col1 = 0
    if col == 'b':
        col1 = 1
    if col == 'c':
        col1 = 2
    if gameboard[row1][col1] == 0:
        gameboard[row1][col1] = 1
    else:
        print("This field is occupied. Please make another move")
        player1turn()
    return gameboard


def player2turn():
    r2 = input("Player 2, it is your turn. Enter row -> ")
    while r2 not in ["0", "1", "2"]:
        r2 = input("You have entered invalid row. Please try again -> ")
    else:
        row2 = int(r2)
    c2 = input("Now enter column -> ")
    while c2.lower() not in ["a", "b", "c"]:
        c2 = input("You have entered invalid column. Please try again -> ")
    else:
        col = c2.lower()
    if col == 'a':
        col2 = 0
    if col == 'b':
        col2 = 1
    if col == 'c':
        col2 = 2
    if gameboard[row2][col2] == 0:
        gameboard[row2][col2] = 2
    else:
        print("This field is occupied. Please make another move")
        player2turn()
    return gameboard


def endgame():
    c = np.array(gameboard)
    for i in range(0, 2):
        if c[i][0] == c[i][1] == c[i][2] == 1 or \
            c[0][i] == c[1][i] == c[2][i] == 1 or \
            c[0][0] == c[1][1] == c[2][2] == 1 or \
                c[0][2] == c[1][1] == c[2][0] == 1:
            print("Player 1 won !!! \n")
            raise SystemExit
        elif c[i][0] == c[i][1] == c[i][2] == 2 or \
            c[0][i] == c[1][i] == c[2][i] == 2 or \
            c[0][0] == c[1][1] == c[2][2] == 1 or \
                c[0][2] == c[1][1] == c[2][0] == 2:
            print("Player 2 won !!!\n")
            raise SystemExit
        elif c.min() == 1:
            print("Draw!!! \n")
            raise SystemExit


def main_loop():
    while True:
        printboard()
        player1turn()
        printboard()
        endgame()
        player2turn()
        printboard()
        endgame()


main_loop()
