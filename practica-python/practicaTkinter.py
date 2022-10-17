import tkinter

ventana = tkinter.Tk()
ventana.geometry('400x300')

ventana.title('PRACTICA TKINTER')

# etiqueta = tkinter.Label(ventana, text = 'Hola Mundo', bg = 'red')
# etiqueta.pack(fill= tkinter.BOTH, expand = True)

boton1 = tkinter.Button(ventana, text='presiona', padx=40, pady=50)
boton1.pack()

ventana.mainloop()