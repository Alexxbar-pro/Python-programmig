# -*- coding: utf-8 -*- 

import random
import time

count = 0

example_board = [ '''
| X |   |   |              | 7 | 8 | 9 |
-------------              -------------
|   | X |   |              | 4 | 5 | 6 |
-------------              -------------
|   |   | X |              | 1 | 2 | 3 |'''
]

def introduction():
    print()
    print('ESTE ES EL JUEGO DEL TA-TE-TI')
    for i in example_board:
        print(i)
        print()
        time.sleep(2)
    print('Tendrás que escoger un jugador ya sea \'X\' u \'O\' y si juntas 3 casillas seguidas ya sea en vertical diagonal u horizontal,')
    print('¡Habrás ganado!')
    print()
    time.sleep(2)
    print('En el ejemplo de las casillas que está arriba te deje el orden de como irán acomodadas y para escoger una')
    print('tendrás que seleccionar el número correspondiente a la casilla.')
    time.sleep(2)
 
def grid():

    print("| " + turn[6] + " | " + turn[7] + " | " + turn[8] + " |")
    print("-" * 13)
    print("| " + turn[3] + " | " + turn[4] + " | " + turn[5] + " |")
    print("-" * 13)
    print("| " + turn[0] + " | " + turn[1] + " | " + turn[2] + " |")

def cls():
    print("\n"*5)

def win_case(iput):
    if turn[0] == turn[1] == turn[2] == iput or turn[4] == turn[5] == turn[3] == iput or turn[7] == turn[8] == turn[6] == iput or turn[0] == turn[3] == turn[6] == iput or turn[1] == turn[4] == turn[7] == iput or turn[2] == turn[5] == turn[8] == iput or turn[0] == turn[4] == turn[8] == iput or turn[2] == turn[4] == turn[6] == iput:
        return 1
    else:
        return 0
 
def check_correct_ip():
    while True:
        try:
            return int(input("Que casilla escoges : ")) - 1
        except:
            print("Ingresa solo numeros porfavor!")
  
def user_turn(count):
    while count < 9:

        temp = check_correct_ip()
        while turn[temp] != ' ':
            print("Esa casilla ya esta ocupada!")
            print()
            temp = int(input("Que casilla escoges : ")) - 1
        else:
            cls()
            turn[temp] = user
            grid()
            count += 1

            if win_case(user):
                print("FELICIDADES GANASTE!! ")
                exit(0)
            else:
                com_turn(count)
        print("Juego empatado!!! Intenta de nuevo.")
        exit(0)


def com_turn(count):
    while count < 9:
        temp = random.randint(0, 8)

        while turn[temp] != ' ':
            temp = random.randint(0, 8)

        cls()
        turn[temp] = computer
        grid()
        count += 1

        if win_case(computer):
            print("Perdiste! Suerte la proxima.")
            exit(0)
        else:
            user_turn(count)
        print("Juego empatado!!! Intenta de nuevo.")
        exit(0)



def toss():
    if user == 'X':
        user_turn(count)
    else:
        com_turn(count)

turn = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

introduction()
print()
print('En este juego el jugador \'X\' siempre empieza primero, asi que sabiendo eso, ')
while True:
    user = (input("Que jugador te gustaría ser el \'X\' o el \'O\'?: ")).upper()
    print()
    if user == 'X':
        computer = 'O'
        break
    elif user == 'O':
        computer = 'X'
        break
    else:
        print("SOLO ESCOGE \'X\' U \'O\' POR FAVOR!")
        print()



grid()
toss()
