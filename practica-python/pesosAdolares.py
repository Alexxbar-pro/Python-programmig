# Pesos a Dolares 

pedido = input('Quieres cambiar pesos o dolares? ').capitalize()

def pesosAdolares():
    pesos = int(input('ingresa los pesos a convertir: '))
    precio = 20.20

    resultado = pesos / precio
    print('$' + str(pesos) + ' pesos en dolares son %.2f' % resultado)

def dolaresApesos():
    dolares = int(input('ingresa los dolares a convertir: '))
    pesos = 20.20
    resultado = dolares * pesos
    print('$' + str(dolares) + ' dolares en pesos son %.2f' % resultado)



if  pedido == 'Pesos':
    pesosAdolares()
elif pedido == 'Dolares':
    dolaresApesos()
else:
    print('Escoge solo pesos o dolares porfavor')
