from tkinter import *
from numpy import *
from random import randint

global c,aux,dado
dado=0
c=0
aux=0

fila=array([3,0,0,0,0,0,0,0])    #0-7 / filas = 8
columna=array([3,0,0,0,0,0,0,0,0,0,0,0,0])    #0-12 / columnas = 13
datamatriz=array(150)

window = Tk()

window.title("Serpientes y Escaleras")

window.geometry('700x500')

#lbl = Label(window, text=c)

#lbl.place(x=0, y=200, width=40, height=40)



       
def boton():
	global dado
	dado=randint(1,6)
	print(dado)

	buttondado = Button(window, text=dado, command=boton)
	buttondado.place(x=560, y=274, width=60, height=60)



for i in range(8):
    for j in range(13):
        op=i%2
        c=c+1
        button = 'btn'+str(c)
        button = Button(window, text=c)

        if(op==0):
        	h=42*(12-j)
        else:
        	h=42*j

        v=42*(8-i)

        if(c==92):
        	h=h+84
        	j=j+2

        button.place(x=h, y=v, width=40, height=40)
        button = Button(window, bg="green")
                
        print(c," - ",h, " - ",v)


buttondado = Button(window, text="v", command=boton)
buttondado.place(x=560, y=274, width=60, height=60)













window.mainloop()

