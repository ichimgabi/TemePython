import sys


def enter_number():
    try:
        n = input("Primul numar: ")
        n = float(n)
    except ValueError:
        print("Inputul nu este un numar valid")
        sys.exit(-1)
    else:
        return n


def operator_valid():
    opp = input("Operatorul dorit: ")
    if opp not in "+-/*^V":
        print("Operator invalid")
        sys.exit(-1)
    return opp


no1 = enter_number()
print("Primul numar introdus este: ", no1)
op = operator_valid()
print("Operatorul introdus este: ", op)
no2 = enter_number()
print("Al doilea numar introdus este: ", no2)


def main():
    if op == '+':
        print("Rezultatul este: ", no1 + no2)
    elif op == '-':
        print("Rezultatul este: ", no1 - no2)
    elif op == '*':
        print("Rezultatul este: ", no1 * no2)
    elif op == '^':
        print("Rezultatul este: ", pow(no1, no2))
    elif op == 'V':
        if no1 < 0:
            print("Eroare matematica")
        else:
            print("Rezultatul este: ", pow(no1, 1/no2))
    elif op == '/':
        try:
            division = no1/no2
        except ZeroDivisionError:
            print("Impartirea la 0 nu este permisa")
        else:
            print("Rezultatul este: ", division)
