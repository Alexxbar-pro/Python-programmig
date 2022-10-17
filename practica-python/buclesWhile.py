# while True:
#     try:
#         x = int(input("Por favor ingrese un número: "))
#         break
#     except ValueError:
#           print("Oops! No era válido. Intente nuevamente...")

         # Este codigo es una excepcion simple

# ====================================================================================================

# i = 1
# while i <= 10:         # Este codigo es para hacer una lista que llegue hasta el numero indicado
#     print(i)
#     i = i + 1
    
# print('Terminado!')

# =================================================================================================

# x = 1
# while x <= 10:                         # Este codigo es para separar los numeros pares e impares
#     if x % 2 == 0:
#         print(str(x) + ' is even')
#     else:
#         print(str(x) + ' is odd')
#     x += 1

# ===================================================================================================

# i = 0
# while True:
#     print(i)
#     i = i + 1       # Este codigo es para crear un bucle infinito de numeros 
#     if 99 >= 100:
#      break
    
# ==================================================================================================

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#     if i == 3:                #Este codigo es para entender mejor la declaracion 'continue'
#         print('skipping 3')
#         continue
        
# ====================================================================================================================

valorIterable = ['gustan los gatos', 'gusta la pasta', 'gusta la programacion', 'gusta el spam']
indice = 0
while (indice < len(valorIterable)):
    cosa = valorIterable[indice]
    if indice == 3:
        print('Realmente no me gusta ' + cosa)
        break
    print('Realmente me ' + cosa)
    indice += 1
 
# Este es un bucle while que se comporta igual que el anterior bucle for mediante la adición de código extra

# =============================================================================================================================