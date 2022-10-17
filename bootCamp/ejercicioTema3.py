""" Primera parte:

Crear una función con tres parámetros que sean números que se suman entre sí.

Llamar a la función en el main y darle valores.

"""

def sumarValores(a, b, c):
    return a+b+c

#print(sumarValores(5, 5, 5))


"""
Segunda parte:

Crear una clase coche.

Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.

Una función que incremente el número de puertas que tiene el coche.

Crear un objeto miCoche en el main y añadirle una puerta.

Mostrar el número de puertas que tiene el objeto.
"""

class coche:
    nPuertas = 4

    def __init__(self):                   #lo dejo asi porque no se cual es la mejor opcion, asi que use la opcion mas sencilla
        print(f"EL coche tiene {self.nPuertas} puertas")
        
    def incrementar(self, puerta):
        puerta = puerta
        puertasTotales = self.nPuertas + puerta
        print(f"El Número de puertas que tiene el coche es: {puertasTotales}")


miCoche = coche().incrementar(1)
#miCoche.incrementar(2)
