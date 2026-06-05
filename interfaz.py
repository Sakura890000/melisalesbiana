import tkinter as tk
import time

ventana=tk.Tk()

ventana.title("Mi primera interfaz")
ventana.geometry("600x600")#pone el tamaño que apaqrece la ventana
ventana.minsize(400, 200)#pone el tamaño minimo de la ventana
ventana.maxsize(700, 700)#tamaño maximo que puede tener la ventana
ventana.configure(bg="orchid1")

frame_1=tk.Frame(ventana)
frame_1.configure(width=300, height=200, bg="blue", bd=5)
frame_2=tk.Frame(frame_1)
frame_2.configure(width=200, height=100, bg="red", bd=5)
frame_1.pack()
frame_2.pack()

etiqueta=tk.Label(frame_2, text="hola, soy un label" )
etiqueta.config(fg="white", bg="Black", font=("Arial", 30, "italic"))
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000, actualizar_hora)

actualizar_hora()

ventana.mainloop()
