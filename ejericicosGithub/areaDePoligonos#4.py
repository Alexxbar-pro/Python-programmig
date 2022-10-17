# /*
#  * Reto #4
#  * ÁREA DE UN POLÍGONO
#  * Fecha publicación enunciado: 24/01/22
#  * Fecha publicación resolución: 31/01/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  *

#Poligono -> Son las líneas que forman la figura. Un polígono debe tener como mínimo tres lados y no existe un máximo de cantidad de lados. Un polígono puede ser, por ejemplo, un triángulo (polígono de tres lados), un pentágono (polígono de cinco lados), un octágono (polígono de ocho lados), entre muchos otros. 
# Todos los lados de un poligono regular miden lo mismo.


"Formula->  A = p*a/2"  # A = 30 * 4.1 / 2 = 61.5 cm2, cm * cm = cm2
# p = Perimetro (Es la suma de todos los lados)  
# a = apotema (Es la medida que tiene desde el centro hasta la mitad de uno de los lados)


def areaPoligono(poligono):
    poligono = poligono.lower()
    if poligono == 'triangulo':
        longitudLado = int(input('ingresa el valor de uno de los lados del triángulo:'))
        apotema = int(input('Ingresa apotema de triángulo: '))
        perimetro = longitudLado*3
        area = perimetro*apotema/2
        print(f"El area del triangulo es {area} cm2")
    
    elif poligono == 'cuadrado':
        longitudLado = int(input('ingresa el valor de uno de los lados del cuadrado:'))
        apotema = int(input('Ingresa apotema de cuadrado: '))
        perimetro = longitudLado*4
        area = perimetro*apotema/2
        print(f"El area del cuadrado es {area} cm2")
    
    elif poligono == 'rectangulo':
        altura = int(input('Ingrese longitud de la altura: '))
        base = int(input('Ingrese longitud de la base'))
        apotema = int(input('Ingrese longitud de apotema: '))
        perimetro = (altura*2) + (base*2) # Se suman las dos alturas y las dos bases 
        area = perimetro*apotema/2
        print(f"El area del triangulo es {area} cm2")

    elif poligono == 'octagono':
        longitudLado = int(input('ingresa el valor de uno de los lados del octagono:'))
        apotema = int(input('Ingresa apotema de octagono: '))
        perimetro = longitudLado *4
        area = perimetro*apotema/2
        print(f'El area del octagono es {area} cm2')

    elif poligono == "pentagono":
        longitudLado = int(input('ingresa el valor de uno de los lados del pentagono:'))
        apotema = float(input('Ingresa apotema del pentagono: '))
        perimetro = longitudLado *5
        area = perimetro*apotema/2
        print(f'El area del octagono es {area} cm2')


areaPoligono('pentagono')


