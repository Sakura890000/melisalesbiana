import turtle as tr
import random
"""
ventana=tr.Screen()

ventana.bgcolor("black")

lapiz=tr.Turtle()

lapiz.shape("turtle")

lapiz.color("blue")


for i in range(4):
    lapiz.forward(120)
    lapiz.left(90)

lapiz.penup()
lapiz.goto(-200,0)
lapiz.pendown()
lapiz.forward(120)
lapiz.left(120)
lapiz.forward(110)
lapiz.left(120)
lapiz.forward(110)

lapiz.penup()
lapiz.goto(-100,250)
lapiz.right(20)
lapiz.pendown()
for i in range(5):
    lapiz.forward(160)
    lapiz.left(144)

tr.done()
"""
ventana=tr.Screen()
ventana.bgcolor("white")
ventana.setup(600,600)#tamaño de la ventana

flecha=tr.Turtle()
def arriba():
    flecha.setheading(90)
    flecha.forward(10)

def abajo():
    flecha.setheading(270)
    flecha.forward(10)

def izquierda():
    flecha.setheading(180)
    flecha.forward(10)

def derecha():
    flecha.setheading(0)
    flecha.forward(10)

def levantar():
    flecha.penup()

def bajar():
    flecha.pendown()

def diag_sup_izq():
    flecha.setheading(45)
    flecha.forward(10)

def diag_sup_der():
    flecha.setheading(135)
    flecha.forward(10)

def diag_infe_izq():
    flecha.setheading(225)
    flecha.forward(10)

def diag_infe_der():
    flecha.setheading(315)
    flecha.forward(10)

ventana.onkeypress(diag_infe_izq, "w")
ventana.onkeypress(diag_infe_der, "s")
ventana.onkeypress(diag_sup_izq, "a")
ventana.onkeypress(diag_sup_der, "d")
ventana.onkeypress(levantar, "space")
ventana.onkeypress(bajar, "Return")
ventana.onkeypress(arriba, "Up")#haga la accion cuando se pulse la tecla
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

ventana.listen()#para que este pendiente
tr.done()
"""

circulos=[]
###tortuga para dibujar los circulos
tortuga=tr.Turtle()
tortuga.hideturtle()#oculto la tortuga
tortuga.color("red")
tortuga.speed(0)


def dibujar_circulo(x,y):
    circulo={
        'x' : x,
        'y' : y,
        'dx' :random.randint(-10,10),
        'dy' :random.randint(-10,10),
        'radio' : random.randint(7,12)
    }
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.pendown()
    tortuga.begin_fill()###colorear poligonos relleno
    tortuga.circle(8)
    tortuga.end_fill()###finalice la accion de colorear

ventana.onscreenclick(dibujar_circulo)###evento click en pantalla

ventana.listen()
tr.done()
"""