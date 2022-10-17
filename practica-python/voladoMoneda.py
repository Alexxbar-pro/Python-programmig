# utf-8

import random
import time

def Intro():
    print()
    print('Trata de adivinar de que lado caera la moneda, cara o aguila.')
    time.sleep(1)
    print('El numero 1 representa la cara y el numero 2 representa al aguila,')
    desicion = int(input('Que escoges?: '))
    return desicion

def Volado(desicion):
    time.sleep(1)
    print()
    print('Tu escogiste ' + str(desicion), end=(', '))
    if desicion == 1:
        print('que representa cara')
    elif desicion == 2:
        print('que representa aguila')
    else:
        print('Solo escoge 1 o 2 porfavor')

    moneda = random.randint(1, 2)

    if moneda == desicion:
        if moneda == 1:
            time.sleep(1)
            print('Y la moneda tambien salio cara, Ganaste!')
        elif moneda == 2:
            time.sleep(1)
            print('Y la moneda tambien salio aguila, Ganaste!')
    elif desicion == 1 or desicion == 2:
        time.sleep(1)
        print('Pero la moneda salio', end=(' '))
        if moneda == 1:
            print('cara, Perdiste!')
        else:
            print('aguila, Perdiste!')
    else:
        print('sigue las instrucciones puta')

jugarDeNuevo = 'Si'
while jugarDeNuevo == 'Si':
    desicion = Intro()
    Volado(desicion)
    print()
    time.sleep(1)
    jugarDeNuevo = input('''Quieres jugar de nuevo? 
(si o no): ''').capitalize()
    