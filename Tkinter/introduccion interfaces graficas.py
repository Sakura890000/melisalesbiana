#tkinter

import tkinter as tk #alias de tkinter
##siempre definir funciones antes de crear o llamar la ventana

def saludar():
    codigo = entrada_codigo.get()
    print(f"hola q ase {codigo}")  #imprimiendo msj usando variables intermedias
    
# if __name__ == "__main__":
#     saludar()

#ya no hace falta if name porque el punto de entrada sera una ventana

ventana = tk.Tk()  #ya cree el punto de entrada

ventana.title("primera ventana")

ventana.geometry("500x300")

ventana.rowconfigure(5) #defino cantidad d filas
ventana.columnconfigure(5)#defino cantidad de columnas

#mensaje =  tk.Label(ventana, text="esto es ventana")
#mensaje.pack()

#
#boton.pack()
entrada_codigo =tk.Entry(ventana)  
texto = tk.Label(ventana, text="codigo del estudiante: ").grid(row=0, column=0) #.grid para las columnas y filas
entrada_codigo = tk.Entry(ventana).grid(row=0, column=1) #
mensaje = tk.Label(ventana, text= "otra cosa").grid(row=1, column=4)
boton = tk.Button(ventana, text="presentarse", command=saludar).grid(row=3, column=3)


ventana.mainloop()  #SIN ESTO NO SE EJECUTA LA VENTANA
##SIEMPRE DEBE IR ULTIMO
