# Este es un algoritmo de ordenamiento acendente y es conocido como metodo burbuja 

def bubbleSort(array):
    # aqui se guarda el total de elemento de la variable array menos un elemento, porque ese ultimo elemento no tiene con quien compararce
    lenght = len(array)-1 
    # Bucle para las pasadas 
    for i in range(0, lenght):
        print(f'pasada #{i + 1}') # aqui se ve en que pasada va 
        # Bucle para las comparaciones e intercambios
        for j in range(0, lenght):
            print(f'comparacion: {array[j]} > {array[j+1]}')
            if array[j] > array[j + 1]: #Aqui se checa si el primer valor es mayor que el segundo 
                print(f'intercambiar: {array[j]} x {array[j+1]}')
                aux = array[j] # Aqui se guarda el primer numero para que no se pierda 
                array[j] = array[j + 1] # Aqui si el segundo numero es mayor pasa al indice del primer numero y se recorre
                array[j + 1] = aux # aqui se desempaqueta el valor guardado en la posicion del segundo 
        print(f'lista: {array}')
    return array


scores = [70, 90, 0, 80, 60, 85]
print(scores)
print(bubbleSort(scores))