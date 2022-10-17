#INICIO
import time
print('bienvenido al juego')
nombre1=input('Jugador X introduce tu nombre: ')
nombre2=input('Jugador O introduce tu nombre: ')

#PRESENTACION
print('Inician las X')
print('posiciones del tablero')
print('|1|2|3|\n|4|5|6|\n|7|8|9|')

#JUEGO
jugadasrestantes=9
matriz=['_','_','_','_','_','_','_','_','_']
while jugadasrestantes>0:
    if matriz[0]==matriz[1]==matriz[2]=='X' or matriz[3]==matriz[4]==matriz[5]=='X' or matriz[6]==matriz[7]==matriz[8]=='X' or matriz[0]==matriz[3]==matriz[6]=='X' or matriz[1]==matriz[4]==matriz[7]=='X' or matriz[2]==matriz[5]==matriz[8]=='X' or matriz[0]==matriz[4]==matriz[8]=='X' or matriz[2]==matriz[4]==matriz[6]=='X':
        Ganador=nombre1
        break
    elif matriz[0]==matriz[1]==matriz[2]=='O' or matriz[3]==matriz[4]==matriz[5]=='O' or matriz[6]==matriz[7]==matriz[8]=='O' or matriz[0]==matriz[3]==matriz[6]=='O' or matriz[1]==matriz[4]==matriz[7]=='O' or matriz[2]==matriz[5]==matriz[8]=='O' or matriz[0]==matriz[4]==matriz[8]=='O' or matriz[2]==matriz[4]==matriz[6]=='O':
        Ganador=nombre2
        break
    elif jugadasrestantes%2!=0:
        print('quedan ',jugadasrestantes,'jugadas')
        jugada=int(input('Juega X\nIngresa la posicion (1-9) para jugar '))
        if jugada>9:
            print('ese movimiento no esta permitido, intente nuevamente ')
            continue
        if matriz[jugada-1]!='_':
            print('esa posicion ya estÃ¡ jugada, prueba con otra')
            continue
        matriz[jugada-1]='X'
        print(' |',matriz[0],'|',matriz[1],'|',matriz[2],'|','\n','|',matriz[3],'|',matriz[4],'|',matriz[5],'|','\n','|',matriz[6],'|',matriz[7],'|',matriz[8],'|')
        jugadasrestantes=jugadasrestantes-1
    elif jugadasrestantes%2==0:
        print('quedan ',jugadasrestantes,'jugadas')
        jugada=int(input('Juega O\nIngresa la posicion (1-9) para jugar '))
        if jugada>9:
            print('ese movimiento no esta permitido, intente nuevamente ')
            continue
        if matriz[jugada-1]!='_':
            print('esa posicion ya estÃ¡ jugada, prueba con otra')
            continue
        matriz[jugada-1]='O'
        print(' |',matriz[0],'|',matriz[1],'|',matriz[2],'|','\n','|',matriz[3],'|',matriz[4],'|',matriz[5],'|','\n','|',matriz[6],'|',matriz[7],'|',matriz[8],'|')
        jugadasrestantes=jugadasrestantes-1

#FIN DE PARTIDA
if matriz[0]==matriz[1]==matriz[2] or matriz[3]==matriz[4]==matriz[5] or matriz[6]==matriz[7]==matriz[8] or matriz[0]==matriz[3]==matriz[6] or matriz[1]==matriz[4]==matriz[7] or matriz[2]==matriz[5]==matriz[8] or matriz[0]==matriz[4]==matriz[8] or matriz[2]==matriz[4]==matriz[6]:
    print('Â¡Felicidades ',Ganador,'! Has ganado la partida')
else:
    print('Empate')
time.sleep(10)