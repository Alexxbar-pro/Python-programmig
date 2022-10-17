#Es un codigo echo para dar un mensaje aleatorio dependiendo del numero que el jugador ingrese.

import time
import random

def Introduccion():
    print()
    print('Bienvenido!')
    Nombre = input('Cual es tu nombre? ' )
    print()
    print('Bueno, ' + Nombre + ' este es un juego en el cual vas a descubirir lo que el mundo te quiere decir atraves de un mensaje.')
    print()
    time.sleep(1)
    print('En el momento que escojas un numero el sistema generara el mensaje que te ayudara en tu vida.')
    return Nombre    

def Decidir(nombreDeljugador):
    decision = ''
    while decision != 'Si' and decision != 'si':
        print('Te gustaria probar tu suerte ' + nombreDelJugador + '?')
        decision = input('(Si o No): ')

def Mensajes():
    print()
    print('Excelente entoces elige un numero del "1" al "5" y veras lo que el mundo te quiere decir')
    elegido = int(input('Ingresa el numero: '))
    print()
    print('Peparate!')
    time.sleep(2)
    print('Lo que el mundo te quiere decir es...')
    time.sleep(2)
    print()

    oracionesDeSuerte = ['Estas cerca de conseguir uno de tus sueños!', 'Alguien va a traicionarte! TEN CUIADO.', 'Muy pronto tendras a esa chava tan especial para ti!', 'Deja el miedo, la desicion que tomes sera la correcta!', 'Ella no era para ti!']
    OracionSecreta = random.randint(0, len(oracionesDeSuerte) -1)
    print(oracionesDeSuerte[OracionSecreta])
    print()


nombreDelJugador = Introduccion()
Decidir(nombreDelJugador)

jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 'Si':
    Mensajes()

    print('Quieres juagar de nuevo?')
    jugarDeNuevo = input()


    





