# while True:
#     try:
#         x = int(input('Por favor ingrese un numero: '))
#         break
#     except ValueError:
#         print('Oops! No era valido. Intente nuevamente...')
#     except (RuntimeError, TypeError, NameError):
#         pass

# Una declaracion try puede tener mas de un except.
# Un except puede tener mas de una excepcion usando parentesis.

# =================================================================================================================================
# import sys

# try:
#     f = open('miarchivo.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print('Error OS: {0}'.format(err))
# except ValueError:
#     print('No puede convertir el dato en un entero.')
# except:
#     print('Error inesperado', sys.exc_info() [0])
#     raise

# El último except puede omitir nombrar qué excepción captura, para servir como comodín. Usá esto con extremo cuidado,
# ya que de esta manera es fácil ocultar un error real de programación

# ===============================================================================================================================
# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('no puede abrir', arg)
#     else:
#         print(arg, 'tiene', len(f.readlines()), 'lineas')
#         f.close()

# Las declaraciones try ... except tienen un bloque else opcional, el cual, cuando está presente, debe seguir a los except.
# Es útil para aquel código que debe ejecutarse si el bloque try no genera una excepción

# ==============================================================================================================================
# def esto_falla():
#     x = 1/0

# try:
#     esto_falla()
# except ZeroDivisionError as err:
#     print('Manejando error en tiempo de ejecucion:', err)

# Los manejadores de excepciones no manejan solamente las excepciones que ocurren en el bloque try, también manejan las
# excepciones que ocurren dentro de las funciones que se llaman (inclusive indirectamente) dentro del bloque try

# ===============================================================================================================================
#try:
    #raise NameError('Hola')
#except NameError:
    #print('volo una excepcion!')
    #raise
# Si necesitás determinar cuando una excepción fue lanzada pero no querés manejarla, una forma simplificada de la
# instrucción raise te permite relanzarla

import math

class NegativeNumber(Exception):
    'Excepcion de tipo numero negativo'
    pass

def raiz_cuadrada(number):
    if number < 0:
        raise NegativeNumber('Numero negativo')
    return math.sqrt(number)

raiz_cuadrada(-1)

# En este codigo lo que hace es crear su propia excepcion apartir de una funcion 'class'