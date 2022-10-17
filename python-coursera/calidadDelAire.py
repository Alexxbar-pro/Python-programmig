#numero = int(input("Ingrese calidad del aire: "))
#if numero >= 0 and numero <= 99:
 # print("Bueno")
#elif numero >= 100 and numero <= 199:
 # print("Regular")
#elif numero >= 200 and numero <= 299:
 # print("Alerta")
#elif numero >= 300 and numero <= 499:
 # print("Preemergencia")
#else:
 # print("Emergencia")

numero = int(input("Ingrese calidad del aire"))
if numero>=0 and numero<=99:
  print("Bueno")
if numero>=100 and numero<=199:
  print("Regular")
if numero>=200 and numero<=299:
  print("Alerta")
if numero>=300 and numero<=499:
  print("Preemergencia")
else:
  print("Emergencia")
