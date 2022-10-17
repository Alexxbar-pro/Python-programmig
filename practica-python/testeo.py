# import random
# import datetime

# palabras = ['hola', 'soy juan', 'y te vengo', 'a decir', 'que estas', 'Horrible']

# indice = random.randint(0, len(palabras) -1)
# desicion = int(input('Elige un numero del 1 al 6: '))

# print(palabras[indice])

# today = datetime.date.today()
# now = datetime.datetime.now()
# print(now)

# def dolaresApesos():
#     pesos = 20.12
#     dolares = int(input('ingresa los dolares a convertir: '))

#     c = dolares * pesos
#     print('$' + dolares + ' dolares en pesos son %.2f' % c)

import random
list = [' ', ' ', ' ', ' ']
count = 0

while count < 4:
    caracter = input('Que quieres agregar X u O?: ').upper()

    while True:
    
        if caracter == 'X':
            indice = random.randint(0, 3)
            if list[indice] != ' ':
                continue
            else:
                list[indice] = 'X'
                count = count + 1
                print(list)
                break
            
                
        else:
            indice = random.randint(0, 3)
            if list[indice] != ' ':
                continue
            else:
                list[indice] = 'O'
                count = count + 1
                print(list)
                break
        
            
