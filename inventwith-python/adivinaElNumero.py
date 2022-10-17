# Este es el juego de adivinar el número.
import random

intentosRealizados = 0

print('Hola! Cómo te llamas?')
miNombre = input('Ingresa tu nombre jugador: ')

numero = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando en un numero entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimacion = input('# ')
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimacion es muy baja.')

    if estimacion > numero:
        print('Tu estimacion es muy alta')

    if estimacion == numero:
     break    

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Buen trabajo, ' + miNombre + ', Has adivinado mi numero en '+
 intentosRealizados + ' intentos!')

if estimacion != numero:
    numero = str(numero)
    print('Pues no. El numero que estaba pensando era ' + numero)      
        

        
