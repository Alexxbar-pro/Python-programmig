n = int(input('Enter a number: '))

for i in range(0, n):  # aqui lo que hace es iterar el bucle desde 0 hasta n que es el numero ingresado
                        # por el usuario
    if i % 2 == 0:    # aqui como ya sabes entra en la condiion si el residuo de i dividido entre 2 es 0
        print(str(i) + ' es par')
    else:
        print(f'{i} es impar')