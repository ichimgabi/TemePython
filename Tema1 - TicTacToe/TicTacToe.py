import random


# print_board afiseaza tabla;
def print_board():
    for index_spatiu, spatiu in enumerate(tabla):
        print(spatiu + "|", end=" ")
        if index_spatiu == 2 or index_spatiu == 5 or index_spatiu == 8:
            print("\n")


# is_win_x si is_win_o verifica toate combinatiile posibile de castig ale jucatorilor;
def is_win(move):
    if tabla[0] == tabla[3] == tabla[6] == move:
        return True
    elif tabla[0] == tabla[1] == tabla[2] == move:
        return True
    elif tabla[6] == tabla[7] == tabla[8] == move:
        return True
    elif tabla[2] == tabla[5] == tabla[8] == move:
        return True
    elif tabla[0] == tabla[4] == tabla[8] == move:
        return True
    elif tabla[2] == tabla[4] == tabla[6] == move:
        return True
    elif tabla[1] == tabla[4] == tabla[7] == move:
        return True
    elif tabla[3] == tabla[4] == tabla[5] == move:
        return True
    else:
        return False


# computer_moves alege mutarile pe care le poate face calculatorul, respectand regulile din cerinta;
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


tabla = [" " for i in range(9)]
choice = ["X", "O"]
# Variabila start retine care dintre jucatori incepe jocul (X este primul, O este al doilea);
start = random.choice(choice)
nr_moves = 0

if start == "X":
    print_board()
    while True:
        m = int(input("Mutarea jucatorului: "))
        if tabla[m - 1] == " ":
            tabla[m - 1] = "X"
            nr_moves += 1
            if is_win("X"):
                print("Ai castigat!")
                break
            if nr_moves == 9:
                print("Egalitate")
                break
            print("Mutarea calculatorului")
            computer_moves("O")
            print_board()
            if is_win("O"):
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
        m = int(input("Mutarea jucatorului: "))
        if tabla[m - 1] == " ":
            tabla[m - 1] = "O"
            nr_moves += 1
            if is_win("O"):
                print("Ai castigat!")
                break
            if nr_moves == 9:
                print("Egalitate")
                break
            print("Mutarea calculatorului")
            computer_moves("X")
            print_board()
            nr_moves += 1
            if is_win("X"):
                print("Ai pierdut!")
                break
            if nr_moves == 9:
                print("Egalitate")
                break
        else:
            print("Mutare invalida!")
