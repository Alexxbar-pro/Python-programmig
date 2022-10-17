# * Reto #3
#  * ¿ES UN NÚMERO PRIMO?
#  * Fecha publicación enunciado: 17/01/22
#  * Fecha publicación resolución: 24/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.

"""
Un numero primo es:
- Un número natural (Que sea entero y positivo)
- Mayor a 1
-Divisible SOLO para si mismo y entre 1 
"Un número es divisible cuando el resultado de ese numero dividido entre otro es 0
"""
# Todos los números son divisibles entre ellos mismos y entre uno


num = 1
while num <= 100:
    contador = 0
    for i in range(1, 101):
        if num % i == 0:  # aqui se evalua si un numero es divisible entre otro
            contador += 1 # se eleva el contador en uno y se gurada en la variable
        
    if contador == 2: # comprueba si el numero solo due divisible con el mismo y con uno
        print(num, end=' ') # se imprime
        num +=1 # y se eleva el numero que se esta dividiendo 
    else:
        num += 1 # si el contador es mas de 2 significa que no es primo, se descarta y se eleva num para comprobar otro numero
    
