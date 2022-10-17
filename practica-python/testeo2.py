# TABLERO_REAL = [
#     ['|', '_', '|', '_', '|', '_', '|'],
#     ['|', '_', '|', '_', '|', '_', '|'],
#     ['|', '_', '|', '_', '|', '_', '|']
# ]

# for fila in TABLERO_REAL:
#     print(fila)
#     for i in range(len(fila)):
#         if i == len(fila) -1:
#             print(i)
        
# numeros = [1, 2, 3, 4, 5]

# formato = ', '.join([str(n) for n in numeros])


# print('Este es el contenido de la variable numeros: ', formato)

# def test(*arg):
#     print('Estos son los nombres:', ', '.join(arg))


# test('erick', 'juan', 'pepe')
import random
count = 0
matriz = [
    ['|','-', '|','-', '|', '-', '|'],
    ['|','-', '|','-', '|', '-', '|'],
    ['|','-', '|','-', '|', '-', '|']
]

def tablero():
    for fila in matriz:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end=('\n'))
            else:
                print(fila[i], end=(' '))
                print(end=(' '))
            

def winner():
    if matriz[0][1] == matriz[0][3] == matriz[0][5] == caracter or matriz[1][1] == matriz[1][3] == matriz[1][5] == caracter or matriz[2][1] == matriz[2][3] == matriz[2][5] == caracter:
        return 1
    else:
        return 0

while count < 9:
    caracter = input('Que quieres agregar X u O?: ').upper()
    def test(count):
        while True:
    
            if caracter == 'X':
                fila = random.randint(0, 2)
                columna = random.choice([1, 3, 5])
                if matriz[fila][columna] != '-':
                    continue
                else:
                    matriz[fila][columna] = 'X'
                    count = count + 1
                    tablero()
                    if winner():
                        print('gano el jugador X')
                        exit(0)
                    return count
            
                
            else:
                fila = random.randint(0, 2)
                columna = random.choice([1, 3, 5])
                if matriz[fila][columna] != '-':
                    continue
                else:
                    matriz[fila][columna] = 'O'
                    count = count + 1
                    tablero()
                    if winner():
                        print('Gano el jugador O')
                        exit(0)
                    return count
    count = test(count)
print('Se empato el juego')

        