# 
#   Reto #0
#   EL FAMOSO "FIZZ BUZZ"
#   Fecha publicación enunciado: 27/12/21
#   Fecha publicación resolución: 03/01/22
#   Dificultad: FÁCIL
#   Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
#   - Múltiplos de 3 por la palabra "fizz".
#   - Múltiplos de 5 por la palabra "buzz".
#   - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


""" Este algoritmo es para saber como identificar los multiplos de n numero, esto siginifica que si un numero dividido entre otro numero da 0 es mutiplo de 3, 5 o de los dos en este caso.
"""

def fizzbuzz(n):
    
    for i in range(1, n+1):
        # if i % 2 == 0:
        #     print(f"{i} -> par")
        if i % 3 == 0 and i % 5 == 0: #Se tienen que cumpir las dos para que entre al bloque y se pone primero siempre 
            print(f"{i} -> FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} -> Fizz")
        elif i % 5 == 0:
            print(f"{i} -> Buzz")
        else:
            print(i)


fizzbuzz(100)