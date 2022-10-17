"""
Palindromos -> palabras que se leen igual asi se leean de adelante para atras o de atras para adelante
ejemplos: ojo, oso, seres, arenera, sometemos.


-Hacer un programa que detecte si la palabra es palindromo o no, inluso aunque no este en orden la palabra
-La constante de un palindormo es que todos sus letras estan en pares excepto una 
"""


palabra = "seres"
#print(''.join(reversed(palabra))) # con el metodo join y la funcion reversed se puede invertir la cadena
#print(sorted(palabra)) #convierte la cadena en lista y devuelve los caracters en orden acendente
#print(palabra[::-1]) #Esta es una manera mas sencilla de invertir una cadena, el doble dos puntos regresa una copia de la cadena y el -1 hace que sea desde el ultimo indice hasta el primero

palabra2 = "rerenaa"

def wordIsPalindrom(palabra):
    number_palindroms = [] #aqui se guardan cuantas letras iguales hay en lista
    for i in palabra: #este for hace que se pueda comparar una letra de la palabra con cada una de las letras de la misma palabra
        count = 0 #Cuenta cuantas veces esta la letra que se esta comparando en la cadena y se restablece en cada iteracion
        for j in palabra:  # este itera en todas las letras de la palabra por cada iteracion del for pasado para comparar
            if i == j: # se compara si la letra es igual
                count += 1  # se suma uno si es igual la letra 
        if count >= 3: # si el contador llega a 3 o mas es porque no es un palindromo y retorna False
            return False
        else:
            number_palindroms.append(count) # si la condicion se cumple se agrega el contador de las letras en la lista 
    if number_palindroms.count(1) == 1: # si solo hay una letra sin par es porque es un palindromo
        return True
    else:
        return False
    


# if wordIsPalindrom(palabra) is True:
#     print(f"{palabra} es un palindromo")
# else:
#     print(f"{palabra} no es un palindromo")

#==============================================================================================================================

def check_palindrome(str_input: str):
    chars = {}  # se establece un diccionario vacio
    for char_input in str_input: # se itera en cada letra de la palabra
        if char_input in chars.keys(): # se comprueba si la letra de la palabra esta en el diccionario
            chars[char_input] +=1 # si esta se le suma uno al valor(value) que tiene la letra de la palabra(key)
        else:
            chars[char_input] = 1 # si la letra no esta en el dic con esta manera se le agrega la letra(key) con el valor 1
            
    counter = 0 # se establece un contador para comprobar si solo hay un a letra sola
    for char_value in chars.values(): # aqui se itera en vada valor del diccionario
        if char_value % 2 != 0: # se comprueba cuantos calores son impares o no son pares
            counter += 1 
        if counter > 1: # si hay mas de un valor que no sea par significa que la palabra no es palindromo y retorna False
            return False
        
    return True
        
# print(check_palindrome("civic"))
# print(check_palindrome("ivicc"))
# print(check_palindrome("civil"))
# print(check_palindrome("livci"))
# print(check_palindrome("frafa"))
# print(check_palindrome("dw"))

#=============================================================================================================================

def palindrome(str_in):
    """
    Checks if any permutation of an input string is a palindrome 
    
    :param str_in: string for checking the palindrome
    :type str_in: str
    
    :return: True id str_in can be a palindrome else False
    :rtype: bool
    """
    #.get(key, value) -> El metodo get devuelve el valor de la clave que le pasas como primer argumento, si esta no esta en el dic regresa None pero si le agregas como segundo argumento un valor y pasa la misma situacion que no se encuentre la clave, lo que hara sera regresar ese valor que le pasaste como parametro
    
    num_chars = {}
    for char in str_in:
        num_chars[char] = 0 if num_chars.get(char, 0) == 1 else 1  #Aqui se va agregar una clave-valor si no esta en el dic y si esta se va a modificar, se agregra 0 si el valor que retorne el dic con el metodo get es igual a uno y si no es igual se agregara 1, ya sea la clave este o no.
        
    return False if sum(num_chars.values()) > 1 else True  # regresa False si la suma de todos los valores que estan en el dec es mayor a 1 y si no regresa True 

print(palindrome('civicc'))
print(palindrome('ivicc'))
print(palindrome('civil'))
print(palindrome('livci'))
print(palindrome('frabfral'))
print(palindrome('dw')) 