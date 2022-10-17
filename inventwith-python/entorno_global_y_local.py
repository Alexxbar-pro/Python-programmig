# Entorno global y entorno local

def bacon():
    # Creamos una variable local llamada 'spam'
    # en lugar de cambiar el valor de la
    # variable global 'spam'
    spam = 99
    # El nombre 'spam' se refire ahora solo a la
    # variable local por el resto de esta funcion:
    print(spam)
    

spam = 42 # Una variable global llamda 'spam':
print(spam) # 42
bacon() # Llama a la funcion bacon():
# La variable global no fue cambiada en bacon():
print(spam) #42
