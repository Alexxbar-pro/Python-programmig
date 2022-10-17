
# def first_1000():
#     'Genera los primeros 1000 numeros.'
#     # como es un range() regresa hasta el 1000 pero sin incluirlo osea que solo regresa hasta el 99
#     for x in range(1000):
#         yield x                    


# gen = first_1000()

# for x in gen:
#     print(x)


# ==========================================================================================================================

def gen_primos(cantidad=1):
    'Generador de números primos'

    contador = 1
    lista_primos = []

    # comienza un ciclo infinito
    while cantidad > contador:
        es_primo = True
        contador += 1 
        if len(lista_primos) > 0:
            for primo in lista_primos:
                if contador % primo == 0:
                    es_primo = False
                    break
        if es_primo:
            lista_primos.append(contador)
            yield contador

first_100_primos = gen_primos(100)

for x in first_100_primos:
    print(x)