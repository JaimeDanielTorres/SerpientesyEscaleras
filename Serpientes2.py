from tkinter import *
from numpy import *
from random import randint

global c,aux,dado,turn
dado=0
c=0
aux=0
turn=1

fila=array([3,0,0,0,0,0,0,0])    #0-7 / filas = 8
columna=array([3,0,0,0,0,0,0,0,0,0,0,0,0])    #0-12 / columnas = 13
datamatriz=[None]*100

window = Tk()

window.title("Serpientes y Escaleras")

window.geometry('700x500')



       
def boton():
	global dado, turn
	dado=randint(1,6)
	print(dado)

	buttondado = Button(window, text=dado, command=boton)
	buttondado.place(x=560, y=275, width=60, height=60)

	if(turn==1):
		turn = 2
		lbl = Label(window, text='Turno: '+str(turn),bg="blue")
	else:
		turn = 1
		lbl = Label(window, text='Turno: '+str(turn),bg="red")

	
	lbl.place(x=560, y=200, width=100, height=40)



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

        v=42*(7-i)

        if(c>=92):
        	if(c<=100):
        		button.place(x=h+84, y=v, width=40, height=40)
        		button = Button(window, bg="green")
        	else:
        		break

        else:
        	button.place(x=h, y=v, width=40, height=40)
        	button = Button(window, bg="green")
                
        print(c," - ",h, " - ",v)


buttondado = Button(window, text="v", command=boton)
buttondado.place(x=560, y=275, width=60, height=60)

lbl = Label(window, text='Turno: '+str(turn),bg="red")
lbl.place(x=560, y=200, width=100, height=40)













window.mainloop()
