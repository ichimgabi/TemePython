import random

tabla = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
choice = ["X", "O"]
start = random.choice(choice)
nr_moves = 0
win = 0


def print_board():
    k = 0
    for i in tabla:
        print(i + "|", end=" ")
        k += 1
        if k == 3:
            print("\n")
        if k == 6:
            print("\n")
        if k == 9:
            print("\n")


def is_win_x():
    if tabla[0] == tabla[3] == tabla[6] == "X":
        return 1
    elif tabla[0] == tabla[1] == tabla[2] == "X":
        return 1
    elif tabla[6] == tabla[7] == tabla[8] == "X":
        return 1
    elif tabla[2] == tabla[5] == tabla[8] == "X":
        return 1
    elif tabla[0] == tabla[4] == tabla[8] == "X":
        return 1
    elif tabla[2] == tabla[4] == tabla[6] == "X":
        return 1
    elif tabla[1] == tabla[4] == tabla[7] == "X":
        return 1
    elif tabla[3] == tabla[4] == tabla[5] == "X":
        return 1
    else:
        return 0


def is_win_o():
    if tabla[0] == tabla[3] == tabla[6] == "O":
        return 1
    elif tabla[0] == tabla[1] == tabla[2] == "O":
        return 1
    elif tabla[6] == tabla[7] == tabla[8] == "O":
        return 1
    elif tabla[2] == tabla[5] == tabla[8] == "O":
        return 1
    elif tabla[0] == tabla[4] == tabla[8] == "O":
        return 1
    elif tabla[2] == tabla[4] == tabla[6] == "O":
        return 1
    elif tabla[1] == tabla[4] == tabla[7] == "O":
        return 1
    elif tabla[3] == tabla[4] == tabla[5] == "O":
        return 1
    else:
        return 0


def computer_moves(move):
    if tabla[4] == " ":
        tabla[4] = move
    elif tabla[0] == " ":
        tabla[0] = move
    elif tabla[2] == " ":
        tabla[2] = move
    elif tabla[6] == " ":
        tabla[6] = move
    elif tabla[8] == " ":
        tabla[8] = move
    elif tabla[1] == " ":
        tabla[1] = move
    elif tabla[3] == " ":
        tabla[3] = move
    elif tabla[5] == " ":
        tabla[5] = move
    elif tabla[7] == " ":
        tabla[7] = move


if start == "X":
    print_board()
    while True:
        m = input("Mutarea jucatorului: ")
        if tabla[int(m) - 1] == " ":
            tabla[int(m) - 1] = "X"
            nr_moves += 1
            win = is_win_x()
            if win == 1:
                print("Ai castigat!")
                break
            if nr_moves == 9:
                print("Egalitate")
                break
            print("Mutarea calculatorului")
            computer_moves("O")
            print_board()
            win = is_win_o()
            if win == 1:
                print("Ai pierdut!")
                break
            nr_moves += 1
        else:
            print("Mutare invalida!")
else:
    computer_moves("X")
    print_board()
    nr_moves += 1
    while True:
        m = input("Mutarea jucatorului: ")
        if tabla[int(m) - 1] == " ":
            tabla[int(m) - 1] = "O"
            nr_moves += 1
            win = is_win_o()
            if win == 1:
                print("Ai castigat!")
                break
            if nr_moves == 9:
                print("Egalitate")
                break
            print("Mutarea calculatorului")
            computer_moves("X")
            print_board()
            nr_moves += 1
            win = is_win_x()
            if win == 1:
                print("Ai pierdut!")
            if nr_moves == 9:
                print("Egalitate")
        else:
            print("Mutare invalida!")
