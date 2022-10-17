import random


respuesta1 = input("presiona para tirar los dados");

while True:   
    Dado1 = random.randint(1, 6);
    Dado2 = random.randint(1, 6);
    Suma = Dado1+Dado2;

    print("El Dado 1 callo en",Dado1,"y el Dado 2 en",Dado2);
    print("y ambos dados suman", Suma);
    respuesta2 = input("Vuelve a presionar para tirar otra vez");
