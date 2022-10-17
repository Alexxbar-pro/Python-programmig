# -*- coding: utf-8 -*-
import random
import time


TABLERO_EJEMPLO = ['''
| X | _ | _ |              | 7 | 8 | 9 |
| _ | X | _ |              | 4 | 5 | 6 |
| _ | _ | X |              | 1 | 2 | 3 |'''
]


def introduccion():
    print()
    print('ESTE ES EL JUEGO DEL TA-TE-TI')
    for i in TABLERO_EJEMPLO:
        print(i)
        print()
        time.sleep(1)
    print('Tendrás que escoger un jugador ya sea \'X\' u \'O\' y si juntas 3 casillas seguidas ya sea en vertical diagonal u horizontal,')
    print('¡Habrás ganado!')
    print()
    time.sleep(1)
    print('En el ejemplo de las casillas que está arriba te deje el orden de como irán acomodadas y para escoger una')
    print('tendrás que seleccionar el número correspondiente a la casilla.')


def desicion(count):
    print()
    print('En este juego el jugador \'X\' siempre empieza primero, asi que sabiendo eso, ')
    #time.sleep(2)
    while True:
        usuario = input('Que jugador te gustaría ser el \'X\' o el \'O\'?: ').upper()
        if usuario == 'X':
            compu = 'O'
            print('Muy bien, entonces tu seras el jugador \'X\' y yo el \'O\'')
            imprimir_tablero()
            return usuario, compu, 0
        elif usuario == 'O':
            compu = 'X'
            print('Muy bien, entonces tu seras el jugador \'O\' y yo el \'X\'')
            count = compu_turn(compu, count)
            imprimir_tablero()
            return usuario, compu, count
        else:
            print()
            print('¡Porfavor solo escoge \'X\' u \'O\'!')
            print()
            continue


TABLERO_REAL = [
    ['|', '_', '|', '_', '|', '_', '|'],
    ['|', '_', '|', '_', '|', '_', '|'],
    ['|', '_', '|', '_', '|', '_', '|']
]


def imprimir_tablero():
    for fila in TABLERO_REAL:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end=('\n'))
            else:
                print(fila[i], end=(' '))
                print(end=(''))


def checar_ganador(jugador):
        if TABLERO_REAL[2][1] == TABLERO_REAL[2][3] == TABLERO_REAL[2][5] == jugador or TABLERO_REAL[1][1] == TABLERO_REAL[1][3]   == TABLERO_REAL[1][5] == jugador or TABLERO_REAL[0][1] == TABLERO_REAL[0][3] == TABLERO_REAL[0][5] == jugador or     TABLERO_REAL[2][1] == TABLERO_REAL[1][1] == TABLERO_REAL[0][1] == jugador or TABLERO_REAL[2][3] == TABLERO_REAL[1][3] == TABLERO_REAL[0][3] == jugador or TABLERO_REAL[2][5] == TABLERO_REAL[1][5] == TABLERO_REAL[0][5] == jugador or TABLERO_REAL[2][5] == TABLERO_REAL[1][3] == TABLERO_REAL[0][1] == jugador or TABLERO_REAL[2][1] == TABLERO_REAL[1][3] == TABLERO_REAL[0][5] == jugador:
            return 1
        else:
            return 0

def compu_turn(compu, count):
    contador = 0
    while True:
        fila = random.randint(0, 2)
        casilla = random.choice([1, 3, 5])
        if TABLERO_REAL[fila][casilla] != '_':
            contador += 1
            if contador == 9:
                return contador
            else:
                continue
        else:
            TABLERO_REAL[fila][casilla] = compu
            count +=1
            if checar_ganador(compu):
                imprimir_tablero()
                print('Gano el jugador:', compu)
                exit(0)
            return count


count = 0
#introduccion()
jugador, compu, count = desicion(count)


while count < 9:                 
                     
    if jugador == 'X' or jugador == 'O':
        eleccion = int(input('Que casilla escoges: '))

        if eleccion == 1:
            if TABLERO_REAL[2][1] != '_' :
                print('Esta casilla esta ocupada, elige otra!')
                print()
                continue
            else:
                TABLERO_REAL[2][1] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
             
        elif eleccion == 2:
            if TABLERO_REAL[2][3] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[2][3] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
            

        elif eleccion == 3:
            if TABLERO_REAL[2][5] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[2][5] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
            
            
        elif eleccion == 4:
            if TABLERO_REAL[1][1] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[1][1] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
            
                
        elif eleccion == 5:
            if TABLERO_REAL[1][3] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[1][3] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
            
                
        elif eleccion == 6:
            if TABLERO_REAL[1][5] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[1][5] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
            
            
        elif eleccion == 7:
            if TABLERO_REAL[0][1] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[0][1] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
            

        elif eleccion == 8:
            if TABLERO_REAL[0][3] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[0][3] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
            
                
        elif eleccion == 9:
            if TABLERO_REAL[0][5] != '_':
                print('Esta casilla esta ocupada, elige otra!')
                continue
            else:
                TABLERO_REAL[0][5] = jugador
                count += 1
                if checar_ganador(jugador):
                    imprimir_tablero()
                    print('Ganaste jugador:', jugador)
                    exit(0)
                count = compu_turn(compu, count)
                imprimir_tablero()
                print(count)
        else:
            print('Elige un posicion valida.')
            print()
            continue
                    
print('El juego se empato, suerte la proxima!')
