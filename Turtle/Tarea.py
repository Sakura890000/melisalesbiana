import turtle as tr
import random
import tkinter as tk

### crear la ventana
ventana = tr.Screen()
ventana.bgcolor("white")
ventana.setup(600,600)
ventana.tracer(0)

circulos = []

pausado = False

### lapiz para dibujar los circulos
tortuga = tr.Turtle()
tortuga.hideturtle()
tortuga.color("red")
tortuga.speed(0)

root = ventana.getcanvas().master

def pausar():
    global pausado
    pausado = True

def reanudar():
    global pausado
    pausado = False

def eliminar():
    circulos.clear()
    tortuga.clear()

boton_pausar = tk.Button(root, text="PAUSAR", command=pausar)
boton_pausar.pack(side=tk.LEFT)

boton_reanudar = tk.Button(root, text="REANUDAR", command=reanudar)
boton_reanudar.pack(side=tk.LEFT)

boton_eliminar = tk.Button(root, text="ELIMINAR", command=eliminar)
boton_eliminar.pack(side=tk.LEFT)

def guardar_circulo(x,y):
    circulo = {
        'x' : x,
        'y' : y,
        'dx': random.randint(-10,10),
        'dy': random.randint(-10,10),
        'radio': random.randint(7,12)
    }
    circulos.append(circulo)

#circulos
def dibujar_circulo(x,y,radio):
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.circle(radio)
    tortuga.end_fill()

def mover_circulos():
    tortuga.clear()

    for circulo in circulos:

        if not pausado:

            circulo["x"] += circulo["dx"]
            circulo["y"] += circulo["dy"]

            if circulo["x"] > 290 or circulo["x"] < -290:
                circulo["dx"] *= -1

            if circulo["y"] > 290 or circulo["y"] < -290:
                circulo["dy"] *= -1

        dibujar_circulo(circulo['x'], circulo['y'],circulo['radio'])
    
    ventana.update()

    ventana.ontimer(mover_circulos, 30)

ventana.onscreenclick(guardar_circulo)

mover_circulos()
tr.done()