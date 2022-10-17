#La función "calcularEdad" calcula la edad de una persona
#Lo hace restando el año actual menos el año de nacimiento

def calcularEdad(añoActual, añoDeNacimiento):
    edad = añoActual - añoDeNacimiento
    return edad


miEdad = calcularEdad(2021, 1999)
edadDeMiAmigo = calcularEdad(2021, 1990)

print('Tengo ' + str(miEdad) + ' años y mi mejor amigo tiene ' + str(edadDeMiAmigo) + ' años')

#Agrega una línea en la función que devuelva la variable "edad"

#Luego, afuera de la función, llámala con el año actual y tu año de nacimiento
#Guarda el valor de llamar a esa función en la variable "miEdad"

#Vuelve a llamar la función con el año actual y el año de nacimiento de tu mejor amigo(a).
#Guarda el valor de llamar a esta función en la variable "edadDeMiAmigo"

#Imprime el siguiente texto:
#"Tengo X años y mi mejor amigo(a) tiene Y años."
#Donde X es tu edad guardada en la variable "miEdad"
#Donde Y es la edad de tu mejor amigo(a) en la variable "edadDeMiAmigo"