import turtle
import random
import tkinter as tk

### ---------------- VENTANA ----------------

ventana = turtle.Screen()
ventana.title("Bolitas rebotando")
ventana.bgcolor("white")
ventana.setup(width=700, height=700)
ventana.tracer(0)

circulos = []
pausado = False

### obtener la ventana interna de tkinter
canvas = ventana.getcanvas()
root = canvas.master

### ---------------- TORTUGA ----------------

tortuga = turtle.Turtle()
tortuga.hideturtle()
tortuga.color("red")
tortuga.speed(0)

### ---------------- FUNCIONES ----------------

def guardar_circulo(x, y):

    ### evitar crear bolitas sobre los botones
    if y < -250:
        return

    circulo = {
        "x": x,
        "y": y,
        "dx": random.randint(-10, 10),
        "dy": random.randint(-10, 10),
        "radio": random.randint(7, 12)
    }

    circulos.append(circulo)


def dibujar_circulo(x, y, radio):

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

        ### mover solo si NO está pausado
        if not pausado:

            circulo["x"] += circulo["dx"]
            circulo["y"] += circulo["dy"]

            ### rebote horizontal
            if circulo["x"] > 330 or circulo["x"] < -330:
                circulo["dx"] *= -1

            ### rebote vertical
            if circulo["y"] > 330 or circulo["y"] < -230:
                circulo["dy"] *= -1

        dibujar_circulo(
            circulo["x"],
            circulo["y"],
            circulo["radio"]
        )

    ventana.update()

    ventana.ontimer(mover_circulos, 30)

### ---------------- BOTONES ----------------

def pausar():
    global pausado
    pausado = True


def reanudar():
    global pausado
    pausado = False


def eliminar_bolitas():
    circulos.clear()
    tortuga.clear()

### frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(side=tk.BOTTOM, pady=10)

### boton pausa
boton_pausa = tk.Button(
    frame_botones,
    text="Pausar",
    width=15,
    command=pausar
)

boton_pausa.pack(side=tk.LEFT, padx=10)

### boton reanudar
boton_reanudar = tk.Button(
    frame_botones,
    text="Reanudar",
    width=15,
    command=reanudar
)

boton_reanudar.pack(side=tk.LEFT, padx=10)

### boton eliminar
boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar bolitas",
    width=15,
    command=eliminar_bolitas
)

boton_eliminar.pack(side=tk.LEFT, padx=10)

### detectar clics
ventana.onscreenclick(guardar_circulo)

### iniciar animacion
mover_circulos()

### mantener abierto
turtle.done()