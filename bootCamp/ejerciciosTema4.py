"""En este ejercicio practicarás las estructuras de control, para ello deberás crear:

Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
Pista: Los números inferiores a 0 son negativos y los superiores, positivos."""

numeroIf = 0

if numeroIf > 0:
    print("Es positvo")
elif numeroIf < 0:
    print("Es negativo")
else:
    print("Es cero")


"""Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:

Incrementar el valor de la variable en uno cada vez que se ejecute.

Mostrarlo por pantalla cada vez que se ejecute. """

numeroWhile = 0

while numeroWhile < 3:
    print(numeroWhile)
    numeroWhile += 1

"""Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez."""

numeroWhile = 0
print(numeroWhile)

while numeroWhile < 3:
    numeroWhile += 1


"""
Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla."""

numeroFor = 0         #Este codigo es la manera de hacerlo en python ya que asi funiona el for 
for i in range(4):
    print(i)
    


'''>>> for (int numeroFor = 0; contador <= 3; contador = contador + 1) 
System.out.println(contador);'''    
#Y esta seria la manera de hacerlo como las instrucciones que creo estan en como funciona for en java


"""
Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación."""


def primavera():          #Esta es una de las maneras que mas me gusto para representar el switch case en python ya que no existe
    print('primavera')    # como tal, y no queria simplemente anidar puras condicionales if, elif o else porque seria lo mismo.
def verano():
    print('verano')
def otoño():
    print('otoño')
def invierno():
    print('invierno')
def default():
    print('Eso no es una estación del año')

switch_estaciones = {
    1: primavera,
    2: verano,
    3: otoño,
    4:invierno
}

Estacion = 1

switch_estaciones.get(Estacion, default)()


# De todas maneras les dejo aqui el pseudocodigo de java conmo se supone que seria el switch case 
'''
var estacion = "OTOÑO";

switch(estacion) {
    case "PRIMAVERA":
        System.out.println("Es primavera")
        break;                          
    case "VERANO":
        System.out.println("Es verano")
    case "OTOÑO"
        System.out.println("Es otoño")
    case "INVIERNO"
        System.out.println("Es invierno")
    default:
        System.out.println("Eso no es una estacion del año")

}
'''