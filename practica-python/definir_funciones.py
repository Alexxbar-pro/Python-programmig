# -*- coding: utf-8 -*-

def peso(masa, gravedad=9.8):
    "Formula del peso"
    return masa * gravedad

# Parametros opcionales
print('Peso en la tierra:', peso(10)) 
# como aqui en la llamada de funcion solo le agregas un valor, lo agrega a masa y toma por defecto el valor que le diste a gravedad como parametro.
print('Peso en la luna:', peso(masa=10, gravedad=1.63))
# aqui como le das dos argumentos a la llamada de funcion agrega el valor corresponidente a cada uno en el orden establecido y lo que le diste a gravedad como parametro lo ignora y cambia su vaor por el que le diste en la llamada a la funcion

# En una funcion definida se puede usar variables globales dentro de la funcion pero no se pueden usar variables locales en el entrono global