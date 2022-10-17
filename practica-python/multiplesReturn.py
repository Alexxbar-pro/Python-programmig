#La función "informacionPersonal" recoge la información personal de una persona

def informacionPersonal(nombre, edad, pais):
    name = input('Cual es tu nombre? ')
    age = input('Cual es tu edad? ')
    country = input('De que pais vienes? ')
    return name, age, country

nombre, edad, pais = informacionPersonal(str, str, str)


print(nombre + ", de " + pais + ", tiene " + str(edad) + " años de edad.")

#Agrega una línea en la función que devuelva las variables "name", "age" y "country".

#Luego, afuera de la función, en la línea 8, llámala
#Guarda el valor de llamar a esa función en las variables "nombre", "edad" y "pais".

#Corre el programa. Debería imprimir el siguiente texto:
#Juana de Arco, de Francia, tiene 10 años de edad.