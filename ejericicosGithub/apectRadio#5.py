import matplotlib.pyplot as plt
import cv2

# * Reto #5
#  * ASPECT RATIO DE UNA IMAGEN
#  * Fecha publicación enunciado: 01/02/22
#  * Fecha publicación resolución: 07/02/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
#  * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
#  * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.


#La relación de aspecto o ratio de una imagen es la proporción entre el ancho y la altura de la imagen. Se calcula dividiendo la anchura entre la altura, y se expresa normalmente con dos números separados por dos puntos. Por ejemplo 3:2, significa que por cada tres unidades a lo largo hay dos unidades a lo alto


image = cv2.imread('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')

print(image)