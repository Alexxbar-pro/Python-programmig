#utf-8
import time
def intro():
    print('Este codigo esta echo para calcular tu IMC(indice de masa corporal)')
    time.sleep(1)

    respuesta = input('Te gustaria saber tu IMC? ').capitalize()
    while True:
        if respuesta == 'Si':
            time.sleep(1)
            print('Hagamoslo!')
            break
    return respuesta 

    
def calcularElImc(Desicion):
    if Desicion == 'Si':
        time.sleep(1)
        print('Para calclular el imc se tiene que dividir el peso en kilogramos por la estatura en metros cudrados')
        kilogramos = int(input('ingresa tu peso: '))
        estatura = float(input('ingresa tu estatura: '))

        imc = kilogramos / estatura**2
        print('tu imc es: %.2f' % imc)




Desicion = intro()
calcularElImc(Desicion)