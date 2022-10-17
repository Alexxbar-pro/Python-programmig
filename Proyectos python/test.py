
import random
tablero=[['_','_','_'], ['_','_','_'],['_','_','_']]
tab=tablero.copy()

tablero_0=("|a|b|c|\n |d|e|f|\n |g|h|i|")

def mostrar_tablero():
    print('|',tab[0][0],'|',tab[0][1],'|',tab[0][2],'|\n|',tab[1][0],'|',tab[1][1],'|',tab[1][2],'|\n|',tab[2][0],'|',tab[2][1],'|',tab[2][2],'|')


def elegir_simbolo():
    print('Â¿Quiere usar X o O?')
    sim=input().upper()
    return sim


def cambia_posicion_h(sim):
    print('Teniendo en cuenta las posiciones \n',tablero_0,'\nÂ¿DÃ³nde desea poner la ',sim,'?')
    pos=input().lower()
    if pos=='a':
        if tab[0][0]=='_':
            tab[0][0]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='b':
        if tab[0][1]=='_':
            tab[0][1]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='c':
        if tab[0][2]=='_':
            tab[0][2]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='d':
        if tab[1][0]=='_':
            tab[1][0]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='e':
        if tab[1][1]=='_':
            tab[1][1]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='f':
        if tab[1][2]=='_':
            tab[1][2]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='g':
        if tab[2][0]=='_':
            tab[2][0]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='h':
        if tab[2][1]=='_':
            tab[2][1]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    elif pos=='i':
        if tab[2][2]=='_':
            tab[2][2]=sim
        else:
            print('La posiciÃ³n se encuentra ocupada')
            cambia_posicion_h(sim)
    else:
        print("La posiciÃ³n es invÃ¡lida")
        cambia_posicion_h(sim) 

def cambia_posicion_M(sim):
    pos=posicion_random()
    if pos=='a':
        if tab[0][0]=='_':
            tab[0][0]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='b':
        if tab[0][1]=='_':
            tab[0][1]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='c':
        if tab[0][2]=='_':
            tab[0][2]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='d':
        if tab[1][0]=='_':
            tab[1][0]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='e':
        if tab[1][1]=='_':
            tab[1][1]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='f':
        if tab[1][2]=='_':
            tab[1][2]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='g':
        if tab[2][0]=='_':
            tab[2][0]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='h':
        if tab[2][1]=='_':
            tab[2][1]=sim
        else:
            cambia_posicion_M(sim)
    elif pos=='i':
        if tab[2][2]=='_':
            tab[2][2]=sim
        else:
            cambia_posicion_M(sim)

     


def posicion_random():
    pos=random.choice(['a','b','c','d','e','f','g','h','i'])
    return pos


def verificar_triqui():
    a=True
    if tab[0][0]==tab[0][1]==tab[0][2] and tab[0][0]!='_':
        print('Juego terminado, ha ganado la ',tab[0][0])
        return a
    elif tab[1][0]==tab[1][1]==tab[1][2] and tab[1][0]!='_':
        print('Juego terminado, ha ganado la ',tab[1][0])
        return a
    elif tab[2][0]==tab[2][1]==tab[2][2] and tab[2][0]!='_':
        print('Juego terminado, ha ganado la ',tab[2][0])
        return a
    elif tab[0][0]==tab[1][0]==tab[2][0] and tab[0][0]!='_':
        print('Juego terminado, ha ganado la ',tab[0][0])
        return a
    elif tab[0][1]==tab[1][1]==tab[2][1] and tab[0][1]!='_':
        print('Juego terminado, ha ganado la ',tab[0][1])
        return a
    elif tab[0][2]==tab[1][2]==tab[2][2] and tab[0][2]!='_':
        print('Juego terminado, ha ganado la ',tab[0][2])
        return a
    elif tab[0][0]==tab[1][1]==tab[2][2] and tab[0][0]!='_':
        print('Juego terminado, ha ganado la ',tab[0][0])
        return a
    elif tab[0][2]==tab[1][1]==tab[2][0] and tab[0][2]!='_':
        print('Juego terminado, ha ganado la ',tab[0][2])
        return a
    else:
        a=False
        return a

def verificar_empate():
    a=0
    for col in range(0,3):
        for fil in range(0,3):
            if tab[fil][col]=='_':
                a+=1
    if a==0:
        print('El juego estÃ¡ empatado')
        return True
    else:
        return False

def empezar_juego():
    A=input('Â¿Desea jugar Ta-Te-Ti? Escribe si o no ')
    if A=='si':
        sim=elegir_simbolo()
        while verificar_triqui()==False:
            if verificar_empate()==False:
                if sim=='X':
                    simM='O'
                    cambia_posicion_h(sim)
                    mostrar_tablero()
                    if verificar_triqui()==False and verificar_empate()==False:
                            print('Turno del computador')
                            cambia_posicion_M(simM)
                            mostrar_tablero()
                elif sim=='O':
                    simM='X'
                    print('Turno del computador')
                    cambia_posicion_M(simM)
                    mostrar_tablero()
                    if verificar_triqui()==False and verificar_empate()==False:
                            cambia_posicion_h(sim)
                            mostrar_tablero()
            else:
                break
        else:
            pass
    elif A=='no':
        print('Gracias por utilizar la aplicaciÃ³n')
    else:
        print('Respuesta no valida, intenta de nuevo')
        empezar_juego()


empezar_juego()

