from tkinter import *

ventana = Tk()
ventana.title('Inversor de pesos y dolares')

i = 0

#Entrada
e_texto = Entry(ventana, font = ('calibri 20'))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5, )

e_texto2 = Entry(ventana, font = ('calibri 20'))
e_texto2.grid(row = 1, column = 1, columnspan = 4, padx = 50, pady = 5)

def operacion():
    ecuacion= e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0


#Botones
boton1 = Button(ventana, text = "1", width = 5, height = 2)

ventana.mainloop()

