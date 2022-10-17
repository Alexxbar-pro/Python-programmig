#Es un codigo echo para dar un mensaje aleatorio dependiendo del numero que el jugador ingrese.

import time
import random

def Introduccion():
    print()
    print('Bienvenido!')
    Nombre = input('Cual es tu nombre? ' )
    print('Bueno, ' + Nombre + ' este es un juego en el cual vas a descubirir lo que el mundo te quiere decir atraves de un mensaje.')
    print('En el momento que escojas un numero del "1" al "2" el sistema escojera un mensaje que te ayudara en tu vida.')
    return Nombre    

def Decidir(nombreDelJugador):
    decision = ''
    while decision != 'Si' and decision != 'si':
        print('Te gustaria probar tu suerte ' + nombreDelJugador + '?')
        decision = input('(Si o No): ')

def Mensajes():

    print('Excelente entoces elige un numero del "1" al "2" y veras lo que el mundo te quiere decir ')
    elegido = int(input('Ingresa el numero: '))
    print()
    print('Peparate!')
    time.sleep(2)
    print('Lo que el mundo te quiere decir es...')
    time.sleep(2)
    print()
    Numero = random.randint(1, 2)
    numero = random.randint(1, 2)
    if elegido == Numero:
        print('Estas cerca de conseguir uno de tus sueños')
    elif elegido == numero:
        print('Alguien te va a traicionar')
    else:
        print('Tu suerte esta de la verga')

nombreDelJugador = Introduccion()
Decidir(nombreDelJugador)

jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 'Si':
    Mensajes()

    print('Quieres juagar de nuevo?')
    jugarDeNuevo = input()


    





