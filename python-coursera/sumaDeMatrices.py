
matriz = [
	[1, 2, 3, 4],
	[5 ,6 ,7 ,8],
	[9, 10, 11, 12]
	]                  # Aqui se genera la matriz con 3 filas y 4 columnas cada fila 

def suma_matrices(A, B): # aqui se le pasa 2 argumentos que contendran lo que se va a sumar en este caso la variable matriz 
    """
    suma dos matrices.
    Precondicion: A y B tienen que ser del mismo tamaño y deben de ser matrices de numeros
    """
    cant_filas = len(A)  # aqui se guarda una variable con el numero de filas que tiene la variable A
    cant_cols = len(A[0]) # aqui se guarda una variable con el numero de columnas o longitud que tiene la fila 0 

    C = []   # aqui se crea una lista vacia que contendra el resultado de sumar las matrices 

    for fila in range(cant_filas):    # aqui se crea un for que itere sobre el numero de la variable cant_filas 
        fila_suma = []                # aqui se crea una lista sola que contendra fila por fila con sus columnas sumadas 
        for col in range(cant_cols): # aqui se crea un for que iterara sobre el valor de la variable cant_cols
            fila_suma.append(A[fila][col] + B[fila][col]) # aqui se agrega el resultado de la suma a la variable fila_suma
        C.append(fila_suma)     # aqui se guarda al final de cada iteracion sobre las filas el resultado de sus columnan sumadas 
    return C   # aqui se retorna a la llamada de la funcion que contendra el resultado final que sera 3 filas con 4 columnas cada una pero sumadas cada columna por su mismo numero 

suma = suma_matrices(matriz, matriz)
print(suma)