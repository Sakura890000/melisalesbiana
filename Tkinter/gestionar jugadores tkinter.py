##Haremos un sistema para gestionar jugadores
#un jugador tiene nombre, codigo y posicion, equipo

##crear jugadores

#borrar jugadores
#buscar jugadores

#generar un archivo plano con todos los jugadores
#
import tkinter as tk

jugadores = {}

#funciones
def agregar_jugadores():
    dic = {
        "nombre": entrada_nombre.get(),
        "posicion": entrada_equipo.get(),
        "equipo": entrada_equipo.get()
    }
    jugadores [entrada_codigo.get()] = dic
    print("jugador agregado")
    
def ver_jugadores ():
    for k, v in jugadores.items():
        print(k, "->", v)
        
##crear el formulario


ventana = tk.Tk()
ventana.title("gestor de jugdores")
ventana.geometry("700x500")
ventana.resizable(False, False)

marco_formulario = tk.LabelFrame(
    ventana, 
    text="datos del jugador",
)
marco_formulario.grid(row= 0, column= 0, padx= 10, pady= 10) 
##padx margen horizontal ##pady margen vertical
nombre_label = tk.Label(marco_formulario, text= "nombre").grid(row= 0, column= 0, padx= 5,   pady= 5)
codigo_label = tk.Label(marco_formulario, text= "codigo").grid(row= 1, column= 0, padx= 5,   pady= 5)
posicion_label = tk.Label(marco_formulario, text= "posicion").grid(row= 2, column= 0, padx= 5,   pady= 5)
equipo_label = tk.Label(marco_formulario, text= "equipo").grid(row= 3, column= 0, padx= 5,   pady= 5)

###entradas

entrada_nombre = tk.Entry(marco_formulario, width=40 )
entrada_nombre.grid(row= 0, column= 1, padx= 10)
entrada_codigo = tk.Entry(marco_formulario, width=40 )
entrada_codigo.grid(row= 1, column= 1, padx= 10)
entrada_posicion = tk.Entry(marco_formulario, width=40 )
entrada_posicion.grid(row= 2, column= 1,padx= 10)
entrada_equipo = tk.Entry(marco_formulario, width=40 )
entrada_equipo.grid(row= 3, column= 1, padx= 10)

###agregar los botones

marco_botones = tk.LabelFrame(
    ventana,
    text= "Acciones del sistema"
)
marco_botones.grid(row= 2, column= 1,padx= 10, pady= 10)

boton_register = tk.Button(marco_botones, text= "registrar un jugador")
boton_register.grid(row= 0, column= 0)

boton_visual = tk.Button(marco_botones, text= "ver jugadores", command= ver_jugadores)
boton_visual.grid(row= 0, column= 1)


ventana.mainloop()
