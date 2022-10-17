# words = ['hello', 'world', 'spam', 'eggs']
# for word in words:
#     print(word + '!')

# Este codigo muestra cada elemento de la lista y agrega un sigo de exclamacion
# ==================================================================================================

# str = 'testing for loops'
# count = 0
# for x in str:
#     if(x == 't'):
#        count += 1
# print(count)

# Este codigo muestra cuntas letras 't' hay en la variable x
# ===================================================================================================

# list = [2, 3, 4, 5, 6, 7]
# for x in list:
#     if(x%2 == 1 and x > 4):
#         print(x)
#         break
# Este codigo lo que hace es regresar un numero de la lista que dividido por 2 sobre 1 y que sea mayor que 4, que en este caso es el 5 y el 7 pero solo regresara 5 por la sentencia break

# ============================================================================================================

# for i in range(5):
#     print('i se establece en ' + str(i))

# Este codigo lo que hace es regresar el numero asignado a cada iteracion que da el bucle para hacer una lista de numero desde el 0 hasta el 4 

# ===========================================================================================================

# for cosa in ['gustan los gatos', 'gusta la pasta', 'gusta la programacion', 'gusta el spam']:
#     if cosa == 'gusta el spam':
#         print('Realmente no me gusta ' + cosa)
#         break
#     print('Realmente me ' + cosa) 
    
    # Este codigo lo que hace es completar la oracion con la lista de cadenas que se le proporciono, cambiando cada que hace una iteracion.

#===========================================================================================================

# def potencia(base, exponente):         #Este codigo saca la potencia del numero que se le des como base y
#     resultado = 1                      # y lo eleva al valor que le des como exponente 
#     for i in range(exponente):
#         resultado = resultado * base  #la iteracion de los bucles For siempre empieza en 0 al menos que 
#                                       #le indiques un argumento de inicio e itera hasta el numero que le  
#     return resultado                  # des como argumento pero sin incluirlo 

# print(potencia(3, 3))         # me equivoque range() es el que itera desde 0 hasta el numero que le des pero sin incluirlo, for itera dependiendo de los parametros que tenga para iterar 

# =========================================================================================================

# for i in range(11):     # Este codigo imprime solo numeros pares o multiplos de 2 
#     if i % 2 == 0:
#         print(i)       