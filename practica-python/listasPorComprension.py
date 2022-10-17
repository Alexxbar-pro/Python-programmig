
numero = [n for n in range(1,6)]      # Este codigo agrega los valores del 1 al 5 en la lista 
#print(numero)

# ====================================================================================================
pares = [n for n in range(21) if n % 2 == 0]   # Este lista por comprension ingresa solo numeros pares
#print(pares)                           # dentro de la lista, nota que tambien se pueden usar condiciones

pares2 = [valor * 2 for valor in range(0, 50) if valor * 2 % 5] # esta es otra manera de regresar una lista por comprension con pares 

# =====================================================================================================
asteriscos = ['*' * a for a in range(1, 6)]  # Esta lista por comprension ingresa una secuencia de 
#print(asteriscos)    # asteriscos dentro de la lista, toma en cuenta que podria ser cualquier signo

# =======================================================================================================
palabras = ['casa', 'mesa', 'silla', 'puerta', 'ventana']

palabras = [i[0] for i in palabras]   # Esta lista por comprension agrega a la lista solo las iniciales 
#print(palabras)      # de las cadenas que estan en la lista palabras, como ves se puede utilizar la misma variable para agregar los valores, cosa que en el codigo normal no se puede

inicia = []          # Este sera el codigo que tuvieras que realizar si no usas las listas por compension 
for e in palabras:     # como ves usar comprension de listas es mucho mas eficiente para utilizar 
    inicia.append(e[0])
#print(inicia)

# =====================================================================================================
utensilios = 'mesa interruptor silla microscopio cubo'.split()

lista = [u for u in utensilios if len(u) > 7]  # Esta lista por comprension agrega solo las palabras que 
#print(lista)     # tengan mas de 7 letras en la lista 

# ===================================================================================================
multiplos = [num for num in range(30) if num % 7 == 0 or num % 11 == 0 if num]
#print(multiplos)   # Esta lista por comprension lo que hace es agregar solo los numeros que sean multiplos  de 7 u 11 en la lista

# ======================================================================================================
cuadrados = [pow(no, 2) for no in range(1, 11) if no % 2 == 0 or no % 2 == 1] 
#print(cuadrados)  # Esta lista por comprension lo que hace es agregar solo los numeros pares e impares pero elevados al cuadrado, la funcion pow() eleva a la potencia los argumentos dados 

# =====================================================================================================
stuff = ['martillos', 'nombres', 'patineta']
letras = [ini[:4] for ini in stuff ]      # Esta lista por comprension lo que hace es agregar solo las 
#print(letras)     # primeras 4 letras de cada valor a la lista 
# =================================================================================================
lenguajes = ['python', 'java', 'c++', 'php', 'swift', 'sql']
# Esta lista por comprension lo que hace es agregar los valores capitalizados a la lista 
capitalizar = [lenguaje.capitalize() for lenguaje in lenguajes]
#print(capitalizar)    # La funcion capitalize() lo que hace es hacer mayuscula la primera letra de cada valor 

for lenguaje in lenguajes[::]:         # Este codigo daria el mismo resultado que la lista por comprension
    lenguajes.append(lenguaje.capitalize())  # pero aqui lo que se hace es guradar el resultado en la 
    del lenguajes[0]            # misma variable que contiene los valores iniciales 
#print(lenguajes)

# =====================================================================================================
