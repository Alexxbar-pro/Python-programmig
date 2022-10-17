# modulo de numeros Fibonacci

def fib(n):   # escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):  # devuelve la serie Fibonacci hasta n
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado
        


fib(2000)
rel = fib2(2000)
#print(rel)