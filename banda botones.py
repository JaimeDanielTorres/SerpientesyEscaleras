from tkinter import *
ch=int(0)
med=int(0)
gr =int(0)
Q=int(0)

ventana=Tk()
ventana.title("Banda con botones")

def chica():
    global ch
    ch=ch+1
    Label(ventana,text=ch).grid(column=1,row=2)
    return ch

def mediana():
    global med
    med=med+1
    Label(ventana,text=med).grid(column=3,row=2)
    return med
    
def grande():
    global gr
    gr=gr+1
    Label(ventana,text=gr).grid(column=5,row=2)
    return gr

def cerrar():
   ventana.destroy()
   ventana1=Tk()
   Label(ventana1,text="Se acabo el pedido con:\n",font=("SYSTEM 10")).grid(column=0,row=0)
   Label(ventana1,text=ch,font=("SYSTEM 10")).grid(column=0,row=1)
   Label(ventana1,text=" Chicas.",font=("SYSTEM 10")).grid(column=1,row=1)
   Label(ventana1,text=med,font=("SYSTEM 10")).grid(column=0,row=2)
   Label(ventana1,text=" Medianas.",font=("SYSTEM 10")).grid(column=1,row=2)
   Label(ventana1,text=gr,font=("SYSTEM 10")).grid(column=0,row=3)
   Label(ventana1,text=" Grandes.",font=("SYSTEM 10")).grid(column=1,row=3)

Label(ventana,text="Selecciona el botón para ingresar cajas correspondientes:\n",font=("SYSTEM 10")).grid(column=0,row=0)
Label(ventana,text="Se tienen",font=("SYSTEM 10")).grid(column=0,row=2)
Label(ventana,text=" Cajas chicas, ",font=("SYSTEM 10")).grid(column=2,row=2)
Label(ventana,text="Cajas medianas y",font=("SYSTEM 10")).grid(column=4,row=2)
Label(ventana,text=" Cajas grandes",font=("SYSTEM 10")).grid(column=6,row=2)
d=Button(ventana,text="CHICA",command=chica,bg="red")
d.grid(column=1,row=1)
d1=Button(ventana,text="MEDIANA",command=mediana,bg="red")
d1.grid(column=2,row=1)
d2=Button(ventana,text="GRANDE",command=grande,bg="red")
d2.grid(column=3,row=1)
d3=Button(ventana,text="Terminar pedido",command=cerrar,bg="red")
d3.grid(column=3,row=3)


ventana.mainloop()

