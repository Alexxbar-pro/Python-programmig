import random
import time

def introduccion():
    print()
    print('Bienvenido al juego de los dados!')
    time.sleep(2)


def decision():
    decision = ('')
    while decision !='si' and decision != 's':
        print('Te atreves a jugar?')
        decision = input('Si o no: ')

    print()
    print('Buena decisión')
    time.sleep(1)
    print('Bueno entonces empecemos...')
    time.sleep(2)



def lanzador():  

    print()
    print('Me preparo para arrojar los dados...')
    print()
    time.sleep(2)
    print('Los arrojo a la mesa y...')

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    time.sleep(2)

    print('Los dados caen en:', dado1,'y', dado2)
    print()
    time.sleep(1)
    print('La suma de los números dan:', dado1 + dado2)


#introduccion() 
#decision()  

jugarDeNuevo = 'Si'
while jugarDeNuevo == 'Si' or jugarDeNuevo == 'No' or jugarDeNuevo != 'Si' or jugarDeNuevo != 'No':
    if jugarDeNuevo != 'Si' and jugarDeNuevo != 'No':
        print('Ingresa si o no prro')
    elif jugarDeNuevo == 'No':
        print('Hasta luego puta')
        break
    else:
        lanzador()  

    time.sleep(1)

    print()
    print('Quieres que lancé de nuevo los dados? (si o no)')
    jugarDeNuevo = input().capitalize()
