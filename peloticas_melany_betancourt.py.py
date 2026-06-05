import turtle
import random
import tkinter as tk

ventana = turtle.Screen()
ventana.title("peloticas")
ventana.bgcolor("white")  # Fondo blanco original
ventana.setup(width=700, height=500)
ventana.tracer(0)

circulos = []
pausado = False

canvas = ventana.getcanvas()
root = canvas.master


tortuga = turtle.Turtle()
tortuga.hideturtle()
tortuga.color("red")  # Bolitas rojas originales
tortuga.speed(0)


def guardar_circulo(x, y):
    ### Evitar crear bolitas sobre la zona de botones
    if y < -200:
        return

    circulo = {
        "x": x,
        "y": y,
        "dx": random.randint(-10,10),
        "dy": random.randint(-10,10),
        "radio": random.randint(7, 12)
    }

    circulos.append(circulo)


def dibujar_circulo(x, y,radio):
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()

    tortuga.begin_fill()
    tortuga.circle(radio)
    tortuga.end_fill()


def mover_circulos():
    global pausado

    tortuga.clear()

    for circulo in circulos:
        if not pausado:
            circulo["x"] += circulo["dx"]
            circulo["y"] += circulo["dy"]

            ### Rebote horizontal corregido (ancho 700 va de -350 a 350)
            limite_x = 350 - circulo["radio"]
            if circulo["x"] > limite_x or circulo["x"] < -limite_x:
                circulo["dx"] *= -1

            ### Rebote vertical corregido (alto 500 va de -250 a 250)
            limite_y_sup = 250 - circulo["radio"]
            limite_y_inf = -210 + circulo["radio"]  # Margen inferior para botones
            
            if circulo["y"] > limite_y_sup or circulo["y"] < limite_y_inf:
                circulo["dy"] *= -1

        dibujar_circulo(
            circulo["x"],
            circulo["y"],
            circulo["radio"]
        )

    ventana.update()
    ventana.ontimer(mover_circulos, 30)

def pausar():
    global pausado
    pausado = True


def reanudar():
    global pausado
    pausado = False


def eliminar():
    circulos.clear()
    tortuga.clear()
    ventana.update()


frame_botones = tk.Frame(root)
frame_botones.pack(side=tk.BOTTOM, pady=20)

boton_pausa = tk.Button(
    frame_botones,
    text="Pausar",
    width=30,
    bg="#E6A6F9",
    command=pausar
)
boton_pausa.pack(side=tk.LEFT, padx=10)

boton_reanudar = tk.Button(
    frame_botones,
    text="Reanudar",
    width=30,
    bg="#E6A6F9",
    command=reanudar
)
boton_reanudar.pack(side=tk.LEFT, padx=10)

boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar",
    width=30,
    bg="#E6A6F9",
    command=eliminar
)
boton_eliminar.pack(side=tk.LEFT, padx=10)

ventana.onscreenclick(guardar_circulo)

mover_circulos()

turtle.done()
