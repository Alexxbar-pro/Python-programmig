import random
IMÁGENES_AHORCADO = ['''

 +---+
 |   |
     |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========='''] 

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigueña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

def obtenerPalabraAlAzar(listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
    espaciosVacios = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): #completras los espacios vacios con las letras adivinadas 
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

    for letra in espaciosVacios: # mostrar la palabra secreta con espacios entre cada letra 
        print(letra, end=' ')
    print()


def obtenerIntento(letrasProbadas):
    # devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado solo una letra, y no ota cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('ya has probado esa letra. Elige otra.')

        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('por favor ingresa una LETRA')
        else:
            return intento

def jugarDeNuevo():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

print()
print('A H O R C A D O')
letrasIncorectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras) 
juegoTerminado = False 

while True:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorectas, letrasCorrectas, palabraSecreta)

    # permite al jugador escribir una letra 
    intento = obtenerIntento(letrasIncorectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        # verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False 
                break
        if encontradoTodasLasLetras:
            print('¡Si! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            juegoTerminado = True

    else:
        letrasIncorectas = letrasIncorectas + intento

        #comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorectas) == len (IMÁGENES_AHORCADO)  - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespues de ' + str(len(letrasIncorectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True

    # preguntar al jugador si quiere volver a jugar (pero solo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break