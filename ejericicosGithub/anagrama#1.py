#  ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.


def anagram(a, b):

    if len(a) != len(b):
        return False
    elif a == b:
        return False
    else:
        array = list(a)
        count = 0
        for i in range(len(a)):
            aux = a[i]
            
            for j in range(len(b)):
                if aux == b[j]:
                    count += 1
                    #print('si', a[i], b[j])
        return count            
        #print(array)


wordOne = 'riesgo'
wordTwo = 'sergio'

conteo = anagram(wordOne, wordTwo)
if conteo == len(wordOne) and conteo == len(wordTwo):
    #print('Si es anagrama')
#else:
    
    #print('No es anagrama')



    """Aqui una forma mas facil de hacerlo"""

def esAnagram(word1, word2):
    print(sorted(word1))
    print(sorted(word2))
    return sorted(word1) == sorted(word2)
# la funcion sorted ordena la cadena en orden acendente o alfabeticamente de A a Z, tambien se puede en orden decendente pero ocupas checar como

print(esAnagram('sergio', 'riesgo'))