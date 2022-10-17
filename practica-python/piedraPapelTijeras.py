# utf-8

import random
import time

def main():
    print()
    print('Este es el juego de piedra, papel o tijeras')
    print()
    time.sleep(1)
    print('Para que no tengas que escribir todo la palabra vamos a representar las palabras con numeros')
    time.sleep(1)
    print('1 = piedra, 2 = papel, 3 = tijeras')
    print()
    time.sleep(1)
    print('''Las reglas del juego por si no las conoces son: 
piedra rompe tijeras,
tijeras corta papel 
y papel envuelve a pierda''')
    print()
    time.sleep(1)
    

def operacion():
    print('Empiezas, que escoges?')
    opcion = int(input('num: '))
    
    generador = random.randint(1, 3)  

    
    if opcion == generador:
        print('Yo escogí', end=' ')
        if generador == 1:
            print('pierda')
            print('Y tu tambien escogiste piedra, Es un empate, intenta de nuevo.')
            
        elif generador == 2:
            print('papel')
            print('Y tu tambien escogiste papel, Es un empate, intenta de nuevo.')
                
        elif generador == 3:
            print('tijeras')
            print('Y tu tambien escogiste tijeras, Es un empate, intenta de nuevo.')
                
    elif opcion != generador:
        print('yo escogi ' + str(generador))
        print()
        if opcion == 3 and generador == 1:
            print('y como Piedra rompe tijeras, yo gano!')
                
        elif opcion == 1 and generador == 2:
            print('y como papel envuelve piedra, yo gano!')
                
        elif opcion == 2 and generador == 3:
            print('y como tijeras corta papel, yo gano!')
                
        elif opcion == 2 and generador == 1:
            print('y como papel envuelve pierda, tu ganas!')
                
        elif opcion == 1 and generador == 3:
            print('y como piedra rompe tijeras, tu ganas!')
                
        elif opcion == 3 and generador == 2:
            print('y como tijeras corta papel, tu ganas!')
        else:
            print('Solo escoge un numero del 1 al 3 porfavor')


while True:
    main()
    operacion()
    otherChance = input('Quieres jugar de nuevo?: ').capitalize()
    
    if otherChance == 'Si':
        main()
        operacion()
    else:
        print('Nos vemos despues!')
        break





