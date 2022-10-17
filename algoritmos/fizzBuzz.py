n = int(input())

for x in range(1, n):             #En este codigo lo que se pide es que regrese los multiplos de 3 como Fizz
    if x % 3 == 0 and x % 5 == 0: #lo multiplos de 5 como Buzz, los multiplos de 3 y 5 (de 15) como FizzBuzz
        print('FizzBuzz')         # y que se salte los numeros pares o multiplos de 2 
    elif x % 2 == 0:
        continue
    elif x % 3 == 0:
        print('Fizz')            # Si un numero dividido por otro numero es 0 es porque ese numero es
    elif x % 5 == 0:             # multiplo del numero 
        print('Buzz')
    else:
        print(x)
