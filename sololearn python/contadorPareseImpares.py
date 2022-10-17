user_input = int(input('Enter your number: '))

even_num = 0              # Numeros pares
odd_num = 0               # Numeros impares

while user_input > 0: # Este es el bucle y condicion que se tiene que romper 
    if user_input % 2 == 0:
        even_num += 1         #  En esta variable se van contando los numeros pares que hay en el user_input
    else:
        odd_num += 1         # En esta variable se van contando los numeros impares que hay en el user_input

    user_input = user_input  // 10 # Esto lo que hace es que al dividir por 10 le quita una unidad al  
#                                  # digito que se le dio y asi salir del bucle e imprimir lo que se pide

print(f'Number of even numbers: {even_num} | Number of odd numbers: {odd_num}')
