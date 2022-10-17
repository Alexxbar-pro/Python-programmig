
# El metodo find() busca en la cadena el caracter o carcters y donde lo encuentre por primera vez ese indice regresa y si no regresa -1
# acomparacion del metodo rfind() que hace lo mismo solo que no regresa el primero si no el ultimo indice donde encontro el caracter o caracters
# por ejemplo si le pasas una cadena y buscas la letra 'a' y en la cadena hay varias letras 'a' find() regresa el indice donde lo encuentra por primera vez y rfind() regresa el indice donde lo encuentra por ultima vez

#a = 'ericka a lejandro delgado'
#b = 'a'
#print(a.find(b)) regresa el indice 5
#print(a.rfind(b)) regresa el indice 22 por que ahi se encuentra la ultima letra a


def tiene_exactamente_un_punto(numero):
	numero = str(numero) #convierte la variable a str porque .find() es metodo de str
	primer_indice = numero.find(".") # si fuera otro valor es error
	if primer_indice is -1: # is es igual '==' regresa True si es el mismo valor False si no
		return False
	return primer_indice is numero.rfind(".") # aqui se comprueba si el valor tiene solo un punto decimal

pruebas = ["1.2", "1", "1.1.2", "500", "5.0"]
for dato in pruebas:
	print("¿'{}' tiene exactamente un punto? {}".format(dato, tiene_exactamente_un_punto(dato)))